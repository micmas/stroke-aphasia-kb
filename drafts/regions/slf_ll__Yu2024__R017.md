---
id: slf_ll
name: SLF lesion load
kind: tract
findings:
- id: f1
  target: aphasia_severity
  target_kind: impairment
  claim: The lesion load of the superior longitudinal fasciculus (SLF-LL) demonstrated
    good predictive performance for aphasia severity.
  direction: likely
  relationship: correlational
  method: LSM
  sample:
    n: 46
    population: Right-handed Chinese speakers with first-ever left hemispheric stroke
      and post-stroke aphasia
    phase: not_reported
    time_post_onset: Subacute phase (median time post-stroke 23.50 days, range 5-89
      days)
  statistics:
    threshold: not_transcribed
  confounders_controlled: []
  confounders_not_controlled: []
  region_definition:
    kind: not_reported
    description: Not transcribed; see source passages and claim.
  author_limitations:
  - Small sample size
  - Majority of participants were male (76.09%)
  - Majority of stroke types were infarction (67.39%)
  - Analysis based on lesion load without DTI data evaluating structural connectivity
  evidence_quality: cohort
  strength: weak
  notes: 'Exposure measurement: Patient lesion overlap with a population reference
    tract template for the superior longitudinal fasciculus (SLF), calculated as the
    proportion of the critical region involved by the lesion (lesion load = volume
    of overlap / total volume of critical region * 100%). Aphasia severity was classified
    into two levels: mild/moderate (AQ >= 51) and severe/very severe (AQ < 51). Additional
    metadata has not been transcribed; review the pending-field flags before approval.
    PDF image reading (P2-S3-C4, two-model agreement, human verification pending):
    Subjects


    Data on forty-six right-handed patients [31 cases of ischemic stroke and 15 cases
    of hemorrhagic stroke; 35 males and 11 females; mean age (standard deviation,
    SD), 56.09 (12.46) years, range, 25–78 years; the median (interquartile range,
    IQR) duration of education, 10.50 (3) years, range, 6–16 years; the median (IQR)
    time post-stroke (TPO), 23.50 (41) days, range, 5–89 days] with PSA admitted to
    the rehabilitation department of our hospital between March 2020 and May 2022
    were analyzed Original text-layer quotation is preserved below. PDF image reading
    (P9-S2-C7, two-model agreement, human verification pending): . Second, the majority
    of the participants (76.09 %) were males, and the majority of stroke type was
    infarction (67.39 %) Original text-layer quotation is preserved below.'
  imaging_details:
    reference_space: not_reported
    atlases_used: []
  lesion_mapping: {}
  provenance:
    extracted_by: model:gemma4:31b
    extracted_on: '2026-11-26'
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
    - proposed_concept:aphasia_severity
  citation: '@Yu2024'
  source_passages:
  - section: Original source P1-S1-C10
    page: 1
    quote: "The ROC curve analyses yielded the validated area under the curve (AUC)\
      \ 0.84 both for \nAreas-LL and SLF-LL and 0.76 for IFOF-LL, indicating good\
      \ predictive performance (p < 0.01)."
    supports: claim
  - section: Original source P2-S3-C4
    page: 2
    quote: "Subjects\nData on forty-six right-handed patients [31 cases of ischemic\
      \ stroke \nand 15 cases of hemorrhagic stroke; 35 males and 11 females; mean\
      \ age \n(standard deviation, SD), 56.09 (12.46) years, range, 25–78 years; the\
      \ \nmedian (interquartile range, IQR) duration of education, 10.50 (3) \nyears,\
      \ range, 6–16 years; the median (IQR) time post-stroke (TPO), \n23.50 (41) days,\
      \ range, 5–89 days] with PSA admitted to the rehabili­\ntation department of\
      \ our hospital between March 2020 and May 2022 \nwere analyzed."
    supports: sample
  - section: Original source P3-S1-C4
    page: 3
    quote: "Several critical sub-cortical language-related neural tracts were \nextracted\
      \ from the Johns Hopkins University (JHU) White Matter \nTractography Atlas\
      \ (JHU-ICBM-tracts-prob-thr25–2 mm) provided by \nthe FSL software package,\
      \ including the left SLF (X=129, Y=112, \nZ=102), IFOF (X=118, Y=54, Z=70),\
      \ ILF (X=120, Y=57, Z=69), and UF \n(X=129, Y=125, Z=52) (Hillis et al., 2018;\
      \ Meier et al., 2019; Wakana \net al., 2004)."
    supports: method
  - section: Original source P3-S2-C2
    page: 3
    quote: "To evaluate the degree of damage to the critical cortical language- \n\
      related areas and sub-cortical white matter tracts, an index “lesion \nload”\
      \ (i.e., the proportion of the critical region involved by the lesion) \nwas\
      \ calculated for every participant according to a formula: lesion load \n= (the\
      \ volume of the overlap/the total volume of the critical regions) ×\n100 % (Benghanem\
      \ et al., 2019; Ivanova et al., 2021; Yu et al., 2022; \nWan et al., 2014)."
    supports: method
  - section: Original source P2-S4-C4
    page: 2
    quote: "However, the \naphasia severity was classified into two levels: mild/moderate\
      \ (AQ ≥\n51) and severe/very severe (AQ < 51) in this study (Lee et al., 2021).\n\
      2.3."
    supports: claim
  - section: Original source P6-S1-C8
    page: 6
    quote: "Therefore, we herein investigated the clinical application value of \n\
      combining structural T1WI with standard brain atlas in predicting the \nseverity\
      \ of subacute PSA."
    supports: claim
  - section: Original source P9-S2-C6
    page: 9
    quote: "First, the sample was \nrelatively small, which limits the generalizability\
      \ of the results."
    supports: limitation
  - section: Original source P9-S2-C7
    page: 9
    quote: "Second, \nthe majority of the participants (76.09 %) were males, and the\
      \ majority \nof stroke type was infarction (67.39 %)."
    supports: limitation
  - section: Original source P9-S2-C10
    page: 9
    quote: "Importantly, we did not provide DTI data evaluating the critical neural\
      \ \ntracts."
    supports: limitation
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-26'
relationship_review:
  paper: Yu2024
  proposal_id: R017
  review_status_sha256: dc2dd885c2965b804d6a334deccb81ebd5958160acb1dc1053ca82b0f859235d
  review_binding:
    version: candidate-inventory-v1
    input_hashes:
      pdf: f71dc47ac2f8923ba9109c78bc40bca67bb33825fb0e5bae629800c0a31eea38
    original_review_binding:
      version: relationship-review-v4
      input_hashes:
        pdf: f71dc47ac2f8923ba9109c78bc40bca67bb33825fb0e5bae629800c0a31eea38
        A/passages.json: 11bcbfef080ee09461ad87f4dbbaf615569a2eb3f8fcd940bf9fe43bdb94926c
        A/raw.json: 8041cff5af928d7718f8a847cd4d51986a837b45a97628f2c3baae98110837e7
        A/source-units.json: 3848716f43cd7af915583d627d530bb42b9b53cb6e732b3b17ba375196010cb5
        A/full-source-units.json: 348c869c36d42ce8d44fb5f1b818503275ccec8eb6d382a17cd2ba113ac3570b
        A/meta.json: bd093056ef9518e4b983795373a1ad6f5df2cd5e67e240b37a2841aa6558e3e8
        A/table-images/TABLE-1-page-3-1.png: 9dd0c6676501c696be6b037bffb8862401cfdc10a1503e016d11d80964ade6af
        A/table-images/TABLE-1-page-5-1.png: c5a5ca7d991251b5496ee2835c90437cbf4a3dd31d357e97483c99ba47fbdcb1
        A/table-images/page-3.png: cb661c6ad3924b6f29b836f7a421df35a5bbd75c3ac9002a40b24738c9307483
        A/table-images/TABLE-3-page-8-1.png: f6f7ed02ec42f51f544ef548a22a23c8fcd1dd3026a940471ba9c2ece3c2651c
        A/table-images/page-7.png: 6a29cc1e1e4eb143968af9b7daa12c86ccf9ec58b151bb1f9831fc73f38f88d8
        A/table-images/page-5.png: b0adc930d5754b5f61956abe253d86c6b680c7900cde8af4b8b90af283069c55
        A/table-images/TABLE-4-page-8-2.png: 68d30213c821be94b8fccba37765cd28e0318464177f1538117eebeebf594bed
        A/table-images/page-8.png: 8491214f0dacab1c1b2ebc4ba82f27bce2437db6e10ae61bebfdb0756973b234
        A/table-images/manifest.json: cf65b195798c75048c587a44325d90b48c5b9c7633f4d9f8bc5d548f2505562f
        A/table-images/TABLE-2-page-7-1.png: 8fefc96726c0a265e26188d161deb5afa9252d24b81942d4eea1cb1aff74229f
        A/clauses/window-03/raw.json: 0b759daf48df930f88ce76c5bea5ea47d71d19c94cbdaada35ae69c54947ed06
        A/clauses/window-03/prompt.txt: c35a18e81cec33a1924c3fe4ccd63bafc8d68b9fd346f13d8334578fdd17900e
        A/clauses/window-03/meta.json: d4785d16eddb07a2dfda0e951ad171c3404558a6e5a7313a068344291959cf51
        A/clauses/window-04/raw.json: cfb76e2c9211a350039529d3bcae78cf846ebd2a9e466fb4c79de2c6fab09a14
        A/clauses/window-04/prompt.txt: aa642666bd8ff9c0867dcbbfbe06af70b322fd31bc410095ff28bd8d04d366c6
        A/clauses/window-04/meta.json: 3300869a352c9716faa90496b706b67c5396f1f45bf814f1a6e6c5390fbc45f7
        A/clauses/window-05/raw.json: d5860805fc72aa818710f1abc19019f76a64152c00c3e2e06a455b6a50c09975
        A/clauses/window-05/prompt.txt: 43a107ce00402016753deee388153b8cf1a21bcdc45eebc279273a2d662f469b
        A/clauses/window-05/meta.json: 2ef9ed18b2f83e3300f4a82e4e8dd0f17cb097dacf15d5b297c4392de8e39921
        A/clauses/window-02/raw.json: 4dff78cc43cbe66bf053edefb9e1bbdcc3c0fb045955ff87fee02837fe600dfb
        A/clauses/window-02/prompt.txt: a5ec62be575a0a46c3514234fb18621a8bd74a2ae6a0588084e60ad1b0ab829f
        A/clauses/window-02/meta.json: e01e1bacfa140ae7821aebc6fb4ea6b6c47575152615e3e4cd86bb048abbd94a
        A/clauses/window-07/raw.json: 48ace834547bb0db6117980cd03e50e7d790b4d9e852eb26c89277a981533553
        A/clauses/window-07/prompt.txt: 1908cb388887975d2d9805552b9fee2c297e53e1205ce82331f92c5eb9a6e569
        A/clauses/window-07/meta.json: d2366eec8c82ed9ed03c1a85a2f91c55043a7e10738138adb3fb274d83a06457
        A/clauses/window-01/raw.json: 12e53986f5c438e5ef36240ed6478baf9bb983d523989d1add5adca62ac1a62f
        A/clauses/window-01/prompt.txt: dadc74d5761cb6b15437d43ad02dbaa6f229d4d651c37f632f53e3c596cdb70a
        A/clauses/window-01/meta.json: da47a6a4efe84908fa716e675279400d5cb594372efe3433c71813b227ebb534
        A/clauses/window-06/raw.json: e7fa4429ff14697fdba40aa0b525a6f92d8dd9841c62036b077c1466b4b76334
        A/clauses/window-06/prompt.txt: fc6f6f02ffadbcf8fc2e99448fc47c3e5edb410d08ce7c7bbd12c2d7ed370d79
        A/clauses/window-06/meta.json: 12cda0536cb4a63524b558834a33680c4331ba70047d4a009462a3d35243e7ab
        A/tables/TABLE-4-page-8-5/raw.json: 7ef7c5e36debf1c4f12d6838eda90049a6269da5de1bf31102ca66268dc77280
        A/tables/TABLE-4-page-8-5/prompt.txt: 6754e73c5d195ea45678b2b4db2198f1324cd6ff0b6041d12c41ed83cd52ac2c
        A/tables/TABLE-4-page-8-5/meta.json: 020a7e214dd6dc1db7f81438175f941181f8c37d656dd9ea810dcd610e66e4e8
        A/tables/TABLE-3-page-8-4/raw.json: df3f534e974e56ac4131d449e368f282a9991d3fbbf0efdb365496f42debac68
        A/tables/TABLE-3-page-8-4/prompt.txt: f77364d75b8913a004629d12c6fc3bdcc7f79cb7a74728f664dc66a4433e70c7
        A/tables/TABLE-3-page-8-4/meta.json: cfb5d70db51af4a736f05e1db6abf7eb1ce21dad7a86249ae5f5c2357275eb87
        A/tables/TABLE-1-page-5-2/raw.json: 2b733aa0cc46d3bd812ed1633ecd3aa6bc652f89cb6fb37388a4c47b98238dea
        A/tables/TABLE-1-page-5-2/prompt.txt: adf9dad96a41c4a0f54eed728ac807bb2390ef6bcf420f3a9854758cff410881
        A/tables/TABLE-1-page-5-2/meta.json: 27929aa76be5a01ff67da711c000aa0353f8d282f042c58e5c22ac16a609f42b
        A/tables/TABLE-1-page-3-1/raw.json: 34b893c2b817a38554b07def1b978ed10f5a5707067c4fe962983d29edf5893a
        A/tables/TABLE-1-page-3-1/prompt.txt: fe377e80c2ab8609c47b8cf068e1cedea81994cd3b7617244d2d9013a58b19ff
        A/tables/TABLE-1-page-3-1/meta.json: 478124df32ce1d33ee062252801cfc934f6a275abfc371c15ec4eac13da6c4bf
        A/tables/TABLE-2-page-7-3/raw.json: 92da99f7774489b756ba610764de7092a750a4e26503dc62590ccb6e2d929a12
        A/tables/TABLE-2-page-7-3/prompt.txt: ef10a17e95d058821fe3420840d973e814be26720173889fd61f07cc908c27fc
        A/tables/TABLE-2-page-7-3/meta.json: c0e60d8f5ad9baac8a0e8a3e28c38db94b2cc6a8821c57b1be575d704e33c5a3
        B/passages.json: 11bcbfef080ee09461ad87f4dbbaf615569a2eb3f8fcd940bf9fe43bdb94926c
        B/raw.json: 1d1010b7b46a6129c4c6b5769bc363e14d842cb60855501e04e4955179dfef8b
        B/source-units.json: 3848716f43cd7af915583d627d530bb42b9b53cb6e732b3b17ba375196010cb5
        B/full-source-units.json: 348c869c36d42ce8d44fb5f1b818503275ccec8eb6d382a17cd2ba113ac3570b
        B/meta.json: 59674da3c89348b7181cc4e424c7af4411b868d9e4238acbb59c63cb99b3633c
        B/table-images/TABLE-1-page-3-1.png: 9dd0c6676501c696be6b037bffb8862401cfdc10a1503e016d11d80964ade6af
        B/table-images/TABLE-1-page-5-1.png: c5a5ca7d991251b5496ee2835c90437cbf4a3dd31d357e97483c99ba47fbdcb1
        B/table-images/page-3.png: cb661c6ad3924b6f29b836f7a421df35a5bbd75c3ac9002a40b24738c9307483
        B/table-images/TABLE-3-page-8-1.png: f6f7ed02ec42f51f544ef548a22a23c8fcd1dd3026a940471ba9c2ece3c2651c
        B/table-images/page-7.png: 6a29cc1e1e4eb143968af9b7daa12c86ccf9ec58b151bb1f9831fc73f38f88d8
        B/table-images/page-5.png: b0adc930d5754b5f61956abe253d86c6b680c7900cde8af4b8b90af283069c55
        B/table-images/TABLE-4-page-8-2.png: 68d30213c821be94b8fccba37765cd28e0318464177f1538117eebeebf594bed
        B/table-images/page-8.png: 8491214f0dacab1c1b2ebc4ba82f27bce2437db6e10ae61bebfdb0756973b234
        B/table-images/manifest.json: 22ed4ec96747577152682ec9c401eb74cc73fb2f8196d532f472402cb6e56593
        B/table-images/TABLE-2-page-7-1.png: 8fefc96726c0a265e26188d161deb5afa9252d24b81942d4eea1cb1aff74229f
        B/clauses/window-03/raw.json: d967660928f725e8988707c25bcd39fecea27b1fa883c42c2683bd79aa59cdee
        B/clauses/window-03/prompt.txt: c35a18e81cec33a1924c3fe4ccd63bafc8d68b9fd346f13d8334578fdd17900e
        B/clauses/window-03/meta.json: ecd5d91f1cf398c8f4dbc43ce2646d3c8b4077260491160bfa788b1ad2dd085f
        B/clauses/window-04/raw.json: b3c66b8cb84afd20177dd263ef2888a3d548a01139e0cc36a50f9f6ebb2d3f03
        B/clauses/window-04/prompt.txt: aa642666bd8ff9c0867dcbbfbe06af70b322fd31bc410095ff28bd8d04d366c6
        B/clauses/window-04/meta.json: f0b5f4c7f1be6e982ddcb0e8c7adcda333f3fea87f7715c61d9c8e2e1a797012
        B/clauses/window-05/raw.json: 88fd8d07566e576fb0597a3a31f6ade0fa22ff9d58bc7e9f5ebb7f3e0dc08a68
        B/clauses/window-05/prompt.txt: 43a107ce00402016753deee388153b8cf1a21bcdc45eebc279273a2d662f469b
        B/clauses/window-05/meta.json: 675860f9b2c1eafcf98bfce7e9f8922c39834e71434bafab70e638ef3a0c95af
        B/clauses/window-02/raw.json: ea203b5482c4f5176c00ac7a7437cae3ecd2b7a85c13371e907c5f9406fc50f1
        B/clauses/window-02/prompt.txt: a5ec62be575a0a46c3514234fb18621a8bd74a2ae6a0588084e60ad1b0ab829f
        B/clauses/window-02/meta.json: 437c164d8f013feffc2ec3985053b391931fe27caed4aa36fa698d9e3bfff4e3
        B/clauses/window-07/raw.json: c873e2fb6f20bb5dc05f5764aa7de4a0ecba11489ab60adf1797f6abad543bce
        B/clauses/window-07/prompt.txt: 1908cb388887975d2d9805552b9fee2c297e53e1205ce82331f92c5eb9a6e569
        B/clauses/window-07/meta.json: e9349e2480c76c9e3b3e1c365e3c08bac8cf25dfc556b96d3bc19acb6147c7cf
        B/clauses/window-01/raw.json: a6bc1c9f27b8f2a44a68262207f3f411d2f016f3e688beb10ff1ee52950cb859
        B/clauses/window-01/prompt.txt: dadc74d5761cb6b15437d43ad02dbaa6f229d4d651c37f632f53e3c596cdb70a
        B/clauses/window-01/meta.json: f9012ae81169ae7bb08bfd48dc04d19c03a39fdc94dacfb7e4235926070647b2
        B/clauses/window-06/raw.json: de7a833c85aab5ce46218c37b912ff7dfa1a84d483fc0d487296df2a5024d3d3
        B/clauses/window-06/prompt.txt: fc6f6f02ffadbcf8fc2e99448fc47c3e5edb410d08ce7c7bbd12c2d7ed370d79
        B/clauses/window-06/meta.json: 04ef3022a9ea85ab74ca7ca960d897a1b4705199bfe19763f52e97fd3c535566
        B/tables/TABLE-4-page-8-5/raw.json: 29a805eb58c1d1a670fa1a098bd1e783180bee6be729d8fd120b3f8f5592f683
        B/tables/TABLE-4-page-8-5/prompt.txt: 6754e73c5d195ea45678b2b4db2198f1324cd6ff0b6041d12c41ed83cd52ac2c
        B/tables/TABLE-4-page-8-5/meta.json: 7a6d471c987f2ced2fb3c21862aeb7186e7766ce5fb25b036627a0c71c7233ca
        B/tables/TABLE-3-page-8-4/raw.json: e50a004a3afd3ad6a46fba74eefdf29f9dc259d98418df2265c624990cc41c85
        B/tables/TABLE-3-page-8-4/prompt.txt: f77364d75b8913a004629d12c6fc3bdcc7f79cb7a74728f664dc66a4433e70c7
        B/tables/TABLE-3-page-8-4/meta.json: 2583a9b74aac4bbdee4b9924c9bece1eb7d99bde25673450cf0c1e9c5e132ad3
        B/tables/TABLE-1-page-5-2/raw.json: 9193d1c58ad00dd5ba6df5cb8cb97684a47ee15f2fc7c3606031732234b80604
        B/tables/TABLE-1-page-5-2/prompt.txt: adf9dad96a41c4a0f54eed728ac807bb2390ef6bcf420f3a9854758cff410881
        B/tables/TABLE-1-page-5-2/meta.json: 5731608bcec5408432b71dda1f7e26b4d08785e2dd3596b3f6e0b20c10aada9a
        B/tables/TABLE-1-page-3-1/raw.json: fe7360ac941adc7a02bf7b8b6d20c71266697ffd118bba836852777836c42129
        B/tables/TABLE-1-page-3-1/prompt.txt: fe377e80c2ab8609c47b8cf068e1cedea81994cd3b7617244d2d9013a58b19ff
        B/tables/TABLE-1-page-3-1/meta.json: c58e1957afbd21d74b9b73dd3725b0d56e6dd3e0a75a70516c4ec0210063b171
        B/tables/TABLE-2-page-7-3/raw.json: 9faab8a10e187e4934333da19676378ee440686c3194d677fd3c5ef5f2869abf
        B/tables/TABLE-2-page-7-3/prompt.txt: ef10a17e95d058821fe3420840d973e814be26720173889fd61f07cc908c27fc
        B/tables/TABLE-2-page-7-3/meta.json: 86f9fc59ef29701619daf5e6ed7d77eb90529c3643628277e3f2b260036db5d5
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
      pdf_sha256: f71dc47ac2f8923ba9109c78bc40bca67bb33825fb0e5bae629800c0a31eea38
      source_review: _compare/relationships-2026-11-16/review-current/Yu2024
      source_status_sha256: 36886f2770d159787e28ec16ed3092b7b15800998a569b3623892f95a49cd4cc
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    packet_preparation_script_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
  proposal:
    id: R017
    exposure:
      text: SLF-LL
    outcome:
      text: aphasia severity
    analysis_label: ROC curve analysis
    relation: performance
    evidence_ids:
    - P1-S1-C10
    - P5-S1-C9
    - P8-S1-C9
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
      pdf_sha256: f71dc47ac2f8923ba9109c78bc40bca67bb33825fb0e5bae629800c0a31eea38
      source_review: _compare/relationships-2026-11-16/review-current/Yu2024
      source_status_sha256: 36886f2770d159787e28ec16ed3092b7b15800998a569b3623892f95a49cd4cc
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
  audit:
    original_audit:
      coverage_issues:
      - Result passage disposed without unit P3-S3-C10
      - Result passage disposed without unit P3-S3-C9
      - Result passage disposed without unit P4-S1-C1
      - Result passage disposed without unit P4-S1-C3
      - Result passage disposed without unit P4-S1-C4
      - Accounting without a linked unit P4-S1-C6
      - Accounting without a linked unit P4-S1-C7
      - Accounting without a linked unit P4-S1-C9
      - Unaccounted source passage P4-S1-C7
      - Unaccounted source passage P4-S1-C9
      - Unaccounted source passage P4-S1-C6
      - Result passage disposed without unit P7-S2-C3
      - Result passage disposed without unit P8-S1-C4
      - Result passage disposed without unit P9-S1-C3
      unattached_null_or_qualifier_ids: []
      suppressed_nonrepresented_units: 9
      default_disposition_count_requires_completeness_check: 149
      unselected_timing_passages:
      - P1-S1-C2
      - P2-S3-C4
      - P2-S3-C5
      personal_effect_slots_without_result_classification: []
      held_frame_selections:
      - slot: dependent_variable_statement
        source_id: P4-S1-C11
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
        source_id: P8-S1-C5
        reason: Requires a Methods outcome definition; model selection retained for
          inspection only
      - slot: validation
        source_id: P1-S2-C3
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      - slot: validation
        source_id: P3-S2-C11
        reason: No validation-design cue; inspect the source rather than inferring
          a design
      empty_frame_slots_require_confirmation:
      - analysis_restrictions
      - personal_factors
      - tested_personal_effects
      - explicitly_not_adjusted
      unclassified_extraction_ids: []
      table_review_required:
      - TABLE-1-page-3-1
      - TABLE-1-page-5-2
      - TABLE-2-page-7-3
      - TABLE-3-page-8-4
      - TABLE-4-page-8-5
      unlinked_tables:
      - TABLE-1-page-3-1
      - TABLE-1-page-5-2
      - TABLE-2-page-7-3
      - TABLE-4-page-8-5
      source_anomalies: []
      visual_review_required:
        scope: All main-paper figures and table crops
        note: Automatic crops and matching transcriptions do not certify visual completeness.
          Figures are not automatically interpreted.
        caption_candidate_units:
        - P3-S1
        - P3-S2
        - P3-S3
        - P4-S1
        - P4-S2
        - P5-S1
        - P5-S2
        - P5-S3
        - P6-S1
        - P6-S2
        - P7-S2
        - P8-S1
      approval: Not performed. Structural checks and model selections do not establish
        semantic correctness.
    candidate_discovery:
      model: gemma4:31b
      model_digest: 92808281a855666acf35743d49004bb30c810152cd004baf78f31b4578920e49
      pdf_sha256: f71dc47ac2f8923ba9109c78bc40bca67bb33825fb0e5bae629800c0a31eea38
      source_review: _compare/relationships-2026-11-16/review-current/Yu2024
      source_status_sha256: 36886f2770d159787e28ec16ed3092b7b15800998a569b3623892f95a49cd4cc
      code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
      version: candidate-inventory-v1
    coverage:
    - source_id: P1-S1-C8
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      reason: Reports significant negative association of Areas-LL, SLF-LL, and IFOF-LL
        with aphasia severity.
    - source_id: P1-S1-C9
      disposition: represented
      result_indexes:
      - 12
      reason: Reports variance explained by Model III.
    - source_id: P1-S1-C10
      disposition: represented
      result_indexes:
      - 15
      - 16
      - 17
      reason: Reports AUC for Areas-LL, SLF-LL, and IFOF-LL.
    - source_id: P1-S2-C3
      disposition: represented
      result_indexes:
      - 18
      reason: Reports AUC for combination of SLF-LL and IFOF-LL.
    - source_id: P3-S3-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to Table 1 for demographic and clinical characteristics.
    - source_id: P3-S3-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes aphasia type distribution.
    - source_id: P3-S3-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Describes group sizes for aphasia severity.
    - source_id: P3-S3-C9
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports difference in aphasia type between groups, not a lesion-outcome
        relationship.
    - source_id: P3-S3-C10
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports null differences in demographics and stroke-related variables.
    - source_id: P4-S1-C1
      disposition: repeated
      result_indexes: []
      reason: Restatement of null demographic differences.
    - source_id: P4-S1-C2
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to lesion overlay maps.
    - source_id: P4-S1-C3
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative description of lesion distribution.
    - source_id: P4-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Qualitative description of lesion extent.
    - source_id: P4-S1-C5
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to Table 2 for lesion loads.
    - source_id: P4-S1-C6
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      reason: Reports significantly smaller lesion loads for Areas-LL, SLF-LL, and
        IFOF-LL in mild/moderate group.
    - source_id: P4-S1-C7
      disposition: represented
      result_indexes:
      - 9
      - 10
      reason: Reports null inter-group difference for ILF-LL and UF-LL.
    - source_id: P4-S1-C9
      disposition: represented
      result_indexes:
      - 0
      - 1
      - 2
      - 3
      reason: Reports Spearman correlations for Areas-LL, SLF-LL, IFOF-LL, and ILF-LL.
    - source_id: P4-S1-C10
      disposition: represented
      result_indexes:
      - 4
      reason: Reports null correlation for UF-LL.
    - source_id: P4-S1-C11
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to Table 3 for regression results.
    - source_id: P4-S1-C12
      disposition: background_or_descriptive
      result_indexes: []
      reason: Introductory sentence for Model I results.
    - source_id: P5-S1-C1
      disposition: represented
      result_indexes:
      - 11
      reason: Reports Model I variance and significance for SLF-LL.
    - source_id: P5-S1-C2
      disposition: represented
      result_indexes:
      - 12
      reason: Reports Model II variance and significance for SLF-LL and Areas-LL.
    - source_id: P5-S1-C3
      disposition: represented
      result_indexes:
      - 13
      reason: Reports Model III variance and significance for SLF-LL, Areas-LL, and
        IFOF-LL.
    - source_id: P5-S1-C4
      disposition: represented
      result_indexes:
      - 14
      reason: Reports Model IV variance and significance including combination variable.
    - source_id: P5-S1-C5
      disposition: repeated
      result_indexes:
      - 11
      - 12
      - 13
      - 14
      reason: Summary statement of significant predictors across models.
    - source_id: P5-S1-C6
      disposition: represented
      result_indexes:
      - 15
      reason: Reports that ILF-LL was not a significant predictor in regression models.
    - source_id: P5-S1-C7
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports VIF values for multicollinearity.
    - source_id: P5-S1-C9
      disposition: represented
      result_indexes:
      - 15
      - 16
      - 17
      - 18
      reason: Reports cut-off values and accuracy for Areas-LL, SLF-LL, IFOF-LL, and
        combination.
    - source_id: P5-S1-C11
      disposition: repeated
      result_indexes:
      - 11
      - 12
      - 13
      - 14
      reason: Discussion restatement of regression predictors.
    - source_id: P7-S1-C11
      disposition: repeated
      result_indexes:
      - 13
      - 18
      reason: Discussion restatement of SLF-LL, IFOF-LL, and combination predictive
        roles.
    - source_id: P7-S1-C12
      disposition: repeated
      result_indexes:
      - 1
      - 16
      reason: Discussion restatement of SLF-LL role.
    - source_id: P7-S2-C3
      disposition: repeated
      result_indexes:
      - 2
      - 17
      - 18
      reason: Discussion restatement of IFOF-LL and combination roles.
    - source_id: P7-S2-C9
      disposition: represented
      result_indexes:
      - 6
      - 7
      - 8
      - 9
      - 10
      reason: Table 2 providing median lesion loads and p-values for inter-group differences.
    - source_id: P8-S1-C4
      disposition: background_or_descriptive
      result_indexes: []
      reason: Refers to Table 3.
    - source_id: P8-S1-C6
      disposition: background_or_descriptive
      result_indexes: []
      reason: Reports VIF < 10.
    - source_id: P9-S1-C3
      disposition: repeated
      result_indexes:
      - 6
      - 7
      - 8
      reason: Restatement of extensive damage in severe group.
    - source_id: P9-S1-C8
      disposition: repeated
      result_indexes:
      - 16
      - 17
      - 18
      reason: Restatement of cutoff values utility.
    - source_id: P9-S1-C9
      disposition: repeated
      result_indexes:
      - 15
      reason: Restatement that ILF-LL and UF-LL did not enter models.
    - source_id: P9-S2-C2
      disposition: repeated
      result_indexes:
      - 9
      - 10
      reason: Restatement of null difference for UF/ILF on overlay maps.
    - source_id: P9-S2-C8
      disposition: background_or_descriptive
      result_indexes: []
      reason: Restatement of aphasia type difference.
    unresolved_coverage:
    - source_id: P4-S1-C1
      disposition: unresolved
      reason: Model claimed coverage without linking a candidate
    - source_id: P5-S1-C11
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    - source_id: P7-S2-C9
      disposition: unresolved
      reason: Coverage source was not requested or was repeated; not accepted as coverage
    pending_source_ids:
    - P3-S3-C5
    - P3-S3-C7
    - P3-S3-C8
    - P3-S3-C9
    - P3-S3-C10
    - P4-S1-C1
    - P4-S1-C2
    - P4-S1-C3
    - P4-S1-C4
    - P4-S1-C5
    - P4-S1-C11
    - P4-S1-C12
    - P5-S1-C5
    - P5-S1-C7
    - P7-S1-C11
    - P7-S1-C12
    - P7-S2-C3
    - P8-S1-C4
    - P8-S1-C6
    - P9-S1-C3
    - P9-S1-C8
    - P9-S1-C9
    - P9-S2-C2
    - P9-S2-C8
    pending_policy: Every result passage without direct candidate evidence remains
      pending, including model-labelled background and restatements; those labels
      never certify completeness.
    tables_requiring_review:
    - TABLE-1-page-3-1
    - TABLE-1-page-5-2
    - TABLE-2-page-7-3
    - TABLE-3-page-8-4
    - TABLE-4-page-8-5
    paper_complete: false
    approved: false
    policy: New candidates require independent source checks; coverage dispositions
      are model suggestions. No original outputs changed.
  study_frame:
    slots:
      analysed_sample:
      - P2-S3-C4
      recruited_sample:
      - P2-S3-C4
      eligibility:
      - P2-S3-C5
      - P2-S3-C6
      imaging_provenance:
      - P3-S1-C2
      - P3-S1-C4
      imaging_timing:
      - P6-S1-C8
      outcome_timing:
      - P6-S1-C8
      outcome_definition:
      - P1-S1-C3
      - P2-S3-C10
      - P2-S4-C4
      validation:
      - P1-S1-C10
      analysis_restrictions: []
      dependent_variable_statement:
      - P3-S2-C9
      limitations:
      - P9-S2-C6
      - P9-S2-C7
      - P9-S2-C9
      - P9-S2-C10
      - P9-S2-C12
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P5-S1-C2
      - P5-S1-C3
      - P5-S1-C4
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P2-S3-C4
      - P3-S3-C10
      - P5-S3-C1
      - P9-S2-C7
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: none_described
    held_selections:
    - slot: dependent_variable_statement
      source_id: P4-S1-C11
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
      source_id: P8-S1-C5
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P1-S2-C3
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P3-S2-C11
      reason: No validation-design cue; inspect the source rather than inferring a
        design
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
      pdf_sha256: f71dc47ac2f8923ba9109c78bc40bca67bb33825fb0e5bae629800c0a31eea38
      review_sha256: dc2dd885c2965b804d6a334deccb81ebd5958160acb1dc1053ca82b0f859235d
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
      - P1-S1-C10
      - P5-S1-C9
      source_result: The study reported that the lesion load of the superior longitudinal
        fasciculus (SLF-LL) demonstrated good predictive performance for aphasia severity,
        with an AUC of 0.84 (95% CI [0.715, 0.965]) in ROC curve analysis. This was
        based on 46 patients with post-stroke aphasia, where SLF-LL was calculated
        as the proportion of the SLF tract involved by the lesion (template overlap).
      result_status: performance_only
      patient_measurement: template_lesion_overlap
      checks:
        analysis_identity:
          answer: fits
          reason: The selected analysis is the ROC curve analysis for SLF-LL predicting
            aphasia severity. The source explicitly states 'The ROC curve analyses
            yielded the validated area under the curve (AUC) 0.84 both for Areas-LL
            and SLF-LL' (P1-S1-C10) and provides the specific cut-off and CI in P5-S1-C9.
            The proposed core correctly identifies this as a performance analysis.
          source_ids:
          - P1-S1-C10
          - P5-S1-C9
          - P3-S2-C11
        direction:
          answer: fits
          reason: The source indicates a significant negative association (P1-S1-C8,
            P4-S1-C9) and good predictive performance (P1-S1-C10). The proposed core
            states 'good predictive performance' and 'likely' direction, which is
            consistent with the significant AUC and negative correlation. It does
            not claim a specific causal direction but correctly reflects the predictive
            utility.
          source_ids:
          - P1-S1-C8
          - P1-S1-C10
          - P4-S1-C9
        construct:
          answer: fits
          reason: 'The exposure is SLF-LL, defined as lesion load (overlap of patient
            lesion with reference tract map). The source confirms this method: ''lesion
            load = (the volume of the overlap/the total volume of the critical regions)
            × 100 %'' (P3-S2-C2) and that tracts were extracted from the JHU atlas
            (P3-S1-C4). The outcome is aphasia severity measured by WAB-AQ (P1-S1-C3).
            The proposed core correctly identifies the measurement as template_lesion_overlap,
            not patient_diffusion, as the study used structural MRI and atlas overlays,
            not DTI for the final metric (P9-S2-C10 notes lack of DTI).'
          source_ids:
          - P3-S1-C4
          - P3-S2-C2
          - P1-S1-C3
          - P9-S2-C10
        qualifications:
          answer: fits
          reason: The proposed core includes the binary classification of aphasia
            severity (mild/moderate vs severe/very severe) as a qualification, which
            is supported by P2-S4-C4. It also lists limitations such as small sample
            size, gender/stroke type imbalance, and lack of DTI, which are supported
            by P9-S2-C6, P9-S2-C7, and P9-S2-C10. These are material caveats for interpreting
            the generalizability and methodological scope.
          source_ids:
          - P2-S4-C4
          - P9-S2-C6
          - P9-S2-C7
          - P9-S2-C10
        missing_material_caveat:
          answer: fits
          reason: 'The core includes the key limitations mentioned in the source:
            small sample, demographic/stroke type imbalance, and the absence of DTI
            data. The binary classification of the outcome is also included. No other
            material caveats that would change the interpretation of the SLF-LL performance
            result appear to be missing from the provided source window.'
          source_ids:
          - P9-S2-C5
          - P9-S2-C6
          - P9-S2-C7
          - P9-S2-C10
      optional_pending:
      - Specific AUC value (0.84) and CI [0.715, 0.965] not transcribed in core fields,
        but present in source P1-S1-C10 and P5-S1-C9
      - Cut-off value for SLF-LL (28.133%) not transcribed, present in P5-S1-C9
      verdict: draft
      reason: All five core checks fit the source.
      material_issues: []
    pending_details:
    - Detailed statistics, atlas/reference-space and structured confounder metadata
      not transcribed.
    - Recovery phase is not classified; use the reported timing words.
    - Evidence-strength rating is a conservative draft placeholder pending human review.
    - Specific AUC value (0.84) and CI [0.715, 0.965] not transcribed in core fields,
      but present in source P1-S1-C10 and P5-S1-C9
    - Cut-off value for SLF-LL (28.133%) not transcribed, present in P5-S1-C9
    normalizations:
    - field: bucket
      original: predictors
      action: route_from_kind
      value: regions
    analysis_identity:
      id: R017
      exposure:
        text: SLF-LL
      outcome:
        text: aphasia severity
      analysis_label: ROC curve analysis
      relation: performance
      evidence_ids:
      - P1-S1-C10
      - P5-S1-C9
      - P8-S1-C9
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
        pdf_sha256: f71dc47ac2f8923ba9109c78bc40bca67bb33825fb0e5bae629800c0a31eea38
        source_review: _compare/relationships-2026-11-16/review-current/Yu2024
        source_status_sha256: 36886f2770d159787e28ec16ed3092b7b15800998a569b3623892f95a49cd4cc
        code_sha256: 758ad70c485d03e6c5870cdbcec7d72f889a388fabed4b3393d3be05f1121872
        version: candidate-inventory-v1
    paper_complete: false
    visual_prose_readings:
      P2-S3-C4:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f71dc47ac2f8923ba9109c78bc40bca67bb33825fb0e5bae629800c0a31eea38
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 3a3a940da341c7e798919daaa2ad68a2c79cb203da55b3cba6a8727d4b888313
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P2-S3-C4
          page: 2
          text_layer_sha256: 3a3a940da341c7e798919daaa2ad68a2c79cb203da55b3cba6a8727d4b888313
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Subjects\nData on forty-six right-handed patients [31 cases\
          \ of ischemic stroke \nand 15 cases of hemorrhagic stroke; 35 males and\
          \ 11 females; mean age \n(standard deviation, SD), 56.09 (12.46) years,\
          \ range, 25–78 years; the \nmedian (interquartile range, IQR) duration of\
          \ education, 10.50 (3) \nyears, range, 6–16 years; the median (IQR) time\
          \ post-stroke (TPO), \n23.50 (41) days, range, 5–89 days] with PSA admitted\
          \ to the rehabili­\ntation department of our hospital between March 2020\
          \ and May 2022 \nwere analyzed."
        anchor_text: "Subjects\nData on forty-six right-handed patients [31 cases\
          \ of ischemic stroke \nand 15 cases of hemorrhagic stroke; 35 males and\
          \ 11 females; mean age \n(standard deviation, SD), 56.09 (12.46) years,\
          \ range, 25–78 years; the \nmedian (interquartile range, IQR) duration of\
          \ education, 10.50 (3) \nyears, range, 6–16 years; the median (IQR) time\
          \ post-stroke (TPO), \n23.50 (41) days, range, 5–89 days] with PSA admitted\
          \ to the rehabili­\ntation department of our hospital between March 2020\
          \ and May 2022 \nwere analyzed."
        excluded_fragments: []
        image_sha256: aa17e372d2fa6434404768b6c288d2095d34d39f6d16630e26ec4dca6891b2ac
        transcription: 'Subjects


          Data on forty-six right-handed patients [31 cases of ischemic stroke and
          15 cases of hemorrhagic stroke; 35 males and 11 females; mean age (standard
          deviation, SD), 56.09 (12.46) years, range, 25–78 years; the median (interquartile
          range, IQR) duration of education, 10.50 (3) years, range, 6–16 years; the
          median (IQR) time post-stroke (TPO), 23.50 (41) days, range, 5–89 days]
          with PSA admitted to the rehabilitation department of our hospital between
          March 2020 and May 2022 were analyzed'
      P9-S2-C7:
        binding:
          version: prose-images-v14
          code_sha256: e3a753f28fa59991e5048d54458af0dad5ae3161412a06fbd2ae3c8dfae57cd1
          pdf_sha256: f71dc47ac2f8923ba9109c78bc40bca67bb33825fb0e5bae629800c0a31eea38
          layout_sha256: d3ffc5761ad06f5cab9d484f62a160200a0fd6f6f8dae0563b2358a6b246ea3d
          anchor_sha256: 947524f45f9bcae06b174eb1ad3b2ecdb01ce689cf5bb02e522613c641723493
          exclusions_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
          source_id: P9-S2-C7
          page: 9
          text_layer_sha256: 947524f45f9bcae06b174eb1ad3b2ecdb01ce689cf5bb02e522613c641723493
          models: *id001
          model_digests: *id002
          host: http://localhost:11434
        status: agreed_model_transcription
        original_text: "Second, \nthe majority of the participants (76.09 %) were\
          \ males, and the majority \nof stroke type was infarction (67.39 %)."
        anchor_text: "Second, \nthe majority of the participants (76.09 %) were males,\
          \ and the majority \nof stroke type was infarction (67.39 %)."
        excluded_fragments: []
        image_sha256: 2491e69ca774ec83d1d0ae14a40e508f2daaedd6c2689dd6d18a5a29671fc076
        transcription: . Second, the majority of the participants (76.09 %) were males,
          and the majority of stroke type was infarction (67.39 %)
    remaining:
    - Human PDF review and approval
    - Pending metadata enrichment
    - Main Results, figures and tables completeness check
reviewer_marks:
- id: relationship-source-check
  page: 1
  quote: "The ROC curve analyses yielded the validated area under the curve (AUC)\
    \ 0.84 both for \nAreas-LL and SLF-LL and 0.76 for IFOF-LL, indicating good predictive\
    \ performance (p < 0.01)."
  status: pending
  by: agent:relationship-converter
  date: '2026-11-26'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
