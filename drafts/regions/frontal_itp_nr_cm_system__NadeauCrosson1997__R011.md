---
id: frontal_itp_nr_cm_system
name: frontal-ITP-NR-CM system cluster
kind: network
findings:
- id: f1
  target: aphasia
  target_kind: impairment
  claim: NadeauCrosson1997 reports, based on the authors’ limited-evidence synthesis of previously reported thalamic cases, that cases of tuberothalamic territory infarction and cases of paramedian territory infarction with aphasia have in common involvement of the frontal-ITP-NR-CM system.
  direction: likely
  relationship: synthesis
  method: narrative_review
  sample:
    n: not_reported
    population: 'Participants in the studies summarized by NadeauCrosson1997; this record is a secondary review report, not a newly recruited cohort. Primary source: the authors’ limited-evidence synthesis of previously reported thalamic cases.'
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
  - few published cases of tuberothalamic infarction have sufficiently precise mapping to determine if NRVA or NR-to-CM projections are invariably involved
  evidence_quality: narrative-review
  strength: weak
  notes: 'Reclassified as a secondary review report, explicitly attributing the result to the authors’ limited-evidence synthesis of previously reported thalamic cases. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication. Source repair (unapproved): Reclassified as a secondary review report, explicitly attributing the result to the authors’ limited-evidence synthesis of previously reported thalamic cases. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.'
  imaging_details:
    reference_space: not_applicable
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: agent:source-repair
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
    - proposed_concept:aphasia
    - agent_source_repair_pending_human_review
  citation: '@NadeauCrosson1997'
  source_passages:
  - section: Original source P24-S1-C5
    page: 24
    quote: 'Thus, we conclude on the basis of this limited evidence that the one thing

      that cases of tuberothalamic territory infarction and cases of paramedian ter-

      ritory infarction with aphasia have in common is involvement of the frontal–

      ITP–NR–CM system.'
    supports: claim
  - section: Original source P21-S1-C8
    page: 21
    quote: 'All four patients had fairly typi-

      cal thalamic aphasia, with anomia in spontaneous language, poor perfor-

      mance on word ﬂuency tests, problems with naming to confrontation, fairly

      good comprehension, and normal repetition.'
    supports: sample
  - section: Original source P22-S1-C4
    page: 22
    quote: 'Note involvement of

      anteroventral aspect VA (Lpo) (the site of the ITP–NR interface) immediately lateral to the

      internal medullary lamina (La.m.o) (H.d 1.5).

      5, H.d 4.0) and some of VA (Lpo), and although it did not extend as far

      inferiorly as in BD, it did involve the site of the ITP–NR interface at antero-

      ventral VA (Fig. 5, H.d 1.5).'
    supports: method
  - section: Original source P23-S1-C7
    page: 23
    quote: 'The one nucleus involved in WT and in all of these other unusual

      cases of paramedian territory infarction with aphasia was CM, except in the

      cases of Lazzarino et al. (1991), in which the internal medullary lamina at

      its junction with CM was involved.'
    supports: method
  - section: Original source P24-S1-C6
    page: 24
    quote: 'Few published cases of tuberothalamic infarction

      have included sufﬁciently precise mapping of the lesions to determine

      whether NRVA or projections from NR to CM are invariably involved.'
    supports: limitation
  design: narrative-review
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-25'
relationship_review:
  paper: NadeauCrosson1997
  proposal_id: R011
  approved: false
  original_core_review:
    paper: NadeauCrosson1997
    proposal_id: R011
    review_status_sha256: c96516efc03a79ca5e7782ac2dfa151e1f940e723cebc823dd2ae2b2c881abd3
    review_binding:
      version: candidate-inventory-v1
      input_hashes:
        pdf: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
      original_review_binding:
        version: relationship-review-v5
        input_hashes:
          pdf: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
          A/passages.json: 9fdd37846530ac758e76cf2145b2c99dba88442e0bccdffb8e80f5c60a5d55c0
          A/raw.json: 31f4f553b4595f321a2dd1fda41adce42663e855ebe4c1b0190085d63e239ba6
          A/source-units.json: 6051eb6556064fc131b573aa7116cefed749f9793183ef965dec31ba1d90c0b8
          A/full-source-units.json: b19b01ef87b4ef664154fa1ef7e7803f4d0fea4921deafa8c7b10b8bafa95ba1
          A/meta.json: 63ea6573dca0c0ddc9f683823b43d5bf0285b2ea13fdd86f67f0a38cb8f062f7
          A/table-images/page-14.png: f2196fe825e438a128154eb510c6bd216db353b88f7927e0d625e282ad4ea497
          A/table-images/TABLE-4-page-14-1.png: acc193cafafc84758a72059fc35417f85dde9eae2896ae82703da891ff4818a6
          A/table-images/page-6.png: 712566c7b268cdb422caa419f4895c1cd4320dad10192217be9c009238dec73c
          A/table-images/page-4.png: 1727ba62a11946618fe4e7aba503bdaa819b2348981a2f22dc8ccb27647bb319
          A/table-images/TABLE-1-page-4-1.png: 09046700e874fb56ef0077eca2ef83c213517019da49184e2cdbd90c55cc67f9
          A/table-images/TABLE-3-page-6-1.png: bb50ad9a640bcd16cf5ed4c1c1beb9918106db6ef5ff11ab7ca76009cad9b6a4
          A/table-images/TABLE-2-page-4-2.png: 09046700e874fb56ef0077eca2ef83c213517019da49184e2cdbd90c55cc67f9
          A/table-images/manifest.json: 08aaef665446dd2e257947d12c83176348670313633ef26d767ed181194f1645
          A/table-images/TABLE-5-page-36-1.png: c693612c63e839a6534f79cef2aba0772b164909fdb6f75538dc6712844dcf8d
          A/table-images/page-36.png: 3c27ec1713268db0f581e78863d7d62fa5fececb13693b05856ea1b8a7c89407
          A/clauses/window-11/raw.json: 7011ef0b459a06e27d35a0a9246ffc65fbc86e4d85e0d9c15ca46d6644d3c037
          A/clauses/window-11/prompt.txt: 64586b516f68134c0dcee8fa0b9c02ebc47e2fb63609d5df6ea8c6bfddf123f9
          A/clauses/window-11/meta.json: 01fa4dd94956d88085f5211d46d3b20fd7c25541a097279fae3c074532d0e3df
          A/clauses/window-10/raw.json: 8cf2f3fc84fc0cccd84b5034cec5699ce0cf019e03418c335a7bef26b849ec63
          A/clauses/window-10/prompt.txt: c06415255e70d0e27b7a005f25bda722dddbcc9db939162aabaca23bbf56e2f5
          A/clauses/window-10/meta.json: eb8f3dfa5b6883085f7d8d53560a2cd80dfb44db3246eba77d0b338b3307dcc8
          A/clauses/window-03/raw.json: c271251a47001b415a216c16432319fa963a209def766c9306bc15a9694407d9
          A/clauses/window-03/prompt.txt: 4c2bc695f0f6f01077da7bc4e0bf31c0617cde89238fc7cc6effe746fccfe773
          A/clauses/window-03/meta.json: 5b5a06f95fe1ec62be7259e4bb945a712f3b8e79efe47048178af2e8ef3a548d
          A/clauses/window-04/raw.json: 0bec363ff09a3f2bf7aebe7d08877e2cd5ba7ad3f55c01fa266fbecd9a2ab958
          A/clauses/window-04/prompt.txt: 1e306c3dd2f3c334233f4665da7fe2b17adc45b578a6f4ddd059e83240b86b6e
          A/clauses/window-04/meta.json: 49d35038b58c74bf05b7c510df50a735592b52fd1f2158e498db915e568f532a
          A/clauses/window-05/raw.json: d5f7a96a69b2e66911035f5dd0e8a9ecca124d2ba2b9b3aeb9160bd56d15128e
          A/clauses/window-05/prompt.txt: 08faa31827174e3d650def125c5f8685177fd090f6e19419dc3d05b49a634c8b
          A/clauses/window-05/meta.json: 4887912c35da7b8ae3003dbf16d0c7f8b8750555c0d3bfd8428e3b819ef95a8f
          A/clauses/window-02/raw.json: 6e7dedad962f42f265817a6409046a1643092ed2eda1bc345b151feea26e7b87
          A/clauses/window-02/prompt.txt: 75ba6560f12080064f0aff15ad057b67f3aa05048cac3a8a6b13e23877b9aa12
          A/clauses/window-02/meta.json: c102da2fe2d08358c0c293378982322c1f09d32652d373add814afb34f315771
          A/clauses/window-15/raw.json: 63c78ac79a767bdf4a118f0b6255d59e14767b94550edf9e06d5b1b11c2d2b18
          A/clauses/window-15/prompt.txt: da49eef7d12ffc4e4a9bf4401b575f0aa859173d1e620a4af21d1447e2109830
          A/clauses/window-15/meta.json: 63ba9d1d5a0b7267fe1952c3494d9aa7bbd3713d01aff278b5ee6887b7a5739b
          A/clauses/window-12/raw.json: b2c7dde69fa1721c79edc01ee251f7c813a25e778738316809d8b47d23756607
          A/clauses/window-12/prompt.txt: 5ddb2407052f2e6e75540fffc7f20b9d5d70c653edd3ba16e909090b28383db0
          A/clauses/window-12/meta.json: 13a10a695770ad512086d092caced2a134a813725ef0efe7a4ce6f638b855c9a
          A/clauses/window-13/raw.json: 6496207a8490941b089d168596816e21d7ec4b94a940f3e4e2ea85d268cc6613
          A/clauses/window-13/prompt.txt: 7cdba2d790250d2456f03e6610cdb980cbe297217da62eea9b15a81cf21f2a0d
          A/clauses/window-13/meta.json: 25d50cebe4645e38d3937eec3d6d64a20c8e8c4dd40f62cc99f3a31e91d1bae4
          A/clauses/window-14/raw.json: 0e135174942f49565fce352c5429dea998c70450661670678f08b8a70d2083ce
          A/clauses/window-14/prompt.txt: a6d3eef42b241131a7d33f64df37d4e89f68288a508ef58233435bfd03f9da0d
          A/clauses/window-14/meta.json: 443a34e360c58de1fac53452f0c90a9f21611c749c018a97c413b814c995b181
          A/clauses/window-09/raw.json: 07f41cdb0a1a767c5fc193e400dee168c9365095fbe3d7a5a2ccc323f697b5a3
          A/clauses/window-09/prompt.txt: a9e960d78b1b8e2db28dfcfc8e5cccf635afd0f10ab5c2ddcaa40c2ec170a044
          A/clauses/window-09/meta.json: 980a290881276b931e68c9bc8dcce8e3da5e21199418483af3d52dec7aaa9b3a
          A/clauses/window-07/raw.json: c913f2b83b1733aa483f237d39fc5f34f57fd45740f9053668bc22442fb12d25
          A/clauses/window-07/prompt.txt: 91d1974b5d3a330c865230b05815251a9da7b109e87752356ca041c166a96835
          A/clauses/window-07/meta.json: 8722ec6d3746f8f4f253516e27708e07033f46f96daa7d0618d8aa1c15ab2229
          A/clauses/window-01/raw.json: 2182e2d8ed2fe306ba13deb5e35158971681f3be17d8f6a5a1a4ee99a008296c
          A/clauses/window-01/prompt.txt: c8620d56fd701b51b6fc4cfd06fa7a7f60c7792a56c527b48eeda0491056c19a
          A/clauses/window-01/meta.json: 452b1d6bc83816484afe025aabb7d9c4eaaddfdea8a66bb83876999582269aff
          A/clauses/window-06/raw.json: 0f35b24f76e4b59c5a2cc977411f0ce8febae2a5fa8916a8f3e9270b37a2a78f
          A/clauses/window-06/prompt.txt: c18639dc9160f6170030e53e9005d850dc7848eee52cdf668c6881f9114beb09
          A/clauses/window-06/meta.json: eb53051dcba8e067be824f0a167d778c70e1db7a6b5d743cd4055d394eaf8583
          A/clauses/window-08/raw.json: 1256847c20b7bd5e0aa53a3acd4a82d57c1fbe94f1af7efadc11e8190cfbb83a
          A/clauses/window-08/prompt.txt: d824ba96fe2972eb0057b4d64d23e30099d29abcedae3208801fea254918d00f
          A/clauses/window-08/meta.json: 84b036ca039a5e8f36ed73db0b7d6f95d8fa2debdfb67141850f5e705524e15a
          A/tables/TABLE-3-page-6-3/raw.json: e9faa855b847d5a5d80d62a61c349167332e8fe5f816bea3d3d404d61a251e81
          A/tables/TABLE-3-page-6-3/prompt.txt: ba1f79ef3b03c83a24062d08b951a4e692ac35db5bf2ff12059f1f18214d14f9
          A/tables/TABLE-3-page-6-3/meta.json: e11228302862ef4856126451fd3a79f3d2ecf8201f51c443d5c33ebaebed9d88
          A/tables/TABLE-1-page-4-1/raw.json: 71f9c62dde8d3e6825fee212d28a4e238a15809f992df3cb03f608ebac239c6a
          A/tables/TABLE-1-page-4-1/prompt.txt: f29df5e4012a5d2a6ff70373891da380a9f0fe9318f3d3cc1076f432e925593b
          A/tables/TABLE-1-page-4-1/meta.json: 16dd1ece8d3234090f7c87b6b0219dc493966110e858e6d9237a3b19451ebfba
          A/tables/TABLE-4-page-14-4/raw.json: 8be19cebd3af58d24e85d619ce70fa2051ffb18ee28e59b03676e5207a67e177
          A/tables/TABLE-4-page-14-4/prompt.txt: 8f77c49ca37c549523ee9e5fb3441c2fb2b6ea7860cd5da2dc07282c58e1488d
          A/tables/TABLE-4-page-14-4/meta.json: d4cb9dd2926b336dce4f3c819c121b81c04103f7ce5931cd724a3f9a18ea993d
          A/tables/TABLE-5-page-36-5/raw.json: 711031a625d5d9d89d173b8f64ff48dea4b54274c569521da085195301dabd16
          A/tables/TABLE-5-page-36-5/prompt.txt: ffab3c15f13c610a44a8ce54721e1db198930a254afcc6d3c016100ff3a7125e
          A/tables/TABLE-5-page-36-5/meta.json: 117d55e5b0d9a411beb4447a518db7d32c9b02bcc07aa112eee6d9a6bd334dcd
          A/tables/TABLE-2-page-4-2/raw.json: b4011dbf51a1eadc3180bb69fbafb502632f030a0c554e42851c9fea579e5463
          A/tables/TABLE-2-page-4-2/prompt.txt: a1657b4d2a3257af8081caf9b9b1f83fbf19916b09d7070285ac4c07f670f1a8
          A/tables/TABLE-2-page-4-2/meta.json: 07bd556481575443a9a81505ed6afe7048d20ffa951a1d060ad7788a6cf068ce
          B/passages.json: 9fdd37846530ac758e76cf2145b2c99dba88442e0bccdffb8e80f5c60a5d55c0
          B/raw.json: d71cd53b510f720a61bd8ddf4481e375adb06212c01a001d4482aa79292ec92b
          B/source-units.json: 6051eb6556064fc131b573aa7116cefed749f9793183ef965dec31ba1d90c0b8
          B/full-source-units.json: b19b01ef87b4ef664154fa1ef7e7803f4d0fea4921deafa8c7b10b8bafa95ba1
          B/meta.json: 6786cac7a996b5d601f654b7a3a4870ec7b32451c559b974209cd3928112b9e4
          B/table-images/page-14.png: f2196fe825e438a128154eb510c6bd216db353b88f7927e0d625e282ad4ea497
          B/table-images/TABLE-4-page-14-1.png: acc193cafafc84758a72059fc35417f85dde9eae2896ae82703da891ff4818a6
          B/table-images/page-6.png: 712566c7b268cdb422caa419f4895c1cd4320dad10192217be9c009238dec73c
          B/table-images/page-4.png: 1727ba62a11946618fe4e7aba503bdaa819b2348981a2f22dc8ccb27647bb319
          B/table-images/TABLE-1-page-4-1.png: 09046700e874fb56ef0077eca2ef83c213517019da49184e2cdbd90c55cc67f9
          B/table-images/TABLE-3-page-6-1.png: bb50ad9a640bcd16cf5ed4c1c1beb9918106db6ef5ff11ab7ca76009cad9b6a4
          B/table-images/TABLE-2-page-4-2.png: 09046700e874fb56ef0077eca2ef83c213517019da49184e2cdbd90c55cc67f9
          B/table-images/manifest.json: 9f7d302ad51f5348f7911871b207cebb9407f6181cca3681e5771c78a0216e80
          B/table-images/TABLE-5-page-36-1.png: c693612c63e839a6534f79cef2aba0772b164909fdb6f75538dc6712844dcf8d
          B/table-images/page-36.png: 3c27ec1713268db0f581e78863d7d62fa5fececb13693b05856ea1b8a7c89407
          B/clauses/window-11/raw.json: b8c73f86c3abe72feda151d56ae219c2252d3f0430edc2fcd33b2f1b214c1d53
          B/clauses/window-11/prompt.txt: 64586b516f68134c0dcee8fa0b9c02ebc47e2fb63609d5df6ea8c6bfddf123f9
          B/clauses/window-11/meta.json: 79a26cc5031c45b07db2c13fe5a0b7944379b0c963160dfa4915c79a368ba608
          B/clauses/window-10/raw.json: 8cd00177eaaa3e152eec8ae9217cbb43a37751531140db3515ab73cc2cdded64
          B/clauses/window-10/prompt.txt: c06415255e70d0e27b7a005f25bda722dddbcc9db939162aabaca23bbf56e2f5
          B/clauses/window-10/meta.json: e0f987831188f9d70d40cdc6c85f56eac810c1c43ee7b36a31bc913080248792
          B/clauses/window-03/raw.json: 7e0f28d9fc0784c03da6148ef2afdc45dcb734dd8427978547e4b54dfb025dba
          B/clauses/window-03/prompt.txt: 4c2bc695f0f6f01077da7bc4e0bf31c0617cde89238fc7cc6effe746fccfe773
          B/clauses/window-03/meta.json: 53b53b924dbbb99957288e51c2c74aa3e010dc2ab2aa52c10d9811fee7301cae
          B/clauses/window-04/raw.json: e06357d981406094067d8e0993157b150362f06ac0677375b2304206327a76fe
          B/clauses/window-04/prompt.txt: 1e306c3dd2f3c334233f4665da7fe2b17adc45b578a6f4ddd059e83240b86b6e
          B/clauses/window-04/meta.json: 0ac83f06972c0781a01fe436d981c88d27b2352d14049ef7924b4171418156b4
          B/clauses/window-05/raw.json: 93388e36d8875ca70416e050adaa52aa808a1847e972fcf81203c03b744c607b
          B/clauses/window-05/prompt.txt: 08faa31827174e3d650def125c5f8685177fd090f6e19419dc3d05b49a634c8b
          B/clauses/window-05/meta.json: bfde7601970569a04ac6c0830f018cab6edc8130a6deb9847feb24312da19d86
          B/clauses/window-02/raw.json: 9e7aa18f3c09195c7a24cc3ae5cc6d9d7badf5b51aee137ceb18b39eb28b9ce5
          B/clauses/window-02/prompt.txt: 75ba6560f12080064f0aff15ad057b67f3aa05048cac3a8a6b13e23877b9aa12
          B/clauses/window-02/meta.json: 3d5de48116dbef67c8dd5bf38e1b0fb3f687e89615135678dd9d2a2b7a15779c
          B/clauses/window-15/raw.json: 771c716673846e90bb6ca4a9a2cfceca2350f243ca097aecd281060a6bf251a7
          B/clauses/window-15/prompt.txt: da49eef7d12ffc4e4a9bf4401b575f0aa859173d1e620a4af21d1447e2109830
          B/clauses/window-15/meta.json: 07aefaec9346932b1e3fbad28b2caf59b1651030a59c02d3b468a9a1178f74be
          B/clauses/window-12/raw.json: bf07d2181df1ea8410a976ec122c4e4bcf4698a997aa454efbdb7aa0ff1b5830
          B/clauses/window-12/prompt.txt: 5ddb2407052f2e6e75540fffc7f20b9d5d70c653edd3ba16e909090b28383db0
          B/clauses/window-12/meta.json: 6e2177b629fa86fcc965b07b7baa87628a2b1d18a3c49998fd7a7bc4788d8024
          B/clauses/window-13/raw.json: 56f2edb01d3aaa88f7d2fd0f8db8d41f0df66b192d5d3dfb06180960059809da
          B/clauses/window-13/prompt.txt: 7cdba2d790250d2456f03e6610cdb980cbe297217da62eea9b15a81cf21f2a0d
          B/clauses/window-13/meta.json: d36472f5933c0916a9af140f01159455a9a24b29efffefd3b68e6b1538770582
          B/clauses/window-14/raw.json: 4c472b218c90783f07899a8b945a74b6f9d8d24ee3f782c80b0adee16204dcf3
          B/clauses/window-14/prompt.txt: a6d3eef42b241131a7d33f64df37d4e89f68288a508ef58233435bfd03f9da0d
          B/clauses/window-14/meta.json: 53eaaa76b85f9c49bb65ba648fa54e5926a4cfc00debbb768da9784a120944c8
          B/clauses/window-09/raw.json: 472293971620fdeee187ca7a32e8426384247eb6d88eeca93331b676e11505d3
          B/clauses/window-09/prompt.txt: a9e960d78b1b8e2db28dfcfc8e5cccf635afd0f10ab5c2ddcaa40c2ec170a044
          B/clauses/window-09/meta.json: f9649c1a52ee0589908abe12748519eff59ecafb8420481b2000472659a219a8
          B/clauses/window-07/raw.json: 714e00bbef8bf6be07e3353dfb68b04c1806cd7d45a4e16f56ae5e5d4a82eb6c
          B/clauses/window-07/prompt.txt: 91d1974b5d3a330c865230b05815251a9da7b109e87752356ca041c166a96835
          B/clauses/window-07/meta.json: df01fd2b39a1a11012e98ee7d39495ccf64a1e070e18da3a4f23216c760503b5
          B/clauses/window-01/raw.json: 5977544b6b11f5ad0a5274c8dedef99db3fdd4c44c3879f2c6b7a22bf87bd565
          B/clauses/window-01/prompt.txt: c8620d56fd701b51b6fc4cfd06fa7a7f60c7792a56c527b48eeda0491056c19a
          B/clauses/window-01/meta.json: 41b46362dc01ba0d659d20c3505cdbd744121acc8e5da8fac3966a5201bf92d6
          B/clauses/window-06/raw.json: 1a4fbcb1b8c798ba349ebb59dcba6385ac29f59afce916aa54fbf66132e30724
          B/clauses/window-06/prompt.txt: c18639dc9160f6170030e53e9005d850dc7848eee52cdf668c6881f9114beb09
          B/clauses/window-06/meta.json: 56a567132445cd33f579222abcb36e017e042ef640dddbcd0f47692b829c7219
          B/clauses/window-08/raw.json: 47bb4c3628f3d7d5d80902f4524e13c98003dff0c8f0b18d745e020e90d2fd98
          B/clauses/window-08/prompt.txt: d824ba96fe2972eb0057b4d64d23e30099d29abcedae3208801fea254918d00f
          B/clauses/window-08/meta.json: 5ef8e0e7ee01480b1242dfa39d165b5e54eb5ce289c96fa4b9a9d7b219c97880
          B/tables/TABLE-3-page-6-3/raw.json: 9f29a1b2688c94c5f6f27e4d29fd826e60a398c533f32d36eee07fadd0fde4ed
          B/tables/TABLE-3-page-6-3/prompt.txt: ba1f79ef3b03c83a24062d08b951a4e692ac35db5bf2ff12059f1f18214d14f9
          B/tables/TABLE-3-page-6-3/meta.json: caf369115580b0333e0bc427251ebc430cc5d3b277f447d6d34d7a44d0ffefcb
          B/tables/TABLE-1-page-4-1/raw.json: 71f9c62dde8d3e6825fee212d28a4e238a15809f992df3cb03f608ebac239c6a
          B/tables/TABLE-1-page-4-1/prompt.txt: f29df5e4012a5d2a6ff70373891da380a9f0fe9318f3d3cc1076f432e925593b
          B/tables/TABLE-1-page-4-1/meta.json: 6496c4d7fcaf4509a4b899decf5933f11ec3ad8cbbc6ddf73bddacfe34a97df3
          B/tables/TABLE-4-page-14-4/raw.json: abafe0e5520a51090b0647c521480a3646cbd4441699edeb9041b8a22653cb47
          B/tables/TABLE-4-page-14-4/prompt.txt: 8f77c49ca37c549523ee9e5fb3441c2fb2b6ea7860cd5da2dc07282c58e1488d
          B/tables/TABLE-4-page-14-4/meta.json: ee81e4172bee288525a8e898070ec07cacbb21431edf07a3eed550c7faa279ed
          B/tables/TABLE-5-page-36-5/raw.json: f2833100c89befd479af8c414edfe3cc83a0666e66f09d1739dff09b5f3af791
          B/tables/TABLE-5-page-36-5/prompt.txt: ffab3c15f13c610a44a8ce54721e1db198930a254afcc6d3c016100ff3a7125e
          B/tables/TABLE-5-page-36-5/meta.json: 47e3b1feaa3681103c3292e413c4c920b23a0b98c223102c611412b906a203fb
          B/tables/TABLE-2-page-4-2/raw.json: b4011dbf51a1eadc3180bb69fbafb502632f030a0c554e42851c9fea579e5463
          B/tables/TABLE-2-page-4-2/prompt.txt: a1657b4d2a3257af8081caf9b9b1f83fbf19916b09d7070285ac4c07f670f1a8
          B/tables/TABLE-2-page-4-2/meta.json: 66d8800dba761264f2081681bbdfe9a101a1628fe4f1b3d8d5daea12b1e96d8c
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
        pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
        source_review: _compare/relationships-2026-11-16/review-current/NadeauCrosson1997
        source_status_sha256: 941e51273b21a58da6ef88fcd29b89f86b4937f7e20accedfc49a0bf589a0a06
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
    proposal:
      id: R011
      exposure:
        text: tuberothalamic territory infarction and paramedian territory infarction
      outcome:
        text: aphasia
      analysis_label: Tuberothalamic/Paramedian Infarcts and Frontal-ITP-NR-CM System
      relation: association
      evidence_ids:
      - P24-S1-C5
      qualifier_ids:
      - P21-S1-C8
      - P22-S1-C4
      - P23-S1-C7
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
        source_review: _compare/relationships-2026-11-16/review-current/NadeauCrosson1997
        source_status_sha256: 941e51273b21a58da6ef88fcd29b89f86b4937f7e20accedfc49a0bf589a0a06
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    audit:
      original_audit:
        coverage_issues:
        - Accounting without a linked unit P2-S2-C7
        - Unaccounted source passage P2-S2-C7
        - Accounting without a linked unit P4-S1-C2
        - Accounting without a linked unit P4-S1-C3
        - Unaccounted source passage P4-S1-C2
        - Unaccounted source passage P4-S1-C3
        - Result passage disposed without unit P4-S1-C4
        - Result passage disposed without unit P4-S1-C5
        - Result passage disposed without unit P4-S1-C6
        - Accounting without a linked unit P5-S1-C2
        - Unaccounted source passage P5-S1-C2
        - 'window 13: invalid/duplicate disposition P14-S2-C1'
        - Result passage disposed without unit P14-S2-C1
        - Accounting without a linked unit P20-S1-C9
        - Accounting without a linked unit P20-S2-C2
        - Accounting without a linked unit P20-S2-C3
        - Unaccounted source passage P20-S2-C2
        - Unaccounted source passage P20-S2-C3
        - Unaccounted source passage P20-S1-C9
        - Result passage disposed without unit P20-S2-C4
        - Result passage disposed without unit P21-S1-C6
        - Result passage disposed without unit P21-S1-C8
        - Accounting without a linked unit P22-S1-C11
        - Accounting without a linked unit P22-S1-C12
        - Unaccounted source passage P22-S1-C11
        - Unaccounted source passage P22-S1-C12
        - Result passage disposed without unit P23-S1-C4
        - Result passage disposed without unit P23-S1-C7
        - Result passage disposed without unit P23-S1-C10
        - Unresolved source passage P24-S1-C6
        - Accounting without a linked unit P25-S2-C5
        - Accounting without a linked unit P25-S2-C6
        - Unaccounted source passage P25-S2-C6
        - Unaccounted source passage P25-S2-C5
        - Result passage disposed without unit P33-S1-C1
        unattached_null_or_qualifier_ids:
        - P23-S1-C7
        suppressed_nonrepresented_units: 24
        default_disposition_count_requires_completeness_check: 322
        unselected_timing_passages: []
        personal_effect_slots_without_result_classification: []
        held_frame_selections:
        - slot: dependent_variable_statement
          source_id: P5-S1-C2
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P14-S2-C2
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P18-S2-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: analysed_sample
          source_ids:
          - P1-S1-C3
          - P1-S1-C6
          - P4-S1-C1
          - P4-S2-C1
          - P6-S1-C1
          - P12-S2-C2
          - P12-S2-C3
          - P12-S2-C5
          - P14-S1-C1
          - P17-S2-C3
          - P21-S1-C7
          - P23-S1-C8
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: recruited_sample
          source_ids:
          - P1-S1-C3
          - P1-S1-C6
          - P4-S1-C1
          - P4-S1-C4
          - P4-S1-C5
          - P4-S1-C7
          - P4-S1-C8
          - P5-S1-C6
          - P5-S1-C7
          - P5-S1-C8
          - P6-S1-C2
          - P12-S2-C2
          - P12-S2-C3
          - P12-S2-C5
          - P14-S1-C1
          - P17-S2-C3
          - P17-S2-C4
          - P21-S1-C7
          - P23-S1-C5
          - P23-S1-C6
          - P23-S1-C7
          - P23-S1-C8
          - P24-S1-C4
          - P25-S1-C1
          - P25-S1-C2
          - P25-S1-C4
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: imaging_provenance
          source_ids:
          - P1-S1-C4
          - P4-S1-C5
          - P5-S1-C6
          - P5-S1-C7
          - P5-S1-C8
          - P5-S2-C1
          - P12-S2-C5
          - P15-S2-C3
          - P18-S2-C4
          - P21-S1-C3
          - P24-S1-C2
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: limitations
          source_ids:
          - P2-S1-C11
          - P2-S1-C12
          - P10-S1-C2
          - P9-S1-C9
          - P12-S2-C4
          - P13-S1-C4
          - P19-S1-C6
          - P19-S1-C7
          - P20-S1-C4
          - P24-S1-C6
          - P24-S1-C7
          - P25-S1-C7
          - P29-S2-C2
          - P29-S2-C5
          - P30-S2-C6
          reason: Runaway selection (>8 passages); entire slot requires source review
        empty_frame_slots_require_confirmation:
        - analysed_sample
        - recruited_sample
        - imaging_provenance
        - validation
        - analysis_restrictions
        - limitations
        - personal_factors
        - adjustment_roles
        - explicitly_not_adjusted
        unclassified_extraction_ids:
        - P22-S1-C12
        table_review_required:
        - TABLE-1-page-4-1
        - TABLE-2-page-4-2
        - TABLE-3-page-6-3
        - TABLE-4-page-14-4
        - TABLE-5-page-36-5
        unlinked_tables:
        - TABLE-2-page-4-2
        - TABLE-5-page-36-5
        source_anomalies: []
        visual_review_required:
          scope: All main-paper figures and table crops
          note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
          caption_candidate_units:
          - P9-S1
          - P10-S1
          - P15-S1
          - P16-S1
          - P21-S1
          - P22-S1
          - P23-S1
          - P24-S1
          - P35-S1
        approval: Not performed. Structural checks and model selections do not establish semantic correctness.
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
        source_review: _compare/relationships-2026-11-16/review-current/NadeauCrosson1997
        source_status_sha256: 941e51273b21a58da6ef88fcd29b89f86b4937f7e20accedfc49a0bf589a0a06
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
      coverage:
      - source_id: P1-S1-C6
        disposition: background_or_descriptive
        result_indexes: []
        reason: Introduces hypothesis regarding the frontal lobe-ITP-NR-CM system.
      - source_id: P2-S2-C7
        disposition: background_or_descriptive
        result_indexes: []
        reason: General statement about lack of evidence for nonthalamic subcortical structures.
      - source_id: P4-S1-C1
        disposition: represented
        result_indexes:
        - 0
        reason: Provides the data table and summary of linguistic features for 33 cases.
      - source_id: P4-S1-C2
        disposition: represented
        result_indexes:
        - 0
        reason: Describes specific linguistic patterns (fluent but impaired comprehension/repetition/naming).
      - source_id: P4-S1-C3
        disposition: represented
        result_indexes:
        - 0
        reason: Describes nonfluent output patterns.
      - source_id: P4-S1-C4
        disposition: represented
        result_indexes:
        - 0
        reason: Reports 17 patients with no language disorder.
      - source_id: P4-S1-C5
        disposition: represented
        result_indexes:
        - 1
        reason: Links the analysis to cases with CT documentation.
      - source_id: P4-S1-C6
        disposition: background_or_descriptive
        result_indexes: []
        reason: General statement about single investigator reports.
      - source_id: P5-S1-C2
        disposition: represented
        result_indexes:
        - 2
        reason: States no correlation between infarct size/pattern and aphasia type/severity.
      - source_id: P6-S1-C2
        disposition: represented
        result_indexes:
        - 3
        reason: Reports that CdH hemorrhages are infrequently aphasic.
      - source_id: P8-S2-C7
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses repetition impairment in putamenal hemorrhage.
      - source_id: P14-S1-C8
        disposition: represented
        result_indexes:
        - 10
        reason: Qualifies the comparison between Table 4 and Table 1.
      - source_id: P14-S2-C1
        disposition: represented
        result_indexes:
        - 10
        reason: States association between temporal stem extension and posterior linguistic features.
      - source_id: P14-S2-C2
        disposition: represented
        result_indexes:
        - 10
        reason: Provides statistical significance for repetition impairment in temporal stem group.
      - source_id: P20-S2-C2
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes radiographic distinction of infarct types.
      - source_id: P20-S2-C3
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes radiographic distinction of infarct types.
      - source_id: P20-S2-C4
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes clinical distinction of paramedian infarcts.
      - source_id: P21-S1-C6
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes lesion map details.
      - source_id: P21-S1-C8
        disposition: represented
        result_indexes:
        - 11
        reason: Describes the typical thalamic aphasia features of the four cases.
      - source_id: P21-S1-C9
        disposition: background_or_descriptive
        result_indexes: []
        reason: Identifies infarct territory for cases BD and CG.
      - source_id: P21-S1-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes lesion anatomy for case BD.
      - source_id: P21-S1-C11
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes lesion anatomy for case CG.
      - source_id: P22-S1-C4
        disposition: represented
        result_indexes:
        - 11
        reason: Describes lesion anatomy for case CG.
      - source_id: P22-S1-C7
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses sparing of ITP-NR interface in paramedian infarcts.
      - source_id: P22-S1-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes patient WT's infarct.
      - source_id: P22-S1-C11
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes lesion anatomy for patient WT.
      - source_id: P23-S1-C4
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses potential roles of DM or LP in aphasia.
      - source_id: P23-S1-C7
        disposition: represented
        result_indexes:
        - 11
        reason: Identifies CM as the common nucleus involved in paramedian infarcts with aphasia.
      - source_id: P23-S1-C8
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes patient JB's infarct.
      - source_id: P23-S1-C9
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes lesion anatomy for patient JB.
      - source_id: P23-S1-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: Describes disruption of the frontal-ITP-NR-CM system in patient JB.
      - source_id: P24-S1-C4
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses cases of paramedian infarction without aphasia.
      - source_id: P25-S1-C7
        disposition: background_or_descriptive
        result_indexes: []
        reason: General hypothesis about the frontal-ITP-NR-CM system.
      - source_id: P29-S2-C2
        disposition: background_or_descriptive
        result_indexes: []
        reason: General statement about limited evidence.
      - source_id: P29-S2-C5
        disposition: background_or_descriptive
        result_indexes: []
        reason: General statement about lack of studies on frontal lobe lesions.
      - source_id: P33-S1-C1
        disposition: background_or_descriptive
        result_indexes: []
        reason: General conclusion summary.
      - source_id: P33-S1-C7
        disposition: background_or_descriptive
        result_indexes: []
        reason: General conclusion summary.
      - source_id: P33-S1-C8
        disposition: background_or_descriptive
        result_indexes: []
        reason: General conclusion summary.
      - source_id: P34-S1-C1
        disposition: background_or_descriptive
        result_indexes: []
        reason: Discusses syntax impairment in Parkinson's disease.
      - source_id: P34-S1-C10
        disposition: background_or_descriptive
        result_indexes: []
        reason: General conclusion summary.
      - source_id: P34-S2-C1
        disposition: background_or_descriptive
        result_indexes: []
        reason: General conclusion summary.
      unresolved_coverage: []
      pending_source_ids:
      - P1-S1-C6
      - P2-S2-C7
      - P4-S1-C6
      - P8-S2-C7
      - P14-S1-C8
      - P20-S2-C2
      - P20-S2-C3
      - P20-S2-C4
      - P21-S1-C6
      - P21-S1-C8
      - P21-S1-C9
      - P21-S1-C10
      - P21-S1-C11
      - P22-S1-C4
      - P22-S1-C7
      - P22-S1-C10
      - P22-S1-C11
      - P23-S1-C4
      - P23-S1-C7
      - P23-S1-C8
      - P23-S1-C9
      - P23-S1-C10
      - P24-S1-C4
      - P25-S1-C7
      - P29-S2-C2
      - P29-S2-C5
      - P33-S1-C1
      - P33-S1-C7
      - P33-S1-C8
      - P34-S1-C1
      - P34-S1-C10
      - P34-S2-C1
      pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
      tables_requiring_review:
      - TABLE-1-page-4-1
      - TABLE-2-page-4-2
      - TABLE-3-page-6-3
      - TABLE-4-page-14-4
      - TABLE-5-page-36-5
      paper_complete: false
      approved: false
      policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
    study_frame:
      slots:
        analysed_sample: []
        recruited_sample: []
        eligibility:
        - P4-S1-C5
        - P17-S2-C4
        imaging_provenance: []
        imaging_timing:
        - P12-S2-C5
        outcome_timing:
        - P12-S2-C5
        outcome_definition:
        - P3-S2-C5
        - P3-S2-C6
        - P3-S2-C7
        - P3-S2-C8
        - P4-S2-C1
        - P6-S1-C1
        - P12-S1-C4
        - P14-S2-C2
        validation: []
        analysis_restrictions: []
        dependent_variable_statement:
        - P3-S2-C5
        - P12-S1-C4
        - P18-S2-C4
        - P18-S2-C5
        limitations: []
        personal_factors: []
        tested_personal_effects:
        - P5-S1-C2
        adjustment_roles: []
        explicitly_not_adjusted: []
        descriptive_personal_factors:
        - P4-S1-C1
        - P12-S2-C2
        - P12-S2-C3
        - P14-S1-C1
        - P17-S2-C4
        - P21-S1-C8
        - P24-S1-C4
      outcome_type: both_reported
      imaging_vs_outcome: mixed
      validation_type: none_described
      window_merge: Union of selected IDs; differing window enums retained conservatively as both/mixed. Not verified study-level facts.
      held_selections:
      - slot: dependent_variable_statement
        source_id: P5-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P14-S2-C2
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P18-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: analysed_sample
        source_ids:
        - P1-S1-C3
        - P1-S1-C6
        - P4-S1-C1
        - P4-S2-C1
        - P6-S1-C1
        - P12-S2-C2
        - P12-S2-C3
        - P12-S2-C5
        - P14-S1-C1
        - P17-S2-C3
        - P21-S1-C7
        - P23-S1-C8
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: recruited_sample
        source_ids:
        - P1-S1-C3
        - P1-S1-C6
        - P4-S1-C1
        - P4-S1-C4
        - P4-S1-C5
        - P4-S1-C7
        - P4-S1-C8
        - P5-S1-C6
        - P5-S1-C7
        - P5-S1-C8
        - P6-S1-C2
        - P12-S2-C2
        - P12-S2-C3
        - P12-S2-C5
        - P14-S1-C1
        - P17-S2-C3
        - P17-S2-C4
        - P21-S1-C7
        - P23-S1-C5
        - P23-S1-C6
        - P23-S1-C7
        - P23-S1-C8
        - P24-S1-C4
        - P25-S1-C1
        - P25-S1-C2
        - P25-S1-C4
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: imaging_provenance
        source_ids:
        - P1-S1-C4
        - P4-S1-C5
        - P5-S1-C6
        - P5-S1-C7
        - P5-S1-C8
        - P5-S2-C1
        - P12-S2-C5
        - P15-S2-C3
        - P18-S2-C4
        - P21-S1-C3
        - P24-S1-C2
        reason: Runaway selection (>8 passages); entire slot requires source review
      - slot: limitations
        source_ids:
        - P2-S1-C11
        - P2-S1-C12
        - P10-S1-C2
        - P9-S1-C9
        - P12-S2-C4
        - P13-S1-C4
        - P19-S1-C6
        - P19-S1-C7
        - P20-S1-C4
        - P24-S1-C6
        - P24-S1-C7
        - P25-S1-C7
        - P29-S2-C2
        - P29-S2-C5
        - P30-S2-C6
        reason: Runaway selection (>8 passages); entire slot requires source review
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
        pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
        review_sha256: c96516efc03a79ca5e7782ac2dfa151e1f940e723cebc823dd2ae2b2c881abd3
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
        - P24-S1-C5
        source_result: The authors conclude that the common anatomical feature in cases of tuberothalamic and paramedian territory infarction associated with aphasia is involvement of the frontal-ITP-NR-CM system, based on a limited series of patients with lesion mapping.
        result_status: qualitative_synthesis
        patient_measurement: template_lesion_overlap
        checks:
          analysis_identity:
            answer: fits
            reason: The source (P24-S1-C5) explicitly states the conclusion that tuberothalamic and paramedian infarcts with aphasia share involvement of the frontal-ITP-NR-CM system. The proposed core correctly identifies this as the analysis result, distinguishing it from the specific vascular territories by focusing on the common anatomical substrate.
            source_ids:
            - P24-S1-C5
            - P20-S1-C7
          direction:
            answer: fits
            reason: The source describes a positive association (involvement of the system is the common factor in aphasia cases). The proposed direction 'likely' is appropriate for a hypothesis-generating conclusion based on limited evidence, as stated in P24-S1-C5 ('conclude on the basis of this limited evidence').
            source_ids:
            - P24-S1-C5
          construct:
            answer: fits
            reason: The exposure is correctly identified as the infarct territories (tuberothalamic/paramedian) which are analyzed for their anatomical overlap. The outcome is aphasia. The measurement is the overlap of patient lesions with the defined frontal-ITP-NR-CM system, which is a template-based lesion mapping approach (using Hassler nomenclature and AC-PC coordinates as per P21-S1-C3/C5), not patient-specific diffusion tractography.
            source_ids:
            - P24-S1-C5
            - P21-S1-C3
            - P21-S1-C5
          qualifications:
            answer: fits
            reason: The proposed core includes the qualification 'based on limited evidence from a small number of cases', which aligns with P24-S1-C5 ('on the basis of this limited evidence') and P24-S1-C6 ('Few published cases... have included sufficiently precise mapping'). The limitation regarding NRVA/NR-to-CM projections is also correctly captured.
            source_ids:
            - P24-S1-C5
            - P24-S1-C6
          missing_material_caveat:
            answer: fits
            reason: The core captures the main caveat about the limited evidence and mapping precision. No other material caveats that would change the interpretation of this specific conclusion are omitted from the provided source window.
            source_ids:
            - P24-S1-C5
            - P24-S1-C6
        optional_pending: []
        verdict: draft
        reason: All five core checks fit the source.
        material_issues: []
      pending_details:
      - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
      - Recovery phase is not classified; use the reported timing words.
      - Evidence-strength rating is a conservative draft placeholder pending human review.
      normalizations: []
      analysis_identity:
        id: R011
        exposure:
          text: tuberothalamic territory infarction and paramedian territory infarction
        outcome:
          text: aphasia
        analysis_label: Tuberothalamic/Paramedian Infarcts and Frontal-ITP-NR-CM System
        relation: association
        evidence_ids:
        - P24-S1-C5
        qualifier_ids:
        - P21-S1-C8
        - P22-S1-C4
        - P23-S1-C7
        context_ids: []
        table_ids: []
        approved: false
        status: requires_source_review
        flags:
        - new_model_candidate_not_verified
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
          source_review: _compare/relationships-2026-11-16/review-current/NadeauCrosson1997
          source_status_sha256: 941e51273b21a58da6ef88fcd29b89f86b4937f7e20accedfc49a0bf589a0a06
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      paper_complete: false
      visual_prose_readings: {}
      remaining:
      - Human PDF review and approval
      - Pending metadata enrichment
      - Main Results, figures and tables completeness check
  original_publication_entry:
    id: frontal_itp_nr_cm_system
    name: frontal-ITP-NR-CM system cluster
    kind: network
    findings:
    - id: f1
      target: aphasia
      target_kind: impairment
      claim: Cases of tuberothalamic territory infarction and cases of paramedian territory infarction with aphasia have in common involvement of the frontal-ITP-NR-CM system.
      direction: likely
      relationship: correlational
      method: LSM
      sample:
        n: not_reported
        population: patients with tuberothalamic or paramedian territory thalamic infarcts
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
      - few published cases of tuberothalamic infarction have sufficiently precise mapping to determine if NRVA or NR-to-CM projections are invariably involved
      evidence_quality: cohort
      strength: weak
      notes: 'Exposure measurement: Patient lesion overlap with the system comprising the frontal lobes, inferior thalamic peduncle (ITP), nucleus reticularis (NR), and centromedian nucleus (CM). based on limited evidence from a small number of cases. Additional metadata has not been transcribed; review the pending-field flags before approval.'
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
        - proposed_concept:aphasia
      citation: '@NadeauCrosson1997'
      source_passages:
      - section: Original source P24-S1-C5
        page: 24
        quote: 'Thus, we conclude on the basis of this limited evidence that the one thing

          that cases of tuberothalamic territory infarction and cases of paramedian ter-

          ritory infarction with aphasia have in common is involvement of the frontal–

          ITP–NR–CM system.'
        supports: claim
      - section: Original source P21-S1-C8
        page: 21
        quote: 'All four patients had fairly typi-

          cal thalamic aphasia, with anomia in spontaneous language, poor perfor-

          mance on word ﬂuency tests, problems with naming to confrontation, fairly

          good comprehension, and normal repetition.'
        supports: sample
      - section: Original source P22-S1-C4
        page: 22
        quote: 'Note involvement of

          anteroventral aspect VA (Lpo) (the site of the ITP–NR interface) immediately lateral to the

          internal medullary lamina (La.m.o) (H.d 1.5).

          5, H.d 4.0) and some of VA (Lpo), and although it did not extend as far

          inferiorly as in BD, it did involve the site of the ITP–NR interface at antero-

          ventral VA (Fig. 5, H.d 1.5).'
        supports: method
      - section: Original source P23-S1-C7
        page: 23
        quote: 'The one nucleus involved in WT and in all of these other unusual

          cases of paramedian territory infarction with aphasia was CM, except in the

          cases of Lazzarino et al. (1991), in which the internal medullary lamina at

          its junction with CM was involved.'
        supports: method
      - section: Original source P24-S1-C6
        page: 24
        quote: 'Few published cases of tuberothalamic infarction

          have included sufﬁciently precise mapping of the lesions to determine

          whether NRVA or projections from NR to CM are invariably involved.'
        supports: limitation
    schema_version: '2.8'
    status: draft
    created_by: agent:relationship-converter
    created_on: '2026-11-25'
    relationship_review:
      paper: NadeauCrosson1997
      proposal_id: R011
      review_status_sha256: c96516efc03a79ca5e7782ac2dfa151e1f940e723cebc823dd2ae2b2c881abd3
      review_binding:
        version: candidate-inventory-v1
        input_hashes:
          pdf: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
        original_review_binding:
          version: relationship-review-v5
          input_hashes:
            pdf: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
            A/passages.json: 9fdd37846530ac758e76cf2145b2c99dba88442e0bccdffb8e80f5c60a5d55c0
            A/raw.json: 31f4f553b4595f321a2dd1fda41adce42663e855ebe4c1b0190085d63e239ba6
            A/source-units.json: 6051eb6556064fc131b573aa7116cefed749f9793183ef965dec31ba1d90c0b8
            A/full-source-units.json: b19b01ef87b4ef664154fa1ef7e7803f4d0fea4921deafa8c7b10b8bafa95ba1
            A/meta.json: 63ea6573dca0c0ddc9f683823b43d5bf0285b2ea13fdd86f67f0a38cb8f062f7
            A/table-images/page-14.png: f2196fe825e438a128154eb510c6bd216db353b88f7927e0d625e282ad4ea497
            A/table-images/TABLE-4-page-14-1.png: acc193cafafc84758a72059fc35417f85dde9eae2896ae82703da891ff4818a6
            A/table-images/page-6.png: 712566c7b268cdb422caa419f4895c1cd4320dad10192217be9c009238dec73c
            A/table-images/page-4.png: 1727ba62a11946618fe4e7aba503bdaa819b2348981a2f22dc8ccb27647bb319
            A/table-images/TABLE-1-page-4-1.png: 09046700e874fb56ef0077eca2ef83c213517019da49184e2cdbd90c55cc67f9
            A/table-images/TABLE-3-page-6-1.png: bb50ad9a640bcd16cf5ed4c1c1beb9918106db6ef5ff11ab7ca76009cad9b6a4
            A/table-images/TABLE-2-page-4-2.png: 09046700e874fb56ef0077eca2ef83c213517019da49184e2cdbd90c55cc67f9
            A/table-images/manifest.json: 08aaef665446dd2e257947d12c83176348670313633ef26d767ed181194f1645
            A/table-images/TABLE-5-page-36-1.png: c693612c63e839a6534f79cef2aba0772b164909fdb6f75538dc6712844dcf8d
            A/table-images/page-36.png: 3c27ec1713268db0f581e78863d7d62fa5fececb13693b05856ea1b8a7c89407
            A/clauses/window-11/raw.json: 7011ef0b459a06e27d35a0a9246ffc65fbc86e4d85e0d9c15ca46d6644d3c037
            A/clauses/window-11/prompt.txt: 64586b516f68134c0dcee8fa0b9c02ebc47e2fb63609d5df6ea8c6bfddf123f9
            A/clauses/window-11/meta.json: 01fa4dd94956d88085f5211d46d3b20fd7c25541a097279fae3c074532d0e3df
            A/clauses/window-10/raw.json: 8cf2f3fc84fc0cccd84b5034cec5699ce0cf019e03418c335a7bef26b849ec63
            A/clauses/window-10/prompt.txt: c06415255e70d0e27b7a005f25bda722dddbcc9db939162aabaca23bbf56e2f5
            A/clauses/window-10/meta.json: eb8f3dfa5b6883085f7d8d53560a2cd80dfb44db3246eba77d0b338b3307dcc8
            A/clauses/window-03/raw.json: c271251a47001b415a216c16432319fa963a209def766c9306bc15a9694407d9
            A/clauses/window-03/prompt.txt: 4c2bc695f0f6f01077da7bc4e0bf31c0617cde89238fc7cc6effe746fccfe773
            A/clauses/window-03/meta.json: 5b5a06f95fe1ec62be7259e4bb945a712f3b8e79efe47048178af2e8ef3a548d
            A/clauses/window-04/raw.json: 0bec363ff09a3f2bf7aebe7d08877e2cd5ba7ad3f55c01fa266fbecd9a2ab958
            A/clauses/window-04/prompt.txt: 1e306c3dd2f3c334233f4665da7fe2b17adc45b578a6f4ddd059e83240b86b6e
            A/clauses/window-04/meta.json: 49d35038b58c74bf05b7c510df50a735592b52fd1f2158e498db915e568f532a
            A/clauses/window-05/raw.json: d5f7a96a69b2e66911035f5dd0e8a9ecca124d2ba2b9b3aeb9160bd56d15128e
            A/clauses/window-05/prompt.txt: 08faa31827174e3d650def125c5f8685177fd090f6e19419dc3d05b49a634c8b
            A/clauses/window-05/meta.json: 4887912c35da7b8ae3003dbf16d0c7f8b8750555c0d3bfd8428e3b819ef95a8f
            A/clauses/window-02/raw.json: 6e7dedad962f42f265817a6409046a1643092ed2eda1bc345b151feea26e7b87
            A/clauses/window-02/prompt.txt: 75ba6560f12080064f0aff15ad057b67f3aa05048cac3a8a6b13e23877b9aa12
            A/clauses/window-02/meta.json: c102da2fe2d08358c0c293378982322c1f09d32652d373add814afb34f315771
            A/clauses/window-15/raw.json: 63c78ac79a767bdf4a118f0b6255d59e14767b94550edf9e06d5b1b11c2d2b18
            A/clauses/window-15/prompt.txt: da49eef7d12ffc4e4a9bf4401b575f0aa859173d1e620a4af21d1447e2109830
            A/clauses/window-15/meta.json: 63ba9d1d5a0b7267fe1952c3494d9aa7bbd3713d01aff278b5ee6887b7a5739b
            A/clauses/window-12/raw.json: b2c7dde69fa1721c79edc01ee251f7c813a25e778738316809d8b47d23756607
            A/clauses/window-12/prompt.txt: 5ddb2407052f2e6e75540fffc7f20b9d5d70c653edd3ba16e909090b28383db0
            A/clauses/window-12/meta.json: 13a10a695770ad512086d092caced2a134a813725ef0efe7a4ce6f638b855c9a
            A/clauses/window-13/raw.json: 6496207a8490941b089d168596816e21d7ec4b94a940f3e4e2ea85d268cc6613
            A/clauses/window-13/prompt.txt: 7cdba2d790250d2456f03e6610cdb980cbe297217da62eea9b15a81cf21f2a0d
            A/clauses/window-13/meta.json: 25d50cebe4645e38d3937eec3d6d64a20c8e8c4dd40f62cc99f3a31e91d1bae4
            A/clauses/window-14/raw.json: 0e135174942f49565fce352c5429dea998c70450661670678f08b8a70d2083ce
            A/clauses/window-14/prompt.txt: a6d3eef42b241131a7d33f64df37d4e89f68288a508ef58233435bfd03f9da0d
            A/clauses/window-14/meta.json: 443a34e360c58de1fac53452f0c90a9f21611c749c018a97c413b814c995b181
            A/clauses/window-09/raw.json: 07f41cdb0a1a767c5fc193e400dee168c9365095fbe3d7a5a2ccc323f697b5a3
            A/clauses/window-09/prompt.txt: a9e960d78b1b8e2db28dfcfc8e5cccf635afd0f10ab5c2ddcaa40c2ec170a044
            A/clauses/window-09/meta.json: 980a290881276b931e68c9bc8dcce8e3da5e21199418483af3d52dec7aaa9b3a
            A/clauses/window-07/raw.json: c913f2b83b1733aa483f237d39fc5f34f57fd45740f9053668bc22442fb12d25
            A/clauses/window-07/prompt.txt: 91d1974b5d3a330c865230b05815251a9da7b109e87752356ca041c166a96835
            A/clauses/window-07/meta.json: 8722ec6d3746f8f4f253516e27708e07033f46f96daa7d0618d8aa1c15ab2229
            A/clauses/window-01/raw.json: 2182e2d8ed2fe306ba13deb5e35158971681f3be17d8f6a5a1a4ee99a008296c
            A/clauses/window-01/prompt.txt: c8620d56fd701b51b6fc4cfd06fa7a7f60c7792a56c527b48eeda0491056c19a
            A/clauses/window-01/meta.json: 452b1d6bc83816484afe025aabb7d9c4eaaddfdea8a66bb83876999582269aff
            A/clauses/window-06/raw.json: 0f35b24f76e4b59c5a2cc977411f0ce8febae2a5fa8916a8f3e9270b37a2a78f
            A/clauses/window-06/prompt.txt: c18639dc9160f6170030e53e9005d850dc7848eee52cdf668c6881f9114beb09
            A/clauses/window-06/meta.json: eb53051dcba8e067be824f0a167d778c70e1db7a6b5d743cd4055d394eaf8583
            A/clauses/window-08/raw.json: 1256847c20b7bd5e0aa53a3acd4a82d57c1fbe94f1af7efadc11e8190cfbb83a
            A/clauses/window-08/prompt.txt: d824ba96fe2972eb0057b4d64d23e30099d29abcedae3208801fea254918d00f
            A/clauses/window-08/meta.json: 84b036ca039a5e8f36ed73db0b7d6f95d8fa2debdfb67141850f5e705524e15a
            A/tables/TABLE-3-page-6-3/raw.json: e9faa855b847d5a5d80d62a61c349167332e8fe5f816bea3d3d404d61a251e81
            A/tables/TABLE-3-page-6-3/prompt.txt: ba1f79ef3b03c83a24062d08b951a4e692ac35db5bf2ff12059f1f18214d14f9
            A/tables/TABLE-3-page-6-3/meta.json: e11228302862ef4856126451fd3a79f3d2ecf8201f51c443d5c33ebaebed9d88
            A/tables/TABLE-1-page-4-1/raw.json: 71f9c62dde8d3e6825fee212d28a4e238a15809f992df3cb03f608ebac239c6a
            A/tables/TABLE-1-page-4-1/prompt.txt: f29df5e4012a5d2a6ff70373891da380a9f0fe9318f3d3cc1076f432e925593b
            A/tables/TABLE-1-page-4-1/meta.json: 16dd1ece8d3234090f7c87b6b0219dc493966110e858e6d9237a3b19451ebfba
            A/tables/TABLE-4-page-14-4/raw.json: 8be19cebd3af58d24e85d619ce70fa2051ffb18ee28e59b03676e5207a67e177
            A/tables/TABLE-4-page-14-4/prompt.txt: 8f77c49ca37c549523ee9e5fb3441c2fb2b6ea7860cd5da2dc07282c58e1488d
            A/tables/TABLE-4-page-14-4/meta.json: d4cb9dd2926b336dce4f3c819c121b81c04103f7ce5931cd724a3f9a18ea993d
            A/tables/TABLE-5-page-36-5/raw.json: 711031a625d5d9d89d173b8f64ff48dea4b54274c569521da085195301dabd16
            A/tables/TABLE-5-page-36-5/prompt.txt: ffab3c15f13c610a44a8ce54721e1db198930a254afcc6d3c016100ff3a7125e
            A/tables/TABLE-5-page-36-5/meta.json: 117d55e5b0d9a411beb4447a518db7d32c9b02bcc07aa112eee6d9a6bd334dcd
            A/tables/TABLE-2-page-4-2/raw.json: b4011dbf51a1eadc3180bb69fbafb502632f030a0c554e42851c9fea579e5463
            A/tables/TABLE-2-page-4-2/prompt.txt: a1657b4d2a3257af8081caf9b9b1f83fbf19916b09d7070285ac4c07f670f1a8
            A/tables/TABLE-2-page-4-2/meta.json: 07bd556481575443a9a81505ed6afe7048d20ffa951a1d060ad7788a6cf068ce
            B/passages.json: 9fdd37846530ac758e76cf2145b2c99dba88442e0bccdffb8e80f5c60a5d55c0
            B/raw.json: d71cd53b510f720a61bd8ddf4481e375adb06212c01a001d4482aa79292ec92b
            B/source-units.json: 6051eb6556064fc131b573aa7116cefed749f9793183ef965dec31ba1d90c0b8
            B/full-source-units.json: b19b01ef87b4ef664154fa1ef7e7803f4d0fea4921deafa8c7b10b8bafa95ba1
            B/meta.json: 6786cac7a996b5d601f654b7a3a4870ec7b32451c559b974209cd3928112b9e4
            B/table-images/page-14.png: f2196fe825e438a128154eb510c6bd216db353b88f7927e0d625e282ad4ea497
            B/table-images/TABLE-4-page-14-1.png: acc193cafafc84758a72059fc35417f85dde9eae2896ae82703da891ff4818a6
            B/table-images/page-6.png: 712566c7b268cdb422caa419f4895c1cd4320dad10192217be9c009238dec73c
            B/table-images/page-4.png: 1727ba62a11946618fe4e7aba503bdaa819b2348981a2f22dc8ccb27647bb319
            B/table-images/TABLE-1-page-4-1.png: 09046700e874fb56ef0077eca2ef83c213517019da49184e2cdbd90c55cc67f9
            B/table-images/TABLE-3-page-6-1.png: bb50ad9a640bcd16cf5ed4c1c1beb9918106db6ef5ff11ab7ca76009cad9b6a4
            B/table-images/TABLE-2-page-4-2.png: 09046700e874fb56ef0077eca2ef83c213517019da49184e2cdbd90c55cc67f9
            B/table-images/manifest.json: 9f7d302ad51f5348f7911871b207cebb9407f6181cca3681e5771c78a0216e80
            B/table-images/TABLE-5-page-36-1.png: c693612c63e839a6534f79cef2aba0772b164909fdb6f75538dc6712844dcf8d
            B/table-images/page-36.png: 3c27ec1713268db0f581e78863d7d62fa5fececb13693b05856ea1b8a7c89407
            B/clauses/window-11/raw.json: b8c73f86c3abe72feda151d56ae219c2252d3f0430edc2fcd33b2f1b214c1d53
            B/clauses/window-11/prompt.txt: 64586b516f68134c0dcee8fa0b9c02ebc47e2fb63609d5df6ea8c6bfddf123f9
            B/clauses/window-11/meta.json: 79a26cc5031c45b07db2c13fe5a0b7944379b0c963160dfa4915c79a368ba608
            B/clauses/window-10/raw.json: 8cd00177eaaa3e152eec8ae9217cbb43a37751531140db3515ab73cc2cdded64
            B/clauses/window-10/prompt.txt: c06415255e70d0e27b7a005f25bda722dddbcc9db939162aabaca23bbf56e2f5
            B/clauses/window-10/meta.json: e0f987831188f9d70d40cdc6c85f56eac810c1c43ee7b36a31bc913080248792
            B/clauses/window-03/raw.json: 7e0f28d9fc0784c03da6148ef2afdc45dcb734dd8427978547e4b54dfb025dba
            B/clauses/window-03/prompt.txt: 4c2bc695f0f6f01077da7bc4e0bf31c0617cde89238fc7cc6effe746fccfe773
            B/clauses/window-03/meta.json: 53b53b924dbbb99957288e51c2c74aa3e010dc2ab2aa52c10d9811fee7301cae
            B/clauses/window-04/raw.json: e06357d981406094067d8e0993157b150362f06ac0677375b2304206327a76fe
            B/clauses/window-04/prompt.txt: 1e306c3dd2f3c334233f4665da7fe2b17adc45b578a6f4ddd059e83240b86b6e
            B/clauses/window-04/meta.json: 0ac83f06972c0781a01fe436d981c88d27b2352d14049ef7924b4171418156b4
            B/clauses/window-05/raw.json: 93388e36d8875ca70416e050adaa52aa808a1847e972fcf81203c03b744c607b
            B/clauses/window-05/prompt.txt: 08faa31827174e3d650def125c5f8685177fd090f6e19419dc3d05b49a634c8b
            B/clauses/window-05/meta.json: bfde7601970569a04ac6c0830f018cab6edc8130a6deb9847feb24312da19d86
            B/clauses/window-02/raw.json: 9e7aa18f3c09195c7a24cc3ae5cc6d9d7badf5b51aee137ceb18b39eb28b9ce5
            B/clauses/window-02/prompt.txt: 75ba6560f12080064f0aff15ad057b67f3aa05048cac3a8a6b13e23877b9aa12
            B/clauses/window-02/meta.json: 3d5de48116dbef67c8dd5bf38e1b0fb3f687e89615135678dd9d2a2b7a15779c
            B/clauses/window-15/raw.json: 771c716673846e90bb6ca4a9a2cfceca2350f243ca097aecd281060a6bf251a7
            B/clauses/window-15/prompt.txt: da49eef7d12ffc4e4a9bf4401b575f0aa859173d1e620a4af21d1447e2109830
            B/clauses/window-15/meta.json: 07aefaec9346932b1e3fbad28b2caf59b1651030a59c02d3b468a9a1178f74be
            B/clauses/window-12/raw.json: bf07d2181df1ea8410a976ec122c4e4bcf4698a997aa454efbdb7aa0ff1b5830
            B/clauses/window-12/prompt.txt: 5ddb2407052f2e6e75540fffc7f20b9d5d70c653edd3ba16e909090b28383db0
            B/clauses/window-12/meta.json: 6e2177b629fa86fcc965b07b7baa87628a2b1d18a3c49998fd7a7bc4788d8024
            B/clauses/window-13/raw.json: 56f2edb01d3aaa88f7d2fd0f8db8d41f0df66b192d5d3dfb06180960059809da
            B/clauses/window-13/prompt.txt: 7cdba2d790250d2456f03e6610cdb980cbe297217da62eea9b15a81cf21f2a0d
            B/clauses/window-13/meta.json: d36472f5933c0916a9af140f01159455a9a24b29efffefd3b68e6b1538770582
            B/clauses/window-14/raw.json: 4c472b218c90783f07899a8b945a74b6f9d8d24ee3f782c80b0adee16204dcf3
            B/clauses/window-14/prompt.txt: a6d3eef42b241131a7d33f64df37d4e89f68288a508ef58233435bfd03f9da0d
            B/clauses/window-14/meta.json: 53eaaa76b85f9c49bb65ba648fa54e5926a4cfc00debbb768da9784a120944c8
            B/clauses/window-09/raw.json: 472293971620fdeee187ca7a32e8426384247eb6d88eeca93331b676e11505d3
            B/clauses/window-09/prompt.txt: a9e960d78b1b8e2db28dfcfc8e5cccf635afd0f10ab5c2ddcaa40c2ec170a044
            B/clauses/window-09/meta.json: f9649c1a52ee0589908abe12748519eff59ecafb8420481b2000472659a219a8
            B/clauses/window-07/raw.json: 714e00bbef8bf6be07e3353dfb68b04c1806cd7d45a4e16f56ae5e5d4a82eb6c
            B/clauses/window-07/prompt.txt: 91d1974b5d3a330c865230b05815251a9da7b109e87752356ca041c166a96835
            B/clauses/window-07/meta.json: df01fd2b39a1a11012e98ee7d39495ccf64a1e070e18da3a4f23216c760503b5
            B/clauses/window-01/raw.json: 5977544b6b11f5ad0a5274c8dedef99db3fdd4c44c3879f2c6b7a22bf87bd565
            B/clauses/window-01/prompt.txt: c8620d56fd701b51b6fc4cfd06fa7a7f60c7792a56c527b48eeda0491056c19a
            B/clauses/window-01/meta.json: 41b46362dc01ba0d659d20c3505cdbd744121acc8e5da8fac3966a5201bf92d6
            B/clauses/window-06/raw.json: 1a4fbcb1b8c798ba349ebb59dcba6385ac29f59afce916aa54fbf66132e30724
            B/clauses/window-06/prompt.txt: c18639dc9160f6170030e53e9005d850dc7848eee52cdf668c6881f9114beb09
            B/clauses/window-06/meta.json: 56a567132445cd33f579222abcb36e017e042ef640dddbcd0f47692b829c7219
            B/clauses/window-08/raw.json: 47bb4c3628f3d7d5d80902f4524e13c98003dff0c8f0b18d745e020e90d2fd98
            B/clauses/window-08/prompt.txt: d824ba96fe2972eb0057b4d64d23e30099d29abcedae3208801fea254918d00f
            B/clauses/window-08/meta.json: 5ef8e0e7ee01480b1242dfa39d165b5e54eb5ce289c96fa4b9a9d7b219c97880
            B/tables/TABLE-3-page-6-3/raw.json: 9f29a1b2688c94c5f6f27e4d29fd826e60a398c533f32d36eee07fadd0fde4ed
            B/tables/TABLE-3-page-6-3/prompt.txt: ba1f79ef3b03c83a24062d08b951a4e692ac35db5bf2ff12059f1f18214d14f9
            B/tables/TABLE-3-page-6-3/meta.json: caf369115580b0333e0bc427251ebc430cc5d3b277f447d6d34d7a44d0ffefcb
            B/tables/TABLE-1-page-4-1/raw.json: 71f9c62dde8d3e6825fee212d28a4e238a15809f992df3cb03f608ebac239c6a
            B/tables/TABLE-1-page-4-1/prompt.txt: f29df5e4012a5d2a6ff70373891da380a9f0fe9318f3d3cc1076f432e925593b
            B/tables/TABLE-1-page-4-1/meta.json: 6496c4d7fcaf4509a4b899decf5933f11ec3ad8cbbc6ddf73bddacfe34a97df3
            B/tables/TABLE-4-page-14-4/raw.json: abafe0e5520a51090b0647c521480a3646cbd4441699edeb9041b8a22653cb47
            B/tables/TABLE-4-page-14-4/prompt.txt: 8f77c49ca37c549523ee9e5fb3441c2fb2b6ea7860cd5da2dc07282c58e1488d
            B/tables/TABLE-4-page-14-4/meta.json: ee81e4172bee288525a8e898070ec07cacbb21431edf07a3eed550c7faa279ed
            B/tables/TABLE-5-page-36-5/raw.json: f2833100c89befd479af8c414edfe3cc83a0666e66f09d1739dff09b5f3af791
            B/tables/TABLE-5-page-36-5/prompt.txt: ffab3c15f13c610a44a8ce54721e1db198930a254afcc6d3c016100ff3a7125e
            B/tables/TABLE-5-page-36-5/meta.json: 47e3b1feaa3681103c3292e413c4c920b23a0b98c223102c611412b906a203fb
            B/tables/TABLE-2-page-4-2/raw.json: b4011dbf51a1eadc3180bb69fbafb502632f030a0c554e42851c9fea579e5463
            B/tables/TABLE-2-page-4-2/prompt.txt: a1657b4d2a3257af8081caf9b9b1f83fbf19916b09d7070285ac4c07f670f1a8
            B/tables/TABLE-2-page-4-2/meta.json: 66d8800dba761264f2081681bbdfe9a101a1628fe4f1b3d8d5daea12b1e96d8c
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
          pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
          source_review: _compare/relationships-2026-11-16/review-current/NadeauCrosson1997
          source_status_sha256: 941e51273b21a58da6ef88fcd29b89f86b4937f7e20accedfc49a0bf589a0a06
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      proposal:
        id: R011
        exposure:
          text: tuberothalamic territory infarction and paramedian territory infarction
        outcome:
          text: aphasia
        analysis_label: Tuberothalamic/Paramedian Infarcts and Frontal-ITP-NR-CM System
        relation: association
        evidence_ids:
        - P24-S1-C5
        qualifier_ids:
        - P21-S1-C8
        - P22-S1-C4
        - P23-S1-C7
        context_ids: []
        table_ids: []
        approved: false
        status: requires_source_review
        flags:
        - new_model_candidate_not_verified
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
          source_review: _compare/relationships-2026-11-16/review-current/NadeauCrosson1997
          source_status_sha256: 941e51273b21a58da6ef88fcd29b89f86b4937f7e20accedfc49a0bf589a0a06
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
      audit:
        original_audit:
          coverage_issues:
          - Accounting without a linked unit P2-S2-C7
          - Unaccounted source passage P2-S2-C7
          - Accounting without a linked unit P4-S1-C2
          - Accounting without a linked unit P4-S1-C3
          - Unaccounted source passage P4-S1-C2
          - Unaccounted source passage P4-S1-C3
          - Result passage disposed without unit P4-S1-C4
          - Result passage disposed without unit P4-S1-C5
          - Result passage disposed without unit P4-S1-C6
          - Accounting without a linked unit P5-S1-C2
          - Unaccounted source passage P5-S1-C2
          - 'window 13: invalid/duplicate disposition P14-S2-C1'
          - Result passage disposed without unit P14-S2-C1
          - Accounting without a linked unit P20-S1-C9
          - Accounting without a linked unit P20-S2-C2
          - Accounting without a linked unit P20-S2-C3
          - Unaccounted source passage P20-S2-C2
          - Unaccounted source passage P20-S2-C3
          - Unaccounted source passage P20-S1-C9
          - Result passage disposed without unit P20-S2-C4
          - Result passage disposed without unit P21-S1-C6
          - Result passage disposed without unit P21-S1-C8
          - Accounting without a linked unit P22-S1-C11
          - Accounting without a linked unit P22-S1-C12
          - Unaccounted source passage P22-S1-C11
          - Unaccounted source passage P22-S1-C12
          - Result passage disposed without unit P23-S1-C4
          - Result passage disposed without unit P23-S1-C7
          - Result passage disposed without unit P23-S1-C10
          - Unresolved source passage P24-S1-C6
          - Accounting without a linked unit P25-S2-C5
          - Accounting without a linked unit P25-S2-C6
          - Unaccounted source passage P25-S2-C6
          - Unaccounted source passage P25-S2-C5
          - Result passage disposed without unit P33-S1-C1
          unattached_null_or_qualifier_ids:
          - P23-S1-C7
          suppressed_nonrepresented_units: 24
          default_disposition_count_requires_completeness_check: 322
          unselected_timing_passages: []
          personal_effect_slots_without_result_classification: []
          held_frame_selections:
          - slot: dependent_variable_statement
            source_id: P5-S1-C2
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P14-S2-C2
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: dependent_variable_statement
            source_id: P18-S2-C6
            reason: Requires a Methods outcome definition; model selection retained for inspection only
          - slot: analysed_sample
            source_ids:
            - P1-S1-C3
            - P1-S1-C6
            - P4-S1-C1
            - P4-S2-C1
            - P6-S1-C1
            - P12-S2-C2
            - P12-S2-C3
            - P12-S2-C5
            - P14-S1-C1
            - P17-S2-C3
            - P21-S1-C7
            - P23-S1-C8
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: recruited_sample
            source_ids:
            - P1-S1-C3
            - P1-S1-C6
            - P4-S1-C1
            - P4-S1-C4
            - P4-S1-C5
            - P4-S1-C7
            - P4-S1-C8
            - P5-S1-C6
            - P5-S1-C7
            - P5-S1-C8
            - P6-S1-C2
            - P12-S2-C2
            - P12-S2-C3
            - P12-S2-C5
            - P14-S1-C1
            - P17-S2-C3
            - P17-S2-C4
            - P21-S1-C7
            - P23-S1-C5
            - P23-S1-C6
            - P23-S1-C7
            - P23-S1-C8
            - P24-S1-C4
            - P25-S1-C1
            - P25-S1-C2
            - P25-S1-C4
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: imaging_provenance
            source_ids:
            - P1-S1-C4
            - P4-S1-C5
            - P5-S1-C6
            - P5-S1-C7
            - P5-S1-C8
            - P5-S2-C1
            - P12-S2-C5
            - P15-S2-C3
            - P18-S2-C4
            - P21-S1-C3
            - P24-S1-C2
            reason: Runaway selection (>8 passages); entire slot requires source review
          - slot: limitations
            source_ids:
            - P2-S1-C11
            - P2-S1-C12
            - P10-S1-C2
            - P9-S1-C9
            - P12-S2-C4
            - P13-S1-C4
            - P19-S1-C6
            - P19-S1-C7
            - P20-S1-C4
            - P24-S1-C6
            - P24-S1-C7
            - P25-S1-C7
            - P29-S2-C2
            - P29-S2-C5
            - P30-S2-C6
            reason: Runaway selection (>8 passages); entire slot requires source review
          empty_frame_slots_require_confirmation:
          - analysed_sample
          - recruited_sample
          - imaging_provenance
          - validation
          - analysis_restrictions
          - limitations
          - personal_factors
          - adjustment_roles
          - explicitly_not_adjusted
          unclassified_extraction_ids:
          - P22-S1-C12
          table_review_required:
          - TABLE-1-page-4-1
          - TABLE-2-page-4-2
          - TABLE-3-page-6-3
          - TABLE-4-page-14-4
          - TABLE-5-page-36-5
          unlinked_tables:
          - TABLE-2-page-4-2
          - TABLE-5-page-36-5
          source_anomalies: []
          visual_review_required:
            scope: All main-paper figures and table crops
            note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
            caption_candidate_units:
            - P9-S1
            - P10-S1
            - P15-S1
            - P16-S1
            - P21-S1
            - P22-S1
            - P23-S1
            - P24-S1
            - P35-S1
          approval: Not performed. Structural checks and model selections do not establish semantic correctness.
        candidate_discovery:
          model: gemma4:31b
          model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
          pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
          source_review: _compare/relationships-2026-11-16/review-current/NadeauCrosson1997
          source_status_sha256: 941e51273b21a58da6ef88fcd29b89f86b4937f7e20accedfc49a0bf589a0a06
          code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
          version: candidate-inventory-v1
        coverage:
        - source_id: P1-S1-C6
          disposition: background_or_descriptive
          result_indexes: []
          reason: Introduces hypothesis regarding the frontal lobe-ITP-NR-CM system.
        - source_id: P2-S2-C7
          disposition: background_or_descriptive
          result_indexes: []
          reason: General statement about lack of evidence for nonthalamic subcortical structures.
        - source_id: P4-S1-C1
          disposition: represented
          result_indexes:
          - 0
          reason: Provides the data table and summary of linguistic features for 33 cases.
        - source_id: P4-S1-C2
          disposition: represented
          result_indexes:
          - 0
          reason: Describes specific linguistic patterns (fluent but impaired comprehension/repetition/naming).
        - source_id: P4-S1-C3
          disposition: represented
          result_indexes:
          - 0
          reason: Describes nonfluent output patterns.
        - source_id: P4-S1-C4
          disposition: represented
          result_indexes:
          - 0
          reason: Reports 17 patients with no language disorder.
        - source_id: P4-S1-C5
          disposition: represented
          result_indexes:
          - 1
          reason: Links the analysis to cases with CT documentation.
        - source_id: P4-S1-C6
          disposition: background_or_descriptive
          result_indexes: []
          reason: General statement about single investigator reports.
        - source_id: P5-S1-C2
          disposition: represented
          result_indexes:
          - 2
          reason: States no correlation between infarct size/pattern and aphasia type/severity.
        - source_id: P6-S1-C2
          disposition: represented
          result_indexes:
          - 3
          reason: Reports that CdH hemorrhages are infrequently aphasic.
        - source_id: P8-S2-C7
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses repetition impairment in putamenal hemorrhage.
        - source_id: P14-S1-C8
          disposition: represented
          result_indexes:
          - 10
          reason: Qualifies the comparison between Table 4 and Table 1.
        - source_id: P14-S2-C1
          disposition: represented
          result_indexes:
          - 10
          reason: States association between temporal stem extension and posterior linguistic features.
        - source_id: P14-S2-C2
          disposition: represented
          result_indexes:
          - 10
          reason: Provides statistical significance for repetition impairment in temporal stem group.
        - source_id: P20-S2-C2
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes radiographic distinction of infarct types.
        - source_id: P20-S2-C3
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes radiographic distinction of infarct types.
        - source_id: P20-S2-C4
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes clinical distinction of paramedian infarcts.
        - source_id: P21-S1-C6
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes lesion map details.
        - source_id: P21-S1-C8
          disposition: represented
          result_indexes:
          - 11
          reason: Describes the typical thalamic aphasia features of the four cases.
        - source_id: P21-S1-C9
          disposition: background_or_descriptive
          result_indexes: []
          reason: Identifies infarct territory for cases BD and CG.
        - source_id: P21-S1-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes lesion anatomy for case BD.
        - source_id: P21-S1-C11
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes lesion anatomy for case CG.
        - source_id: P22-S1-C4
          disposition: represented
          result_indexes:
          - 11
          reason: Describes lesion anatomy for case CG.
        - source_id: P22-S1-C7
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses sparing of ITP-NR interface in paramedian infarcts.
        - source_id: P22-S1-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes patient WT's infarct.
        - source_id: P22-S1-C11
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes lesion anatomy for patient WT.
        - source_id: P23-S1-C4
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses potential roles of DM or LP in aphasia.
        - source_id: P23-S1-C7
          disposition: represented
          result_indexes:
          - 11
          reason: Identifies CM as the common nucleus involved in paramedian infarcts with aphasia.
        - source_id: P23-S1-C8
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes patient JB's infarct.
        - source_id: P23-S1-C9
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes lesion anatomy for patient JB.
        - source_id: P23-S1-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: Describes disruption of the frontal-ITP-NR-CM system in patient JB.
        - source_id: P24-S1-C4
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses cases of paramedian infarction without aphasia.
        - source_id: P25-S1-C7
          disposition: background_or_descriptive
          result_indexes: []
          reason: General hypothesis about the frontal-ITP-NR-CM system.
        - source_id: P29-S2-C2
          disposition: background_or_descriptive
          result_indexes: []
          reason: General statement about limited evidence.
        - source_id: P29-S2-C5
          disposition: background_or_descriptive
          result_indexes: []
          reason: General statement about lack of studies on frontal lobe lesions.
        - source_id: P33-S1-C1
          disposition: background_or_descriptive
          result_indexes: []
          reason: General conclusion summary.
        - source_id: P33-S1-C7
          disposition: background_or_descriptive
          result_indexes: []
          reason: General conclusion summary.
        - source_id: P33-S1-C8
          disposition: background_or_descriptive
          result_indexes: []
          reason: General conclusion summary.
        - source_id: P34-S1-C1
          disposition: background_or_descriptive
          result_indexes: []
          reason: Discusses syntax impairment in Parkinson's disease.
        - source_id: P34-S1-C10
          disposition: background_or_descriptive
          result_indexes: []
          reason: General conclusion summary.
        - source_id: P34-S2-C1
          disposition: background_or_descriptive
          result_indexes: []
          reason: General conclusion summary.
        unresolved_coverage: []
        pending_source_ids:
        - P1-S1-C6
        - P2-S2-C7
        - P4-S1-C6
        - P8-S2-C7
        - P14-S1-C8
        - P20-S2-C2
        - P20-S2-C3
        - P20-S2-C4
        - P21-S1-C6
        - P21-S1-C8
        - P21-S1-C9
        - P21-S1-C10
        - P21-S1-C11
        - P22-S1-C4
        - P22-S1-C7
        - P22-S1-C10
        - P22-S1-C11
        - P23-S1-C4
        - P23-S1-C7
        - P23-S1-C8
        - P23-S1-C9
        - P23-S1-C10
        - P24-S1-C4
        - P25-S1-C7
        - P29-S2-C2
        - P29-S2-C5
        - P33-S1-C1
        - P33-S1-C7
        - P33-S1-C8
        - P34-S1-C1
        - P34-S1-C10
        - P34-S2-C1
        pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
        tables_requiring_review:
        - TABLE-1-page-4-1
        - TABLE-2-page-4-2
        - TABLE-3-page-6-3
        - TABLE-4-page-14-4
        - TABLE-5-page-36-5
        paper_complete: false
        approved: false
        policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
      study_frame:
        slots:
          analysed_sample: []
          recruited_sample: []
          eligibility:
          - P4-S1-C5
          - P17-S2-C4
          imaging_provenance: []
          imaging_timing:
          - P12-S2-C5
          outcome_timing:
          - P12-S2-C5
          outcome_definition:
          - P3-S2-C5
          - P3-S2-C6
          - P3-S2-C7
          - P3-S2-C8
          - P4-S2-C1
          - P6-S1-C1
          - P12-S1-C4
          - P14-S2-C2
          validation: []
          analysis_restrictions: []
          dependent_variable_statement:
          - P3-S2-C5
          - P12-S1-C4
          - P18-S2-C4
          - P18-S2-C5
          limitations: []
          personal_factors: []
          tested_personal_effects:
          - P5-S1-C2
          adjustment_roles: []
          explicitly_not_adjusted: []
          descriptive_personal_factors:
          - P4-S1-C1
          - P12-S2-C2
          - P12-S2-C3
          - P14-S1-C1
          - P17-S2-C4
          - P21-S1-C8
          - P24-S1-C4
        outcome_type: both_reported
        imaging_vs_outcome: mixed
        validation_type: none_described
        window_merge: Union of selected IDs; differing window enums retained conservatively as both/mixed. Not verified study-level facts.
        held_selections:
        - slot: dependent_variable_statement
          source_id: P5-S1-C2
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P14-S2-C2
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: dependent_variable_statement
          source_id: P18-S2-C6
          reason: Requires a Methods outcome definition; model selection retained for inspection only
        - slot: analysed_sample
          source_ids:
          - P1-S1-C3
          - P1-S1-C6
          - P4-S1-C1
          - P4-S2-C1
          - P6-S1-C1
          - P12-S2-C2
          - P12-S2-C3
          - P12-S2-C5
          - P14-S1-C1
          - P17-S2-C3
          - P21-S1-C7
          - P23-S1-C8
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: recruited_sample
          source_ids:
          - P1-S1-C3
          - P1-S1-C6
          - P4-S1-C1
          - P4-S1-C4
          - P4-S1-C5
          - P4-S1-C7
          - P4-S1-C8
          - P5-S1-C6
          - P5-S1-C7
          - P5-S1-C8
          - P6-S1-C2
          - P12-S2-C2
          - P12-S2-C3
          - P12-S2-C5
          - P14-S1-C1
          - P17-S2-C3
          - P17-S2-C4
          - P21-S1-C7
          - P23-S1-C5
          - P23-S1-C6
          - P23-S1-C7
          - P23-S1-C8
          - P24-S1-C4
          - P25-S1-C1
          - P25-S1-C2
          - P25-S1-C4
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: imaging_provenance
          source_ids:
          - P1-S1-C4
          - P4-S1-C5
          - P5-S1-C6
          - P5-S1-C7
          - P5-S1-C8
          - P5-S2-C1
          - P12-S2-C5
          - P15-S2-C3
          - P18-S2-C4
          - P21-S1-C3
          - P24-S1-C2
          reason: Runaway selection (>8 passages); entire slot requires source review
        - slot: limitations
          source_ids:
          - P2-S1-C11
          - P2-S1-C12
          - P10-S1-C2
          - P9-S1-C9
          - P12-S2-C4
          - P13-S1-C4
          - P19-S1-C6
          - P19-S1-C7
          - P20-S1-C4
          - P24-S1-C6
          - P24-S1-C7
          - P25-S1-C7
          - P29-S2-C2
          - P29-S2-C5
          - P30-S2-C6
          reason: Runaway selection (>8 passages); entire slot requires source review
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
          pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
          review_sha256: c96516efc03a79ca5e7782ac2dfa151e1f940e723cebc823dd2ae2b2c881abd3
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
          - P24-S1-C5
          source_result: The authors conclude that the common anatomical feature in cases of tuberothalamic and paramedian territory infarction associated with aphasia is involvement of the frontal-ITP-NR-CM system, based on a limited series of patients with lesion mapping.
          result_status: qualitative_synthesis
          patient_measurement: template_lesion_overlap
          checks:
            analysis_identity:
              answer: fits
              reason: The source (P24-S1-C5) explicitly states the conclusion that tuberothalamic and paramedian infarcts with aphasia share involvement of the frontal-ITP-NR-CM system. The proposed core correctly identifies this as the analysis result, distinguishing it from the specific vascular territories by focusing on the common anatomical substrate.
              source_ids:
              - P24-S1-C5
              - P20-S1-C7
            direction:
              answer: fits
              reason: The source describes a positive association (involvement of the system is the common factor in aphasia cases). The proposed direction 'likely' is appropriate for a hypothesis-generating conclusion based on limited evidence, as stated in P24-S1-C5 ('conclude on the basis of this limited evidence').
              source_ids:
              - P24-S1-C5
            construct:
              answer: fits
              reason: The exposure is correctly identified as the infarct territories (tuberothalamic/paramedian) which are analyzed for their anatomical overlap. The outcome is aphasia. The measurement is the overlap of patient lesions with the defined frontal-ITP-NR-CM system, which is a template-based lesion mapping approach (using Hassler nomenclature and AC-PC coordinates as per P21-S1-C3/C5), not patient-specific diffusion tractography.
              source_ids:
              - P24-S1-C5
              - P21-S1-C3
              - P21-S1-C5
            qualifications:
              answer: fits
              reason: The proposed core includes the qualification 'based on limited evidence from a small number of cases', which aligns with P24-S1-C5 ('on the basis of this limited evidence') and P24-S1-C6 ('Few published cases... have included sufficiently precise mapping'). The limitation regarding NRVA/NR-to-CM projections is also correctly captured.
              source_ids:
              - P24-S1-C5
              - P24-S1-C6
            missing_material_caveat:
              answer: fits
              reason: The core captures the main caveat about the limited evidence and mapping precision. No other material caveats that would change the interpretation of this specific conclusion are omitted from the provided source window.
              source_ids:
              - P24-S1-C5
              - P24-S1-C6
          optional_pending: []
          verdict: draft
          reason: All five core checks fit the source.
          material_issues: []
        pending_details:
        - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
        - Recovery phase is not classified; use the reported timing words.
        - Evidence-strength rating is a conservative draft placeholder pending human review.
        normalizations: []
        analysis_identity:
          id: R011
          exposure:
            text: tuberothalamic territory infarction and paramedian territory infarction
          outcome:
            text: aphasia
          analysis_label: Tuberothalamic/Paramedian Infarcts and Frontal-ITP-NR-CM System
          relation: association
          evidence_ids:
          - P24-S1-C5
          qualifier_ids:
          - P21-S1-C8
          - P22-S1-C4
          - P23-S1-C7
          context_ids: []
          table_ids: []
          approved: false
          status: requires_source_review
          flags:
          - new_model_candidate_not_verified
          candidate_discovery:
            model: gemma4:31b
            model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
            pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
            source_review: _compare/relationships-2026-11-16/review-current/NadeauCrosson1997
            source_status_sha256: 941e51273b21a58da6ef88fcd29b89f86b4937f7e20accedfc49a0bf589a0a06
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
      page: 24
      quote: 'Thus, we conclude on the basis of this limited evidence that the one thing

        that cases of tuberothalamic territory infarction and cases of paramedian ter-

        ritory infarction with aphasia have in common is involvement of the frontal–

        ITP–NR–CM system.'
      status: pending
      by: agent:relationship-converter
      date: '2026-11-25'
      note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
  original_mapping:
    decision: draft
    reason: The authors analyzed a small series of patients with tuberothalamic and paramedian territory infarcts to identify a common anatomical substrate for their aphasia, concluding that involvement of the frontal-ITP-NR-CM system is the shared feature.
    bucket: regions
    entity_id: frontal_itp_nr_cm_system
    name: frontal-ITP-NR-CM system cluster
    kind: network
    predictor_type: imaging_metric
    definition: Patient lesion overlap with the system comprising the frontal lobes, inferior thalamic peduncle (ITP), nucleus reticularis (NR), and centromedian nucleus (CM).
    assessment: []
    target: aphasia
    target_kind: impairment
    claim: Cases of tuberothalamic territory infarction and cases of paramedian territory infarction with aphasia have in common involvement of the frontal-ITP-NR-CM system.
    direction: likely
    method: LSM
    relationship: correlational
    therapy: null
    sample_n: null
    population: patients with tuberothalamic or paramedian territory thalamic infarcts
    timing: concurrent
    qualifications:
    - based on limited evidence from a small number of cases
    limitations:
    - few published cases of tuberothalamic infarction have sufficiently precise mapping to determine if NRVA or NR-to-CM projections are invariably involved
    optional_pending: []
    evidence_quality: cohort
    passages:
    - source_id: P24-S1-C5
      supports: claim
    - source_id: P21-S1-C8
      supports: sample
    - source_id: P22-S1-C4
      supports: method
    - source_id: P23-S1-C7
      supports: method
    - source_id: P24-S1-C6
      supports: limitation
  original_attempt:
    binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
      review_sha256: c96516efc03a79ca5e7782ac2dfa151e1f940e723cebc823dd2ae2b2c881abd3
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
    proposal: R011
    status: draft
    reason: All five core checks fit the source.
    material_issues: []
    path: drafts/regions/frontal_itp_nr_cm_system__NadeauCrosson1997__R011.md
    seconds_this_run: 85.75125170798856
  source_check:
    profile: agent-repair
    scope: Agent source reconstruction; original model reviews do not certify the changed record. No independent model pass or human approval.
    approved: false
    paper_complete: false
    binding:
      pdf_sha256: 42852a88c6b3696c4fbb6e6a4561d28a636098b234890eef17469398c5440182
      original_mapping_sha256: a83ea9cc9d614b9e23120e5599f60a63258ea83f1e9275e859f2b715cb5ff82d
      original_status_sha256: 007cbb7cac406b353b73d4edf9d027818db29550338391e4fccb3512cb8a5354
      evidence_sha256: 4f00a6a885fc1786f3a93750068b7143070547f6a38ecf6d6e1baf37b832454c
    publication_correction:
      by: agent:source-repair
      date: '2026-11-26T02:05:16.806224+00:00'
      pdf_pages:
      - 1
      - 21
      - 22
      - 23
      - 24
      note: Reclassified as a secondary review report, explicitly attributing the result to the authors’ limited-evidence synthesis of previously reported thalamic cases. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
      approved: false
      audit: logs/publication/draft-repairs-2026-11-26-round2.json
    remaining:
    - Human source review and approval
    - Full paper completeness review
reviewer_marks:
- id: relationship-source-check
  page: 24
  quote: 'Thus, we conclude on the basis of this limited evidence that the one thing

    that cases of tuberothalamic territory infarction and cases of paramedian ter-

    ritory infarction with aphasia have in common is involvement of the frontal–

    ITP–NR–CM system.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-25'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: source-repair-round2
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: Reclassified as a secondary review report, explicitly attributing the result to the authors’ limited-evidence synthesis of previously reported thalamic cases. This is not a new primary sample or independent replication; quantitative estimates and study-level attribution require human verification against the primary publication.
---

# Source review required

This repaired draft remains unapproved. Original outputs and review provenance are preserved.
