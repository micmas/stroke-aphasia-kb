---
id: right_hemisphere_bg_lesions
name: right hemisphere basal ganglia lesions
kind: classical
findings:
- id: f1
  target: language_functions
  target_kind: impairment
  claim: In the acute phase, a majority of patients with right hemisphere basal ganglia
    lesions tested normal for language functions, while a minority presented with
    disturbances such as pure dysarthria, repetition impairment, or aphasia (e.g.,
    Broca's or transcortical sensory aphasia).
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 72
    population: Not transcribed; confirm from the original PDF population and timing
      passages.
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
  - Data derived from a systematic review of heterogeneous studies (including multiple
    case reports)
  - High heterogeneity in clinical descriptions and batteries used for diagnosis
  evidence_quality: meta-analysis
  strength: weak
  notes: 'Exposure measurement: Presence of a single focal vascular lesion in the
    right hemisphere basal ganglia (and/or adjacent internal capsule) without cortical
    or periventricular white matter involvement, documented by neuroimaging (CT, SPECT,
    PET, or MRI). 79.1% of the right hemisphere lesion group tested normal for language
    functions; 20.9% presented with disturbances; Disturbances included pure dysarthria
    (11.1%), repetition impairment (5.5% in putaminal lesions), and rare cases of
    Broca''s aphasia or transcortical sensory aphasia. Additional metadata has not
    been transcribed; review the pending-field flags before approval.'
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
    - not_transcribed:sample.population
    - not_transcribed:sample.time_post_onset
    - proposed_concept:language_functions
  citation: '@Radanovic2017'
  source_passages:
  - section: Original source P4-S2-C6
    page: 4
    quote: 'Right hemisphere lesions

      Acute phase – Out of the total 297 patients, 72 (24.2%) had right

      hemisphere lesions (RHL).'
    supports: sample
  - section: Original source P4-S2-C7
    page: 4
    quote: 'Of these 72, 57 (79.1%) tested normal for

      language functions.'
    supports: claim
  - section: Original source P4-S2-C8
    page: 4
    quote: 'Disturbances in speech or language were pre-

      sent in 15 (20.9%) patients, comprising 8 (11.1%) cases of pure dys-

      arthria (4 in putaminal lesions, 2 in capsular lesions and 2 in

      striatocapsular lesions).'
    supports: claim
  - section: Original source P4-S2-C9
    page: 4
    quote: 'Four (5.5%) patients with putaminal

      lesions had repetition impairment.'
    supports: claim
  - section: Original source P4-S2-C10
    page: 4
    quote: 'In 2 left-handed patients with

      striatocapsular lesion, 1 presented with Broca’s aphasia and the

      other had anomia, comprehension deﬁcit, paraphasia and dysar-

      thria.'
    supports: claim
  - section: Original source P4-S2-C11
    page: 4
    quote: 'One right-handed patient with lenticular lesion presented

      transcortical sensory aphasia.

      1–6 months after ictus – Follow-up information for this period

      was available in 6 cases: 2 patients with lesion in internal capsule

      were normal; in 3 patients with striatocapsular lesion, 2 had only

      dysarthria and 1 had anomia; 1 patient with a lenticulocapsular

      lesion was normal.'
    supports: claim
  - section: Original source P2-S4-C3
    page: 2
    quote: 'Patient selection

      Patients aged over 18 years of both sexes with a single (left or

      right hemisphere) vascular lesion in the basal ganglia and without

      PVWM or cortical involvement were included.'
    supports: method
  - section: Original source P4-S1-C6
    page: 4
    quote: 'Neuroimaging data

      Only articles featuring neuroimaging scans (cranial CT, SPECT,

      PET or magnetic resonance) were included.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Radanovic2017
  proposal_id: R009
  review_status_sha256: d60360ddc233f2c4980ae378e8913b3a71b877cd232ccb2815de7863332ca3b5
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 4e6241a4c4cc6cd8758e60a7f42e59618cbedebea80a52c43294ceec233c370f
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 4e6241a4c4cc6cd8758e60a7f42e59618cbedebea80a52c43294ceec233c370f
        A/passages.json: 54afcdff2b5877d32c97b4e98252fa6f4e404444851e6bb7578cf4f9badbab9d
        A/raw.json: a8585cc8ae62e82c6d196ad6c49ad1391a1eba9d9d560169511c42bb5a75bbbc
        A/source-units.json: a122cba338bcf3e1ec7be8212e61d4adf410517efdbd20a447a7e09f79c840be
        A/full-source-units.json: 5d0055312c556bcdaa767628083c4ee7f100783c3fb2cfbdd650d021bf58f01a
        A/meta.json: d5db568302ceef291affcd6536bb0aadfcd35079adea78ab7bc86359cd6a48ce
        A/table-images/TABLE-1-page-3-1.png: a67b90481e61fe1299ca108a4f042aa6fa84f10f767c9bd820df8536108ada18
        A/table-images/page-3.png: fce02db1e3ec004f34716b29479a24889c6c33fd1295b1b63c84aa152d3cba2c
        A/table-images/page-6.png: a30ea4093fc3940fe9f611a6e3e52c5db369c4b1a7009fdc9900fe1016588478
        A/table-images/page-7.png: 63691070b95e592055cdc06dfd5964b02b1601aa26e87240084ed29da73e42f9
        A/table-images/page-4.png: 53280f562106e531b5315c16f5066629db6b83e0220c60951cad7042d422a173
        A/table-images/TABLE-1-page-4-1.png: 4da661310627aba65921e51c0627e8fa76b856abf558eedbcfa45e13619dab06
        A/table-images/TABLE-6-page-8-1.png: 57a34e1c66fda3685266c313a7c372f18c363e090cef7fa8f90a0093fb89b01b
        A/table-images/page-8.png: 8b64020b9bcbd22cfccfafe83c7c96fb41c09f2b7ec4e3e3c7898ee037cb965a
        A/table-images/TABLE-3-page-6-2.png: 53b4e9b7e80ff35f43e25962f3f0c65d76cc840e241caa55f364837c501cbbc8
        A/table-images/TABLE-2-page-6-1.png: 21b44bfd287627fdfd0d1475a44617647ce6f30bfd3a0cd775d7e484c69311be
        A/table-images/manifest.json: 233598a32aecb9551f05b9f7abaf1b90d708051d45584dce5249fec060e44199
        A/table-images/TABLE-4-page-7-1.png: 2254669eff92a0dbab2cd8dc972dff3f95cc76e64c0173a785e16566061bd8f0
        A/table-images/TABLE-5-page-7-2.png: c188375e5b13cf5150e3ba3b6b3f4fdb14d7e63a19f1a8c286a530295b89df94
        A/clauses/window-10/raw.json: e5a6436cd7dc9100eaf6103520ab4e9e081f72c98fca65be58842aab3579faf2
        A/clauses/window-10/prompt.txt: bfa97235db4a2fce5fa034afc761e77771b7e19e928e2a1995255093c32ca285
        A/clauses/window-10/meta.json: 9c4bd242d62c8b63747bc9fd26c55152a65e34c6fe2a09aea43fecfd2a5e6905
        A/clauses/window-03/raw.json: b8f03dc97e0068a738fb905f1049b82dcb86950a81ad8d2dfb95c690b64b4eff
        A/clauses/window-03/prompt.txt: eca778399e080dc43a1f9094642961b3e4e96e886642dfbf240158184316b8ad
        A/clauses/window-03/meta.json: 186ac0e3b99f60d904a2a356e7edb72c3d6f4dba7f556cb6165a0ec91f5994aa
        A/clauses/window-04/raw.json: 7580375cbdd77b805f36948176b6116c1ac9f5fccd6be056ae34f196a249175e
        A/clauses/window-04/prompt.txt: cfb27033675c458c7304178ae04f6bc15d676c66bdba4cee6cb066d90cd0fb0b
        A/clauses/window-04/meta.json: dd7b075bb621d0454936deaeb7bbd777f7cb5bbbefa8cc49dfa8356f62abaaf9
        A/clauses/window-05/raw.json: a03e11ce69d2edfcc84bde56d5af5b12a1331cd4a23f4b47f0c4405aab02e53b
        A/clauses/window-05/prompt.txt: ae6d4dd655c8159423a4e936e3a10c0161aa4b8908e5ff0bf49c3b83568dc73a
        A/clauses/window-05/meta.json: b7f8c7c73c1363b6c24fb3844125d43bf467e321d0a0238fe299da9d43c4bc6f
        A/clauses/window-02/raw.json: f32ed82287d462b408130b6789e21c489d359a9f497d8dfe92846b017113e14f
        A/clauses/window-02/prompt.txt: c42ade2b292c5f42a019dc05a7706385b13c8c92bfee890e38095133dd379ee0
        A/clauses/window-02/meta.json: 1839d98c5d001431e3e09e098c2e9aaaad4de5b2a0a51a57dd6611fdde35fe93
        A/clauses/window-09/raw.json: 16fe2174de01f15779829ad4dd6ef831570c3fc4a9536e61f1348d62dc355142
        A/clauses/window-09/prompt.txt: 807bb0c7e1c1ead44d6289b6da587242b94f8b16132ff4c8147d4c5121e00de5
        A/clauses/window-09/meta.json: 901cedc86293ef8cdb8775d59369669a434e73ffda2b8fdeb390193b30a3d671
        A/clauses/window-07/raw.json: efb38f52a8b43a901da3127c4b2056afa27a1a5e0be05c02ead506dee6a6cbab
        A/clauses/window-07/prompt.txt: 13f640ca8a1d0e6e731c56d74fd27127e6b670304545a908da5ff3017e6a3fbc
        A/clauses/window-07/meta.json: b0ba4486f04343f6713ecb55e5c0885410b0a9a214cfb761e1e33f8a8a4d01c4
        A/clauses/window-01/raw.json: 6a620f3dd62e4b1fda39c0511a050c8895d550b42b956a85aac6cd664d2e7541
        A/clauses/window-01/prompt.txt: d439736c477a8e1b9ef7d986a61af2f1661e9436e87668fa277b4ed70866f24d
        A/clauses/window-01/meta.json: 67c83b4d57322dc4cc49a430b74cae57319599f4c341c835cca4a38e7d524c46
        A/clauses/window-06/raw.json: 3fdc2074c6969caa4387298b11d6623b9081425fec6f3e9202d33bd65e6a7cf3
        A/clauses/window-06/prompt.txt: 088d73391bb0d3548ce24a9e58bae2d23e44cb8130d3ae857687ef7fba9017ae
        A/clauses/window-06/meta.json: 510af3c89efaa6aba3b3e9417898347edd511c91f1d97af8e3b553349a0f4e52
        A/clauses/window-08/raw.json: 1efda44b9adc845fd83096528860a5c18e13e1493eadefd345942df5146cb3f3
        A/clauses/window-08/prompt.txt: ac939a64830f1c9c0832aca447cc1f12a90f03fc3e2c07875c7ae79ab83d090f
        A/clauses/window-08/meta.json: edfbaa08e4214fae6b92e895a62b0da19eb11b93f294c6ac29fb91ba249ee42e
        A/tables/TABLE-6-page-8-7/raw.json: 82196041ad8cdb62fb042fd1a203a88c98e7c7514f38d3a4293848cd6dd7110f
        A/tables/TABLE-6-page-8-7/prompt.txt: 775ba16dd8b992269ace80d57a5caa2c496e0b992d19c3e9b9b67fabce84fcf4
        A/tables/TABLE-6-page-8-7/meta.json: 98612b4bd9be2b4b3e6f553953211e002bc667843b1fd6da1ab88858bc14174b
        A/tables/TABLE-1-page-4-2/raw.json: 1b786aef3434bc57b54a2990f5ab48d8fd3855291266aec4b76b1933a253de81
        A/tables/TABLE-1-page-4-2/prompt.txt: d8746eeb1232d996a6c49a2c784a102620dd1537f436a8b788ab209d7dafecd7
        A/tables/TABLE-1-page-4-2/meta.json: e704848f45d23c5c3bd588a7596a02af1558e9e3efd61de842f6bc22ea5f1f81
        A/tables/TABLE-5-page-7-6/raw.json: c102bb3a6bfbc8699bb804145765930d12247f097c87e221d183d7bd6cb5b3b1
        A/tables/TABLE-5-page-7-6/prompt.txt: 26be5e431f3f2efc77e99a098dafb1a525a24458eb9398ad03c0865ac9430baa
        A/tables/TABLE-5-page-7-6/meta.json: 05323386da3ee7be30142fa719c2c477bc5ff8e2160c0c0ac8838016491b0ba3
        A/tables/TABLE-3-page-6-4/raw.json: 125e2d58be12b14068e8cd59fe43db206f0a0395a441e23c4de12cb6ae55c756
        A/tables/TABLE-3-page-6-4/prompt.txt: 75796de308dd819705f633a47376a979c8d24667de516e7a732580e24ae76791
        A/tables/TABLE-3-page-6-4/meta.json: 0f108cf62332497d1dc8b5a79a65a124a45f0317eed77e734810c2c48f756def
        A/tables/TABLE-2-page-6-3/raw.json: 85ba0244d2bf8a46689d834b749a2a4dcb5a4d2e7255c2c529b3c75a93afacf1
        A/tables/TABLE-2-page-6-3/prompt.txt: 87178171b575354bf1d45c7f79f2a7e86c858712d446209274e6044feb7c642d
        A/tables/TABLE-2-page-6-3/meta.json: 23a71f09c79d24295a787aaaa8f4c5cc72f2f307d1f1a59605defefcb9d3628a
        A/tables/TABLE-1-page-3-1/raw.json: 07d47ec1c0b54d64c0c61505dfc543ded623c239fc4b2ce10afb646b6855d6f4
        A/tables/TABLE-1-page-3-1/prompt.txt: 266dd0c146e458881e402f2e2cabd2bd47eba71c65247921050e0d784dbc9b2e
        A/tables/TABLE-1-page-3-1/meta.json: 6db8375f68189cf211f7ccb899c5e8110da6272372b2b72d095559fa84240481
        A/tables/TABLE-4-page-7-5/raw.json: 05888ed476c84ab87ae8206d66271270e12b800acc5e6e70f020a0b4fdc005b8
        A/tables/TABLE-4-page-7-5/prompt.txt: 8f30eef72078074937324d376ecd51f9ff8cd1e43272a50dfddebdeeb1d9d198
        A/tables/TABLE-4-page-7-5/meta.json: 81fb7aabdc27e75c43f6df74da70ae2f92b71263ca051595de26475efbe0d241
        B/passages.json: 54afcdff2b5877d32c97b4e98252fa6f4e404444851e6bb7578cf4f9badbab9d
        B/raw.json: 5dea32211bef60b630d7dc7d65d300c64cea1e3728391d96eb61f06a395a4ca8
        B/source-units.json: a122cba338bcf3e1ec7be8212e61d4adf410517efdbd20a447a7e09f79c840be
        B/full-source-units.json: 5d0055312c556bcdaa767628083c4ee7f100783c3fb2cfbdd650d021bf58f01a
        B/meta.json: ba44b8e82b8df3871193ebd5408ed8959636df4ba9628277bcd97e7bea9aa8f0
        B/table-images/TABLE-1-page-3-1.png: a67b90481e61fe1299ca108a4f042aa6fa84f10f767c9bd820df8536108ada18
        B/table-images/page-3.png: fce02db1e3ec004f34716b29479a24889c6c33fd1295b1b63c84aa152d3cba2c
        B/table-images/page-6.png: a30ea4093fc3940fe9f611a6e3e52c5db369c4b1a7009fdc9900fe1016588478
        B/table-images/page-7.png: 63691070b95e592055cdc06dfd5964b02b1601aa26e87240084ed29da73e42f9
        B/table-images/page-4.png: 53280f562106e531b5315c16f5066629db6b83e0220c60951cad7042d422a173
        B/table-images/TABLE-1-page-4-1.png: 4da661310627aba65921e51c0627e8fa76b856abf558eedbcfa45e13619dab06
        B/table-images/TABLE-6-page-8-1.png: 57a34e1c66fda3685266c313a7c372f18c363e090cef7fa8f90a0093fb89b01b
        B/table-images/page-8.png: 8b64020b9bcbd22cfccfafe83c7c96fb41c09f2b7ec4e3e3c7898ee037cb965a
        B/table-images/TABLE-3-page-6-2.png: 53b4e9b7e80ff35f43e25962f3f0c65d76cc840e241caa55f364837c501cbbc8
        B/table-images/TABLE-2-page-6-1.png: 21b44bfd287627fdfd0d1475a44617647ce6f30bfd3a0cd775d7e484c69311be
        B/table-images/manifest.json: d7c1ba2b0d366efe8cd8c53acef5a76ed8d17735cb101e8d683501a9146780f0
        B/table-images/TABLE-4-page-7-1.png: 2254669eff92a0dbab2cd8dc972dff3f95cc76e64c0173a785e16566061bd8f0
        B/table-images/TABLE-5-page-7-2.png: c188375e5b13cf5150e3ba3b6b3f4fdb14d7e63a19f1a8c286a530295b89df94
        B/clauses/window-10/raw.json: 2b906f04c81a43c5f4ca145d40c453bc79921947dd09b5decdb17aa8fcb4fa63
        B/clauses/window-10/prompt.txt: bfa97235db4a2fce5fa034afc761e77771b7e19e928e2a1995255093c32ca285
        B/clauses/window-10/meta.json: 8b65b60cef1e585ceb56362d400b35af2041ecb0665a10e63cf82132b468993a
        B/clauses/window-03/raw.json: 09e2029267646460048d6e4a65f3af3eb669929ff584f04e1910f6ea320a9e6d
        B/clauses/window-03/prompt.txt: eca778399e080dc43a1f9094642961b3e4e96e886642dfbf240158184316b8ad
        B/clauses/window-03/meta.json: a6241fbe5b2a9cc884d6f5dea38bc0425a9643e23d215d91807c1ff967f6cf94
        B/clauses/window-04/raw.json: 32e298a7956400e11b566a8028fecf3fe8ce1757b9eb52f37c64155136910314
        B/clauses/window-04/prompt.txt: cfb27033675c458c7304178ae04f6bc15d676c66bdba4cee6cb066d90cd0fb0b
        B/clauses/window-04/meta.json: 90e96b1b25a880320a953e2eab76bde985fdf1b65c2c3436d3f5cfee9774ece5
        B/clauses/window-05/raw.json: 90aac4bb3f2e7a9d740daa5ebe77569873320a370823886714110eb5f74e9c57
        B/clauses/window-05/prompt.txt: ae6d4dd655c8159423a4e936e3a10c0161aa4b8908e5ff0bf49c3b83568dc73a
        B/clauses/window-05/meta.json: 8a314d4a45b11828b1e93b3cc32e49e2c1c31190a9f8111eabeb0b029db501da
        B/clauses/window-02/raw.json: 41c72c32a0e85383973e00bf49ba720e3463d6439d621eb703b484dee0684c9d
        B/clauses/window-02/prompt.txt: c42ade2b292c5f42a019dc05a7706385b13c8c92bfee890e38095133dd379ee0
        B/clauses/window-02/meta.json: 07395135dae9cb09a5fca1de5f0c6db572af1d95f147cd490a6398e566e976fc
        B/clauses/window-09/raw.json: 2817e4675cc5320fcb4da5d52b8792eb977ea910c2533e8e4aa63b862b92fa9b
        B/clauses/window-09/prompt.txt: 807bb0c7e1c1ead44d6289b6da587242b94f8b16132ff4c8147d4c5121e00de5
        B/clauses/window-09/meta.json: 0d2bcdd42264b0814a4d3aabfe9831f6b280696069e5fbaa6a72651a4126f44e
        B/clauses/window-07/raw.json: 6697c07d995d608a5c58d52be0d20f3c0933cc45320067a826b6e829a194d581
        B/clauses/window-07/prompt.txt: 13f640ca8a1d0e6e731c56d74fd27127e6b670304545a908da5ff3017e6a3fbc
        B/clauses/window-07/meta.json: c883827ed1efbb327fa14d9b3090873c9406974644067a19ef8d32518bce8044
        B/clauses/window-01/raw.json: 500eac8adb68b285984d44c31e04f59a90cac73a465ff0499da4d6bb7877cf2b
        B/clauses/window-01/prompt.txt: d439736c477a8e1b9ef7d986a61af2f1661e9436e87668fa277b4ed70866f24d
        B/clauses/window-01/meta.json: e544c4871042e5ec73431c4c4282fa6f5f962c226a77f98151db9dcc8e509658
        B/clauses/window-06/raw.json: 7ea0d83b809a780105b9c70215f504414dee64d32a160b84dafab12c9f95ddd7
        B/clauses/window-06/prompt.txt: 088d73391bb0d3548ce24a9e58bae2d23e44cb8130d3ae857687ef7fba9017ae
        B/clauses/window-06/meta.json: afe5cbb4a0b6d3a2a8573112451ecb527bb9b8a7e39852bb1d2bdbd737f2ddfd
        B/clauses/window-08/raw.json: 10715b5eebe14096c1dda368897b38b7ee87eed3f7daaaa583981a31e1b3cdbd
        B/clauses/window-08/prompt.txt: ac939a64830f1c9c0832aca447cc1f12a90f03fc3e2c07875c7ae79ab83d090f
        B/clauses/window-08/meta.json: a6c2da8a6f1d5d4786ebad8b5ad5c0584ef33c6e345c931db36af99f67552277
        B/tables/TABLE-6-page-8-7/raw.json: 608f8e4cc2792a50789566c131706b61b18a9a4210256658fa1e3d07e6e651bd
        B/tables/TABLE-6-page-8-7/prompt.txt: 775ba16dd8b992269ace80d57a5caa2c496e0b992d19c3e9b9b67fabce84fcf4
        B/tables/TABLE-6-page-8-7/meta.json: 5bda62698f04de8cf314e1195f331017196fb1ed7901c2f00e5f14d9e8d8e590
        B/tables/TABLE-1-page-4-2/raw.json: f35064174bcf6309d2c01888f39b8ffa195b184dea0a31cb29b1215331b1d6b6
        B/tables/TABLE-1-page-4-2/prompt.txt: d8746eeb1232d996a6c49a2c784a102620dd1537f436a8b788ab209d7dafecd7
        B/tables/TABLE-1-page-4-2/meta.json: 743c105fc3f9202112406e53259d2a9476443ca5f069ad89bde9330c7d7f1661
        B/tables/TABLE-5-page-7-6/raw.json: c102bb3a6bfbc8699bb804145765930d12247f097c87e221d183d7bd6cb5b3b1
        B/tables/TABLE-5-page-7-6/prompt.txt: 26be5e431f3f2efc77e99a098dafb1a525a24458eb9398ad03c0865ac9430baa
        B/tables/TABLE-5-page-7-6/meta.json: 020b7f9984d4ac92a58e785483136aed3e71dc1e212fb597e6a63139bab5f716
        B/tables/TABLE-3-page-6-4/raw.json: 31638f1907024afb2adb24709d6b0e4bea91e8d3699597ea450c8d60233652e6
        B/tables/TABLE-3-page-6-4/prompt.txt: 75796de308dd819705f633a47376a979c8d24667de516e7a732580e24ae76791
        B/tables/TABLE-3-page-6-4/meta.json: 396b5bc44c2d2f59fdeafdf58c895a8e4d125bd5cb367cbe50b47fbf865a7ef8
        B/tables/TABLE-2-page-6-3/raw.json: 295aa5358012e5e8e62b04fe07fcc397a1746877fb2a0428f38892318b1eafa6
        B/tables/TABLE-2-page-6-3/prompt.txt: 87178171b575354bf1d45c7f79f2a7e86c858712d446209274e6044feb7c642d
        B/tables/TABLE-2-page-6-3/meta.json: c1bfac0a00e4e38becbf836e0fa469fccaa902100ebbb359572baa36d6dc65d3
        B/tables/TABLE-1-page-3-1/raw.json: 361b8a3aa2b1893c6aa76270469b8acdae0889d6c5637ee703caef2aacb1cfc0
        B/tables/TABLE-1-page-3-1/prompt.txt: 266dd0c146e458881e402f2e2cabd2bd47eba71c65247921050e0d784dbc9b2e
        B/tables/TABLE-1-page-3-1/meta.json: 98a1df0c0f0499f2d7ec86528cca34cb63f7baf97395e3ff7c1f69a62a628223
        B/tables/TABLE-4-page-7-5/raw.json: 6e23759528facda41e09c306f5e569419a65311a913c8ee71e8d59a1a9e33794
        B/tables/TABLE-4-page-7-5/prompt.txt: 8f30eef72078074937324d376ecd51f9ff8cd1e43272a50dfddebdeeb1d9d198
        B/tables/TABLE-4-page-7-5/meta.json: b457fdd4a10cb217cd6c90b1ea2211008613f5873453944c9a8bd6a5bf198979
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
      pdf_sha256: 4e6241a4c4cc6cd8758e60a7f42e59618cbedebea80a52c43294ceec233c370f
      source_review: _compare/relationships-2026-11-16/review-current/Radanovic2017
      source_status_sha256: 575e30d3883950959d7d9e8379cd56df8448d0b55ebda448d28b4a8701a588ab
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R009
    exposure:
      text: right hemisphere lesions
    outcome:
      text: language functions (normality vs disturbances)
    analysis_label: Right hemisphere acute phase analysis
    relation: association
    evidence_ids:
    - P4-S2-C7
    - P4-S2-C8
    qualifier_ids:
    - P4-S2-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 4e6241a4c4cc6cd8758e60a7f42e59618cbedebea80a52c43294ceec233c370f
      source_review: _compare/relationships-2026-11-16/review-current/Radanovic2017
      source_status_sha256: 575e30d3883950959d7d9e8379cd56df8448d0b55ebda448d28b4a8701a588ab
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P4-S2-C3
      - Result passage disposed without unit P4-S2-C4
      - Result passage disposed without unit P4-S2-C6
      - Result passage disposed without unit P4-S2-C15
      - Result passage disposed without unit P5-S1-C1
      - Result passage disposed without unit P9-S3-C11
      - Result passage disposed without unit P9-S4-C3
      - Result passage disposed without unit P9-S4-C4
      - Accounting without a linked unit P9-S4-C7
      - Result passage disposed without unit P9-S4-C8
      - Result passage disposed without unit P9-S5-C2
      - Unaccounted source passage P9-S4-C7
      - Result passage disposed without unit P10-S1-C1
      - Result passage disposed without unit P10-S1-C5
      - Result passage disposed without unit P10-S1-C13
      - Result passage disposed without unit P10-S1-C14
      - Accounting without a linked unit P10-S3-C4
      - Accounting without a linked unit P10-S3-C5
      - Accounting without a linked unit P10-S3-C9
      - Unaccounted source passage P10-S3-C9
      - Unaccounted source passage P10-S3-C4
      - Unaccounted source passage P10-S3-C5
      - 'window 13: invalid/duplicate disposition P10-S4-C3'
      - Accounting without a linked unit P11-S1-C2
      - Unaccounted source passage P11-S1-C2
      - Result passage disposed without unit P11-S2-C7
      unattached_null_or_qualifier_ids:
      - P9-S4-C3
      - P9-S4-C7
      - P9-S4-C8
      - P9-S4-C9
      - P10-S3-C9
      - P10-S3-C11
      suppressed_nonrepresented_units: 27
      default_disposition_count_requires_completeness_check: 188
      unselected_timing_passages:
      - P1-S1-C4
      - P2-S3-C3
      - P2-S4-C3
      - P2-S4-C4
      - P2-S4-C7
      - P4-S1-C9
      - P4-S2-C5
      - P5-S1-C2
      - P10-S4-C3
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P12-S1-C1
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: outcome_timing
        source_ids:
        - P2-S4-C7
        - P4-S1-C9
        - P4-S2-C11
        - P4-S2-C12
        - P5-S1-C2
        - P5-S1-C3
        - P5-S1-C8
        - P7-S2-C4
        - P7-S3-C2
        - P7-S3-C3
        - P9-S2-C11
        - P9-S3-C3
        - P10-S1-C5
        - P10-S1-C11
        - P10-S1-C12
        - P10-S1-C13
        - P10-S2-C5
        - P10-S2-C6
        - P10-S2-C9
        - P11-S1-C1
        - P11-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P4-S1-C3
        - P4-S1-C4
        - P4-S2-C9
        - P5-S1-C3
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C6
        - P5-S1-C7
        - P5-S1-C8
        - P8-S3-C5
        - P9-S3-C4
        - P9-S3-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
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
      - TABLE-1-page-4-2
      - TABLE-2-page-6-3
      - TABLE-3-page-6-4
      - TABLE-4-page-7-5
      - TABLE-5-page-7-6
      - TABLE-6-page-8-7
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-1-page-4-2
      - TABLE-3-page-6-4
      - TABLE-4-page-7-5
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S3
        - P2-S4
        - P5-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 4e6241a4c4cc6cd8758e60a7f42e59618cbedebea80a52c43294ceec233c370f
      source_review: _compare/relationships-2026-11-16/review-current/Radanovic2017
      source_status_sha256: 575e30d3883950959d7d9e8379cd56df8448d0b55ebda448d28b4a8701a588ab
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes: []
      reason: General summary of heterogeneity and weak correlations.
    - source_id: P1-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General hypothesis about hypoperfusion.
    - source_id: P2-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Search result counts.
    - source_id: P2-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Search result counts.
    - source_id: P2-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Selection process count.
    - source_id: P2-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Final inclusion count.
    - source_id: P2-S4-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient exclusion count.
    - source_id: P4-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Publication date range.
    - source_id: P4-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Patient count per study.
    - source_id: P4-S2-C6
      disposition: represented
      result_indexes:
      - 8
      reason: Defines the RHL sub-sample.
    - source_id: P4-S2-C7
      disposition: represented
      result_indexes:
      - 8
      reason: Reports normality rate in RHL.
    - source_id: P4-S2-C8
      disposition: represented
      result_indexes:
      - 8
      reason: Reports disturbance rate and dysarthria in RHL.
    - source_id: P4-S2-C9
      disposition: represented
      result_indexes:
      - 9
      reason: Reports repetition impairment in right putaminal lesions.
    - source_id: P4-S2-C10
      disposition: represented
      result_indexes: []
      reason: Case reports of left-handed patients with RHL.
    - source_id: P4-S2-C11
      disposition: represented
      result_indexes: []
      reason: Case report of right-handed patient with RHL.
    - source_id: P4-S2-C12
      disposition: represented
      result_indexes: []
      reason: Follow-up results for RHL.
    - source_id: P4-S2-C13
      disposition: represented
      result_indexes: []
      reason: Follow-up results for RHL.
    - source_id: P4-S2-C14
      disposition: represented
      result_indexes: []
      reason: Follow-up results for RHL.
    - source_id: P4-S2-C15
      disposition: represented
      result_indexes:
      - 11
      reason: Defines the LHL acute sub-sample.
    - source_id: P4-S2-C16
      disposition: represented
      result_indexes: []
      reason: LHL acute phase data.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 11
      reason: Reports normality rate in LHL acute stage.
    - source_id: P5-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 3.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Association of lentiform nucleus with repetition, comprehension, non-fluency,
        and normality.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Association of putaminal lesions with paraphasia and striatal lesions
        with dysarthria.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Association of caudate and capsular lesions with non-fluent aphasia.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 4
      reason: Association of caudate lesions with repetition impairment.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 5
      reason: Null association for globus pallidus and striatum.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Chronic stage association for putamen (dysarthria) and internal capsule
        (normality).
    - source_id: P9-S1-C7
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of RHL results.
    - source_id: P9-S2-C7
      disposition: repeated
      result_indexes:
      - 11
      reason: Restatement of LHL acute normality rate.
    - source_id: P9-S2-C8
      disposition: represented
      result_indexes: []
      reason: LHL acute symptom frequencies.
    - source_id: P9-S2-C9
      disposition: represented
      result_indexes: []
      reason: LHL acute anomia frequency.
    - source_id: P9-S2-C10
      disposition: represented
      result_indexes: []
      reason: LHL acute paraphasia and dysarthria frequency.
    - source_id: P9-S2-C11
      disposition: represented
      result_indexes: []
      reason: LHL 1-6 month symptom frequencies.
    - source_id: P9-S2-C12
      disposition: represented
      result_indexes: []
      reason: LHL 1-6 month dysarthria frequency.
    - source_id: P9-S2-C13
      disposition: represented
      result_indexes: []
      reason: LHL >6 month symptom frequencies.
    - source_id: P9-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of anomia frequency.
    - source_id: P9-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of LHL >6 month symptoms.
    - source_id: P9-S3-C4
      disposition: represented
      result_indexes: []
      reason: Lentiform nucleus association with non-fluency, comprehension, and repetition.
    - source_id: P9-S3-C5
      disposition: represented
      result_indexes: []
      reason: Lentiform nucleus association with absence of disturbances.
    - source_id: P9-S3-C6
      disposition: represented
      result_indexes: []
      reason: Lentiform nucleus acute aphasia rate.
    - source_id: P9-S3-C7
      disposition: represented
      result_indexes: []
      reason: Lentiform nucleus follow-up persistence.
    - source_id: P9-S3-C8
      disposition: represented
      result_indexes: []
      reason: Lentiform nucleus MCA occlusion cases.
    - source_id: P9-S3-C9
      disposition: represented
      result_indexes: []
      reason: Case of residual apraxia of speech.
    - source_id: P9-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Author's interpretation of a case.
    - source_id: P9-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lack of follow-up data.
    - source_id: P9-S3-C12
      disposition: represented
      result_indexes:
      - 12
      reason: Citing SPECT studies on cortical hypoperfusion.
    - source_id: P9-S3-C13
      disposition: represented
      result_indexes: []
      reason: Hypometabolism in lentiform/capsule lesions.
    - source_id: P9-S3-C14
      disposition: represented
      result_indexes: []
      reason: Anomia persistence in non-fluent aphasia.
    - source_id: P9-S4-C3
      disposition: represented
      result_indexes: []
      reason: Striatal/striatocapsular acute normality rate.
    - source_id: P9-S4-C4
      disposition: represented
      result_indexes: []
      reason: Striatal/striatocapsular acute symptom frequencies.
    - source_id: P9-S4-C5
      disposition: represented
      result_indexes: []
      reason: Striatopallidal acute symptoms.
    - source_id: P9-S4-C6
      disposition: represented
      result_indexes: []
      reason: Case reports of striatal/striatocapsular lesions.
    - source_id: P9-S4-C7
      disposition: represented
      result_indexes:
      - 2
      reason: Consistent association between striatal lesions and dysarthria.
    - source_id: P9-S4-C8
      disposition: represented
      result_indexes: []
      reason: Symptomatic patients after acute stage.
    - source_id: P9-S4-C9
      disposition: represented
      result_indexes: []
      reason: Symptom types in chronic striatal lesions.
    - source_id: P9-S5-C2
      disposition: represented
      result_indexes: []
      reason: Chronic striatal comprehension deficit rate.
    - source_id: P10-S1-C1
      disposition: represented
      result_indexes: []
      reason: Chronic striatal comprehension deficit count.
    - source_id: P10-S1-C2
      disposition: represented
      result_indexes: []
      reason: Chronic striatal repetition deficit rate.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes: []
      reason: Chronic striatal anomia rate.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes: []
      reason: Chronic striatal paraphasia count.
    - source_id: P10-S1-C5
      disposition: represented
      result_indexes: []
      reason: Hypoperfusion hypothesis for persistent disturbances.
    - source_id: P10-S1-C11
      disposition: represented
      result_indexes: []
      reason: Caudate nucleus association with non-fluent aphasia and repetition.
    - source_id: P10-S1-C12
      disposition: represented
      result_indexes: []
      reason: Caudate acute normality rate.
    - source_id: P10-S1-C13
      disposition: represented
      result_indexes: []
      reason: Caudate acute symptom frequencies.
    - source_id: P10-S1-C14
      disposition: represented
      result_indexes: []
      reason: Caudate acute paraphasia and stuttering.
    - source_id: P10-S2-C3
      disposition: represented
      result_indexes: []
      reason: Hemorrhagic stroke symptom severity.
    - source_id: P10-S2-C4
      disposition: represented
      result_indexes: []
      reason: Ischemic infarct outcomes in caudate lesions.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes: []
      reason: Caudate symptomatic rate at 1 month.
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes: []
      reason: Caudate 1-month symptom frequencies.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes: []
      reason: Caudate 1-month dysarthria case.
    - source_id: P10-S2-C8
      disposition: represented
      result_indexes: []
      reason: Caudate persistent aphasia and hypoperfusion.
    - source_id: P10-S2-C9
      disposition: represented
      result_indexes: []
      reason: Caudate hemorrhagic follow-up.
    - source_id: P10-S2-C10
      disposition: represented
      result_indexes: []
      reason: Caudate-frontal disconnection hypothesis.
    - source_id: P10-S3-C2
      disposition: represented
      result_indexes: []
      reason: Pallidal lesion sample size.
    - source_id: P10-S3-C3
      disposition: represented
      result_indexes: []
      reason: Pure pallidal lesion normality.
    - source_id: P10-S3-C4
      disposition: represented
      result_indexes: []
      reason: Pallidal + IC lesion symptoms.
    - source_id: P10-S3-C5
      disposition: represented
      result_indexes: []
      reason: TMA follow-up results.
    - source_id: P10-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Author's conclusion on loop interruption.
    - source_id: P10-S3-C7
      disposition: represented
      result_indexes: []
      reason: Thalamus-frontal disconnection case.
    - source_id: P10-S3-C8
      disposition: represented
      result_indexes: []
      reason: Internal capsule lesion sample size.
    - source_id: P10-S3-C9
      disposition: represented
      result_indexes: []
      reason: IC acute normality and dysarthria.
    - source_id: P10-S3-C10
      disposition: represented
      result_indexes: []
      reason: IC acute symptom frequencies.
    - source_id: P10-S3-C11
      disposition: represented
      result_indexes: []
      reason: IC chronic aphasia cases.
    - source_id: P10-S3-C12
      disposition: represented
      result_indexes: []
      reason: ICA occlusion and hypoperfusion case.
    - source_id: P10-S4-C2
      disposition: represented
      result_indexes: []
      reason: IC lesion evidence for cortical involvement.
    - source_id: P10-S4-C3
      disposition: represented
      result_indexes: []
      reason: Left putaminal acute sample size.
    - source_id: P10-S4-C4
      disposition: represented
      result_indexes: []
      reason: Putaminal acute normality and dysarthria.
    - source_id: P10-S4-C5
      disposition: represented
      result_indexes: []
      reason: Putaminal acute fluency rates.
    - source_id: P10-S4-C6
      disposition: represented
      result_indexes: []
      reason: Putaminal acute symptom frequencies.
    - source_id: P10-S4-C7
      disposition: represented
      result_indexes: []
      reason: Putaminal acute paraphasia and dysarthria.
    - source_id: P10-S4-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Association of putaminal lesions with paraphasias.
    - source_id: P10-S4-C9
      disposition: represented
      result_indexes: []
      reason: Putaminal acute hypoperfusion cases.
    - source_id: P10-S4-C10
      disposition: represented
      result_indexes: []
      reason: Putaminal disconnection hypothesis.
    - source_id: P10-S4-C11
      disposition: represented
      result_indexes: []
      reason: Putaminal hemorrhagic stroke cases.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes: []
      reason: Putaminal chronic symptom frequencies.
    - source_id: P11-S1-C3
      disposition: represented
      result_indexes: []
      reason: Putaminal chronic hypoperfusion cases.
    - source_id: P11-S1-C4
      disposition: represented
      result_indexes: []
      reason: Putaminal chronic disconnection hypothesis.
    - source_id: P11-S1-C8
      disposition: represented
      result_indexes:
      - 12
      reason: Correlation of cortical hypoperfusion with language disturbances.
    - source_id: P11-S2-C7
      disposition: represented
      result_indexes: []
      reason: Language impairments in Parkinson's/Huntington's.
    unresolved_coverage:
    - source_id: P1-S1-C6
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P4-S2-C10
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P4-S2-C11
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P4-S2-C12
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P4-S2-C13
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P4-S2-C14
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P4-S2-C16
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S2-C8
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S2-C9
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S2-C10
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S2-C11
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S2-C12
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S2-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S3-C5
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S3-C6
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S3-C7
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S3-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S3-C14
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S4-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S4-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S4-C5
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S4-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P9-S4-C8
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S4-C9
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P9-S5-C2
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S1-C1
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S1-C2
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S1-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S1-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S1-C5
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S1-C11
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S1-C12
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S1-C13
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S1-C14
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S2-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S2-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S2-C5
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S2-C6
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S2-C9
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S2-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S3-C2
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S3-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S3-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S3-C5
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S3-C6
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S3-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S3-C8
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S3-C9
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S3-C10
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S3-C11
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S3-C12
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S4-C2
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S4-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S4-C4
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S4-C5
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S4-C6
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S4-C7
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S4-C9
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P10-S4-C10
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S4-C11
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P11-S1-C2
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P11-S1-C3
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P11-S1-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S1-C8
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P11-S2-C7
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    pending_source_ids:
    - P1-S1-C6
    - P1-S1-C7
    - P2-S2-C7
    - P2-S2-C9
    - P2-S3-C5
    - P2-S3-C9
    - P2-S4-C5
    - P4-S2-C3
    - P4-S2-C4
    - P4-S2-C6
    - P4-S2-C10
    - P4-S2-C11
    - P4-S2-C12
    - P4-S2-C13
    - P4-S2-C14
    - P4-S2-C15
    - P4-S2-C16
    - P5-S1-C2
    - P9-S1-C7
    - P9-S2-C7
    - P9-S2-C8
    - P9-S2-C9
    - P9-S2-C10
    - P9-S2-C11
    - P9-S2-C12
    - P9-S3-C1
    - P9-S3-C3
    - P9-S3-C4
    - P9-S3-C5
    - P9-S3-C6
    - P9-S3-C7
    - P9-S3-C11
    - P9-S4-C3
    - P9-S4-C4
    - P9-S4-C7
    - P9-S4-C8
    - P9-S4-C9
    - P9-S5-C2
    - P10-S1-C1
    - P10-S1-C2
    - P10-S1-C3
    - P10-S1-C4
    - P10-S1-C5
    - P10-S1-C11
    - P10-S1-C12
    - P10-S1-C13
    - P10-S1-C14
    - P10-S2-C3
    - P10-S2-C4
    - P10-S2-C5
    - P10-S2-C6
    - P10-S2-C9
    - P10-S3-C2
    - P10-S3-C3
    - P10-S3-C4
    - P10-S3-C5
    - P10-S3-C8
    - P10-S3-C9
    - P10-S3-C10
    - P10-S3-C11
    - P10-S4-C2
    - P10-S4-C3
    - P10-S4-C4
    - P10-S4-C5
    - P10-S4-C6
    - P10-S4-C7
    - P10-S4-C8
    - P10-S4-C9
    - P10-S4-C11
    - P11-S1-C2
    - P11-S1-C3
    - P11-S2-C7
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-1-page-4-2
    - TABLE-2-page-6-3
    - TABLE-3-page-6-4
    - TABLE-4-page-7-5
    - TABLE-5-page-7-6
    - TABLE-6-page-8-7
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C9
      - P4-S2-C5
      recruited_sample:
      - P2-S2-C7
      - P2-S3-C5
      - P2-S3-C9
      eligibility:
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C8
      - P2-S3-C10
      - P2-S4-C3
      - P2-S4-C8
      imaging_provenance:
      - P4-S1-C6
      - P4-S1-C7
      - P7-S1-C3
      - P7-S1-C4
      - P10-S1-C5
      - P10-S1-C9
      - P10-S4-C9
      - P11-S1-C3
      imaging_timing:
      - P4-S1-C7
      - P10-S1-C5
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P2-S3-C8
      - P2-S4-C11
      - P10-S1-C9
      dependent_variable_statement:
      - P4-S2-C1
      limitations:
      - P11-S3-C6
      - P12-S1-C1
      - P12-S1-C2
      - P12-S1-C3
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S4-C5
      - P4-S2-C5
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P12-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: outcome_timing
      source_ids:
      - P2-S4-C7
      - P4-S1-C9
      - P4-S2-C11
      - P4-S2-C12
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C8
      - P7-S2-C4
      - P7-S3-C2
      - P7-S3-C3
      - P9-S2-C11
      - P9-S3-C3
      - P10-S1-C5
      - P10-S1-C11
      - P10-S1-C12
      - P10-S1-C13
      - P10-S2-C5
      - P10-S2-C6
      - P10-S2-C9
      - P11-S1-C1
      - P11-S1-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P4-S1-C3
      - P4-S1-C4
      - P4-S2-C9
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C6
      - P5-S1-C7
      - P5-S1-C8
      - P8-S3-C5
      - P9-S3-C4
      - P9-S3-C5
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
      pdf_sha256: 4e6241a4c4cc6cd8758e60a7f42e59618cbedebea80a52c43294ceec233c370f
      review_sha256: d60360ddc233f2c4980ae378e8913b3a71b877cd232ccb2815de7863332ca3b5
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
      - P4-S2-C7
      - P4-S2-C8
      source_result: In the acute phase, 72 patients had right hemisphere lesions.
        57 (79.1%) tested normal for language functions. 15 (20.9%) presented with
        disturbances, including pure dysarthria (8 cases, 11.1%), repetition impairment
        (4 cases, 5.5%), and rare cases of aphasia (Broca's, transcortical sensory).
      result_status: qualitative_synthesis
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the descriptive frequency of
            language outcomes in the right hemisphere lesion subgroup during the acute
            phase, as detailed in P4-S2-C6 through P4-S2-C10. It is distinct from
            the Chi-square association analyses between lesion site and symptom type
            presented in P5-S1-C3.
          source_ids:
          - P4-S2-C6
          - P4-S2-C7
          - P4-S2-C8
          - P5-S1-C3
        direction:
          answer: fits
          reason: 'The claim accurately reflects the source data: a majority (79.1%)
            were normal, and a minority (20.9%) had disturbances. The specific types
            of disturbances (dysarthria, repetition, aphasia) match the source descriptions.'
          source_ids:
          - P4-S2-C7
          - P4-S2-C8
          - P4-S2-C9
          - P4-S2-C10
        construct:
          answer: fits
          reason: The exposure is correctly identified as right hemisphere basal ganglia
            lesions. The outcome is language function status (normal vs. disturbance).
            The patient measurement is non-imaging (clinical language assessment),
            as the review aggregates clinical data from various studies; neuroimaging
            was used for lesion localization, not as the primary outcome measure for
            language function itself.
          source_ids:
          - P2-S4-C3
          - P4-S1-C6
          - P4-S2-C6
        qualifications:
          answer: fits
          reason: The draft correctly includes the specific percentages and types
            of disturbances found in the source. It also notes the context of the
            systematic review and heterogeneity, which are material limitations mentioned
            in the source (P12-S1-C1, P12-S1-C2).
          source_ids:
          - P4-S2-C7
          - P4-S2-C8
          - P12-S1-C1
          - P12-S1-C2
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft acknowledges the heterogeneous
            nature of the data and the specific subgroup (right hemisphere, acute
            phase). The distinction between this descriptive frequency and the statistical
            association analyses (Table 6) is maintained by not claiming a statistical
            association for this specific descriptive finding.
          source_ids:
          - P4-S2-C6
          - P12-S1-C2
      optional_pending:
      - 'sample.population: source confirmation required; original proposed wording
        remains in the audit.'
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - 'sample.population: source confirmation required; original proposed wording
      remains in the audit.'
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.population
      original: Adults (aged 21-94 years) with a single focal vascular lesion of the
        right hemisphere basal ganglia.
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 21, 94'
    - field: sample.time_post_onset
      original: Acute phase (up to 30 days following the ictus).
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 3E+1'
    analysis_identity:
      id: R009
      exposure:
        text: right hemisphere lesions
      outcome:
        text: language functions (normality vs disturbances)
      analysis_label: Right hemisphere acute phase analysis
      relation: association
      evidence_ids:
      - P4-S2-C7
      - P4-S2-C8
      qualifier_ids:
      - P4-S2-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 4e6241a4c4cc6cd8758e60a7f42e59618cbedebea80a52c43294ceec233c370f
        source_review: _compare/relationships-2026-11-16/review-current/Radanovic2017
        source_status_sha256: 575e30d3883950959d7d9e8379cd56df8448d0b55ebda448d28b4a8701a588ab
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S4-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 4e6241a4c4cc6cd8758e60a7f42e59618cbedebea80a52c43294ceec233c370f
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: ebdc811cbb2628f040d417ce6f16293b05d9a696d209f27f2f9e950225216cd0
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S4-C3
          page: 2
          text_layer_sha256: ebdc811cbb2628f040d417ce6f16293b05d9a696d209f27f2f9e950225216cd0
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Patient selection

          Patients aged over 18 years of both sexes with a single (left or

          right hemisphere) vascular lesion in the basal ganglia and without

          PVWM or cortical involvement were included.'
        anchor_text: 'Patient selection

          Patients aged over 18 years of both sexes with a single (left or

          right hemisphere) vascular lesion in the basal ganglia and without

          PVWM or cortical involvement were included.'
        excluded_fragments: []
        image_sha256: eb34e9f24b6617504e75a9fce6178dd5eb0dde071166ee575f62c10604f06dae
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 4
  quote: 'Right hemisphere lesions

    Acute phase – Out of the total 297 patients, 72 (24.2%) had right

    hemisphere lesions (RHL).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
