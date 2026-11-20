---
schema_version: 2.7
id: initial_aphasia_severity
name: Initial aphasia severity (acute WAB composite)
aliases:
- WABinitial
- baseline WAB
- acute aphasia severity
- admission aphasia severity
- initial severity
- WAB at admission
kind: predictor
predictor_type: behavioural
short_definition: Composite WAB score (comprehension + repetition + naming subtests,
  0–30) obtained within 24–72 hours of stroke onset; lower scores indicate more severe
  aphasia.
assessment:
- Western Aphasia Battery (WAB) — comprehension, repetition, and naming subtests
- WAB composite score (0–30)
units: score 0–30 (lower = more severe)
typical_range: 0–30; cut-off for aphasia ≤28; mild-to-moderate range 14–28 in this
  sample
direction_of_severity: lower_is_worse
status: approved
review_tier: legacy
created_by: agent:claude-sonnet-4-6
created_on: 2026-05-06
findings: []
source: curated
last_reviewed: '2026-10-30'
notes: 'Lazar et al. 2010 (Stroke) is a 4-page paper using n=21 mild-to-moderate aphasic

  stroke patients from the PARIS database. The key finding is that initial WAB composite

  score (WABinitial, 0–30) predicts 81% of variance in 90-day change score, and that

  recovery is proportional (0.73 of maximum potential recovery) regardless of whether

  patients received speech-language therapy. The proportionality is interpreted as
  evidence

  for a domain-general spontaneous biological recovery mechanism in the first 90 days

  post-stroke. Lesion volume and age are not significant predictors when WABinitial
  is

  in the model.


  Note: imaging used DWI for lesion volume estimation only; not a lesion-symptom mapping
  paper.

  Method coded as behavioral_only; imaging: none for this finding.'
reviewer: auto-reviewer
reviewed_on: '2026-05-06'
---
# Initial aphasia severity as predictor of 90-day recovery (Lazar 2010)

## Predictor definition

Initial WAB composite score measured at 24–72 hours post-stroke using three standardised
WAB subtests: comprehension (0–10), repetition (0–10), and naming (0–10), yielding a
composite score of 0–30 (WABmax). A score ≤28 was the operational definition of aphasia
in this study.

## Key finding

In a regression model with WABinitial, age, and lesion volume as predictors of
90-day WAB change:
- WABinitial alone R² = 0.81 (p<0.001)
- Full model R² = 0.83
- Age: not significant (p=0.818)
- Lesion volume: not significant (p=0.236)

The proportional recovery relation (achieved ΔWAB ≈ 0.73 × potential ΔWAB) was found
for both therapy-treated (R²=0.76) and untreated (R²=0.90) subgroups.

## Clinical implication

A new therapy within the first 90 days post-stroke should produce a WAB change score
*greater* than that predicted by the 0.73 proportionality model to be considered
more effective than current modalities.

## Scope limitation

Severe aphasia was excluded (consent restriction). The proportionality constant and
R² values apply only to mild-to-moderate aphasia. Whether the model holds for severe
aphasia remains untested.
