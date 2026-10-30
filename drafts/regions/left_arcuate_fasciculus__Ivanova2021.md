---
schema_version: 2.8
id: left_arcuate_fasciculus
name: Left arcuate fasciculus
kind: tract
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
hemisphere: left
members: []
networks: []
tracts_adjacent: []
findings:
- id: f1
  target: anomia
  target_kind: impairment
  claim: The long segment of the left arcuate fasciculus contributes to naming abilities beyond the contribution
    of cortical language areas.
  direction: likely
  relationship: causal
  citation: '@Ivanova2021'
  method: tractography
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 32
    population: chronic aphasia following left hemisphere stroke
    time_post_onset: Mtimepost-onset = 96.6 93.1 months
    phase: chronic
    age_range: 40 to 83 years (Mage = 63.7 1.4)
    handedness: strongly right-handed (all except 3)
    language: native-like proficiency in English
  statistics:
    threshold: p < 0.05
    effect_size: not_reported
  confounders_controlled:
  - gender
  - time post-onset
  - lesion load to frontal, temporal, and parietal language areas
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Long segment of the AF connecting the temporal and frontal areas dorsally, defined by
      Frontal and Temporal ROIs (Catani 3-segment model).
  imaging_details:
    field_strength: 3T
    modalities:
    - modality: T1
      sequence: MPRAGE
      voxel_size_mm:
      - 1
      - 1
      - 1
      TR_ms: 2400
      TE_ms: 3.16
    - modality: DWI
      voxel_size_mm:
      - 2
      - 2
      - 2
      n_directions: 64
      b_values:
      - 0
      - 2000
    preprocessing_pipeline: FSL fieldmap correction, ExploreDTI movement/eddy current corrections, and
      HARDI deterministic tractography (StarTrack).
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Cortical Structural Atlas
  author_limitations:
  - Relied on the WAB for a number of measures; more linguistically sensitive tests may be useful.
  - Tracts located close together tend to often be damaged together, making it challenging to ascertain
    unique functionality.
  - Idiosyncratic reorganization and compensation in chronic stroke might have masked differential effects.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 8; Table 5, page 10
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 8
    quote: 'Involvement of the following tract segments in the left hemisphere in language processing
      beyond the contribution of cortical areas was demonstrated: the long segment of the AF contributed
      to naming abilities'
    supports: claim
  - section: Materials and Methods - Participants
    page: 3
    quote: a group of thirty-three successively scanned participants with aphasia (PWA... following a
      left hemisphere stroke
    supports: sample
  - section: Materials and Methods - DWI Data Processing
    page: 5
    quote: HARDI deterministic tractography based on constrained spherical deconvolution was done
    supports: method
  - section: Materials and Methods - Brain Imaging
    page: 4
    quote: Brain imaging data were acquired on a Siemens Magnetom Verio 3T MRI scanner
    supports: imaging_details
  - section: Discussion - Limitations
    page: 12
    quote: Although we used a number of specialized language tests such as the CYCLE and BNT, we relied
      on the WAB for a number of measures.
    supports: limitation
- id: f2
  target: fluency
  target_kind: impairment
  claim: The anterior segment of the left arcuate fasciculus contributes to speech fluency beyond the
    contribution of cortical language areas.
  direction: likely
  relationship: causal
  citation: '@Ivanova2021'
  method: tractography
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 32
    population: chronic aphasia following left hemisphere stroke
    time_post_onset: Mtimepost-onset = 96.6 93.1 months
    phase: chronic
    age_range: 40 to 83 years (Mage = 63.7 1.4)
    handedness: strongly right-handed (all except 3)
    language: native-like proficiency in English
  statistics:
    threshold: p < 0.05
    effect_size: not_reported
  confounders_controlled:
  - gender
  - time post-onset
  - lesion load to frontal, temporal, and parietal language areas
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Anterior segment of the AF connecting frontal regions with inferior parietal areas, defined
      by Frontal and Parietal ROIs (Catani 3-segment model).
  imaging_details:
    field_strength: 3T
    modalities:
    - modality: T1
      sequence: MPRAGE
      voxel_size_mm:
      - 1
      - 1
      - 1
      TR_ms: 2400
      TE_ms: 3.16
    - modality: DWI
      voxel_size_mm:
      - 2
      - 2
      - 2
      n_directions: 64
      b_values:
      - 0
      - 2000
    preprocessing_pipeline: FSL fieldmap correction, ExploreDTI movement/eddy current corrections, and
      HARDI deterministic tractography (StarTrack).
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Cortical Structural Atlas
  author_limitations:
  - Relied on the WAB for a number of measures; more linguistically sensitive tests may be useful.
  - Tracts located close together tend to often be damaged together, making it challenging to ascertain
    unique functionality.
  - Idiosyncratic reorganization and compensation in chronic stroke might have masked differential effects.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 8; Table 5, page 10
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 8
    quote: 'Involvement of the following tract segments in the left hemisphere in language processing
      beyond the contribution of cortical areas was demonstrated: [...] anterior segment – to fluency
      and naming'
    supports: claim
  - section: Materials and Methods - Participants
    page: 3
    quote: a group of thirty-three successively scanned participants with aphasia (PWA... following a
      left hemisphere stroke
    supports: sample
  - section: Materials and Methods - DWI Data Processing
    page: 5
    quote: HARDI deterministic tractography based on constrained spherical deconvolution was done
    supports: method
  - section: Materials and Methods - Brain Imaging
    page: 4
    quote: Brain imaging data were acquired on a Siemens Magnetom Verio 3T MRI scanner
    supports: imaging_details
  - section: Discussion - Limitations
    page: 12
    quote: Although we used a number of specialized language tests such as the CYCLE and BNT, we relied
      on the WAB for a number of measures.
    supports: limitation
- id: f3
  target: form_to_meaning
  target_kind: impairment
  claim: The posterior segment of the left arcuate fasciculus contributes to language comprehension beyond
    the contribution of cortical language areas.
  direction: likely
  relationship: causal
  citation: '@Ivanova2021'
  method: tractography
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 32
    population: chronic aphasia following left hemisphere stroke
    time_post_onset: Mtimepost-onset = 96.6 93.1 months
    phase: chronic
    age_range: 40 to 83 years (Mage = 63.7 1.4)
    handedness: strongly right-handed (all except 3)
    language: native-like proficiency in English
  statistics:
    threshold: p < 0.05
    effect_size: not_reported
  confounders_controlled:
  - gender
  - time post-onset
  - lesion load to frontal, temporal, and parietal language areas
  confounders_not_controlled: []
  region_definition:
    kind: tract
    description: Posterior segment of the AF connecting inferior parietal regions with the temporal lobes,
      defined by Parietal and Temporal ROIs (Catani 3-segment model).
  imaging_details:
    field_strength: 3T
    modalities:
    - modality: T1
      sequence: MPRAGE
      voxel_size_mm:
      - 1
      - 1
      - 1
      TR_ms: 2400
      TE_ms: 3.16
    - modality: DWI
      voxel_size_mm:
      - 2
      - 2
      - 2
      n_directions: 64
      b_values:
      - 0
      - 2000
    preprocessing_pipeline: FSL fieldmap correction, ExploreDTI movement/eddy current corrections, and
      HARDI deterministic tractography (StarTrack).
    reference_space: MNI152
    atlases_used:
    - Harvard-Oxford Cortical Structural Atlas
  author_limitations:
  - Relied on the WAB for a number of measures; more linguistically sensitive tests may be useful.
  - Tracts located close together tend to often be damaged together, making it challenging to ascertain
    unique functionality.
  - Idiosyncratic reorganization and compensation in chronic stroke might have masked differential effects.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 8; Table 5, page 10
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 8
    quote: 'Involvement of the following tract segments in the left hemisphere in language processing
      beyond the contribution of cortical areas was demonstrated: [...] the posterior segment – to comprehension.'
    supports: claim
  - section: Materials and Methods - Participants
    page: 3
    quote: a group of thirty-three successively scanned participants with aphasia (PWA... following a
      left hemisphere stroke
    supports: sample
  - section: Materials and Methods - DWI Data Processing
    page: 5
    quote: HARDI deterministic tractography based on constrained spherical deconvolution was done
    supports: method
  - section: Materials and Methods - Brain Imaging
    page: 4
    quote: Brain imaging data were acquired on a Siemens Magnetom Verio 3T MRI scanner
    supports: imaging_details
  - section: Discussion - Limitations
    page: 12
    quote: Although we used a number of specialized language tests such as the CYCLE and BNT, we relied
      on the WAB for a number of measures.
    supports: limitation
---
