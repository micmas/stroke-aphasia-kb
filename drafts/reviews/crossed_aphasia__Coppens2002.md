---
schema_version: 2.8
id: crossed_aphasia__Coppens2002
name: Crossed Aphasia
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: crossed_aphasia
  target_kind: impairment
  claim: Crossed aphasia (aphasia following a right-hemisphere lesion in right-handed individuals) is
    not a separate clinical entity semeiologically, as its symptom distribution is comparable to that
    of left-hemisphere aphasia.
  direction: likely
  relationship: synthesis
  citation: '@Coppens2002'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: moderate
  author_limitations:
  - The nonstandardized character of published case descriptions leads to variability in detail and time
    post onset.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results and Discussion
    confidence: high
    flags: []
  source_passages:
  - section: Introduction
    page: 3
    quote: It became progressively clear that CA could not be distinguished from left-hemisphere aphasia
      simply on the basis of an individual patient's symptomatology.
    supports: claim
  - section: Methods
    page: 4
    quote: The purpose of the present review was to collate all available CA cases to date, including
      the Japanese cases, to analyze (a) the frequency of specific symptoms, (b) the possible differences
      between CA and left-hemisphere aphasia...
    supports: method
  - section: Discussion
    page: 20
    quote: In conclusion, a thorough analysis of published CA cases showed that these patients are comparable
      to LHA subjects in terms of age, gender distribution, and aphasia type distribution.
    supports: claim
  - section: Discussion
    page: 29
    quote: The limitations of this review are inherent to the nonstandardized character of published CA
      case descriptions.
    supports: limitation
- id: f2
  target: crossed_aphasia
  target_kind: impairment
  claim: Male patients with crossed aphasia are significantly more likely than female patients to have
    a positive history of familial sinistrality.
  direction: likely
  relationship: synthesis
  citation: '@Coppens2002'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: moderate
  author_limitations:
  - Familial sinistrality is difficult to establish accurately in most cases and may be influenced by
    family size.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: However, male were significantly more likely than female CA subjects to show a positive history
      of familial sinistrality.
    supports: claim
  - section: Results
    page: 18
    quote: However, there was a significant difference between the frequency of familial sinistrality
      (Yates corrected v2 = 5.021, df = 1, p = .025). A history of familial sinistrality was significantly
      more frequent in male than in female CA subjects.
    supports: claim
  - section: Discussion
    page: 28
    quote: As a caveat, we would strongly underscore that familial sinistrality is rather difficult to
      establish in most CA cases.
    supports: limitation
- id: f3
  target: crossed_aphasia
  target_kind: impairment
  claim: Oral praxis tends to lateralize with language skills, as evidenced by the higher prevalence of
    oral apraxia compared to limb apraxia in crossed aphasia.
  direction: likely
  relationship: synthesis
  citation: '@Coppens2002'
  method: narrative_review
  design: systematic-review
  evidence_quality: narrative-review
  strength: moderate
  author_limitations:
  - Frequency of apraxia of speech could not be computed due to inconsistent reporting in original case
    studies.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Discussion
    confidence: high
    flags: []
  source_passages:
  - section: Discussion
    page: 22
    quote: These figures now confirm that oral apraxia is almost three times more prevalent in CA than
      limb apraxia, which in turn supports the hypothesis that oral praxis tends to lateralize with language
      skills whereas limb praxis tends to lateralize with hand dominance.
    supports: claim
  - section: Discussion
    page: 26
    quote: The frequency of apraxia of speech could not be computed because too many authors have failed
      to specifically report this type of apraxia.
    supports: limitation
---
