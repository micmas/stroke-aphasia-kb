---
id: left_slf_non_af
name: left SLF (non-AF) cluster
kind: network
findings:
- id: f1
  target: language_processing
  target_kind: impairment
  claim: The remaining parts of the SLF (excluding the AF component) were not related
    to language processing.
  direction: no_effect
  relationship: correlational
  method: LSM
  sample:
    n: not_reported
    population: individuals with aphasia due to left hemisphere stroke
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
  - Lesion location was not used as a covariate in correlational analyses
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a population reference
    tract template for the left superior longitudinal fasciculus, with the arcuate
    fasciculus mask subtracted to isolate the non-AF portion, measured via mean DTI
    indices (FA, MD, RD, AD). Analysis used partial correlations factoring out effects
    of age, time post-onset, and lesion size. Additional metadata has not been transcribed;
    review the pending-field flags before approval.'
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
    - proposed_concept:language_processing
  citation: '@Ivanova2016'
  source_passages:
  - section: Original source P12-S1-C8
    page: 12
    quote: 'The remaining parts of

      the SLF were not related to language processing.'
    supports: claim
  - section: Original source P7-S1-C4
    page: 7
    quote: 'Thus, to be able to differentiate the functional role of the

      SLF we subtracted the AF mask from the SLF mask followed by

      standard

      thresholding

      procedures

      described

      above.'
    supports: method
  - section: Original source P5-S2-C11
    page: 5
    quote: 'All in-

      dividuals in this group had aphasia resulting from single or

      multiple left-hemisphere strokes (bilateral strokes were

      excluded), the latest being not earlier than four months prior

      to scanning (M ¼ 26.38, SD ¼ 21.40 months post-onset; range:

      4e100 months).'
    supports: sample
  - section: Original source P7-S1-C15
    page: 7
    quote: 'Initially, partial regression plots be-

      tween language measures and mean DTI metrics were visu-

      ally

      examined

      to

      conﬁrm the

      absence

      of

      outliers

      and

      inﬂuential cases, while factoring out effects of age, time post-

      onset and lesion size.'
    supports: confounders
  - section: Original source P12-S2-C7
    page: 12
    quote: 'It should be acknowledged that the extent to which lan-

      guage deﬁcits are directly a result of white or grey matter

      involvement cannot be deﬁnitively determined here, as only

      lesion size (but not location) was used as a covariate in the

      correlational analyses.'
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Ivanova2016
  proposal_id: R010
  review_status_sha256: bd4370e9649b7b4bc7cba4f3b59861b7c19bfac30a8270f3fb2232a53cf85dfc
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: a578a68cf0df404ad55655a1393a67ae45fe75c2005f60ee6fc71951e7d648ca
    original_review_binding:
      version: relationship-review-v5
      input_hashes:
        pdf: a578a68cf0df404ad55655a1393a67ae45fe75c2005f60ee6fc71951e7d648ca
        A/passages.json: fad366d0e03b7a19706748cde1e7227624109b7f2747eedbf5e6d700b4d7915c
        A/raw.json: b2dcafe2ee072fe4dc12c507ed3e0e272c17ef6164779eb29621ec3872148815
        A/source-units.json: 38ef4e6a240833b5813fd2856b72cc59c8ce254fd66af15b1d6e4d128b830700
        A/full-source-units.json: 38ef4e6a240833b5813fd2856b72cc59c8ce254fd66af15b1d6e4d128b830700
        A/meta.json: a379a4b1bf1b91fd9dede7e48649904c50ad4347590de28c5c328d717af6878c
        A/table-images/manifest.json: 71a64de5adb053fd817490a02a7187c37f8bef4b0651d16a4186af677a48dcb3
        A/clauses/window-11/raw.json: 19395b9fe140846fea011fc5a732dc74f49d023a46230459e400170599316cd7
        A/clauses/window-11/prompt.txt: b9356c5d7b126e96e75407a3480b1a5bd412e7cd0125b0be2aaa67b67d2e466e
        A/clauses/window-11/meta.json: 258e84043b8a1732b1ad3b05e957bb65dbc39bafd2bbec1e80b6064636eeadfa
        A/clauses/window-16/raw.json: 0e637a3947cd2a48294b1f9d197d5e51c9bfa7761e51149a79c4839d8a8dc71e
        A/clauses/window-16/prompt.txt: 95ea39ae7a99c7c6d6820f8d92230efa487e3d37d88f17fe1742875c68136dd4
        A/clauses/window-16/meta.json: 3750590355c472ca9a907c6a06963348cdbaa506da5a393e74b759ccbcdbf70a
        A/clauses/window-20/raw.json: 8225a1399fdf0a4b0ed7a3792efd64868df84f0376f8111243b9ec330a1aab89
        A/clauses/window-20/prompt.txt: 0155b07ffe5a873149bd945b5a2a2364a63876323e88106189f6bca09b064e64
        A/clauses/window-20/meta.json: e19964f0e9f0d70a559fffa45e59d294538e9cf16b2f1f0ef9a8c9ac3ff1dd55
        A/clauses/window-18/raw.json: 3e8ce32f0e817beee470991ce0fa4a43b628774dcf823beb82334cf0fc944050
        A/clauses/window-18/prompt.txt: 4dcd4fd4bbe492fab7e49fea7e2baec0e357a934f683b748529fab0052638ac9
        A/clauses/window-18/meta.json: c43ce00023661912b9c1ff319ff58c0b11cac4d13f01197ea2547ec66e5f0443
        A/clauses/window-19/raw.json: b5590bbd009aff760cfac53fbf3350e21626c281ad00c019e0ac51201e8a4e19
        A/clauses/window-19/prompt.txt: 29a097e3456d1b030ad1458691a72ccbbd465c522b50a37ed7acd671b212457c
        A/clauses/window-19/meta.json: acb8d451b2f41a2b5c634dc52bbf28f1d00dc4d6dfa661ac18b0533f6d765b6c
        A/clauses/window-21/raw.json: faaa6624fdd9c309812e7cb21761c5e4cd385ccbe301fa10d54a9ee052520b3e
        A/clauses/window-21/prompt.txt: b39deb0871e8564109b486dacd0d9843c0b365f0830c36d8bdd389e18b17df4d
        A/clauses/window-21/meta.json: 7ac61bdee56d15fd54d8c6406fd19ae2352474ebdd4c90f0427569ef409f7674
        A/clauses/window-17/raw.json: 1072f3ab1df6340d2e2997654305776679fa5e6267f132fec2fedcdda4b43543
        A/clauses/window-17/prompt.txt: 2e10020c8f8280110995715a8b638cd1dda457684a662c34447bf691f754b9e8
        A/clauses/window-17/meta.json: bcd417dfb13c03046f835c7b466badb73f1c7ab1b481571bfae26147a673d860
        A/clauses/window-10/raw.json: 664b31d68e5a6b68be6adff454edc52461b29897aefb5b7faebbf39c912b602f
        A/clauses/window-10/prompt.txt: b4d6182c25572a37cd3e4f2e79fb0c808ba560d2b903ce20d9337b54ed5e673b
        A/clauses/window-10/meta.json: ee53e5af134ba174bb0decced8a122f09add9c991eb3a69116df93a892385944
        A/clauses/window-03/raw.json: 1c4922c2e8e663e042177470f2c8db91093ecd44bbe32d0611597694dba52e53
        A/clauses/window-03/prompt.txt: 9a2228322212a23b83b7ffd02ce1065e6c05efa66aac7c97e1ee23d9e28c97ec
        A/clauses/window-03/meta.json: 00e6d8edf0b3faa157943577704d07d0734c785501d43e7f209579943baf5a05
        A/clauses/window-04/raw.json: 7dafa6c80e6ed6e2f88e2563523576a46aec1543de42a26362c7aaadb164bfc2
        A/clauses/window-04/prompt.txt: 5a61e41d11665e710ac79ca7b493930de4784b4f08d9f52e1eabcd0dc6d09010
        A/clauses/window-04/meta.json: 80ea952f8a883df0e4feb37971174828238eacadbeee1559ee578a442714ef34
        A/clauses/window-05/raw.json: 5d989cf1f9648bec76a40cc685011d421defe129197e1a56db0d1713a0a2a973
        A/clauses/window-05/prompt.txt: 7b1b29ae22a6ebc4c379666eddd4a6ebee155812e947a1d8c326652eaefe97c7
        A/clauses/window-05/meta.json: 3b5e24bdc99d5d46f05f4ab0164022387973d59286a18af7bbf7086d929f5fd6
        A/clauses/window-02/raw.json: 99d0e718b27a9ebfb5fe562ee6687b1584acd392045d3a55cc2e82e90e6cea5c
        A/clauses/window-02/prompt.txt: fd9983f3d0ee63fceeed031b3117cc519d2b1dcff2e2fff87041b05f1dc46e9f
        A/clauses/window-02/meta.json: 7617a08e479bf1490ae15edc7f548975d511c3e109248a3e8c7915282dc2dc39
        A/clauses/window-15/raw.json: 3c8a0825eec433bd672378be3148f2572c4ef29b7aca7ad6bb3b91fb8e730238
        A/clauses/window-15/prompt.txt: 6c6b669f04a1fae4842bdcffdb046097d86268a00e35e456ed07bf89f432bc98
        A/clauses/window-15/meta.json: 881f7e1722fbd81354969a8f8608250dd3a66e6025fdcd53f10fbd0a57d682b9
        A/clauses/window-12/raw.json: c91946a174964e3863af4283a902641d878a7d0410a7ab618163b4a19f6aa23d
        A/clauses/window-12/prompt.txt: e9c8c61b11294f0d07a886c4c42f2bcaabc8a6aa3368d4c1d7fa52593631dc09
        A/clauses/window-12/meta.json: 4738d863a3cd761b20d7213ee56988ab235bbb8c6146936716c4ec48b6e0db1c
        A/clauses/window-24/raw.json: a56faa3843ca9fa42ad479a78fa472ca1cf5d02633c61ae70ec62ce4821ab77a
        A/clauses/window-24/prompt.txt: 6955c0ab18f9c2aeeddaf8c980a2e0ab07353bf9af93f2dc63982b8698d90705
        A/clauses/window-24/meta.json: 633302d005f7b51e81bc5692036742aac24db311eaa171ffb112b2220b709af4
        A/clauses/window-23/raw.json: 9886aa828ea0f6810d299b643691296317707d9fce0654dccdec6987363fea19
        A/clauses/window-23/prompt.txt: 3f82649b7b40b1c928a872770a6a1de80fb407b7378e4fc33857ba4f845887e1
        A/clauses/window-23/meta.json: 2a25635bdcd3aa00c98edf78b7f569a25e86082924780cccb0fff4e8cf624284
        A/clauses/window-22/raw.json: 73ba04d2dacafeacc678a54c1129916fedac660c775962b88268dabc2a1ed919
        A/clauses/window-22/prompt.txt: cbdb60b81823ef6827cbdb83a3659a98c8443d76d633176f0163a256a18dd3f2
        A/clauses/window-22/meta.json: fc3d1669e354e19fa07b277fdf3c6c0f73b5bcbd8228da651b2387cf4c0d632b
        A/clauses/window-13/raw.json: 48c3408e5a157eac6fb7ca5dd3f80d399cf7e0874ae7dfbd914ee5c903caa8d0
        A/clauses/window-13/prompt.txt: 1f9f1c1fcd31c4c7a4067ed1ac1a47a85c207746e313ebdc3792e4b801e7f303
        A/clauses/window-13/meta.json: d4d89dac98fb4bef19fd21af95affa9eef735920198acae7a7a137f724d79f92
        A/clauses/window-14/raw.json: 945ae0b116910fa6bafd5d0c443408db75c03ed6c736cd5dd2c0e33008985be8
        A/clauses/window-14/prompt.txt: f0aa14154a421a7b075dc4fd5ac2633abcc5f1730b3cb549a06534c0e1c13ae1
        A/clauses/window-14/meta.json: c3b4873a9f60e6c6d4bc96377484f50762b7d3941e36c6656c88e867cf02557f
        A/clauses/window-09/raw.json: c203d893d580051bcfbba85eca04c2bcdc66cc493e573e509a1ad3a224837cf4
        A/clauses/window-09/prompt.txt: 7f30e70a25d5201a26e27ca55f81470faf093fea54f80b25bd0d82a914ba49d3
        A/clauses/window-09/meta.json: 27612038ca289f940131bc22d8f64c1851a211a4dbd61fafe2f222ee7859f99c
        A/clauses/window-07/raw.json: 30083c9ce1230a7b556ccb09a6baf872495dd85b4380d9098c749305f17cb180
        A/clauses/window-07/prompt.txt: c9bd1919e5d536150443a0901deaba14970d4480e2407e0f2b17e061f5b4e934
        A/clauses/window-07/meta.json: b9ffb4399f0678aa5622ffff7de2f0b91e5b04360e7ff4777f354a8d2982cb32
        A/clauses/window-01/raw.json: 0acb736dbb8b69ed6f147530c2ebe367f0939367b62ef1deb19fc87722bd5a8d
        A/clauses/window-01/prompt.txt: a7c3f71cb920ff95d7a6424ee320d0e3035673be59200bd61be3ddc3ee701aff
        A/clauses/window-01/meta.json: 8a6cba90c1d1e4f8eda612d5953df37f9730abc54a7275834e82cafb100e5779
        A/clauses/window-06/raw.json: 7a10a6776c48100a11c1a440345ba3d8ea47037eaeb27bc2c5d206256ec9ef55
        A/clauses/window-06/prompt.txt: 24d484ab53e28ab09e6fbc5c0b996d9c7732331b404feb135f00b4488da1fcef
        A/clauses/window-06/meta.json: 6a8da23282d85baa2290b6453fdb5ca13d89fd7c83fd88b966f4304c3b165289
        A/clauses/window-08/raw.json: 3661ed7dfa3bc2f8f4f2a5c8a0c957d6d7545d442616479544739d78a9a1536e
        A/clauses/window-08/prompt.txt: 0b74ac8e0a49eecfceded78f5512f90eba65899063e2a62aa97afaa60073beff
        A/clauses/window-08/meta.json: 93a6348963f07897122dac9b73bd139edd90751f4a140c6b563b1082d6ce9cc8
        B/passages.json: fad366d0e03b7a19706748cde1e7227624109b7f2747eedbf5e6d700b4d7915c
        B/raw.json: cca0343c215c6883ef8c9d71a579aa06ded0e19820ef5cf8f40aee3f877245cb
        B/source-units.json: 38ef4e6a240833b5813fd2856b72cc59c8ce254fd66af15b1d6e4d128b830700
        B/full-source-units.json: 38ef4e6a240833b5813fd2856b72cc59c8ce254fd66af15b1d6e4d128b830700
        B/meta.json: 86c8722df6d6b5a38e661247cc08894edc9fec8112e8b17e67a000fa90980cbf
        B/table-images/manifest.json: 71a64de5adb053fd817490a02a7187c37f8bef4b0651d16a4186af677a48dcb3
        B/clauses/window-11/raw.json: 5be9f287bcbc22bba3ea4468d6591784f92cad461196857b6c12e830b03e4cc2
        B/clauses/window-11/prompt.txt: b9356c5d7b126e96e75407a3480b1a5bd412e7cd0125b0be2aaa67b67d2e466e
        B/clauses/window-11/meta.json: c9a48a81de1481dad598b4575e78d2551a4c5b04a8742667889a5ace69c75092
        B/clauses/window-16/raw.json: 302bcd3d060056fb68c45c3cfefe621aa462cc2ae29e57678e08405fc4fa508a
        B/clauses/window-16/prompt.txt: 95ea39ae7a99c7c6d6820f8d92230efa487e3d37d88f17fe1742875c68136dd4
        B/clauses/window-16/meta.json: be1b0f07a41af518438a5d2bc2083019eda8f23ac05cd6dacea17547cad2dab7
        B/clauses/window-20/raw.json: c48bbdd84a1dc373080fa3bb6ffcde81da92f5309e865f02f295fb8e8d0434fa
        B/clauses/window-20/prompt.txt: 0155b07ffe5a873149bd945b5a2a2364a63876323e88106189f6bca09b064e64
        B/clauses/window-20/meta.json: 1c7d84ea5069be1ffd335a7fc6c21b6f30939ffe87b9dc7e86f4faec74a960ca
        B/clauses/window-18/raw.json: 6ba46feda368840f6627eea12a20e29e040478ff9ca4b8d97b749e3374e5a074
        B/clauses/window-18/prompt.txt: 4dcd4fd4bbe492fab7e49fea7e2baec0e357a934f683b748529fab0052638ac9
        B/clauses/window-18/meta.json: 8cf1d03300a7acbc355f1e543b5ed3249b1b07b9199083bab6c1ba8adf37d9ff
        B/clauses/window-19/raw.json: 9441b1188df02f2989386465b960e18aaa78744736669d3f6de3f191208a8267
        B/clauses/window-19/prompt.txt: 29a097e3456d1b030ad1458691a72ccbbd465c522b50a37ed7acd671b212457c
        B/clauses/window-19/meta.json: 0574e4ad78b365033b20e9b305b7dff8b0be340c64fc5133090be91d04dec218
        B/clauses/window-21/raw.json: 4b661c270e2f763182cf0651788fcf7662010a5632a10c37ba63ce786d03df01
        B/clauses/window-21/prompt.txt: b39deb0871e8564109b486dacd0d9843c0b365f0830c36d8bdd389e18b17df4d
        B/clauses/window-21/meta.json: 55a0fb8e93ceaae4d5d9ccf4f7c1c1499fa0a96a57264f27e2047263210e353a
        B/clauses/window-17/raw.json: c4aa26ba383df24010a6d5e6c0b05f481da6cbf3a7bf57168043706409a9056a
        B/clauses/window-17/prompt.txt: 2e10020c8f8280110995715a8b638cd1dda457684a662c34447bf691f754b9e8
        B/clauses/window-17/meta.json: 8a4d025b816cd10ab5b4a97d29549336ae1b791c68d3bc69442b8dab6dd635c3
        B/clauses/window-10/raw.json: b3a9de3ae94dfaff98795da09ff413a58c9f30ef5c77b3663e537cf8df3e9fca
        B/clauses/window-10/prompt.txt: b4d6182c25572a37cd3e4f2e79fb0c808ba560d2b903ce20d9337b54ed5e673b
        B/clauses/window-10/meta.json: 7356b9ab8c48af8814804544babe237c75d72c385917ecfcc19feb7d215c4640
        B/clauses/window-03/raw.json: 4335ee8c54c2d4bc06b24d53f49b134037314c6310715d69c2a925035ce1ce23
        B/clauses/window-03/prompt.txt: 9a2228322212a23b83b7ffd02ce1065e6c05efa66aac7c97e1ee23d9e28c97ec
        B/clauses/window-03/meta.json: a6d50fe2361322ec9fdb3f7c2335f4623504c3a8e4efc9326704601d15f8efe7
        B/clauses/window-04/raw.json: d79f603c29a9c6f5c65f70f6096303cd1296a8fba47c686b3a41cb0ade5165e2
        B/clauses/window-04/prompt.txt: 5a61e41d11665e710ac79ca7b493930de4784b4f08d9f52e1eabcd0dc6d09010
        B/clauses/window-04/meta.json: 6bd706ba7ea3b3f83c8ae427b6b9874fad307c3db9c68a5322eee8e91f20e47b
        B/clauses/window-05/raw.json: d68eaf56e50e71b455356b302ac9cdb9b3eccc03ab961b93f0164446882e9566
        B/clauses/window-05/prompt.txt: 7b1b29ae22a6ebc4c379666eddd4a6ebee155812e947a1d8c326652eaefe97c7
        B/clauses/window-05/meta.json: d02349abbc9fcf52d2ea582510781cefe52a41047f9821cf40076eeb30072031
        B/clauses/window-02/raw.json: 02ba220ed2284cf596402af1da18d226ea4327fd7ff17d069c439a3214196768
        B/clauses/window-02/prompt.txt: fd9983f3d0ee63fceeed031b3117cc519d2b1dcff2e2fff87041b05f1dc46e9f
        B/clauses/window-02/meta.json: 1cbd1d545a99bc5f663328c5fce3647f190bff83daff8b01fa4a03a62d069e77
        B/clauses/window-15/raw.json: 995ab3a8a972e68ce0fc00bd67abdd6faddf57f5ce432da2136f1a6751b336ec
        B/clauses/window-15/prompt.txt: 6c6b669f04a1fae4842bdcffdb046097d86268a00e35e456ed07bf89f432bc98
        B/clauses/window-15/meta.json: 492e7b5d61ca41064dc86d23ca0bca8ee5895dbfff0016a2580cd577a9986d9c
        B/clauses/window-12/raw.json: 3456befe7cb0daf50ff5ecb0f102d8001024eeb94b69c34a708984064a6fc184
        B/clauses/window-12/prompt.txt: e9c8c61b11294f0d07a886c4c42f2bcaabc8a6aa3368d4c1d7fa52593631dc09
        B/clauses/window-12/meta.json: 78cb23e1afe8a962ae0f0a2f56f54d8bff30423f46d4588bf837b4fbb4094790
        B/clauses/window-24/raw.json: a631729e66ef05912e72c54a050a5dfb03cb7e0460982f17ba05320f9ae964fa
        B/clauses/window-24/prompt.txt: 6955c0ab18f9c2aeeddaf8c980a2e0ab07353bf9af93f2dc63982b8698d90705
        B/clauses/window-24/meta.json: d659a66d1fa3519a672b2fa5e553d5270e3b0ec3526b6057f7ddd712f22edcd4
        B/clauses/window-23/raw.json: f6da28f5d291681e77cae2b3916e5ede43da825afc0ba5da7143fe27269142a7
        B/clauses/window-23/prompt.txt: 3f82649b7b40b1c928a872770a6a1de80fb407b7378e4fc33857ba4f845887e1
        B/clauses/window-23/meta.json: 02bbe3a7ad22806272b89cd7c74bff05dae4ed807d9037fb60dd19255e09c090
        B/clauses/window-22/raw.json: f85d655521e43d5f6b5d84544e3807e81c6b4e6c9fe11a54c51fcaffafb97f11
        B/clauses/window-22/prompt.txt: cbdb60b81823ef6827cbdb83a3659a98c8443d76d633176f0163a256a18dd3f2
        B/clauses/window-22/meta.json: 457f6e76c87d146e16eac86ad4fd2f6b51843eb8bb10a37dab6fae129999fb49
        B/clauses/window-13/raw.json: 58f9a26e9171b5f5c3d964ca6b0bcee8d75dd8de91a59c9ee64ba355604bfbc6
        B/clauses/window-13/prompt.txt: 1f9f1c1fcd31c4c7a4067ed1ac1a47a85c207746e313ebdc3792e4b801e7f303
        B/clauses/window-13/meta.json: de8377c81be1d4b92c761d921b15a62350f3d29aaaad11792b6925670a58c44a
        B/clauses/window-14/raw.json: ce0cb2015a1b4fdbe43d4126f48eb1daec7e56befb311ccf71bd95ac9a2d956a
        B/clauses/window-14/prompt.txt: f0aa14154a421a7b075dc4fd5ac2633abcc5f1730b3cb549a06534c0e1c13ae1
        B/clauses/window-14/meta.json: 155354ee947be99345a7b0738c1371fc53013ec3755ce8c0be5cc9c52ff4f200
        B/clauses/window-09/raw.json: a1e7c5634fbf242d2ddf02923e1514b02cad421bb05652e1324ebd9f9ccc8771
        B/clauses/window-09/prompt.txt: 7f30e70a25d5201a26e27ca55f81470faf093fea54f80b25bd0d82a914ba49d3
        B/clauses/window-09/meta.json: 8e8333d2838416661d80f225d18c51348fd2baa14f21035e2225ce2cd0553356
        B/clauses/window-07/raw.json: a23165deb233b4f8bbea84a68e742a71549a110c6ad0ffc7e929d67ddfe20408
        B/clauses/window-07/prompt.txt: c9bd1919e5d536150443a0901deaba14970d4480e2407e0f2b17e061f5b4e934
        B/clauses/window-07/meta.json: f0e1d9d194f7901d4db819658ba75c197691ccbfdd25217f0c4207596f5d3691
        B/clauses/window-01/raw.json: d6e6673a86989fbba2655a09f3cffee4cb47583b5d04d5fa27f74786a3738287
        B/clauses/window-01/prompt.txt: a7c3f71cb920ff95d7a6424ee320d0e3035673be59200bd61be3ddc3ee701aff
        B/clauses/window-01/meta.json: f49a79f7da9205a5408e20ded6fc378c1957563d582414a4a07aecb061db2a49
        B/clauses/window-06/raw.json: 32f9202602a7986a06629f6bcbc8c1e68243251ad3cb9614d2f407d225f18a41
        B/clauses/window-06/prompt.txt: 24d484ab53e28ab09e6fbc5c0b996d9c7732331b404feb135f00b4488da1fcef
        B/clauses/window-06/meta.json: 1ca7649c2290bfeaa8e243e15d2004a68db45b0850140c0031ddad7142221062
        B/clauses/window-08/raw.json: 23b444f6119cef2fb4b9f46e03a8d13ce5febcfaf593ca0b2c53072326dabbee
        B/clauses/window-08/prompt.txt: 0b74ac8e0a49eecfceded78f5512f90eba65899063e2a62aa97afaa60073beff
        B/clauses/window-08/meta.json: 10582a7e479c3bbf16020376eb32bf2783532e852bfbf29e88f436b68b10f26c
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
      pdf_sha256: a578a68cf0df404ad55655a1393a67ae45fe75c2005f60ee6fc71951e7d648ca
      source_review: _compare/relationships-2026-11-16/review-current/Ivanova2016
      source_status_sha256: 6728000e53f4471e699ca7c19d667031b0ba1d523caea3f988232c36c6ffc3b8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R010
    exposure:
      text: left SLF (non-AF) integrity
    outcome:
      text: language processing
    analysis_label: Tract segment correlational analysis
    relation: association
    evidence_ids:
    - P12-S1-C8
    qualifier_ids:
    - P8-S2-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a578a68cf0df404ad55655a1393a67ae45fe75c2005f60ee6fc71951e7d648ca
      source_review: _compare/relationships-2026-11-16/review-current/Ivanova2016
      source_status_sha256: 6728000e53f4471e699ca7c19d667031b0ba1d523caea3f988232c36c6ffc3b8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Accounting without a linked unit P5-S3-C4
      - Unaccounted source passage P5-S3-C4
      - Result passage disposed without unit P7-S2-C6
      - Accounting without a linked unit P7-S2-C8
      - Unaccounted source passage P7-S2-C8
      - 'window 10: invalid/duplicate disposition P8-S1-C3'
      - 'window 10: invalid/duplicate disposition P8-S1-C4'
      - Result passage disposed without unit P8-S1-C4
      - 'window 10: invalid/duplicate disposition P8-S1-C5'
      - Result passage disposed without unit P8-S1-C5
      - Result passage disposed without unit P8-S1-C10
      - Accounting without a linked unit P8-S1-C11
      - Result passage disposed without unit P8-S1-C9
      - Unaccounted source passage P8-S1-C11
      - Accounting without a linked unit P8-S2-C2
      - Accounting without a linked unit P8-S2-C3
      - Accounting without a linked unit P8-S2-C5
      - Unaccounted source passage P8-S2-C5
      - Unaccounted source passage P8-S2-C2
      - Unaccounted source passage P8-S2-C3
      - Result passage disposed without unit P12-S2-C6
      - Accounting without a linked unit P12-S2-C9
      - Result passage disposed without unit P13-S1-C1
      - Unaccounted source passage P12-S2-C9
      - Result passage disposed without unit P13-S1-C10
      - Accounting without a linked unit P13-S1-C11
      - Result passage disposed without unit P13-S1-C12
      - Result passage disposed without unit P13-S1-C2
      - Unaccounted source passage P13-S1-C11
      - Result passage disposed without unit P13-S3-C4
      - Result passage disposed without unit P13-S3-C5
      - Result passage disposed without unit P13-S3-C12
      - Result passage disposed without unit P13-S4-C2
      - Result passage disposed without unit P13-S4-C3
      unattached_null_or_qualifier_ids:
      - P8-S2-C2
      - P8-S2-C3
      - P8-S2-C5
      - P13-S1-C2
      suppressed_nonrepresented_units: 8
      default_disposition_count_requires_completeness_check: 278
      unselected_timing_passages:
      - P5-S2-C9
      - P5-S2-C11
      - P5-S3-C3
      - P8-S3-C2
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P2-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P6-S3-C12
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S1-C14
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C8
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P8-S2-C9
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S2-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P12-S3-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S1-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S2-C11
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P13-S3-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C28
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S4-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P7-S2-C7
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysed_sample
        source_ids:
        - P1-S1-C12
        - P5-S1-C7
        - P5-S2-C9
        - P5-S3-C3
        - P6-S3-C9
        - P8-S1-C7
        - P8-S1-C8
        - P8-S1-C14
        - P8-S1-C15
        - P8-S2-C3
        - P8-S2-C5
        - P8-S2-C8
        - P8-S2-C9
        - P8-S3-C2
        - P11-S1-C3
        - P13-S1-C2
        - P13-S3-C9
        - P14-S2-C28
        - P16-S4-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C12
        - P5-S1-C7
        - P5-S2-C9
        - P5-S3-C3
        - P8-S1-C3
        - P8-S3-C2
        - P11-S1-C3
        - P13-S1-C2
        - P14-S1-C3
        - P14-S1-C5
        - P14-S2-C28
        - P16-S4-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P1-S2-C3
        - P5-S1-C7
        - P6-S2-C8
        - P6-S2-C9
        - P6-S2-C10
        - P6-S3-C14
        - P6-S3-C15
        - P7-S1-C9
        - P8-S3-C2
        - P11-S2-C4
        - P12-S2-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: outcome_definition
        source_ids:
        - P1-S1-C11
        - P2-S1-C2
        - P5-S1-C7
        - P5-S3-C7
        - P5-S3-C8
        - P6-S2-C2
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        - P6-S2-C7
        - P6-S3-C12
        - P7-S1-C8
        - P12-S1-C3
        - P12-S1-C10
        - P12-S2-C10
        - P12-S3-C1
        - P13-S1-C10
        - P13-S1-C11
        - P13-S2-C3
        - P16-S4-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P4-S2-C11
        - P4-S2-C12
        - P4-S2-C13
        - P4-S3-C2
        - P4-S3-C3
        - P4-S3-C6
        - P4-S3-C7
        - P4-S4-C1
        - P11-S1-C4
        - P12-S1-C2
        - P12-S2-C4
        - P12-S2-C7
        - P13-S1-C5
        - P13-S2-C10
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: descriptive_personal_factors
        source_ids:
        - P1-S1-C12
        - P5-S2-C9
        - P5-S2-C10
        - P5-S2-C11
        - P5-S2-C12
        - P5-S3-C2
        - P5-S3-C3
        - P5-S3-C4
        - P8-S1-C16
        - P8-S3-C2
        - P11-S1-C8
        - P13-S1-C2
        - P13-S3-C9
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - analysed_sample
      - recruited_sample
      - imaging_provenance
      - outcome_definition
      - validation
      - limitations
      - explicitly_not_adjusted
      - descriptive_personal_factors
      unclassified_extraction_ids: []
      table_review_required: []
      unlinked_tables: []
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P7-S1
        - P7-S3
        - P8-S1
        - P8-S2
        - P8-S3
        - P9-S2
        - P11-S2
        - P12-S2
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: a578a68cf0df404ad55655a1393a67ae45fe75c2005f60ee6fc71951e7d648ca
      source_review: _compare/relationships-2026-11-16/review-current/Ivanova2016
      source_status_sha256: 6728000e53f4471e699ca7c19d667031b0ba1d523caea3f988232c36c6ffc3b8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P2-S1-C1
      disposition: represented
      result_indexes:
      - 0
      reason: States aphasia group had lower FA in LH and higher MD, RD, AD in LH/RH
        compared to controls.
    - source_id: P2-S1-C2
      disposition: represented
      result_indexes:
      - 3
      reason: Relates comprehension to left IFOF/ILF and production to left AF.
    - source_id: P2-S1-C3
      disposition: represented
      result_indexes:
      - 6
      reason: States individual segments of AF, IFOF, ILF were differentially associated
        with production and comprehension.
    - source_id: P5-S3-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia subtype distribution.
    - source_id: P5-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes age difference between groups.
    - source_id: P7-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes co-registration quality assessment.
    - source_id: P7-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Validates T1 space for FA extraction.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion location distribution.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap in white matter.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes lesion overlap in cortex.
    - source_id: P8-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Reports lower FA in all LH tracts for aphasia group.
    - source_id: P8-S1-C8
      disposition: represented
      result_indexes:
      - 0
      reason: Reports higher MD, AD, RD for LH tracts in aphasia group.
    - source_id: P8-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      reason: Visual representation of FA differences.
    - source_id: P8-S1-C10
      disposition: represented
      result_indexes:
      - 2
      reason: Reports no significant differences in control group except for ILF,
        SLF, CST.
    - source_id: P8-S1-C11
      disposition: represented
      result_indexes:
      - 2
      reason: Right ILF higher FA than left ILF in controls.
    - source_id: P8-S1-C12
      disposition: represented
      result_indexes:
      - 2
      reason: Left SLF higher RD than right SLF in controls.
    - source_id: P8-S1-C13
      disposition: represented
      result_indexes:
      - 2
      reason: Left CST higher RD than right CST in controls.
    - source_id: P8-S1-C14
      disposition: represented
      result_indexes:
      - 1
      reason: Reports significant differences for all major tracts and indices in
        aphasia group.
    - source_id: P8-S1-C15
      disposition: represented
      result_indexes:
      - 1
      reason: Lower FA in LH vs RH, higher MD, RD, AD in LH vs RH for aphasia group.
    - source_id: P8-S2-C2
      disposition: represented
      result_indexes:
      - 5
      reason: No significant results for major RH tracts.
    - source_id: P8-S2-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Only FA for left AF, ILF, IFOF significantly related to language.
    - source_id: P8-S2-C5
      disposition: represented
      result_indexes:
      - 4
      reason: MD, AD, RD not significantly related to language (except AF/CC splenium
        and naming).
    - source_id: P8-S2-C10
      disposition: represented
      result_indexes:
      - 6
      reason: Inferior ventral AF related to comprehension; middle AF related to production.
    - source_id: P8-S2-C11
      disposition: represented
      result_indexes:
      - 7
      reason: Middle/posterior ILF and IFOF related to comprehension; anterior segments
        related to production.
    - source_id: P10-S1-C3
      disposition: represented
      result_indexes:
      - 1
      reason: LH tracts had lower FA and higher MD, RD, AD than RH tracts in aphasia
        group.
    - source_id: P10-S1-C4
      disposition: represented
      result_indexes:
      - 2
      reason: Control group inter-hemispheric differences only in ILF (higher FA in
        RH).
    - source_id: P11-S1-C2
      disposition: represented
      result_indexes:
      - 0
      reason: Intergroup differences in FA, MD, RD, AD for AF, ILF, IFOF in RH.
    - source_id: P11-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post-hoc correlational analysis between CC and RH tracts.
    - source_id: P11-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: RH tracts showed greater differences from controls specifically in RD.
    - source_id: P11-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Post-hoc correlations between age and DTI indices in RH.
    - source_id: P11-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Age relationship not significant for controls or LH tracts.
    - source_id: P12-S1-C3
      disposition: represented
      result_indexes:
      - 3
      reason: Comprehension related to left IFOF/ILF; production related to left AF.
    - source_id: P12-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: No contribution of UF to language processing.
    - source_id: P12-S1-C8
      disposition: represented
      result_indexes:
      - 9
      reason: Remaining parts of SLF not related to language processing.
    - source_id: P12-S1-C10
      disposition: represented
      result_indexes:
      - 5
      reason: No significant relationship between RH DTI indices and language processing.
    - source_id: P13-S1-C11
      disposition: represented
      result_indexes:
      - 6
      reason: Inferior ventral AF FA related to comprehension and production.
    - source_id: P13-S2-C3
      disposition: represented
      result_indexes:
      - 6
      reason: Middle AF FA related exclusively to production.
    - source_id: P13-S2-C11
      disposition: represented
      result_indexes:
      - 7
      reason: Middle and posterior IFOF/ILF FA strongly related to comprehension.
    - source_id: P13-S3-C3
      disposition: represented
      result_indexes:
      - 7
      reason: Anterior IFOF/ILF moderately associated with production.
    - source_id: P8-S3-C3
      disposition: represented
      result_indexes:
      - 0
      reason: Aphasia group had lower FA in LH and higher MD, RD, AD in LH and some
        RH tracts.
    unresolved_coverage:
    - source_id: P8-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S1-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P12-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C1
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S1-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S2-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C4
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S3-C12
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S4-C2
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P13-S4-C3
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P5-S3-C2
    - P5-S3-C4
    - P7-S2-C6
    - P7-S2-C8
    - P8-S1-C3
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C9
    - P8-S2-C9
    - P11-S1-C2
    - P11-S1-C5
    - P11-S1-C7
    - P11-S1-C9
    - P11-S1-C10
    - P12-S1-C7
    - P12-S2-C6
    - P12-S2-C9
    - P13-S1-C1
    - P13-S1-C2
    - P13-S1-C10
    - P13-S1-C12
    - P13-S2-C9
    - P13-S2-C12
    - P13-S3-C4
    - P13-S3-C5
    - P13-S3-C11
    - P13-S3-C12
    - P13-S4-C2
    - P13-S4-C3
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
      - P1-S1-C12
      - P5-S2-C10
      - P5-S2-C11
      - P5-S2-C12
      - P11-S1-C3
      imaging_provenance: []
      imaging_timing:
      - P11-S1-C4
      - P12-S2-C4
      - P16-S4-C5
      outcome_timing:
      - P12-S1-C1
      - P12-S2-C4
      - P16-S4-C5
      outcome_definition: []
      validation: []
      analysis_restrictions:
      - P12-S2-C7
      dependent_variable_statement:
      - P1-S1-C11
      - P5-S1-C7
      - P5-S2-C5
      - P6-S2-C7
      limitations: []
      personal_factors:
      - P8-S1-C16
      - P8-S2-C8
      - P11-S1-C8
      - P11-S1-C9
      - P11-S1-C10
      tested_personal_effects:
      - P11-S1-C9
      adjustment_roles:
      - P5-S1-C5
      - P7-S1-C15
      - P8-S1-C16
      - P8-S2-C8
      - P10-S2-C1
      - P12-S2-C7
      explicitly_not_adjusted: []
      descriptive_personal_factors: []
    outcome_type: both_reported
    imaging_vs_outcome: mixed
    validation_type: mixed
    window_merge: Union of selected IDs; differing window enums retained conservatively
      as both/mixed. Not verified study-level facts.
    held_selections:
    - slot: dependent_variable_statement
      source_id: P2-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S3-C12
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C14
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C8
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P8-S2-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S2-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P12-S3-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S2-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P13-S3-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P14-S2-C28
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S4-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P7-S2-C7
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysed_sample
      source_ids:
      - P1-S1-C12
      - P5-S1-C7
      - P5-S2-C9
      - P5-S3-C3
      - P6-S3-C9
      - P8-S1-C7
      - P8-S1-C8
      - P8-S1-C14
      - P8-S1-C15
      - P8-S2-C3
      - P8-S2-C5
      - P8-S2-C8
      - P8-S2-C9
      - P8-S3-C2
      - P11-S1-C3
      - P13-S1-C2
      - P13-S3-C9
      - P14-S2-C28
      - P16-S4-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: recruited_sample
      source_ids:
      - P1-S1-C12
      - P5-S1-C7
      - P5-S2-C9
      - P5-S3-C3
      - P8-S1-C3
      - P8-S3-C2
      - P11-S1-C3
      - P13-S1-C2
      - P14-S1-C3
      - P14-S1-C5
      - P14-S2-C28
      - P16-S4-C4
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: imaging_provenance
      source_ids:
      - P1-S2-C3
      - P5-S1-C7
      - P6-S2-C8
      - P6-S2-C9
      - P6-S2-C10
      - P6-S3-C14
      - P6-S3-C15
      - P7-S1-C9
      - P8-S3-C2
      - P11-S2-C4
      - P12-S2-C9
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: outcome_definition
      source_ids:
      - P1-S1-C11
      - P2-S1-C2
      - P5-S1-C7
      - P5-S3-C7
      - P5-S3-C8
      - P6-S2-C2
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C5
      - P6-S2-C7
      - P6-S3-C12
      - P7-S1-C8
      - P12-S1-C3
      - P12-S1-C10
      - P12-S2-C10
      - P12-S3-C1
      - P13-S1-C10
      - P13-S1-C11
      - P13-S2-C3
      - P16-S4-C5
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: limitations
      source_ids:
      - P4-S2-C11
      - P4-S2-C12
      - P4-S2-C13
      - P4-S3-C2
      - P4-S3-C3
      - P4-S3-C6
      - P4-S3-C7
      - P4-S4-C1
      - P11-S1-C4
      - P12-S1-C2
      - P12-S2-C4
      - P12-S2-C7
      - P13-S1-C5
      - P13-S2-C10
      reason: Runaway selection (>8 passages); entire slot requires source review
    - slot: descriptive_personal_factors
      source_ids:
      - P1-S1-C12
      - P5-S2-C9
      - P5-S2-C10
      - P5-S2-C11
      - P5-S2-C12
      - P5-S3-C2
      - P5-S3-C3
      - P5-S3-C4
      - P8-S1-C16
      - P8-S3-C2
      - P11-S1-C8
      - P13-S1-C2
      - P13-S3-C9
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
      pdf_sha256: a578a68cf0df404ad55655a1393a67ae45fe75c2005f60ee6fc71951e7d648ca
      review_sha256: bd4370e9649b7b4bc7cba4f3b59861b7c19bfac30a8270f3fb2232a53cf85dfc
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
      - P12-S1-C8
      source_result: The study found that the remaining parts of the superior longitudinal
        fasciculus (SLF), after subtracting the arcuate fasciculus (AF) mask, were
        not related to language processing. This was determined via partial correlations
        between DTI indices (FA, MD, RD, AD) and language measures, controlling for
        age, time post-onset, and lesion size.
      result_status: not_detected
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis corresponds to the correlational analysis
            of the left SLF (non-AF) tract segments/metrics with language measures,
            as described in the discussion (P12-S1-C8) and methods (P7-S1-C4, P8-S2-C1).
          source_ids:
          - P12-S1-C8
          - P7-S1-C4
          - P8-S2-C1
        direction:
          answer: fits
          reason: The source explicitly states that the remaining parts of the SLF
            were 'not related to language processing' (P12-S1-C8), which aligns with
            the 'no_effect' direction in the draft.
          source_ids:
          - P12-S1-C8
        construct:
          answer: fits
          reason: The exposure is correctly identified as the left SLF (non-AF) integrity,
            measured via DTI indices extracted from tract masks (template overlap).
            The outcome is language processing, assessed via the ASA battery. The
            method is correlational (partial correlations).
          source_ids:
          - P12-S1-C8
          - P7-S1-C4
          - P5-S3-C6
          - P8-S2-C1
        qualifications:
          answer: fits
          reason: The draft correctly includes the qualification that the analysis
            used partial correlations factoring out age, time post-onset, and lesion
            size (P8-S2-C1, P7-S1-C15). It also correctly notes the limitation that
            lesion location was not used as a covariate (P12-S2-C7).
          source_ids:
          - P8-S2-C1
          - P7-S1-C15
          - P12-S2-C7
        missing_material_caveat:
          answer: fits
          reason: No material caveats are missing. The draft captures the key limitations
            regarding lesion location and the specific nature of the SLF analysis
            (subtracting AF).
          source_ids:
          - P12-S2-C7
          - P7-S1-C4
      optional_pending:
      - Sample size requires source confirmation; it has not been transcribed.
      - 'sample.time_post_onset: source confirmation required; original proposed wording
        remains in the audit.'
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
    - Sample size requires source confirmation; it has not been transcribed.
    - 'sample.time_post_onset: source confirmation required; original proposed wording
      remains in the audit.'
    normalizations:
    - field: sample.n
      original: 37
      action: not_transcribed
      reason: Not supported by selected quotations
    - field: sample.time_post_onset
      original: chronic stage (mean 26.38 months post-onset; range 4-100 months)
      action: not_transcribed
      reason: 'Numbers not grounded in usable selected source readings: 1E+2, 26.38,
        4'
    analysis_identity:
      id: R010
      exposure:
        text: left SLF (non-AF) integrity
      outcome:
        text: language processing
      analysis_label: Tract segment correlational analysis
      relation: association
      evidence_ids:
      - P12-S1-C8
      qualifier_ids:
      - P8-S2-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: a578a68cf0df404ad55655a1393a67ae45fe75c2005f60ee6fc71951e7d648ca
        source_review: _compare/relationships-2026-11-16/review-current/Ivanova2016
        source_status_sha256: 6728000e53f4471e699ca7c19d667031b0ba1d523caea3f988232c36c6ffc3b8
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P5-S2-C11:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: a578a68cf0df404ad55655a1393a67ae45fe75c2005f60ee6fc71951e7d648ca
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 7ee602421930152afa3de69a4774f45f967082932ddb48229ef43ebebf14e2c2
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P5-S2-C11
          page: 5
          text_layer_sha256: 7ee602421930152afa3de69a4774f45f967082932ddb48229ef43ebebf14e2c2
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: held
        original_text: 'All in-

          dividuals in this group had aphasia resulting from single or

          multiple left-hemisphere strokes (bilateral strokes were

          excluded), the latest being not earlier than four months prior

          to scanning (M ¼ 26.38, SD ¼ 21.40 months post-onset; range:

          4e100 months).'
        anchor_text: 'All in-

          dividuals in this group had aphasia resulting from single or

          multiple left-hemisphere strokes (bilateral strokes were

          excluded), the latest being not earlier than four months prior

          to scanning (M ¼ 26.38, SD ¼ 21.40 months post-onset; range:

          4e100 months).'
        excluded_fragments: []
        image_sha256: 0710eeda1d7b255e43792e81a7b86873e9daa82f71cd5b879c61d7558c901ee1
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 12
  quote: 'The remaining parts of

    the SLF were not related to language processing.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
