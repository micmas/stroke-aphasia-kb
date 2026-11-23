---
schema_version: 2.7
id: stroke_severity_sss
name: Neurological stroke severity (Scandinavian Stroke Scale)
aliases:
- Scandinavian Stroke Scale
- SSS neurological severity
- general stroke severity
- modified SSS
- SSS excluding speech and orientation
kind: predictor
predictor_type: clinical
short_definition: Total score on the Scandinavian Stroke Scale (SSS, 0–58) assessing
  general neurological impairment after stroke; a modified version excluding speech
  and orientation items (0–42) was used to avoid confounding with aphasia.
assessment:
- Scandinavian Stroke Scale (SSS, 0–58)
- Modified SSS excluding speech and orientation items (0–42)
units: score 0–58 (SSS) or 0–42 (modified SSS); higher score = less severe impairment
typical_range: mean 23.4 (SD 9.3) for modified SSS in this aphasia sample (n=82)
direction_of_severity: lower_is_worse
status: approved
review_tier: legacy
created_by: agent:claude-sonnet-4-6
created_on: 2026-05-06
findings: []
source: curated
last_reviewed: '2026-05-07'
notes: "Pedersen et al. 2004 (Cerebrovasc Dis) is the Copenhagen Aphasia Study, a\
  \ 9-page\nprospective longitudinal study of 270 acute stroke patients with aphasia\
  \ (203 first-ever\nstrokes) from three Copenhagen hospitals (1996–1999), assessed\
  \ with the Danish WAB.\n\nTwo main predictor findings:\n1. Initial WAB-AQ + modified\
  \ SSS together predict R²=0.60 of 1-year WAB-AQ.\n2. Initial WAB-AQ alone predicts\
  \ R²=0.47 of 1-year WAB-AQ.\n\nNon-significant predictors: age, sex, aphasia type.\n\
  \nAdditional descriptive findings (not encoded as KB findings):\n- Acute aphasia\
  \ types: global 32%, anomic 25%, Wernicke's 16%, Broca's 12%, transcortical\n  sensory\
  \ 7%, conduction 5%, transcortical motor 2%, isolation 2%.\n- 61% still aphasic\
  \ at 1 year (in milder form).\n- Aphasia type always changed to a less severe form;\
  \ nonfluent → fluent evolution possible,\n  but fluent → nonfluent never observed.\n\
  - No imaging (lesion-symptom) analyses performed; study is purely clinical/behavioural."
reviewer: claude-cowork
reviewed_on: '2026-05-06'
---
# Stroke severity (SSS) as predictor of aphasia prognosis (Pedersen 2004)

## Study overview

The Copenhagen Aphasia Study prospectively enrolled 270 consecutive acute stroke patients
with aphasia (203 first-ever strokes) from three Copenhagen hospitals, assessed with the
Danish WAB at admission (median 4 days post-onset) and again at 1 year.

## Main predictor findings

**Finding f1** — Two-variable prediction model:
- Predictors retained: initial WAB-AQ and neurological stroke severity (modified SSS, 0–42)
- Predictors dropped: age, sex, aphasia type
- R² = 0.60 for 1-year WAB-AQ

**Finding f2** — Single-variable prediction:
- Initial WAB-AQ alone R² = 0.47 for 1-year WAB-AQ
- Regression formula (printed in paper): initial AQ = 45.3 + 0.65 × AQ at 1 year

## Aphasia type evolution

Type of aphasia always changed to a less severe classification over the year.
Non-fluent aphasia (e.g. global) could evolve to fluent (e.g. anomic),
but fluent types never became non-fluent. Initial aphasia type does not predict
degree of recovery beyond its correlation with severity.

## Clinical takeaway

Adding a brief neurological severity rating (Scandinavian Stroke Scale) at admission
improves aphasia outcome prediction beyond initial WAB-AQ alone (R² 0.47 → 0.60).
Age and sex do not improve prediction.
