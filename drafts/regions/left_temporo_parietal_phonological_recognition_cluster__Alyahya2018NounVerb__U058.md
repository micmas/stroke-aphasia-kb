---
id: left_temporo_parietal_phonological_recognition_cluster
name: Left temporoparietal phonological recognition cluster
kind: network
findings:
- id: f1
  target_kind: impairment
  direction: likely
  relationship: correlational
  method: VBCM
  design: cross-sectional
  sample:
    n: 48
    population: Native English-speaking chronic aphasia after a single left ischaemic
      or haemorrhagic stroke; 34 men, 14 women; premorbidly left-handed and other
      neurological conditions excluded
    phase: chronic
    time_post_onset: At least 12 months; Table 1 observed range 16–280 months
    cohort: Overlapping participant series with Alyahya2020 and Butler2014/Halai2017;
      not independent replication
  statistics:
    threshold: Primary PCA voxel p=.001, cluster FWE p<.05; executive voxel p=.005.
      Figure 5 adjusted model voxel p=.005 conflicts with Methods .001.
    effect_size: Cluster statistics, not validated individual prediction
  confounders_controlled:
  - Other four PCA factors entered simultaneously
  confounders_not_controlled:
  - Age, education, sex and time since stroke not listed as VBCM covariates
  - Lesion volume omitted in primary map; sensitivity analysis separately qualified
  region_definition:
    kind: data_driven_cluster
    description: Significant cluster locations labelled using Harvard–Oxford and NatBrainLab
      white-matter atlases in MNI space; not entire atlas parcels
  author_limitations:
  - White-matter associations based on atlas overlap rather than diffusion-weighted
    imaging
  evidence_quality: cohort
  strength: moderate
  provenance:
    extracted_by: agent:codex (source mapping after dual extraction and local review)
    extracted_on: '2026-11-18'
    paper_section: Main PDF Methods, Results, Table 6 and Figures 4–5
    confidence: medium
    flags:
    - human_approval_pending
    - shared_cohort
    - atlas_overlap_not_tractography
  imaging: T1
  imaging_details:
    reference_space: other
    reference_space_detail: MNI; exact variant not specified in main text
    atlases_used:
    - Harvard–Oxford (as reported)
    - NatBrainLab white-matter atlas (Catani et al. 2012)
  lesion_mapping:
    analysis: univariate
    n_analysed: 48
    min_lesion_overlap: not_reported
    lesion_volume_correction: none
    multiple_comparisons: cluster_fwe
  outcome_timing:
    type: status_at_assessment
    interval: Cross-sectional chronic status; not longitudinal recovery or treatment
      response
  notes: Group association; not validated individual prediction. Keep shared-cohort
    provenance. Atlas overlap cannot establish disconnection of an individual tract.
  target: phonological_recognition
  claim: The phonological-recognition factor was associated with left auditory/posterior
    temporal and parietal tissue integrity including Heschl, planum temporale, middle/posterior
    superior temporal, angular and posterior supramarginal regions. Smaller similarly
    located clusters were reported after volume adjustment, with the threshold discrepancy
    retained.
  citation: '@Alyahya2018NounVerb'
  source_passages:
  - section: Source passage P9-S2-C6
    page: 9
    quote: 'Performance on the

      phonological recognition factor was uniquely associated with the left

      posterior superior temporal gyrus, Heschl''s gyrus (including H1 and

      H2), and posterior superior and inferior temporal gyri.'
    supports: claim
  - section: Main PDF page 3 (agent source check)
    page: 3
    quote: 'Forty-eight stroke patients (single left ischaemic or haemorrhagic

      stroke) with chronic aphasia participated in this study (34 males and 14

      females).

      The

      Boston

      Diagnostic

      Aphasia

      Examination

      (BDAE:

      Goodglass and Kaplan, 1983) was administered to each participant, and

      their aphasia was classiﬁed using the BDAE standard aphasia classiﬁ-

      cation criteria. Their age ranged between 44 and 87 (Mean = 63.31,

      SD = 11.8)

      and

      educational

      level

      varied

      from

      9

      to

      19 years

      (Mean = 12.58, SD = 2.5). Participants were recruited from the North

      West of England via stroke community support groups and speech and

      language therapy services. They were recruited on the basis that they

      had a single left hemispheric stroke and were at least 12 months post-

      stroke. All participants were native English speakers with normal or

      corrected-to-normal hearing and/or vision. Participants were not se-

      lected based on their neuropsychological proﬁle or lesion location, and

      no restrictions were placed according to aphasia severity or classiﬁca-

      tion, in order to sample the full range of severities and classiﬁcations of

      aphasia. The exclusion criteria included any contraindications for MRI

      scanning, being pre-morbidly left-handed and having more than one

      stroke or any other signiﬁcant neurological conditions. Demographic

      details on all participated are available in Table 1. Informed consent

      was obtained from all participants prior to participation under approval

      from the local ethics committee.

      '
    supports: sample
  - section: Main PDF page 6 (agent source check)
    page: 6
    quote: 'behavioural data. Several VBCM analyses were conducted. First, noun

      and verb scores were analysed separately to identify the neural corre-

      lates associated with performance on noun versus verb production and

      comprehension. Individual scores on these tests (noun naming, verb

      naming, noun picture-to-word matching, and verb picture-to-word

      matching) were entered into separate analyses. Secondly, noun and

      verb scores on naming and picture-to-word matching tests were

      summed for each patient, to generate an overall naming and picture-to-

      word matching scores. These two measures were analysed separately, to

      identify the neural correlates associated with naming versus compre-

      hension. These results were thresholded at p = 0.0005 voxel-level,

      cluster-level corrected using family-wise error (FWE) p < 0.05. This

      stringent threshold was used, in order to increase the speciﬁcity of the

      large clusters measured with each condition when they were examined

      in a separate model. Thirdly, whole brain direct contrasts were con-

      ducted between: (i) noun versus verb naming; (ii) noun versus verb

      picture-to-word matching; and (iii) naming versus picture-to-word

      matching. These direct contrasts were performed in order to identify

      regions that are uniquely associated with performance on one test over-

      and-above the other. Finally, patients'' factor scores obtained from the

      PCA (of the entire aphasiological and neuropsychological assessments

      including the noun and verb measures) were entered simultaneously

      into a VBCM analysis. The identiﬁed clusters indicate where tissue

      concentrations uniquely correlate with a given factor over-and-above

      the other factors. This was done to identify the neural correlates of the

      extracted language and cognitive aphasia domains. As these factors are

      orthogonal, this analysis could either be done in one step with all fac-

      tors entered simultaneously, or in several steps where each factor is

      entered in a separate model. The former method was followed to reduce

      the number of analyses, and it is believed that a single model that

      captures all (or as much) behaviours as possible is more elegant. The

      standard threshold of p = 0.001 voxel-level, cluster-level corrected

      using FWE p < 0.05 was used in the direct contrasts and the PCA-

      VBCM analyses, when several measures were entered simultaneously in

      the same model, as these eﬀects are expected to be more subtle. The

      results of these VBCM analyses indicate which voxels'' variation in tissue

      concentration corresponds to the variance in a given measure or factor

      score, while controlling for variation of other factors if included in the

      same model.

      All VBCM analyses were carried out using multiple regression

      models on T1-weighted images, and test measures or PCA-factor scores

      entered as regressors of interest. Moreover, each patient''s lesion volume

      (proxy of neurological severity) obtained from the output of the auto-

      mated lesion identiﬁcation procedure (Seghier et al., 2008) was entered

      as a covariate in subsequent VBCM analyses at the standard threshold of

      p < 0.001 voxel-level and cluster corrected using FWE p < 0.05. It is

      important to notice, however, that by partialling out lesion volume

      there is a high risk for type II error. Hence, all VBCM analyses were

      performed and reported in this paper once with the behaviours of in-

      terest only and once with a correction for lesion volume. This protocol

      was followed in order to account for both type I and type II errors. All

      anatomical results are described using labels based on the Harvard-

      Oxford atlas in MNI space (Desikan et al., 2006) and natbrainlab white

      matter connections atlas based on diﬀusion tensor tractography (Catani

      et al., 2012). All images were constructed using MRIcron (Rorden et al.,

      2007).

      '
    supports: method
  - section: Main PDF page 11 (agent source check)
    page: 11
    quote: '3.2.4. Eﬀect of lesion size

      Given that some cortical regions are more likely to be damaged after

      MCA stroke than others (Phan et al., 2005), lesion volume was included

      (see Methods) as a covariate in subsequent VBCM analyses. When

      adding lesion volume to each of the verb and noun processing analyses

      (verb naming, noun naming, verb comprehension, and noun compre-

      hension), even using a more liberal threshold (p = 0.005 voxel-level

      and p < 0.05 FWE-corrected cluster level), the verb naming and verb

      comprehension clusters dropped out of signiﬁcance; whereas smaller

      clusters were identiﬁed for noun naming (cluster size = 1373 voxels) in

      the left angular gyrus, posterior supramarginal gyrus, and superior

      lateral

      occipital

      cortex;

      and

      for

      noun

      comprehension

      (cluster

      size = 1359 voxels) in the left inferior lateral occipital cortex, occipital

      fusiform cortex, temporal occipital fusiform cortex and posterior in-

      ferior temporal gyrus. Indeed, lesion volume correlated with beha-

      vioural performance on all four measures (verb naming: r = 0.65, verb

      picture-to-word matching: r = 0.67, noun naming: r = 0.62, and noun

      picture-to-word matching: r = 0.56, p < 0.0001).

      In contrast, when adding lesion volume to the PCA-VBCM, the

      clusters remain signiﬁcant. This outcome supports the proposal that

      PCA generates statically independent components, and improves power

      by extracting factors of interest and removing sources of noise in ex-

      cluded factors (see Butler et al., 2014; Halai et al., 2017). Results are

      shown in Fig. 5b. Three of the ﬁve components did not signiﬁcantly

      correlate with lesion volume [phonological production (r = 0.22,

      p = 0.12); phonological recognition (r = 0.18, p = 0.21); and executive

      function (r = 0.14, p = 0.33)], and therefore controlling for lesion vo-

      lume did not have a signiﬁcant eﬀect on the neural correlates identiﬁed

      from the previous analysis conducted without accounting for lesion

      volume, as the clusters were smaller in size but they covered the same

      regions. The remaining two factors did correlate with lesion volume

      and thus partialling out this variable had some eﬀect on the lesion

      correlates. Firstly, the neural correlates for the semantic factor (corre-

      lation with lesion volume: r = 0.37, p = 0.01) showed a reduction in

      cluster size and were limited to the left superior and inferior lateral

      '
    supports: confounders
  - section: Main PDF page 12 (agent source check)
    page: 12
    quote: 'occipital cortex, precuneus, and occipital fusiform gyrus. Secondly,

      there were no signiﬁcant clusters remaining for the ﬂuency factor

      (correlation with lesion volume r = 0.59, p < 0.0001).

      '
    supports: confounders
  - section: Main PDF page 12 (agent source check)
    page: 12
    quote: 'Table 6

      Neural correlates of signiﬁcant clusters and peak MNI coordinates related to
      language and cognitive factors extracted from PCA with and without accounting
      for lesion volume.

      Principal component factor

      Location

      Cluster size (voxels)

      Z

      MNI co-ordinate

      x

      y

      z

      Factor 1: Phonological production

      Posterior segment of arcuate fasciculus

      Angular gyrus

      Parietal operculum cortex

      Posterior supramarginal gyrus

      Inferior longitudinal fasciculus

      3905

      4.51

      4.41

      4.30

      3.85

      3.79

      −40

      −34

      −32

      −50

      −34

      −44

      −54

      −36

      −46

      −46

      12

      24

      22

      40

      0

      Factor 2: Semantics

      Superior lateral occipital cortex

      Precuneus cortex

      Inferior longitudinal fasciculus

      Anterior temporal fusiform cortex

      Anterior inferior temporal gyrus

      Posterior inferior temporal gyrus

      Posterior middle temporal gyrus

      Anterior middle temporal gyrus

      Temporal pole

      8326

      5.53

      5.01

      4.67

      4.67

      4.28

      4.12

      4.04

      3.90

      3.78

      −28

      −18

      −38

      −38

      −44

      −46

      −44

      −48

      −42

      −74

      −56

      −8

      −8

      −10

      −42

      −58

      −6

      4

      14

      26

      −20

      −22

      −32

      −14

      −2

      −26

      −26

      Factor 3: Fluency

      Central opercular cortex

      Post-central gyrus

      Pre-central gyrus

      Anterior segment of arcuate fasciculus

      6008

      4.78

      4.48

      3.58

      3.30

      −66

      −66

      −50

      −37

      −6

      −14

      −4

      −19

      8

      16

      40

      25

      Factor 4: Phonological recognition

      Planum temporale

      Middle temporal gyrus

      Heschl''s gyrus

      Angular gyrus

      Posterior supramarginal gyrus

      Posterior superior temporal gyrus

      4088

      4.42

      4.31

      3.96

      3.40

      3.36

      3.32

      −60

      −54

      −52

      −46

      −46

      −46

      −30

      −44

      −20

      −52

      −48

      −38

      8

      6

      6

      20

      14

      6

      Factor 5: Executive functions⁎

      Superior frontal gyrus

      Paracingulate gyrus

      Supplementary motor areas

      pre-central gyrus

      1085

      3.65

      3.36

      3.27

      2.96

      −22

      −6

      −10

      −12

      20

      30

      −8

      −16

      52

      32

      52

      48

      Results threshold p = 0.001 voxel-level, cluster-level corrected using FWE p
      < 0.05.

      ⁎ Reduced threshold to p = 0.005 voxel-level, cluster-level corrected using
      FWE p = 0.05, as the clusters do not survive the FWE-cluster level p < 0.05
      correction at p = 0.001 voxel-

      level.

      '
    supports: statistics
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-18'
relationship_review:
  paper: Alyahya2018NounVerb
  proposal_id: U058
  review_status_sha256: da0786b392643e80d95b85068f6c3b1b98846eac9822c48bbce15ac9082825c0
  review_binding:
    version: relationship-review-v4
    input_hashes:
      pdf: 5ed1039a01ab3cfc667a78c7b356bbe093a4c29145b49409590d3fd9a46f60f5
      A/passages.json: 587767c4e7f2cd584b6e3e9a71acded9da6c0791b94cf81936f07162650fd8aa
      A/raw.json: 03af4378c8b55ee1b61f0354d8a5011fe02f0a4c94b67caf19bafd970c84198f
      A/source-units.json: 043d2ac9597f656ebbc30829a3acec9d3e4c42d048f7cb173206a910adbd1367
      A/full-source-units.json: 76588e7657118e33c3e174c48869bb8a7660db3aae884f0ba4efdd43296e1f0c
      A/meta.json: 0f1608e835dfa080463473a4993739c013854674dcfcdde676693e3c8690f4e3
      A/table-images/page-12.png: 00d46e259c787fc3b2c99f3575a91195a3f618aa76e77cdc69ec2762f3935ea9
      A/table-images/page-10.png: 52280f11317c2e744735558cbbef6c2e66a869ebd9880c1d398e04404b0fa512
      A/table-images/page-11.png: a724833ccf8a2face7b6489dd1c55c238184f786135157c8ff3891d142d3ec9a
      A/table-images/page-3.png: 505b5826f773a4b856208ae0872961f4ab6d9a9c0923c12971e4720bf2d9e601
      A/table-images/TABLE-4-page-8-1.png: 572b30743e67a24070ca93db5be7ae958972327b64d779f5a9ddf80d08644edc
      A/table-images/page-7.png: edb70d9f67b70dbe2896170e611db913e585d5d3f437ee0a7132b5b31a8cd547
      A/table-images/page-4.png: 3e28ad405144084720d6ec5a24147f5505750804f8f4296c095f0367f64a2cc9
      A/table-images/TABLE-1-page-4-1.png: 9f24eab1181bb2eb5b3af2bbf160c897711c1e9ba6a4ff0479a6087fed949006
      A/table-images/page-9.png: 32f06ac42d993ffb42799d72701ba35cb1ab66673b4230861731ac943851f600
      A/table-images/page-8.png: 1068ecadba52f42de0a199912a0ea52748156c8cb7a5b9e6cfd940ec7f03e830
      A/table-images/TABLE-5-page-11-1.png: b62189fe93bb4279098e7cd1e2c2047658be69865318bbee19002a5f9c106484
      A/table-images/TABLE-2-page-4-2.png: e2dd15ad3b9e5f1220d4e1f889bb4409d7c727fed652c0802c39c0e1ecbbf62c
      A/table-images/manifest.json: e5b49966ac2fc09af6533a36e451d17aa653657bdf08386e5ab1d09b4fabdae4
      A/table-images/TABLE-2-page-3-1.png: 89566f7689f2fba2be1a0faf260857ebb066a744879395d25b23dabdf1b6eb03
      A/table-images/TABLE-5-page-10-1.png: 25c88aeab348c376e99f760491723c8906cead29efaab1a927816cf2f3839f1c
      A/table-images/TABLE-3-page-7-1.png: 17956a90396dcc2fa98737e9892f75aa12b4257ee0fa9e72447e7b2564c8a514
      A/table-images/TABLE-6-page-9-1.png: 1a3b8a6e3f9a2335df9609199b821799c26535a78eed98726d3fad2df7597a5c
      A/table-images/TABLE-6-page-12-1.png: afc993f8ef65d38b7af929830add6ce8bc9c8d8cd00573a751ff9a8f996d9c7d
      A/clauses/window-11/raw.json: bf8e491f1894c8910d71a6189f036917e40c3e3798d0a63b8a8a11b6c3a100a6
      A/clauses/window-11/prompt.txt: 46bad234dbc5ddaf04a09afe36bf6ffe1ac1ab579dde05496b39982db0e1b8bb
      A/clauses/window-11/meta.json: b9534c3c2ce9852e6e6c291141562d84d9468ea845d47c8f2736544b9003edd7
      A/clauses/window-10/raw.json: f5526453675d23f7471686b1b1859235d646e094abc4492f3ea0243b22e4d36b
      A/clauses/window-10/prompt.txt: 4d9dfcef114ed548f875d30b20e01f35f2925e576145896e1cbf3f346acb833d
      A/clauses/window-10/meta.json: 65f722fe2acbde602983531dfcf9a3f38219a309cb28fefda5032756fcd2ca10
      A/clauses/window-03/raw.json: 4516896831f82c321ef732dc39b68625b846890590fb968d86770bcedbd2c2cc
      A/clauses/window-03/prompt.txt: c04fe89751793784e90e41d4c86604b21275ffab7200d3b22cfadb9174ed843b
      A/clauses/window-03/meta.json: 327d667412cc2aa294369f3f46e65406bb2346761a90979f84360089c8a8c76f
      A/clauses/window-04/raw.json: 4b1c37e310f17f0d2fda4be5774547125f9e24650d1653d03c6a2af077969d33
      A/clauses/window-04/prompt.txt: 1ba151876c11fd3ffc9e3db31fb16f9647723976b0555de6995f7a6cc3dc9c3f
      A/clauses/window-04/meta.json: 737b9081dec67c8ed8d3484e4518b446e3b460c6e5e224216344933f53a217c7
      A/clauses/window-05/raw.json: 5c925f6eaccd988b25058b3abbcc7ab8c6d1156bf4a69ed0694906d1adc56934
      A/clauses/window-05/prompt.txt: b9b72441dea55d64fda5d43c509f46389482fcebbe8a1ac727189015fd5ad442
      A/clauses/window-05/meta.json: 8448c6eed591446e8fc9665a6b32d1106226c215f328a5270e7776523721ff33
      A/clauses/window-02/raw.json: 900f29a0a2c5012449948712bb560a74bcf448a4963b317d56abb9a0331e6781
      A/clauses/window-02/prompt.txt: cb2737a8ad1e0fd7e638afa62dd73527f722b5869fc22c08ee96967ec1896302
      A/clauses/window-02/meta.json: 6eaa3c32bbbeb19aef7ab37c8e5ec4fc63ecd001552a51af4e391ccfec810936
      A/clauses/window-12/raw.json: 9ffa91f90b4f95c0a6043c2a4e65d6de2ac7f7242b8d93d616a4df88968ced5b
      A/clauses/window-12/prompt.txt: 7feee6c6d2fff122ac31d84d5b333c3c580dfa08bd7623a51941a0e985392352
      A/clauses/window-12/meta.json: 1f1fe8e9ff8a5be7e1f9c2f17c0bb9993acb77e007e605c7d94aa81ce96b701e
      A/clauses/window-13/raw.json: ce8f5d9877d1d1473a207a22838dd00617d21b7033736a20f49dafe3c9920bfc
      A/clauses/window-13/prompt.txt: 6138dc1d7bc27580ec9972ce95cd58650e7902c33416456d38cc7bbf3eb95faa
      A/clauses/window-13/meta.json: 26aed1abc1941e8bb88e2e45fcbb1ff94b8cc64d2a370f162d3bb5b499c2fd66
      A/clauses/window-09/raw.json: aa745c318967cc0c471016f71cec72bddf07a89d67b1c8e48ab201a5d934e5a9
      A/clauses/window-09/prompt.txt: ecfd930f3c16457f0baa73039590dc812f3fa213d8917d5486198699aab615c9
      A/clauses/window-09/meta.json: 7a0110513ad8fec3768ca4494fabac3da6e774414820647d1bc52b701efaa760
      A/clauses/window-07/raw.json: 4e3fdc29ec42fdc7c163d49ded540717e14a20a1e2de0e955087846b272f8be5
      A/clauses/window-07/prompt.txt: 1945b065446ce58fb8d1cd8183515e68648c85c575d3269d987f75d6240909e3
      A/clauses/window-07/meta.json: 8d1bd9ec6a72b6c99cdc1e3249dc9045e992643cc44f734ba24700b73cd1366b
      A/clauses/window-01/raw.json: 714ab684b42ce589b86be2716d2d44811a87391b0f4ea1b74cff2b1162565ee2
      A/clauses/window-01/prompt.txt: 0c8117f473f708962dc50f4d90d5c9b5a02c231d91b3122a17f1aa45c89184a4
      A/clauses/window-01/meta.json: a4d01ae526e714c6c30fd012dd0a2223a4932585c5f190fdac1858ed2ea19b4d
      A/clauses/window-06/raw.json: e18016e14cf8a9db9b90c17db95384b575f4dff988b8276cbf41cf2b2377eff4
      A/clauses/window-06/prompt.txt: a9dcaed9fc3ff90c241a89fb8c162407780d26733a1cea14ceae94bc8b4cdb82
      A/clauses/window-06/meta.json: 789e0af42d502f032afd81ef4234562509784703c4ba7829c52800ca5c8076bc
      A/clauses/window-08/raw.json: 85d6192460791724a91f0d0466b7ac0bf54c2fa4ff33ecf5842fe3db5d8c3dd1
      A/clauses/window-08/prompt.txt: 1b1e5881016314667ac7ce0f3c948db2f50b01a26691f11835a23c0c541f60a9
      A/clauses/window-08/meta.json: e21f01676047c2f031ecba22349988d073ba363799fad22dc37d168deadfb52f
      A/tables/TABLE-4-page-8-5/raw.json: 9e910888ccca977aa970dd347675081039e995e586f5457d77d7e6acafa73462
      A/tables/TABLE-4-page-8-5/prompt.txt: 3c615fe494781978c1eb93c60c82c9a22fe04773d71d2e21d2ff7468261bc25f
      A/tables/TABLE-4-page-8-5/meta.json: 6aec5302be138042c8aec1ee5d0e3ba5d8ebbab007b29a6f9c4b101f988c5902
      A/tables/TABLE-2-page-3-1/raw.json: 9ef3e3f81d1df7bcb0a0c7e6229929a97c706636847ceecc15878ad2eeaba1f1
      A/tables/TABLE-2-page-3-1/prompt.txt: 04954ff60ad5aefb451d9d14ea966cc543aab6d75d93ee0fa7bd5d09080ece97
      A/tables/TABLE-2-page-3-1/meta.json: c28365fc7dfb77b14bf27855f22cfa7124b5d4789955490f6dac7c60862e8b0a
      A/tables/TABLE-5-page-10-7/raw.json: 068e0942eb1ac60a75bbeea6d37eed0cd8de455b08e8788aacc0a80eac157e55
      A/tables/TABLE-5-page-10-7/prompt.txt: 2cc8dc0948f6cdcedde76fc45dfb6e8d759f97651c0f82b13ddc49916c83e769
      A/tables/TABLE-5-page-10-7/meta.json: c363d553f36a5f0e5b636b19f046d7b63490f91bd42989b2d5a37ede2da945e0
      A/tables/TABLE-1-page-4-2/raw.json: ece98f28a77e1f7e303185a9818d8985cf0ff3b8ea6fc8d893d1e580b62be55e
      A/tables/TABLE-1-page-4-2/prompt.txt: 51cf4940fb416e8eb2a06cfe0ed9d31b4c397b43e178b707d26f8a8f7a4aab1a
      A/tables/TABLE-1-page-4-2/meta.json: bb6607f73393b224e008a4c75bda9fbb0a3b38b0c5577efc7a40e2f8841efd72
      A/tables/TABLE-6-page-12-9/raw.json: 344602f1ab2dd90a652c26e618bc6a5ad1b1560ee08247b0a7b0ebd3addfee63
      A/tables/TABLE-6-page-12-9/prompt.txt: ce4905b5a7289aec35f8abeef7a7d066e9ead7e28e05e00e1e41607eca1a1450
      A/tables/TABLE-6-page-12-9/meta.json: 7b00ba2ec60ebe9a4f6fa103529c96269f757ba8ab688ec1c4008ce8f76da387
      A/tables/TABLE-3-page-7-4/raw.json: 573ae390b7387d3262ded4383bfe195face35895785daef40d740d29bdb403b1
      A/tables/TABLE-3-page-7-4/prompt.txt: 84b525fb51abb42ba44a1396f0bb37c61c830ecf5b5e4324876d1e0d0a25f5d9
      A/tables/TABLE-3-page-7-4/meta.json: c83c90cfb0381a73babd049fb35bd302d3af0183e0ddad74f35520d7a227d8ea
      A/tables/TABLE-5-page-11-8/raw.json: 64b93e6cf82dd23bb42330318c255b3a8b16fe69995158bc68d0280d56703117
      A/tables/TABLE-5-page-11-8/prompt.txt: db111f04f2f7200cd02283cf633cd91855f6e0f4c969a5bf198ebb82155c5db6
      A/tables/TABLE-5-page-11-8/meta.json: 68c78f86b7f4e0aa27e21977094bde30999378c04cc433080533d49c7ff004e3
      A/tables/TABLE-2-page-4-3/raw.json: 343a58878ca9be7c9905fc6cff87591e03b78bc4afab70ef3c3058e10c640731
      A/tables/TABLE-2-page-4-3/prompt.txt: 1d52440d95ab914c1fa4d380a12d547f10eaa8e143241bd52d9409d047cb7ebd
      A/tables/TABLE-2-page-4-3/meta.json: 2a30afcfef03f95a3e7118bab718e02ce4cbe1c5c4d5e321ce499f1ec6d596dd
      A/tables/TABLE-6-page-9-6/raw.json: 9983ad30dfd3c79b78f83f4634c105f0d83ed39b3815e052c6159f496ba91a27
      A/tables/TABLE-6-page-9-6/prompt.txt: f94accc1f4484ef289d3a63bff233c0ae71c1ecc6e71d400d89ccdbdcdf2f4d1
      A/tables/TABLE-6-page-9-6/meta.json: 72be13cb20a1c2bcf075765546b30ab5716bb607f0bf240c64de95329605d607
      B/passages.json: 587767c4e7f2cd584b6e3e9a71acded9da6c0791b94cf81936f07162650fd8aa
      B/raw.json: d7def0217f3ce35fac04b36f4be11dbb39321227b09da386c16c4c496a1d82dd
      B/source-units.json: 043d2ac9597f656ebbc30829a3acec9d3e4c42d048f7cb173206a910adbd1367
      B/full-source-units.json: 76588e7657118e33c3e174c48869bb8a7660db3aae884f0ba4efdd43296e1f0c
      B/meta.json: 2b3a6bc9cf8256cabbba78a87da9f852b8d8533e7ee4aa45556cdaa6331151b1
      B/table-images/page-12.png: 00d46e259c787fc3b2c99f3575a91195a3f618aa76e77cdc69ec2762f3935ea9
      B/table-images/page-10.png: 52280f11317c2e744735558cbbef6c2e66a869ebd9880c1d398e04404b0fa512
      B/table-images/page-11.png: a724833ccf8a2face7b6489dd1c55c238184f786135157c8ff3891d142d3ec9a
      B/table-images/page-3.png: 505b5826f773a4b856208ae0872961f4ab6d9a9c0923c12971e4720bf2d9e601
      B/table-images/TABLE-4-page-8-1.png: 572b30743e67a24070ca93db5be7ae958972327b64d779f5a9ddf80d08644edc
      B/table-images/page-7.png: edb70d9f67b70dbe2896170e611db913e585d5d3f437ee0a7132b5b31a8cd547
      B/table-images/page-4.png: 3e28ad405144084720d6ec5a24147f5505750804f8f4296c095f0367f64a2cc9
      B/table-images/TABLE-1-page-4-1.png: 9f24eab1181bb2eb5b3af2bbf160c897711c1e9ba6a4ff0479a6087fed949006
      B/table-images/page-9.png: 32f06ac42d993ffb42799d72701ba35cb1ab66673b4230861731ac943851f600
      B/table-images/page-8.png: 1068ecadba52f42de0a199912a0ea52748156c8cb7a5b9e6cfd940ec7f03e830
      B/table-images/TABLE-5-page-11-1.png: b62189fe93bb4279098e7cd1e2c2047658be69865318bbee19002a5f9c106484
      B/table-images/TABLE-2-page-4-2.png: e2dd15ad3b9e5f1220d4e1f889bb4409d7c727fed652c0802c39c0e1ecbbf62c
      B/table-images/manifest.json: a3a908269280172e0b6a9641b05eade9f7112034f085720484393be726af921d
      B/table-images/TABLE-2-page-3-1.png: 89566f7689f2fba2be1a0faf260857ebb066a744879395d25b23dabdf1b6eb03
      B/table-images/TABLE-5-page-10-1.png: 25c88aeab348c376e99f760491723c8906cead29efaab1a927816cf2f3839f1c
      B/table-images/TABLE-3-page-7-1.png: 17956a90396dcc2fa98737e9892f75aa12b4257ee0fa9e72447e7b2564c8a514
      B/table-images/TABLE-6-page-9-1.png: 1a3b8a6e3f9a2335df9609199b821799c26535a78eed98726d3fad2df7597a5c
      B/table-images/TABLE-6-page-12-1.png: afc993f8ef65d38b7af929830add6ce8bc9c8d8cd00573a751ff9a8f996d9c7d
      B/clauses/window-11/raw.json: 66623b9ffbdcd0e6c409c4ecfa0c4ffb6646a4c73e3b6303d01313ea473ffe84
      B/clauses/window-11/prompt.txt: 46bad234dbc5ddaf04a09afe36bf6ffe1ac1ab579dde05496b39982db0e1b8bb
      B/clauses/window-11/meta.json: 98e0790c14afc8a5a8b13f7dd25fe9eb1ebf04d9b894ae5ef8c4d4466959f41a
      B/clauses/window-10/raw.json: 0e5f010d804081cd2638ee04fb873076742e9351897b3540b11e6c1f123cfa26
      B/clauses/window-10/prompt.txt: 4d9dfcef114ed548f875d30b20e01f35f2925e576145896e1cbf3f346acb833d
      B/clauses/window-10/meta.json: 965534a9c1d135312ebfcdc7c925f64a169f517e0114ba38892c69bb908f9cc1
      B/clauses/window-03/raw.json: 5916df5d67b65174e5140714f93a7588fac6b2da94dd32058675ac54839c8fcf
      B/clauses/window-03/prompt.txt: c04fe89751793784e90e41d4c86604b21275ffab7200d3b22cfadb9174ed843b
      B/clauses/window-03/meta.json: 4ae097b22c1472e31650b0a5e8eae1a844bdf26aae4417f862c6ce7ec7e3b3f6
      B/clauses/window-04/raw.json: 9cfd8aa02ad74a9741a923165516fab538320e19cc2d207db7e3a5810b4a176a
      B/clauses/window-04/prompt.txt: 1ba151876c11fd3ffc9e3db31fb16f9647723976b0555de6995f7a6cc3dc9c3f
      B/clauses/window-04/meta.json: e6f04fc1d524a9603a6e2a050760dc6ed43fc35593fc21b1ae55c377e30bf76e
      B/clauses/window-05/raw.json: 837c7de1d5415a16b7893d0fdf81382e5c667680764c6db98e7e01fbb5185a86
      B/clauses/window-05/prompt.txt: b9b72441dea55d64fda5d43c509f46389482fcebbe8a1ac727189015fd5ad442
      B/clauses/window-05/meta.json: a13fc6b4d4737fdc8713b4d6124d41b40700048b6211442d320d2646baa5c5e3
      B/clauses/window-02/raw.json: 6d9c7aebc57e53c5e855de22d103e01e469156945feff148a4cfa09efdcca1f7
      B/clauses/window-02/prompt.txt: cb2737a8ad1e0fd7e638afa62dd73527f722b5869fc22c08ee96967ec1896302
      B/clauses/window-02/meta.json: 6b6b9959d3814d094c2aa81245a591b8907fa9f3842f7279098887120e2f3a24
      B/clauses/window-12/raw.json: 601ca631a158cecf47bc61144a4f4fccdfabebcdcc5c7be09919b088bd532647
      B/clauses/window-12/prompt.txt: 7feee6c6d2fff122ac31d84d5b333c3c580dfa08bd7623a51941a0e985392352
      B/clauses/window-12/meta.json: d5065b51c5b1e1d45fe35f5e06b1dfa8ad8f58500b761c912913271d45875613
      B/clauses/window-13/raw.json: ce8f5d9877d1d1473a207a22838dd00617d21b7033736a20f49dafe3c9920bfc
      B/clauses/window-13/prompt.txt: 6138dc1d7bc27580ec9972ce95cd58650e7902c33416456d38cc7bbf3eb95faa
      B/clauses/window-13/meta.json: d981485e25b670f887a66658b1c373006060dbf77fe3b3782cc80bc92459b27c
      B/clauses/window-09/raw.json: baa2c73d13e1d77b3b09fb801a8a4ccd150a29500d27fdebd4d99bb972946ad1
      B/clauses/window-09/prompt.txt: ecfd930f3c16457f0baa73039590dc812f3fa213d8917d5486198699aab615c9
      B/clauses/window-09/meta.json: 5c6af43e81e6256afe62861db3b7792bcdeb8b94f95120be6bbc798e16c6750b
      B/clauses/window-07/raw.json: 12139534bdf77e19821452df735c09db87451812fcbfedbbff2d21355d15514b
      B/clauses/window-07/prompt.txt: 1945b065446ce58fb8d1cd8183515e68648c85c575d3269d987f75d6240909e3
      B/clauses/window-07/meta.json: bab719d8a9f95d450533ff7ee70c71d830890825ff0f333efdf0984d43d66dbb
      B/clauses/window-01/raw.json: 7bd56887233d1fcb24211513a57d4aca0e168a484dc9b59d36b97881041184f4
      B/clauses/window-01/prompt.txt: 0c8117f473f708962dc50f4d90d5c9b5a02c231d91b3122a17f1aa45c89184a4
      B/clauses/window-01/meta.json: 0658a44352c9f8c1bd7c642ea640f1cb09b10d72912e14ee5e699987352a2df3
      B/clauses/window-06/raw.json: 9e1a4300a21a4a19f878b8fe36762b914d4117ace3763d8ec96e2a3025e9a960
      B/clauses/window-06/prompt.txt: a9dcaed9fc3ff90c241a89fb8c162407780d26733a1cea14ceae94bc8b4cdb82
      B/clauses/window-06/meta.json: 42d66078444faf80658bc9c38f3451b3b55ab14a16791f49fdd75d382098e460
      B/clauses/window-08/raw.json: 5a41a460fb9b78ea4c83dd3e1ef7a52ce46ed26bf83ae0dc100015227a18b0fe
      B/clauses/window-08/prompt.txt: 1b1e5881016314667ac7ce0f3c948db2f50b01a26691f11835a23c0c541f60a9
      B/clauses/window-08/meta.json: 595f1bdbcb0828b3a4d82810213574db1955176c9e5a428387a08f03c75d4385
      B/tables/TABLE-4-page-8-5/raw.json: afcb486a159c09e183b3d0058d97fde801ace012eda6281349cfd6521a4278c9
      B/tables/TABLE-4-page-8-5/prompt.txt: 3c615fe494781978c1eb93c60c82c9a22fe04773d71d2e21d2ff7468261bc25f
      B/tables/TABLE-4-page-8-5/meta.json: 817a9fea5df974898e605ac12cf2c67b489ba087918ba5d697350723e449d565
      B/tables/TABLE-2-page-3-1/raw.json: 57c3ecbcf16a3976a6d7b180dd005f6fa02cef2f3a3351027309435e94ac33a0
      B/tables/TABLE-2-page-3-1/prompt.txt: 04954ff60ad5aefb451d9d14ea966cc543aab6d75d93ee0fa7bd5d09080ece97
      B/tables/TABLE-2-page-3-1/meta.json: 81b5470280f0db5630a9ea577868718d9931a04cced204149d9925c58c099ba9
      B/tables/TABLE-5-page-10-7/raw.json: f231764ce4f3a1592745313cdd247bd08933211a74ea4badf220b4b0eb221267
      B/tables/TABLE-5-page-10-7/prompt.txt: 2cc8dc0948f6cdcedde76fc45dfb6e8d759f97651c0f82b13ddc49916c83e769
      B/tables/TABLE-5-page-10-7/meta.json: ae3504b97e32c6672f3575794948d989303cb05a53beb7c781eecb6978e4f897
      B/tables/TABLE-1-page-4-2/raw.json: 5ea4ef011a51c688073f631c0de4c60703d0544233f1a37d388e712f6b74e408
      B/tables/TABLE-1-page-4-2/prompt.txt: 51cf4940fb416e8eb2a06cfe0ed9d31b4c397b43e178b707d26f8a8f7a4aab1a
      B/tables/TABLE-1-page-4-2/meta.json: 7eac5d336f1f3b79f283199a5634690fbefc8677d78fe540ccb6eab15ae6f178
      B/tables/TABLE-6-page-12-9/raw.json: 08c2d5b53bedae996744e4e0debaa66d163b94e6cad6c7d9020f8ec148b11f91
      B/tables/TABLE-6-page-12-9/prompt.txt: ce4905b5a7289aec35f8abeef7a7d066e9ead7e28e05e00e1e41607eca1a1450
      B/tables/TABLE-6-page-12-9/meta.json: 085779e0c70d7c61e3ffb0432ddf53de61955fc03856a899afb9ea113972f008
      B/tables/TABLE-3-page-7-4/raw.json: fafb4254e929474d78296f61797001524f3cb9a6952d81c521e81b0a40d16235
      B/tables/TABLE-3-page-7-4/prompt.txt: 84b525fb51abb42ba44a1396f0bb37c61c830ecf5b5e4324876d1e0d0a25f5d9
      B/tables/TABLE-3-page-7-4/meta.json: 5ab04fcdc4d93448f98cf94ca33e2817bff8f4ee8bf138aef5a150ba35b34f9e
      B/tables/TABLE-5-page-11-8/raw.json: 157b1c123a777ddf0a4eb65e460c2b6b4ec3954c5a2e566208038afffd125d95
      B/tables/TABLE-5-page-11-8/prompt.txt: db111f04f2f7200cd02283cf633cd91855f6e0f4c969a5bf198ebb82155c5db6
      B/tables/TABLE-5-page-11-8/meta.json: 1004592ab89eca3061784a263462a9d9586e0bf2a2d648be7d78e9fbe8c1297d
      B/tables/TABLE-2-page-4-3/raw.json: 3bb468aa674c044b7c9736bf7ecff4a0d3ed49a55363e4d3aa8dca8c09f8d13f
      B/tables/TABLE-2-page-4-3/prompt.txt: 1d52440d95ab914c1fa4d380a12d547f10eaa8e143241bd52d9409d047cb7ebd
      B/tables/TABLE-2-page-4-3/meta.json: 944964d64847028ed815a56388174c8d252ff731164bfb05b7b9fc1b4a7d4763
      B/tables/TABLE-6-page-9-6/raw.json: d3aa15fe56d02ea8c79ff84805006277fc66743e182d5d5dce2c8e989fa1c55c
      B/tables/TABLE-6-page-9-6/prompt.txt: f94accc1f4484ef289d3a63bff233c0ae71c1ecc6e71d400d89ccdbdcdf2f4d1
      B/tables/TABLE-6-page-9-6/meta.json: d5a34e80c3c989cf3b8723931dd88312778d5891e85159e0b9df0f0870543d54
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
    - P9-S2-C6
    qualifier_ids: []
    context_ids:
    - P6-S2-C4
    table_ids: []
    exposure:
      text: phonological recognition factor
      source_id: P9-S2-C6
    outcome:
      text: left posterior superior temporal gyrus, Heschl's gyrus (including H1 and
        H2), and posterior superior and inferior temporal gyri
      source_id: P9-S2-C6
    relation: association
    effect_unit: individual
    result_status: reported_detected
    outcome_type: not_applicable
    direction: not_stated
    direction_source_id: ''
    origin: current_study
    label_match_candidates: {}
    id: U058
    flags: []
    linked_tables: []
    approved: false
    status: requires_source_review
    context_candidates:
    - P11-S1-C3
    - P14-S1-C9
    - P3-S2-C10
    - P3-S2-C11
    - P3-S2-C8
    - P3-S2-C9
    - P4-S1-C2
    - P4-S1-C3
    - P5-S2-C10
    - P5-S2-C11
    - P6-S1-C10
    - P6-S1-C11
    - P6-S1-C12
    - P6-S1-C13
    - P6-S1-C14
    - P6-S1-C15
    - P6-S1-C2
    - P6-S1-C3
    - P6-S1-C4
    - P6-S1-C5
    - P6-S1-C6
    - P6-S1-C7
    - P6-S1-C8
    - P6-S1-C9
    - P6-S2-C2
    - P6-S2-C3
    - P6-S2-C5
    - P6-S2-C6
    - P6-S2-C7
    - P6-S2-C8
    - P6-S2-C9
    - P7-S1-C9
    - P9-S1-C7
    - P9-S1-C8
    - P9-S1-C9
    - P9-S2-C10
    - P9-S2-C9
    - P9-S3-C2
    context_policy: Script-attached frame, Methods and nearby source passages; candidates
      are not confirmed analysis-specific controls
    conditional_or_conflicting_unit_ids: []
    digest: a656382096810103bc366b8de06e82f21db5328aad82c8d3c4dc3f3bfca1beb4
  audit:
    coverage_issues:
    - Result passage disposed without unit P1-S1-C11
    - Accounting without a linked unit P1-S1-C12
    - Accounting without a linked unit P1-S2-C5
    - Accounting without a linked unit P1-S2-C6
    - Accounting without a linked unit P1-S2-C7
    - Unaccounted source passage P1-S2-C7
    - Unaccounted source passage P1-S2-C5
    - Unaccounted source passage P1-S2-C6
    - Unaccounted source passage P1-S1-C12
    - Accounting without a linked unit P3-S4-C11
    - Accounting without a linked unit P3-S4-C12
    - Accounting without a linked unit P3-S4-C13
    - Accounting without a linked unit P4-S1-C4
    - Unaccounted source passage P3-S4-C11
    - Unaccounted source passage P3-S4-C13
    - Unaccounted source passage P3-S4-C12
    - Unaccounted source passage P4-S1-C4
    - Result passage disposed without unit P5-S3-C7
    - Result passage disposed without unit P5-S4-C5
    - Result passage disposed without unit P6-S3-C11
    - Result passage disposed without unit P6-S3-C13
    - Result passage disposed without unit P6-S4-C2
    - Accounting without a linked unit P6-S5-C1
    - Unaccounted source passage P6-S5-C1
    - Result passage disposed without unit P7-S1-C12
    - Result passage disposed without unit P8-S1-C10
    - Result passage disposed without unit P8-S1-C4
    - Result passage disposed without unit P8-S1-C5
    - Result passage disposed without unit P8-S1-C6
    - Result passage disposed without unit P8-S1-C7
    - Result passage disposed without unit P8-S1-C9
    - Result passage disposed without unit P8-S3-C2
    - Result passage disposed without unit P9-S2-C1
    - Result passage disposed without unit P9-S2-C2
    - Result passage disposed without unit P9-S2-C4
    - Result passage disposed without unit P11-S1-C1
    - Result passage disposed without unit P11-S1-C2
    - Result passage disposed without unit P9-S2-C10
    - Result passage disposed without unit P9-S2-C9
    - Result passage disposed without unit P9-S3-C2
    - Result passage disposed without unit P9-S3-C3
    - Result passage disposed without unit P12-S1-C1
    - Result passage disposed without unit P13-S3-C11
    - Accounting without a linked unit P14-S1-C8
    - Result passage disposed without unit P14-S2-C10
    - Result passage disposed without unit P14-S2-C8
    - Accounting without a linked unit P14-S2-C9
    - Unaccounted source passage P14-S2-C9
    - Unaccounted source passage P14-S1-C8
    unattached_null_or_qualifier_ids:
    - P7-S1-C12
    - P7-S1-C13
    - P9-S2-C1
    suppressed_nonrepresented_units: 27
    default_disposition_count_requires_completeness_check: 241
    unselected_timing_passages:
    - P1-S1-C8
    - P2-S3-C8
    - P3-S1-C5
    - P3-S2-C4
    - P3-S2-C6
    - P4-S1-C2
    - P5-S2-C10
    - P13-S1-C1
    personal_effect_slots_without_result_classification: []
    held_frame_selections:
    - slot: dependent_variable_statement
      source_id: P6-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C13
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
      source_id: P7-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S4-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    empty_frame_slots_require_confirmation:
    - validation
    - explicitly_not_adjusted
    unclassified_extraction_ids:
    - P2-S5-C1
    - P8-S2-C16
    table_review_required:
    - TABLE-1-page-4-2
    - TABLE-2-page-3-1
    - TABLE-2-page-4-3
    - TABLE-3-page-7-4
    - TABLE-4-page-8-5
    - TABLE-5-page-10-7
    - TABLE-5-page-11-8
    - TABLE-6-page-12-9
    - TABLE-6-page-9-6
    unlinked_tables:
    - TABLE-1-page-4-2
    - TABLE-2-page-3-1
    - TABLE-2-page-4-3
    - TABLE-3-page-7-4
    - TABLE-6-page-12-9
    - TABLE-6-page-9-6
    source_anomalies: []
    visual_review_required:
      scope: All main-paper figures and table crops
      note: Automatic crops and matching transcriptions do not certify visual completeness.
        Figures are not automatically interpreted.
      caption_candidate_units:
      - P5-S3
      - P5-S4
      - P7-S1
      - P7-S2
      - P7-S3
      - P8-S1
      - P8-S2
      - P9-S1
      - P9-S2
      - P9-S3
      - P11-S2
      - P12-S1
    approval: Not performed. Structural checks and model selections do not establish
      semantic correctness.
  study_frame:
    slots:
      analysed_sample:
      - P3-S2-C4
      - P4-S1-C8
      - P4-S2-C1
      - P5-S2-C11
      - P10-S1-C2
      recruited_sample:
      - P3-S2-C4
      - P3-S2-C7
      - P3-S2-C8
      - P4-S1-C8
      eligibility:
      - P3-S2-C8
      - P3-S2-C9
      - P3-S2-C10
      - P3-S2-C11
      imaging_provenance:
      - P5-S2-C10
      imaging_timing:
      - P5-S2-C11
      outcome_timing:
      - P3-S2-C8
      outcome_definition:
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C9
      - P6-S1-C11
      - P7-S1-C9
      - P7-S1-C11
      validation: []
      analysis_restrictions:
      - P6-S1-C7
      - P6-S1-C8
      - P6-S1-C14
      - P6-S1-C15
      - P6-S2-C2
      - P6-S2-C7
      - P11-S1-C4
      dependent_variable_statement:
      - P6-S1-C3
      - P6-S1-C4
      - P6-S1-C5
      - P6-S1-C6
      limitations:
      - P6-S2-C6
      - P14-S1-C9
      personal_factors:
      - P4-S1-C2
      - P4-S1-C3
      - P4-S1-C5
      - P4-S1-C6
      - P5-S2-C10
      tested_personal_effects:
      - P4-S1-C5
      - P4-S1-C6
      - P7-S1-C10
      - P7-S1-C11
      - P11-S2-C5
      - P11-S2-C6
      - P11-S2-C7
      adjustment_roles:
      - P6-S2-C5
      - P11-S1-C3
      explicitly_not_adjusted: []
      descriptive_personal_factors:
      - P3-S2-C6
      - P3-S2-C9
      - P4-S1-C2
      - P4-S1-C3
      - P4-S1-C8
      - P5-S2-C10
    outcome_type: status_at_assessment
    imaging_vs_outcome: concurrent
    validation_type: internal_cross_validation
    held_selections:
    - slot: dependent_variable_statement
      source_id: P6-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P6-S1-C13
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
      source_id: P7-S1-C9
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: dependent_variable_statement
      source_id: P7-S1-C11
      reason: Requires a Methods outcome definition; model selection retained for
        inspection only
    - slot: validation
      source_id: P3-S4-C10
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    - slot: validation
      source_id: P4-S1-C1
      reason: No validation-design cue; inspect the source rather than inferring a
        design
    policy: All slots and enums remain unverified. Held selections are not evidence
      of absence. Original response is preserved in frame/raw.json.
  approved: false
  source_check:
    checked_by: agent:codex
    date: '2026-11-18'
    approved: false
    pdf_sha256: 5ed1039a01ab3cfc667a78c7b356bbe093a4c29145b49409590d3fd9a46f60f5
    licence:
      category: cc
      label: CC BY 4.0
      url: http://creativecommons.org/licenses/by/4.0/
      version: published
      source: crossref
      doi: 10.1016/j.nicl.2018.01.023
      checked: '2026-10-30'
      consulted:
      - crossref
      - unpaywall
      - pdf
    checked_pdf_pages:
    - 1
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
    - 14
    visual_pages:
    - 7
    - 11
    - 12
    scope: Main-paper core PCA imaging findings, noun/verb overlap and direct contrasts,
      matched/unmatched behavioural accuracy and imageability. Table 6 and Figures
      2,4,5 visually inspected. Main-paper scope only.
    corrections:
    - Age/education null correlations on page 4 concern 25 healthy older controls,
      not the 48 stroke participants; do not convert into patient predictors.
    - Age-of-acquisition is a word characteristic, not participant age at stroke.
    - Fluency cluster disappears with lesion-volume adjustment; generic statement
      that PCA clusters remain cannot override the specific result.
    - Executive association requires a relaxed voxel threshold. Figure 5 adjusted
      threshold .005 differs from Methods .001; preserve discrepancy.
    - Printed lesion-volume correlations have positive signs despite better-performance
      interpretation being unclear; no signed clinical volume effect inferred.
    - Atlas tract names describe T1 cluster overlap, not acquired diffusion or disconnectome
      measurements.
    - Overlapping cohort with later Alyahya2020 and Butler/Halai work, not independent
      replication.
    remaining:
    - Named-person review; shared-cohort reconciliation.
    - Do not infer precise ROI boundaries or tract-specific effects from cluster labels.
    - Regression reporting has inconsistent t/p combinations and unclear observational
      unit (df differs from 48 participants); retain as qualified assessment finding
      only.
    - Individual exceptions, all error subtypes and every secondary contrast not separately
      converted; no exhaustive completeness claim.
    - Table 5 page 10 not visually checked; coordinates not transcribed. Supplements
      excluded.
reviewer_marks:
- id: relationship-source-check
  page: 9
  quote: 'Performance on the

    phonological recognition factor was uniquely associated with the left

    posterior superior temporal gyrus, Heschl''s gyrus (including H1 and

    H2), and posterior superior and inferior temporal gyri.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-18'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
