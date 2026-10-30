---
schema_version: 2.8
id: executive_functions
name: "Executive Functions"
kind: predictor
predictor_type: behavioural
short_definition: "A collection of higher-level cognitive processes including inhibition, attention, task-switching, working memory, and self-monitoring."
assessment: ["Wisconsin Card Sort Task (WCST)", "Wiegl Sorting Test (WST)", "Cognitive Linguistic Quick Test (CLQT)", "Test of Everyday Attention (TEA)", "Raven's Coloured Progressive Matrices (RCPM)"]
units: "score"
typical_range: "not_reported"
direction_of_severity: "lower_is_worse"
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30

findings:
  - id: f1
    target: anomia
    target_kind: impairment
    claim: "Baseline executive control and cognitive abilities are positively correlated with improvements in naming accuracy following naming therapy."
    direction: likely
    relationship: correlational
    citation: "@Simic2019"
    method: narrative_review
    design: systematic-review
    strength: moderate
    evidence_quality: narrative-review
    primary_papers_cited:
      - "@Fillingham2006"
      - "@LambonRalph2010"
      - "@Conroy2009b"
      - "@Conroy2009c"
      - "@Yeung2009"
    author_limitations:
      - "Measurement of EC was highly variable across studies, often using broad or vague definitions."
      - "Many studies reported composite scores, making it difficult to isolate the specific role of EC."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Main findings, page 16"
      confidence: high
      flags: []
    source_passages:
      - section: "Main findings"
        page: 16
        quote: "Overall, greater performance on measures of EC and other cognitive tasks was significantly correlated to better language therapy outcomes in 10 of the 15 studies reviewed (67%...)"
        supports: claim
      - section: "Discussion"
        page: 29
        quote: "the measurement of EC was highly variable across studies, likely due to overly broad and/or vague definitions of EC"
        supports: limitation
      - section: "Discussion"
        page: 29
        quote: "many studies reported composite scores of cognitive abilities which included, but were not limited to measures of EC, further complicating the interpretation of results."
        supports: limitation

  - id: f2
    target: constraint_induced_aphasia_therapy
    target_kind: therapy
    claim: "Baseline executive control abilities do not significantly correlate with treatment success in intensive constraint-induced aphasia therapy."
    direction: no_effect
    relationship: responder
    citation: "@Simic2019"
    method: narrative_review
    design: systematic-review
    strength: moderate
    evidence_quality: narrative-review
    primary_papers_cited:
      - "@Babbitt2016"
      - "@Rose2013"
      - "@Kristensen2015"
    author_limitations:
      - "The nature of CIAT may bypass the positive relationship between EC and language therapy outcomes found in non-intensive therapies."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Main findings, page 16"
      confidence: high
      flags: []
    source_passages:
      - section: "Main findings"
        page: 16
        quote: "This relationship emerged when EC was measured using specific (e.g., divided attention), as opposed to broad (e.g., reasoning) tasks, and primarily when naming therapy was administered; intensive constraint-induced therapy did not correlate with treatment success."
        supports: claim
      - section: "Discussion"
        page: 31
        quote: "Rose and colleagues (2013) suggest that the nature of CIAT (e.g., intense treatment within a socially mediated practice context) bypasses the positive relationship between EC and language therapy outcomes"
        supports: limitation

  - id: f3
    target: anomia
    target_kind: impairment
    claim: "The positive correlation between baseline executive control and naming therapy success is more prominent in individuals with moderate-to-severe aphasia."
    direction: likely
    relationship: correlational
    citation: "@Simic2019"
    method: narrative_review
    design: systematic-review
    strength: moderate
    evidence_quality: narrative-review
    author_limitations: []
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "The impact of aphasia severity, page 28"
      confidence: high
      flags: []
    source_passages:
      - section: "The impact of aphasia severity"
        page: 28
        quote: "In studies treating primarily moderate-severe language deficits, positive correlations tended to emerge between baseline EC and/or cognitive abilities (and in some cases baseline language ability), and language therapy outcomes"
        supports: claim
---

# Executive Functions

Systematic review of the relationship between baseline executive control (EC) and language therapy gains in post-stroke aphasia.
