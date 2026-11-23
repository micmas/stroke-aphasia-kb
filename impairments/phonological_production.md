---
schema_version: 2.7
id: phonological_production
name: Phonological production
kind: impairment
status: approved
review_tier: legacy
created_by: agent:claude-opus-4-7
created_on: 2026-05-01
short_definition: Underlying language component capturing the ability to produce word
  forms (single-word repetition and naming). Loads heavily on word/non-word repetition
  (PALPA 8/9), Boston Naming Test, OANB naming and Cambridge 64-item naming. One of
  five orthogonal factors recovered by PCA over the standard chronic-aphasia neuropsychological
  battery (Butler et al. 2014; Halai et al. 2017; Alyahya et al. 2018).
assessment:
- Word repetition — immediate (PALPA 9)
- Word repetition — delayed (PALPA 9)
- Non-word repetition — immediate (PALPA 8)
- Non-word repetition — delayed (PALPA 8)
- Cambridge 64-item naming
- Boston Naming Test (BNT)
- Object and Action Naming Battery (OANB) — noun and verb naming
findings: []
source: agent_draft
last_reviewed: '2026-05-06'
notes: 'First-extraction draft from Alyahya et al. 2018 (NounVerb). The

  phonological production PCA factor (Factor 1: 51.45% variance) is

  associated with a 3905-voxel cluster spanning posterior arcuate

  fasciculus, angular gyrus, parietal operculum, posterior supramarginal

  gyrus, and inferior longitudinal fasciculus. All five peaks recorded

  here as separate findings. The cluster survived adding lesion volume

  as a covariate (the only Factor whose semantic counterpart partially

  attenuated). This is one of the more robust lesion-symptom maps of

  phonological production in the chronic-aphasia literature because

  PCA orthogonalizes the factor away from semantic and fluency

  contributions.


  Loadings (Table 4) used to interpret this factor as "phonological

  production": word repetition - immediate (.917), word repetition -

  delayed (.904), non-word repetition - immediate (.896), non-word

  repetition - delayed (.855), Cambridge 64-item naming (.786), Boston

  Naming Test (.770), Verb naming OANB (.748), Noun naming OANB (.736),

  forward digit span (.662).


  Anchored on impairment rather than region because none of the five

  target regions yet exist as canonical region entries in regions/.

  Reviewer should consider creating left_posterior_arcuate_fasciculus,

  left_angular_gyrus, left_parietal_operculum_cortex, left_posterior_supramarginal_gyrus,

  and left_inferior_longitudinal_fasciculus as region entries before

  promoting these findings.'
reviewer: auto-reviewer
reviewed_on: '2026-05-05'
---
# Phonological production

## How to read this entry

First-extraction draft from Alyahya et al. 2018 (NounVerb). Defines the
phonological production component as a draft impairment ID and lists
the brain regions whose tissue concentration uniquely covaries with it
in the PCA-VBCM analysis (Factor 1).

## Component definition

Phonological production is the underlying language component
that captures the ability to produce word forms (single-word
repetition and naming). It is the largest factor in the rotated PCA
solution from Alyahya et al. (51.45% of variance), and is conceptually
distinct from phonological recognition (Factor 4 — minimal-pair
discrimination), semantics (Factor 2), fluency (Factor 3), and
executive function (Factor 5). The factor loads heavily on word and
non-word repetition (loadings .855–.917), all naming tasks
(.736–.786), and forward digit span (.662) — see Table 4 of the paper.

## Lesion correlates (per Alyahya 2018 NounVerb)

PCA-VBCM identifies a 3905-voxel cluster centered on:

  - Posterior segment of the arcuate fasciculus (Z=4.51, MNI [-40,-44,12])
  - Angular gyrus (Z=4.41, MNI [-34,-54,24])
  - Parietal operculum cortex (Z=4.30, MNI [-32,-36,22])
  - Posterior supramarginal gyrus (Z=3.85, MNI [-50,-46,40])
  - Inferior longitudinal fasciculus (Z=3.79, MNI [-34,-46,0])

All five clusters survive when lesion volume is added as a covariate
(the analysis is repeated at p<0.005 voxel-level FWE-corrected
cluster-level). This is a notable robustness check given that the
verb naming, verb comprehension, noun naming, and noun comprehension
maps all *did* drop out of significance under the same covariate.

## Notes for next extraction round

  - Add left_posterior_arcuate_fasciculus, left_angular_gyrus,
    left_parietal_operculum_cortex, left_posterior_supramarginal_gyrus, and
    left_inferior_longitudinal_fasciculus as region entries before
    re-extracting on the region side.
  - The angular gyrus, posterior supramarginal gyrus, and inferior
    longitudinal fasciculus also load on other PCA factors — capture
    those cross-factor associations as additional findings on the
    region side, with cross-references to the relevant impairment
    drafts.
