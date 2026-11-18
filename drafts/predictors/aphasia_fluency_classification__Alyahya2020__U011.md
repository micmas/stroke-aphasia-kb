---
id: aphasia_fluency_classification
name: Aphasia fluency classification
kind: predictor
findings:
- id: f1
  target_kind: impairment
  direction: likely
  relationship: correlational
  method: behavioral_only
  design: cross-sectional
  sample:
    n: 46
    population: 25 fluent and 21 non-fluent chronic aphasia patients
    phase: chronic
    time_post_onset: Patient group 16–280 months; not applicable to controls
    cohort: Same participants as earlier Alyahya studies; same or subsample in Butler2014/Halai2017,
      not independent replication
  statistics:
    threshold: 'Four mixed ANOVAs: alpha .0125; Bonferroni-adjusted post hoc tests'
    effect_size: See claim; group and task effects, not prognosis
  confounders_controlled:
  - Mixed ANOVA group and discourse-task factors
  confounders_not_controlled:
  - Not a fully adjusted demographic prognostic analysis
  region_definition:
    kind: not_reported
  author_limitations:
  - White-matter associations based on atlas overlap rather than diffusion-weighted
    imaging
  evidence_quality: cohort
  strength: moderate
  provenance:
    extracted_by: agent:codex (source mapping after dual extraction and local review)
    extracted_on: '2026-11-18'
    paper_section: Main PDF Methods, Results, Table 2 and Figure 4
    confidence: medium
    flags:
    - human_approval_pending
    - shared_cohort
    - atlas_overlap_not_tractography
  outcome_timing:
    type: status_at_assessment
    interval: Cross-sectional chronic status; not longitudinal recovery or treatment
      response
  notes: Assessment context matters. Task effects do not establish therapy benefit;
    group classification is not a causal exposure.
  target: fluency
  claim: The BDAE-defined fluent group (n=25) outperformed the non-fluent group (n=21)
    in quantity, lexical diversity, informativeness and speech rate across discourse
    tasks. Main group effects were p<.001; partial eta-squared .46, .52, .44 and .39
    respectively. Effects persisted when lesion size was added; classification and
    outcomes overlap conceptually, so this is not an independent prognostic model.
  citation: '@Alyahya2020'
  source_passages:
  - section: Source passage P5-S2-C3
    page: 5
    quote: 'The

      ANOVA results revealed significant group effects with better

      performance for the fluent group than the non-fluent group

      on the quantity of production [F(1,44) = 38.11, P 5 0.001,

      partial g2

      =

      0.46], lexical diversity [F(1,44)

      =

      48.46,

      P 5 0.001, partial g2 = 0.52], informativeness [F(1,44) =

      35.04, P 5 0.001, partial g2 = 0.44], and speech rate

      [F(1,44) = 28.15, P 5 0.001, partial g2 = 0.39].'
    supports: claim
  - section: Source passage P4-S1-C5
    page: 4
    quote: 'The dependant variable for

      the ANOVAs were: (i) number of content words (quantity); (ii)

      type count (lexical diversity); (iii) informativeness (quality); and

      (iv) WPM (speech rate), with an alpha of P = 0.0125 (Bonferroni

      corrected for multiple comparison).'
    supports: claim
  - section: Source passage P3-S2-C8
    page: 3
    quote: Four measures were extracted from each sample.
    supports: claim
  - section: Source passage P3-S2-C9
    page: 3
    quote: 'First, the number of content words was counted as a measure of

      quantity of production.'
    supports: claim
  - section: Source passage P3-S2-C13
    page: 3
    quote: 'Second, the number of distinct

      content words (type count) was coded as a measure of lexical

      diversity.'
    supports: claim
  - section: Source passage P3-S2-C15
    page: 3
    quote: 'Third, informativeness was coded as

      a measure of quality in terms of information accuracy and ap-

      propriateness.'
    supports: claim
  - section: Source passage P3-S3-C4
    page: 3
    quote: 'Finally, words per minute (WPM) measur-

      ing speech rate was obtained by dividing the total number of

      tokens by the duration of the sample.'
    supports: claim
  - section: Main PDF page 3 (agent source check)
    page: 3
    quote: 'Forty-six patients who had developed aphasia following a single

      left haemorrhagic or ischaemic stroke were tested in the chronic

      stage (412 months post-stroke). Aphasia was diagnosed and

      classified using the BDAE (Goodglass and Kaplan, 1983).

      Participants were native English speakers with normal or cor-

      rected-to-normal vision and/or hearing. The exclusion criteria

      included multiple strokes or any other neurological conditions, se-

      vere motor-speech disorders, visual neglect, any contraindications

      for MRI scanning, being pre-morbidly left-handed, and patients

      who did not produce any response in all discourse samples. No

      restrictions were placed according to aphasia severity or classifi-

      cation, in order to sample the full range of aphasia symptoms. In

      addition to the patients, discourse samples were collected from

      20 age- and education-matched neurotypical adults. All partici-

      pants were native English-speakers, right-handed, and reported

      no abnormal neurological conditions or history of brain injury.

      Demographic information of both groups is presented in Table 1.

      Informed consent was obtained from all participants prior to par-

      ticipation under approval from local ethics committee.

      '
    supports: sample
  - section: Main PDF page 4 (agent source check)
    page: 4
    quote: 'The unified PCA model was mapped onto brain lesions using a

      voxel-based correlational methodology (VBCM) (Tyler et al.,

      2005). In contrast to voxel-lesion symptom mapping (Bates et al.,

      2003), which uses binary lesion status of a voxel, VBCM identi-

      fies statistical relationships between brain and behavioural by

      correlating the signal intensity per voxel (as a continuous value)

      with the behavioural performance (see Geva et al., 2012 for a

      comparison between the two methods). A multiple regression

      model was created using the normalized-smoothed T1-weighted

      images as the dependant variable and language and cognitive

      component as regressors of interest, entered simultaneously along

      with the other components and demographic variables (age, edu-

      cation, and time since stroke onset). Two parallel analyses were

      performed, with/without lesion volume as a covariate, to avoid a

      possible risk for type II error with the inclusion of lesion volume.

      The results were thresholded at P5 0.001 voxel-level and clus-

      ter-level corrected using family-wise error (FWE) at P5 0.05.

      '
    supports: method
  - section: Main PDF page 4 (agent source check)
    page: 4
    quote: "We conducted four 2 \x02 3 mixed ANOVAs for each connected\nspeech measure,\
      \ with group (neurotypical versus patients with\naphasia) as the between-subject\
      \ factor and discourse genre (com-\nposite picture description versus storytelling\
      \ narrative versus pro-\ncedural) as the within-subject factor. The dependant\
      \ variable for\nthe ANOVAs were: (i) number of content words (quantity); (ii)\n\
      type count (lexical diversity); (iii) informativeness (quality); and\n(iv) WPM\
      \ (speech rate), with an alpha of P = 0.0125 (Bonferroni\ncorrected for multiple\
      \ comparison). All significant interactions\nwere explored using post hoc t-tests,\
      \ and Bonferroni corrected\nfor multiple comparisons. These analyses were repeated,\
      \ but in-\nstead, the between-subject group factor involved fluent (n = 25)\n\
      versus non-fluent (n = 21) aphasia groups, the patients were\ngrouped according\
      \ to their aphasia classification as diagnosed\nusing the BDAE and demonstrated\
      \ in Table 1.\n"
    supports: method
  - section: Main PDF page 5 (agent source check)
    page: 5
    quote: "[F(1,64) = 31.54, P5 0.001, partial g2 = 0.33], lexical diver-\nsity [F(1,64)\
      \ = 40.69 P5 0.001, partial g2 = 0.39], inform-\nativeness [F(1,64) = 26.9,\
      \ P5 0.001, partial g2 = 0.3], and\nspeech rate [F(1,64) = 95.97, P5 0.001,\
      \ partial g2 = 0.6].\nThe results revealed significant main effects of discourse\
      \ genre\nfor the quantity of production [F(2,128) = 73.86, P5 0.001,\npartial\
      \ g2 = 0.54], lexical diversity [F(2,128) = 96.67,\nP5 0.001, partial g2 = 0.6]\
      \ and speech rate [F(2,128) =\n12.02, P5 0.001, partial g2 = 0.15]. For quantity\
      \ of produc-\ntion, storytelling narrative was significantly higher than both\n\
      composite\npicture\ndescription\nand\nprocedural\ndiscourse\n(P5 0.001). For\
      \ lexical diversity, storytelling was again the\nhighest, followed by composite\
      \ picture description and then\nprocedural discourse. The differences between\
      \ storytelling and\nthe other two discourses were significant (P5 0.001), and\
      \ the\ndifferences between picture description and procedural dis-\ncourse was\
      \ also significant (P = 0.01). Finally, for speech rate,\nthe fastest speech\
      \ was produced during procedural discourse,\nfollowed by picture description,\
      \ and then storytelling. The dif-\nferences, however, were only significant\
      \ between procedural\ndiscourse and storytelling (P5 0.001), and procedural\
      \ dis-\ncourse and picture description (P = 0.002).\nThe Group \x02 Discourse\
      \ interaction effects were signifi-\ncant\nfor\nquantity\nof\nproduction\n[F(2,128)\n\
      =\n10.91,\nP 5 0.001,\npartial\ng2\n=\n0.15],\nand\nlexical\ndiversity\n[F(2,128)\
      \ = 6.14, P = 0.003, partial g2 = 0.087]. Both inter-\nactions were driven by\
      \ significantly higher quantity and di-\nversity produced during storytelling\
      \ narrative compared to\nthe other two discourses for both groups (P 5 0.001).\
      \ The\ndifferences between picture description and procedural dis-\ncourse were\
      \ significant for diversity among the patient group\nonly, in favour of picture\
      \ description (P = 0.002). The differ-\nences between the two groups were significant\
      \ for all three\ndiscourses with better performance among the neurotypical\n\
      group (P 5 0.001). Supplementary Table 1 provides a sum-\nmary of the significant\
      \ effects.\nFluent and non-fluent aphasia groups\nThe distribution of the data\
      \ is illustrated in Fig. 3. The\nANOVA results revealed significant group effects\
      \ with better\nperformance for the fluent group than the non-fluent group\n\
      on the quantity of production [F(1,44) = 38.11, P 5 0.001,\npartial g2\n=\n\
      0.46], lexical diversity [F(1,44)\n=\n48.46,\nP 5 0.001, partial g2 = 0.52],\
      \ informativeness [F(1,44) =\n35.04, P 5 0.001, partial g2 = 0.44], and speech\
      \ rate\n[F(1,44) = 28.15, P 5 0.001, partial g2 = 0.39]. There were\nsignificant\
      \ main effects of discourse genre for quantity of\nproduction [F(2,88) = 45.18,\
      \ P 5 0.001, partial g2 = 0.51],\nlexical diversity [F(2,88) = 62.84, P5 0.001,\
      \ partial g2 =\n0.59], and speech rate [F(2,88) = 5.01, P = 0.009, partial g2\n\
      = 0.1]. A greater number of words were produced during\nstorytelling narrative\
      \ than picture description and procedural\ndiscourse (P 5 0.001). For lexical\
      \ diversity, there was greater\ndiversity during storytelling followed by picture\
      \ description\nand then procedural discourse. The differences were signifi-\n\
      cant between storytelling and the other two discourses\n(P 5 0.001), and between\
      \ picture description and procedural\ndiscourse (P = 0.01). Finally, for speech\
      \ rate, patients spoke\nsignificantly faster during procedural discourse compared\
      \ to\nboth storytelling and picture description (P 4 0.003).\nThe Group \x02\
      \ Discourse interaction effects were significant\nfor quantity of production\
      \ [F(2,188) = 19.19, P 5 0.001,\npartial g2 = 0.3] and lexical diversity [F(2,188)\
      \ = 17.48,\nP 5 0.001, partial g2 = 0.28]. Both interactions were driven\nby\
      \ significantly higher quantity and diversity during storytell-\ning compared\
      \ to the other two discourses for both groups\n(P 4 0.01). The differences between\
      \ picture description and\nprocedural discourse were significant for diversity\
      \ among the\nfluent aphasia group only, in favour of picture description\n(P\
      \ = 0.01). The differences between the two groups were sig-\nnificant for all\
      \ three discourses with better performance\namong the fluent group (P 5 0.001).\
      \ Supplementary Table 1\nprovides a summary of the significant effects. We repeated\n\
      the ANOVAs with the addition of lesion size as a covariate.\nThe significant\
      \ main effects and interaction effects remained\nthe same, and specific lesion\
      \ size effects (either as main or\ninteraction effects) were not significant\
      \ in any analysis.\n"
    supports: statistics
