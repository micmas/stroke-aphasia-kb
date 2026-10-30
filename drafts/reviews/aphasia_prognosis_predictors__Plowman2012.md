---
schema_version: 2.8
id: aphasia_prognosis_predictors__Plowman2012
name: "Post-stroke aphasia prognosis: a review of patient-related and stroke-related factors"
kind: review
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
findings:
  - id: f1
    target: initial_aphasia_severity
    target_kind: predictor
    claim: "Initial aphasia severity is the most predictive factor for long-term language recovery following stroke."
    direction: likely
    relationship: synthesis
    citation: "@Plowman2012"
    method: narrative_review
    design: narrative-review
    evidence_quality: narrative-review
    strength: moderate
    author_limitations: []
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 1
        quote: "Initial severity of aphasia emerged as the factor most predictive of long-term aphasia recovery."
        supports: claim
  - id: f2
    target: age
    target_kind: predictor
    claim: "The impact of age on aphasia recovery is unclear, with conflicting reports on whether it is a useful prognostic indicator."
    direction: mixed
    relationship: synthesis
    citation: "@Plowman2012"
    method: narrative_review
    design: narrative-review
    evidence_quality: narrative-review
    strength: weak
    author_limitations: []
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 2
        quote: "While age does appear to influence both the incidence and type of post-stroke aphasia, the impact of age on aphasia recovery is unclear."
        supports: claim
  - id: f3
    target: sex
    target_kind: predictor
    claim: "Gender does not appear to significantly impact the incidence, type, or recovery patterns of post-stroke aphasia."
    direction: no_effect
    relationship: synthesis
    citation: "@Plowman2012"
    method: narrative_review
    design: narrative-review
    evidence_quality: narrative-review
    strength: moderate
    author_limitations: []
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 2
        quote: "In summary, evidence is largely equivocal and gender does not appear to significantly impact incidence of aphasia, aphasia type or recovery patterns in post-stroke individuals."
        supports: claim
  - id: f4
    target: lesion_volume
    target_kind: predictor
    claim: "Lesion size and location are critical factors that influence aphasia recovery patterns."
    direction: likely
    relationship: synthesis
    citation: "@Plowman2012"
    method: narrative_review
    design: narrative-review
    evidence_quality: narrative-review
    strength: moderate
    author_limitations: []
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results"
      confidence: high
      flags: []
    source_passages:
      - section: "Results"
        page: 1
        quote: "Other influential factors of post-stroke language recovery included lesion site and size."
        supports: claim
---

This review synthesizes evidence on patient-related and stroke-related prognostic factors for aphasia recovery, concluding that stroke-related factors (severity, site, size) are more critical than patient demographics.
