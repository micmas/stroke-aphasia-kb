---
id: rh_slf3_rd
name: right hemisphere SLF III RD
kind: network
findings:
- id: f1
  target_audit:
    status: behaviour_label_present
    category: behaviour_or_language_construct
    original_target: language_performance
    reason: Label names a behaviour or language construct; its exact operational definition and measurement
      still need source review.
    audited_on: '2026-11-25'
    scope: Published metadata and linked excerpts; no new model pass or human approval
  outcome_measurement:
    status: needs_source_review
    instruments: []
    note: Outcome instrument/task is not yet verified for this finding. Do not infer it from the predictor
      or a paper-wide test list.
  target: language_performance
  target_kind: impairment
  claim: In the AG2 subgroup (patients with partial damage to left hemisphere language
    tracts), right hemisphere SLF III RD showed a marginally significant negative
    correlation with phonemic fluency, the Boston Naming Test (BNT), and the Comprehension
    of Instructions test in Greek (CIG).
  direction: likely
  relationship: correlational
  method: DTI
  sample:
    n: 17
    population: Right-handed, native Greek-speaking chronic aphasic patients after
      a single left hemisphere middle cerebral artery stroke, specifically those with
      partial damage to left hemisphere language tracts (AG2 subgroup).
    phase: not_reported
    time_post_onset: Chronic phase
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size (n=17 for the subgroup)
  - Marginal significance of the specific correlations for phonemic fluency, BNT,
    and CIG
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Radial diffusivity (RD) of the right hemisphere homolog
    of the Superior Longitudinal Fasciculus III, reconstructed using DTI with specific
    ROI protocols for the supramarginal gyrus and inferior frontal gyrus. Analysis
    performed specifically on the AG2 subgroup; Results for these specific targets
    were described as marginally significant; p-values were adjusted with FDR. Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P6-S2-C9, two-model agreement, human verification pending):
    Data Processing Analysis

    After the reconstruction of the LH white matter tracts, the experimental group
    was further divided into individuals with aphasia in whom there was an absence
    of reconstruction of the left hemisphere language pathways because of the extensive
    lesion [henceforth AG1 (Aphasia Group 1); n = 8] and individuals with aphasia
    in whom there was partial damage to the left hemisphere language pathways [henceforth
    AG2 (Aphasia Group 2); n = 17], as described later in this section Original text-layer
    quotation is preserved below. PDF image reading (P4-S3-C4, two-model agreement,
    human verification pending): MATERIALS AND METHODS


    Participants

    Twenty-five (25) right-handed, native, Greek-speaking patients with chronic aphasia
    after a single left hemisphere middle cerebral artery cerebrovascular accident
    (CVA) and absence of other neurological or psychiatric conditions were included
    in the experimental group Original text-layer quotation is preserved below.'
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
  citation: '@Kourtidou2021'
  source_passages:
  - section: Original source P10-S2-C7
    page: 10
    quote: 'A

      marginally significant negative correlation was also observed

      with (a) phonemic fluency (ρ = −0.593, padjusted = 0.051); (b)

      '
    supports: claim
  - section: Original source P10-S3-C2
    page: 10
    quote: 'A

      marginally significant negative correlation was also observed

      with (a) phonemic fluency (ρ = −0.593, padjusted = 0.051); (b)

      BNT (ρ = −0.555, padjusted = 0.051); and (c) CIG (ρ = −0.604,

      padjusted = 0.051).'
    supports: claim
  - section: Original source P4-S2-C7
    page: 4
    quote: 'For this purpose, the aphasic patients

      were divided into two subgroups according to whether there was

      complete (Aphasia Group 1: AG1) or partial (Aphasia Group

      2: AG2) damage to the language tracts of interest in the left

      hemisphere.'
    supports: sample
  - section: Original source P6-S2-C9
    page: 6
    quote: 'Data Processing Analysis

      After the reconstruction of the LH white matter tracts, the

      experimental group was further divided into individuals with

      aphasia in whom there was an absence of reconstruction

      of the left hemisphere language pathways because of the

      extensive lesion [henceforth AG1 (Aphasia Group 1); n = 8]

      and individuals with aphasia in whom there was partial

      damage to the left hemisphere language pathways [henceforth

      AG2 (Aphasia Group 2); n = 17], as described later in

      this section.'
    supports: sample
  - section: Original source P4-S3-C4
    page: 4
    quote: 'MATERIALS AND METHODS

      Participants

      Twenty-five (25) right-handed, native, Greek-speaking patients

      with chronic aphasia after a single left hemisphere middle

      cerebral artery cerebrovascular accident (CVA) and absence of

      other neurological or psychiatric conditions were included in the

      experimental group.'
    supports: sample
  - section: Original source P7-S2-C3
    page: 7
    quote: 'The Spearman

      Rho between the structure of the RH white matter tracts and

      language performance was also conducted for the AG2 subgroup.'
    supports: method
  - section: Original source P5-S1-C9
    page: 5
    quote: 'Additionally, the Greek version of the Boston Naming

      Test (BNT; Simos et al., 2010) and a receptive vocabulary

      test, the Greek version of the Peabody Picture Vocabulary

      Test-Revised (PPVT-R; Simos et al., 2010) were used, including

      the Controlled Oral Word Fluency (COWF) test (Kosmidis

      et al., 2004), a verbal fluency task standardized in Greek.'
    supports: method
  - section: Original source P5-S2-C5
    page: 5
    quote: 'Finally, the

      Comprehension of Instructions test in Greek (CIG; Simos

      et al., 2014), a verbal comprehension task standardized for the

      Greek population, was also included.'
    supports: method
  - section: Original source P5-S3-C4
    page: 5
    quote: 'The

      quantitative measures of the DTI variables calculated were mean

      fractional anisotropy (FA), axial diffusivity (AD), and radial

      diffusivity (RD).'
    supports: method
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-24'
relationship_review:
  paper: Kourtidou2021
  proposal_id: R008
  review_status_sha256: 6285d358177a37cbbe021f9d845b0e37763ecb52d5ad07058bf46b7668924bda
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: 03316aefb5179e5d630b2cbe493aa3d0fe140aebe1d37d15de673a91a566787e
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: 03316aefb5179e5d630b2cbe493aa3d0fe140aebe1d37d15de673a91a566787e
        A/passages.json: 576b3688b1d36566786de39218d4400e6b0e637df8b1957fb81184c3ff446aa8
        A/raw.json: 82216c9d2e7c5587f8f3381e4690d7d0fbb3b9e0df1a6c246cbda6b8929751cc
        A/source-units.json: 03189f683304f919928d409594b17ba7e265c29f2a33992a6e646b563f881f2c
        A/full-source-units.json: feba3c8e89468ce0b9fb879e7b4fbde3a31518e0b292063bd6edcfd13d8c602b
        A/meta.json: b318a1cdf463a5837fbdc651d9ae7ba1c12050f71ad7d974b36c6b553c6b1e36
        A/table-images/TABLE-3-page-10-2.png: 2ce445dde12d2faa2c306abc747758b09d23db98caa4e49305febddc36701cf8
        A/table-images/page-13.png: e62cf31f2ad00d40cdb1a7a32692a8d8baebea440e706762890261839bbdccdd
        A/table-images/page-12.png: c4bc67b562b171519ad2e7dc0ee24f3e077353935e37b132a87b2656818899d3
        A/table-images/page-10.png: 3e8bfa1fc840a38bf6c631164f6317f16113e55ccefe4ad34aa66551a8cc1ca8
        A/table-images/TABLE-4-page-12-1.png: bbbd9a87a15922e3a5e0e73df58bbaa8008f3fcee66207157c48e1bfc57796f3
        A/table-images/page-4.png: 55b2db1486ed8562cced0773711db768f3b1bde5843c3cd26d3901326aa3c31b
        A/table-images/TABLE-1-page-4-1.png: ddadc5f72bac38e74602849d2fae6bc017e018a4bd460d2e9fbaad00810beeaf
        A/table-images/TABLE-5-page-13-1.png: 1415653bf6fdce8704274092026117220a6af6f4eaeb882ebe35eaebb2d70553
        A/table-images/manifest.json: c509d56f46224ad87baeda04d4ac5c84ccd070170d2e7f7974bdb5d04a9af1cf
        A/table-images/TABLE-2-page-10-1.png: fd017677ba07300689581a4219e0b5a0ec334f0cf6e67503f6d8544ab577ae79
        A/clauses/window-11/raw.json: 14fba229486f3d470273bb5929788afc751b2005bff5c4d547bbc13ca5e0d7b6
        A/clauses/window-11/prompt.txt: a2a4e0e71a6641bfad8f7abf6c81c5073abde7f6767ca192e5d98d168e518c55
        A/clauses/window-11/meta.json: f0c25d35a56f8a13da0762cf5317dd78d14b9ca79acf242cbff4a221259dc1ad
        A/clauses/window-10/raw.json: a43e26cb8f5af4fff913d0b6019e3425870d0587b8274c413e7ec30b0f827f29
        A/clauses/window-10/prompt.txt: cd9a3948c70efab057ecb381a03859d3741728d28d7dfa2e30cd0d220fea8b91
        A/clauses/window-10/meta.json: 209c7f97be82c651dcb18d713d085ab9a6edecd63a7a11567c2c7ec5769cbabc
        A/clauses/window-03/raw.json: cf8122ed4b24049dec01516bb20746042452b19e4e3aa50445e92e43496f5532
        A/clauses/window-03/prompt.txt: 489526428106df2a1b6950d2df2eba98ca84b0a34aed517c7da31572d370aab8
        A/clauses/window-03/meta.json: ae260e2a0564488a79a69547868b4545c2a5638085e3bbc9a3b4a1e2ac51e882
        A/clauses/window-04/raw.json: da7e97a69f3b1f1f421b389ee008c2019c6924190c2693ddf657346377cc5ea0
        A/clauses/window-04/prompt.txt: 68c050026cdcfa599e745eb8be5a15743cf255a41d3b779c873070207b205ee2
        A/clauses/window-04/meta.json: 997fc64c535a3b1f66f179c9bb3991e26e923ed5b8c9ac28f456d5126f261f41
        A/clauses/window-05/raw.json: 380638601936bcd3a2433d65db76f2626bca48f6baa7631f69d59fb14b53c072
        A/clauses/window-05/prompt.txt: 619a483daea6f922df923a5ca6dd255b8f50b50246c1b57335564406a0e39ee9
        A/clauses/window-05/meta.json: 3f9982233f499f57773ff0719f0d25f011952528b9e967535fc09200ab6597f8
        A/clauses/window-02/raw.json: 48104993dd23aecd1e27807166a2f94590b3860c2b65f3449107627548d88f00
        A/clauses/window-02/prompt.txt: e7cdc03a7327ecd49e251c8bfebdfb01428d0fdc80116de3811655d410234d75
        A/clauses/window-02/meta.json: af398071d5ef7b843081ff0867ae61b407c5a7f69912555336828d920958c5b9
        A/clauses/window-09/raw.json: 5e13327638c9086d7fcfd9fb9949ddd7bfa7806ac62f151fa7f579d919a7adf6
        A/clauses/window-09/prompt.txt: 15bb7f93ee764cf60b7b32910780d3688e75db04e0b75709c599e271fdfb5cf1
        A/clauses/window-09/meta.json: 12e4902555f7c0ac1dc3c3c54bf9c52d044a5ea2d5193f0d0262c6e821c20a65
        A/clauses/window-07/raw.json: a56369110d4b01db7f13f9ef41c0e9f3540ace59c6551a14cd3cc2fa05168df3
        A/clauses/window-07/prompt.txt: 302cb1f4073168d8a59fb186572548ccbd0625fd4db9b0cad9659e097dee6144
        A/clauses/window-07/meta.json: 8cbe0f01c15c65e7d5b9745bdf7dce589486461555d5abc22fdb6633f8e88da2
        A/clauses/window-01/raw.json: 984045f3e6e25db3608d3e2d4239eae510ca13e5439ac29a70cb232e1804279b
        A/clauses/window-01/prompt.txt: 3408d732e2e5931f99e6a80661590d487c87b5ab0996fbcf42ac640c8d61fd94
        A/clauses/window-01/meta.json: 119411ec309d9e845ad46749b05fca64f8161d8dc36456a7d12d950555e1f56d
        A/clauses/window-06/raw.json: f632f01ed2ff70a6b1bb2a62876ae40a1b2a800b2554260c66542cfec4dd6437
        A/clauses/window-06/prompt.txt: a585970c00e063f1f1798e6c3b000763d7e54d2bd37a89f97c2844d6a6a2099d
        A/clauses/window-06/meta.json: 4980640d9d5297078e58b5dd9923d5718afed19a0bd57ed18485e18daa14af42
        A/clauses/window-08/raw.json: b872fbb61c264e0fd3cf6bcf6ad3a1be521b14ce0ebe3d7dc111e78b8850f7cb
        A/clauses/window-08/prompt.txt: 20026d72aa6c9cfb17504a4d1ff7201a9d50c1222d451bcc959e62d02f107824
        A/clauses/window-08/meta.json: 9a990b4f5540764187c1eb9ce35011d2ebd073e8a580912d04d11f7e4b216ba2
        A/tables/TABLE-4-page-12-4/raw.json: 56aa31c1b87e938af5e5a2c9a0f0b1f86d8c0b56693ed8d98b29977307819cc8
        A/tables/TABLE-4-page-12-4/prompt.txt: 90a7e57ae15828f5f8d9f95414e20b3e85de2a7b41349e8f7fdf8cb002003edf
        A/tables/TABLE-4-page-12-4/meta.json: c0441829357ff04cedd5e0434241b957874f3cadc961db96f6577856f788859e
        A/tables/TABLE-3-page-10-3/raw.json: 5700eb953da747718599065f15a5242cfa145b8ac09e58ef6206f19b4618f1ee
        A/tables/TABLE-3-page-10-3/prompt.txt: e0b65eb09959bd4cd6b56c4b9de6a4b3bb03592ae856a1c6df203ffd3f9eff22
        A/tables/TABLE-3-page-10-3/meta.json: a3c6155c34efdd9ca2e6ba39679ba1ad5d2774803f02401ab19e6796803d2548
        A/tables/TABLE-2-page-10-2/raw.json: 97b7a3b75d9ab85b84ed0d77e8d795faa2774f31bd6fe4300a645a600230b715
        A/tables/TABLE-2-page-10-2/prompt.txt: 506f02777f6431be25b65ad63a28abebdf46e7aa4bb42477f1fafbb8fb8faf46
        A/tables/TABLE-2-page-10-2/meta.json: 1ba2b93f73cf52dd7a927c519643facfac364af98c7b18b8670ff502d6147087
        A/tables/TABLE-1-page-4-1/raw.json: ffc57d09b78868c5912164663f3dafb6672fc0eec22e6756905af64af13db49c
        A/tables/TABLE-1-page-4-1/prompt.txt: 10c32bbc3ff768fdb31723fc476af2b81c3340b107d68ff86fd6956c1fc0eb2c
        A/tables/TABLE-1-page-4-1/meta.json: 3046d6778651e1e0ba0a35d03ab704c315ab433faccabc7df2baaaeb13e0d5d9
        A/tables/TABLE-5-page-13-5/raw.json: adfc8126140a47d7ab28e34b32bb581003fdd6cdee78147d449257e12d81f2c1
        A/tables/TABLE-5-page-13-5/prompt.txt: 5a21e197323c84fcff16d54e80747dadc0a5cb3b4e3e37a222db853b3a1e7e16
        A/tables/TABLE-5-page-13-5/meta.json: 455baa4ee039de193a1b65d53e81b264419de451ce480ab5598987504f5139c8
        B/passages.json: 576b3688b1d36566786de39218d4400e6b0e637df8b1957fb81184c3ff446aa8
        B/raw.json: a06243158d2de273949dc5ca2065adcd81c2e818489ed1bd423317a85b934e8b
        B/source-units.json: 03189f683304f919928d409594b17ba7e265c29f2a33992a6e646b563f881f2c
        B/full-source-units.json: feba3c8e89468ce0b9fb879e7b4fbde3a31518e0b292063bd6edcfd13d8c602b
        B/meta.json: fb4efceb1295b0d477882bec5b93911561feaa84e323ee446cd122036fc88272
        B/table-images/TABLE-3-page-10-2.png: 2ce445dde12d2faa2c306abc747758b09d23db98caa4e49305febddc36701cf8
        B/table-images/page-13.png: e62cf31f2ad00d40cdb1a7a32692a8d8baebea440e706762890261839bbdccdd
        B/table-images/page-12.png: c4bc67b562b171519ad2e7dc0ee24f3e077353935e37b132a87b2656818899d3
        B/table-images/page-10.png: 3e8bfa1fc840a38bf6c631164f6317f16113e55ccefe4ad34aa66551a8cc1ca8
        B/table-images/TABLE-4-page-12-1.png: bbbd9a87a15922e3a5e0e73df58bbaa8008f3fcee66207157c48e1bfc57796f3
        B/table-images/page-4.png: 55b2db1486ed8562cced0773711db768f3b1bde5843c3cd26d3901326aa3c31b
        B/table-images/TABLE-1-page-4-1.png: ddadc5f72bac38e74602849d2fae6bc017e018a4bd460d2e9fbaad00810beeaf
        B/table-images/TABLE-5-page-13-1.png: 1415653bf6fdce8704274092026117220a6af6f4eaeb882ebe35eaebb2d70553
        B/table-images/manifest.json: 46ce65a93099126fe9d557d65d0baa0000ca913cc78143116976c5b69ab2271f
        B/table-images/TABLE-2-page-10-1.png: fd017677ba07300689581a4219e0b5a0ec334f0cf6e67503f6d8544ab577ae79
        B/clauses/window-11/raw.json: fb1dd0c302591b15dbe6aabc1bcab5aff55d72b746d35d245ffaca143ea5d832
        B/clauses/window-11/prompt.txt: a2a4e0e71a6641bfad8f7abf6c81c5073abde7f6767ca192e5d98d168e518c55
        B/clauses/window-11/meta.json: 2fdbd04e3e9448afc5e128a58ed903e37be9eb5049aa61e9b12003372f63a199
        B/clauses/window-10/raw.json: d12ef2f4c97fdecf515cbc7d54ddb31bf9eeb8ea4ebf31f616a651d01a9733c8
        B/clauses/window-10/prompt.txt: cd9a3948c70efab057ecb381a03859d3741728d28d7dfa2e30cd0d220fea8b91
        B/clauses/window-10/meta.json: c30662d6f4d3e6926545639b31c1da5cb6b5d8b6458532e82839a6fa8d9fcd6b
        B/clauses/window-03/raw.json: 8184c9986ed0bdda325a72e8ff44e7d8448f974c9c1a13dd7b90aa5f8e3a1629
        B/clauses/window-03/prompt.txt: 489526428106df2a1b6950d2df2eba98ca84b0a34aed517c7da31572d370aab8
        B/clauses/window-03/meta.json: 604319c20518a7792265fb8b6b9ed74ca760821bce94b846e85b27a383a8235b
        B/clauses/window-04/raw.json: 7190cc68b19457d870387763dd2886dd629d5e235debdf1b40cd5ba08ca2a64a
        B/clauses/window-04/prompt.txt: 68c050026cdcfa599e745eb8be5a15743cf255a41d3b779c873070207b205ee2
        B/clauses/window-04/meta.json: 9b80654c8948b073fb62f35233ea1c9c0f3421cc1b4e7d9b1615dbe16059fd57
        B/clauses/window-05/raw.json: 82c0c4f47220d1376f915047661b6474cdabb4a0f49d33b766bfe0a9f2e300f4
        B/clauses/window-05/prompt.txt: 619a483daea6f922df923a5ca6dd255b8f50b50246c1b57335564406a0e39ee9
        B/clauses/window-05/meta.json: 0247d67e75d4dc5e48f0ed4b997eef0172f595c287842b3e54dbc5f12e341c02
        B/clauses/window-02/raw.json: 48104993dd23aecd1e27807166a2f94590b3860c2b65f3449107627548d88f00
        B/clauses/window-02/prompt.txt: e7cdc03a7327ecd49e251c8bfebdfb01428d0fdc80116de3811655d410234d75
        B/clauses/window-02/meta.json: e5002a6c4591d03f6dd14514e034468ff816ea1c309d021a8caee3315472ce6b
        B/clauses/window-09/raw.json: 3112393c2df79017167c652b0a949aa8591a7d714cb6f62d45aa0aa45956976b
        B/clauses/window-09/prompt.txt: 15bb7f93ee764cf60b7b32910780d3688e75db04e0b75709c599e271fdfb5cf1
        B/clauses/window-09/meta.json: 5012328185aa5ab3cd8c690302988020082528b748b894724da6f8ebb85a385b
        B/clauses/window-07/raw.json: c46f5f6b16fd810996860fb429d2243d4b68f1276d8ab1418eb751532d9fb0a6
        B/clauses/window-07/prompt.txt: 302cb1f4073168d8a59fb186572548ccbd0625fd4db9b0cad9659e097dee6144
        B/clauses/window-07/meta.json: 24db9d6dbe3d7d338537710ebb4fc3d2b3e04b7c85dbf01309680008c6401d0f
        B/clauses/window-01/raw.json: 7d65186c9c9f59cbee13f60a4662dc8b84dde9d1f544bad3bb792cad3d727e04
        B/clauses/window-01/prompt.txt: 3408d732e2e5931f99e6a80661590d487c87b5ab0996fbcf42ac640c8d61fd94
        B/clauses/window-01/meta.json: 9b665df517c6e4efeba23443111fd6c41679180028fff8cc1fcc016786b407a2
        B/clauses/window-06/raw.json: 4f027e98999d6d95d6545a8e4ae24baf8f14f19162e5f5a66d0b237b7fd745a0
        B/clauses/window-06/prompt.txt: a585970c00e063f1f1798e6c3b000763d7e54d2bd37a89f97c2844d6a6a2099d
        B/clauses/window-06/meta.json: 9471259a9353207db6591384c2cb6cf15ae0a91232f9e21998cda3df261296ce
        B/clauses/window-08/raw.json: a61fb17352084a2894205edbb5365f231e1beac6c6e714eacf8087bc8022c4df
        B/clauses/window-08/prompt.txt: 20026d72aa6c9cfb17504a4d1ff7201a9d50c1222d451bcc959e62d02f107824
        B/clauses/window-08/meta.json: 5505694d971caf026c57921e64062812241872fafbec9c140f94351ec9c64f71
        B/tables/TABLE-4-page-12-4/raw.json: 2a676d6a4aa23e7eee9800c06516fb21c8cf804b06ca91476783e313622b65a7
        B/tables/TABLE-4-page-12-4/prompt.txt: 90a7e57ae15828f5f8d9f95414e20b3e85de2a7b41349e8f7fdf8cb002003edf
        B/tables/TABLE-4-page-12-4/meta.json: 16fb09b3eaa403175ccb2acbff7867e7dfda372936b463fe4294fd4cb1242ef5
        B/tables/TABLE-3-page-10-3/raw.json: a0b7b1f83bd50213520ffdfcd09f97cb34aea0b436e708b232e96457998c1d56
        B/tables/TABLE-3-page-10-3/prompt.txt: e0b65eb09959bd4cd6b56c4b9de6a4b3bb03592ae856a1c6df203ffd3f9eff22
        B/tables/TABLE-3-page-10-3/meta.json: 56e80199a33dea22cb94f38807212b230ea9e9a67c47d707e6a0cc0655cf4310
        B/tables/TABLE-2-page-10-2/raw.json: a6a7ca67056dc90a155aeece8103b06be755ec878dc841dd84e89502fbe36ecf
        B/tables/TABLE-2-page-10-2/prompt.txt: 506f02777f6431be25b65ad63a28abebdf46e7aa4bb42477f1fafbb8fb8faf46
        B/tables/TABLE-2-page-10-2/meta.json: 4128bb8f2315ce7101c5c527ff9e5abb3553414ea9bdc584040e408decf12fad
        B/tables/TABLE-1-page-4-1/raw.json: e6d2edcad0196b072fde9653523fe16b1199a1456a265f9c4be9ac7f803acab4
        B/tables/TABLE-1-page-4-1/prompt.txt: 10c32bbc3ff768fdb31723fc476af2b81c3340b107d68ff86fd6956c1fc0eb2c
        B/tables/TABLE-1-page-4-1/meta.json: 155e52b4fbd3348bd98507803aae677c58fa6854d4cba38a7086213ddbc46f61
        B/tables/TABLE-5-page-13-5/raw.json: 066d3df8d58f619287d529ff2e7badd27429b94821b62ce0d551f0e77cd721b3
        B/tables/TABLE-5-page-13-5/prompt.txt: 5a21e197323c84fcff16d54e80747dadc0a5cb3b4e3e37a222db853b3a1e7e16
        B/tables/TABLE-5-page-13-5/meta.json: a47201c73a04edc61173d19e0332399394ec7fa642850627755b81b468f1b420
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
      pdf_sha256: 03316aefb5179e5d630b2cbe493aa3d0fe140aebe1d37d15de673a91a566787e
      source_review: _compare/relationships-2026-11-16/review-current/Kourtidou2021
      source_status_sha256: 82ec6c00da01a1a5aa34e6da43a1a79b7409d6073a33ddcfe58735b9e90135e8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R008
    exposure:
      text: right hemisphere SLF III RD
    outcome:
      text: phonemic fluency, BNT, and CIG
    analysis_label: Language performance correlation (AG2 subgroup)
    relation: association
    evidence_ids:
    - P10-S2-C7
    qualifier_ids:
    - P10-S2-C4
    context_ids: []
    table_ids: []
    approved: false
    status: requires_source_review
    flags:
    - new_model_candidate_not_verified
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 03316aefb5179e5d630b2cbe493aa3d0fe140aebe1d37d15de673a91a566787e
      source_review: _compare/relationships-2026-11-16/review-current/Kourtidou2021
      source_status_sha256: 82ec6c00da01a1a5aa34e6da43a1a79b7409d6073a33ddcfe58735b9e90135e8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P2-S1-C1
      - Result passage disposed without unit P8-S1-C3
      - Accounting without a linked unit P8-S1-C5
      - Unaccounted source passage P8-S1-C5
      - Result passage disposed without unit P10-S1-C5
      - Result passage disposed without unit P10-S1-C6
      - Accounting without a linked unit P10-S1-C8
      - Accounting without a linked unit P10-S2-C1
      - Result passage disposed without unit P10-S2-C4
      - Accounting without a linked unit P10-S2-C5
      - Result passage disposed without unit P9-S2-C2
      - Unaccounted source passage P10-S2-C5
      - Unaccounted source passage P10-S2-C1
      - Unaccounted source passage P10-S1-C8
      - Result passage disposed without unit P14-S2-C5
      - Result passage disposed without unit P14-S2-C7
      - 'window 7: invalid/duplicate disposition P15-S1-C5'
      - 'window 8: invalid/duplicate disposition P16-S2-C8'
      - Result passage disposed without unit P16-S2-C8
      - Result passage disposed without unit P16-S3-C2
      - Result passage disposed without unit P17-S1-C1
      unattached_null_or_qualifier_ids:
      - P2-S1-C1
      - P9-S2-C2
      - P17-S1-C1
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 255
      unselected_timing_passages:
      - P1-S1-C6
      - P1-S2-C1
      - P4-S3-C4
      - P4-S3-C8
      - P4-S3-C11
      - P4-S4-C1
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P1-S2-C7
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P7-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C1
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S2-C6
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P10-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S1-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S2-C3
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S3-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P15-S3-C4
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C2
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: dependent_variable_statement
        source_id: P16-S1-C10
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P7-S2-C6
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P7-S2-C8
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: analysis_restrictions
        source_ids:
        - P4-S2-C8
        - P5-S3-C10
        - P5-S3-C11
        - P5-S3-C12
        - P6-S1-C6
        - P6-S1-C7
        - P6-S1-C8
        - P6-S1-C9
        - P6-S2-C3
        - P6-S2-C4
        - P6-S2-C5
        reason: Runaway selection (>8 passages); entire slot requires source review
      empty_frame_slots_require_confirmation:
      - validation
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - adjustment_roles
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-4-1
      - TABLE-2-page-10-2
      - TABLE-3-page-10-3
      - TABLE-4-page-12-4
      - TABLE-5-page-13-5
      unlinked_tables:
      - TABLE-1-page-4-1
      - TABLE-3-page-10-3
      - TABLE-4-page-12-4
      - TABLE-5-page-13-5
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P5-S3
        - P5-S4
        - P6-S1
        - P10-S2
        - P11-S1
        - P15-S3
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: 03316aefb5179e5d630b2cbe493aa3d0fe140aebe1d37d15de673a91a566787e
      source_review: _compare/relationships-2026-11-16/review-current/Kourtidou2021
      source_status_sha256: 82ec6c00da01a1a5aa34e6da43a1a79b7409d6073a33ddcfe58735b9e90135e8
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S2-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: States increased axial diffusivity in RH tracts of aphasic patients.
    - source_id: P1-S2-C7
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: States correlations of language performance with RD in RH homologs for
        TFexcF, SLF III, and AF in limited damage subgroup.
    - source_id: P2-S1-C1
      disposition: represented
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: Specifies correlations with TFexcF in the extensive damage subgroup.
    - source_id: P8-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the composition of AG1 based on reconstruction failure.
    - source_id: P8-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes the composition of AG2 and FA reduction in some patients.
    - source_id: P8-S1-C6
      disposition: represented
      result_indexes:
      - 10
      reason: Reports significant difference in lesion volume between AG1 and AG2.
    - source_id: P9-S1-C5
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Reports significant differences in dorsal fasciculi and marginal difference
        in ventral TFexcF.
    - source_id: P9-S1-C6
      disposition: represented
      result_indexes:
      - 0
      - 1
      reason: Specifies significant differences in R AF AD, R SLF III AD, R SLF II
        AD, R SLF II RD, and marginal difference in R TFexcF AD.
    - source_id: P9-S1-C7
      disposition: represented
      result_indexes:
      - 0
      reason: Specifies that AD and R SLF II RD were higher for patients.
    - source_id: P9-S1-C8
      disposition: represented
      result_indexes:
      - 2
      reason: Reports no significant RD or FA differences for the listed tracts.
    - source_id: P9-S1-C9
      disposition: represented
      result_indexes:
      - 3
      reason: Reports no significant differences in R UF FA, AD, and RD.
    - source_id: P9-S2-C1
      disposition: repeated
      result_indexes:
      - 3
      reason: Restatement of R UF results.
    - source_id: P9-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: States no significant differences between aphasia subgroups.
    - source_id: P10-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      reason: Confirms t-test results via non-parametric analysis.
    - source_id: P10-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Summary statement about group comparability.
    - source_id: P10-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Table 5.
    - source_id: P10-S1-C8
      disposition: represented
      result_indexes:
      - 4
      reason: Reports negative relationship between RH TFexcF RD and reading/speech
        rate in AG1.
    - source_id: P10-S2-C1
      disposition: repeated
      result_indexes:
      - 4
      reason: Qualifies the AG1 subgroup as having extensive lesions.
    - source_id: P10-S2-C4
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: Introduces correlations for the AG2 subgroup.
    - source_id: P10-S2-C5
      disposition: represented
      result_indexes:
      - 5
      reason: Reports negative correlation between RH TFexcF RD and comprehension/repetition
        in AG2.
    - source_id: P10-S2-C6
      disposition: represented
      result_indexes:
      - 6
      reason: Reports negative correlation between RH SLF III RD and repetition/PPVT-R
        in AG2.
    - source_id: P10-S2-C7
      disposition: represented
      result_indexes:
      - 7
      reason: Reports marginal negative correlation between RH SLF III RD and fluency/naming/CIG
        in AG2.
    - source_id: P10-S3-C1
      disposition: repeated
      result_indexes:
      - 6
      reason: Restatement of SLF III RD correlation.
    - source_id: P10-S3-C2
      disposition: repeated
      result_indexes:
      - 7
      reason: Restatement of SLF III RD marginal correlations.
    - source_id: P10-S3-C3
      disposition: represented
      result_indexes:
      - 8
      - 9
      reason: Reports correlations for RH SLF III FA and RH AF RD in AG2.
    - source_id: P10-S3-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Footer text.
    - source_id: P11-S1-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reference to Supplementary Table 1.
    - source_id: P13-S1-C4
      disposition: represented
      result_indexes:
      - 10
      reason: Reports significant differences in repetition, reading, and speech rate
        between AG1 and AG2.
    - source_id: P13-S2-C1
      disposition: repeated
      result_indexes:
      - 10
      reason: Restatement of AG2 superiority in specific tasks.
    - source_id: P14-S1-C5
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      reason: Discussion restatement of structural differences in RH tracts.
    - source_id: P14-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Cites prior study (Kraus et al., 2007).
    - source_id: P14-S2-C5
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: Discussion restatement that RD measures correlated with performance.
    - source_id: P14-S2-C6
      disposition: repeated
      result_indexes:
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: Discussion restatement of negative correlations between RD and performance.
    - source_id: P14-S3-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Cites prior study (Schlaug et al., 2009; Zipse et al., 2012).
    - source_id: P15-S1-C4
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of reading comprehension and RH TFexcF RD relationship
        in AG1.
    - source_id: P15-S2-C3
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of speech fluency and RH TFexcF RD relationship
        in AG1.
    - source_id: P15-S3-C2
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: Discussion restatement of RD correlations in AG2.
    - source_id: P15-S3-C4
      disposition: repeated
      result_indexes:
      - 5
      reason: Discussion restatement of TFexcF RD correlation with PPVT-R, CIG, and
        simple command comprehension.
    - source_id: P15-S4-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Cites prior study (Kuperberg et al., 2000).
    - source_id: P15-S4-C2
      disposition: repeated
      result_indexes:
      - 6
      - 7
      reason: Discussion restatement of CIG correlation with TFexcF and SLF III.
    - source_id: P16-S1-C2
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: Discussion restatement of repetition correlations with RD of AF, SLF
        III, and TFexcF.
    - source_id: P16-S2-C1
      disposition: repeated
      result_indexes:
      - 7
      reason: Discussion restatement of marginal correlation between SLF III RD and
        BNT.
    - source_id: P16-S3-C2
      disposition: repeated
      result_indexes:
      - 0
      - 1
      - 2
      reason: Discussion restatement of increased AD in RH homologs.
    - source_id: P16-S4-C1
      disposition: repeated
      result_indexes:
      - 4
      - 5
      reason: Discussion restatement of different association patterns between subgroups.
    - source_id: P16-S4-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes performance differences between AG1 and AG2.
    - source_id: P17-S1-C1
      disposition: repeated
      result_indexes:
      - 4
      reason: Discussion restatement of TFexcF and speech narration in AG1.
    - source_id: P17-S1-C2
      disposition: repeated
      result_indexes:
      - 5
      - 6
      - 7
      - 8
      - 9
      reason: Discussion restatement of TFexcF, SLF III, and AF correlations in AG2.
    - source_id: P17-S2-C1
      disposition: background_or_descriptive
      result_indexes: []
      reason: Author contribution statement.
    - source_id: P17-S2-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Author contribution statement.
    unresolved_coverage:
    - source_id: P10-S2-C7
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P10-S3-C4
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P13-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P14-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P14-S3-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P15-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P16-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P16-S4-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P17-S2-C1
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P17-S2-C2
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P14-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S1-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C7
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S2-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C6
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C8
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C9
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S3-C10
      disposition: unresolved
      reason: Discovery omitted this passage
    - source_id: P16-S4-C5
      disposition: unresolved
      reason: Discovery omitted this passage
    pending_source_ids:
    - P1-S2-C5
    - P1-S2-C7
    - P2-S1-C1
    - P8-S1-C3
    - P8-S1-C5
    - P8-S1-C6
    - P9-S2-C1
    - P9-S2-C2
    - P10-S1-C5
    - P10-S1-C6
    - P10-S1-C7
    - P10-S2-C1
    - P10-S2-C4
    - P10-S3-C2
    - P11-S1-C9
    - P14-S1-C5
    - P14-S2-C5
    - P14-S2-C6
    - P14-S2-C7
    - P15-S1-C4
    - P15-S2-C3
    - P15-S3-C2
    - P15-S3-C4
    - P15-S4-C2
    - P16-S1-C2
    - P16-S1-C10
    - P16-S2-C7
    - P16-S2-C8
    - P16-S2-C10
    - P16-S3-C2
    - P16-S3-C6
    - P16-S3-C8
    - P16-S3-C9
    - P16-S3-C10
    - P16-S4-C2
    - P16-S4-C5
    - P17-S1-C1
    - P17-S1-C2
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-4-1
    - TABLE-2-page-10-2
    - TABLE-3-page-10-3
    - TABLE-4-page-12-4
    - TABLE-5-page-13-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P1-S2-C1
      - P4-S3-C5
      recruited_sample:
      - P1-S2-C1
      - P4-S3-C5
      eligibility:
      - P4-S3-C4
      imaging_provenance:
      - P5-S2-C12
      imaging_timing:
      - P1-S2-C3
      outcome_timing:
      - P1-S2-C3
      outcome_definition:
      - P1-S2-C4
      - P5-S1-C3
      - P5-S1-C4
      - P5-S1-C9
      - P5-S2-C5
      validation: []
      analysis_restrictions: []
      dependent_variable_statement:
      - P4-S3-C1
      - P7-S1-C4
      - P7-S1-C5
      - P7-S1-C7
      limitations:
      - P14-S2-C3
      - P16-S3-C4
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles: []
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S3-C4
      - P4-S3-C5
      - P4-S3-C11
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P1-S2-C7
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C1
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S2-C6
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P10-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S1-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S2-C3
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S3-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P15-S3-C4
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C2
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P16-S1-C10
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P7-S2-C6
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P7-S2-C8
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: analysis_restrictions
      source_ids:
      - P4-S2-C8
      - P5-S3-C10
      - P5-S3-C11
      - P5-S3-C12
      - P6-S1-C6
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C9
      - P6-S2-C3
      - P6-S2-C4
      - P6-S2-C5
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
      pdf_sha256: 03316aefb5179e5d630b2cbe493aa3d0fe140aebe1d37d15de673a91a566787e
      review_sha256: 6285d358177a37cbbe021f9d845b0e37763ecb52d5ad07058bf46b7668924bda
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
      source_result: In the AG2 subgroup, right hemisphere SLF III RD showed a marginally
        significant negative correlation with phonemic fluency, BNT, and CIG (p_adjusted
        = 0.051 for all three).
      result_status: detected_only_at_relaxed_threshold
      patient_measurement: patient_diffusion
      checks:
        analysis_identity:
          answer: fits
          reason: The source P10-S2-C7 and P10-S3-C2 explicitly describe the correlation
            of RH SLF III RD with phonemic fluency, BNT, and CIG in the AG2 subgroup.
            The proposed core correctly identifies this specific analysis.
          source_ids:
          - P10-S2-C7
          - P10-S3-C2
          - P7-S2-C3
        direction:
          answer: fits
          reason: The source states a 'negative correlation' (rho values are negative).
            The proposed core uses 'likely' direction, which is a valid qualitative
            representation of a detected negative association, especially given the
            marginal significance.
          source_ids:
          - P10-S2-C7
          - P10-S3-C2
        construct:
          answer: fits
          reason: The exposure is correctly identified as RH SLF III RD. The outcomes
            are correctly identified as phonemic fluency, BNT, and CIG. The population
            is correctly identified as the AG2 subgroup (partial LH damage). The method
            is DTI.
          source_ids:
          - P10-S2-C7
          - P10-S3-C2
          - P4-S2-C7
          - P6-S2-C9
        qualifications:
          answer: fits
          reason: The core correctly includes the qualification that the analysis
            is specific to the AG2 subgroup and that the results are 'marginally significant'
            (p=0.051). It also notes FDR adjustment. These are material qualifiers
            present in the source.
          source_ids:
          - P10-S2-C7
          - P10-S3-C2
          - P7-S2-C4
        missing_material_caveat:
          answer: fits
          reason: 'The core captures the key caveats: subgroup specificity (AG2),
            marginal significance, and small sample size (n=17). No other material
            caveats from the source passages appear to be omitted that would change
            the interpretation of this specific correlation.'
          source_ids:
          - P10-S2-C7
          - P10-S3-C2
          - P6-S2-C9
      optional_pending: []
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R008
      exposure:
        text: right hemisphere SLF III RD
      outcome:
        text: phonemic fluency, BNT, and CIG
      analysis_label: Language performance correlation (AG2 subgroup)
      relation: association
      evidence_ids:
      - P10-S2-C7
      qualifier_ids:
      - P10-S2-C4
      context_ids: []
      table_ids: []
      approved: false
      status: requires_source_review
      flags:
      - new_model_candidate_not_verified
      candidate_discovery:
        model: gemma4:31b
        model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
        pdf_sha256: 03316aefb5179e5d630b2cbe493aa3d0fe140aebe1d37d15de673a91a566787e
        source_review: _compare/relationships-2026-11-16/review-current/Kourtidou2021
        source_status_sha256: 82ec6c00da01a1a5aa34e6da43a1a79b7409d6073a33ddcfe58735b9e90135e8
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P6-S2-C9:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 03316aefb5179e5d630b2cbe493aa3d0fe140aebe1d37d15de673a91a566787e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: f0512f053316f3196b7f4dfd99ba9c8868d3828e28e1b9462f49266403894733
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P6-S2-C9
          page: 6
          text_layer_sha256: f0512f053316f3196b7f4dfd99ba9c8868d3828e28e1b9462f49266403894733
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'Data Processing Analysis

          After the reconstruction of the LH white matter tracts, the

          experimental group was further divided into individuals with

          aphasia in whom there was an absence of reconstruction

          of the left hemisphere language pathways because of the

          extensive lesion [henceforth AG1 (Aphasia Group 1); n = 8]

          and individuals with aphasia in whom there was partial

          damage to the left hemisphere language pathways [henceforth

          AG2 (Aphasia Group 2); n = 17], as described later in

          this section.'
        anchor_text: 'Data Processing Analysis

          After the reconstruction of the LH white matter tracts, the

          experimental group was further divided into individuals with

          aphasia in whom there was an absence of reconstruction

          of the left hemisphere language pathways because of the

          extensive lesion [henceforth AG1 (Aphasia Group 1); n = 8]

          and individuals with aphasia in whom there was partial

          damage to the left hemisphere language pathways [henceforth

          AG2 (Aphasia Group 2); n = 17], as described later in

          this section.'
        excluded_fragments: []
        image_sha256: 7467ff8e82a76e7c4b3560dd0ff46b3bdd8feb466cc3d70dff97122f70412201
        transcription: 'Data Processing Analysis

          After the reconstruction of the LH white matter tracts, the experimental
          group was further divided into individuals with aphasia in whom there was
          an absence of reconstruction of the left hemisphere language pathways because
          of the extensive lesion [henceforth AG1 (Aphasia Group 1); n = 8] and individuals
          with aphasia in whom there was partial damage to the left hemisphere language
          pathways [henceforth AG2 (Aphasia Group 2); n = 17], as described later
          in this section'
      P4-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: 03316aefb5179e5d630b2cbe493aa3d0fe140aebe1d37d15de673a91a566787e
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 8ae1692aa443a0d7f1b7822e902017c8d90f463509a7fa6a119febba1346e664
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P4-S3-C4
          page: 4
          text_layer_sha256: 8ae1692aa443a0d7f1b7822e902017c8d90f463509a7fa6a119febba1346e664
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: 'MATERIALS AND METHODS

          Participants

          Twenty-five (25) right-handed, native, Greek-speaking patients

          with chronic aphasia after a single left hemisphere middle

          cerebral artery cerebrovascular accident (CVA) and absence of

          other neurological or psychiatric conditions were included in the

          experimental group.'
        anchor_text: 'MATERIALS AND METHODS

          Participants

          Twenty-five (25) right-handed, native, Greek-speaking patients

          with chronic aphasia after a single left hemisphere middle

          cerebral artery cerebrovascular accident (CVA) and absence of

          other neurological or psychiatric conditions were included in the

          experimental group.'
        excluded_fragments: []
        image_sha256: 741b5539fa17c6596e47a50ba644efa337c679ef3de538eec5bc2e07b1eeeddf
        transcription: 'MATERIALS AND METHODS


          Participants

          Twenty-five (25) right-handed, native, Greek-speaking patients with chronic
          aphasia after a single left hemisphere middle cerebral artery cerebrovascular
          accident (CVA) and absence of other neurological or psychiatric conditions
          were included in the experimental group'
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 10
  quote: 'A

    marginally significant negative correlation was also observed

    with (a) phonemic fluency (ρ = −0.593, padjusted = 0.051); (b)

    '
  status: pending
  by: agent:relationship-converter
  date: '2026-11-24'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
