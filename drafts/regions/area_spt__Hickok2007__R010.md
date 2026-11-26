---
id: area_spt
name: area Spt cluster
kind: network
findings:
- id: f1
  target: vocal_tract_reproduction
  target_kind: impairment
  claim: Hickok2007 reports, based on G.H.’s unpublished observations reported in this Opinion article, that area Spt was significantly more active during the humming condition than the imagining-playing-on-a-keyboard condition, suggesting it is more tightly coupled to the vocal tract motor effector system than to other effector systems. This is an unpublished observation recounted in an Opinion article, not an independently published cohort result.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Participants in the studies summarized by Hickok2007; this record is a secondary review report, not a newly recruited cohort. Primary source: G.H.’s unpublished observations reported in this Opinion article.'
    phase: not_reported
    time_post_onset: Varies across reviewed studies; see cited primary study and source passages.
  statistics:
    threshold: not_applicable_review_synthesis
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - finding is based on a review of functional imaging studies
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reclassified as a secondary review report, explicitly attributing the result to G.H.’s unpublished observations reported in this Opinion article. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication. Source repair (unapproved): Reclassified as a secondary review report, explicitly attributing the result to G.H.’s unpublished observations reported in this Opinion article. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.'
  imaging_details:
    reference_space: not_applicable
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
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
    - proposed_concept:vocal_tract_reproduction
    - agent_source_repair_pending_human_review
  citation: '@Hickok2007'
  source_passages:
  - section: Original source P8-S3-C5
    page: 8
    quote: "Spt was significantly \nmore active during the humming condi-\ntion than the playing condition, despite \nthe fact that the playing condition is more \ndifficult (G.H., unpublished observations)."
    supports: claim
  - section: Original source P8-S3-C6
    page: 8
    quote: "These results indicate that Spt might be \nmore tightly coupled to a specific motor \neffector system, the vocal tract, than to a \nspecific sensory system."
    supports: claim
  - section: Original source P8-S3-C4
    page: 8
    quote: "Skilled \npianists were asked to listen to novel melo-\ndies and then to covertly reproduce them \nby either humming or imagining playing \nthem on a keyboard."
    supports: sample
  - section: Original source P8-S2-C7
    page: 8
    quote: "A network \nof regions was identified, including the pos-\nterior STS bilaterally, a left-dominant site \nin the Sylvian fissure at the boundary \nbetween the parietal and temporal lobes \n(area Spt), and left posterior frontal regions \n(FIG. 4)52,53."
    supports: method
  design: narrative-review
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Hickok2007
  proposal_id: R010
  approved: false
  original_core_review:
    paper: Hickok2007
    proposal_id: R010
    review_status_sha256: ef63ddb34895013b3db1661021d9b6efcf4e6d57005eeb884167168f27fe7cc2
    review_binding:
      version: candidate-inventory-v1
      input_hashes:
        pdf: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
      original_review_binding:
        version: relationship-review-v5
        input_hashes:
          pdf: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
          A/passages.json: 907c1915be60c97c7569c28ed3b1cd3cf233ef64214c93c874c84a6ba8d5991a
          A/raw.json: 0d92ffabcd811c15a00d09ee3eb8a5cd89b7ab77ef57184adf7051e13c2077ac
          A/source-units.json: 6653a2b26599062177ce2b9500b16427e2a805fe8eb8b2b2693e61f429f37384
          A/full-source-units.json: 6653a2b26599062177ce2b9500b16427e2a805fe8eb8b2b2693e61f429f37384
          A/meta.json: 58f43d078cf897a33075d49a40174056bd111b29022e4aab5a73ec5c2e4bf90f
          A/table-images/TABLE-1-page-5-1.png: 9025e74d97b7a453e2181219d835f0d49144c6d8ae9f91ba72bbb7374b10befd
          A/table-images/page-5.png: 3ea980326d20fe58b612ef64536ca085bb6ac49ec7aebd5e5d189993e222e623
          A/table-images/manifest.json: a0e06360ba3d3346627d4ceb4a6463a7090bb4b542bbbf3d5599b1e4d17d436f
          A/clauses/window-11/raw.json: f7b9a4f4131465763449d70999e6d25ae5be0fb5bb1160c281cc1a9c7db8fb3d
          A/clauses/window-11/prompt.txt: 3782aba25d5035e150c81ac5e47d2b78ce6f72b98a4f9811776d3377cfd4f0cc
          A/clauses/window-11/meta.json: c46d22db0ae725eb76abe2f31b6ab5b96e5e6dc1738934cc3bee1f1c777f7909
          A/clauses/window-16/raw.json: 31abf317f2f2316673dbd59da9854d21b4601c49b55b6a513d7f7219ce242917
          A/clauses/window-16/prompt.txt: 458c81e7c87d938dc2803577ff4db667db9f4c57adb04f4c72593d95e9e3660c
          A/clauses/window-16/meta.json: 8e5dbb65d5ab451807caa87145b116ec80cbaa2c2124ca15fd254fc4b915eb7b
          A/clauses/window-20/raw.json: bde48d2cf80136e5e5520a799379d67a95090ba329bb3ddd9a269366cc9e9465
          A/clauses/window-20/prompt.txt: 28e76f3955d9614c838d4e3f007972b66cfe3ed5552df2fb8272a0026745b8c7
          A/clauses/window-20/meta.json: 3ad62bf679a35b1bc062b4c1b3df486de4faf2358398c83550a3455c3ecf8249
          A/clauses/window-18/raw.json: 0457b703280d87f4dce29c03c5d679c545211515674e211c6933069078887d79
          A/clauses/window-18/prompt.txt: e504c00b97d539fe7529cfaaf91498c0f94c7d495354111b4f29796b3e79164e
          A/clauses/window-18/meta.json: 35bdce459ba9649e79dfd0df1c0030167383a7e323e15a53f9f32f3b2ce24e72
          A/clauses/window-19/raw.json: bbc8e218b1edb85cde0b71e18116f50c8beba0967bc5d04b5b2bb4fdb50825cd
          A/clauses/window-19/prompt.txt: 039074410b7de82f2978b89b3101596cec90a54a99942ce561a7447290859100
          A/clauses/window-19/meta.json: de609acebc620d429d68ebc37583a201d757c92488837143d466e780982552c5
          A/clauses/window-21/raw.json: 58d1501c9087ae195d8bd2cc63faee58292c342e643e1ea624618d64f4682339
          A/clauses/window-21/prompt.txt: 2c800272b42e1ff802475b9721bab8648c63ecfb49a309991f7964241372b90f
          A/clauses/window-21/meta.json: c3c95a6126f45c788fba643d6e85c4bbc67c520bc9aea0a7908533ffab304c46
          A/clauses/window-17/raw.json: f0fde1247bea343dcf9b37289470699f20a6f0e2cafc654b06ae11ef398531b4
          A/clauses/window-17/prompt.txt: 5a6f58fbfb42646ae4845a12294ea9528da376eda7f682c632745cb1ad539502
          A/clauses/window-17/meta.json: 5e7d512b80deee35e8b59c66a5893382794e7835dcb4467c831fdd703225db55
          A/clauses/window-10/raw.json: be65df56bbfd26a47154eb84ba613e04559ec986abdf048c82599222e2d6f18b
          A/clauses/window-10/prompt.txt: e0d0a3d580dd30195b91198484841967aae190e212285e70ad39d574db70faf6
          A/clauses/window-10/meta.json: f3f5d10a8b1dbf879f9b13ee13fa7aecdb9efc85163b2305665005a04de62820
          A/clauses/window-03/raw.json: ba660cde61e70845a1e5f445fd8bbe6c5025ccfd7a64f3be608cc7c55c381162
          A/clauses/window-03/prompt.txt: 99569569b31799c1cce7d450e2cf4fe31b6c76fea1d32ba93e251e06e4391316
          A/clauses/window-03/meta.json: 3fec4de411acaf3f92efc65c4a60e0c6ef76ef5e059b89665908548a57da922a
          A/clauses/window-04/raw.json: 3a5ebb2820dc16735f74050dcdcc6572654e00659ebd420dec80ee5f9b76589f
          A/clauses/window-04/prompt.txt: 6599869f7e7759a6b59afa8f7d7f879c64ecaac3c200f1b2226c02e2faa959a4
          A/clauses/window-04/meta.json: 406ba82c4c5896a48c0ae96e85dda38725d8dd156165a4a566a0a6c79db96011
          A/clauses/window-05/raw.json: cfe3412b81c03bad347868450c3ed6471f9a36dda27ab04cac0093f9cb21240e
          A/clauses/window-05/prompt.txt: 4e197710f939259b60546b7875a22c307dba14e055e8581f0857ce66b0712673
          A/clauses/window-05/meta.json: e882d4d2d262b868c66d350d388777b6d0bcbf561ce1d97389a69d17178427fe
          A/clauses/window-02/raw.json: 27a4f80ae2805a7da56b68e344f2fbd1e73f9bb4f44f25b801ecc22a79de0ae9
          A/clauses/window-02/prompt.txt: ce66ff9f6c7fe0be0e6ce548b8afca58e7fa2870a5d751c159cbdc1182198854
          A/clauses/window-02/meta.json: 69a3e29a8e035b299aaabc2b404372004a4df8705e610eaa494fa1537032c0cb
          A/clauses/window-15/raw.json: 4464530737a8dcaea34009059f82603ae16257e377740e61132357ba787eada8
          A/clauses/window-15/prompt.txt: a53ebf960406bfb0c767f6733485406c83a3472628d7e111fb89fc3acd3f06bb
          A/clauses/window-15/meta.json: 65aa8027cb833192688c2f57cf0a7bcf7f88226b2c7c286200097b3739a67eb1
          A/clauses/window-12/raw.json: b064fcb7776e2d133727d553e4aa4af229a83727756437c4a2214407e186adc4
          A/clauses/window-12/prompt.txt: f7fc1a91ffb612ea08512a8aa32b9d2466f3822dfcceb260eee6a5d700fbc6ae
          A/clauses/window-12/meta.json: f906239d3e870073fe0040e2d69d42d14c74b048cf6fcb2054255e3aad7efca6
          A/clauses/window-23/raw.json: b2dff731923ebf4a3a11d07a52340bef0b13951462e539f216556408b2764948
          A/clauses/window-23/prompt.txt: 4ddaeeacedf9975ab6a8619808a098e0571890fe919cde89f4eff17d90a9a5e7
          A/clauses/window-23/meta.json: e93f6aec90c2a8a5670e877431e9a856435d3b9da42ecc452e70b0c73928e56f
          A/clauses/window-22/raw.json: 6ff9f0bc1cbfee57b54cc346ade22a2d1381e12edeade2ceb2e7f493a93f42ae
          A/clauses/window-22/prompt.txt: c1c8bf6f6bf44d503f5078c8cb3ee96f2df2eb2739aa3351c70d006f5947b201
          A/clauses/window-22/meta.json: 7688175c9584fb89feb11d23597ccdc5566166d4eac517511976f7419101897e
          A/clauses/window-13/raw.json: eaab4eeadc9aaefc4426869f181dedc0470753bcc1f9ae747111a317af433593
          A/clauses/window-13/prompt.txt: 6b94f4a56417bcef16bcb9616fd1940760c9da0b7cb53fad576e0ceadd21e7e2
          A/clauses/window-13/meta.json: aca5e02ee19ff6a968b4b88ffc6ce22e6fa321c33b91dba111bbac80af64d4d2
          A/clauses/window-14/raw.json: 7e7d40979d4aff333bb805fec22691fbe5327ec4fc29c3b02d985b66215ee2e3
          A/clauses/window-14/prompt.txt: 1c9c2d1a39f1cc6ecbeac3c40f03df8854bfeed2d9664b880a71d92fe4a775a4
          A/clauses/window-14/meta.json: c5d0ad99f4833dd13606d05dfba8c33acb76ecd350ec2b8879815c810d9181c6
          A/clauses/window-09/raw.json: f683b48a92cf762fd4d8ecbac76a0f0546c170497b840a6588aa11b4c6009f4f
          A/clauses/window-09/prompt.txt: 84f7f4e5e4acca18323bc1b1c96e1882673a069cb956aa6c39f1b5e4fbd03bd3
          A/clauses/window-09/meta.json: af5dfafd32c10ecfca34fcbcce04039a3d43321a23ae2f99c6b7b049bfa0d519
          A/clauses/window-07/raw.json: 14aa931d624b495010e2fa8412c5289eba528cf10cb699367e354c254c3ef695
          A/clauses/window-07/prompt.txt: adfe8fe58687cf5ff8a30632983bb712fb76baf2b278d3eff54df9fa3f5425cf
          A/clauses/window-07/meta.json: 7633749f6c6cb3974ef8335f299858d4ff89ede901a94ee0fc56aa3fbc3ce42e
          A/clauses/window-01/raw.json: 936a071138a146942551cd1dc59b3b8d90aff9b87fa2f7a8ae95691fc33a4ae3
          A/clauses/window-01/prompt.txt: 9e914fe71b7ce5e0a526a462a202607e4629b7546d26030ecf6a5565871a70c6
          A/clauses/window-01/meta.json: fbf38f062ee3e66e2e69a389ad5e6fb20928a42b8142a4ce577bedbc749139e3
          A/clauses/window-06/raw.json: 2fefea3b969dfbd230a979ae876a92773c5b1512b20518fa80aa83153cdd9ff6
          A/clauses/window-06/prompt.txt: 0328e90c3505903a46a7972b0860a57c1c01663bb3f4585f54dc8227d574a3ee
          A/clauses/window-06/meta.json: 396e4050c0eeb6fce10ebf85d5e15d6f45aee8a2bd83d549943dea4fe1d08645
          A/clauses/window-08/raw.json: a7f37b924fde61dcb04a3040cb540c18c1ccfb8bc3c5ca2d918637ebd8936bae
          A/clauses/window-08/prompt.txt: 1930d20e7a08bb863a202cd0af128fe282daa1109d2ec06944590da1785c8ece
          A/clauses/window-08/meta.json: aa84afc97261877d2c9931a378c20a54933a16832b19d48076abb41a0ac1d585
          A/tables/TABLE-1-page-5-1/raw.json: 941c1907029814a8cf02c2b6045b08ec6d7a97dace3bd9d9487608507526a0d1
          A/tables/TABLE-1-page-5-1/prompt.txt: b384e13eb279bb80d607b0df16648ff947f48c54e70aa617446f897abdebe691
          A/tables/TABLE-1-page-5-1/meta.json: 88f5a6a6808d27644d6f9efbd400a5aafc4ea3db68111fdcb2a9e42b9396f472
          B/passages.json: 907c1915be60c97c7569c28ed3b1cd3cf233ef64214c93c874c84a6ba8d5991a
          B/raw.json: 2a4bb959b2419c44956fdb2577b23f5525634ac1629e3339c7ac143144ca75fc
          B/source-units.json: 6653a2b26599062177ce2b9500b16427e2a805fe8eb8b2b2693e61f429f37384
          B/full-source-units.json: 6653a2b26599062177ce2b9500b16427e2a805fe8eb8b2b2693e61f429f37384
          B/meta.json: 028626a50ddb53b1660ddb21313ac4a7fe4a179f2040a857d849b52010ff4435
          B/table-images/TABLE-1-page-5-1.png: 9025e74d97b7a453e2181219d835f0d49144c6d8ae9f91ba72bbb7374b10befd
          B/table-images/page-5.png: 3ea980326d20fe58b612ef64536ca085bb6ac49ec7aebd5e5d189993e222e623
          B/table-images/manifest.json: b7c9e5baf1fd8f4e2c84d28b181e026652ca6da193ca1e0dfbe9772668062ef4
          B/clauses/window-11/raw.json: 3a59ceeb07ecef9d7b8c466629170ea40830248ca9d5895dcde4c833b6f5d083
          B/clauses/window-11/prompt.txt: 3782aba25d5035e150c81ac5e47d2b78ce6f72b98a4f9811776d3377cfd4f0cc
          B/clauses/window-11/meta.json: bdccb98c2f571896a9168edaa82eebb3f9031ee18e2316c58025a5b50511320d
          B/clauses/window-16/raw.json: afdb16c7ad6b4aa71d01b315662673c3a38f6ce4913316de99a0f85bb28639fd
          B/clauses/window-16/prompt.txt: 458c81e7c87d938dc2803577ff4db667db9f4c57adb04f4c72593d95e9e3660c
          B/clauses/window-16/meta.json: 9c31d589be331c7fd04169ae3e6172330b7782136009fe5a9252e57351bcbdeb
          B/clauses/window-20/raw.json: cdb7747880649bd226e51c2e62284ae1660a1f4ae43cbc99750c25326dbb03bd
          B/clauses/window-20/prompt.txt: 28e76f3955d9614c838d4e3f007972b66cfe3ed5552df2fb8272a0026745b8c7
          B/clauses/window-20/meta.json: b651ec997796c2b6e147e4735033a83a5d051572b56a0fea434f6d27008105e4
          B/clauses/window-18/raw.json: 3cb88cf180d0315322cc3a25235c9413722e1d8dc48fac659da3a09998fb3cdf
          B/clauses/window-18/prompt.txt: e504c00b97d539fe7529cfaaf91498c0f94c7d495354111b4f29796b3e79164e
          B/clauses/window-18/meta.json: c95c2a949dc25d73bf27fbb7fa2eafda69e5397907873461c52016084f32bc1c
          B/clauses/window-19/raw.json: a805ee1877c7502dcd2dec775be0153bca5e36b17f6f24cd5435cdadeb4a6bc5
          B/clauses/window-19/prompt.txt: 039074410b7de82f2978b89b3101596cec90a54a99942ce561a7447290859100
          B/clauses/window-19/meta.json: 2a77a08cee295fa25e1804ce236775f503ec8f3691f8f5ff64f3ba7182f079ad
          B/clauses/window-21/raw.json: 549c5e0aab792365c81836963eaf2ce759bb724843e9327c6861ecd2f8686c5b
          B/clauses/window-21/prompt.txt: 2c800272b42e1ff802475b9721bab8648c63ecfb49a309991f7964241372b90f
          B/clauses/window-21/meta.json: 3e33739a418cc0c562044f174e8aa2a1485a6454fdbf7db0b853c5db31f51141
          B/clauses/window-17/raw.json: 2e748291cd8e9b63284f20b6039e4b9ce8e5f008c96d4e630af00c255942c3df
          B/clauses/window-17/prompt.txt: 5a6f58fbfb42646ae4845a12294ea9528da376eda7f682c632745cb1ad539502
          B/clauses/window-17/meta.json: 0a04e8125e89f3185be7e1831a3ee89d4840e27632470eefed71999192774f61
          B/clauses/window-10/raw.json: b98ba7937ae22eceaf10bceedee447c3d3dc3604f1fede5dfcacbba345c91c2d
          B/clauses/window-10/prompt.txt: e0d0a3d580dd30195b91198484841967aae190e212285e70ad39d574db70faf6
          B/clauses/window-10/meta.json: 7c594d9471de742ffa742b749b7ebc814bd90913047fa9b8eb4af8a9740794e4
          B/clauses/window-03/raw.json: e010678c8ff8fcb880e7997ee9be58914b41ed808924827113854f8f8eb9aed5
          B/clauses/window-03/prompt.txt: 99569569b31799c1cce7d450e2cf4fe31b6c76fea1d32ba93e251e06e4391316
          B/clauses/window-03/meta.json: 0c97551fdb9fcae1bb0b2c3e456b1ff2e1bc6c2a42834949e43547d2bc45905b
          B/clauses/window-04/raw.json: 7ed13e92bebac2ace02c231ea27d6beb1900decffb7c7c02d7384d61726afcd6
          B/clauses/window-04/prompt.txt: 6599869f7e7759a6b59afa8f7d7f879c64ecaac3c200f1b2226c02e2faa959a4
          B/clauses/window-04/meta.json: 543889edfbca36aa0eeed45753547278b31696c065444214112c443c521aeb9d
          B/clauses/window-05/raw.json: 21ea9670806eb81448f7739d7406ebe4e19b0f768ed584e3947a2af6ec495d71
          B/clauses/window-05/prompt.txt: 4e197710f939259b60546b7875a22c307dba14e055e8581f0857ce66b0712673
          B/clauses/window-05/meta.json: b4ad2b589b99744483f57901e17af828a7f70b8c5c1e7a5d960560914f062997
          B/clauses/window-02/raw.json: d4bd96702d5d1c4bd97769a6c6bd851c02f318b4bf68b04bea31342af8e479f4
          B/clauses/window-02/prompt.txt: ce66ff9f6c7fe0be0e6ce548b8afca58e7fa2870a5d751c159cbdc1182198854
          B/clauses/window-02/meta.json: 4cff04a875d1c1f11f5ed8a99c2ea8cfac658c002cafbde6e292327103e66177
          B/clauses/window-15/raw.json: 94af29ab2a1e5ca1101baf6e5ecd37c753b19424760300f0d309c7325ae4140b
          B/clauses/window-15/prompt.txt: a53ebf960406bfb0c767f6733485406c83a3472628d7e111fb89fc3acd3f06bb
          B/clauses/window-15/meta.json: f94d36c72a18dd567e296b44e69b62e4cae98c22bcf3b5063af4ad4df38917e4
          B/clauses/window-12/raw.json: 1d8f1581b1000fb2ccddc9163d2325f327377c49d012d5a402672de8ec69b82d
          B/clauses/window-12/prompt.txt: f7fc1a91ffb612ea08512a8aa32b9d2466f3822dfcceb260eee6a5d700fbc6ae
          B/clauses/window-12/meta.json: 17e35500b6acc6b91d2706346fe3245e3b42c446de08b4888c771d9c0552cd95
          B/clauses/window-23/raw.json: b2dff731923ebf4a3a11d07a52340bef0b13951462e539f216556408b2764948
          B/clauses/window-23/prompt.txt: 4ddaeeacedf9975ab6a8619808a098e0571890fe919cde89f4eff17d90a9a5e7
          B/clauses/window-23/meta.json: a53e5ebd72fc0ab700b5701443729f0ad611440124eadf3eff5bad86b0a0a727
          B/clauses/window-22/raw.json: e00ea7bec783c7eb474aefdb36ebf16d77feba42dbe66fe4fceb7b31a8adc7f2
          B/clauses/window-22/prompt.txt: c1c8bf6f6bf44d503f5078c8cb3ee96f2df2eb2739aa3351c70d006f5947b201
          B/clauses/window-22/meta.json: 14cb3cc866ebb74477b2314872c1fd60f3e79fab28c7b65067555e557d612fa0
          B/clauses/window-13/raw.json: 1ac56a16a5c8e7e85c9d4e1285c95b6f420a847aef08dc89d37840ef159c5054
          B/clauses/window-13/prompt.txt: 6b94f4a56417bcef16bcb9616fd1940760c9da0b7cb53fad576e0ceadd21e7e2
          B/clauses/window-13/meta.json: eadf28106df6dac0f087a68bc30f71767f579ff4b573a8211f5681895f531299
          B/clauses/window-14/raw.json: 9a7da223539b00581fa60fc8f7ea080de84a9686e0f3a2adfd269494c83bfdc5
          B/clauses/window-14/prompt.txt: 1c9c2d1a39f1cc6ecbeac3c40f03df8854bfeed2d9664b880a71d92fe4a775a4
          B/clauses/window-14/meta.json: 5f76551b58d231020a7d21f6041a15af27547e51fa6612158a38a205558af8f2
          B/clauses/window-09/raw.json: 3069970b4aed69b3fd74fd0ee5d73b1c4b875f4716784488ed64e686845d5284
          B/clauses/window-09/prompt.txt: 84f7f4e5e4acca18323bc1b1c96e1882673a069cb956aa6c39f1b5e4fbd03bd3
          B/clauses/window-09/meta.json: d3509cbdacaf2fa87788c29b33434272154a207c21db5b7adb6703ce94ab4330
          B/clauses/window-07/raw.json: 0e0db5aa1a74ecf05efb3184ba6798a46c2b5ffbdd4fd5fc6ee9cf7c7ef94ecc
          B/clauses/window-07/prompt.txt: adfe8fe58687cf5ff8a30632983bb712fb76baf2b278d3eff54df9fa3f5425cf
          B/clauses/window-07/meta.json: 23010ef527663db2e6cf76736c179f40a2f13871bf1df3fb5d296c32fea0a778
          B/clauses/window-01/raw.json: 507dc0207ebc60da89fdd92cb7e3c1faced94de7d0c8b64bf393b4ff727154be
          B/clauses/window-01/prompt.txt: 9e914fe71b7ce5e0a526a462a202607e4629b7546d26030ecf6a5565871a70c6
          B/clauses/window-01/meta.json: c7d85bd9f610cdfc11e16743972a41d77ebe9f1c7caa07abe1a6a334450f5162
          B/clauses/window-06/raw.json: 965d6731b4504d285f1fe42040b8b579cbb3700502b359323f6e25ca304168dd
          B/clauses/window-06/prompt.txt: 0328e90c3505903a46a7972b0860a57c1c01663bb3f4585f54dc8227d574a3ee
          B/clauses/window-06/meta.json: 595244d54a3ddae22439b26f885f2bd56a04b61760172badf98b529ac4510352
          B/clauses/window-08/raw.json: 987fc112165c9b7e29581f9803e7896ddd264dc1c30d8fce1db25bab65d2cb72
          B/clauses/window-08/prompt.txt: 1930d20e7a08bb863a202cd0af128fe282daa1109d2ec06944590da1785c8ece
          B/clauses/window-08/meta.json: c14a0a16480275cd89852d51f8cfc093c4cda0671f41d444d1b3132b351436f4
          B/tables/TABLE-1-page-5-1/raw.json: 0e85077d2c19c848a26792a9df67aa4814533625b9aa8d0ad310b1933a62c95d
          B/tables/TABLE-1-page-5-1/prompt.txt: b384e13eb279bb80d607b0df16648ff947f48c54e70aa617446f897abdebe691
          B/tables/TABLE-1-page-5-1/meta.json: 820ba16a5033110e3500f8ed9bc55274f8ca5d5bd04c9b501fc0e66004765a59
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
        pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
        source_review: _compare/relationships-2026-11-16/review-current/Hickok2007
        source_status_sha256: 15e7142713989de4b66ee158d05ad36c2ca3f3c491c6dee848d5672ea88ec739
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
    proposal:
      id: R010
      exposure:
        text: area Spt activation
      outcome:
        text: vocal tract reproduction (humming)
      analysis_label: Spt area motor effector specificity
      relation: association
      evidence_ids:
      - P8-S3-C5
      qualifier_ids:
      - P8-S3-C6
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
        source_review: _compare/relationships-2026-11-16/review-current/Hickok2007
        source_status_sha256: 15e7142713989de4b66ee158d05ad36c2ca3f3c491c6dee848d5672ea88ec739
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    audit:
      original_audit:
        coverage_issues:
        - Result passage disposed without unit P4-S2-C6
        - Result passage disposed without unit P4-S2-C7
        - Result passage disposed without unit P4-S2-C8
        - Result passage disposed without unit P8-S3-C3
        unattached_null_or_qualifier_ids:
        - P4-S2-C5
        - P4-S2-C6
        - P9-S1-C2
        suppressed_nonrepresented_units: 14
        default_disposition_count_requires_completeness_check: 401
        unselected_timing_passages: []
        personal_effect_slots_without_result_classification: []
        held_frame_selections:
        - slot: dependent_variable_statement
          source_id: P8-S3-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        empty_frame_slots_require_confirmation:
        - eligibility
        - imaging_timing
        - outcome_timing
        - validation
        - analysis_restrictions
        - personal_factors
        - tested_personal_effects
        - adjustment_roles
        - explicitly_not_adjusted
        unclassified_extraction_ids:
        - P9-S2-C10
        table_review_required:
        - TABLE-1-page-5-1
        unlinked_tables:
        - TABLE-1-page-5-1
        source_anomalies: []
        visual_review_required:
          scope: All main-paper figures and table crops
          note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
          caption_candidate_units:
          - P3-S3
          - P6-S3
          - P7-S2
          - P7-S3
          - P9-S4
        approval: Not performed. Structural checks and model selections do not establish semantic correctness.
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
        source_review: _compare/relationships-2026-11-16/review-current/Hickok2007
        source_status_sha256: 15e7142713989de4b66ee158d05ad36c2ca3f3c491c6dee848d5672ea88ec739
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      coverage:
      - source_id: P2-S1-C7
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses the logic of using sublexical tasks but is not a measured result.
      - source_id: P2-S1-C12
        disposition: represented
        result_indexes:
        - 0
        reason: Establishes the lack of correlation/prediction between speech perception and recognition.
      - source_id: P4-S2-C5
        disposition: background_or_descriptive
        result_indexes: []
        reason: States evidence exists for conjectures but does not provide the specific relationship.
      - source_id: P4-S2-C6
        disposition: background_or_descriptive
        result_indexes: []
        reason: References unpublished observations regarding performance changes.
      - source_id: P4-S2-C7
        disposition: represented
        result_indexes:
        - 4
        reason: Links right hemisphere to long-term integration.
      - source_id: P4-S2-C8
        disposition: represented
        result_indexes:
        - 4
        reason: Qualifies the left hemisphere's lack of selectivity.
      - source_id: P8-S3-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: Introduces the fact that Spt activity is modulated by output modality.
      - source_id: P8-S3-C5
        disposition: represented
        result_indexes:
        - 9
        reason: Reports higher Spt activity during humming vs playing.
      - source_id: P9-S1-C2
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes the proposed dominance of the dorsal stream.
      - source_id: P9-S4-C66
        disposition: background_or_descriptive
        result_indexes: []
        reason: Figure caption describing sensorimotor responses.
      - source_id: P9-S4-C67
        disposition: background_or_descriptive
        result_indexes: []
        reason: Figure caption noting bilateral/unilateral activation patterns.
      unresolved_coverage: []
      pending_source_ids:
      - P2-S1-C7
      - P4-S2-C5
      - P4-S2-C6
      - P4-S2-C8
      - P8-S3-C3
      - P9-S1-C2
      - P9-S4-C66
      - P9-S4-C67
      pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
      tables_requiring_review:
      - TABLE-1-page-5-1
      paper_complete: false
      approved: false
      policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
    study_frame:
      slots:
        analysed_sample:
        - P3-S1-C10
        - P3-S2-C1
        - P3-S2-C2
        - P3-S2-C3
        - P7-S3-C1
        - P8-S2-C5
        - P8-S3-C4
        recruited_sample:
        - P3-S1-C10
        - P3-S2-C1
        - P3-S2-C2
        - P3-S2-C3
        - P6-S2-C11
        - P6-S3-C9
        - P8-S3-C4
        eligibility: []
        imaging_provenance:
        - P3-S2-C4
        - P3-S2-C5
        - P5-S1-C4
        - P6-S2-C12
        - P7-S3-C1
        - P8-S2-C4
        imaging_timing: []
        outcome_timing: []
        outcome_definition:
        - P7-S3-C4
        - P8-S3-C5
        validation: []
        analysis_restrictions: []
        dependent_variable_statement:
        - P6-S1-C5
        - P7-S3-C4
        - P8-S2-C2
        limitations:
        - P2-S3-C8
        personal_factors: []
        tested_personal_effects: []
        adjustment_roles: []
        explicitly_not_adjusted: []
        descriptive_personal_factors:
        - P6-S3-C9
        - P8-S3-C4
      outcome_type: not_stated
      imaging_vs_outcome: not_stated
      validation_type: none_described
      window_merge: Union of selected IDs; differing window enums retained conservatively as both/mixed. Not verified study-level facts.
      held_selections:
      - slot: dependent_variable_statement
        source_id: P8-S3-C5
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
    approved: false
    source_check:
      profile: core
      scope: Independent model text review of core meaning; not human approval or complete PDF verification
      binding:
        profile: core
        version: core-source-check-v3
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        checker_model: qwen3.8:27b
        checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
        host: http://localhost:11434
        pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
        review_sha256: ef63ddb34895013b3db1661021d9b6efcf4e6d57005eeb884167168f27fe7cc2
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
        - P8-S3-C5
        source_result: In skilled pianists, area Spt was significantly more active during the humming condition (vocal tract reproduction) than during the imagining playing condition (keyboard reproduction), despite the playing condition being more difficult. This suggests Spt is more tightly coupled to the vocal tract effector system.
        result_status: detected
        patient_measurement: functional_imaging
        checks:
          analysis_identity:
            answer: fits
            reason: The selected analysis correctly identifies the comparison between humming and keyboard imagination conditions in skilled pianists as described in P8-S3-C5 and P8-S3-C4.
            source_ids:
            - P8-S3-C5
            - P8-S3-C4
          direction:
            answer: fits
            reason: The draft correctly states that Spt activation was higher during humming than playing, matching the source's finding of significant difference favoring the vocal tract effector.
            source_ids:
            - P8-S3-C5
          construct:
            answer: fits
            reason: The exposure (Spt activation) and outcome (vocal tract reproduction vs. other effector) are correctly identified. The measurement is functional imaging (fMRI), not lesion overlap or diffusion tractography.
            source_ids:
            - P8-S3-C5
            - P8-S2-C7
          qualifications:
            answer: fits
            reason: The draft includes the qualification that the playing condition was more difficult, which is explicitly stated in P8-S3-C5 and is material to interpreting the result (activation was higher for the easier task).
            source_ids:
            - P8-S3-C5
          missing_material_caveat:
            answer: fits
            reason: The draft notes that the finding is based on a review of functional imaging studies (specifically unpublished observations cited in the review), which is an appropriate limitation for this context. No other material caveats are omitted that would change the interpretation of this specific comparison.
            source_ids:
            - P8-S3-C5
        optional_pending:
        - Specific statistical values (p-values, t-statistics) for the Spt activation difference are not transcribed.
        - Exact coordinates or atlas definitions for area Spt are not transcribed.
        verdict: draft
        reason: All five core checks fit the source.
        material_issues: []
      pending_details:
      - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
      - Recovery phase is not classified; use the reported timing words.
      - Evidence-strength rating is a conservative draft placeholder pending human review.
      - Specific statistical values (p-values, t-statistics) for the Spt activation difference are not transcribed.
      - Exact coordinates or atlas definitions for area Spt are not transcribed.
      normalizations: []
      analysis_identity:
        id: R010
        exposure:
          text: area Spt activation
        outcome:
          text: vocal tract reproduction (humming)
        analysis_label: Spt area motor effector specificity
        relation: association
        evidence_ids:
        - P8-S3-C5
        qualifier_ids:
        - P8-S3-C6
        context_ids: []
        table_ids: []
        approved: false
        status: requires_source_review
        flags:
        - new_model_candidate_not_verified
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
          source_review: _compare/relationships-2026-11-16/review-current/Hickok2007
          source_status_sha256: 15e7142713989de4b66ee158d05ad36c2ca3f3c491c6dee848d5672ea88ec739
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      paper_complete: false
      visual_prose_readings: {}
      remaining:
      - Human PDF review and approval
      - Pending metadata enrichment
      - Main Results, figures and tables completeness check
  original_publication_entry:
    id: area_spt
    name: area Spt cluster
    kind: network
    findings:
    - id: f1
      target: vocal_tract_reproduction
      target_kind: impairment
      claim: Area Spt was significantly more active during the humming condition than the imagining-playing-on-a-keyboard condition, suggesting it is more tightly coupled to the vocal tract motor effector system than to other effector systems.
      direction: likely
      relationship: correlational
      method: fMRI_activation
      sample:
        n: not_reported
        population: skilled pianists
        phase: not_reported
        time_post_onset: concurrent
      statistics:
        threshold: not_transcribed
      confounders_controlled: []
      confounders_not_controlled: []
      region_definition:
        kind: not_reported
        description: Not transcribed; see source passages and claim.
      author_limitations:
      - finding is based on a review of functional imaging studies
      evidence_quality: cohort
      strength: weak
      notes: 'Exposure measurement: fMRI activation in area Spt (a site in the Sylvian fissure at the boundary between the parietal and temporal lobes) during the reproduction of aurally perceived novel melodies. the playing condition was reported to be more difficult than the humming condition. Additional metadata has not been transcribed; review the pending-field flags before approval.'
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
        - proposed_concept:vocal_tract_reproduction
      citation: '@Hickok2007'
      source_passages:
      - section: Original source P8-S3-C5
        page: 8
        quote: "Spt was significantly \nmore active during the humming condi-\ntion than the playing condition, despite \nthe fact that the playing condition is more \ndifficult (G.H., unpublished observations)."
        supports: claim
      - section: Original source P8-S3-C6
        page: 8
        quote: "These results indicate that Spt might be \nmore tightly coupled to a specific motor \neffector system, the vocal tract, than to a \nspecific sensory system."
        supports: claim
      - section: Original source P8-S3-C4
        page: 8
        quote: "Skilled \npianists were asked to listen to novel melo-\ndies and then to covertly reproduce them \nby either humming or imagining playing \nthem on a keyboard."
        supports: sample
      - section: Original source P8-S2-C7
        page: 8
        quote: "A network \nof regions was identified, including the pos-\nterior STS bilaterally, a left-dominant site \nin the Sylvian fissure at the boundary \nbetween the parietal and temporal lobes \n(area Spt), and left posterior frontal regions \n(FIG. 4)52,53."
        supports: method
    schema_version: '2.8'
    status: draft
    created_by: agent:relationship-converter
    created_on: '2026-11-24'
    relationship_review:
      paper: Hickok2007
      proposal_id: R010
      review_status_sha256: ef63ddb34895013b3db1661021d9b6efcf4e6d57005eeb884167168f27fe7cc2
      review_binding:
        version: candidate-inventory-v1
        input_hashes:
          pdf: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
        original_review_binding:
          version: relationship-review-v5
          input_hashes:
            pdf: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
            A/passages.json: 907c1915be60c97c7569c28ed3b1cd3cf233ef64214c93c874c84a6ba8d5991a
            A/raw.json: 0d92ffabcd811c15a00d09ee3eb8a5cd89b7ab77ef57184adf7051e13c2077ac
            A/source-units.json: 6653a2b26599062177ce2b9500b16427e2a805fe8eb8b2b2693e61f429f37384
            A/full-source-units.json: 6653a2b26599062177ce2b9500b16427e2a805fe8eb8b2b2693e61f429f37384
            A/meta.json: 58f43d078cf897a33075d49a40174056bd111b29022e4aab5a73ec5c2e4bf90f
            A/table-images/TABLE-1-page-5-1.png: 9025e74d97b7a453e2181219d835f0d49144c6d8ae9f91ba72bbb7374b10befd
            A/table-images/page-5.png: 3ea980326d20fe58b612ef64536ca085bb6ac49ec7aebd5e5d189993e222e623
            A/table-images/manifest.json: a0e06360ba3d3346627d4ceb4a6463a7090bb4b542bbbf3d5599b1e4d17d436f
            A/clauses/window-11/raw.json: f7b9a4f4131465763449d70999e6d25ae5be0fb5bb1160c281cc1a9c7db8fb3d
            A/clauses/window-11/prompt.txt: 3782aba25d5035e150c81ac5e47d2b78ce6f72b98a4f9811776d3377cfd4f0cc
            A/clauses/window-11/meta.json: c46d22db0ae725eb76abe2f31b6ab5b96e5e6dc1738934cc3bee1f1c777f7909
            A/clauses/window-16/raw.json: 31abf317f2f2316673dbd59da9854d21b4601c49b55b6a513d7f7219ce242917
            A/clauses/window-16/prompt.txt: 458c81e7c87d938dc2803577ff4db667db9f4c57adb04f4c72593d95e9e3660c
            A/clauses/window-16/meta.json: 8e5dbb65d5ab451807caa87145b116ec80cbaa2c2124ca15fd254fc4b915eb7b
            A/clauses/window-20/raw.json: bde48d2cf80136e5e5520a799379d67a95090ba329bb3ddd9a269366cc9e9465
            A/clauses/window-20/prompt.txt: 28e76f3955d9614c838d4e3f007972b66cfe3ed5552df2fb8272a0026745b8c7
            A/clauses/window-20/meta.json: 3ad62bf679a35b1bc062b4c1b3df486de4faf2358398c83550a3455c3ecf8249
            A/clauses/window-18/raw.json: 0457b703280d87f4dce29c03c5d679c545211515674e211c6933069078887d79
            A/clauses/window-18/prompt.txt: e504c00b97d539fe7529cfaaf91498c0f94c7d495354111b4f29796b3e79164e
            A/clauses/window-18/meta.json: 35bdce459ba9649e79dfd0df1c0030167383a7e323e15a53f9f32f3b2ce24e72
            A/clauses/window-19/raw.json: bbc8e218b1edb85cde0b71e18116f50c8beba0967bc5d04b5b2bb4fdb50825cd
            A/clauses/window-19/prompt.txt: 039074410b7de82f2978b89b3101596cec90a54a99942ce561a7447290859100
            A/clauses/window-19/meta.json: de609acebc620d429d68ebc37583a201d757c92488837143d466e780982552c5
            A/clauses/window-21/raw.json: 58d1501c9087ae195d8bd2cc63faee58292c342e643e1ea624618d64f4682339
            A/clauses/window-21/prompt.txt: 2c800272b42e1ff802475b9721bab8648c63ecfb49a309991f7964241372b90f
            A/clauses/window-21/meta.json: c3c95a6126f45c788fba643d6e85c4bbc67c520bc9aea0a7908533ffab304c46
            A/clauses/window-17/raw.json: f0fde1247bea343dcf9b37289470699f20a6f0e2cafc654b06ae11ef398531b4
            A/clauses/window-17/prompt.txt: 5a6f58fbfb42646ae4845a12294ea9528da376eda7f682c632745cb1ad539502
            A/clauses/window-17/meta.json: 5e7d512b80deee35e8b59c66a5893382794e7835dcb4467c831fdd703225db55
            A/clauses/window-10/raw.json: be65df56bbfd26a47154eb84ba613e04559ec986abdf048c82599222e2d6f18b
            A/clauses/window-10/prompt.txt: e0d0a3d580dd30195b91198484841967aae190e212285e70ad39d574db70faf6
            A/clauses/window-10/meta.json: f3f5d10a8b1dbf879f9b13ee13fa7aecdb9efc85163b2305665005a04de62820
            A/clauses/window-03/raw.json: ba660cde61e70845a1e5f445fd8bbe6c5025ccfd7a64f3be608cc7c55c381162
            A/clauses/window-03/prompt.txt: 99569569b31799c1cce7d450e2cf4fe31b6c76fea1d32ba93e251e06e4391316
            A/clauses/window-03/meta.json: 3fec4de411acaf3f92efc65c4a60e0c6ef76ef5e059b89665908548a57da922a
            A/clauses/window-04/raw.json: 3a5ebb2820dc16735f74050dcdcc6572654e00659ebd420dec80ee5f9b76589f
            A/clauses/window-04/prompt.txt: 6599869f7e7759a6b59afa8f7d7f879c64ecaac3c200f1b2226c02e2faa959a4
            A/clauses/window-04/meta.json: 406ba82c4c5896a48c0ae96e85dda38725d8dd156165a4a566a0a6c79db96011
            A/clauses/window-05/raw.json: cfe3412b81c03bad347868450c3ed6471f9a36dda27ab04cac0093f9cb21240e
            A/clauses/window-05/prompt.txt: 4e197710f939259b60546b7875a22c307dba14e055e8581f0857ce66b0712673
            A/clauses/window-05/meta.json: e882d4d2d262b868c66d350d388777b6d0bcbf561ce1d97389a69d17178427fe
            A/clauses/window-02/raw.json: 27a4f80ae2805a7da56b68e344f2fbd1e73f9bb4f44f25b801ecc22a79de0ae9
            A/clauses/window-02/prompt.txt: ce66ff9f6c7fe0be0e6ce548b8afca58e7fa2870a5d751c159cbdc1182198854
            A/clauses/window-02/meta.json: 69a3e29a8e035b299aaabc2b404372004a4df8705e610eaa494fa1537032c0cb
            A/clauses/window-15/raw.json: 4464530737a8dcaea34009059f82603ae16257e377740e61132357ba787eada8
            A/clauses/window-15/prompt.txt: a53ebf960406bfb0c767f6733485406c83a3472628d7e111fb89fc3acd3f06bb
            A/clauses/window-15/meta.json: 65aa8027cb833192688c2f57cf0a7bcf7f88226b2c7c286200097b3739a67eb1
            A/clauses/window-12/raw.json: b064fcb7776e2d133727d553e4aa4af229a83727756437c4a2214407e186adc4
            A/clauses/window-12/prompt.txt: f7fc1a91ffb612ea08512a8aa32b9d2466f3822dfcceb260eee6a5d700fbc6ae
            A/clauses/window-12/meta.json: f906239d3e870073fe0040e2d69d42d14c74b048cf6fcb2054255e3aad7efca6
            A/clauses/window-23/raw.json: b2dff731923ebf4a3a11d07a52340bef0b13951462e539f216556408b2764948
            A/clauses/window-23/prompt.txt: 4ddaeeacedf9975ab6a8619808a098e0571890fe919cde89f4eff17d90a9a5e7
            A/clauses/window-23/meta.json: e93f6aec90c2a8a5670e877431e9a856435d3b9da42ecc452e70b0c73928e56f
            A/clauses/window-22/raw.json: 6ff9f0bc1cbfee57b54cc346ade22a2d1381e12edeade2ceb2e7f493a93f42ae
            A/clauses/window-22/prompt.txt: c1c8bf6f6bf44d503f5078c8cb3ee96f2df2eb2739aa3351c70d006f5947b201
            A/clauses/window-22/meta.json: 7688175c9584fb89feb11d23597ccdc5566166d4eac517511976f7419101897e
            A/clauses/window-13/raw.json: eaab4eeadc9aaefc4426869f181dedc0470753bcc1f9ae747111a317af433593
            A/clauses/window-13/prompt.txt: 6b94f4a56417bcef16bcb9616fd1940760c9da0b7cb53fad576e0ceadd21e7e2
            A/clauses/window-13/meta.json: aca5e02ee19ff6a968b4b88ffc6ce22e6fa321c33b91dba111bbac80af64d4d2
            A/clauses/window-14/raw.json: 7e7d40979d4aff333bb805fec22691fbe5327ec4fc29c3b02d985b66215ee2e3
            A/clauses/window-14/prompt.txt: 1c9c2d1a39f1cc6ecbeac3c40f03df8854bfeed2d9664b880a71d92fe4a775a4
            A/clauses/window-14/meta.json: c5d0ad99f4833dd13606d05dfba8c33acb76ecd350ec2b8879815c810d9181c6
            A/clauses/window-09/raw.json: f683b48a92cf762fd4d8ecbac76a0f0546c170497b840a6588aa11b4c6009f4f
            A/clauses/window-09/prompt.txt: 84f7f4e5e4acca18323bc1b1c96e1882673a069cb956aa6c39f1b5e4fbd03bd3
            A/clauses/window-09/meta.json: af5dfafd32c10ecfca34fcbcce04039a3d43321a23ae2f99c6b7b049bfa0d519
            A/clauses/window-07/raw.json: 14aa931d624b495010e2fa8412c5289eba528cf10cb699367e354c254c3ef695
            A/clauses/window-07/prompt.txt: adfe8fe58687cf5ff8a30632983bb712fb76baf2b278d3eff54df9fa3f5425cf
            A/clauses/window-07/meta.json: 7633749f6c6cb3974ef8335f299858d4ff89ede901a94ee0fc56aa3fbc3ce42e
            A/clauses/window-01/raw.json: 936a071138a146942551cd1dc59b3b8d90aff9b87fa2f7a8ae95691fc33a4ae3
            A/clauses/window-01/prompt.txt: 9e914fe71b7ce5e0a526a462a202607e4629b7546d26030ecf6a5565871a70c6
            A/clauses/window-01/meta.json: fbf38f062ee3e66e2e69a389ad5e6fb20928a42b8142a4ce577bedbc749139e3
            A/clauses/window-06/raw.json: 2fefea3b969dfbd230a979ae876a92773c5b1512b20518fa80aa83153cdd9ff6
            A/clauses/window-06/prompt.txt: 0328e90c3505903a46a7972b0860a57c1c01663bb3f4585f54dc8227d574a3ee
            A/clauses/window-06/meta.json: 396e4050c0eeb6fce10ebf85d5e15d6f45aee8a2bd83d549943dea4fe1d08645
            A/clauses/window-08/raw.json: a7f37b924fde61dcb04a3040cb540c18c1ccfb8bc3c5ca2d918637ebd8936bae
            A/clauses/window-08/prompt.txt: 1930d20e7a08bb863a202cd0af128fe282daa1109d2ec06944590da1785c8ece
            A/clauses/window-08/meta.json: aa84afc97261877d2c9931a378c20a54933a16832b19d48076abb41a0ac1d585
            A/tables/TABLE-1-page-5-1/raw.json: 941c1907029814a8cf02c2b6045b08ec6d7a97dace3bd9d9487608507526a0d1
            A/tables/TABLE-1-page-5-1/prompt.txt: b384e13eb279bb80d607b0df16648ff947f48c54e70aa617446f897abdebe691
            A/tables/TABLE-1-page-5-1/meta.json: 88f5a6a6808d27644d6f9efbd400a5aafc4ea3db68111fdcb2a9e42b9396f472
            B/passages.json: 907c1915be60c97c7569c28ed3b1cd3cf233ef64214c93c874c84a6ba8d5991a
            B/raw.json: 2a4bb959b2419c44956fdb2577b23f5525634ac1629e3339c7ac143144ca75fc
            B/source-units.json: 6653a2b26599062177ce2b9500b16427e2a805fe8eb8b2b2693e61f429f37384
            B/full-source-units.json: 6653a2b26599062177ce2b9500b16427e2a805fe8eb8b2b2693e61f429f37384
            B/meta.json: 028626a50ddb53b1660ddb21313ac4a7fe4a179f2040a857d849b52010ff4435
            B/table-images/TABLE-1-page-5-1.png: 9025e74d97b7a453e2181219d835f0d49144c6d8ae9f91ba72bbb7374b10befd
            B/table-images/page-5.png: 3ea980326d20fe58b612ef64536ca085bb6ac49ec7aebd5e5d189993e222e623
            B/table-images/manifest.json: b7c9e5baf1fd8f4e2c84d28b181e026652ca6da193ca1e0dfbe9772668062ef4
            B/clauses/window-11/raw.json: 3a59ceeb07ecef9d7b8c466629170ea40830248ca9d5895dcde4c833b6f5d083
            B/clauses/window-11/prompt.txt: 3782aba25d5035e150c81ac5e47d2b78ce6f72b98a4f9811776d3377cfd4f0cc
            B/clauses/window-11/meta.json: bdccb98c2f571896a9168edaa82eebb3f9031ee18e2316c58025a5b50511320d
            B/clauses/window-16/raw.json: afdb16c7ad6b4aa71d01b315662673c3a38f6ce4913316de99a0f85bb28639fd
            B/clauses/window-16/prompt.txt: 458c81e7c87d938dc2803577ff4db667db9f4c57adb04f4c72593d95e9e3660c
            B/clauses/window-16/meta.json: 9c31d589be331c7fd04169ae3e6172330b7782136009fe5a9252e57351bcbdeb
            B/clauses/window-20/raw.json: cdb7747880649bd226e51c2e62284ae1660a1f4ae43cbc99750c25326dbb03bd
            B/clauses/window-20/prompt.txt: 28e76f3955d9614c838d4e3f007972b66cfe3ed5552df2fb8272a0026745b8c7
            B/clauses/window-20/meta.json: b651ec997796c2b6e147e4735033a83a5d051572b56a0fea434f6d27008105e4
            B/clauses/window-18/raw.json: 3cb88cf180d0315322cc3a25235c9413722e1d8dc48fac659da3a09998fb3cdf
            B/clauses/window-18/prompt.txt: e504c00b97d539fe7529cfaaf91498c0f94c7d495354111b4f29796b3e79164e
            B/clauses/window-18/meta.json: c95c2a949dc25d73bf27fbb7fa2eafda69e5397907873461c52016084f32bc1c
            B/clauses/window-19/raw.json: a805ee1877c7502dcd2dec775be0153bca5e36b17f6f24cd5435cdadeb4a6bc5
            B/clauses/window-19/prompt.txt: 039074410b7de82f2978b89b3101596cec90a54a99942ce561a7447290859100
            B/clauses/window-19/meta.json: 2a77a08cee295fa25e1804ce236775f503ec8f3691f8f5ff64f3ba7182f079ad
            B/clauses/window-21/raw.json: 549c5e0aab792365c81836963eaf2ce759bb724843e9327c6861ecd2f8686c5b
            B/clauses/window-21/prompt.txt: 2c800272b42e1ff802475b9721bab8648c63ecfb49a309991f7964241372b90f
            B/clauses/window-21/meta.json: 3e33739a418cc0c562044f174e8aa2a1485a6454fdbf7db0b853c5db31f51141
            B/clauses/window-17/raw.json: 2e748291cd8e9b63284f20b6039e4b9ce8e5f008c96d4e630af00c255942c3df
            B/clauses/window-17/prompt.txt: 5a6f58fbfb42646ae4845a12294ea9528da376eda7f682c632745cb1ad539502
            B/clauses/window-17/meta.json: 0a04e8125e89f3185be7e1831a3ee89d4840e27632470eefed71999192774f61
            B/clauses/window-10/raw.json: b98ba7937ae22eceaf10bceedee447c3d3dc3604f1fede5dfcacbba345c91c2d
            B/clauses/window-10/prompt.txt: e0d0a3d580dd30195b91198484841967aae190e212285e70ad39d574db70faf6
            B/clauses/window-10/meta.json: 7c594d9471de742ffa742b749b7ebc814bd90913047fa9b8eb4af8a9740794e4
            B/clauses/window-03/raw.json: e010678c8ff8fcb880e7997ee9be58914b41ed808924827113854f8f8eb9aed5
            B/clauses/window-03/prompt.txt: 99569569b31799c1cce7d450e2cf4fe31b6c76fea1d32ba93e251e06e4391316
            B/clauses/window-03/meta.json: 0c97551fdb9fcae1bb0b2c3e456b1ff2e1bc6c2a42834949e43547d2bc45905b
            B/clauses/window-04/raw.json: 7ed13e92bebac2ace02c231ea27d6beb1900decffb7c7c02d7384d61726afcd6
            B/clauses/window-04/prompt.txt: 6599869f7e7759a6b59afa8f7d7f879c64ecaac3c200f1b2226c02e2faa959a4
            B/clauses/window-04/meta.json: 543889edfbca36aa0eeed45753547278b31696c065444214112c443c521aeb9d
            B/clauses/window-05/raw.json: 21ea9670806eb81448f7739d7406ebe4e19b0f768ed584e3947a2af6ec495d71
            B/clauses/window-05/prompt.txt: 4e197710f939259b60546b7875a22c307dba14e055e8581f0857ce66b0712673
            B/clauses/window-05/meta.json: b4ad2b589b99744483f57901e17af828a7f70b8c5c1e7a5d960560914f062997
            B/clauses/window-02/raw.json: d4bd96702d5d1c4bd97769a6c6bd851c02f318b4bf68b04bea31342af8e479f4
            B/clauses/window-02/prompt.txt: ce66ff9f6c7fe0be0e6ce548b8afca58e7fa2870a5d751c159cbdc1182198854
            B/clauses/window-02/meta.json: 4cff04a875d1c1f11f5ed8a99c2ea8cfac658c002cafbde6e292327103e66177
            B/clauses/window-15/raw.json: 94af29ab2a1e5ca1101baf6e5ecd37c753b19424760300f0d309c7325ae4140b
            B/clauses/window-15/prompt.txt: a53ebf960406bfb0c767f6733485406c83a3472628d7e111fb89fc3acd3f06bb
            B/clauses/window-15/meta.json: f94d36c72a18dd567e296b44e69b62e4cae98c22bcf3b5063af4ad4df38917e4
            B/clauses/window-12/raw.json: 1d8f1581b1000fb2ccddc9163d2325f327377c49d012d5a402672de8ec69b82d
            B/clauses/window-12/prompt.txt: f7fc1a91ffb612ea08512a8aa32b9d2466f3822dfcceb260eee6a5d700fbc6ae
            B/clauses/window-12/meta.json: 17e35500b6acc6b91d2706346fe3245e3b42c446de08b4888c771d9c0552cd95
            B/clauses/window-23/raw.json: b2dff731923ebf4a3a11d07a52340bef0b13951462e539f216556408b2764948
            B/clauses/window-23/prompt.txt: 4ddaeeacedf9975ab6a8619808a098e0571890fe919cde89f4eff17d90a9a5e7
            B/clauses/window-23/meta.json: a53e5ebd72fc0ab700b5701443729f0ad611440124eadf3eff5bad86b0a0a727
            B/clauses/window-22/raw.json: e00ea7bec783c7eb474aefdb36ebf16d77feba42dbe66fe4fceb7b31a8adc7f2
            B/clauses/window-22/prompt.txt: c1c8bf6f6bf44d503f5078c8cb3ee96f2df2eb2739aa3351c70d006f5947b201
            B/clauses/window-22/meta.json: 14cb3cc866ebb74477b2314872c1fd60f3e79fab28c7b65067555e557d612fa0
            B/clauses/window-13/raw.json: 1ac56a16a5c8e7e85c9d4e1285c95b6f420a847aef08dc89d37840ef159c5054
            B/clauses/window-13/prompt.txt: 6b94f4a56417bcef16bcb9616fd1940760c9da0b7cb53fad576e0ceadd21e7e2
            B/clauses/window-13/meta.json: eadf28106df6dac0f087a68bc30f71767f579ff4b573a8211f5681895f531299
            B/clauses/window-14/raw.json: 9a7da223539b00581fa60fc8f7ea080de84a9686e0f3a2adfd269494c83bfdc5
            B/clauses/window-14/prompt.txt: 1c9c2d1a39f1cc6ecbeac3c40f03df8854bfeed2d9664b880a71d92fe4a775a4
            B/clauses/window-14/meta.json: 5f76551b58d231020a7d21f6041a15af27547e51fa6612158a38a205558af8f2
            B/clauses/window-09/raw.json: 3069970b4aed69b3fd74fd0ee5d73b1c4b875f4716784488ed64e686845d5284
            B/clauses/window-09/prompt.txt: 84f7f4e5e4acca18323bc1b1c96e1882673a069cb956aa6c39f1b5e4fbd03bd3
            B/clauses/window-09/meta.json: d3509cbdacaf2fa87788c29b33434272154a207c21db5b7adb6703ce94ab4330
            B/clauses/window-07/raw.json: 0e0db5aa1a74ecf05efb3184ba6798a46c2b5ffbdd4fd5fc6ee9cf7c7ef94ecc
            B/clauses/window-07/prompt.txt: adfe8fe58687cf5ff8a30632983bb712fb76baf2b278d3eff54df9fa3f5425cf
            B/clauses/window-07/meta.json: 23010ef527663db2e6cf76736c179f40a2f13871bf1df3fb5d296c32fea0a778
            B/clauses/window-01/raw.json: 507dc0207ebc60da89fdd92cb7e3c1faced94de7d0c8b64bf393b4ff727154be
            B/clauses/window-01/prompt.txt: 9e914fe71b7ce5e0a526a462a202607e4629b7546d26030ecf6a5565871a70c6
            B/clauses/window-01/meta.json: c7d85bd9f610cdfc11e16743972a41d77ebe9f1c7caa07abe1a6a334450f5162
            B/clauses/window-06/raw.json: 965d6731b4504d285f1fe42040b8b579cbb3700502b359323f6e25ca304168dd
            B/clauses/window-06/prompt.txt: 0328e90c3505903a46a7972b0860a57c1c01663bb3f4585f54dc8227d574a3ee
            B/clauses/window-06/meta.json: 595244d54a3ddae22439b26f885f2bd56a04b61760172badf98b529ac4510352
            B/clauses/window-08/raw.json: 987fc112165c9b7e29581f9803e7896ddd264dc1c30d8fce1db25bab65d2cb72
            B/clauses/window-08/prompt.txt: 1930d20e7a08bb863a202cd0af128fe282daa1109d2ec06944590da1785c8ece
            B/clauses/window-08/meta.json: c14a0a16480275cd89852d51f8cfc093c4cda0671f41d444d1b3132b351436f4
            B/tables/TABLE-1-page-5-1/raw.json: 0e85077d2c19c848a26792a9df67aa4814533625b9aa8d0ad310b1933a62c95d
            B/tables/TABLE-1-page-5-1/prompt.txt: b384e13eb279bb80d607b0df16648ff947f48c54e70aa617446f897abdebe691
            B/tables/TABLE-1-page-5-1/meta.json: 820ba16a5033110e3500f8ed9bc55274f8ca5d5bd04c9b501fc0e66004765a59
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
          pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
          source_review: _compare/relationships-2026-11-16/review-current/Hickok2007
          source_status_sha256: 15e7142713989de4b66ee158d05ad36c2ca3f3c491c6dee848d5672ea88ec739
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      proposal:
        id: R010
        exposure:
          text: area Spt activation
        outcome:
          text: vocal tract reproduction (humming)
        analysis_label: Spt area motor effector specificity
        relation: association
        evidence_ids:
        - P8-S3-C5
        qualifier_ids:
        - P8-S3-C6
        context_ids: []
        table_ids: []
        approved: false
        status: requires_source_review
        flags:
        - new_model_candidate_not_verified
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
          source_review: _compare/relationships-2026-11-16/review-current/Hickok2007
          source_status_sha256: 15e7142713989de4b66ee158d05ad36c2ca3f3c491c6dee848d5672ea88ec739
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      audit:
        original_audit:
          coverage_issues:
          - Result passage disposed without unit P4-S2-C6
          - Result passage disposed without unit P4-S2-C7
          - Result passage disposed without unit P4-S2-C8
          - Result passage disposed without unit P8-S3-C3
          unattached_null_or_qualifier_ids:
          - P4-S2-C5
          - P4-S2-C6
          - P9-S1-C2
          suppressed_nonrepresented_units: 14
          default_disposition_count_requires_completeness_check: 401
          unselected_timing_passages: []
          personal_effect_slots_without_result_classification: []
          held_frame_selections:
          - slot: dependent_variable_statement
            source_id: P8-S3-C5
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          empty_frame_slots_require_confirmation:
          - eligibility
          - imaging_timing
          - outcome_timing
          - validation
          - analysis_restrictions
          - personal_factors
          - tested_personal_effects
          - adjustment_roles
          - explicitly_not_adjusted
          unclassified_extraction_ids:
          - P9-S2-C10
          table_review_required:
          - TABLE-1-page-5-1
          unlinked_tables:
          - TABLE-1-page-5-1
          source_anomalies: []
          visual_review_required:
            scope: All main-paper figures and table crops
            note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
            caption_candidate_units:
            - P3-S3
            - P6-S3
            - P7-S2
            - P7-S3
            - P9-S4
          approval: Not performed. Structural checks and model selections do not establish semantic correctness.
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
          source_review: _compare/relationships-2026-11-16/review-current/Hickok2007
          source_status_sha256: 15e7142713989de4b66ee158d05ad36c2ca3f3c491c6dee848d5672ea88ec739
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        coverage:
        - source_id: P2-S1-C7
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses the logic of using sublexical tasks but is not a measured result.
        - source_id: P2-S1-C12
          disposition: represented
          result_indexes:
          - 0
          reason: Establishes the lack of correlation/prediction between speech perception and recognition.
        - source_id: P4-S2-C5
          disposition: background_or_descriptive
          result_indexes: []
          reason: States evidence exists for conjectures but does not provide the specific relationship.
        - source_id: P4-S2-C6
          disposition: background_or_descriptive
          result_indexes: []
          reason: References unpublished observations regarding performance changes.
        - source_id: P4-S2-C7
          disposition: represented
          result_indexes:
          - 4
          reason: Links right hemisphere to long-term integration.
        - source_id: P4-S2-C8
          disposition: represented
          result_indexes:
          - 4
          reason: Qualifies the left hemisphere's lack of selectivity.
        - source_id: P8-S3-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: Introduces the fact that Spt activity is modulated by output modality.
        - source_id: P8-S3-C5
          disposition: represented
          result_indexes:
          - 9
          reason: Reports higher Spt activity during humming vs playing.
        - source_id: P9-S1-C2
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes the proposed dominance of the dorsal stream.
        - source_id: P9-S4-C66
          disposition: background_or_descriptive
          result_indexes: []
          reason: Figure caption describing sensorimotor responses.
        - source_id: P9-S4-C67
          disposition: background_or_descriptive
          result_indexes: []
          reason: Figure caption noting bilateral/unilateral activation patterns.
        unresolved_coverage: []
        pending_source_ids:
        - P2-S1-C7
        - P4-S2-C5
        - P4-S2-C6
        - P4-S2-C8
        - P8-S3-C3
        - P9-S1-C2
        - P9-S4-C66
        - P9-S4-C67
        pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
        tables_requiring_review:
        - TABLE-1-page-5-1
        paper_complete: false
        approved: false
        policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
      study_frame:
        slots:
          analysed_sample:
          - P3-S1-C10
          - P3-S2-C1
          - P3-S2-C2
          - P3-S2-C3
          - P7-S3-C1
          - P8-S2-C5
          - P8-S3-C4
          recruited_sample:
          - P3-S1-C10
          - P3-S2-C1
          - P3-S2-C2
          - P3-S2-C3
          - P6-S2-C11
          - P6-S3-C9
          - P8-S3-C4
          eligibility: []
          imaging_provenance:
          - P3-S2-C4
          - P3-S2-C5
          - P5-S1-C4
          - P6-S2-C12
          - P7-S3-C1
          - P8-S2-C4
          imaging_timing: []
          outcome_timing: []
          outcome_definition:
          - P7-S3-C4
          - P8-S3-C5
          validation: []
          analysis_restrictions: []
          dependent_variable_statement:
          - P6-S1-C5
          - P7-S3-C4
          - P8-S2-C2
          limitations:
          - P2-S3-C8
          personal_factors: []
          tested_personal_effects: []
          adjustment_roles: []
          explicitly_not_adjusted: []
          descriptive_personal_factors:
          - P6-S3-C9
          - P8-S3-C4
        outcome_type: not_stated
        imaging_vs_outcome: not_stated
        validation_type: none_described
        window_merge: Union of selected IDs; differing window enums retained conservatively as both/mixed. Not verified study-level facts.
        held_selections:
        - slot: dependent_variable_statement
          source_id: P8-S3-C5
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original responses are preserved in frame/chunk-*/attempt-*/raw.json.
      approved: false
      source_check:
        profile: core
        scope: Independent model text review of core meaning; not human approval or complete PDF verification
        binding:
          profile: core
          version: core-source-check-v3
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          checker_model: qwen3.8:27b
          checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
          host: http://localhost:11434
          pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
          review_sha256: ef63ddb34895013b3db1661021d9b6efcf4e6d57005eeb884167168f27fe7cc2
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
          - P8-S3-C5
          source_result: In skilled pianists, area Spt was significantly more active during the humming condition (vocal tract reproduction) than during the imagining playing condition (keyboard reproduction), despite the playing condition being more difficult. This suggests Spt is more tightly coupled to the vocal tract effector system.
          result_status: detected
          patient_measurement: functional_imaging
          checks:
            analysis_identity:
              answer: fits
              reason: The selected analysis correctly identifies the comparison between humming and keyboard imagination conditions in skilled pianists as described in P8-S3-C5 and P8-S3-C4.
              source_ids:
              - P8-S3-C5
              - P8-S3-C4
            direction:
              answer: fits
              reason: The draft correctly states that Spt activation was higher during humming than playing, matching the source's finding of significant difference favoring the vocal tract effector.
              source_ids:
              - P8-S3-C5
            construct:
              answer: fits
              reason: The exposure (Spt activation) and outcome (vocal tract reproduction vs. other effector) are correctly identified. The measurement is functional imaging (fMRI), not lesion overlap or diffusion tractography.
              source_ids:
              - P8-S3-C5
              - P8-S2-C7
            qualifications:
              answer: fits
              reason: The draft includes the qualification that the playing condition was more difficult, which is explicitly stated in P8-S3-C5 and is material to interpreting the result (activation was higher for the easier task).
              source_ids:
              - P8-S3-C5
            missing_material_caveat:
              answer: fits
              reason: The draft notes that the finding is based on a review of functional imaging studies (specifically unpublished observations cited in the review), which is an appropriate limitation for this context. No other material caveats are omitted that would change the interpretation of this specific comparison.
              source_ids:
              - P8-S3-C5
          optional_pending:
          - Specific statistical values (p-values, t-statistics) for the Spt activation difference are not transcribed.
          - Exact coordinates or atlas definitions for area Spt are not transcribed.
          verdict: draft
          reason: All five core checks fit the source.
          material_issues: []
        pending_details:
        - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
        - Recovery phase is not classified; use the reported timing words.
        - Evidence-strength rating is a conservative draft placeholder pending human review.
        - Specific statistical values (p-values, t-statistics) for the Spt activation difference are not transcribed.
        - Exact coordinates or atlas definitions for area Spt are not transcribed.
        normalizations: []
        analysis_identity:
          id: R010
          exposure:
            text: area Spt activation
          outcome:
            text: vocal tract reproduction (humming)
          analysis_label: Spt area motor effector specificity
          relation: association
          evidence_ids:
          - P8-S3-C5
          qualifier_ids:
          - P8-S3-C6
          context_ids: []
          table_ids: []
          approved: false
          status: requires_source_review
          flags:
          - new_model_candidate_not_verified
          candidate_discovery:
            model: gemma4:31b
            model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
            pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
            source_review: _compare/relationships-2026-11-16/review-current/Hickok2007
            source_status_sha256: 15e7142713989de4b66ee158d05ad36c2ca3f3c491c6dee848d5672ea88ec739
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
      page: 8
      quote: "Spt was significantly \nmore active during the humming condi-\ntion than the playing condition, despite \nthe fact that the playing condition is more \ndifficult (G.H., unpublished observations)."
      status: pending
      by: agent:relationship-converter
      date: '2026-11-24'
      note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
  original_mapping:
    decision: draft
    reason: The source describes a functional imaging finding where area Spt activation was significantly higher during humming (vocal tract reproduction) compared to imagining playing a keyboard, supporting the claim that Spt is coupled to the vocal tract effector system.
    bucket: regions
    entity_id: area_spt
    name: area Spt cluster
    kind: network
    predictor_type: imaging_metric
    definition: fMRI activation in area Spt (a site in the Sylvian fissure at the boundary between the parietal and temporal lobes) during the reproduction of aurally perceived novel melodies
    assessment: []
    target: vocal_tract_reproduction
    target_kind: impairment
    claim: Area Spt was significantly more active during the humming condition than the imagining-playing-on-a-keyboard condition, suggesting it is more tightly coupled to the vocal tract motor effector system than to other effector systems.
    direction: likely
    method: fMRI_activation
    relationship: correlational
    therapy: null
    sample_n: null
    population: skilled pianists
    timing: concurrent
    qualifications:
    - the playing condition was reported to be more difficult than the humming condition
    limitations:
    - finding is based on a review of functional imaging studies
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P8-S3-C5
      supports: claim
    - source_id: P8-S3-C6
      supports: claim
    - source_id: P8-S3-C4
      supports: sample
    - source_id: P8-S2-C7
      supports: method
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
      review_sha256: ef63ddb34895013b3db1661021d9b6efcf4e6d57005eeb884167168f27fe7cc2
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
    proposal: R010
    status: draft
    reason: All five core checks fit the source.
    material_issues: []
    path: drafts/regions/area_spt__Hickok2007__R010.md
    seconds_this_run: 58.89072962499631
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 4d46e2ed0a0be5dc23e31b74eca951b19b14741ccfbd1c8d8f3fabda62365b74
      original_mapping_sha256: 7d04e469e26c3538ddfddab37d2496e57534fd76911818b6f7f1c7b2b516855a
      original_status_sha256: 0c4d5c4290d66247c2f6a4250923dd5fd02ca65887e0cb6d6439a8ee738741bd
      evidence_sha256: c6e22b99c50b22415fc695ab56b6423e667dc0e276f1a70943f2578e73f9661a
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 8
      note: Reclassified as a secondary review report, explicitly attributing the result to G.H.’s unpublished observations reported in this Opinion article. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: relationship-source-check
  page: 8
  quote: "Spt was significantly \nmore active during the humming condi-\ntion than the playing condition, despite \nthe fact that the playing condition is more \ndifficult (G.H., unpublished observations)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Reclassified as a secondary review report, explicitly attributing the result to G.H.’s unpublished observations reported in this Opinion article. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
