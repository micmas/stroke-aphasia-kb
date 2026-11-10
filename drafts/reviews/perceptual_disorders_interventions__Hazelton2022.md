---
schema_version: 2.8
id: perceptual_disorders_interventions__Hazelton2022
name: Interventions for Perceptual Disorders Following Stroke
kind: review
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: perceptual_disorders
  target_kind: impairment
  claim: There is currently insufficient high-quality RCT evidence to support or refute the effectiveness
    of specific interventions for perceptual disorders following stroke.
  direction: mixed
  relationship: synthesis
  citation: '@Hazelton2022'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: weak
  author_limitations:
  - The quality of evidence was judged to be very low due to risk of bias, imprecision, and indirectness.
  - Small sample sizes in included trials limit the ability to draw generalisable conclusions.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Authors' Conclusions, page 28
    confidence: high
    flags: []
  source_passages:
  - section: Authors' Conclusions
    page: 28
    quote: Following a detailed, systematic search, we identified limited RCT evidence of the effectiveness
      of interventions for perceptual disorders following stroke. There is insufficient evidence to support
      or refute the suggestion that perceptual interventions are effective.
    supports: claim
  - section: Discussion
    page: 28
    quote: The number of participants within the included trials was small, ranging from 11 to 80 participants...
      trial variations limited the pooling of data which, in turn, limited the conclusions that could
      be drawn from the evidence.
    supports: limitation
- id: f2
  target: pusher_syndrome
  target_kind: impairment
  claim: Game-based posture training may be more beneficial than standard physiotherapy for improving
    activities of daily living and measures of Pusher Syndrome severity.
  direction: likely
  relationship: synthesis
  citation: '@Hazelton2022'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: weak
  author_limitations:
  - All evidence for this finding was of very low quality.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Discussion, page 26
    confidence: high
    flags: []
  source_passages:
  - section: Discussion
    page: 26
    quote: For Pusher Syndrome... Game-based posture training may be more beneficial than standard physiotherapy
      for improving ADL and measures of Pusher Syndrome severity. All evidence was of very low quality.
    supports: claim
- id: f3
  target: tactile_perception
  target_kind: impairment
  claim: Active interventions for tactile perception disorders may have a beneficial effect on perceptual
    function, though evidence is of very low quality.
  direction: likely
  relationship: synthesis
  citation: '@Hazelton2022'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: weak
  author_limitations:
  - Evidence is of very low quality.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Discussion, page 26
    confidence: high
    flags: []
  source_passages:
  - section: Discussion
    page: 26
    quote: Interventions for touch perception disorders... there may be a beneficial effect of active
      intervention on perceptual function; this evidence is of very low quality.
    supports: claim
- id: f4
  target: visual_perception
  target_kind: impairment
  claim: There is no evidence of a difference between active intervention and no treatment on measures
    of visual perception.
  direction: no_effect
  relationship: synthesis
  citation: '@Hazelton2022'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: weak
  author_limitations:
  - Evidence is of very low quality.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Discussion, page 26
    confidence: high
    flags: []
  source_passages:
  - section: Discussion
    page: 26
    quote: Interventions for visual perception disorders... We found no difference between intervention
      and no treatment on measures of perception; this evidence is of very low quality.
    supports: claim
---
