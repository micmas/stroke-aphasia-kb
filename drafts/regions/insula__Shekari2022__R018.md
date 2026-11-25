---
id: insula
name: insula cluster
kind: network
findings:
- id: f1
  target: phonological_based_therapy
  target_kind: therapy
  claim: activation of the insula was revealed after phonological-based therapies
  direction: likely
  relationship: treatment_response
  method: fMRI_activation
  sample:
    n: not_reported
    population: individuals with acquired aphasia caused by CVA
    phase: not_reported
    time_post_onset: chronic phase of stroke
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - difficulty in dissociating effects of semantic and phonemic treatments as they
    are often used alternately
  - heterogeneity in study designs (single-subject vs group)
  evidence_quality: narrative-review
  strength: weak
  notes: 'Exposure measurement: activation of the insula measured via task-based fMRI
    during picture-naming. measured during picture-naming tasks; finding synthesized
    from a narrative review of 14 studies. Additional metadata has not been transcribed;
    review the pending-field flags before approval.'
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
    - proposed_concept:phonological_based_therapy
  therapy:
    id: phonological_based_therapy
    name: phonological-based therapy
  citation: '@Shekari2022'
  source_passages:
  - section: Original source P13-S2-C9
    page: 13
    quote: 'Insula

      The activation of this area was revealed after phonological-

      based therapies (Nardo et al., 2017; Vitali et al., 2007).'
    supports: claim
  - section: Original source P3-S1-C14
    page: 3
    quote: 'All participants of the reviewed studies were in the chronic

      phase of stroke.'
    supports: sample
  - section: Original source P3-S2-C11
    page: 3
    quote: 'The fMRI task of all reviewed studies was pic-

      ture naming.'
    supports: method
  - section: Original source P15-S3-C2
    page: 15
    quote: 'Most

      studies alternately used these two treatments, and therefore

      it is hardly challenging that dissociate the effects of these

      two treatments on brain function.'
    supports: limitation
  - section: Original source P1-S1-C2
    page: 1
    quote: 'This article aims to review studies investigating brain reorganization

      after semantic and phonological-based anomia therapy that used picture-naming
      fMRI tasks.'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Shekari2022
  proposal_id: R018
  review_status_sha256: ddcc5025518180128fcc9f580a9d484df35db26e268192e69650a6c10abf9ef3
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
        A/passages.json: d675bfa85b5876cf1886835b029326f1e98003f6cf875e1854500edfab315678
        A/raw.json: ce0ac3bc4a82a40b8a786a03659a1df3c38a7a55cc0246ad5789651f8b0cb7b8
        A/source-units.json: c3a5da11ecda62ea0a14ce213517fd7105b1100903c65c29a322b4efdec95840
        A/full-source-units.json: 21b392590594d4f43c53153851a41f93ce654c77b72d4322e6ea6639b8037b77
        A/meta.json: b5c8a88ff06291913cca9b168017373fb202cd462ec7b17e3b5c612094eab822
        A/table-images/TABLE-5-page-9-1.png: 67daafcc9c6b44c1ae28506d80eeb2612408201464f0d1fce44714f0c045ebd0
        A/table-images/TABLE-1-page-3-2.png: bcc57522ea6c16526a2bc5f584acecfddb2f793213dbb25602299eb7610f0f02
        A/table-images/page-3.png: 05ce4271bad89a2be4857977d25c2ddd88d34ab1b0e99e61635de1d6fbed912b
        A/table-images/page-6.png: dee64f1f56536a1c5b73459a73e6a427c00686dbad5c9beb08d770fee1b603ae
        A/table-images/TABLE-4-page-8-1.png: 076c692a261a1aa0fc359d03e48cc2ecc90db5ac79f7f9477cb1c81b82d4e738
        A/table-images/page-7.png: d2b0fc027bef1d4c561ad5ba526b4a3399bacca1c1f6ddb5a4562fa0cbe25ab6
        A/table-images/page-5.png: 505a2ad7f4905bf4fff1e4b5020663b863a485e8ac95de011335a9bb2dc04e9a
        A/table-images/page-4.png: c9c172cbc4e4a1b1089109858adb3f4c0725e6e0a1a5826a3ee26bb33b3a3fcd
        A/table-images/page-9.png: 0b769fabe432db79f27e1a025e732cc72d67a33d5b239ca82a5a0bde40a71dbf
        A/table-images/TABLE-3-page-6-1.png: 831d1dc3d767e4cd42a394f41923ead2d817b92c4aad6e0af671c764152d4c44
        A/table-images/page-8.png: 5fdec18b53c44285a5fc978d7522bba89c9c94284a23a4dea953a9605f8844f8
        A/table-images/manifest.json: 6d1f94403024d62d7fa920f6d49bbdb22ded28454daf6037ea84fbfa7a346b29
        A/table-images/TABLE-2-page-4-1.png: e0aa21098344e42768e03fd1cfb364de6dd67be327724eac9b012b14ef886be7
        A/table-images/TABLE-3-page-5-1.png: 4bcce4e86881bcdd0d65a9477d0c1ebdff7c4378424bff8286dc652d07dbb4ea
        A/table-images/TABLE-4-page-7-1.png: 6649fb48005b734775149d7a67ed34ff3888616aac4c02080500fb49911d29d9
        A/table-images/TABLE-3-page-3-1.png: 6f112c1cd31eba6bd8c541a42a3e3aaae4cda3bf47b7688c77ac6e37888cce4e
        A/clauses/window-03/raw.json: adc155ee043a6fd35dba82134de7d2778da1f9a2fa7ec47f319492b4653e9142
        A/clauses/window-03/prompt.txt: 758a2fdace3a7a0926823bc7769e7207623174f84136c1c9ad2516987cba6fcd
        A/clauses/window-03/meta.json: 0fc91d4915892855488ac2dbd6c69690d30c7125fc4e01cdfb1630031c9273f9
        A/clauses/window-04/raw.json: a592c334892cd835b17c11cc82d340be3ea60ef81265936a3b5c3347f407c5a7
        A/clauses/window-04/prompt.txt: f2435cb510b59892faf6a0af4fb4fc8d20946238649f9bf6635f5ad2c169b84e
        A/clauses/window-04/meta.json: b806bafd29c541059b6b4735ac49e46d51aa34404dcd2f0466e9abefecf09a6d
        A/clauses/window-05/raw.json: 2218587a600268080c6a798f08df530c324988daa68b8d83df2908e6c20e3851
        A/clauses/window-05/prompt.txt: e1fa2c4b50ba92a35f187b2abc80fec8f57840acf813a76e1b2abb08e35a2850
        A/clauses/window-05/meta.json: 2b1ce9bb22d1c4396d461beb312c8f4575c135922a59547f0fb752b71e9c7f6a
        A/clauses/window-02/raw.json: 83975b62630e3915b25d10c6a306943c4f993a74248bb0c71f31256a5c70ca4f
        A/clauses/window-02/prompt.txt: b1949171e219e33d9b384b5c6cb1a790e9cdfe188d5d5a308b7ccf58b396bd5b
        A/clauses/window-02/meta.json: 28836e3623967989ad10e3c9d088cfee186d736335e9758c046ba732bcb6e8b1
        A/clauses/window-09/raw.json: 8faca8ca4e01cba5e29cf4896edcfbdff88fa5a0e036efddf99f9c5132120f9a
        A/clauses/window-09/prompt.txt: 5c7e39391c4bee67089169116d055a864b2924ab7c4ca6e0e36474a6c6236dc1
        A/clauses/window-09/meta.json: f3982a16192bffb1a34a608492d6f52f933096b3e418ef90c351f56abdf2baf8
        A/clauses/window-07/raw.json: 8e3894247709dd9f2be84762ae758e87d5f4493ea25358192597d80758e63200
        A/clauses/window-07/prompt.txt: c144787ac67dc26d3bfb1c35c190254e221d9bf84ebf685febf80f5791e14441
        A/clauses/window-07/meta.json: 446f9c5814b72193d39b0697fb65637c0b6bcea482ec7beff6c7091c8067127e
        A/clauses/window-01/raw.json: 39b120ceb243379a0aa92eade25e23c5ee36aa7690b06ca5e5352b91e21f5333
        A/clauses/window-01/prompt.txt: ee240ae7c5f9a04895ed073dafbf901b4da2a7e7016a80f073503bed5ed3e596
        A/clauses/window-01/meta.json: 4193823694281b2d55b1a083e88da2c11701b2fdd107c8268ba213adf66d2118
        A/clauses/window-06/raw.json: 59ef4a751aa3f8451b3f9b23b9ed9c920fc708f69346bdcf16aac0d165a9afa6
        A/clauses/window-06/prompt.txt: 68c49c9047c81d75ff79137ac15cba11a49ca8aa02635a1522b8827a121ec32e
        A/clauses/window-06/meta.json: adb9b16879360328ba44e21c1a1127962e300204a78755294bd9663f42ebf343
        A/clauses/window-08/raw.json: 20c629d6961d2f0f683dc33ed445f58b76326b353f5d66e838d0cdfa605402c5
        A/clauses/window-08/prompt.txt: 495829182d5ae3f2a35b4a7ba33ae5de61fda35abba2c24902369c22adea2080
        A/clauses/window-08/meta.json: 7f9e86a63b8da09dd3d397fb1460a2cbfd8321b1e2e0b5e20585d43e902fb3f9
        A/tables/TABLE-1-page-3-2/raw.json: 400f1a793db1676d0f1c5039bd70eaa9bfc823b5cbe544fe7969adaeb6f2c035
        A/tables/TABLE-1-page-3-2/prompt.txt: 0a56c7406b8188d0827538c8c9008c344a078962e0a8bf0e18e8bac43bd24eb0
        A/tables/TABLE-1-page-3-2/meta.json: 1f8605445a7d86f02a6c32db067c6e8f759a605439d21bb6ddf3da460bb13b5f
        A/tables/TABLE-3-page-5-4/raw.json: 8a002e09a5da5580f0b5d2bb0dfd03225d43ee5a94309ed57ec74925700e1726
        A/tables/TABLE-3-page-5-4/prompt.txt: 9a42f6d213e4ea901ae4d99c580e82d3d63129ead9e02543b61814fe88b00e42
        A/tables/TABLE-3-page-5-4/meta.json: 49f59bde4a19254d052ec966987a2c3983b5ef8c0b1d533ffb5a285b5c0b8cbc
        A/tables/TABLE-3-page-3-1/raw.json: 6a30c378ef1d5cb74d9d9bdf9c6a2e938f9a53a3beaadfe9675eb9b286d58c1c
        A/tables/TABLE-3-page-3-1/prompt.txt: 076b6ac4d7eebfd5d7cff71d4334ad85c3eefa2cc822ae47560e30f499b1d78c
        A/tables/TABLE-3-page-3-1/meta.json: 038e6828915038eb976a8eeb95140f6dd21448b3c2dc8f12ac63d36f4588a9f1
        A/tables/TABLE-5-page-9-8/raw.json: 776567c592350400ef15f7f53e6f683460a3668c23e1367292c78061c58091c2
        A/tables/TABLE-5-page-9-8/prompt.txt: 0bd5872e25e0cec2047a0054c3c1788f26e83fdb3219d523ae591f96c8c52d57
        A/tables/TABLE-5-page-9-8/meta.json: 2ad1e74405467318de72f51e4d2ddb912ad0c7d9e7cfcf7a18c20538a2177458
        A/tables/TABLE-4-page-7-6/raw.json: 4c22cbe1a26b6ff561e87db8b66864a3fe1e8c8f5600e6e919cd87ea4b66b21a
        A/tables/TABLE-4-page-7-6/prompt.txt: 28da6b5bfa674458f20a22fb754b765535773bb79fd138c9876c1a163c7f9985
        A/tables/TABLE-4-page-7-6/meta.json: f6c621774c444e70ae3b82b7f689218105c64039c05d476039b6666b9a333722
        A/tables/TABLE-3-page-6-5/raw.json: eb2deb45754fd7069b99bf2a419853e511b24e22f4db0715f231f6946c4ce404
        A/tables/TABLE-3-page-6-5/prompt.txt: 9729c76fd484e2073ceed8189c411af15dedc6f765dea9dd42c0af2b74d4cc6d
        A/tables/TABLE-3-page-6-5/meta.json: b4137886510ba440c655b12cee8984e6e177117ddcbb53f0045c1013e07def13
        A/tables/TABLE-4-page-8-7/raw.json: b26e879844d0690d3205fb3b329edf20f415fe7b8f0d3d2e995721026121b38f
        A/tables/TABLE-4-page-8-7/prompt.txt: 699a45f56205b2ab1832af7f53e64c212d838543f1e61c6feb5a7310c1e5457c
        A/tables/TABLE-4-page-8-7/meta.json: 3593cf042f4efff3ed8c7556a61030d4a013e53d4f7f9f286594d81dbea9a3a1
        A/tables/TABLE-2-page-4-3/raw.json: 78391e60e3d736545e7a94bc1de00f9278234b9b9d518004e3b84b85a6140636
        A/tables/TABLE-2-page-4-3/prompt.txt: cb307342e10d20a225ac7489f0c63d049aeaa960fc8b8a0ac75c4f4c593c585e
        A/tables/TABLE-2-page-4-3/meta.json: 9e01b721a5d5669819b6b22a232608d6f52db686e55f288b00a1f056ac8b6c6c
        B/passages.json: d675bfa85b5876cf1886835b029326f1e98003f6cf875e1854500edfab315678
        B/raw.json: 7f693d6e729bb029fb1e906983198f18ab59ee14b443c54cc54368dc32e48400
        B/source-units.json: c3a5da11ecda62ea0a14ce213517fd7105b1100903c65c29a322b4efdec95840
        B/full-source-units.json: 21b392590594d4f43c53153851a41f93ce654c77b72d4322e6ea6639b8037b77
        B/meta.json: de674f5d0186499415ffec89481031617492a6bcb05f5e0b9511544acab31dbc
        B/table-images/TABLE-5-page-9-1.png: 67daafcc9c6b44c1ae28506d80eeb2612408201464f0d1fce44714f0c045ebd0
        B/table-images/TABLE-1-page-3-2.png: bcc57522ea6c16526a2bc5f584acecfddb2f793213dbb25602299eb7610f0f02
        B/table-images/page-3.png: 05ce4271bad89a2be4857977d25c2ddd88d34ab1b0e99e61635de1d6fbed912b
        B/table-images/page-6.png: dee64f1f56536a1c5b73459a73e6a427c00686dbad5c9beb08d770fee1b603ae
        B/table-images/TABLE-4-page-8-1.png: 076c692a261a1aa0fc359d03e48cc2ecc90db5ac79f7f9477cb1c81b82d4e738
        B/table-images/page-7.png: d2b0fc027bef1d4c561ad5ba526b4a3399bacca1c1f6ddb5a4562fa0cbe25ab6
        B/table-images/page-5.png: 505a2ad7f4905bf4fff1e4b5020663b863a485e8ac95de011335a9bb2dc04e9a
        B/table-images/page-4.png: c9c172cbc4e4a1b1089109858adb3f4c0725e6e0a1a5826a3ee26bb33b3a3fcd
        B/table-images/page-9.png: 0b769fabe432db79f27e1a025e732cc72d67a33d5b239ca82a5a0bde40a71dbf
        B/table-images/TABLE-3-page-6-1.png: 831d1dc3d767e4cd42a394f41923ead2d817b92c4aad6e0af671c764152d4c44
        B/table-images/page-8.png: 5fdec18b53c44285a5fc978d7522bba89c9c94284a23a4dea953a9605f8844f8
        B/table-images/manifest.json: c1faaae386d8088cb0caa0b0d4b7a71841fe259e04e49c81c566fcfc5c0b8eea
        B/table-images/TABLE-2-page-4-1.png: e0aa21098344e42768e03fd1cfb364de6dd67be327724eac9b012b14ef886be7
        B/table-images/TABLE-3-page-5-1.png: 4bcce4e86881bcdd0d65a9477d0c1ebdff7c4378424bff8286dc652d07dbb4ea
        B/table-images/TABLE-4-page-7-1.png: 6649fb48005b734775149d7a67ed34ff3888616aac4c02080500fb49911d29d9
        B/table-images/TABLE-3-page-3-1.png: 6f112c1cd31eba6bd8c541a42a3e3aaae4cda3bf47b7688c77ac6e37888cce4e
        B/clauses/window-03/raw.json: a4d26a503072532cb683d77355c0f2b7edd9631083597700010178d87ca78904
        B/clauses/window-03/prompt.txt: 758a2fdace3a7a0926823bc7769e7207623174f84136c1c9ad2516987cba6fcd
        B/clauses/window-03/meta.json: 0e61ffc51ded3cd34ba951ecda0687d9208062aef14b4a55df873ac8eb841de7
        B/clauses/window-04/raw.json: 3e2bbf38167a6998fc3a180c77b5f2b032c6bac93d7c8185d6c497469f1bc7e0
        B/clauses/window-04/prompt.txt: f2435cb510b59892faf6a0af4fb4fc8d20946238649f9bf6635f5ad2c169b84e
        B/clauses/window-04/meta.json: ac0e1e8ffadf6b23fef331840cc1bb0b9500bec9c1c6c8ef187cff731b19629a
        B/clauses/window-05/raw.json: 61c44d5158f3f01ff790b981a616c5317a18dc23b742a4f117af045d0ad82f47
        B/clauses/window-05/prompt.txt: e1fa2c4b50ba92a35f187b2abc80fec8f57840acf813a76e1b2abb08e35a2850
        B/clauses/window-05/meta.json: 05d34187fd26c6d0087699ffba2b8e979729de9c40f1ccc6340368b45c5a78df
        B/clauses/window-02/raw.json: 85738cfc6836b417b91adf9d573c825ee8314671eeef2e51d12fe64c5de2f0b2
        B/clauses/window-02/prompt.txt: b1949171e219e33d9b384b5c6cb1a790e9cdfe188d5d5a308b7ccf58b396bd5b
        B/clauses/window-02/meta.json: 4094f23ebf69a3046d9620e91c5e546bfa1649b920a527778e809d31b36fff22
        B/clauses/window-09/raw.json: fe06e17790c7ad371ffe6a759c56518a166f6b3e4a70efe3d630c240761006ab
        B/clauses/window-09/prompt.txt: 5c7e39391c4bee67089169116d055a864b2924ab7c4ca6e0e36474a6c6236dc1
        B/clauses/window-09/meta.json: 39b06fd6087f5332c3057ce26c243a163fdb19116bf4de850f788f4a09be747b
        B/clauses/window-07/raw.json: 3c0905ede262b43281ad8bafaeafb4454028334069616e38e5404e0c31c21a40
        B/clauses/window-07/prompt.txt: c144787ac67dc26d3bfb1c35c190254e221d9bf84ebf685febf80f5791e14441
        B/clauses/window-07/meta.json: b878aebc82280497a1d46e73489278372f2e76f54d96c0ff3322bc7fdb30395d
        B/clauses/window-01/raw.json: 07e9d4e85563fb9715523d9918cf3f3d506dbd784846d5be471b88b9670d9977
        B/clauses/window-01/prompt.txt: ee240ae7c5f9a04895ed073dafbf901b4da2a7e7016a80f073503bed5ed3e596
        B/clauses/window-01/meta.json: e3a9239fbb0fce925ae89fce56a8ca9d5f91ebd3872314245400419bf91f6e15
        B/clauses/window-06/raw.json: 075971e0191b0b5c887ba8d37870e58c4594ec938904b121f46e0e8a3a491e06
        B/clauses/window-06/prompt.txt: 68c49c9047c81d75ff79137ac15cba11a49ca8aa02635a1522b8827a121ec32e
        B/clauses/window-06/meta.json: 55cf515c4983cc605a66f893e96a451981e1e9d1e788929f9c9fdc5ee8886547
        B/clauses/window-08/raw.json: 2b1f82a0c22afde307662252d9faa07e8a647e688049ee8d54440a8aeb25af6c
        B/clauses/window-08/prompt.txt: 495829182d5ae3f2a35b4a7ba33ae5de61fda35abba2c24902369c22adea2080
        B/clauses/window-08/meta.json: 59ce450fbfadc1f3fadade089798a6ba54dae3fb86b6bcd6106dc5dfcc7e6f39
        B/tables/TABLE-1-page-3-2/raw.json: 88417efa2855cd48167c924de7ab2992d51cc2d3e0efec78c44341fcb52b0e8e
        B/tables/TABLE-1-page-3-2/prompt.txt: 0a56c7406b8188d0827538c8c9008c344a078962e0a8bf0e18e8bac43bd24eb0
        B/tables/TABLE-1-page-3-2/meta.json: 92ab4166f4f418db3cf549a4c24180da8e196869b7d7adf18503c044b3f284a8
        B/tables/TABLE-3-page-5-4/raw.json: a58c50374f05a18558041a4e99ca0167f404d18c72c14787efa79f0fddfb015c
        B/tables/TABLE-3-page-5-4/prompt.txt: 9a42f6d213e4ea901ae4d99c580e82d3d63129ead9e02543b61814fe88b00e42
        B/tables/TABLE-3-page-5-4/meta.json: f3d7600a32fde94e0cd12a90c596aae08fbd570595bf3a3a261933bf8e1ce4b8
        B/tables/TABLE-3-page-3-1/raw.json: 2b98f05cbb1fc6fcbe58e6f74105f6553bc10c324520ca68c0fb421e97367862
        B/tables/TABLE-3-page-3-1/prompt.txt: 076b6ac4d7eebfd5d7cff71d4334ad85c3eefa2cc822ae47560e30f499b1d78c
        B/tables/TABLE-3-page-3-1/meta.json: 891b7713cc9560a76491ce380941f61b5bb05eb44adf95f3d57eaafedf2a6d5c
        B/tables/TABLE-5-page-9-8/raw.json: 77bfb1e0265d40cecd89a5ae9cc3a044d9c50170084fbbdfbb301f763150f1c2
        B/tables/TABLE-5-page-9-8/prompt.txt: 0bd5872e25e0cec2047a0054c3c1788f26e83fdb3219d523ae591f96c8c52d57
        B/tables/TABLE-5-page-9-8/meta.json: 538601b4d23ca3d3ec3947a078a06b9fca1bf72e6d6ae0fb27f64103ee9981b0
        B/tables/TABLE-4-page-7-6/raw.json: 943eda9beaa58b7c2e68e42c92fbb444ab4438f6f3ba0964723ad2d6284b05dc
        B/tables/TABLE-4-page-7-6/prompt.txt: 28da6b5bfa674458f20a22fb754b765535773bb79fd138c9876c1a163c7f9985
        B/tables/TABLE-4-page-7-6/meta.json: a2ea65ac0988574ad32c11bfed2a01ed2211eaa93db8b5785242b67965cdd879
        B/tables/TABLE-3-page-6-5/raw.json: 33e60fef990adfd387138720495bb358d2e847710620f7e65da04d6f1c4c75b0
        B/tables/TABLE-3-page-6-5/prompt.txt: 9729c76fd484e2073ceed8189c411af15dedc6f765dea9dd42c0af2b74d4cc6d
        B/tables/TABLE-3-page-6-5/meta.json: ca0c50316839b67c5daade1598c121f71278131ba957c6680b943b5fa8674acb
        B/tables/TABLE-4-page-8-7/raw.json: a0b4cf8fbb170345bcdb60463bb822b2575a73b9ac86cb14986075a5ad51383d
        B/tables/TABLE-4-page-8-7/prompt.txt: 699a45f56205b2ab1832af7f53e64c212d838543f1e61c6feb5a7310c1e5457c
        B/tables/TABLE-4-page-8-7/meta.json: 05f6a6e357c55e53ab304f443b2a9e1d8594fafd497bb970ff66b78b7a75dccc
        B/tables/TABLE-2-page-4-3/raw.json: f22ee7eed54d84c7e5b8490f65c3938c2569ea725cfd2aa15e6e662962511374
        B/tables/TABLE-2-page-4-3/prompt.txt: cb307342e10d20a225ac7489f0c63d049aeaa960fc8b8a0ac75c4f4c593c585e
        B/tables/TABLE-2-page-4-3/meta.json: 316d51a9d0e951c0ed48d643689a3ef4f9e08d8b2dd8582178873e6c155da6c4
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
      pdf_sha256: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
      source_review: _compare/relationships-2026-11-16/review-current/Shekari2022
      source_status_sha256: 651562489a7fc85ec63cffe64e61fa2fbd3cea6b0ec50dbcacf9db1cf2ff74f3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R018
    exposure:
      text: phonological-based therapies
    outcome:
      text: activation of insula
    analysis_label: Treatment and Insula activation
    relation: association
    evidence_ids:
    - P13-S2-C9
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
      pdf_sha256: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
      source_review: _compare/relationships-2026-11-16/review-current/Shekari2022
      source_status_sha256: 651562489a7fc85ec63cffe64e61fa2fbd3cea6b0ec50dbcacf9db1cf2ff74f3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C6
      - Result passage disposed without unit P1-S1-C7
      - Result passage disposed without unit P3-S2-C13
      - Result passage disposed without unit P3-S2-C14
      - Result passage disposed without unit P3-S2-C3
      - Result passage disposed without unit P3-S2-C5
      - Result passage disposed without unit P3-S2-C15
      - Result passage disposed without unit P3-S2-C16
      - Result passage disposed without unit P3-S2-C17
      - Result passage disposed without unit P3-S2-C18
      - Result passage disposed without unit P8-S1-C4
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P8-S1-C6
      - Result passage disposed without unit P15-S3-C10
      - Result passage disposed without unit P15-S3-C11
      - Result passage disposed without unit P15-S3-C12
      unattached_null_or_qualifier_ids:
      - P3-S2-C7
      suppressed_nonrepresented_units: 14
      default_disposition_count_requires_completeness_check: 220
      unselected_timing_passages:
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C14
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P3-S2-C16
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S2-C17
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S2-C18
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S3-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S3-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P8-S1-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P8-S2-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: tested_personal_effects
        source_id: P12-S1-C10
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: eligibility
        source_ids:
        - P2-S3-C7
        - P2-S3-C8
        - P2-S3-C9
        - P2-S3-C10
        - P2-S3-C11
        - P2-S3-C12
        - P2-S3-C13
        - P2-S3-C14
        - P2-S3-C15
        - P2-S3-C16
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_timing
        source_ids:
        - P7-S1-C3
        - P7-S1-C4
        - P7-S1-C5
        - P7-S1-C6
        - P7-S1-C7
        - P7-S1-C8
        - P7-S1-C9
        - P7-S2-C1
        - P7-S2-C2
        - P7-S2-C3
        - P8-S3-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_timing
        source_ids:
        - P7-S1-C3
        - P7-S1-C4
        - P7-S1-C5
        - P7-S1-C6
        - P7-S1-C7
        - P7-S1-C8
        - P7-S1-C9
        - P7-S2-C1
        - P7-S2-C2
        - P7-S2-C3
        - P8-S3-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P3-S2-C16
        - P3-S2-C17
        - P3-S2-C18
        - P10-S1-C4
        - P10-S1-C5
        - P11-S1-C1
        - P11-S1-C2
        - P11-S1-C5
        - P12-S1-C5
        - P12-S1-C9
        - P13-S1-C1
        - P13-S1-C3
        - P13-S1-C4
        - P13-S1-C5
        - P13-S1-C7
        - P13-S1-C8
        - P13-S1-C9
        - P13-S1-C10
        - P13-S2-C4
        - P13-S2-C6
        - P13-S2-C9
        - P13-S3-C7
        - P13-S3-C8
        - P13-S3-C10
        - P14-S1-C4
        - P14-S1-C8
        - P14-S1-C9
        - P14-S1-C10
        - P14-S1-C11
        - P14-S1-C12
        - P14-S1-C13
        - P14-S2-C4
        - P14-S2-C5
        - P14-S2-C7
        - P14-S2-C8
        - P14-S3-C3
        - P14-S3-C4
        - P14-S3-C5
        - P14-S3-C7
        - P14-S3-C8
        - P14-S3-C9
        - P14-S3-C11
        - P15-S1-C6
        - P15-S1-C7
        - P15-S1-C9
        - P15-S2-C7
        - P15-S2-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P3-S1-C11
        - P3-S1-C12
        - P3-S1-C14
        - P3-S1-C15
        - P3-S1-C18
        - P3-S1-C19
        - P3-S1-C20
        - P3-S2-C10
        - P4-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - eligibility
      - imaging_timing
      - outcome_timing
      - outcome_definition
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-2
      - TABLE-2-page-4-3
      - TABLE-3-page-3-1
      - TABLE-3-page-5-4
      - TABLE-3-page-6-5
      - TABLE-4-page-7-6
      - TABLE-4-page-8-7
      - TABLE-5-page-9-8
      unlinked_tables:
      - TABLE-1-page-3-2
      - TABLE-2-page-4-3
      - TABLE-3-page-3-1
      - TABLE-3-page-5-4
      - TABLE-3-page-6-5
      - TABLE-4-page-7-6
      - TABLE-4-page-8-7
      - TABLE-5-page-9-8
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P4-S1
        - P9-S2
        - P10-S1
        - P11-S1
        - P12-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
      source_review: _compare/relationships-2026-11-16/review-current/Shekari2022
      source_status_sha256: 651562489a7fc85ec63cffe64e61fa2fbd3cea6b0ec50dbcacf9db1cf2ff74f3
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the number of studies selected for review.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes association between naming improvement and brain activation
        changes.
    - source_id: P3-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Provides participant demographics.
    - source_id: P3-S1-C19
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes types of aphasia in the sample.
    - source_id: P3-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes participant characteristics (word-retrieval problems).
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes treatment duration.
    - source_id: P3-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes MRI scanner characteristics.
    - source_id: P3-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes imaging acquisition (T1-weighted images).
    - source_id: P3-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes study designs.
    - source_id: P3-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the distribution of treatment protocols used.
    - source_id: P3-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement of naming improvement without specific brain relationship.
    - source_id: P3-S2-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes generalization effects.
    - source_id: P3-S2-C15
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes negligible effects for untreated items.
    - source_id: P3-S2-C16
      disposition: represented
      result_indexes:
      - 0
      reason: Establishes association between naming improvement and brain activation
        changes.
    - source_id: P3-S2-C17
      disposition: represented
      result_indexes:
      - 1
      reason: Specifies that both increased and decreased activation are associated
        with naming improvement.
    - source_id: P3-S2-C18
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies bilateral involvement in naming improvement.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement that treatments improved naming.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about brain reorganization.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about bilateral involvement.
    - source_id: P9-S2-C1
      disposition: represented
      result_indexes:
      - 24
      reason: Table 5 data for Marcotte et al. 2012 showing brain area activation.
    - source_id: P12-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Figure 7 caption.
    - source_id: P15-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P15-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P15-S3-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    - source_id: P15-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: General conclusion statement.
    unresolved_coverage: []
    pending_source_ids:
    - P1-S1-C6
    - P3-S1-C11
    - P3-S1-C19
    - P3-S2-C3
    - P3-S2-C5
    - P3-S2-C7
    - P3-S2-C9
    - P3-S2-C10
    - P3-S2-C12
    - P3-S2-C13
    - P3-S2-C14
    - P3-S2-C15
    - P3-S2-C18
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C6
    - P9-S2-C1
    - P12-S2-C5
    - P15-S3-C9
    - P15-S3-C10
    - P15-S3-C11
    - P15-S3-C12
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-2
    - TABLE-2-page-4-3
    - TABLE-3-page-3-1
    - TABLE-3-page-5-4
    - TABLE-3-page-6-5
    - TABLE-4-page-7-6
    - TABLE-4-page-8-7
    - TABLE-5-page-9-8
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S1-C11
      recruited_sample:
      - P2-S2-C9
      - P2-S3-C2
      eligibility: []
      imaging_provenance:
      - P2-S1-C4
      - P2-S1-C5
      imaging_timing: []
      outcome_timing: []
      outcome_definition: []
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P10-S1-C4
      - P10-S1-C5
      - P11-S1-C1
      - P12-S1-C5
      limitations:
      - P15-S3-C7
      - P15-S3-C8
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P3-S2-C16
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S2-C17
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S2-C18
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S3-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S3-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S3-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P8-S1-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P8-S2-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: tested_personal_effects
      source_id: P12-S1-C10
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: eligibility
      source_ids:
      - P2-S3-C7
      - P2-S3-C8
      - P2-S3-C9
      - P2-S3-C10
      - P2-S3-C11
      - P2-S3-C12
      - P2-S3-C13
      - P2-S3-C14
      - P2-S3-C15
      - P2-S3-C16
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_timing
      source_ids:
      - P7-S1-C3
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C8
      - P7-S1-C9
      - P7-S2-C1
      - P7-S2-C2
      - P7-S2-C3
      - P8-S3-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_timing
      source_ids:
      - P7-S1-C3
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C8
      - P7-S1-C9
      - P7-S2-C1
      - P7-S2-C2
      - P7-S2-C3
      - P8-S3-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P3-S2-C16
      - P3-S2-C17
      - P3-S2-C18
      - P10-S1-C4
      - P10-S1-C5
      - P11-S1-C1
      - P11-S1-C2
      - P11-S1-C5
      - P12-S1-C5
      - P12-S1-C9
      - P13-S1-C1
      - P13-S1-C3
      - P13-S1-C4
      - P13-S1-C5
      - P13-S1-C7
      - P13-S1-C8
      - P13-S1-C9
      - P13-S1-C10
      - P13-S2-C4
      - P13-S2-C6
      - P13-S2-C9
      - P13-S3-C7
      - P13-S3-C8
      - P13-S3-C10
      - P14-S1-C4
      - P14-S1-C8
      - P14-S1-C9
      - P14-S1-C10
      - P14-S1-C11
      - P14-S1-C12
      - P14-S1-C13
      - P14-S2-C4
      - P14-S2-C5
      - P14-S2-C7
      - P14-S2-C8
      - P14-S3-C3
      - P14-S3-C4
      - P14-S3-C5
      - P14-S3-C7
      - P14-S3-C8
      - P14-S3-C9
      - P14-S3-C11
      - P15-S1-C6
      - P15-S1-C7
      - P15-S1-C9
      - P15-S2-C7
      - P15-S2-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C14
      - P3-S1-C15
      - P3-S1-C18
      - P3-S1-C19
      - P3-S1-C20
      - P3-S2-C10
      - P4-S1-C3
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
      pdf_sha256: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
      review_sha256: ddcc5025518180128fcc9f580a9d484df35db26e268192e69650a6c10abf9ef3
      code_sha256: c4650d24fa3e36e6f317cb65cc7626277a28936a7cdf5d07248d4b1e5bfa09aa
      source_helpers_sha256: e0e0f295e5efa1fdb4e9e8c84ca491d062df3aefe8ca8b4d9ca85fcb6d4c9082
      converter_sha256: 048f1e35905528676837a00b1b2406b1c97cb1eb47c48d63f121a5c00cc0afeb
      table_helpers_sha256: 78e562e9725fc484d6a12279ea710856dfd1d9aa13ee178d0358e9c0acdd2c8c
      mapper_budget: 2500
      reviewer_budget: 1600
      approved: false
      visual:
        models:
        - gemma4:31b
        - qwen3.8:27b
        digests:
        - 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        - 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
        layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
    approved: false
    core_review:
      own_result_source_ids:
      - P13-S2-C9
      source_result: The source states that activation of the insula was revealed
        after phonological-based therapies in patients with aphasia, specifically
        citing Nardo et al. (2017) and Vitali et al. (2007). This is a qualitative
        synthesis of findings from a systematic review of fMRI studies.
      result_status: qualitative_synthesis
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis R018 correctly identifies the relationship
            between phonological-based therapies and insula activation as reported
            in the source. The source is a narrative review, so the 'analysis' is
            the synthesis of findings from included studies, not a new statistical
            model. The draft correctly reflects this as a qualitative synthesis.
          source_ids:
          - P13-S2-C9
          - P3-S1-C2
        direction:
          answer: fits
          reason: The source explicitly states that activation was 'revealed' after
            therapy, indicating a detected association (increased activation). The
            draft's direction 'likely' and claim 'activation... was revealed' align
            with this positive finding.
          source_ids:
          - P13-S2-C9
        construct:
          answer: fits
          reason: The exposure (phonological-based therapy) and outcome (insula activation)
            are correctly identified. The measurement method is task-based fMRI during
            picture-naming, which is consistent with the source description of the
            included studies.
          source_ids:
          - P13-S2-C9
          - P3-S2-C11
          - P1-S1-C2
        qualifications:
          answer: fits
          reason: The draft includes relevant qualifications such as the measurement
            context (picture-naming tasks) and the nature of the evidence (narrative
            review). It also notes limitations regarding the dissociation of semantic
            and phonemic treatments, which is a key caveat in the source.
          source_ids:
          - P15-S3-C2
          - P3-S1-C2
        missing_material_caveat:
          answer: fits
          reason: The draft captures the main limitations mentioned in the source,
            such as the difficulty in dissociating treatment effects and study heterogeneity.
            No material caveats that would change the interpretation of the insula
            finding are omitted.
          source_ids:
          - P15-S3-C2
          - P15-S3-C8
      optional_pending:
      - Specific statistical values or coordinates for insula activation are not transcribed
        as this is a qualitative review.
      - Exact sample sizes for the specific studies cited (Nardo, Vitali) are not
        detailed in the provided source window, only the aggregate of 146 participants
        across 14 studies.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific statistical values or coordinates for insula activation are not transcribed
      as this is a qualitative review.
    - Exact sample sizes for the specific studies cited (Nardo, Vitali) are not detailed
      in the provided source window, only the aggregate of 146 participants across
      14 studies.
    normalizations:
    - field: sample.n
      original: 146
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R018
      exposure:
        text: phonological-based therapies
      outcome:
        text: activation of insula
      analysis_label: Treatment and Insula activation
      relation: association
      evidence_ids:
      - P13-S2-C9
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
        pdf_sha256: 070c1deead0f311773ac0324e4b3ca57dcd9dd5c348f9de6ef0cfdda433ae20a
        source_review: _compare/relationships-2026-11-16/review-current/Shekari2022
        source_status_sha256: 651562489a7fc85ec63cffe64e61fa2fbd3cea6b0ec50dbcacf9db1cf2ff74f3
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings: {}
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 13
  quote: 'Insula

    The activation of this area was revealed after phonological-

    based therapies (Nardo et al., 2017; Vitali et al., 2007).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
