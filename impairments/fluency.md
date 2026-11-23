---
schema_version: 2.7
id: fluency
name: Fluency (speech fluency)
kind: impairment
status: approved
created_by: agent:claude-opus-4-7
created_on: 2026-05-01
short_definition: 'Underlying language component capturing connected-speech fluency:
  words per minute, mean length of utterance, and number of tokens in spontaneous
  speech. One of five orthogonal factors recovered by PCA over the standard chronic-aphasia
  neuropsychological battery (Butler et al. 2014; Halai et al. 2017; Alyahya et al.
  2018). Distinct from the BDAE/WAB clinical fluency dichotomy, which is a binary
  syndromic classification.'
assessment:
- Words per minute (Cookie theft picture description)
- Mean length of utterance (Cookie theft)
- Number of tokens (Cookie theft)
- Backward digit span (loads partially)
findings: []
source: agent_draft
last_reviewed: null
notes: 'First-extraction draft from Alyahya et al. 2018 (NounVerb). The

  fluency PCA factor (Factor 3: 7.8% variance) is associated with a

  6008-voxel cluster spanning left frontal and parietal regions

  including central opercular cortex, pre- and post-central gyri, and

  the anterior segment of the arcuate fasciculus. Three peak findings

  recorded.


  Loadings (Table 4) used to interpret this factor as "fluency":

  word-per-minute (.837), mean length of utterance (.828), number of

  tokens (.811), backward digit span (.511). All three primary

  loadings derived from coding spontaneous speech in the BDAE Cookie

  Theft picture description task.


  CRITICAL CAVEAT: the fluency cluster did NOT survive when lesion

  volume was added as a covariate (correlation with lesion volume:

  r=0.59, p<0.0001). The fluency factor is the most lesion-volume-

  confounded of the five PCA factors. Promotion of these findings

  should reflect that lesion-volume independence has not been

  demonstrated.


  Discussion (page 228) emphasises that the relevant white-matter tract

  is most likely the frontal aslant tract (Catani 2013, Rojkova 2015,

  Halai 2017) rather than the arcuate per se. The natbrainlab atlas

  used here does not resolve the frontal aslant from the anterior

  arcuate, so the f1 finding may include both fibre systems.'
reviewer: michele
reviewed_on: '2026-05-06'
---
# Fluency (speech fluency)

## Component definition

Connected-speech fluency, operationalised as words per minute, mean
length of utterance, and number of tokens in the BDAE Cookie Theft
picture description task. This is a continuous measure of speech
production rate, distinct from the BDAE/WAB clinical fluency
dichotomy (which is a binary syndromic classification).

## Lesion correlates (per Alyahya 2018 NounVerb)

PCA-VBCM identifies a 6008-voxel cluster with peaks in:

  - Central opercular cortex (Z=4.78)
  - Post-central gyrus (Z=4.48)
  - Pre-central gyrus (Z=3.58)
  - Anterior segment of arcuate fasciculus (Z=3.30)

The cluster does NOT survive lesion-volume covariate. The Discussion
attributes the fluency white-matter finding to the frontal aslant
tract (FAT) on theoretical grounds, but the natbrainlab atlas used
in this paper does not separate FAT from anterior-arcuate.

## Notes for next extraction round

  - Add left_anterior_arcuate_fasciculus, left_central_opercular_cortex,
    left_pre_central_gyrus, post_central_gyrus as region entries before
    re-extracting on the region side.
  - Consider creating a frontal_aslant_tract region entry given the
    Discussion's emphasis on FAT.
  - Findings here should be flagged as "lesion-volume confounded"
    when used in interpret_overlap downstream.
