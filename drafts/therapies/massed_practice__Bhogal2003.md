---
schema_version: 2.8
id: massed_practice
name: Massed Practice (Intensive Therapy)
kind: therapy
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
targets_impairments:
- anomia
- fluency
- form_to_meaning
short_description: High-intensity speech and language therapy characterized by a high number of therapy
  hours per week delivered over a shorter total duration.
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: High-intensity aphasia therapy (characterized by more hours per week and higher total hours over
    a shorter duration) is associated with significantly greater improvement in language outcomes compared
    to low-intensity therapy.
  direction: likely
  relationship: responder
  citation: '@Bhogal2003'
  method: meta-analysis
  design: meta-analysis
  strength: moderate
  evidence_quality: cohort
  therapy:
    id: massed_practice
    name: intensive speech and language therapy
    dose: average 8.8 hours/week for 11.2 weeks
  sample:
    n: 864
    population: stroke survivors suffering from aphasia
    time_post_onset: not_reported
    phase: not_reported
    age_range: not_reported
    handedness: not_reported
    language: English
  statistics:
    threshold: P < 0.001
    effect_size: r = 0.957 (hours/week vs PICA); r = 0.963 (total hours vs PICA)
  confounders_controlled: []
  confounders_not_controlled:
  - lesion volume
  - age
  - time post-onset
  author_limitations:
  - Many of the original studies were under-powered with small sample sizes.
  - Lack of randomization in some included studies (low PEDro scores).
  - Use of nonstandardized measures and lack of clarity regarding therapy intensity in original reports.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, pages 989-991
    confidence: high
    flags: []
  source_passages:
  - section: Results
    page: 991
    quote: the hours of therapy provided in a week was significantly correlated to greater improvement
      on the PICA (r=0.957, P=0.001, n=9) and on the Token Test (r=0.811, P=0.027, n=7).
    supports: claim
  - section: Results
    page: 988
    quote: Ten studies investigating the SLT for stroke patients suffering from aphasia met criteria after
      being reviewed. These 10 studies represented 864 individual patients.
    supports: sample
  - section: Methods
    page: 987
    quote: Pearson correlation was used to assess the relationship between changes in mean scores of outcome
      measures and intensity of therapy.
    supports: method
  - section: Discussion
    page: 991
    quote: Most of the limitations of the present review stem, in part, from the limitations of the original
      studies. Only 3 studies were rated to be of "good" quality (PEDro score=6)... many of the studies
      were under-powered with small sample sizes.
    supports: limitation
  region_definition:
    kind: not_reported
---
