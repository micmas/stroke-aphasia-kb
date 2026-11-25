---
id: within_network_intrahemispheric_connectivity
name: within-network intrahemispheric connectivity cluster
kind: network
findings:
- id: f1
  target: stroke_status
  target_kind: impairment
  claim: Within-network intrahemispheric connectivity was not significantly changed
    in both the ipsilesional and contralesional hemispheres when comparing stroke
    patients to age-matched controls.
  direction: no_effect
  relationship: correlational
  method: rs_fMRI
  sample:
    n: not_reported
    population: subacute first-time symptomatic stroke patients and age-matched controls
    phase: not_reported
    time_post_onset: 1-2 weeks post-stroke onset
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Cortical parcellation excluded the cerebellum and basal ganglia
  - Parcellation was originally generated on young adults (18-33 years) and applied
    to a broader age range (21-83 years)
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Resting-state functional connectivity (FC) measured
    between parcels within the same network located in the same hemisphere, using
    a 324-region cortical parcellation. Analysis compared 100 stroke patients and
    27 age-matched controls; Results were consistent regardless of whether global
    signal regression was used or replaced by CompCor. Additional metadata has not
    been transcribed; review the pending-field flags before approval. PDF image reading
    (P2-S1-C12, two-model agreement, human verification pending): . After exclusion,
    100 stroke patients and 27

    age-matched controls were studied Original text-layer quotation is preserved below.
    PDF image reading (P2-S1-C9, two-model agreement, human verification pending):
    We recruited 132 first-time symptomatic stroke patients 1–2 wk after stroke, and
    31 demographically matched controls Original text-layer quotation is preserved
    below. PDF image reading (P2-S1-C2, two-model agreement, human verification pending):
    We evaluated these predictions within a clinically relevant sample, i.e., a large
    population of subacute stroke patients (n = 132) shown to be representative of
    a larger clinical population Original text-layer quotation is preserved below.'
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
    - proposed_concept:stroke_status
  citation: '@Siegel2016'
  source_passages:
  - section: Original source P2-S2-C9
    page: 2
    quote: 'By con-

      trast, within-network intrahemispheric connectivity was not sig-

      nificantly changed in both the ipsilesional and contralesional

      hemispheres (Fig. 1 B and C).'
    supports: claim
  - section: Original source P2-S1-C12
    page: 2
    quote: 'After exclusion, 100 stroke patients and 27

      age-matched controls were studied.'
    supports: sample
  - section: Original source P2-S1-C9
    page: 2
    quote: 'We recruited 132 first-time symp-

      tomatic stroke patients 1–2 wk after stroke, and 31 demographi-

      cally matched controls.'
    supports: sample
  - section: Original source P2-S1-C2
    page: 2
    quote: 'We evaluated these predictions within a clinically relevant

      sample, i.e., a large population of subacute stroke patients (n =

      132) shown to be representative of a larger clinical population.'
    supports: sample
  - section: Original source P2-S1-C4
    page: 2
    quote: 'Structural magnetic resonance imaging (MRI) and resting func-

      tional magnetic resonance imaging (R-fMRI) were used to mea-

      sure lesion topography, and functional connectivity (FC) of brain

      networks, respectively.'
    supports: method
  - section: Original source P2-S2-C3
    page: 2
    quote: 'A cortical

      parcellation of 324 regions was divided into 13 networks based

      on Gordon et al. (25) (Figs. S1 and S2).'
    supports: method
  - section: Original source P2-S2-C11
    page: 2
    quote: 'We found that functional connectivity analyses

      conducted without global signal regression produced highly

      similar results (Fig. S3).'
    supports: claim
  - section: Original source P7-S1-C5
    page: 7
    quote: 'However, data

      from the cerebellum and basal ganglia were not included in this

      parcellation.'
    supports: limitation
  - section: Original source P8-S4-C3
    page: 8
    quote: 'Notably, the parcellation was gener-

      ated on young adults age 18–33 and is applied here to adults age 21–83.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: Siegel2016
  proposal_id: R005
  review_status_sha256: 03e75b5c1c65071410bb6c69d75bbabfd12690c0e3d38162f959864342a6fa62
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
        A/passages.json: 2dab02426cbbbae44033facb4591b9a9c714d67f6f73ca10cac2d111f710bccb
        A/raw.json: 61819a49c36d7c04d37843d242ddf632dd9e66f5a348b5d51dffb1c578fbe05e
        A/source-units.json: 09f46445a08e930d5965ea4f6aad1f741e4affdf91a609df14d9fc0d691fbc7e
        A/full-source-units.json: 09f46445a08e930d5965ea4f6aad1f741e4affdf91a609df14d9fc0d691fbc7e
        A/meta.json: 6ee05d140be71ec311dcdff9beee6841c368c27d9c1b6825d6ea4c45c339f425
        A/table-images/manifest.json: 588054c782479884058fca740eee6561251e3617a041e603803bbd5e15ae8256
        A/clauses/window-11/raw.json: 5282222879b7a417f674f23442cec4f370e0085c40d720ddd88f468537eed02c
        A/clauses/window-11/prompt.txt: 6e943de065d3168cc8e1c30823a16d769c79a82e584f19ca683f616b414fa457
        A/clauses/window-11/meta.json: 0f60fa5361cf3ccb566a5a1ba5e3fb861ecde007af7604d61d6fb8f43d2ec8dd
        A/clauses/window-16/raw.json: f45dbc170fce58439530d846601f3945bef40cdb9a17ecbd6cd631de3315a994
        A/clauses/window-16/prompt.txt: 43ec316b80ed1bbf3935a806f427f646e7c3c40204ad48537598f4fda522d1f9
        A/clauses/window-16/meta.json: 80c4d393bf34dedbd6d2c14e3780094ad7bd32fbb51fad20b383b77f563d3e67
        A/clauses/window-18/raw.json: 3af53340109dca55b5db6efc1c8a8f2b5bc315b838f074e212dd344e56a21de9
        A/clauses/window-18/prompt.txt: 040936ec81a956ad8cc7e3771e68fe62c30bb52a1f880df0e8c1dac2bd2fcdda
        A/clauses/window-18/meta.json: bcde4014490b59fd4a1dc43368a6bb653e3fe90a3d2244001b6aea9add87ad7b
        A/clauses/window-17/raw.json: a8eabaf8984aec3f07c34e37dd552e4385b9dd2b4b5dfef781c0555ce201c20b
        A/clauses/window-17/prompt.txt: e336d9ae6e7b13922974557c834c5c6dc14ab0acc4c1ad9256a98659d5a018f6
        A/clauses/window-17/meta.json: 44cbb6717ecab30a8e0127a23012c99749cd91000dff7431f71087106d3bb54f
        A/clauses/window-10/raw.json: 375e1e457335246af6f67670998951c2e404a1029bfa3ca0b1b6e1dce3320e60
        A/clauses/window-10/prompt.txt: 7d2ba42fc316c0e32ea8319fdc28778e9578d91fbe0477d3babf1a14540eca76
        A/clauses/window-10/meta.json: ca1e9d8afe8e6507c510a9a8f433b6f878b262ec2dafe39a99c5e11a27180bcc
        A/clauses/window-03/raw.json: 602a3af071dc9aba046119fbc7bd48479cca4b9f07b07635558b349b415f894d
        A/clauses/window-03/prompt.txt: 6c1a4514089dbac3b936a1e96cfefd5361e2ddfdf376f7142a2de76cc335868d
        A/clauses/window-03/meta.json: 1f00e28eb94af8f2042c8bea3b2ecc8b5095c83354b8667572e253e231235b7b
        A/clauses/window-04/raw.json: b5d40bd7366c84ce30fc16eee4694be2939d5cf112f4b53a2aae1c38eb41bced
        A/clauses/window-04/prompt.txt: c2d54618d064254cc2e7d694333efb7d66092fbbcbd6ba6a480d74b1adbc5a6f
        A/clauses/window-04/meta.json: 3439b7cdab12913c127b2605ec92c6de49289e75855acfdd29fc0794fb69dc36
        A/clauses/window-05/raw.json: c5b3c19639f8dabf1031a9d0d8f50ea589562383b95e1c21cd84a7ad27a1d848
        A/clauses/window-05/prompt.txt: 246918598d9c22d46d5e2f8b2cfd1728842807c3789e6549e538482f0c6169a5
        A/clauses/window-05/meta.json: 872e59969d132ba18c986a575a7d22db22ba14125013c99af68a65517ddf7403
        A/clauses/window-02/raw.json: 1cdf85c13a9169e87c517ca13d67847d01526a39ad610d2ab5b8c3dbbdd58283
        A/clauses/window-02/prompt.txt: a5106f3026d1c22b6c271950009c4de5f6addbe2f785150124d1b813405b9bf2
        A/clauses/window-02/meta.json: 0c5ece5822ffaaa052770a537f5f4e9b8fef0abb851eb7b96c73df3ada6e850b
        A/clauses/window-15/raw.json: 11f0e51534564acccbc5f63d4cfa986202983e8c4a640468ff0a80c2b94591f9
        A/clauses/window-15/prompt.txt: 013bad527515b27c700c08c05eef155d48ea80edd6b356475ccb0cadc3fbc639
        A/clauses/window-15/meta.json: 9488587751e3ae2801375183ad8d2252715dba44752dc68a63be87de61a6587d
        A/clauses/window-12/raw.json: 6f907711a8c1cc1cefd5a5e01293045d314e40fc81e3e61b5ee6289c091942a1
        A/clauses/window-12/prompt.txt: 482f269b736004dded797052ec7b991a012f528dc8cdb7746e53fef05ec1e748
        A/clauses/window-12/meta.json: 60369e4ff71755f00b6f8b05a40983410e7d6a1df85ff0ba8f16e4e52b798847
        A/clauses/window-13/raw.json: 61ab0dc951c534afa9ddc3e8e68b16d77ed701f8ec0d0344b252b87acb91c21f
        A/clauses/window-13/prompt.txt: ab05df6ee1208958fb516eff2248a565302c6cd654f88971fb5dbed178fe3323
        A/clauses/window-13/meta.json: 19da8871adae074c190bd3866fa683ef6aae8d55d2379686e71cfb7816efc764
        A/clauses/window-14/raw.json: d082b03fedc69537e9268e006bfc62a63ef13641e4cfa1dccf77f1b37c990103
        A/clauses/window-14/prompt.txt: 6c3a64101940a78f5f706d5983a1a385b65c8115bcea43379438683712025ff7
        A/clauses/window-14/meta.json: bcd9c433203ff919816796ef591023de419d680aa601327c14f4e91749b931d0
        A/clauses/window-09/raw.json: 62d1a652b76873429f163e7239691ca83899e9061e077ee9fae441a1f3de5728
        A/clauses/window-09/prompt.txt: a9311293b342c79381f8c113036905554aadabcad3b7545376e883de706e085f
        A/clauses/window-09/meta.json: d2e5eaf9fac3c4231304c984387c446180efda771b8c73feabf451924ca12900
        A/clauses/window-07/raw.json: e835a17c5d770618e3ca91cc11615146cf470444f6e35b42440fe622bc0fb17e
        A/clauses/window-07/prompt.txt: 224d7c7e097f9283aed5a751757745dd9ab764bd544262cd30283d36f3901e5e
        A/clauses/window-07/meta.json: a5316b9b3aaa9edd4be7df036dc469e731e9ea88c4334e84d44988bfc68fa67c
        A/clauses/window-01/raw.json: e77a9b0aed8813b3d9fcdc48150504c6ad5c4fab17a6a162f750bc875e26efa0
        A/clauses/window-01/prompt.txt: ac4ee42050b22ca9b18b8fa71a5ff7f12f216808988561391a1d471e7e10ff75
        A/clauses/window-01/meta.json: 5a103cf055f8dd0b908bf5350b61d34302a87af172c2e59bbc4d22421a9d9feb
        A/clauses/window-06/raw.json: 548fd2b0e65729becbd17f2ab2cf1f0a2e5060025c7307785e302735e849cbda
        A/clauses/window-06/prompt.txt: dbb2a0e52501d9b7099c62c13fcd02edf0ae99e977ccf97ee2cbea121d8bd9bf
        A/clauses/window-06/meta.json: 24eaec1c461ab8335ba611995796fe37488f675193e51ae621cb5d2d98d29b7c
        A/clauses/window-08/raw.json: 641325a0b807ae3f32bfffbb7cac7e503d32d4c45ac3c95e1e4f132a3fe94963
        A/clauses/window-08/prompt.txt: 0c1b1f432dc8779064133dbeefa5009e1228c4cfb481413d8271f4311f5a122d
        A/clauses/window-08/meta.json: a696ff0cda4bd141d5bc81a361eb9b4903621a8b14ae22e0e2cc4570560072a9
        B/passages.json: 2dab02426cbbbae44033facb4591b9a9c714d67f6f73ca10cac2d111f710bccb
        B/raw.json: ebe6f1724f8c3f56d0add97e15f0b46bbf381f4cc40ac4d8a42c4180c4de242b
        B/source-units.json: 09f46445a08e930d5965ea4f6aad1f741e4affdf91a609df14d9fc0d691fbc7e
        B/full-source-units.json: 09f46445a08e930d5965ea4f6aad1f741e4affdf91a609df14d9fc0d691fbc7e
        B/meta.json: 0fc0f5c62ce749d3d4a602f9284b80256bb82d8e0580d0171f780ea1a74a84ee
        B/table-images/manifest.json: 588054c782479884058fca740eee6561251e3617a041e603803bbd5e15ae8256
        B/clauses/window-11/raw.json: 5282222879b7a417f674f23442cec4f370e0085c40d720ddd88f468537eed02c
        B/clauses/window-11/prompt.txt: 6e943de065d3168cc8e1c30823a16d769c79a82e584f19ca683f616b414fa457
        B/clauses/window-11/meta.json: 5d7cd2043c57eae21e91bef561fb31d214ddb6bdf1a2e2fe601d0d31549e45a5
        B/clauses/window-16/raw.json: f1fd9329e52c9c32983d23cab65d62f4c97b8932d8879231130b30b560cb6ffa
        B/clauses/window-16/prompt.txt: 43ec316b80ed1bbf3935a806f427f646e7c3c40204ad48537598f4fda522d1f9
        B/clauses/window-16/meta.json: 2c64e8a11d4e3f4c9272257780a4a63a8061d81dbdb5a916bd7d48e0985fe477
        B/clauses/window-18/raw.json: a366fa6ccebfc0d91b210072d384ef87adeaaa323873e3ff855b72751eb4f6c9
        B/clauses/window-18/prompt.txt: 040936ec81a956ad8cc7e3771e68fe62c30bb52a1f880df0e8c1dac2bd2fcdda
        B/clauses/window-18/meta.json: a7decc74c625f7dfd06fe8ed77a615c79bec1461dfee09f927cbb1ecffb87d89
        B/clauses/window-17/raw.json: ccceab39d96be2a625f30339f2037cb273289087608899a4b07039ede3475f1f
        B/clauses/window-17/prompt.txt: e336d9ae6e7b13922974557c834c5c6dc14ab0acc4c1ad9256a98659d5a018f6
        B/clauses/window-17/meta.json: a5ae7b6799b0100efc606c6b9cf0ab5296af90d9127b940d76342d8b125c6675
        B/clauses/window-10/raw.json: 65f32e35c2bdb948559ec0536b5cd3ce5c6f3e5f14a547f651760b6a19232aea
        B/clauses/window-10/prompt.txt: 7d2ba42fc316c0e32ea8319fdc28778e9578d91fbe0477d3babf1a14540eca76
        B/clauses/window-10/meta.json: aceaa02ce25cf34a8aa82afc5846b877d4e3b81bf34dd7d2c322f9f5819e675e
        B/clauses/window-03/raw.json: b723cf8e20116450eafb9913a1e7d922ebcaa50486675a84f3c308cee6a1115d
        B/clauses/window-03/prompt.txt: 6c1a4514089dbac3b936a1e96cfefd5361e2ddfdf376f7142a2de76cc335868d
        B/clauses/window-03/meta.json: 78662feb5dad32470597bffaf19136951fb1a4b415843f76cd2c98ecc8eb0a11
        B/clauses/window-04/raw.json: b4d2f04e8443d7c6e0b80717e29fd0a0b3f1315e734ce8aa9f1a28f7118b5f78
        B/clauses/window-04/prompt.txt: c2d54618d064254cc2e7d694333efb7d66092fbbcbd6ba6a480d74b1adbc5a6f
        B/clauses/window-04/meta.json: 0d65aaf34beb6df65b8903fc6eef399f190e61aa8f3baf81eefe621b6b6357e5
        B/clauses/window-05/raw.json: f1341be1ae2ae51314640246b0b1c2c417f02c756831bc660bfdd1872694402a
        B/clauses/window-05/prompt.txt: 246918598d9c22d46d5e2f8b2cfd1728842807c3789e6549e538482f0c6169a5
        B/clauses/window-05/meta.json: d48fa0352899a24dc2d16ee43b31b8111d42a7f291cdcd47851ad61772ddc6f8
        B/clauses/window-02/raw.json: 5171a7fbc185f2c47e61732af0dc6bf5867d729f89928e91da9211890025c8d8
        B/clauses/window-02/prompt.txt: a5106f3026d1c22b6c271950009c4de5f6addbe2f785150124d1b813405b9bf2
        B/clauses/window-02/meta.json: f02f45863dcaf16d785bc762eba0571c76aec214882925326abefb7bad402e7e
        B/clauses/window-15/raw.json: e3e0a1d48097b0e0babd2cf22015fa601d7fc4bb1fa50b448f55803469e9b33c
        B/clauses/window-15/prompt.txt: 013bad527515b27c700c08c05eef155d48ea80edd6b356475ccb0cadc3fbc639
        B/clauses/window-15/meta.json: bd8185230b2560881b593191175429f9ad3b1194d2d9e2eac4815ef36fd069bc
        B/clauses/window-12/raw.json: d339f057857d440744751c5581673b49016486e61f79039af12935b152dcdcfb
        B/clauses/window-12/prompt.txt: 482f269b736004dded797052ec7b991a012f528dc8cdb7746e53fef05ec1e748
        B/clauses/window-12/meta.json: f6611925720fd8d3e03772c99b41971c95bed0cbd4278e16a12694081347b8c2
        B/clauses/window-13/raw.json: 40f42afddbed125692b6efb111439fb828a95fb24013ec1c84540a73a115ce84
        B/clauses/window-13/prompt.txt: ab05df6ee1208958fb516eff2248a565302c6cd654f88971fb5dbed178fe3323
        B/clauses/window-13/meta.json: dcbdedce76e5f7f942f24dbf97002fa6609252014d5211678cca4b4856e8e647
        B/clauses/window-14/raw.json: b39d9d7c45495bdad50079f2767299b6bb4075b09339a0e6b882cc57c67c8c49
        B/clauses/window-14/prompt.txt: 6c3a64101940a78f5f706d5983a1a385b65c8115bcea43379438683712025ff7
        B/clauses/window-14/meta.json: 2b6e624dba60a7ca005ce162615f730d12e14cf552f007edc84f3d834ebfb960
        B/clauses/window-09/raw.json: 345294ff8de259c2a70230995b4e4787c91217e9ae8545e46150ce0e1bf96c18
        B/clauses/window-09/prompt.txt: a9311293b342c79381f8c113036905554aadabcad3b7545376e883de706e085f
        B/clauses/window-09/meta.json: 06f1d627ed4b66c6442e52ff4648eaffedbb209c09eb391c9f8990761ecfebdc
        B/clauses/window-07/raw.json: ed2ea7611536c759cf511d8ffc7e7190295ce34d92ec1c750c1f51eb79c8a1cd
        B/clauses/window-07/prompt.txt: 224d7c7e097f9283aed5a751757745dd9ab764bd544262cd30283d36f3901e5e
        B/clauses/window-07/meta.json: c8a2f4027df5e0d651b55367489d7664532774b312fd76ddf96c5f0ffd934a88
        B/clauses/window-01/raw.json: aea486aa587e7f9329f7ea725d2bc46c0f18b80ce29b2929c1339e4c71150ff2
        B/clauses/window-01/prompt.txt: ac4ee42050b22ca9b18b8fa71a5ff7f12f216808988561391a1d471e7e10ff75
        B/clauses/window-01/meta.json: 6590f672e909384d7a63116102176b83e208394f7e921057c7cf90fb964d8299
        B/clauses/window-06/raw.json: b80ea2797f94f6f7b7200f5be49742b42876bddb3f9e4ee238187b5f68a718fb
        B/clauses/window-06/prompt.txt: dbb2a0e52501d9b7099c62c13fcd02edf0ae99e977ccf97ee2cbea121d8bd9bf
        B/clauses/window-06/meta.json: 500262233ef63781afcf939d7fbaa4463c550fae081ef847d64de5a74f804dbf
        B/clauses/window-08/raw.json: de3c698f523db6a03ac41b8a0f453713f465da58a2b64c35590934ada0cfcd53
        B/clauses/window-08/prompt.txt: 0c1b1f432dc8779064133dbeefa5009e1228c4cfb481413d8271f4311f5a122d
        B/clauses/window-08/meta.json: 8edd85fb7bc99b02addff7b0af8bfba86cd19a13285864fb9b3a566675c9fef3
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
      pdf_sha256: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
      source_review: _compare/relationships-2026-11-16/review-current/Siegel2016
      source_status_sha256: 481e97225cd277541b9f139d96058fce3f26ad1bf402be1338560c4a840c73e8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R005
    exposure:
      text: stroke
    outcome:
      text: within-network intrahemispheric connectivity
    analysis_label: Group Comparison (FC Patterns)
    relation: association
    evidence_ids:
    - P2-S2-C9
    - P2-S3-C12
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
      pdf_sha256: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
      source_review: _compare/relationships-2026-11-16/review-current/Siegel2016
      source_status_sha256: 481e97225cd277541b9f139d96058fce3f26ad1bf402be1338560c4a840c73e8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - 'window 1: invalid/duplicate disposition P1-S1-C15'
      - Result passage disposed without unit P1-S1-C18
      - 'window 2: invalid/duplicate disposition P1-S1-C19'
      - Result passage disposed without unit P1-S1-C19
      - Result passage disposed without unit P2-S2-C11
      - Result passage disposed without unit P2-S2-C13
      - Accounting without a linked unit P2-S3-C3
      - Unaccounted source passage P2-S3-C3
      - Result passage disposed without unit P2-S3-C4
      - Result passage disposed without unit P3-S1-C1
      - Result passage disposed without unit P3-S2-C2
      - Accounting without a linked unit P3-S2-C3
      - Accounting without a linked unit P3-S2-C4
      - Accounting without a linked unit P3-S2-C5
      - Unaccounted source passage P3-S2-C3
      - Unaccounted source passage P3-S2-C5
      - Unaccounted source passage P3-S2-C4
      - Result passage disposed without unit P4-S1-C5
      - Result passage disposed without unit P4-S1-C6
      - 'window 13: invalid/duplicate disposition P4-S1-C13'
      - Result passage disposed without unit P4-S1-C13
      - Accounting without a linked unit P4-S2-C7
      - Accounting without a linked unit P4-S2-C8
      - Unaccounted source passage P4-S2-C7
      - Unaccounted source passage P4-S2-C8
      - Result passage disposed without unit P5-S1-C7
      - 'window 16: invalid/duplicate disposition P5-S1-C9'
      - Result passage disposed without unit P5-S1-C9
      - Result passage disposed without unit P5-S1-C16
      - Result passage disposed without unit P5-S2-C11
      - Result passage disposed without unit P5-S3-C7
      - Result passage disposed without unit P6-S1-C9
      - Result passage disposed without unit P7-S2-C5
      - Result passage disposed without unit P7-S2-C6
      - Result passage disposed without unit P7-S2-C7
      - Result passage disposed without unit P7-S4-C6
      - Accounting without a linked unit P7-S4-C7
      - Accounting without a linked unit P7-S4-C8
      - Accounting without a linked unit P7-S4-C9
      - Unaccounted source passage P7-S4-C8
      - Unaccounted source passage P7-S4-C9
      - Unaccounted source passage P7-S4-C7
      - Result passage disposed without unit P7-S4-C17
      - Result passage disposed without unit P7-S5-C10
      unattached_null_or_qualifier_ids:
      - P2-S2-C13
      - P2-S4-C5
      - P5-S2-C11
      - P7-S2-C2
      - P7-S2-C6
      suppressed_nonrepresented_units: 22
      default_disposition_count_requires_completeness_check: 415
      unselected_timing_passages:
      - P2-S1-C2
      - P7-S2-C13
      - P7-S2-C15
      - P7-S3-C3
      - P7-S3-C7
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S1-C16
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S1-C17
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S3-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P1-S4-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S2-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P2-S3-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P3-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S1-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P4-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P5-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S4-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S4-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S4-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S4-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S4-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S3-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C13
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C15
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S4-C17
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S5-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S5-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S5-C16
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P9-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P3-S1-C9
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S2-C2
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P4-S1-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P9-S2-C4
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: tested_personal_effects
        source_id: P2-S3-C5
        reason: No current-result classification; a covariate description is not an
          individual test
      - slot: analysed_sample
        source_ids:
        - P1-S1-C15
        - P1-S3-C11
        - P1-S4-C2
        - P2-S1-C12
        - P2-S3-C8
        - P3-S1-C14
        - P3-S2-C1
        - P5-S1-C10
        - P7-S3-C3
        - P7-S3-C7
        - P8-S2-C9
        - P8-S3-C11
        - P8-S4-C10
        - P9-S2-C4
        - P10-S1-C16
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C15
        - P1-S3-C11
        - P2-S1-C9
        - P2-S3-C8
        - P7-S2-C13
        - P7-S2-C14
        - P7-S2-C15
        - P7-S3-C4
        - P7-S3-C7
        - P8-S2-C9
        - P8-S3-C11
        - P10-S1-C16
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P1-S1-C15
        - P2-S1-C4
        - P3-S1-C9
        - P4-S2-C14
        - P6-S3-C16
        - P7-S5-C3
        - P7-S5-C4
        - P8-S1-C4
        - P8-S1-C5
        - P8-S1-C6
        - P8-S1-C7
        - P8-S1-C8
        - P8-S2-C13
        - P8-S2-C14
        - P8-S3-C3
        - P8-S3-C13
        - P8-S3-C14
        - P8-S5-C7
        - P9-S2-C3
        - P10-S1-C16
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C15
        - P1-S1-C16
        - P1-S1-C17
        - P1-S3-C11
        - P1-S4-C2
        - P2-S1-C5
        - P2-S2-C14
        - P2-S3-C3
        - P2-S3-C4
        - P2-S3-C5
        - P2-S3-C9
        - P2-S3-C10
        - P2-S3-C12
        - P2-S3-C13
        - P3-S1-C9
        - P3-S1-C12
        - P3-S3-C7
        - P4-S2-C5
        - P4-S2-C9
        - P4-S2-C13
        - P5-S1-C3
        - P5-S1-C4
        - P5-S1-C12
        - P5-S1-C13
        - P5-S1-C14
        - P5-S2-C3
        - P5-S2-C4
        - P5-S2-C10
        - P5-S2-C11
        - P7-S4-C5
        - P7-S4-C7
        - P7-S4-C8
        - P7-S4-C9
        - P7-S4-C13
        - P7-S4-C16
        - P7-S4-C17
        - P8-S3-C7
        - P8-S3-C9
        - P8-S4-C11
        - P8-S4-C13
        - P8-S4-C15
        - P8-S4-C17
        - P8-S5-C12
        - P8-S5-C14
        - P8-S5-C16
        - P9-S2-C4
        - P9-S2-C7
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P1-S2-C7
        - P1-S2-C8
        - P1-S2-C9
        - P1-S2-C10
        - P1-S3-C4
        - P5-S2-C13
        - P5-S3-C8
        - P7-S1-C2
        - P7-S1-C3
        - P7-S1-C4
        - P7-S1-C5
        - P7-S1-C6
        - P7-S1-C7
        - P7-S1-C8
        - P7-S1-C9
        - P7-S1-C10
        - P7-S1-C11
        - P7-S1-C12
        - P7-S1-C13
        - P7-S1-C14
        - P7-S1-C15
        - P8-S4-C3
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - imaging_provenance
      - outcome_definition
      - limitations
      - personal_factors
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies:
      - evidence_id: P2-S2-C6
        as_printed: P = 10
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P2-S3-C3
        as_printed: P = 9
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P2-S3-C4
        as_printed: P = 5.2
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      - evidence_id: P2-S3-C4
        as_printed: P = 4.4
        reason: Printed p-value outside [0,1]; verify PDF, never correct automatically
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P2-S2
        - P2-S3
        - P3-S1
        - P3-S2
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
        - P5-S3
        - P5-S4
        - P6-S3
        - P7-S1
        - P8-S4
        - P8-S5
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
      source_review: _compare/relationships-2026-11-16/review-current/Siegel2016
      source_status_sha256: 481e97225cd277541b9f139d96058fce3f26ad1bf402be1338560c4a840c73e8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C16
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: States memory better predicted by FC and motor/visual by lesion topography.
    - source_id: P1-S1-C17
      disposition: represented
      result_indexes:
      - 2
      reason: States attention and language well predicted by both.
    - source_id: P1-S1-C18
      disposition: represented
      result_indexes:
      - 13
      reason: Links interhemispheric integration/intrahemispheric segregation to behavioral
        impairment.
    - source_id: P1-S1-C19
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory statement about network-specific patterns.
    - source_id: P1-S2-C2
      disposition: represented
      result_indexes:
      - 14
      reason: Associates loss of interhemispheric communication with multidomain impairment.
    - source_id: P1-S3-C11
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Restates memory vs sensorimotor prediction results.
    - source_id: P1-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about cortical areas predicting cognitive deficit.
    - source_id: P2-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of Figure 1.
    - source_id: P2-S2-C6
      disposition: represented
      result_indexes:
      - 3
      reason: Reports decreased homotopic FC in patients.
    - source_id: P2-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Details on individual network differences.
    - source_id: P2-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: ANOVA results on homotopic FC.
    - source_id: P2-S2-C9
      disposition: represented
      result_indexes:
      - 4
      reason: Reports no significant change in intrahemispheric connectivity.
    - source_id: P2-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Sensitivity analysis regarding global signal regression.
    - source_id: P2-S2-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement about RSN pair changes.
    - source_id: P2-S2-C14
      disposition: represented
      result_indexes:
      - 5
      reason: Reports DAN-DMN FC connectivity changes.
    - source_id: P2-S3-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Correlation between DAN homotopic FC and DAN-DMN FC.
    - source_id: P2-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Similar relationships in other networks.
    - source_id: P2-S4-C5
      disposition: repeated
      result_indexes:
      - 5
      reason: Restatement of DAN-DMN connectivity result.
    - source_id: P3-S1-C1
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Lesion size predicts homotopic FC, but topography does not improve prediction.
    - source_id: P3-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Null findings for head motion, eyes open, or lag laterality.
    - source_id: P3-S1-C14
      disposition: background_or_descriptive
      result_indexes: []
      reason: Permutation test significance for individual models.
    - source_id: P3-S2-C1
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of model significance.
    - source_id: P3-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Control analysis for null models.
    - source_id: P3-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on significant differences between models.
    - source_id: P3-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Details of Wilcoxon signed rank test.
    - source_id: P3-S3-C1
      disposition: represented
      result_indexes:
      - 1
      reason: Lesion location better in motor and visual domains.
    - source_id: P3-S3-C2
      disposition: represented
      result_indexes:
      - 0
      reason: FC better in visual and verbal memory domains.
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General statement that models perform better than chance.
    - source_id: P4-S1-C1
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Quantifies variance explained for memory (FC > lesion) and motor/visual
        (lesion > FC).
    - source_id: P4-S1-C2
      disposition: represented
      result_indexes:
      - 2
      reason: Reports attention trend and language equality.
    - source_id: P4-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Generalization to raw scores.
    - source_id: P4-S1-C13
      disposition: background_or_descriptive
      result_indexes: []
      reason: Observation of common features in FC-deficit maps.
    - source_id: P4-S1-C14
      disposition: represented
      result_indexes:
      - 8
      reason: Positive interhemispheric and negative intrahemispheric weights correlate
        with behavior.
    - source_id: P4-S2-C3
      disposition: represented
      result_indexes:
      - 8
      reason: ANOVA confirms contribution of connection types.
    - source_id: P4-S2-C4
      disposition: represented
      result_indexes:
      - 9
      reason: Language depends on positive intrahemispheric weights in left hemisphere.
    - source_id: P4-S3-C7
      disposition: repeated
      result_indexes:
      - 8
      reason: Restatement of ANOVA result.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 10
      reason: MTL model explained 28.7% of variance.
    - source_id: P5-S1-C14
      disposition: represented
      result_indexes:
      - 11
      reason: Reduced interhemispheric FC predicts shared deficits.
    - source_id: P5-S2-C3
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of memory vs sensorimotor prediction.
    - source_id: P5-S2-C4
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of language and attention results.
    - source_id: P5-S3-C4
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of lesion load predicting homotopic FC.
    - source_id: P6-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      - 1
      reason: Restatement of associative vs sensorimotor prediction.
    - source_id: P6-S2-C5
      disposition: repeated
      result_indexes:
      - 0
      reason: Restatement of memory prediction.
    - source_id: P6-S3-C2
      disposition: repeated
      result_indexes:
      - 2
      reason: Restatement of language model accuracy.
    - source_id: P6-S3-C10
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of MTL variance explained.
    - source_id: P7-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Difference in parcel homogeneity between groups.
    - source_id: P7-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: General summary of findings.
    - source_id: P7-S4-C17
      disposition: background_or_descriptive
      result_indexes: []
      reason: Counts of patients with deficits.
    - source_id: P7-S5-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Lesion size statistics.
    - source_id: P8-S4-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of t-tests for FC differences.
    - source_id: P8-S5-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Details on PCA components retained.
    unresolved_coverage:
    - source_id: P1-S2-C2
      disposition: unresolved
      reason: Unknown result index; not accepted as coverage
    - source_id: P4-S3-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P4-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P4-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P4-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P4-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S1-C16
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S2-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P5-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S1-C13
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P6-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S3-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S4-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S4-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S4-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S4-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P7-S4-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P8-S4-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C19
    - P1-S3-C11
    - P1-S4-C2
    - P2-S2-C5
    - P2-S2-C7
    - P2-S2-C8
    - P2-S2-C11
    - P2-S2-C13
    - P2-S3-C3
    - P2-S3-C4
    - P3-S1-C6
    - P3-S1-C14
    - P3-S2-C1
    - P3-S2-C2
    - P3-S2-C4
    - P3-S2-C5
    - P3-S3-C5
    - P4-S1-C5
    - P4-S1-C6
    - P4-S1-C13
    - P4-S2-C6
    - P4-S2-C7
    - P4-S2-C8
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S1-C9
    - P5-S1-C10
    - P5-S1-C11
    - P5-S1-C12
    - P5-S1-C13
    - P5-S1-C16
    - P5-S2-C9
    - P5-S2-C10
    - P5-S2-C11
    - P5-S3-C7
    - P5-S3-C9
    - P6-S1-C9
    - P6-S1-C13
    - P6-S2-C2
    - P6-S2-C8
    - P6-S3-C2
    - P6-S3-C3
    - P6-S3-C4
    - P7-S1-C9
    - P7-S2-C2
    - P7-S2-C5
    - P7-S2-C6
    - P7-S2-C7
    - P7-S3-C12
    - P7-S4-C5
    - P7-S4-C6
    - P7-S4-C7
    - P7-S4-C8
    - P7-S4-C9
    - P7-S4-C17
    - P7-S5-C10
    - P8-S4-C6
    - P8-S4-C7
    - P8-S5-C8
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
      eligibility:
      - P2-S1-C11
      - P7-S2-C15
      - P7-S3-C2
      - P7-S3-C5
      - P7-S3-C6
      - P8-S2-C10
      - P8-S3-C10
      imaging_provenance: []
      imaging_timing:
      - P2-S1-C9
      - P5-S1-C9
      - P7-S3-C10
      - P8-S1-C2
      outcome_timing:
      - P2-S1-C9
      - P5-S1-C9
      - P8-S1-C2
      outcome_definition: []
      validation:
      - P8-S4-C5
      - P8-S5-C9
      analysis_restrictions:
      - P7-S3-C11
      - P7-S3-C12
      - P7-S4-C12
      - P8-S3-C1
      - P8-S3-C8
      dependent_variable_statement:
      - P1-S1-C15
      - P2-S1-C5
      - P2-S3-C5
      - P3-S1-C9
      limitations: []
      personal_factors: []
      tested_personal_effects:
      - P5-S3-C4
      adjustment_roles:
      - P2-S2-C8
      - P3-S1-C5
      - P3-S1-C6
      - P8-S2-C6
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P1-S1-C15
      - P2-S1-C9
      - P2-S1-C12
      - P2-S3-C8
      - P7-S3-C3
      - P7-S3-C7
      - P8-S4-C3
      - P10-S1-C16
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: mixed
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S1-C16
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S1-C17
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S3-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P1-S4-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S2-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P2-S3-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P3-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S1-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P4-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P5-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S4-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S4-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S4-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S4-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S4-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S3-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C13
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C15
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S4-C17
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S5-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S5-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S5-C16
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P9-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S1-C9
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S2-C2
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P9-S2-C4
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: tested_personal_effects
      source_id: P2-S3-C5
      reason: No current-result classification; a covariate description is not an
        individual test
    - slot: analysed_sample
      source_ids:
      - P1-S1-C15
      - P1-S3-C11
      - P1-S4-C2
      - P2-S1-C12
      - P2-S3-C8
      - P3-S1-C14
      - P3-S2-C1
      - P5-S1-C10
      - P7-S3-C3
      - P7-S3-C7
      - P8-S2-C9
      - P8-S3-C11
      - P8-S4-C10
      - P9-S2-C4
      - P10-S1-C16
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C15
      - P1-S3-C11
      - P2-S1-C9
      - P2-S3-C8
      - P7-S2-C13
      - P7-S2-C14
      - P7-S2-C15
      - P7-S3-C4
      - P7-S3-C7
      - P8-S2-C9
      - P8-S3-C11
      - P10-S1-C16
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S1-C15
      - P2-S1-C4
      - P3-S1-C9
      - P4-S2-C14
      - P6-S3-C16
      - P7-S5-C3
      - P7-S5-C4
      - P8-S1-C4
      - P8-S1-C5
      - P8-S1-C6
      - P8-S1-C7
      - P8-S1-C8
      - P8-S2-C13
      - P8-S2-C14
      - P8-S3-C3
      - P8-S3-C13
      - P8-S3-C14
      - P8-S5-C7
      - P9-S2-C3
      - P10-S1-C16
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C15
      - P1-S1-C16
      - P1-S1-C17
      - P1-S3-C11
      - P1-S4-C2
      - P2-S1-C5
      - P2-S2-C14
      - P2-S3-C3
      - P2-S3-C4
      - P2-S3-C5
      - P2-S3-C9
      - P2-S3-C10
      - P2-S3-C12
      - P2-S3-C13
      - P3-S1-C9
      - P3-S1-C12
      - P3-S3-C7
      - P4-S2-C5
      - P4-S2-C9
      - P4-S2-C13
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C12
      - P5-S1-C13
      - P5-S1-C14
      - P5-S2-C3
      - P5-S2-C4
      - P5-S2-C10
      - P5-S2-C11
      - P7-S4-C5
      - P7-S4-C7
      - P7-S4-C8
      - P7-S4-C9
      - P7-S4-C13
      - P7-S4-C16
      - P7-S4-C17
      - P8-S3-C7
      - P8-S3-C9
      - P8-S4-C11
      - P8-S4-C13
      - P8-S4-C15
      - P8-S4-C17
      - P8-S5-C12
      - P8-S5-C14
      - P8-S5-C16
      - P9-S2-C4
      - P9-S2-C7
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P1-S2-C7
      - P1-S2-C8
      - P1-S2-C9
      - P1-S2-C10
      - P1-S3-C4
      - P5-S2-C13
      - P5-S3-C8
      - P7-S1-C2
      - P7-S1-C3
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C6
      - P7-S1-C7
      - P7-S1-C8
      - P7-S1-C9
      - P7-S1-C10
      - P7-S1-C11
      - P7-S1-C12
      - P7-S1-C13
      - P7-S1-C14
      - P7-S1-C15
      - P8-S4-C3
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
      pdf_sha256: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
      review_sha256: 03e75b5c1c65071410bb6c69d75bbabfd12690c0e3d38162f959864342a6fa62
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
      - P2-S2-C9
      source_result: Within-network intrahemispheric connectivity was not significantly
        changed in both the ipsilesional and contralesional hemispheres when comparing
        stroke patients to age-matched controls.
      result_status: not_detected
      patient_measurement: functional_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The source P2-S2-C9 explicitly describes the comparison of within-network
            intrahemispheric connectivity between stroke patients and controls, matching
            the proposed analysis label and outcome.
          source_ids:
          - P2-S2-C9
          - P8-S4-C13
        direction:
          answer: fits
          reason: The source states that connectivity was 'not significantly changed',
            which aligns with the 'no_effect' direction in the draft, indicating a
            null finding for this specific comparison.
          source_ids:
          - P2-S2-C9
        construct:
          answer: fits
          reason: The exposure is stroke status (patient vs control), the outcome
            is within-network intrahemispheric connectivity, and the measurement is
            resting-state fMRI (functional_imaging). The draft correctly identifies
            the imaging modality and the specific connectivity type.
          source_ids:
          - P2-S1-C4
          - P2-S2-C4
          - P8-S2-C4
        qualifications:
          answer: fits
          reason: The draft includes the sample size (100 patients, 27 controls) and
            the robustness check regarding global signal regression vs CompCor, both
            of which are supported by P2-S1-C12 and P2-S2-C11. The limitations regarding
            parcellation coverage and age range are also correctly cited.
          source_ids:
          - P2-S1-C12
          - P2-S2-C11
          - P7-S1-C5
          - P8-S4-C3
        missing_material_caveat:
          answer: fits
          reason: The draft captures the key methodological constraints (parcellation
            limits, age range) and the specific null result context. No material caveats
            that would change the interpretation of the null finding are omitted.
          source_ids:
          - P7-S1-C5
          - P8-S4-C3
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Sample size requires source confirmation; it has not been transcribed.
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Sample size requires source confirmation; it has not been transcribed.
    normalizations:
    - field: sample.n
      original: 127
      action: not_transcribed
      reason: Not supported by selected quotations
    analysis_identity:
      id: R005
      exposure:
        text: stroke
      outcome:
        text: within-network intrahemispheric connectivity
      analysis_label: Group Comparison (FC Patterns)
      relation: association
      evidence_ids:
      - P2-S2-C9
      - P2-S3-C12
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
        pdf_sha256: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
        source_review: _compare/relationships-2026-11-16/review-current/Siegel2016
        source_status_sha256: 481e97225cd277541b9f139d96058fce3f26ad1bf402be1338560c4a840c73e8
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S1-C12:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 1404b20c503077ad208d8244cd69115d8efa2287ebf4863b74994451c94726fb
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C12
          page: 2
          text_layer_sha256: 1404b20c503077ad208d8244cd69115d8efa2287ebf4863b74994451c94726fb
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'After exclusion, 100 stroke patients and 27

          age-matched controls were studied.'
        anchor_text: 'After exclusion, 100 stroke patients and 27

          age-matched controls were studied.'
        excluded_fragments: []
        image_sha256: ba8927bd780a2a2a6271b46abd52da67773a495e8e41d2d9026e6de1216a873d
        transcription: '. After exclusion, 100 stroke patients and 27

          age-matched controls were studied'
      P2-S1-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f02ff389bbd3e442fd7e91926588947e2849cfde6a34d7c6e7466e53fd5bb950
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C9
          page: 2
          text_layer_sha256: f02ff389bbd3e442fd7e91926588947e2849cfde6a34d7c6e7466e53fd5bb950
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'We recruited 132 first-time symp-

          tomatic stroke patients 1–2 wk after stroke, and 31 demographi-

          cally matched controls.'
        anchor_text: 'We recruited 132 first-time symp-

          tomatic stroke patients 1–2 wk after stroke, and 31 demographi-

          cally matched controls.'
        excluded_fragments: []
        image_sha256: a64f06323040ae2d3c062a750e2dec1e0848ef073dabbc29e6e02be28e69853f
        transcription: We recruited 132 first-time symptomatic stroke patients 1–2
          wk after stroke, and 31 demographically matched controls
      P2-S1-C2:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: b9a9d5290e8b6ac7489832fb901432c527993087a2dd7ae98af2566b99ecfbb9
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: a1359dbb3116f00f86a121892f189ef11d53e9e72dde2bb7e0cc600a364cf19a
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S1-C2
          page: 2
          text_layer_sha256: a1359dbb3116f00f86a121892f189ef11d53e9e72dde2bb7e0cc600a364cf19a
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'We evaluated these predictions within a clinically relevant

          sample, i.e., a large population of subacute stroke patients (n =

          132) shown to be representative of a larger clinical population.'
        anchor_text: 'We evaluated these predictions within a clinically relevant

          sample, i.e., a large population of subacute stroke patients (n =

          132) shown to be representative of a larger clinical population.'
        excluded_fragments: []
        image_sha256: 38fe11d65cb01dad9bb22156b290194e5a425904238f05aeef717c89eb47eb12
        transcription: We evaluated these predictions within a clinically relevant
          sample, i.e., a large population of subacute stroke patients (n = 132) shown
          to be representative of a larger clinical population
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 2
  quote: 'By con-

    trast, within-network intrahemispheric connectivity was not sig-

    nificantly changed in both the ipsilesional and contralesional

    hemispheres (Fig. 1 B and C).'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
