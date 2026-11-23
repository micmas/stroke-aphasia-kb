---
schema_version: 2.8
id: global_aphasia
name: Global aphasia
kind: impairment
status: approved
review_tier: legacy
created_by: agent:claude-opus-4-7
created_on: 2026-05-01
short_definition: The most severe aphasia syndrome, characterized by profoundly impaired
  comprehension and production across all language modalities, often with spared automatic
  speech. Associated with extensive cortical damage in the territory supplied by the
  middle cerebral artery, typically encompassing both Broca's and Wernicke's areas.
assessment:
- Western Aphasia Battery (WAB / WAB-R)
- Boston Diagnostic Aphasia Examination (BDAE)
findings: []
source: agent_draft
last_reviewed: '2026-05-06'
notes: 'Re-extraction draft from Yourganov 2015. Eight findings extracted —

  the highest-relevance regions in Table 3''s Global column. The

  remaining Table 3 entries for global aphasia (rolandic operculum

  Z=1.96, IFG opercular Z=1.78, Heschl''s gyrus Z=1.78, long-segment

  arcuate Z=1.47, IFG orbital Z=1.28, arcuate combined Z=1.21,

  superior frontal gyrus Z=1.21, cortico-spinal tract Z=1.08,

  superior temporal gyrus Z=1.31) are not extracted as separate

  findings here to keep the draft within ~10 findings; the file-level

  notes capture them and the full Table 3 is in the source PDF.


  Critical caveat: global aphasia could not be classified above

  chance versus Broca''s aphasia in this study. Many of these eight

  findings are shared with the brocas_aphasia draft; cross-link via

  `replications` when promoted.'
reviewer: auto-reviewer
reviewed_on: '2026-05-05'
---
# Global aphasia

## Clinical definition

Global aphasia is the most severe aphasia syndrome, characterized
by profoundly impaired comprehension and production across all
language modalities. Associated with extensive cortical damage in
the territory supplied by the middle cerebral artery, typically
encompassing both Broca's and Wernicke's areas plus surrounding
cortex.

## Lesion correlates (per Yourganov 2015)

Top eight regions extracted (Table 3, Global column, predictive
relevance Z > 1.5):

  - Middle frontal gyrus (Z = 2.51) — f1
  - IFG pars triangularis (Z = 2.18) — f2
  - Temporal pole, MTG (Z = 2.15) — f3
  - Precentral gyrus (Z = 2.05) — f4
  - Putamen (Z = 2.02) — f5
  - Uncinate fasciculus (Z = 1.71) — f6
  - Insula (Z = 1.66) — f7
  - Anterior segment of arcuate fasciculus (Z = 1.65) — f8

Additional Table 3 regions with predictive relevance > 1 not
extracted as separate findings: rolandic operculum (1.96),
IFG opercular = `ho-cort_44` (1.78), Heschl's gyrus (1.78),
long-segment arcuate (1.47), IFG orbital (1.28), arcuate combined
(1.21), superior frontal gyrus (1.21), superior temporal gyrus
(1.31), cortico-spinal tract (1.08).

## Important caveat

Global vs Broca's classification was at chance (Table 1). Many
predictive regions overlap with Broca's aphasia. The two non-fluent
syndromes are not clearly separable on lesion pattern alone.
