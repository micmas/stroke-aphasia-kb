---
id: pace_therapy
name: PACE therapy
kind: therapy
findings:
- id: f1
  target: language_performance
  target_kind: impairment
  claim: In a pilot study of chronic aphasia, only one member of the PACE group showed the same amount of change on the WAB AQ and BNT as the CILT group, and this was the participant who selected the spoken modality almost exclusively in therapy; otherwise, there was no evidence of continued gains during the follow-up interval for available PACE participants.
  direction: unlikely
  relationship: treatment_response
  method: behavioral_only
  sample:
    n: 5
    population: Adults with a single, left hemisphere CVA at least one year prior, right hand dominance, and English speaking, who had previously received speech-language intervention.
    phase: not_reported
    time_post_onset: Pre-therapy, post-therapy, and one month after therapy was finished.
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Sample of convenience, not a randomized clinical trial
  - Small sample size
  - Higher incidence of severe apraxia of speech impairment in the comparison group
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: A modified Promoting Aphasic Communicative Effectiveness (PACE) treatment approach where participants are permitted to communicate using any and all modalities (e.g., gesturing, pointing, writing) during therapy sessions, with treatment stimuli semantically organized and requiring expression of each element of the utterance. The PACE group was balanced with the CILT group based on aphasia severity and degree of apraxia of speech rather than randomized; One PACE participant (P5) refused to use any modality other than speech, making their experience similar to CILT. Additional metadata has not been transcribed; review the pending-field flags before approval. Publication correction (human verification pending): Nonrandomized repeated-measures pilot. CILT: 5 enrolled, 4 completed; PACE: 6 enrolled, 5 completed. Sample field now describes the relevant completers, with follow-up availability retained as a limitation.'
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
    - proposed_concept:language_performance
    - publication_correction_pending_human_verification
  therapy:
    id: pace_therapy
    name: PACE therapy
  citation: '@Maher2006'
  source_passages:
  - section: Original source P6-S1-C7
    page: 6
    quote: 'In contrast, only one member of the PACE group evinced

      the same mount of change on the WAB and BNT, and this

      was the participant who selected the spoken modality almost

      exclusively in therapy.'
    supports: claim
  - section: Original source P6-S1-C9
    page: 6
    quote: 'There was no evidence of continued gains during the

      follow-up interval for any of the PACE participants for whom

      follow-up data were available.'
    supports: claim
  - section: Original source P3-S2-C10
    page: 3
    quote: 'Inclusion criteria were a single, left hemisphere CVA at

      least one year prior (confirmed by CT or MRI), right hand

      dominance, and English speaking with a negative history of

      other neurologic impairments or learning disability.'
    supports: sample
  - section: Original source P3-S3-C2
    page: 3
    quote: 'There

      were five participants in the CILT group and six partici-

      pants in the comparison group.'
    supports: sample
  - section: Original source P4-S1-C12
    page: 4
    quote: 'For the comparison group intervention was modeled after

      a modified PACE treatment approach (Carlomagno, 1994;

      Chin Li et al., 1988; Davis & Wilcox, 1985; Glindemann &

      Springer, 1995).'
    supports: method
  - section: Original source P4-S1-C13
    page: 4
    quote: 'The PACE participants were permitted to

      communicate in any and all modalities (e.g., gesturing, point-

      ing, writing, etc) throughout the therapy session.'
    supports: method
  - section: Original source P4-S1-C14
    page: 4
    quote: 'This ver-

      sion of PACE differed from the conventional version of

      PACE in that the treatment stimuli were semantically orga-

      nized and the subjects were required to express each ele-

      ment of the utterance rather than the communication of a

      general idea.'
    supports: method
  - section: Original source P3-S3-C14
    page: 3
    quote: 'Therapy for both groups consisted of three-

      hour sessions, four days a week, for two weeks.'
    supports: method
  - section: Original source P2-S3-C9
    page: 2
    quote: 'To assess

      behavioral change, the aphasia measures were administered

      pre- and post-therapy and at one month after therapy was

      finished.'
    supports: method
  - section: Original source P3-S1-C1
    page: 3
    quote: '

      in performance immediately upon completion of therapy

      and again one month after therapy was concluded: The

      Aphasia Quotient (AQ) from the Western Aphasia Battery

      (WAB) (Kertesz, 1982), the Boston Naming Test (BNT)

      (Kaplan et al., 2000) raw score, Action Naming Test (ANT)

      (Nicholas et al., 1985) raw score, Apraxia Battery for

      Adults-2, (ABA-2) (subtest 2A repeated words) (Dabul,

      2000), and a narrative discourse sample (Cinderella retell-

      ing).'
    supports: method
  - section: Original source P3-S2-C12
    page: 3
    quote: 'Given the sample size, group assignment to the Con-

      straint Induced Language Therapy (CILT) group or the com-

      parison group (described below) could not be randomized

      without the risk of having different aphasia syndromes and

      severities in the two groups.'
    supports: confounders
  - section: Original source P8-S2-C11
    page: 8
    quote: 'First, this was a sample of convenience,

      not a randomized clinical trial.'
    supports: limitation
  - section: Original source P7-S2-C3
    page: 7
    quote: 'One potentially confounding factor in our study was the

      higher incidence of severe apraxia of speech impairment in

      the comparison group.'
    supports: limitation
  design: longitudinal
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Maher2006
  proposal_id: R007
  review_status_sha256: 28d0f5fe6a26db4ea8aeea874974a43abde08265d0d3d3aa189aa87137b9bf7d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 5a0ee67e9b271d6aa0a9023fe42d054f07daf04814486e5fc9fe5c4566a04b8a
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 5a0ee67e9b271d6aa0a9023fe42d054f07daf04814486e5fc9fe5c4566a04b8a
        A/passages.json: 9bfdbbc641afb8546745616f2b67539bfe84912e81def1c78322760e8abb3aa7
        A/raw.json: 4e19e3b5206c5a0223f76628a12933c120347f354ef72ee303ca2bbb9d836ff3
        A/source-units.json: b2e280129f8604c9d72fccb974ea2b0be16f841f8c89ab7d926deb736c0e3a19
        A/full-source-units.json: 2d796fa55fdec9fe4131a0ded95925dc426a53d015a9c498a908af4a0d79536d
        A/meta.json: 276e589b745cabf570634562d7f9b5f2bcadbb8a5793868957bb2464315f926e
        A/table-images/TABLE-1-page-3-1.png: 1935e88d30275576e24fac31627cfca9bda7f382dfb5c0bed9a9b7a52f507a82
        A/table-images/page-3.png: 42af98c2bf302a5c3f4be1cec849ebac389b263dc7876147cef758b3b220c31c
        A/table-images/page-6.png: afe4259a658b545156b4fc29f1440e12496c179de32582bf634d89fca942467e
        A/table-images/page-5.png: decc33925466b97b8434d6266a35c9a23fa2b0767e7a89256593d7fb6392d3c2
        A/table-images/page-4.png: f54d0e7b41f11116b130c4fc32aa0209b1726b0df63275bd11defd94392a87ed
        A/table-images/TABLE-1-page-4-1.png: c30bafd7b307025ce33c55e5947097445c2909e5b0688badc34981f5ae6095c5
        A/table-images/TABLE-3-page-6-1.png: 3a4d305a5e774100609d69afc9ccfd9f63412bfbff239295d89879c8e01acf53
        A/table-images/manifest.json: 94c049a239302db0f797d7897536effd55deb41c8fb70cdb8c6960bfb25c921c
        A/table-images/TABLE-2-page-5-1.png: 07c85874743fbbd5394593fd378f960a9dfd8a575fa42f8b845f4ec2dd0a0aa1
        A/clauses/window-03/raw.json: d44dc788b15a712c90ed3724bf8f6bc3225e234ac3da90d2acfae00d1be36426
        A/clauses/window-03/prompt.txt: 66dc61d0fb1ac9b80882b55354e9c64233ad44f36ea5d94f475d2fc90e886cc9
        A/clauses/window-03/meta.json: 7604cc401a069b101e6837f6bb63e6d6dd8ddd0695b59447549d3f6bd48d79f1
        A/clauses/window-04/raw.json: 58a8b367e1604863a4595d063ecec59206849d2add090922ac8d175c6207cf48
        A/clauses/window-04/prompt.txt: 36940f852b1452afcac44438b1d0ffd5ff3c048fb83d6ab12c45df09fce59774
        A/clauses/window-04/meta.json: 9e29dc0e53b59ef4a801df393477f94391e7e8a5af82f1e2f47eec35c00a011f
        A/clauses/window-05/raw.json: b8b9f80927aa814787778d520f73af72e96a94aaf5faf2b5e19903a9a525d65e
        A/clauses/window-05/prompt.txt: da4bc459370b10ea940dbf8f6c81facd699b189e87b6fb3102aceb81c2855545
        A/clauses/window-05/meta.json: 7b1e4e36c8b49b64a4d01c5da915eb785f001349c89e0753b807dfc0584e4bae
        A/clauses/window-02/raw.json: 431fac9be92dc86a0b4c6099d695208c73c889eff0d5e2590043b8823fe1cbe7
        A/clauses/window-02/prompt.txt: 9fb6213dfd8fd344f6e64e6ca24dbbc285e667456605c1ebe5214fa6d9444a4e
        A/clauses/window-02/meta.json: 20dab6b307e5f7e7b86902e26d9375e437e7e456f53e29077bf3b7a50bd3761e
        A/clauses/window-07/raw.json: 6af010420530be3582c009960966949a2d7084ce8bca3957c658f01d1dac93d6
        A/clauses/window-07/prompt.txt: c775f69c0ed4b447fe0dbc3ce5f1a832d1ec823a44cd7c69b50070ececaf1bf8
        A/clauses/window-07/meta.json: e6f3466fbff811863c6ceb7bc4a93374d2ae9811aea0199d37fae63fd2f306ec
        A/clauses/window-01/raw.json: 17ac5139ee073e8d2e040eebcbb7345e5a8f6ca2f17d79855c8e3b2eb8e6b82d
        A/clauses/window-01/prompt.txt: 4bcba4fe5292d3dd9eb184c466550d7a614fcab73c97ab1603e67830aa0cdb8d
        A/clauses/window-01/meta.json: b9c0492db118f9d123a5ac876da923c323291d619c2e61db2041c1b56676e1de
        A/clauses/window-06/raw.json: 9276528da16fd59ba36df25861627e8ee159970b797e0593718445b3f9f6a5fd
        A/clauses/window-06/prompt.txt: 5c27ea6ae6305a63e34d89da9d3453a388e7896103b18fae85cdb8e49bb9c0d6
        A/clauses/window-06/meta.json: eb807a2b8d6763db219ec38242d63659f5c247caeccb346d2964d15bf86d8068
        A/clauses/window-08/raw.json: 29583290764360166e2acca8ec15f42acfeb4e16805bb5be300a543fe2914711
        A/clauses/window-08/prompt.txt: 9a0913605f20e7093db44c9d84ee1d8f03424f3e2cac539f2e84b22fef7015bc
        A/clauses/window-08/meta.json: e2b2f20095039efd07a9186fa65dabcd51ab1ba999683400e61801a9c14035d1
        A/tables/TABLE-2-page-5-3/raw.json: 1a905183bb05b6bc4fe3c043c7309d2a71e1a58b4cfdeeb0c3f7124893794eea
        A/tables/TABLE-2-page-5-3/prompt.txt: 66f1576323816bbcdbed35c4be9bd42c71dffe58b77aae192650cf69d6efbfca
        A/tables/TABLE-2-page-5-3/meta.json: 27d4d76c96a30f10a9071433b5a96abbf9fd51d739afe8aa306173c05b68ef10
        A/tables/TABLE-1-page-4-2/raw.json: 25276daffee7bf4876c0f06f8ce079f1a11bc01c1f37875bbd205b443e226389
        A/tables/TABLE-1-page-4-2/prompt.txt: 8ed583498916c8ac33d045775a808e3ca5837bf77602ff47d99ea2e1e1399350
        A/tables/TABLE-1-page-4-2/meta.json: b8bd970b915f56c653d849cce907bbe7fbd4616c6fb29b35dbd6d7f3ed88e014
        A/tables/TABLE-3-page-6-4/raw.json: 478dcaa5bf3e441543bfc5e1b6e86000b80d3a04be505f89078da5507cd2c96f
        A/tables/TABLE-3-page-6-4/prompt.txt: a6f74fa5528c6c4d9dfcd8246389cf2a5e5ae30dd6a655860eb948a9265a317f
        A/tables/TABLE-3-page-6-4/meta.json: bad2b8ef9c184f9343d169f2603442ca99fef707cbdf6decaee9b689bbc27bbd
        A/tables/TABLE-1-page-3-1/raw.json: b4caac489357f8aebe9349846d6ea3e346987c8143fa4d1b5e01c42034fbade0
        A/tables/TABLE-1-page-3-1/prompt.txt: 5d3b015981ba0d8fd1bf1022af206ee8de8b48a01be73b8aa5d7c5a22f6d73da
        A/tables/TABLE-1-page-3-1/meta.json: 8bb72e1dbc1fc7df908f90566fe32ae1a92b28d63e08262bacf145d76eaee68d
        B/passages.json: 9bfdbbc641afb8546745616f2b67539bfe84912e81def1c78322760e8abb3aa7
        B/raw.json: 7c7e1272030350645d7fb48680cac47e0e7324e2c0bc74f988afc31dd185bee4
        B/source-units.json: b2e280129f8604c9d72fccb974ea2b0be16f841f8c89ab7d926deb736c0e3a19
        B/full-source-units.json: 2d796fa55fdec9fe4131a0ded95925dc426a53d015a9c498a908af4a0d79536d
        B/meta.json: 9c5913fe7913f21e39c4daa3c02a7ed0912faacbd666a67a98f862ee8eec3408
        B/table-images/TABLE-1-page-3-1.png: 1935e88d30275576e24fac31627cfca9bda7f382dfb5c0bed9a9b7a52f507a82
        B/table-images/page-3.png: 42af98c2bf302a5c3f4be1cec849ebac389b263dc7876147cef758b3b220c31c
        B/table-images/page-6.png: afe4259a658b545156b4fc29f1440e12496c179de32582bf634d89fca942467e
        B/table-images/page-5.png: decc33925466b97b8434d6266a35c9a23fa2b0767e7a89256593d7fb6392d3c2
        B/table-images/page-4.png: f54d0e7b41f11116b130c4fc32aa0209b1726b0df63275bd11defd94392a87ed
        B/table-images/TABLE-1-page-4-1.png: c30bafd7b307025ce33c55e5947097445c2909e5b0688badc34981f5ae6095c5
        B/table-images/TABLE-3-page-6-1.png: 3a4d305a5e774100609d69afc9ccfd9f63412bfbff239295d89879c8e01acf53
        B/table-images/manifest.json: befd178f0dff4131453babcd6f82bae3824d53b9854f24665c0e8c9da0eaae97
        B/table-images/TABLE-2-page-5-1.png: 07c85874743fbbd5394593fd378f960a9dfd8a575fa42f8b845f4ec2dd0a0aa1
        B/clauses/window-03/raw.json: ce61ba19c239f048a465f74c91364928f0c34d24dc9c5d25d1c6ad38e78a086e
        B/clauses/window-03/prompt.txt: 66dc61d0fb1ac9b80882b55354e9c64233ad44f36ea5d94f475d2fc90e886cc9
        B/clauses/window-03/meta.json: 9bf7d1cac6a63805f29501cf91b839f366e6ea77cd2faf4bc7b0aee00f557bc8
        B/clauses/window-04/raw.json: 7c799572a7a89954ca6e0ae9d921cf299c0da0f45d90da925b7a4882e160002a
        B/clauses/window-04/prompt.txt: 36940f852b1452afcac44438b1d0ffd5ff3c048fb83d6ab12c45df09fce59774
        B/clauses/window-04/meta.json: cc5945bbcbc6b4f68b0fd6a533cd552c21e13af96b9f3f0f2effa33655d841a8
        B/clauses/window-05/raw.json: adf3a13c3ca38801dc2d9b5de65fa0cdac48991c9b133d1a65f2798b4e9406d5
        B/clauses/window-05/prompt.txt: da4bc459370b10ea940dbf8f6c81facd699b189e87b6fb3102aceb81c2855545
        B/clauses/window-05/meta.json: a0009ad2ad0769334f372e8deee1dfd6236c4d9de3f4ff429ee0aa74895b2ccf
        B/clauses/window-02/raw.json: 0fe77da5ef8eca0802508dd03d2dfccfa64297df087992ead544028bfa7bb9f3
        B/clauses/window-02/prompt.txt: 9fb6213dfd8fd344f6e64e6ca24dbbc285e667456605c1ebe5214fa6d9444a4e
        B/clauses/window-02/meta.json: c230cdd207c15139ea0a503f19510b93827b4feeedb90495bfd5eef1aff43c3c
        B/clauses/window-07/raw.json: 07de0d002b9d4bf306444a07048da83bdd320a27c0f1b9cda5e234f1512c5c15
        B/clauses/window-07/prompt.txt: c775f69c0ed4b447fe0dbc3ce5f1a832d1ec823a44cd7c69b50070ececaf1bf8
        B/clauses/window-07/meta.json: d1ea7bf5c6fea3b34aad3616b05ff25d68056ddc9453ac48c41304de1704a6cb
        B/clauses/window-01/raw.json: 3ca55830dad1ffc65d1e79471c69221a4fc7173a2846e5032fb7b99e78be56e6
        B/clauses/window-01/prompt.txt: 4bcba4fe5292d3dd9eb184c466550d7a614fcab73c97ab1603e67830aa0cdb8d
        B/clauses/window-01/meta.json: 4841928ad51795556f5b7d91eb80cfefdd1051a9d12edd072ad86ee6d8eaa614
        B/clauses/window-06/raw.json: cc82db8512a5ee3376739ce328bc57f9e0a877894f7e97cb2e9b4dc456a47cb4
        B/clauses/window-06/prompt.txt: 5c27ea6ae6305a63e34d89da9d3453a388e7896103b18fae85cdb8e49bb9c0d6
        B/clauses/window-06/meta.json: 0e335ea5684ede21e72a65900b0d8037f08e6c068de96b451605d7d3c38b0e9c
        B/clauses/window-08/raw.json: 8d7efb1afbe5bd431613518369c242e4c9750271cb51dc212d310fa4d4f385bb
        B/clauses/window-08/prompt.txt: 9a0913605f20e7093db44c9d84ee1d8f03424f3e2cac539f2e84b22fef7015bc
        B/clauses/window-08/meta.json: ba7298b3e248b62203b616c8cb9036d83fcb7ffc49f4e78fac3d29c65c9e889c
        B/tables/TABLE-2-page-5-3/raw.json: c66cf54a65e71eec49278db2c4f707b759f9d1b11f355b9c7f4e79f86c0cf8bc
        B/tables/TABLE-2-page-5-3/prompt.txt: 66f1576323816bbcdbed35c4be9bd42c71dffe58b77aae192650cf69d6efbfca
        B/tables/TABLE-2-page-5-3/meta.json: f66a40592c9aae92086b06ebc16dfd07233ff900ee9ca5312cf6760fa279e545
        B/tables/TABLE-1-page-4-2/raw.json: c54b2047c5cfc1fe28c93e4f92b85ae3cf269f352b5e4b3c5591613165f1a0d2
        B/tables/TABLE-1-page-4-2/prompt.txt: 8ed583498916c8ac33d045775a808e3ca5837bf77602ff47d99ea2e1e1399350
        B/tables/TABLE-1-page-4-2/meta.json: 0fe563866e60e45bb715883ef7393ae31f977c289596d71ea314d91cbebd8754
        B/tables/TABLE-3-page-6-4/raw.json: 45d4f8b4d3b5975e0568f4904aa5dfaa9afa3ffa476a43c15d3cb984253d46ca
        B/tables/TABLE-3-page-6-4/prompt.txt: a6f74fa5528c6c4d9dfcd8246389cf2a5e5ae30dd6a655860eb948a9265a317f
        B/tables/TABLE-3-page-6-4/meta.json: 6db7778481deeabd83e467ac88ae447b9696121e1cd96bd53d43dbae4b69d37c
        B/tables/TABLE-1-page-3-1/raw.json: 9900a7969ac637bc22cb7304a9cfdd2621b6f98bf8beba6c29282bfaed28c8da
        B/tables/TABLE-1-page-3-1/prompt.txt: 5d3b015981ba0d8fd1bf1022af206ee8de8b48a01be73b8aa5d7c5a22f6d73da
        B/tables/TABLE-1-page-3-1/meta.json: 05814dae6c00a1f7edac6685b69b1a2a91bf6c06dc943ff2efa5199ca3d31f80
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
      pdf_sha256: 5a0ee67e9b271d6aa0a9023fe42d054f07daf04814486e5fc9fe5c4566a04b8a
      source_review: _compare/relationships-2026-11-16/review-current/Maher2006
      source_status_sha256: 525a65a1fa13c1156e036fb15945d18b1bf1df66d8948b333d35bfc5b54a131b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R007
    exposure:
      text: PACE therapy
    outcome:
      text: WAB AQ and BNT
    analysis_label: Individual case analysis (PACE group)
    relation: association
    evidence_ids:
    - P6-S1-C7
    qualifier_ids:
    - P5-S3-C1
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 5a0ee67e9b271d6aa0a9023fe42d054f07daf04814486e5fc9fe5c4566a04b8a
      source_review: _compare/relationships-2026-11-16/review-current/Maher2006
      source_status_sha256: 525a65a1fa13c1156e036fb15945d18b1bf1df66d8948b333d35bfc5b54a131b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S3-C12
      - Result passage disposed without unit P3-S3-C9
      - Result passage disposed without unit P4-S2-C10
      - Result passage disposed without unit P4-S2-C11
      - Result passage disposed without unit P4-S2-C12
      - Accounting without a linked unit P5-S2-C5
      - Unaccounted source passage P5-S2-C5
      - Result passage disposed without unit P5-S2-C12
      - Accounting without a linked unit P5-S2-C14
      - Result passage disposed without unit P5-S2-C6
      - Result passage disposed without unit P5-S2-C7
      - Result passage disposed without unit P5-S2-C8
      - Result passage disposed without unit P5-S2-C9
      - Unaccounted source passage P5-S2-C14
      - Result passage disposed without unit P5-S2-C15
      - Result passage disposed without unit P6-S1-C1
      - Result passage disposed without unit P6-S1-C11
      - Result passage disposed without unit P6-S1-C12
      - Unresolved source passage P6-S1-C17
      - Result passage disposed without unit P7-S1-C1
      - Result passage disposed without unit P7-S1-C3
      - Result passage disposed without unit P7-S1-C5
      - Result passage disposed without unit P7-S1-C8
      - Accounting without a linked unit P7-S1-C11
      - Accounting without a linked unit P7-S1-C12
      - Result passage disposed without unit P7-S2-C3
      - Accounting without a linked unit P7-S2-C5
      - Accounting without a linked unit P8-S1-C8
      - Unaccounted source passage P8-S1-C8
      - Unaccounted source passage P7-S1-C12
      - Unaccounted source passage P7-S2-C5
      - Unaccounted source passage P7-S1-C11
      - 'window 10: invalid/duplicate disposition P8-S1-C11'
      - Result passage disposed without unit P8-S1-C9
      - Result passage disposed without unit P8-S2-C3
      - Result passage disposed without unit P8-S2-C4
      - Result passage disposed without unit P8-S2-C5
      - Result passage disposed without unit P8-S2-C6
      unattached_null_or_qualifier_ids:
      - P5-S2-C12
      - P5-S2-C14
      - P5-S2-C15
      - P7-S1-C3
      - P8-S2-C5
      suppressed_nonrepresented_units: 22
      default_disposition_count_requires_completeness_check: 164
      unselected_timing_passages:
      - P2-S2-C4
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P5-S2-C13
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      - slot: dependent_variable_statement
        source_id: P6-S1-C13
        reason: Requires a Methods outcome definition; model selection retained for inspection only
      empty_frame_slots_require_confirmation:
      - imaging_provenance
      - imaging_timing
      - validation
      - analysis_restrictions
      - dependent_variable_statement
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-1-page-4-2
      - TABLE-2-page-5-3
      - TABLE-3-page-6-4
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-1-page-4-2
      - TABLE-3-page-6-4
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness. Figures are not automatically interpreted.
        caption_candidate_units:
        - P6-S1
        - P6-S2
        - P7-S2
      approval: Not performed. Structural checks and model selections do not establish semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 5a0ee67e9b271d6aa0a9023fe42d054f07daf04814486e5fc9fe5c4566a04b8a
      source_review: _compare/relationships-2026-11-16/review-current/Maher2006
      source_status_sha256: 525a65a1fa13c1156e036fb15945d18b1bf1df66d8948b333d35bfc5b54a131b
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C10
      disposition: repeated
      result_indexes:
      - 0
      - 8
      reason: Abstract restatement of results
    - source_id: P2-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a prior study (Pulvermüller et al., 2001)
    - source_id: P2-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a prior study (Pulvermüller et al., 2001)
    - source_id: P2-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes results of a prior study (Meinzer et al., 2005)
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline demographic/clinical comparison
    - source_id: P3-S3-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline clinical description
    - source_id: P3-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline clinical description
    - source_id: P3-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline clinical description
    - source_id: P3-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline clinical description
    - source_id: P3-S3-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Baseline screening data
    - source_id: P4-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of treatment process (shaping)
    - source_id: P4-S2-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of participant behavior during treatment
    - source_id: P4-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Description of treatment process
    - source_id: P5-S2-C5
      disposition: represented
      result_indexes:
      - 10
      reason: Reports increase in difficulty levels as a measure of communication improvement
    - source_id: P5-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anecdotal reports of enjoyment/benefit
    - source_id: P5-S2-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anecdotal report of frustration
    - source_id: P5-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anecdotal report of frustration
    - source_id: P5-S2-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Anecdotal report of participant preference
    - source_id: P5-S2-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 2
    - source_id: P5-S2-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statistical methodology statement
    - source_id: P5-S2-C13
      disposition: represented
      result_indexes:
      - 0
      reason: Reports significant change on WAB AQ for both groups
    - source_id: P5-S2-C14
      disposition: represented
      result_indexes:
      - 0
      reason: Reports no significant group effect or interaction for WAB AQ
    - source_id: P5-S2-C15
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Reports significant change on BNT and ANT but no group effects
    - source_id: P6-S1-C1
      disposition: represented
      result_indexes:
      - 1
      - 2
      reason: Provides p-values for BNT and ANT group effects
    - source_id: P6-S1-C4
      disposition: represented
      result_indexes:
      - 3
      reason: Reports individual WAB AQ gains for CILT participants
    - source_id: P6-S1-C5
      disposition: represented
      result_indexes:
      - 4
      reason: Reports individual BNT gains for CILT participants
    - source_id: P6-S1-C6
      disposition: represented
      result_indexes:
      - 5
      reason: Reports individual ANT gains for CILT participants
    - source_id: P6-S1-C7
      disposition: represented
      result_indexes:
      - 6
      reason: Reports individual WAB/BNT gains for a specific PACE participant
    - source_id: P6-S1-C8
      disposition: represented
      result_indexes:
      - 7
      reason: Reports individual ANT gain for a PACE participant
    - source_id: P6-S1-C9
      disposition: represented
      result_indexes:
      - 6
      - 7
      reason: Reports lack of continued gains for PACE participants at follow-up
    - source_id: P6-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Inter-judge reliability data
    - source_id: P6-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Intra-judge reliability data
    - source_id: P6-S1-C13
      disposition: represented
      result_indexes:
      - 9
      reason: Reports increase in words, utterances, and sentences for most participants
    - source_id: P6-S1-C14
      disposition: represented
      result_indexes:
      - 9
      reason: Reports decrease in output in some cases
    - source_id: P6-S1-C15
      disposition: represented
      result_indexes:
      - 8
      reason: Reports qualitative difference in narrative samples between groups
    - source_id: P6-S2-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Reports rater preference for CILT post-therapy and follow-up samples
    - source_id: P6-S2-C6
      disposition: represented
      result_indexes:
      - 8
      reason: Reports lower rater preference for PACE post-therapy samples
    - source_id: P7-S1-C1
      disposition: represented
      result_indexes:
      - 8
      reason: Reports maintenance of improvement for a PACE participant
    - source_id: P7-S1-C3
      disposition: represented
      result_indexes:
      - 8
      reason: Reports continued improvement for P5 in PACE group
    - source_id: P7-S1-C5
      disposition: represented
      result_indexes:
      - 8
      reason: Notes some subjects in both groups showed improvement
    - source_id: P7-S1-C8
      disposition: repeated
      result_indexes:
      - 0
      - 3
      - 4
      - 5
      - 8
      reason: Discussion restatement of consistent improvement in CILT
    - source_id: P7-S1-C9
      disposition: repeated
      result_indexes:
      - 0
      - 3
      - 4
      - 5
      - 8
      reason: Discussion restatement of substantial improvement in CILT
    - source_id: P7-S1-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Comparison to prior study (Pulvermüller et al., 2001)
    - source_id: P7-S1-C11
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      reason: Notes positive outcomes in the PACE group
    - source_id: P7-S1-C12
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      reason: Reports improvement for specific PACE participants
    - source_id: P7-S1-C13
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      reason: Concludes modified PACE had positive impact
    - source_id: P7-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Discussion of potential confounding factor (apraxia)
    - source_id: P7-S2-C5
      disposition: represented
      result_indexes:
      - 3
      - 4
      reason: Reports improvement in a CILT subject with severe apraxia
    - source_id: P8-S1-C9
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 5
      reason: Discussion restatement of continued impact of CILT
    - source_id: P8-S1-C10
      disposition: repeated
      result_indexes:
      - 3
      - 4
      - 5
      reason: Discussion restatement of maintained gains in CILT
    - source_id: P8-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on safety of the approach
    - source_id: P8-S2-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on completion of intervention
    - source_id: P8-S2-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on reasons for withdrawal
    - source_id: P8-S2-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on treatment schedule as a deterrent
    - source_id: P8-S2-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Statement on transportation and session length
    unresolved_coverage:
    - source_id: P7-S1-C13
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P8-S1-C11
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S1-C10
    - P2-S2-C7
    - P2-S2-C8
    - P2-S2-C9
    - P3-S3-C5
    - P3-S3-C6
    - P3-S3-C7
    - P3-S3-C8
    - P3-S3-C9
    - P3-S3-C12
    - P4-S2-C10
    - P4-S2-C11
    - P4-S2-C12
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C8
    - P5-S2-C9
    - P5-S2-C10
    - P5-S2-C12
    - P6-S1-C9
    - P6-S1-C11
    - P6-S1-C12
    - P7-S1-C1
    - P7-S1-C3
    - P7-S1-C5
    - P7-S1-C8
    - P7-S1-C9
    - P7-S1-C10
    - P7-S1-C11
    - P7-S1-C12
    - P7-S2-C3
    - P7-S2-C5
    - P8-S1-C9
    - P8-S1-C10
    - P8-S1-C11
    - P8-S2-C2
    - P8-S2-C3
    - P8-S2-C4
    - P8-S2-C5
    - P8-S2-C6
    pending_policy: Every result passage without direct candidate evidence remains pending, including model-labelled background and restatements; those labels never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-1-page-4-2
    - TABLE-2-page-5-3
    - TABLE-3-page-6-4
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P3-S3-C2
      recruited_sample:
      - P3-S2-C5
      eligibility:
      - P3-S2-C10
      imaging_provenance: []
      imaging_timing: []
      outcome_timing:
      - P2-S3-C9
      - P3-S1-C1
      - P5-S2-C10
      - P6-S1-C10
      outcome_definition:
      - P3-S1-C1
      - P3-S1-C7
      - P5-S2-C13
      - P6-S1-C13
      validation: []
      analysis_restrictions: []
      dependent_variable_statement: []
      limitations:
      - P6-S1-C2
      - P8-S2-C10
      - P8-S2-C11
      - P8-S2-C13
      - P8-S2-C14
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S3-C4
      - P3-S3-C5
      - P3-S3-C6
      - P3-S3-C7
      - P3-S3-C12
    outcome_type: both_reported
    imaging_vs_outcome: not_stated
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P5-S2-C13
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C13
      reason: Requires a Methods outcome definition; model selection retained for inspection only
    policy: All slots and enums remain unverified. Held selections are not evidence of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    profile: agent-repair
    scope: 'Agent corrected this draft against the original paper. The original automated attempt is retained as historical provenance and does not verify this revised version. Human PDF review and approval remain required. Nonrandomized repeated-measures pilot. CILT: 5 enrolled, 4 completed; PACE: 6 enrolled, 5 completed. Sample field now describes the relevant completers, with follow-up availability retained as a limitation.'
    binding:
      source_pdf_sha256: 5a0ee67e9b271d6aa0a9023fe42d054f07daf04814486e5fc9fe5c4566a04b8a
      original_source_sha256: 4310c3baf3531984c4e804a6cd20ce642c9b8be3e995519b024a7da9268a664d
      repair_audit: logs/publication/draft-repairs-2026-11-26.json
      agent_repair_approved: false
    approved: false
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations: []
    analysis_identity:
      id: R007
      exposure:
        text: PACE therapy
      outcome:
        text: WAB AQ and BNT
      analysis_label: Individual case analysis (PACE group)
      relation: association
      evidence_ids:
      - P6-S1-C7
      qualifier_ids:
      - P5-S3-C1
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 5a0ee67e9b271d6aa0a9023fe42d054f07daf04814486e5fc9fe5c4566a04b8a
        source_review: _compare/relationships-2026-11-16/review-current/Maher2006
        source_status_sha256: 525a65a1fa13c1156e036fb15945d18b1bf1df66d8948b333d35bfc5b54a131b
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings: {}
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
    publication_correction:
      date: '2026-11-26T00:24:06.569756+00:00'
      by: agent:source-repair
      approved: false
      human_verification_required: true
      original_source_sha256: 4310c3baf3531984c4e804a6cd20ce642c9b8be3e995519b024a7da9268a664d
      source_pdf_sha256: 5a0ee67e9b271d6aa0a9023fe42d054f07daf04814486e5fc9fe5c4566a04b8a
      pdf_pages:
      - 3
      - 7
      - 8
      note: 'Nonrandomized repeated-measures pilot. CILT: 5 enrolled, 4 completed; PACE: 6 enrolled, 5 completed. Sample field now describes the relevant completers, with follow-up availability retained as a limitation.'
      audit: logs/publication/draft-repairs-2026-11-26.json
    checked_by: agent:source-repair (human approval pending)
    date: '2026-11-26'
    corrections:
    - 'Nonrandomized repeated-measures pilot. CILT: 5 enrolled, 4 completed; PACE: 6 enrolled, 5 completed. Sample field now describes the relevant completers, with follow-up availability retained as a limitation.'
    original_scope: Independent model text review of core meaning; not human approval or complete PDF verification
    original_core_review:
      own_result_source_ids:
      - P6-S1-C7
      source_result: In the individual case analysis, only one PACE group member (P5, who used speech almost exclusively) showed the same amount of change on WAB AQ and BNT as the CILT group; no PACE participants showed continued gains at follow-up.
      result_status: detected
      patient_measurement: non_imaging
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the individual case analysis of the PACE group, which is distinct from the group-level ANOVA. The source explicitly separates these analyses (P6-S1-C4 vs P5-S2-C13).
          source_ids:
          - P6-S1-C4
          - P6-S1-C7
        direction:
          answer: fits
          reason: The claim accurately reflects the source finding that PACE therapy was associated with limited improvement (only one participant matching CILT gains) and no follow-up gains, contrasting with the CILT group. The direction 'unlikely' (implying less likely to produce the observed gains) is consistent with the source's description of PACE as the comparison group with fewer positive outcomes.
          source_ids:
          - P6-S1-C7
          - P6-S1-C9
        construct:
          answer: fits
          reason: The exposure is PACE therapy, and the outcomes are WAB AQ and BNT. The measurement is non-imaging (standard aphasia tests). The source confirms these measures were used for the PACE group.
          source_ids:
          - P3-S1-C1
          - P4-S1-C12
        qualifications:
          answer: fits
          reason: The draft includes the critical qualification that the one PACE participant who improved (P5) used speech exclusively, making their experience similar to CILT. It also notes the lack of follow-up gains. These are material qualifiers present in the source.
          source_ids:
          - P6-S1-C7
          - P7-S1-C2
        missing_material_caveat:
          answer: fits
          reason: The draft includes the key caveats regarding the non-randomized design, small sample size, and the specific behavior of P5. No material caveats that change the interpretation of the PACE result are omitted.
          source_ids:
          - P8-S2-C11
          - P7-S2-C3
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    original_profile: core
    original_binding:
      profile: core
      version: core-source-check-v3
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      checker_model: qwen3.8:27b
      checker_digest: 47951e4a666180bc2aedfc93c169472f2de783696fe196efbf063f5730ecf163
      host: http://localhost:11434
      pdf_sha256: 5a0ee67e9b271d6aa0a9023fe42d054f07daf04814486e5fc9fe5c4566a04b8a
      review_sha256: 28d0f5fe6a26db4ea8aeea874974a43abde08265d0d3d3aa189aa87137b9bf7d
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
reviewer_marks:
- id: relationship-source-check
  page: 6
  quote: 'In contrast, only one member of the PACE group evinced

    the same mount of change on the WAB and BNT, and this

    was the participant who selected the spoken modality almost

    exclusively in therapy.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor roles, all qualifiers, source audit issues and main-PDF tables/figures; check missing results. This model proposal is not verified.'
- id: publication-source-repair-2026-11-26
  status: pending
  by: agent:source-repair
  date: '2026-11-26'
  note: 'Nonrandomized repeated-measures pilot. CILT: 5 enrolled, 4 completed; PACE: 6 enrolled, 5 completed. Sample field now describes the relevant completers, with follow-up availability retained as a limitation. Original automated review applies to the original version; verify the corrected finding against the cited pages before approval.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