predictor_type: clinical
short_definition: Aphasia fluency classification
assessment:
- BDAE classification
- Cookie Theft description
- Dinner Party narrative
- Tea-making procedural discourse
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-18'
relationship_review:
  paper: Alyahya2020
  proposal_id: U011
  review_status_sha256: 2098be11ece6e6965b0178d3e7e122b0a8799637b7236495c9d3f6311d0ed502
  review_binding:
    version: relationship-review-v4
    input_hashes:
      pdf: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
      A/passages.json: 9911233de4e837bf81ba7b6fd2d506e7b02d9f201d3f3f9c76fa87f396473b41
      A/raw.json: 927365420fa3a9f31ce43024189a8b27ad1a3fee901562b8af14597e652dc28b
      A/source-units.json: 5385076b47c3f953efaf01fff04edda1796fe4f5ff57fdd6cd93054b4cc2fedf
      A/full-source-units.json: 506f27cd9c6b5a72cb96e6d2be95432885ad69a55146ac9fac0ba598476ccffc
      A/meta.json: f21184492fb92a7caa58322b05181047963d62ceab371b099ec53b61b8155644
      A/table-images/page-10.png: 102d76252b3cec1f61a5d8290d340e4f288bff2e5bc34fce7772d035f3fecf7e
      A/table-images/page-4.png: df53d5d8f28a82be71abaf653d8e05041aa03031a89c67f4ecf3fa39134d4db9
      A/table-images/TABLE-1-page-4-1.png: 1be9e838e72f02cefcf039c55841dc92e6f4cd231dc4463f9886a5afc430195b
      A/table-images/manifest.json: d398904ed6ab009c72dfe6d623a76d3bfe8a65d3cfcf961ed76feb6c69f76d4d
      A/table-images/TABLE-2-page-10-1.png: c3983f15dfd989f4835e08a85878655b5b89c43d22b66c9fae1c95a9bb6aa990
      A/clauses/window-03/raw.json: 5555e99a6a1cd116865ccdcab248eef6a7810974a2b0ff54a287853d1ddf39f0
      A/clauses/window-03/prompt.txt: f151627d62b35adc5d53cbcb20d4bb27ba80ae0ce87309617d899bdfc83a3752
      A/clauses/window-03/meta.json: b669a5c272186fb25e283f75ca099a4e3636714ad9e0c84f2d5f2526983cd520
      A/clauses/window-04/raw.json: a7a2d8454902eaedbc930e4e6b39aac2bb43daa76148f2a1a140344cf63ce6dd
      A/clauses/window-04/prompt.txt: 7f29b54c25c066e54eaa8ad7f4b9f4ad4bf97c5fc54bf6e5bfe14317d03f5f87
      A/clauses/window-04/meta.json: f6e4417b7bfa72168091cc1439ad01133703eed53653c10a22842876450515d4
      A/clauses/window-05/raw.json: ba624f2cd4c53b7b0836021e5ff82f7694ecd75e890616944604a1606362af49
      A/clauses/window-05/prompt.txt: b06dbebbb6acc8bad9a4c6f9ea270ed15f3e4364f2fe4c0e0fe40eed16f36d81
      A/clauses/window-05/meta.json: 4cddde3ddd6a386c141633e606f92e847c743b6bfd0e76c6a76a6313bbd51726
      A/clauses/window-02/raw.json: 8033908f6d4e01db9f0d81973b8e7b4a6a84c1cf1923f77e5aa8729cdf3bd842
      A/clauses/window-02/prompt.txt: 9c4f2a62f1bf72075c7a49e5ad51f06a189ec00bd8a1d43916462849ef7cc97b
      A/clauses/window-02/meta.json: 876ca664afef1e6562cb716ec49394a3814ddc6c063b4f3dab3679b51de94eb7
      A/clauses/window-09/raw.json: 9fe2e2868974b2fdfa1d5f3b62f674769c3ff86ac405856f9618d864d9024ec8
      A/clauses/window-09/prompt.txt: 4ad0c44c3b39fc0cdbc01794962f4a8a8f3a6dd576e92a63788ad8853b849ba7
      A/clauses/window-09/meta.json: 00745bea8c9b4a19e7fa9fc8b74dce1520cad1e2b594d30cf3fa66fbd1cf60ab
      A/clauses/window-07/raw.json: 44785dd8ee2fffc18eced0926abc86ba273361252d887b8a575d8f8f946d7fd8
      A/clauses/window-07/prompt.txt: f30b52bf5e5b13b570b25b8fd719bbcd39e81de9be782d284a7502393e3ba78a
      A/clauses/window-07/meta.json: 4793dea5219c9a05e29dba9d8a5b47c5fff4a0ceb72431d0abd3e918a93b8d27
      A/clauses/window-01/raw.json: 4cff88c707551defb00ac0dc559250574ece1c83ba6eb98ddf9b36a660404645
      A/clauses/window-01/prompt.txt: 157c4a540fbb6b882573137499c359766ab38bd809b1094acb612925376bcbbe
      A/clauses/window-01/meta.json: 5205d6cecab74463a65f73d663c74addfb6fbe8c70fa423f1f74c18f010e13e2
      A/clauses/window-06/raw.json: f3affada4c52340df4572bb3c9dd56f80e67ac073e89a1e4005cf524ddfeb803
      A/clauses/window-06/prompt.txt: af6679030afca46f3ac1d75eb5725d183c3d96965fee240ca988718c1df13a56
      A/clauses/window-06/meta.json: 60e5eefa1afe46f34ec82d0bb84166c582d68dd1bbdf7158c52252b8b73d6724
      A/clauses/window-08/raw.json: b5fafbcdc1023f1c6b27fdf2c228f51c8e6b6e0be2e99e429581bd0652e1c474
      A/clauses/window-08/prompt.txt: 5c59c84a4df04ca78d649d1ba87ca2b791585773759d042509691c70dca2906d
      A/clauses/window-08/meta.json: 3f7e17e379f2f25a5fa7626687dc87b7fd602b114d99a689a5d1914bbb57c9ff
      A/tables/TABLE-2-page-10-2/raw.json: 102f6c9952a596937f2854950d8bf4a3eb7587c0d2a67b6ade1f1b19d44fbfac
      A/tables/TABLE-2-page-10-2/prompt.txt: 70c16ba02c2712a70054020672f0deecbca63d0c189d603b9a72e3d3e6e47174
      A/tables/TABLE-2-page-10-2/meta.json: 9c7b491c3636955255ca6375ff714c2c322999c994d63ae213dd51272ec03937
      A/tables/TABLE-1-page-4-1/raw.json: e2e5d87b08eba98bd9096063ce9ff912535691b1daaa0958ec8eff4ddd967622
      A/tables/TABLE-1-page-4-1/prompt.txt: 49295ec3c3eafbf59adff23c08d4d6d3b5902eb976ef5900c7daebd2cdfe5887
      A/tables/TABLE-1-page-4-1/meta.json: 799de74499a24566cacf060b82df2622c139578411441d2aa9f1b32f099359b0
      B/passages.json: 9911233de4e837bf81ba7b6fd2d506e7b02d9f201d3f3f9c76fa87f396473b41
      B/raw.json: 706e8fc7502a93720a885a0d504da13bb67bc8df6496e4b1544e63504eba8ab8
      B/source-units.json: 5385076b47c3f953efaf01fff04edda1796fe4f5ff57fdd6cd93054b4cc2fedf
      B/full-source-units.json: 506f27cd9c6b5a72cb96e6d2be95432885ad69a55146ac9fac0ba598476ccffc
      B/meta.json: 6bd35b7e5641e757404604c5b965f526998da922159976b0c4b2247524eeb8ac
      B/table-images/page-10.png: 102d76252b3cec1f61a5d8290d340e4f288bff2e5bc34fce7772d035f3fecf7e
      B/table-images/page-4.png: df53d5d8f28a82be71abaf653d8e05041aa03031a89c67f4ecf3fa39134d4db9
      B/table-images/TABLE-1-page-4-1.png: 1be9e838e72f02cefcf039c55841dc92e6f4cd231dc4463f9886a5afc430195b
      B/table-images/manifest.json: 02b0e79cbfc2f12eb02df548ac49c3020d3c8e8852bcb450010a03c4645edec6
      B/table-images/TABLE-2-page-10-1.png: c3983f15dfd989f4835e08a85878655b5b89c43d22b66c9fae1c95a9bb6aa990
      B/clauses/window-03/raw.json: e56e8d984fcd5b38481701a0eec7e0524271ed53b70a097631a43a3866f54a20
      B/clauses/window-03/prompt.txt: f151627d62b35adc5d53cbcb20d4bb27ba80ae0ce87309617d899bdfc83a3752
      B/clauses/window-03/meta.json: a36b53c9c233a1997ccdee5572175c71ff5d6d62cc64b79a054df262e4c90f0a
      B/clauses/window-04/raw.json: 879b61c2a093904b10225805e466eeeb5f26ac29c3701ac3eb060f2ba45c7706
      B/clauses/window-04/prompt.txt: 7f29b54c25c066e54eaa8ad7f4b9f4ad4bf97c5fc54bf6e5bfe14317d03f5f87
      B/clauses/window-04/meta.json: 3665012c822024e4b77b446b818aa5b114d147369be5d526196b6f2987fddbce
      B/clauses/window-05/raw.json: 2d1ebf125d923000f13874be040198e3d1b1b2426bcd01a6fddfc69a6f9687a8
      B/clauses/window-05/prompt.txt: b06dbebbb6acc8bad9a4c6f9ea270ed15f3e4364f2fe4c0e0fe40eed16f36d81
      B/clauses/window-05/meta.json: 049c36e0469817f0a8c99354cf44b5dbe18b1db73a54d13767c062031489e930
      B/clauses/window-02/raw.json: d3405b8222098d2d8487cb3284519f7c72eee0887cc4448d4c92ac4607412cb3
      B/clauses/window-02/prompt.txt: 9c4f2a62f1bf72075c7a49e5ad51f06a189ec00bd8a1d43916462849ef7cc97b
      B/clauses/window-02/meta.json: 1b9acb206feefdb257957db790a314685178def6e5dea3db50c6fcd064d571db
      B/clauses/window-09/raw.json: 490f9e18f4e8f589f8398f8dc399016fd04d7d6f03012464f7ec0697a29c6d95
      B/clauses/window-09/prompt.txt: 4ad0c44c3b39fc0cdbc01794962f4a8a8f3a6dd576e92a63788ad8853b849ba7
      B/clauses/window-09/meta.json: 7cffe10dd88dc62db9280b4c56f582d9b04b10a7fdd2fb12ea5627648d502309
      B/clauses/window-07/raw.json: c143729dd1aeba61e4e6b54a58f2480203b7747f951494cc1b2374eccf1748d2
      B/clauses/window-07/prompt.txt: f30b52bf5e5b13b570b25b8fd719bbcd39e81de9be782d284a7502393e3ba78a
      B/clauses/window-07/meta.json: 9fe4a2e9185afd2ea930bf96d35273d428f8d1c03a429157cd1dd1417c645005
      B/clauses/window-01/raw.json: 94a7a0266eaf2a44190d60952365a610a2af0511ef1fe01509c9cacc3970b933
      B/clauses/window-01/prompt.txt: 157c4a540fbb6b882573137499c359766ab38bd809b1094acb612925376bcbbe
      B/clauses/window-01/meta.json: 34497c87a478bae3404ca688ef9f71d0b23b6a5e401062c7f5a834924b901aa9
      B/clauses/window-06/raw.json: c8f0e091faf6ba40fcd66961833de58fb93241506e1e6b0d394b72ac932a8f50
      B/clauses/window-06/prompt.txt: af6679030afca46f3ac1d75eb5725d183c3d96965fee240ca988718c1df13a56
      B/clauses/window-06/meta.json: b1a20528cc77b61f82e2b692451ebe9b315f38b7fa6ed374c451ec1e9cbeb644
      B/clauses/window-08/raw.json: 7d1829723e9623eeef6281429c1e8a33a624ded85fc4dcfcf0c06200fc7ea08e
      B/clauses/window-08/prompt.txt: 5c59c84a4df04ca78d649d1ba87ca2b791585773759d042509691c70dca2906d
      B/clauses/window-08/meta.json: 59a63adba23ba32ec4242c2cb2a00c88108c54afa94bdc9e48fab3b70d6e0c9b
      B/tables/TABLE-2-page-10-2/raw.json: be24d4ae4a65774a9c8f3c997a84cb75a3cc506f06ea67f453a028e8cede6678
      B/tables/TABLE-2-page-10-2/prompt.txt: 70c16ba02c2712a70054020672f0deecbca63d0c189d603b9a72e3d3e6e47174
      B/tables/TABLE-2-page-10-2/meta.json: 62d81e5da057a493aae6b056c9ede05736589063ed4b6b121acf47d327eefb54
      B/tables/TABLE-1-page-4-1/raw.json: 8fdf13a51d5b4eaec28602c72f6b1d96f8956238981d6926768822b222c319f2
      B/tables/TABLE-1-page-4-1/prompt.txt: 49295ec3c3eafbf59adff23c08d4d6d3b5902eb976ef5900c7daebd2cdfe5887
      B/tables/TABLE-1-page-4-1/meta.json: d136cce6a1d9d0f9e8cc093ead32652ac072df580de2d24e8c887174b121a5ff
    code:
      relationship_review.py: e1418d43751ffa47aebde470eca9d70747211671c954e9423a376203ee2281a0
      relationship_evidence.py: 531c8a74f366f92842f315f2722b2ba7dbdbeaf052aefa60cdf0c8365ccd6fbb
      ollama_client.py: 4f76f789470a78483698ab86b038600fc2e8c2281692a370bea05f364cee76ea
      strict_data.py: 1b2d69dbbb3b87e23d461caecf0302db7464712a2b2613624bde4a3512473d0b
    model: gemma4:26b
    model_digest: 48eb98ec778c163d87f69d735fcdd79e345063af9af4685613fd018ae5debf5e
    host: http://localhost:11434
    max_output_tokens: 20000
  proposal:
    evidence_ids:
    - P5-S2-C3
    qualifier_ids:
    - P4-S1-C5
    - P3-S2-C8
    - P3-S2-C9
    - P3-S2-C13
    - P3-S2-C15
    - P3-S3-C4
    context_ids:
    - P4-S1-C5
    - P3-S2-C8
    - P3-S2-C9
    - P3-S2-C13
    - P3-S2-C15
    - P3-S3-C4
    table_ids: []
    exposure:
      text: fluent group
      source_id: ''
    outcome:
      text: quantity of production
      source_id: P3-S2-C8
    relation: group_difference
    effect_unit: individual
    result_status: reported_detected
    outcome_type: not_applicable
    direction: positive
    direction_source_id: P5-S2-C3
    origin: current_study
    label_match_candidates:
      exposure:
      - P5-S2-C3
      outcome:
      - P3-S2-C9
      - P5-S1-C8
      - P5-S2-C3
      - P5-S2-C4
    id: U011
    flags:
    - nonverbatim_or_missing_label
    - overlapping_evidence_roles
    - source_display_check
    linked_tables: []
    approved: false
    status: requires_resolution
    context_candidates:
    - P1-S1-C10
    - P12-S3-C5
    - P12-S3-C6
    - P3-S1-C10
    - P3-S1-C11
    - P3-S1-C12
    - P3-S1-C14
    - P3-S2-C11
    - P3-S2-C12
    - P3-S2-C14
    - P3-S2-C3
    - P3-S2-C4
    - P3-S2-C5
    - P3-S2-C6
    - P3-S2-C7
    - P3-S3-C3
    - P3-S3-C5
    - P3-S3-C6
    - P3-S3-C7
    - P4-S2-C5
    - P4-S2-C6
    - P5-S1-C5
    - P5-S1-C6
    - P5-S1-C7
    - P5-S2-C14
    - P5-S2-C6
    - P5-S2-C7
    - P5-S2-C8
    context_policy: Script-attached frame, Methods and nearby source passages; candidates
      are not confirmed analysis-specific controls
    conditional_or_conflicting_unit_ids: []
    digest: d4ebc81e94b0dacb87563b7775e1f31850ae4c2911444c81dae25f16549536df
  audit:
    coverage_issues:
    - Result passage disposed without unit P1-S2-C3
    - Result passage disposed without unit P1-S2-C4
    - Result passage disposed without unit P1-S2-C6
    - Accounting without a linked unit P2-S2-C11
    - Unaccounted source passage P2-S2-C11
    - Accounting without a linked unit P4-S1-C11
    - Result passage disposed without unit P4-S1-C12
    - Result passage disposed without unit P4-S2-C2
    - Unaccounted source passage P4-S1-C11
    - Result passage disposed without unit P4-S2-C11
    - Accounting without a linked unit P5-S1-C1
    - Accounting without a linked unit P5-S1-C2
    - Accounting without a linked unit P5-S1-C3
    - Accounting without a linked unit P5-S1-C4
    - Accounting without a linked unit P5-S1-C5
    - Accounting without a linked unit P5-S1-C6
    - Accounting without a linked unit P5-S1-C7
    - Unaccounted source passage P5-S1-C7
    - Unaccounted source passage P5-S1-C4
    - Unaccounted source passage P5-S1-C1
    - Unaccounted source passage P5-S1-C6
    - Unaccounted source passage P5-S1-C3
    - Unaccounted source passage P5-S1-C5
    - Unaccounted source passage P5-S1-C2
    - Accounting without a linked unit P5-S2-C10
    - Accounting without a linked unit P5-S2-C11
    - Accounting without a linked unit P5-S2-C12
    - Accounting without a linked unit P5-S2-C8
    - Accounting without a linked unit P5-S2-C9
    - Accounting without a linked unit P5-S3-C4
    - Unaccounted source passage P5-S2-C9
    - Unaccounted source passage P5-S3-C4
    - Unaccounted source passage P5-S2-C10
    - Unaccounted source passage P5-S2-C11
    - Unaccounted source passage P5-S2-C8
    - Unaccounted source passage P5-S2-C12
    - Result passage disposed without unit P5-S3-C5
    - Result passage disposed without unit P5-S3-C8
    - Result passage disposed without unit P8-S1-C10
    - Result passage disposed without unit P8-S1-C11
    - Result passage disposed without unit P8-S1-C7
    - Result passage disposed without unit P8-S1-C8
    - Result passage disposed without unit P8-S2-C4
    - Result passage disposed without unit P11-S1-C4
    - Result passage disposed without unit P8-S3-C5
    - Result passage disposed without unit P8-S3-C7
    - Result passage disposed without unit P11-S1-C6
    - Result passage disposed without unit P11-S1-C7
    - Result passage disposed without unit P11-S1-C8
    - Result passage disposed without unit P11-S2-C1
    - Accounting without a linked unit P11-S3-C7
    - Accounting without a linked unit P11-S3-C8
    - Accounting without a linked unit P11-S3-C9
    - Accounting without a linked unit P12-S1-C2
    - Accounting without a linked unit P12-S1-C4
    - Accounting without a linked unit P12-S1-C8
    - Unaccounted source passage P12-S1-C2
    - Unaccounted source passage P11-S3-C9
    - Unaccounted source passage P12-S1-C4
    - Unaccounted source passage P11-S3-C8
    - Unaccounted source passage P11-S3-C7
    - Unaccounted source passage P12-S1-C8
    - Accounting without a linked unit P12-S2-C3
    - Accounting without a linked unit P12-S2-C5
    - Accounting without a linked unit P12-S2-C7
    - Accounting without a linked unit P12-S2-C9
    - Accounting without a linked unit P12-S3-C3
    - Unaccounted source passage P12-S3-C3
    - Unaccounted source passage P12-S2-C9
    - Unaccounted source passage P12-S2-C7
    - Unaccounted source passage P12-S2-C5
    - Unaccounted source passage P12-S2-C3
    - Result passage disposed without unit P12-S3-C8
    - Accounting without a linked unit P12-S4-C2
    - Accounting without a linked unit P12-S4-C3
    - Accounting without a linked unit P13-S1-C2
    - Result passage disposed without unit P13-S1-C3
    - Unaccounted source passage P13-S1-C2
    - Unaccounted source passage P12-S4-C2
    - Unaccounted source passage P12-S4-C3
    - Result passage disposed without unit P13-S1-C8
    unattached_null_or_qualifier_ids:
    - P5-S1-C7
    - P5-S2-C9
    - P5-S2-C10
    - P5-S2-C11
    - P5-S3-C4
    - P8-S1-C10
    - P8-S3-C5
    - P11-S3-C9
    suppressed_nonrepresented_units: 17
    default_disposition_count_requires_completeness_check: 145
    unselected_timing_passages:
    - P3-S1-C8
    personal_effect_slots_without_result_classification: []
    held_frame_selections: []
    empty_frame_slots_require_confirmation:
    - personal_factors
    - tested_personal_effects
    - explicitly_not_adjusted
    unclassified_extraction_ids: []
    table_review_required:
    - TABLE-1-page-4-1
    - TABLE-2-page-10-2
    unlinked_tables:
    - TABLE-1-page-4-1
    - TABLE-2-page-10-2
    source_anomalies: []
    visual_review_required:
      scope: All main-paper figures and table crops
      note: Automatic crops and matching transcriptions do not certify visual completeness.
        Figures are not automatically interpreted.
      caption_candidate_units:
      - P4-S1
      - P4-S2
      - P5-S1
      - P5-S2
      - P5-S3
      - P6-S1
      - P7-S1
      - P8-S1
      - P8-S3
      - P9-S1
      - P11-S3
    approval: Not performed. Structural checks and model selections do not establish
      semantic correctness.
  study_frame:
    slots:
      analysed_sample:
      - P1-S1-C10
      - P3-S1-C13
      recruited_sample:
      - P1-S1-C10
      - P3-S1-C8
      eligibility:
      - P3-S1-C10
      - P3-S1-C11
      - P3-S1-C12
      - P3-S1-C14
      imaging_provenance:
      - P3-S3-C7
      imaging_timing:
      - P3-S3-C7
      outcome_timing:
      - P1-S1-C10
      outcome_definition:
      - P3-S2-C8
      - P3-S2-C9
      - P3-S2-C13
      - P3-S2-C15
      - P3-S3-C4
      validation:
      - P4-S1-C10
      analysis_restrictions:
      - P4-S2-C6
      dependent_variable_statement:
      - P4-S1-C5
      - P4-S2-C5
      limitations:
      - P12-S3-C6
      personal_factors: []
      tested_personal_effects: []
      adjustment_roles:
      - P4-S2-C5
      - P4-S2-C6
      - P5-S2-C14
      - P8-S3-C4
      - P9-S1-C4
      - P10-S2-C2
      - P12-S3-C5
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P4-S2-C11
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections: []
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    checked_by: agent:codex
    date: '2026-11-18'
    approved: false
    pdf_sha256: 7c7fe679ca9614ffbed99fcf352167912a75739289a9dcd5406488095ae29b29
    licence:
      category: cc
      label: CC BY 4.0
      url: http://creativecommons.org/licenses/by/4.0/
      version: published
      source: crossref
      doi: 10.1093/brain/awaa074
      checked: '2026-10-30'
      consulted:
      - crossref
      - unpaywall
      - pdf
    checked_pdf_pages:
    - 1
    - 2
    - 3
    - 4
    - 5
    - 6
    - 7
    - 8
    - 9
    - 10
    - 11
    - 12
    - 13
    visual_pages:
    - 4
    - 5
    - 8
    - 9
    - 10
    scope: 'Main-paper review: seven PCA imaging components, lesion-volume correlation,
      discourse-task differences and fluent/non-fluent group contrast. Table 1, Table
      2, Figure 4 and numerical Results visually checked. Supplements excluded.'
    corrections:
    - Separate models with and without lesion-volume correction; verbal quantity and
      motor speech survive only a lenient adjusted threshold, while verbal quality
      and semantics are not among surviving adjusted components.
    - Executive cluster appears only after lesion-volume adjustment.
    - White-matter anatomy is descriptive atlas overlap, not patient tractography
      or measured disconnection.
    - Age, education and time since stroke are adjustment variables, not demonstrated
      independent predictors; sex is descriptive.
    - Same or overlapping cohort with Alyahya2018 papers, Butler2014 and Halai2017;
      no independent replication claim.
    - Visual PDF confirms <= signs in discourse results that text extraction renders
      as >; subgroup interaction df=188 is printed despite n=46, retained as unresolved.
    remaining:
    - Named-person approval; reconcile shared-cohort evidence before synthesis.
    - Voxel maps and exact atlas/template versions unavailable from main paper; no
      whole-parcel or tract-specific causal claim.
    - Figure 2/3 distributions not visually audited; no exhaustive conversion of every
      behavioural interaction or PCA loading.
    - Supplement-only acquisition/preprocessing details excluded.
reviewer_marks:
- id: relationship-source-check
  page: 5
  quote: 'The

    ANOVA results revealed significant group effects with better

    performance for the fluent group than the non-fluent group

    on the quantity of production [F(1,44) = 38.11, P 5 0.001,

    partial g2

    =

    0.46], lexical diversity [F(1,44)

    =

    48.46,

    P 5 0.001, partial g2 = 0.52], informativeness [F(1,44) =

    35.04, P 5 0.001, partial g2 = 0.44], and speech rate

    [F(1,44) = 28.15, P 5 0.001, partial g2 = 0.39].'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-18'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
