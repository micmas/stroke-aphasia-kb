---
id: extrasylvian_extension
name: extrasylvian damage cluster
kind: network
findings:
- id: f1
  target: reading_spelling_phonological_ability
  target_kind: impairment
  claim: There were no significant differences between patients with only perisylvian
    damage and those with substantial extrasylvian damage on measures of reading accuracy,
    spelling accuracy, or phonological ability, after controlling for the number of
    damaged perisylvian regions.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: left-hemisphere damaged patients with language impairment and perisylvian
      cortical damage
    phase: not_reported
    time_post_onset: subacute or chronic stage (typically several months or years
      post-onset)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Retrospective study design
  - Mix of clinical CT and research MRI scans introduced variability in image quality
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Presence or absence of lesion extension outside a
    mask of the entire perisylvian region, categorized as ''perisylvian only'' (no
    or minimal extension) versus ''perisylvian plus'' (substantial extrasylvian damage).
    Analysis was performed using ANCOVAs with the number of damaged perisylvian regions
    as a covariate. Additional metadata has not been transcribed; review the pending-field
    flags before approval. PDF image reading (P3-S3-C3, two-model agreement, human
    verification pending): . To be included, participants had to fulfill the following

    selection criteria: (1) CT or MRI evidence of damage to one or

    more perisylvian cortical regions implicated in phonological

    processing, including posterior inferior frontal gyrus/Broca’s

    area (BA44/45), precentral gyrus (BA4/6), insula, superior tem-

    poral gyrus/Wernicke’s area (BA22), and supramarginal gyrus

    (BA40), and (2) having received a detailed evaluation of reading

    and spelling performance in the subacute or chronic stage of

    their illness (typically several months or years post-onset) Original text-layer
    quotation is preserved below.'
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
    - proposed_concept:reading_spelling_phonological_ability
  citation: '@Rapcsak2009'
  source_passages:
  - section: Original source P11-S3-C2
    page: 11
    quote: 'Based on this information, we subdivided patients into

      two groups: the ‘‘perisylvian only’’ group included individuals

      whose lesions showed no or minimal extension outside the

      perisylvian region (n ¼ 13), whereas the ‘‘perisylvian plus’’

      group included participants with evidence of more substantial

      extrasylvian damage (n ¼ 18).'
    supports: method
  - section: Original source P11-S3-C6
    page: 11
    quote: 'To accomplish this, we conducted a series of

      ANCOVAs with group (‘‘perisylvian only’’ vs ‘‘perisylvian

      plus’’) as the factor, non-word and real word reading/spelling

      scores and PC scores as the dependent variables, and the

      number of damaged perisylvian regions as the covariate.'
    supports: method
  - section: Original source P11-S3-C7
    page: 11
    quote: 'The results of these analyses indicated that there were no sig-

      niﬁcant differences between the groups on any of the relevant

      measures of reading/spelling accuracy or phonological ability

      after controlling for the effect of the extent of the perisylvian

      damage on performance.'
    supports: claim
  - section: Original source P3-S3-C3
    page: 3
    quote: 'To be included, participants had to fulﬁll the following

      selection criteria: (1) CT or MRI evidence of damage to one or

      more perisylvian cortical regions implicated in phonological

      processing, including posterior inferior frontal gyrus/Broca’s

      area (BA44/45), precentral gyrus (BA4/6), insula, superior tem-

      poral gyrus/Wernicke’s area (BA22), and supramarginal gyrus

      (BA40), and (2) having received a detailed evaluation of reading

      and spelling performance in the subacute or chronic stage of

      their illness (typically several months or years post-onset).'
    supports: sample
  - section: Original source P3-S3-C4
    page: 3
    quote: 'Us-

      ing these dual criteria, we were able to identify 31 participants

      for the study (mean age ¼ 60.07 years, range: 40–78; average

      years of education ¼ 14.55, range: 11–20).'
    supports: sample
  - section: Original source P14-S3-C10
    page: 14
    quote: 'Due to the ret-

      rospective nature of this investigation, we were unable to en-

      '
    supports: limitation
  - section: Original source P15-S1-C1
    page: 15
    quote: '

      relied on a mix of clinical and research scans which introduced

      some variability in terms of image quality and detail.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Rapcsak2009
  proposal_id: R014
  review_status_sha256: 0988d0022f0e697b7c73b644ce317bd5eaa909feca6dffd6865086c6e23bc6ce
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
    original_review_binding:
      version: relationship-review-v6
      input_hashes:
        pdf: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
        A/passages.json: 3e32cfec0e12804e672ec44b271d4cd8788148aeb567977855e2954d6b6dfb88
        A/raw.json: 412b7029a548da60c95e2c6fd35878e0ad1ff704f9fb361db0249b2c4fc2d666
        A/source-units.json: 56a0613fe298c1b777d00754df25452405c0741358df3d474b4b083af959f1b8
        A/full-source-units.json: 56a0613fe298c1b777d00754df25452405c0741358df3d474b4b083af959f1b8
        A/meta.json: af8dd11f6c33cb33d920f3cedf375f90000ab9eea06cf8bbf8b96c477538d4b9
        A/table-images/manifest.json: f56c0e1fe77ba467382185f69f55f252420c57f0c8986276d40123d534c3f996
        A/clauses/window-11/raw.json: 43a97a47cb8e1ba0d2cff6285b6189fff75d4a70833a18b1c6d2c2e425b4794f
        A/clauses/window-11/prompt.txt: f30744c8b13e0db91ff80fe7403442b797a13e373d97ccb9c4d1bba524d73be3
        A/clauses/window-11/meta.json: 7eeed54eb12d15715f48dd0c8c1399e080da6ec9729cfcc608b9455596a19dc7
        A/clauses/window-16/raw.json: 9c3fedfe55fde0902b3104225ceeda776a0b88180cc97a60aba159bdd0030211
        A/clauses/window-16/prompt.txt: 82327ce50b99588f30a02f8a3545fcf6b592a4911192882a8cc280307cda1403
        A/clauses/window-16/meta.json: 64e78b047e9f16b3e5cff8b0fd9f832be8b2cb3a36b82b028b9de0682ee7d32a
        A/clauses/window-20/raw.json: 0f5d2917ded97b164757d8bc37eaf2fd59ba8f6c568d8a7e8d15d2871d96fbdd
        A/clauses/window-20/prompt.txt: 484d8fbd7b1becb68cfc96e4f15e706ec3c33e66edebdfc0ba96b21c7639ac18
        A/clauses/window-20/meta.json: 9caa54435670558f8ee0af5874a673da42d12a029bdf02e3a1bcf1b0e34aa260
        A/clauses/window-18/raw.json: 0fcefa7447c27bf4498e1cc7e01eccd9e2d693b7b957acab21b959ae68fcf28c
        A/clauses/window-18/prompt.txt: 700a1aeb2c99bafeb7f062ed851fee346c67291e48927dc72ddb884572d8a977
        A/clauses/window-18/meta.json: 71cb399115a77049f6c3e9952df6d188c33dde7708228eb3585de96e8a62fc8a
        A/clauses/window-19/raw.json: 614377e32ea91e19b09f7c0b421dfaf029329c9ed1d98dae84434636c6b2c3c1
        A/clauses/window-19/prompt.txt: 14821665dbd07cd9eb056bb7a91094614d4878333a3977d2bfb285b29be20bc6
        A/clauses/window-19/meta.json: 4d1c9259705fb79fca7f14630b5096983ac9a28aaf23c62949a81a7944e50a79
        A/clauses/window-21/raw.json: e5c805e98582942b647a5223546d956d7ded41d9291fdd06af92618d3325ba4a
        A/clauses/window-21/prompt.txt: ee755a40bb3d59562f192a01ba32c11d232d892a635037d3676a362bed9daafc
        A/clauses/window-21/meta.json: 27c2479ded27d96a4151b94aff628c228d2172820f2b451edfadbd5432a0656c
        A/clauses/window-17/raw.json: 59f4d43f9e3d4bbc9f4b7ba089ef329abe549c5d7edc720af3414b6afbb92a2f
        A/clauses/window-17/prompt.txt: 4c6bf43194363e525b602464aaa37e124c7a07e5c1ae9b8d125616cf212e197a
        A/clauses/window-17/meta.json: 60da281f5205f29dc8651fa334f1def7af38fa686e69bf7cc1867ac5fabe9524
        A/clauses/window-10/raw.json: 9df21457076162efbba7220b9cad0df38c8f99d5aa01e95698cfaf8eb6568c46
        A/clauses/window-10/prompt.txt: cd4d30cac68684c857df1b91ae62bddec687ea5922e2831d010036fe420c71e5
        A/clauses/window-10/meta.json: b82d6a7638739b1c6bb3bf588e69ac9343be91c1ea508c24175da0f48aeb6e98
        A/clauses/window-03/raw.json: a306c0deca494578fa169aa5474561009345e4adeda50865d97a79e36e20bfc3
        A/clauses/window-03/prompt.txt: b315631d34720182d2f48ca9f0b9cec82126506ffd4492ff0c0dbceeb9c729a3
        A/clauses/window-03/meta.json: 59c92d5a708e161a1c42b7b9fc1cfcf8f56b45ad4e39fa9034c2d75edace4573
        A/clauses/window-04/raw.json: 176e87483ed3710ea47eb12333948c69c5d2ed80deba47dfa692c7439550d336
        A/clauses/window-04/prompt.txt: 2dc80bcdbcd30ad86a666136b39a028e5890378358dbb88ec2329469dfd4a5d6
        A/clauses/window-04/meta.json: c3a179c17b85bdca1200a4495949c9be8f6f2e1b62d9a621941f9c2396377cb6
        A/clauses/window-05/raw.json: 91d61803b08f82e17942c7b43724395d30b73d938d5ac6938d28e7f03900f821
        A/clauses/window-05/prompt.txt: bb8ef5174e002556dd9100b4e31e980ba4e8f5815e9cbc4135d488029b4c91e0
        A/clauses/window-05/meta.json: 9f5c6b4eb7fd08b5ba40765f86bbf064b0c588f8716ff24d66a5dba65d032217
        A/clauses/window-02/raw.json: 769b199072f3f842055b17c6883b8094bcc5826cf7895ef848b1d88722f2c5f1
        A/clauses/window-02/prompt.txt: c32cdde48f616dc5b2f2f42ee08d479d27b07b5ecba293fedb7f593f93a93107
        A/clauses/window-02/meta.json: 5fcba767df489fc71258c6af842618bffd6ea53d8c581c7163fc3b3c216b5c36
        A/clauses/window-15/raw.json: 03f4a7e952fce679af598fda0b4f282d711a35e19dda343ff7ac92e50bb77fc3
        A/clauses/window-15/prompt.txt: c13ce348e69bfabe55c0387942e197de2d76d6bdcd52dfdc66dabe2ce47e7c98
        A/clauses/window-15/meta.json: 6d4dfee169628dfddb8d3a7d4d962ea82b76eccc2302830400bc040720de36a2
        A/clauses/window-12/raw.json: 9da2b73f5eeebbaeadf2a6f34ef2e5d2982236ab0f1d75a85e7be4b3ff803d3f
        A/clauses/window-12/prompt.txt: 416cbba3ecf61ff134a3aaac69e3810bd980a01a99f303fe6cc553709fbcafcd
        A/clauses/window-12/meta.json: e69e5e883fb334e2bcfabfaf8f33efad388196aa8b7088debc003a8b019130d9
        A/clauses/window-22/raw.json: 6b941120ad3ed96adb9b7f8e2f02ac3badda3c690a119e6916a7eafabe7151fb
        A/clauses/window-22/prompt.txt: 55c5d0880635c93ab06c050fa7dcf75e666dfc3ffee480e33f706b0e39c6b49c
        A/clauses/window-22/meta.json: 9892bdf935fe7253812843819684ab12f7244170e1df8d82f9cf2ba34079fba4
        A/clauses/window-13/raw.json: f995a47384aeebe519901c9d3254fbe11875ab4bda1ec5e6c6d29aff45cebc80
        A/clauses/window-13/prompt.txt: a93fb430227c2f3814322b096530c88a6e86d1b3bfdc2543914202310b506a16
        A/clauses/window-13/meta.json: e282a143922450ec439b1c1686dbc78e717d34ce07114723058b251e496b12a1
        A/clauses/window-14/raw.json: 3a506cd1121f8c73199f19ff4d42be2a989a76bcb9a1ab890cd2f49f040dbf45
        A/clauses/window-14/prompt.txt: 035d61ebd5e6a5551418fdfdaff706db0a42be0eff53888c17275352bf1b2543
        A/clauses/window-14/meta.json: 5260d6107d1a0442c02acf9bed9533289d18d684f096aad7e17b2c800997b2af
        A/clauses/window-09/raw.json: 5c533c9a78102940c78ae36dbf5e116be55a37bc067757b6610899bb799257db
        A/clauses/window-09/prompt.txt: 0f7c00302db85ad70041cbcdd5bc38dfb907d422869478603680fcca4abfbccb
        A/clauses/window-09/meta.json: cd4f5ab127732c8fc4f9a113e0337625ac2c0d8d386e2c001695c804064edd35
        A/clauses/window-07/raw.json: 1685e4a97839277b84ef5c2768758b58dcf731d2aff93ed02369796c185989f8
        A/clauses/window-07/prompt.txt: 5e6cdf426a8cfd6ca4f4cfb9e8380e4c8f9f0ca354d766b59a8c51d9b4489eb3
        A/clauses/window-07/meta.json: be467675b6ab2b3cb218df58b72ed1d441a127f4a21f66aa9d16d9fecc53f691
        A/clauses/window-01/raw.json: f30c2fb8035a7d2ede4280552179a573b62eaf367857fdd7c6f137fd9a195e75
        A/clauses/window-01/prompt.txt: ef19fa8fc32910efe4c4cb7384418b4cc5ad4660b811d66911c0dac952142b4e
        A/clauses/window-01/meta.json: bf8c82d97d274db06c21e1b5b1f9bf870fdee027677c34b2800d23a5e310df38
        A/clauses/window-06/raw.json: 354a953d06f39e18cf2601de40c85d098f24b4cb59a8a2cb38e20457eef1fe2b
        A/clauses/window-06/prompt.txt: 6ee7becf7a81ed6c748098a783b966823a88aaf6782d10b0cd9f051ed9219971
        A/clauses/window-06/meta.json: f5c98d5ba239168bb77c211533b3ed43d39c64651f59a261026e8bbce0617b7b
        A/clauses/window-08/raw.json: ab0174f6ac6d3c839accbb679d4fddcf73eb1da1b29f0dcfcece253bdad10072
        A/clauses/window-08/prompt.txt: 8c2419cb038c0ae4ac1d683923bd9756000516e0dd10673621491fb27291c32e
        A/clauses/window-08/meta.json: 6ec2f51a62a23e12f629455be6ceef998232bbdf49c528bdbff87877d28eec8e
        B/passages.json: 3e32cfec0e12804e672ec44b271d4cd8788148aeb567977855e2954d6b6dfb88
        B/raw.json: dfa259aaded00b5d5bb08f12d66614ffe4899edf0d4bb16c70301e5ee7639ea6
        B/source-units.json: 56a0613fe298c1b777d00754df25452405c0741358df3d474b4b083af959f1b8
        B/full-source-units.json: 56a0613fe298c1b777d00754df25452405c0741358df3d474b4b083af959f1b8
        B/meta.json: 9e4d6579c77d64bb6a4b944a812efa4c96657f401c371ffdd223d6a279960fc5
        B/table-images/manifest.json: f56c0e1fe77ba467382185f69f55f252420c57f0c8986276d40123d534c3f996
        B/clauses/window-11/raw.json: 6efac73ea75ca07ed607b35eef0b074c933bb413d8af11453e9ca70d1f6c82a2
        B/clauses/window-11/prompt.txt: f30744c8b13e0db91ff80fe7403442b797a13e373d97ccb9c4d1bba524d73be3
        B/clauses/window-11/meta.json: c90a2e913a29c3060da15e52f5430304fe52542f7aa402ea7fbaf0ac7012abdf
        B/clauses/window-16/raw.json: e7fda3bf9806bb7350e16bcf2f31d32e36fc3256d60481611f5ec9f1727b8f9a
        B/clauses/window-16/prompt.txt: 82327ce50b99588f30a02f8a3545fcf6b592a4911192882a8cc280307cda1403
        B/clauses/window-16/meta.json: 69c0ab4d73a05f6396c28d223afe6933a72a895a5ac915f9e3c3ce6316bc28a6
        B/clauses/window-20/raw.json: 63b4a368bf16b8b343c5df885aca826b978fba928c6a1527792c00e67f692afc
        B/clauses/window-20/prompt.txt: 484d8fbd7b1becb68cfc96e4f15e706ec3c33e66edebdfc0ba96b21c7639ac18
        B/clauses/window-20/meta.json: 0eab296f99ff25696cca177ae55472d37b8c5ea203516d5f35e3cd6123fe759d
        B/clauses/window-18/raw.json: 2844c3dab4f9f516d1dc559564d9332aebe73302bc4c3d19cfe5a4ec42cad774
        B/clauses/window-18/prompt.txt: 700a1aeb2c99bafeb7f062ed851fee346c67291e48927dc72ddb884572d8a977
        B/clauses/window-18/meta.json: 2e204a315344524be6fc665dc7c6fc06ca6d187fa17f98009fdb97daef61ff26
        B/clauses/window-19/raw.json: aab88189090e85ab49daade5c44342083f517cca89d2bcd329c813c2585244e2
        B/clauses/window-19/prompt.txt: 14821665dbd07cd9eb056bb7a91094614d4878333a3977d2bfb285b29be20bc6
        B/clauses/window-19/meta.json: c7c8d1624e67992fee2f1c02421b86e4f4f52540ef32fa8925f31570ea4af055
        B/clauses/window-21/raw.json: f611563d3511f4784473ed3e921f45cbf1e18db0240f715c2d1d28a5caaf8997
        B/clauses/window-21/prompt.txt: ee755a40bb3d59562f192a01ba32c11d232d892a635037d3676a362bed9daafc
        B/clauses/window-21/meta.json: 00cf85e4f3b46f1341d8b8a7b58bcf0e7e1cc99ec70adf981bdde01f991f47b1
        B/clauses/window-17/raw.json: 0f83cfb0717f282106bcb8f23166a165e03625bf866d243c4bd02238bf67d9f6
        B/clauses/window-17/prompt.txt: 4c6bf43194363e525b602464aaa37e124c7a07e5c1ae9b8d125616cf212e197a
        B/clauses/window-17/meta.json: 4675d792e0be2278b6bf80ff0191239673d3d490e339f6259fe32f494f4d809c
        B/clauses/window-10/raw.json: 60757e0055acd8c92caa198d691bd7a8d66942d42236dae18be5565b8a52d470
        B/clauses/window-10/prompt.txt: cd4d30cac68684c857df1b91ae62bddec687ea5922e2831d010036fe420c71e5
        B/clauses/window-10/meta.json: ca17d8deb1eec55e9b0ea47944ce0aee0c661b637b42ecdd905ed5eaf4b90d91
        B/clauses/window-03/raw.json: 72536c82130a0dfeb00d4093ff3935da0194ff6ba6d4c4e262e5cc4824bf1be5
        B/clauses/window-03/prompt.txt: b315631d34720182d2f48ca9f0b9cec82126506ffd4492ff0c0dbceeb9c729a3
        B/clauses/window-03/meta.json: 6b376d00c5fa84881e8684e01eed55e7e11a17fce57912b0cc7cea10e7f8c7d5
        B/clauses/window-04/raw.json: cbd73be01042268a3aab6bbe1b3bdb152ba23263fe30a3d4f43f3a2ccbf41d0b
        B/clauses/window-04/prompt.txt: 2dc80bcdbcd30ad86a666136b39a028e5890378358dbb88ec2329469dfd4a5d6
        B/clauses/window-04/meta.json: 4e6918c3381bf4f80aed3e7ca97c62b93dc84444d22fcd381955178363b18c85
        B/clauses/window-05/raw.json: 9b6e0dc3a93691a668e67fd6caf46ae66d308450872844dcf081be81431e8ff1
        B/clauses/window-05/prompt.txt: bb8ef5174e002556dd9100b4e31e980ba4e8f5815e9cbc4135d488029b4c91e0
        B/clauses/window-05/meta.json: ae8d50dc9970a86b81a0f9ef0ec6d42c487656df3da50de175838634754b23ed
        B/clauses/window-02/raw.json: adf3476306b2b211b7edf0fbf89d6663a64dc190c4714d41a3407936c6d27a4b
        B/clauses/window-02/prompt.txt: c32cdde48f616dc5b2f2f42ee08d479d27b07b5ecba293fedb7f593f93a93107
        B/clauses/window-02/meta.json: 7ffbf048414768edd608805b0ee310b479b4a213e09de9ad4d89a3b1916da664
        B/clauses/window-15/raw.json: f698b41b2ce058a632ef8de2adccfd1e23ec7dc8c980b53d0c83f6329b018acf
        B/clauses/window-15/prompt.txt: c13ce348e69bfabe55c0387942e197de2d76d6bdcd52dfdc66dabe2ce47e7c98
        B/clauses/window-15/meta.json: e22c53bc2e187c264096fd07825ef30a5c8b4827d31da126b3a05fe11c2d3183
        B/clauses/window-12/raw.json: 4560b0cac36302f0cc640305afdf82bfc38262802bc0d904562391be11e7fb2a
        B/clauses/window-12/prompt.txt: 416cbba3ecf61ff134a3aaac69e3810bd980a01a99f303fe6cc553709fbcafcd
        B/clauses/window-12/meta.json: 692a56711ff8721a1f507cc765cdb888d29322449256e43c040af576448e24fd
        B/clauses/window-22/raw.json: 39b9e1f6b6b691e03877ec9951a16cdd25482f3ccae0ca4b26b0de1e02b446e3
        B/clauses/window-22/prompt.txt: 55c5d0880635c93ab06c050fa7dcf75e666dfc3ffee480e33f706b0e39c6b49c
        B/clauses/window-22/meta.json: 659e802a1d0766d3cc819b2cae791a3f6805da079d92d98ec4aabde098f9bffb
        B/clauses/window-13/raw.json: 3390419cd480b2b75f79ed9b96d9651d9f0d4b2dc20628890de5be4efb0e3cb9
        B/clauses/window-13/prompt.txt: a93fb430227c2f3814322b096530c88a6e86d1b3bfdc2543914202310b506a16
        B/clauses/window-13/meta.json: 8cbc17f1b8d63a8db87013c6de9de68f109131120a3bdff4d0d2c2e7a2ce31f4
        B/clauses/window-14/raw.json: 3d6c3966273e0b9a2f69263f6e58d47042e18115b889caba4bb08438a33c196c
        B/clauses/window-14/prompt.txt: 035d61ebd5e6a5551418fdfdaff706db0a42be0eff53888c17275352bf1b2543
        B/clauses/window-14/meta.json: 07e16d3be5f7c643e7d55cc72f05970593a1e45311505f612632a7c6509ba5f6
        B/clauses/window-09/raw.json: 23e790753a42bd2e5d7f80df8717a8ee92cb662e990f2f0cddbf0f089797224e
        B/clauses/window-09/prompt.txt: 0f7c00302db85ad70041cbcdd5bc38dfb907d422869478603680fcca4abfbccb
        B/clauses/window-09/meta.json: 991dfc0f4f4d3619f621cd84b33154c5b5abe36835c4a6bdbc658da4bd4783b4
        B/clauses/window-07/raw.json: 28f06f443d7e6dff753d34f56483d0c90b108f4e51609b29d288a2a2c50290f1
        B/clauses/window-07/prompt.txt: 5e6cdf426a8cfd6ca4f4cfb9e8380e4c8f9f0ca354d766b59a8c51d9b4489eb3
        B/clauses/window-07/meta.json: 8001e70844b153c12c5a73c6726e1a1e6108f2fcc2f8e2322ecdc18c50057008
        B/clauses/window-01/raw.json: 564592af0c86781355d11f4b8d7a9124a49e3a78a899afab9ebca6b87ef11e9f
        B/clauses/window-01/prompt.txt: ef19fa8fc32910efe4c4cb7384418b4cc5ad4660b811d66911c0dac952142b4e
        B/clauses/window-01/meta.json: 5a63449afba9bde214c401be56ee6b051c15440e2eb0d6df23c4320e3ec8dfe1
        B/clauses/window-06/raw.json: 9284f092fcda5fc594d64cd1f10f22dbdb6ce08076cc9716045b084a2dd5be75
        B/clauses/window-06/prompt.txt: 6ee7becf7a81ed6c748098a783b966823a88aaf6782d10b0cd9f051ed9219971
        B/clauses/window-06/meta.json: d389a7f8b89ab0072415c8e617d50c4f7a04dfa6553895d07ecf9c1771852f86
        B/clauses/window-08/raw.json: cf656f9983fa271319e723e588aa4d9d5b5483cbcd78f6d7a71232fa9aa520af
        B/clauses/window-08/prompt.txt: 8c2419cb038c0ae4ac1d683923bd9756000516e0dd10673621491fb27291c32e
        B/clauses/window-08/meta.json: 8a5cf2b04ca7bfed4a9af216bb76f4ca03805222a0d70c837f7ddf2fa74bf8e4
      code:
        relationship_review.py: ab52eac5603e2f4080aa82e51ec2d579714fe7aeecc6cc376f345c9001157135
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
      pdf_sha256: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
      source_review: _compare/relationships-2026-11-16/review-current/Rapcsak2009
      source_status_sha256: 4d9757cffc6971427447a68e06eba0d88b975d448de749d06f6ba1ba4d3dd3ed
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R014
    exposure:
      text: extrasylvian damage (perisylvian only vs perisylvian plus)
    outcome:
      text: reading/spelling accuracy and phonological ability
    analysis_label: Extrasylvian lesion extension and language performance
    relation: sensitivity
    evidence_ids:
    - P11-S3-C7
    qualifier_ids:
    - P11-S3-C6
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
      source_review: _compare/relationships-2026-11-16/review-current/Rapcsak2009
      source_status_sha256: 4d9757cffc6971427447a68e06eba0d88b975d448de749d06f6ba1ba4d3dd3ed
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P1-S1-C5
      - Result passage disposed without unit P1-S1-C6
      - Accounting without a linked unit P1-S1-C7
      - Result passage disposed without unit P1-S1-C8
      - Unaccounted source passage P1-S1-C7
      - Accounting without a linked unit P4-S4-C2
      - Unaccounted source passage P4-S4-C2
      - Result passage disposed without unit P5-S2-C10
      - Result passage disposed without unit P6-S1-C1
      - Accounting without a linked unit P6-S1-C7
      - Accounting without a linked unit P6-S1-C8
      - Accounting without a linked unit P6-S1-C9
      - Unaccounted source passage P6-S1-C8
      - Unaccounted source passage P6-S1-C7
      - Unaccounted source passage P6-S1-C9
      - Accounting without a linked unit P6-S2-C3
      - Accounting without a linked unit P6-S2-C4
      - Accounting without a linked unit P6-S2-C5
      - Unaccounted source passage P6-S2-C5
      - Unaccounted source passage P6-S2-C3
      - Unaccounted source passage P6-S2-C4
      - Result passage disposed without unit P6-S2-C8
      - Result passage disposed without unit P7-S1-C9
      - Accounting without a linked unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C4
      - Accounting without a linked unit P7-S2-C5
      - Unaccounted source passage P7-S2-C4
      - Unaccounted source passage P7-S2-C5
      - Unaccounted source passage P7-S2-C3
      - Result passage disposed without unit P7-S2-C6
      - Accounting without a linked unit P7-S2-C7
      - Result passage disposed without unit P7-S3-C5
      - Unaccounted source passage P7-S2-C7
      - Result passage disposed without unit P8-S1-C4
      - Result passage disposed without unit P8-S1-C6
      - Accounting without a linked unit P8-S1-C7
      - Accounting without a linked unit P8-S1-C8
      - Accounting without a linked unit P8-S1-C9
      - Unaccounted source passage P8-S1-C8
      - Unaccounted source passage P8-S1-C7
      - Unaccounted source passage P8-S1-C9
      - Result passage disposed without unit P8-S2-C2
      - Accounting without a linked unit P8-S2-C3
      - Unaccounted source passage P8-S2-C3
      - Result passage disposed without unit P8-S2-C10
      - Result passage disposed without unit P8-S2-C8
      - Result passage disposed without unit P8-S2-C9
      - Result passage disposed without unit P8-S2-C11
      - Result passage disposed without unit P8-S3-C4
      - Result passage disposed without unit P8-S3-C5
      - Accounting without a linked unit P8-S3-C6
      - Unaccounted source passage P8-S3-C6
      - Result passage disposed without unit P9-S2-C5
      - Accounting without a linked unit P9-S2-C8
      - Accounting without a linked unit P9-S2-C9
      - Unaccounted source passage P9-S2-C8
      - Unaccounted source passage P9-S2-C9
      - Result passage disposed without unit P10-S2-C5
      - Result passage disposed without unit P10-S3-C2
      - Accounting without a linked unit P11-S1-C2
      - Accounting without a linked unit P11-S1-C5
      - Accounting without a linked unit P11-S1-C6
      - Unaccounted source passage P11-S1-C5
      - Unaccounted source passage P11-S1-C2
      - Unaccounted source passage P11-S1-C6
      - Accounting without a linked unit P11-S3-C3
      - Accounting without a linked unit P11-S3-C4
      - Accounting without a linked unit P11-S3-C5
      - Unaccounted source passage P11-S3-C5
      - Unaccounted source passage P11-S3-C3
      - Unaccounted source passage P11-S3-C4
      - Result passage disposed without unit P12-S1-C2
      - Result passage disposed without unit P12-S1-C6
      - Result passage disposed without unit P12-S1-C7
      - Result passage disposed without unit P12-S1-C8
      - Accounting without a linked unit P12-S2-C3
      - Accounting without a linked unit P12-S2-C4
      - Unaccounted source passage P12-S2-C3
      - Unaccounted source passage P12-S2-C4
      - Result passage disposed without unit P13-S1-C7
      - Result passage disposed without unit P13-S1-C8
      - Result passage disposed without unit P13-S2-C3
      - Result passage disposed without unit P13-S2-C4
      - Result passage disposed without unit P13-S2-C5
      - Result passage disposed without unit P13-S2-C6
      - Result passage disposed without unit P13-S2-C7
      - Accounting without a linked unit P13-S3-C4
      - Unaccounted source passage P13-S3-C4
      - Result passage disposed without unit P14-S4-C3
      - Result passage disposed without unit P15-S1-C2
      unattached_null_or_qualifier_ids:
      - P1-S1-C6
      - P6-S1-C8
      - P6-S1-C9
      - P6-S2-C5
      - P6-S2-C7
      - P7-S2-C3
      - P7-S2-C4
      - P8-S1-C6
      - P8-S1-C8
      - P8-S2-C3
      - P10-S2-C4
      - P11-S1-C2
      - P11-S1-C5
      - P11-S3-C3
      - P12-S1-C8
      - P12-S2-C3
      - P12-S2-C4
      - P15-S1-C4
      suppressed_nonrepresented_units: 31
      default_disposition_count_requires_completeness_check: 220
      unselected_timing_passages:
      - P3-S3-C2
      - P3-S3-C4
      - P3-S3-C11
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C4
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
        source_id: P10-S1-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P11-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P6-S1-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P6-S1-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P13-S2-C5
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysed_sample
        source_ids:
        - P1-S1-C1
        - P3-S1-C1
        - P3-S3-C4
        - P4-S1-C9
        - P4-S1-C10
        - P5-S1-C2
        - P5-S1-C3
        - P5-S2-C11
        - P5-S3-C2
        - P5-S3-C3
        - P6-S1-C3
        - P6-S1-C5
        - P6-S1-C6
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P7-S1-C8
        - P7-S2-C2
        - P8-S1-C3
        - P8-S3-C5
        - P8-S4-C3
        - P9-S1-C2
        - P9-S1-C3
        - P9-S1-C5
        - P9-S2-C4
        - P9-S2-C8
        - P9-S3-C1
        - P9-S3-C2
        - P10-S2-C8
        - P10-S3-C7
        - P11-S3-C2
        - P12-S2-C5
        - P13-S2-C5
        - P13-S3-C4
        - P13-S3-C8
        - P13-S4-C2
        - P13-S4-C3
        - P14-S1-C1
        - P14-S1-C4
        - P14-S1-C6
        - P14-S2-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C1
        - P3-S1-C1
        - P3-S3-C2
        - P4-S1-C9
        - P4-S1-C10
        - P5-S1-C2
        - P5-S1-C3
        - P5-S2-C7
        - P5-S2-C10
        - P6-S1-C6
        - P7-S2-C3
        - P8-S1-C3
        - P8-S3-C3
        - P10-S2-C8
        - P10-S3-C7
        - P11-S3-C2
        - P12-S2-C5
        - P13-S2-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: eligibility
        source_ids:
        - P3-S1-C5
        - P3-S3-C2
        - P3-S3-C3
        - P5-S1-C1
        - P5-S1-C2
        - P5-S1-C3
        - P7-S4-C2
        - P10-S2-C8
        - P13-S2-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P3-S3-C2
        - P4-S2-C10
        - P4-S2-C11
        - P4-S3-C3
        - P4-S3-C4
        - P4-S3-C5
        - P4-S3-C9
        - P10-S2-C8
        - P10-S3-C7
        - P11-S2-C9
        - P11-S4-C1
        - P12-S1-C1
        - P12-S2-C7
        - P15-S1-C1
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C7
        - P1-S2-C2
        - P3-S1-C2
        - P3-S1-C3
        - P3-S4-C2
        - P4-S1-C7
        - P4-S1-C8
        - P4-S2-C9
        - P5-S1-C4
        - P5-S1-C5
        - P5-S1-C10
        - P5-S2-C11
        - P5-S3-C2
        - P5-S3-C3
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P7-S1-C8
        - P7-S2-C2
        - P7-S4-C3
        - P8-S1-C6
        - P8-S3-C6
        - P8-S4-C4
        - P9-S1-C4
        - P9-S1-C5
        - P9-S2-C4
        - P9-S3-C2
        - P9-S3-C3
        - P10-S1-C7
        - P10-S2-C3
        - P11-S1-C4
        - P11-S1-C5
        - P11-S1-C6
        - P11-S2-C4
        - P11-S2-C5
        - P11-S3-C6
        - P12-S2-C5
        - P13-S1-C5
        - P13-S1-C8
        - P13-S3-C4
        - P13-S4-C2
        - P14-S1-C2
        - P14-S1-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P2-S2-C3
        - P2-S2-C4
        - P2-S2-C5
        - P2-S2-C6
        - P2-S3-C2
        - P2-S3-C3
        - P6-S1-C4
        - P8-S2-C7
        - P8-S3-C2
        - P8-S3-C4
        - P10-S3-C3
        - P10-S3-C4
        - P13-S2-C6
        - P13-S2-C7
        - P14-S3-C9
        - P14-S3-C10
        - P14-S4-C2
        - P14-S4-C4
        - P14-S4-C5
        - P15-S1-C1
        - P15-S1-C2
        - P15-S1-C3
        - P15-S2-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P3-S1-C1
        - P3-S3-C4
        - P3-S3-C5
        - P3-S3-C6
        - P3-S3-C7
        - P3-S3-C8
        - P3-S3-C9
        - P3-S3-C11
        - P3-S3-C12
        - P7-S2-C4
        - P8-S2-C5
        - P8-S4-C3
        - P10-S2-C8
        - P11-S2-C7
        - P11-S3-C2
        - P12-S2-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - eligibility
      - imaging_provenance
      - imaging_timing
      - outcome_definition
      - limitations
      - personal_factors
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids:
      - P5-S2-C12
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S1
        - P5-S2
        - P5-S3
        - P6-S2
        - P6-S3
        - P9-S3
        - P10-S1
        - P11-S4
        - P12-S1
        - P12-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
      source_review: _compare/relationships-2026-11-16/review-current/Rapcsak2009
      source_status_sha256: 4d9757cffc6971427447a68e06eba0d88b975d448de749d06f6ba1ba4d3dd3ed
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Abstract statement of lexicality effects in reading and spelling.
    - source_id: P1-S1-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Abstract statement of lexicality effects in oral repetition.
    - source_id: P1-S1-C7
      disposition: represented
      result_indexes:
      - 4
      reason: Abstract statement of PC score predicting reading and spelling.
    - source_id: P1-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about task difficulty effects.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Abstract statement of spelling vulnerability.
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 9
      reason: Abstract statement of distributed network models.
    - source_id: P3-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic data (Aphasia Quotient).
    - source_id: P3-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Demographic comparison (age/education).
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Stimulus list validation.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Stimulus list description.
    - source_id: P4-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of excluded participants.
    - source_id: P5-S1-C5
      disposition: represented
      result_indexes:
      - 0
      reason: ANOVA for reading accuracy by stimulus type.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 0
      reason: Contrasts for reading accuracy.
    - source_id: P5-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Within-group reading comparisons.
    - source_id: P5-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Null finding for controls in reading.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 0
      reason: Overall real word vs non-word reading.
    - source_id: P5-S1-C10
      disposition: represented
      result_indexes:
      - 1
      reason: ANOVA for spelling accuracy by stimulus type.
    - source_id: P5-S2-C2
      disposition: represented
      result_indexes:
      - 1
      reason: Contrasts for spelling accuracy.
    - source_id: P5-S2-C3
      disposition: represented
      result_indexes:
      - 1
      reason: Within-group spelling comparisons.
    - source_id: P5-S2-C4
      disposition: represented
      result_indexes:
      - 1
      reason: Regular vs irregular spelling advantage.
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 1
      reason: Control spelling performance.
    - source_id: P5-S2-C6
      disposition: represented
      result_indexes:
      - 1
      reason: Control regular vs irregular spelling.
    - source_id: P5-S2-C7
      disposition: represented
      result_indexes:
      - 1
      reason: Overall real word vs non-word spelling.
    - source_id: P5-S2-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Exaggerated lexicality effect in reading and spelling.
    - source_id: P5-S3-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Lexicality effect size comparison.
    - source_id: P5-S3-C3
      disposition: represented
      result_indexes:
      - 2
      reason: Null finding for regularity effect size.
    - source_id: P6-S1-C1
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of regularity effect null.
    - source_id: P6-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prevalence of phonological dyslexia.
    - source_id: P6-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of global dyslexia cases.
    - source_id: P6-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of non-significant cases.
    - source_id: P6-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary of reading profiles.
    - source_id: P6-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Continuum of severity description.
    - source_id: P6-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Prevalence of phonological dysgraphia.
    - source_id: P6-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of global dysgraphia cases.
    - source_id: P6-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of other spelling profiles.
    - source_id: P6-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Continuum of severity for spelling.
    - source_id: P6-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on spelling deficits.
    - source_id: P6-S2-C8
      disposition: represented
      result_indexes:
      - 1
      reason: Quantitative difference between reading and spelling vulnerability.
    - source_id: P6-S3-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of spelling vulnerability.
    - source_id: P6-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control group spelling vs reading difference.
    - source_id: P7-S1-C9
      disposition: represented
      result_indexes:
      - 7
      reason: Prevalence of semantic errors.
    - source_id: P7-S2-C2
      disposition: represented
      result_indexes:
      - 7
      reason: Percentage of semantic errors.
    - source_id: P7-S2-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Proportion of participants with semantic errors.
    - source_id: P7-S2-C7
      disposition: represented
      result_indexes:
      - 7
      - 8
      reason: Correlations between accuracy and semantic errors.
    - source_id: P7-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation of reading/spelling profiles.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Individual analysis of concordant profiles.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of discordant profiles.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Explanation of floor effects in spelling.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Criteria for true dissociation.
    - source_id: P8-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of mild written language deficits.
    - source_id: P8-S1-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reliability of non-word reading/spelling differences.
    - source_id: P8-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Identification of complementary dissociations.
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Analysis of a specific discordant case.
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Specific case lexicality effect.
    - source_id: P8-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Identification of single dissociation case.
    - source_id: P8-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case reading performance.
    - source_id: P8-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Case spelling performance.
    - source_id: P8-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Conclusion on double dissociations.
    - source_id: P8-S3-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Correlations between reading and spelling scores.
    - source_id: P8-S4-C4
      disposition: represented
      result_indexes:
      - 3
      reason: ANOVA for oral repetition.
    - source_id: P9-S1-C1
      disposition: represented
      result_indexes:
      - 3
      reason: ANOVA interaction for oral repetition.
    - source_id: P9-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Contrasts for oral repetition.
    - source_id: P9-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Within-group repetition comparisons.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 3
      reason: Lexicality effect size in repetition.
    - source_id: P9-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Task difficulty order (repetition > reading > spelling).
    - source_id: P9-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: PC scores vs controls.
    - source_id: P9-S3-C1
      disposition: represented
      result_indexes:
      - 4
      reason: Correlations between PC and reading/spelling.
    - source_id: P9-S3-C2
      disposition: represented
      result_indexes:
      - 4
      reason: Variance explained by PC scores.
    - source_id: P9-S3-C3
      disposition: represented
      result_indexes:
      - 5
      reason: Correlation between PC and repetition.
    - source_id: P10-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General observation on phonological capacity.
    - source_id: P10-S2-C2
      disposition: repeated
      result_indexes:
      - 1
      reason: Restatement of spelling sensitivity.
    - source_id: P10-S3-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Association of perisylvian damage with phonological dyslexia/dysgraphia.
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Null finding for single critical cortical area.
    - source_id: P11-S1-C5
      disposition: represented
      result_indexes:
      - 10
      reason: Null association between ROI damage and spelling lexicality.
    - source_id: P11-S1-C6
      disposition: represented
      result_indexes:
      - 11
      reason: Association between anterior ROI damage and reading lexicality.
    - source_id: P11-S2-C1
      disposition: represented
      result_indexes:
      - 10
      reason: Comparison of anterior vs posterior lesions in spelling.
    - source_id: P11-S2-C2
      disposition: represented
      result_indexes:
      - 11
      reason: Comparison of anterior vs posterior lesions in reading.
    - source_id: P11-S2-C4
      disposition: represented
      result_indexes:
      - 12
      reason: Correlation between ROI count and reading/spelling impairment.
    - source_id: P11-S2-C5
      disposition: represented
      result_indexes:
      - 12
      reason: Correlation between ROI count and PC scores.
    - source_id: P11-S3-C7
      disposition: represented
      result_indexes:
      - 13
      reason: ANCOVA results for extrasylvian damage.
    - source_id: P12-S1-C7
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Abstract restatement of lexicality effects.
    - source_id: P12-S2-C5
      disposition: repeated
      result_indexes:
      - 4
      reason: Abstract restatement of PC score prediction.
    - source_id: P13-S1-C5
      disposition: repeated
      result_indexes:
      - 1
      reason: Discussion restatement of spelling vulnerability.
    - source_id: P13-S3-C2
      disposition: represented
      result_indexes:
      - 9
      reason: Distributed network model support.
    - source_id: P15-S1-C5
      disposition: repeated
      result_indexes:
      - 13
      reason: Restatement of extrasylvian damage null.
    unresolved_coverage:
    - source_id: P6-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P13-S3-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P5-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P9-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P10-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P11-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P14-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P15-S1-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C5
    - P1-S1-C6
    - P1-S1-C7
    - P1-S1-C8
    - P1-S2-C2
    - P1-S2-C5
    - P3-S3-C7
    - P3-S3-C12
    - P4-S1-C3
    - P4-S1-C6
    - P4-S4-C2
    - P5-S1-C8
    - P5-S2-C5
    - P5-S2-C6
    - P5-S2-C8
    - P5-S2-C9
    - P5-S2-C10
    - P5-S3-C4
    - P6-S1-C1
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S2-C3
    - P6-S2-C4
    - P6-S2-C5
    - P6-S2-C6
    - P6-S2-C7
    - P6-S2-C8
    - P6-S3-C2
    - P6-S3-C5
    - P7-S1-C9
    - P7-S2-C2
    - P7-S2-C3
    - P7-S2-C4
    - P7-S2-C5
    - P7-S2-C6
    - P7-S3-C5
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C6
    - P8-S1-C7
    - P8-S1-C8
    - P8-S1-C9
    - P8-S2-C2
    - P8-S2-C3
    - P8-S2-C4
    - P8-S2-C5
    - P8-S2-C8
    - P8-S2-C9
    - P8-S2-C10
    - P8-S2-C11
    - P8-S3-C4
    - P8-S3-C5
    - P8-S4-C4
    - P9-S2-C3
    - P9-S2-C4
    - P9-S2-C5
    - P9-S2-C8
    - P9-S2-C9
    - P10-S1-C2
    - P10-S1-C3
    - P10-S1-C4
    - P10-S1-C5
    - P10-S1-C6
    - P10-S2-C2
    - P10-S2-C3
    - P10-S2-C4
    - P10-S2-C5
    - P10-S3-C2
    - P11-S1-C8
    - P11-S2-C1
    - P11-S2-C2
    - P11-S3-C3
    - P11-S3-C4
    - P11-S3-C5
    - P12-S1-C2
    - P12-S1-C6
    - P12-S1-C7
    - P12-S1-C8
    - P12-S2-C3
    - P12-S2-C4
    - P12-S2-C5
    - P13-S1-C5
    - P13-S1-C7
    - P13-S1-C8
    - P13-S2-C3
    - P13-S2-C4
    - P13-S2-C5
    - P13-S2-C6
    - P13-S2-C7
    - P13-S3-C4
    - P14-S1-C6
    - P14-S4-C3
    - P15-S1-C2
    - P15-S1-C4
    - P15-S1-C5
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review: []
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
      outcome_timing:
      - P3-S3-C3
      outcome_definition: []
      validation:
      - P3-S2-C6
      analysis_restrictions:
      - P4-S3-C2
      - P7-S4-C3
      - P8-S1-C2
      - P15-S1-C7
      dependent_variable_statement:
      - P3-S1-C2
      - P3-S1-C3
      - P3-S2-C5
      - P4-S1-C7
      limitations: []
      personal_factors: []
      tested_personal_effects:
      - P7-S2-C7
      - P8-S2-C5
      adjustment_roles:
      - P11-S3-C5
      - P11-S3-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: status_at_assessment
    imaging_vs_outcome: precedes_outcome
    validation_type: mixed
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C4
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
      source_id: P10-S1-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P11-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P6-S1-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P6-S1-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P13-S2-C5
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysed_sample
      source_ids:
      - P1-S1-C1
      - P3-S1-C1
      - P3-S3-C4
      - P4-S1-C9
      - P4-S1-C10
      - P5-S1-C2
      - P5-S1-C3
      - P5-S2-C11
      - P5-S3-C2
      - P5-S3-C3
      - P6-S1-C3
      - P6-S1-C5
      - P6-S1-C6
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C5
      - P7-S1-C8
      - P7-S2-C2
      - P8-S1-C3
      - P8-S3-C5
      - P8-S4-C3
      - P9-S1-C2
      - P9-S1-C3
      - P9-S1-C5
      - P9-S2-C4
      - P9-S2-C8
      - P9-S3-C1
      - P9-S3-C2
      - P10-S2-C8
      - P10-S3-C7
      - P11-S3-C2
      - P12-S2-C5
      - P13-S2-C5
      - P13-S3-C4
      - P13-S3-C8
      - P13-S4-C2
      - P13-S4-C3
      - P14-S1-C1
      - P14-S1-C4
      - P14-S1-C6
      - P14-S2-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C1
      - P3-S1-C1
      - P3-S3-C2
      - P4-S1-C9
      - P4-S1-C10
      - P5-S1-C2
      - P5-S1-C3
      - P5-S2-C7
      - P5-S2-C10
      - P6-S1-C6
      - P7-S2-C3
      - P8-S1-C3
      - P8-S3-C3
      - P10-S2-C8
      - P10-S3-C7
      - P11-S3-C2
      - P12-S2-C5
      - P13-S2-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: eligibility
      source_ids:
      - P3-S1-C5
      - P3-S3-C2
      - P3-S3-C3
      - P5-S1-C1
      - P5-S1-C2
      - P5-S1-C3
      - P7-S4-C2
      - P10-S2-C8
      - P13-S2-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P3-S3-C2
      - P4-S2-C10
      - P4-S2-C11
      - P4-S3-C3
      - P4-S3-C4
      - P4-S3-C5
      - P4-S3-C9
      - P10-S2-C8
      - P10-S3-C7
      - P11-S2-C9
      - P11-S4-C1
      - P12-S1-C1
      - P12-S2-C7
      - P15-S1-C1
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C7
      - P1-S2-C2
      - P3-S1-C2
      - P3-S1-C3
      - P3-S4-C2
      - P4-S1-C7
      - P4-S1-C8
      - P4-S2-C9
      - P5-S1-C4
      - P5-S1-C5
      - P5-S1-C10
      - P5-S2-C11
      - P5-S3-C2
      - P5-S3-C3
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C5
      - P7-S1-C8
      - P7-S2-C2
      - P7-S4-C3
      - P8-S1-C6
      - P8-S3-C6
      - P8-S4-C4
      - P9-S1-C4
      - P9-S1-C5
      - P9-S2-C4
      - P9-S3-C2
      - P9-S3-C3
      - P10-S1-C7
      - P10-S2-C3
      - P11-S1-C4
      - P11-S1-C5
      - P11-S1-C6
      - P11-S2-C4
      - P11-S2-C5
      - P11-S3-C6
      - P12-S2-C5
      - P13-S1-C5
      - P13-S1-C8
      - P13-S3-C4
      - P13-S4-C2
      - P14-S1-C2
      - P14-S1-C3
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P2-S2-C3
      - P2-S2-C4
      - P2-S2-C5
      - P2-S2-C6
      - P2-S3-C2
      - P2-S3-C3
      - P6-S1-C4
      - P8-S2-C7
      - P8-S3-C2
      - P8-S3-C4
      - P10-S3-C3
      - P10-S3-C4
      - P13-S2-C6
      - P13-S2-C7
      - P14-S3-C9
      - P14-S3-C10
      - P14-S4-C2
      - P14-S4-C4
      - P14-S4-C5
      - P15-S1-C1
      - P15-S1-C2
      - P15-S1-C3
      - P15-S2-C2
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P3-S1-C1
      - P3-S3-C4
      - P3-S3-C5
      - P3-S3-C6
      - P3-S3-C7
      - P3-S3-C8
      - P3-S3-C9
      - P3-S3-C11
      - P3-S3-C12
      - P7-S2-C4
      - P8-S2-C5
      - P8-S4-C3
      - P10-S2-C8
      - P11-S2-C7
      - P11-S3-C2
      - P12-S2-C5
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
      pdf_sha256: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
      review_sha256: 0988d0022f0e697b7c73b644ce317bd5eaa909feca6dffd6865086c6e23bc6ce
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
      - P11-S3-C7
      source_result: ANCOVAs comparing 'perisylvian only' vs 'perisylvian plus' groups
        on reading, spelling, and phonological ability, controlling for the number
        of damaged perisylvian ROIs, found no significant differences between the
        groups on any of these measures.
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The source (P11-S3-C6, P11-S3-C7) describes ANCOVAs with group (perisylvian
            only vs plus) as factor and number of damaged perisylvian ROIs as covariate.
            The draft correctly identifies this specific analysis.
          source_ids:
          - P11-S3-C6
          - P11-S3-C7
        direction:
          answer: fits
          reason: The source states 'no significant differences' (P11-S3-C7). The
            draft claims 'no significant differences' and direction 'no_effect'. This
            is a faithful representation of a null result.
          source_ids:
          - P11-S3-C7
        construct:
          answer: fits
          reason: Exposure is extrasylvian damage (perisylvian only vs plus), outcome
            is reading/spelling/phonological ability. The method is correctly identified
            as ANCOVA (though the draft label 'LSM' is imprecise, the claim text is
            accurate). The patient measurement is template_lesion_overlap (lesions
            mapped to template to determine extrasylvian extension).
          source_ids:
          - P11-S2-C9
          - P11-S3-C2
          - P11-S3-C6
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the analysis
            controlled for the number of damaged perisylvian regions (P11-S3-C6).
            It also includes limitations regarding retrospective design and mixed
            scan types (P14-S3-C10, P15-S1-C1).
          source_ids:
          - P11-S3-C6
          - P14-S3-C10
          - P15-S1-C1
        missing_material_caveat:
          answer: fits
          reason: The draft captures the main caveats. The 'new_model_candidate_not_verified'
            flag is a system status, not a source caveat. The source notes that the
            'perisylvian plus' group had more extensive perisylvian damage (P11-S3-C3),
            which is why the covariate was used; the draft correctly reflects the
            adjusted nature of the result.
          source_ids:
          - P11-S3-C3
          - P11-S3-C5
      optional_pending:
      - Specific p-values or effect sizes for the ANCOVAs are not transcribed in the
        draft, but the qualitative null result is clear.
      - Exact sample sizes for the ANCOVA subgroups (n=13 vs n=18) are mentioned in
        source P11-S3-C2 but not explicitly in the draft claim, though the population
        is correctly identified.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific p-values or effect sizes for the ANCOVAs are not transcribed in the
      draft, but the qualitative null result is clear.
    - Exact sample sizes for the ANCOVA subgroups (n=13 vs n=18) are mentioned in
      source P11-S3-C2 but not explicitly in the draft claim, though the population
      is correctly identified.
    normalizations:
    - field: sample.n
      original: 31
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R014
      exposure:
        text: extrasylvian damage (perisylvian only vs perisylvian plus)
      outcome:
        text: reading/spelling accuracy and phonological ability
      analysis_label: Extrasylvian lesion extension and language performance
      relation: sensitivity
      evidence_ids:
      - P11-S3-C7
      qualifier_ids:
      - P11-S3-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
        source_review: _compare/relationships-2026-11-16/review-current/Rapcsak2009
        source_status_sha256: 4d9757cffc6971427447a68e06eba0d88b975d448de749d06f6ba1ba4d3dd3ed
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P11-S3-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: d5b4c9a810683c223ce6e555e75003d86aeb76efcc64f6e8157811003176914c
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P11-S3-C2
          page: 11
          text_layer_sha256: d5b4c9a810683c223ce6e555e75003d86aeb76efcc64f6e8157811003176914c
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Based on this information, we subdivided patients into

          two groups: the ‘‘perisylvian only’’ group included individuals

          whose lesions showed no or minimal extension outside the

          perisylvian region (n ¼ 13), whereas the ‘‘perisylvian plus’’

          group included participants with evidence of more substantial

          extrasylvian damage (n ¼ 18).'
        anchor_text: 'Based on this information, we subdivided patients into

          two groups: the ‘‘perisylvian only’’ group included individuals

          whose lesions showed no or minimal extension outside the

          perisylvian region (n ¼ 13), whereas the ‘‘perisylvian plus’’

          group included participants with evidence of more substantial

          extrasylvian damage (n ¼ 18).'
        excluded_fragments: []
        image_sha256: d342a36e74980dd54d91a63f5a079e5c48dcda3b512c000a36543fd9d39e49d8
      P3-S3-C3:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 09414ee70b25f37d4179040d32f1be58fda8ab6d741f76ba735a2f45b9636c3f
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C3
          page: 3
          text_layer_sha256: 09414ee70b25f37d4179040d32f1be58fda8ab6d741f76ba735a2f45b9636c3f
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'To be included, participants had to fulﬁll the following

          selection criteria: (1) CT or MRI evidence of damage to one or

          more perisylvian cortical regions implicated in phonological

          processing, including posterior inferior frontal gyrus/Broca’s

          area (BA44/45), precentral gyrus (BA4/6), insula, superior tem-

          poral gyrus/Wernicke’s area (BA22), and supramarginal gyrus

          (BA40), and (2) having received a detailed evaluation of reading

          and spelling performance in the subacute or chronic stage of

          their illness (typically several months or years post-onset).'
        anchor_text: 'To be included, participants had to fulﬁll the following

          selection criteria: (1) CT or MRI evidence of damage to one or

          more perisylvian cortical regions implicated in phonological

          processing, including posterior inferior frontal gyrus/Broca’s

          area (BA44/45), precentral gyrus (BA4/6), insula, superior tem-

          poral gyrus/Wernicke’s area (BA22), and supramarginal gyrus

          (BA40), and (2) having received a detailed evaluation of reading

          and spelling performance in the subacute or chronic stage of

          their illness (typically several months or years post-onset).'
        excluded_fragments: []
        image_sha256: 5e32c37945f383b882fbdfeb51e084b978e3e462e412b6a54ccac3558e732a65
        transcription: '. To be included, participants had to fulfill the following

          selection criteria: (1) CT or MRI evidence of damage to one or

          more perisylvian cortical regions implicated in phonological

          processing, including posterior inferior frontal gyrus/Broca’s

          area (BA44/45), precentral gyrus (BA4/6), insula, superior tem-

          poral gyrus/Wernicke’s area (BA22), and supramarginal gyrus

          (BA40), and (2) having received a detailed evaluation of reading

          and spelling performance in the subacute or chronic stage of

          their illness (typically several months or years post-onset)'
      P3-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 58e213f19cb82d4d4a5b76c65c7a2024dd9e00c64644c6625ec3d4ad13901921
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 032ee7c927ee3ecc6a7bcfe0aa7936f2b371e93b1f789061b92d77a8c1f0ccd7
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P3-S3-C4
          page: 3
          text_layer_sha256: 032ee7c927ee3ecc6a7bcfe0aa7936f2b371e93b1f789061b92d77a8c1f0ccd7
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'Us-

          ing these dual criteria, we were able to identify 31 participants

          for the study (mean age ¼ 60.07 years, range: 40–78; average

          years of education ¼ 14.55, range: 11–20).'
        anchor_text: 'Us-

          ing these dual criteria, we were able to identify 31 participants

          for the study (mean age ¼ 60.07 years, range: 40–78; average

          years of education ¼ 14.55, range: 11–20).'
        excluded_fragments: []
        image_sha256: fc5f1668328825e79fe1624a4413b99555666baaf0b0145d900f4e8cc46b4edf
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 11
  quote: 'Based on this information, we subdivided patients into

    two groups: the ‘‘perisylvian only’’ group included individuals

    whose lesions showed no or minimal extension outside the

    perisylvian region (n ¼ 13), whereas the ‘‘perisylvian plus’’

    group included participants with evidence of more substantial

    extrasylvian damage (n ¼ 18).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
