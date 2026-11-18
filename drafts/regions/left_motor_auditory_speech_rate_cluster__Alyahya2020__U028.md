---
id: left_motor_auditory_speech_rate_cluster
name: Left motor-auditory speech rate clusters
kind: network
findings:
- id: f1
  target_kind: impairment
  direction: likely
  relationship: correlational
  method: VBCM
  design: cross-sectional
  sample:
    n: 46
    population: Native English-speaking chronic aphasia after a single left ischaemic
      or haemorrhagic stroke; premorbidly left-handed, severe motor-speech disorder
      and no discourse response excluded
    phase: chronic
    time_post_onset: 16–280 months; mean 69.43 months (Table 1)
    cohort: Same participants as earlier Alyahya studies; same or subsample in Butler2014/Halai2017,
      not independent replication
  statistics:
    threshold: Voxel p<.001; cluster FWE p<.05. Table 2 components 1–6 omit lesion-volume
      adjustment; component 7 includes it.
    effect_size: Cluster and peak statistics, not an individual prognostic effect
      size
  confounders_controlled:
  - Other six PCA components entered simultaneously
  - Age
  - Education
  - Time since stroke onset
  confounders_not_controlled:
  - Sex not listed as covariate
  - Lesion volume omitted in primary map; sensitivity model described in claim
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
    paper_section: Main PDF Methods, Results, Table 2 and Figure 4
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
    n_analysed: 46
    min_lesion_overlap: not_reported
    lesion_volume_correction: none
    multiple_comparisons: cluster_fwe
  outcome_timing:
    type: status_at_assessment
    interval: Cross-sectional chronic status; not longitudinal recovery or treatment
      response
  notes: Group association; not validated individual prediction. Keep shared-cohort
    provenance. Atlas overlap cannot establish disconnection of an individual tract.
  target: fluency
  claim: The motor-speech factor represents words per minute across discourse tasks,
    not a diagnosis of apraxia. Its unadjusted map included pre/postcentral and opercular
    cortex, auditory/temporal regions, orbitofrontal cortex and reported fornix/cingulum
    overlap. After lesion-volume adjustment, clusters were reported only at lenient
    voxel p=.05 / cluster FWE p<.01.
  citation: '@Alyahya2020'
  source_passages:
  - section: Source passage P8-S2-C3
    page: 8
    quote: 'The ‘motor speech’ component showed

      neural correlates in the pre/post-central gyri, central opercu-

      lar cortex, orbito-frontal cortex, and deep temporal tissues

      including Heschl’s gyrus and planum polare, in addition to

      the

      fornix

      and

      cingulum.'
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
  - section: Main PDF page 12 (agent source check)
    page: 12
    quote: 'However, it

      must be acknowledged that white matter tracts described in

      this study are descriptive, based on the overlap of the signifi-

      cant clusters with a white matter atlas (Catani et al., 2012)

      rather than directly measured using diffusion-weighted imag-

      ing. Future studies could use connectome-based approaches

      as a direct measure of the role of the identified tracts with

      connected speech production.

      '
    supports: limitation
  - section: Main PDF page 8 (agent source check)
    page: 8
    quote: 'None of the seven fundamental components correlate with

      lesion volume except for the semantic processing component

      (r = –0.54, P 5 0.001). On the other hand, the VBCM

      model with lesion volume correction revealed significant cor-

      relations between brain regions and three components:

      ‘phonological production’, ‘phonological recognition’ and

      ‘executive functions’, while two components, ‘verbal quan-

      tity’ and ‘motor speech’, showed significant clusters at a leni-

      ent threshold of P = 0.05 voxel-level and FWE-corrected

      cluster level at P 5 0.01. Overall, the significant clusters cor-

      responded exactly to the earlier results (i.e. without lesion

      volume correction), except for being smaller in size. The ‘ex-

      ecutive function’ component correlated with the left precen-

      tral gyrus, superior and middle frontal gyri, supplementary

      motor areas, paracingulate gyrus, and the frontal aslant

      tract. These frontal regions showed overlap with the regions

      identified

      in

      association

      with

      the

      connected

      speech

      components.

      '
    supports: confounders
  - section: Main PDF page 10 (agent source check)
    page: 10
    quote: 'Table 2 Signiﬁcant clusters and peak MNI coordinates related to language
      and cognitive components extracted

      from a varimax rotated PCA

      Principal components

      Locationa

      Cluster size (number of voxels)

      MNI coordinate

      Z-score

      x

      y

      z

      Component 1: Phonological production

      Corticospinal tract

      1889

      4.14

      –28

      –46

      30

      Long segment of arcuate fasciculus

      3.95

      –30

      –34

      22

      Parietal opercular cortex

      3.88

      –32

      –36

      22

      Posterior segment of arcuate fasciculus

      3.84

      –40

      –44

      12

      Angular gyrus

      3.62

      –34

      –54

      24

      Anterior supramarginal gyrus

      3.55

      –60

      –40

      42

      Posterior supramarginal gyrus

      3.48

      –50

      –46

      40

      Inferior longitudinal fasciculus

      3.47

      –34

      –46

      0

      Component 2: Verbal quantity

      Precentral gyrus

      2280

      4.67

      –60

      0

      8

      Central opercular cortex

      4.20

      –52

      –16

      12

      Frontal aslant tract

      3.98

      –54

      3

      6

      Frontal opercular cortex

      3.91

      –48

      8

      2

      Post-central gyrus

      3.47

      –54

      –14

      26

      Long segment of arcuate fasciculus

      3.40

      –47

      –3

      21

      Inferior frontal gyrus (pars opercularis)

      3.25

      –55

      8

      0

      Anterior segment of arcuate fasciculus

      3.02

      –44

      –14

      20

      Component 3: Semantic processing

      Inferior lateral occipital cortex

      1255

      4.45

      –30

      –76

      10

      Cingulum

      4.42

      –10

      –56

      28

      Superior lateral occipital cortex

      3.95

      –26

      –64

      24

      Inferior fronto-occipital fasciculus

      3.27

      –35

      –21

      –10

      Posterior middle temporal gyrus

      3.15

      –40

      –58

      10

      Anterior middle temporal gyrus

      595

      3.92

      –50

      –8

      –24

      Inferior longitudinal fasciculus

      3.91

      –38

      –10

      –20

      Anterior inferior temporal gyrus

      3.85

      –44

      –10

      –32

      Posterior inferior temporal gyrus

      3.70

      –46

      –26

      –18

      Anterior temporal fusiform cortex

      3.34

      –38

      –6

      –26

      Uncinate

      3.25

      –37

      –5

      –19

      Planum polare

      3.05

      –41

      –3

      –21

      Component 4: Verbal quality

      Middle frontal gyrus

      2237

      3.71

      –34

      16

      32

      Frontal pole

      3.54

      –16

      54

      4

      Orbito-frontal cortex

      3.54

      –34

      35

      –16

      Anterior cingulate gyrus

      2.91

      –6

      30

      6

      Superior lateral occipital cortex

      1087

      3.98

      –20

      –50

      46

      Superior parietal lobule

      3.41

      –24

      –48

      54

      Inferior frontal gyrus (pars opercularis)

      2.79

      –50

      18

      17

      Component 5: Phonological recognition

      Posterior inferior temporal gyrus

      6916

      4.99

      –50

      –38

      –16

      Posterior middle temporal gyrus

      4.89

      –58

      –26

      –18

      Planum temporale

      4.07

      –60

      –28

      8

      Angular gyrus

      4.04

      –52

      –52

      14

      Anterior inferior temporal gyrus

      3.86

      –42

      –8

      –40

      Posterior supramarginal gyrus

      3.86

      –54

      –45

      14

      Superior lateral occipital cortex

      3.64

      –28

      –78

      22

      Anterior middle temporal gyrus

      3.62

      –52

      –6

      –24

      Heschl’s gyrus

      3.40

      –46

      –18

      4

      Posterior segment of arcuate fasciculus

      3.32

      –48

      –49

      16

      Posterior superior temporal gyrus

      3.14

      –68

      –10

      4

      Planum polare

      3.05

      –42

      –20

      –8

      Inferior longitudinal fasciculus

      2.98

      –48

      –18

      –19

      Component 6: Motor speech

      Cingulum

      1124

      4.88

      –18

      –30

      –4

      Fornix

      3.76

      –16

      –28

      18

      Planum polare

      1893

      4.49

      –46

      –10

      0

      Central opercular cortex

      4.10

      –58

      –14

      12

      Post-central gyrus

      4.05

      –58

      –14

      26

      Heschl’s gyrus

      3.99

      –50

      –18

      10

      Precentral gyrus

      3.85

      –55

      –2

      20

      Orbito-frontal cortex

      420

      3.85

      –20

      6

      –22

      Component 7: Executive functions

      Superior frontal gyrus

      2159

      5.07

      –18

      2

      48

      Supplementary motor areas

      4.83

      –14

      –4

      50

      Frontal aslant tract

      4.13

      –14

      11

      50

      Paracingulate gyrus

      4.05

      –10

      30

      30

      Middle frontal gyrus

      3.68

      –34

      2

      58

      Precentral gyrus

      3.28

      –34

      –6

      52

      aAnatomical labels obtained using Harvard-Oxford atlas (Desikan et al., 2006)
      and NatBrainLab white matter atlas based on diffusion tensor tractography (Catani
      et al., 2012) in MNI space.

      All results were thresholded at P 5 0.001 voxel-level and FWE cluster-level
      corrected at P 5 0.05 with demographic variables (age, education, and time since
      stroke onset) entered as

      covariates, except for Component 7, which included lesion volume as covariate
      (as the cluster associated with this component was not signiﬁcant without controlling
      for lesion volume).

      '
    supports: statistics
