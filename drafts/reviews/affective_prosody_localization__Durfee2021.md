---
schema_version: 2.8
id: affective_prosody_localization__Durfee2021
name: Affective Prosody Localization in Right Hemisphere Stroke
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: affective_prosody_comprehension
  target_kind: impairment
  claim: Damage to postero-lateral (ventral stream) regions of the right hemisphere, particularly the
    temporal lobe, is associated with affective prosody comprehension deficits.
  direction: likely
  relationship: synthesis
  citation: '@Durfee2021'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Ross1981'
  - '@Sheppard2020'
  - '@Starkstein1994'
  author_limitations:
  - Data quality in available studies is a main limitation, with most studies being small (<100 patients).
  - Heterogeneous presentation of study findings renders cross-study statistical comparisons a challenge.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Abstract, Results
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: damage to more postero-lateral (i.e., ventral stream) regions resulted in affective prosody
      comprehension deficits.
    supports: claim
  - section: Results
    page: 6
    quote: Studies in RH acute, subacute, and chronic stroke strongly converge on temporoparietal damage
      and impaired affective prosody recognition.
    supports: claim
  - section: Discussion
    page: 10
    quote: The main limitation of this review is data quality in available studies. Most affective prosody
      studies have been small (<100 patients)
    supports: limitation
- id: f2
  target: affective_prosody_production
  target_kind: impairment
  claim: Damage to antero-superior (dorsal stream) regions of the right hemisphere, primarily the inferior
    frontal lobe, is associated with affective prosody production impairments.
  direction: likely
  relationship: synthesis
  citation: '@Durfee2021'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Ross1981'
  - '@Patel2018'
  - '@Ross2008'
  author_limitations:
  - Data quality in available studies is a main limitation, with most studies being small (<100 patients).
  - Heterogeneous presentation of study findings renders cross-study statistical comparisons a challenge.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Abstract, Results
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: Localized right antero-superior (i.e., dorsal stream) regions contributed to affective prosody
      production impairments
    supports: claim
  - section: Results
    page: 7
    quote: To summarize, expressive aprosodia following RH stroke is most commonly associated with frontal
      lesions, primarily the inferior frontal lobe.
    supports: claim
  - section: Discussion
    page: 10
    quote: The main limitation of this review is data quality in available studies. Most affective prosody
      studies have been small (<100 patients)
    supports: limitation
- id: f3
  target: affective_prosody_shared_processes
  target_kind: impairment
  claim: Right parietal regions appear to serve as shared ground for both affective prosody expression
    and recognition.
  direction: likely
  relationship: synthesis
  citation: '@Durfee2021'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: weak
  primary_papers_cited: []
  author_limitations:
  - The proportions of parietal damage were similar for both receptive and expressive aprosodia, making
    the distinction less clear than for frontal or temporal regions.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Discussion
    confidence: high
    flags: []
  source_passages:
  - section: Discussion
    page: 9
    quote: the parietal lobe serves as shared ground for language production and comprehension processes
      with more anterior portions recruited for expressive affective prosody and posterior portions playing
      an integrative role with both expression and recognition of affective prosody.
    supports: claim
  - section: Results
    page: 9
    quote: There appeared to be a slightly higher proportion of articles reporting parietal damage and
      receptive aprosodia compared to expressive aprosodia (1.14 vs. 0.88), but these ratios were much
      closer and similar in value compared to other RH regions.
    supports: limitation
---

This systematic review synthesizes 50 years of evidence on the localization of affective prosody (aprosodia) in right hemisphere (RH) stroke. It identifies a dual-stream organization mirroring the left hemisphere's propositional language system: a dorsal stream (frontal regions) for production and a ventral stream (temporal/subcortical regions) for comprehension, with the parietal lobe serving as an integrative hub.
