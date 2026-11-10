---
schema_version: 2.8
id: dysarthria_interventions__Mitchell2017
name: Interventions for Dysarthria due to Stroke and Other Adult-Acquired Brain Injury
kind: review
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: dysarthria
  target_kind: impairment
  claim: There is limited evidence suggesting a short-term beneficial effect of dysarthria interventions
    on impairment-level measures, such as muscle movement, but no evidence of long-term persisting effects
    on activity or participation levels.
  direction: mixed
  relationship: synthesis
  citation: '@Mitchell2017'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: weak
  author_limitations:
  - The evidence base is limited, with only five small trials included, none of which were adequately
    powered.
  - There is a lack of consensus on outcome measures and time points for measurement.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Abstract, Main results
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 5
    quote: 'There was a statistically significant effect favouring intervention at the immediate, impairment
      level of measurement (SMD 0.47, 95% CI 0.02 to 0.92, P = 0.04, I2 = 0%; 4 trials, 99 participants,
      GRADE: very low quality)'
    supports: claim
  - section: Abstract
    page: 5
    quote: 'Our primary analysis of a persisting (three to nine months post-intervention) effect at the
      activity level of measurement found no evidence in favour of dysarthria intervention compared with
      any control (SMD 0.18, 95% CI -0.18 to 0.55; 3 trials, 116 participants, GRADE: low quality)'
    supports: claim
  - section: Discussion
    page: 16
    quote: The one significant finding at the impairment level immediately post-intervention... means
      that clinically there may be some improvement of tongue and lip movement for example but there is
      no evidence that these persist long-term
    supports: claim
  - section: Discussion
    page: 16
    quote: We only identified five, small trials which indicates the evidence base is limited. In addition
      to the limited number of trials there were only small numbers of participants within the trials
    supports: limitation
  - section: Discussion
    page: 16
    quote: There was no consensus on outcome measures or time points for measurement.
    supports: limitation
---

This systematic review evaluates various interventions for dysarthria following stroke and other non-progressive adult-acquired brain injuries. The authors found that while some immediate improvements in impairment-level measures (e.g., oromotor control) were observed, there was no robust evidence for persisting effects on functional communication (activity level) or social participation.