schema_version: '2.8'
status: draft
created_by: agent:relationship-converter
created_on: '2026-11-18'
relationship_review:
  paper: Alyahya2020
  proposal_id: U028
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
    - P8-S2-C3
    qualifier_ids: []
    context_ids: []
    table_ids: []
    exposure:
      text: motor speech
      source_id: P8-S2-C3
    outcome:
      text: motor speech
      source_id: P8-S2-C3
    relation: descriptive
    effect_unit: descriptive
    result_status: reported_detected
    outcome_type: not_applicable
    direction: not_stated
    direction_source_id: ''
    origin: current_study
    label_match_candidates: {}
    id: U028
    flags: []
    linked_tables: []
    approved: false
    status: requires_source_review
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
    - P3-S2-C13
    - P3-S2-C14
    - P3-S2-C15
    - P3-S2-C3
    - P3-S2-C4
    - P3-S2-C5
    - P3-S2-C6
    - P3-S2-C7
    - P3-S2-C8
    - P3-S2-C9
    - P3-S3-C3
    - P3-S3-C4
    - P3-S3-C5
    - P3-S3-C6
    - P3-S3-C7
    - P4-S1-C5
    - P4-S2-C5
    - P4-S2-C6
    - P5-S2-C14
    - P8-S1-C4
    - P8-S1-C5
    - P8-S1-C6
    - P8-S2-C4
    - P8-S2-C5
    - P8-S2-C6
    context_policy: Script-attached frame, Methods and nearby source passages; candidates
      are not confirmed analysis-specific controls
    conditional_or_conflicting_unit_ids: []
    digest: e74f65d615fee871affd2cf5851b11fa522d602838b64a8081e8fc25d9ac1dc0
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
  page: 8
  quote: 'The ‘motor speech’ component showed

    neural correlates in the pre/post-central gyri, central opercu-

    lar cortex, orbito-frontal cortex, and deep temporal tissues

    including Heschl’s gyrus and planum polare, in addition to

    the

    fornix

    and

    cingulum.'
  status: pending
  by: agent:relationship-converter
  date: '2026-11-18'
  note: 'Before approval: verify mapped claim/target, anatomy, timing, personal-factor
    roles, all qualifiers, source audit issues and main-PDF tables/figures; check
    missing results. This model proposal is not verified.'
---

# Source review required

This draft is unapproved. The full audit and original proposal are retained in the frontmatter. Resolve the pending source-check mark before approval.
