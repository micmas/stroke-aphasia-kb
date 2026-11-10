---
schema_version: 2.8
id: crossed_aphasia
name: Crossed Aphasia
kind: impairment
short_definition: Acquired language disturbance caused by a lesion in the cerebral hemisphere ipsilateral
  to the dominant hand (typically a right-hemisphere lesion in right-handed individuals).
assessment: []
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b
created_on: 2026-11-10
findings:
- id: f1
  target: crossed_aphasia
  target_kind: impairment
  claim: The symptomatology of crossed aphasia is comparable to that of left-hemisphere aphasia, with
    Broca aphasia being systematically the most frequent type.
  direction: likely
  relationship: causal
  citation: '@Coppens2002'
  method: behavioral_only
  design: cross-sectional
  strength: moderate
  evidence_quality: cohort
  sample:
    n: 167
    population: right-handed individuals with right-hemisphere cerebrovascular accidents and acquired
      language impairment
    time_post_onset: not_reported
    phase: not_reported
    age_range: mean 57.34 years
    handedness: strongly right-handed
    language: not_reported
  statistics:
    threshold: not_reported
    effect_size: not_reported
  confounders_controlled: []
  confounders_not_controlled:
  - ' time post onset'
  author_limitations:
  - The nonstandardized character of published case descriptions leads to variability in detail and time
    post onset.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, Discussion
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: Results suggested that the CA population is comparable to the left-hemisphere patient population.
    supports: claim
  - section: Discussion
    page: 20
    quote: The only conclusion that can be drawn from a comparison between all these studies is that Broca
      aphasia is systematically the most frequent. This observation seems to be valid for CA also.
    supports: claim
  - section: Methods
    page: 4
    quote: The inclusion criteria included (a) a clear right hemisphere cerebrovascular accident, (b)
      a strongly right-handed patient, (c) a diagnosis of acquired language impairment
    supports: sample
  - section: Discussion
    page: 29
    quote: The limitations of this review are inherent to the nonstandardized character of published CA
      case descriptions.
    supports: limitation
  region_definition:
    kind: not_reported
---
