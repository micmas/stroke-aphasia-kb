---
schema_version: 2.8
id: thalamic_aphasia__Fritsch2022
name: Thalamic Aphasia
kind: impairment
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: anomia
  target_kind: impairment
  claim: Aphasia after thalamic lesions is typically mild and characterized predominantly by lexical-semantic
    deficits, specifically anomia and semantic paraphasias.
  direction: likely
  relationship: synthesis
  citation: '@Fritsch2022'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Radanovic2017'
  - '@Rangus2022'
  author_limitations:
  - Many reported data were collected prior to routine MRI availability and neurocognitive assessment
    was rarely standardized.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Clinical Presentation and Phenotypes of Thalamic Aphasia, page 2
    confidence: high
    flags: []
  source_passages:
  - section: Clinical Presentation and Phenotypes of Thalamic Aphasia
    page: 2
    quote: Overall, aphasia after thalamic lesions has mostly been described as mild, with predominantly
      lexical-semantic deficits [35, 39]. This means that patients exhibit anomia, or naming deficits,
      in speaking and writing while substituting with semantic paraphasias...
    supports: claim
  - section: Clinical Presentation and Phenotypes of Thalamic Aphasia
    page: 3
    quote: Critically, however, a relevant amount of the reported data has been collected prior to MRI
      being routinely available, and neurocognitive assessment was rarely standardized.
    supports: limitation
- id: f2
  target: fluency
  target_kind: impairment
  claim: Lesions to the anterior thalamic nuclei are associated with reduced word fluency and overall
    higher aphasia severity.
  direction: likely
  relationship: synthesis
  citation: '@Fritsch2022'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: weak
  primary_papers_cited:
  - '@Rangus2022'
  author_limitations:
  - Most studies are based on small samples with differing quality of language assessment and imaging
    techniques.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Anatomy of Thalamic Aphasia, page 3-4
    confidence: high
    flags: []
  source_passages:
  - section: Anatomy of Thalamic Aphasia
    page: 3
    quote: For example, lesions to the pulvinar are more often associated with fluent aphasia including
      naming deficits and semantic paraphasias, while lesions to the anterior nuclei can lead to reduced
      word fluency and show an overall higher severity.
    supports: claim
  - section: Anatomy of Thalamic Aphasia
    page: 4
    quote: Most of the aforementioned studies are based on small samples with differing quality of language
      assessment and imaging techniques, rendering specific differentiations of phenotypes difficult.
    supports: limitation
- id: f3
  target: left_thalamus
  target_kind: region
  claim: Aphasia is predominantly associated with lesions or electrode placement in the left thalamic
    areas, particularly the left anterior region.
  direction: likely
  relationship: synthesis
  citation: '@Fritsch2022'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Rangus2022'
  author_limitations:
  - Handedness was often not tested, and language impairment was often assessed in patients with left-sided
    thalamic lesions only.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Lateralization, page 4
    confidence: high
    flags: []
  source_passages:
  - section: Lateralization
    page: 4
    quote: studies of patients with thalamic strokes, or following DBS placement, have reported aphasia
      to be predominantly associated with lesions, or electrode placement, in left thalamic areas [16-20,
      24, 81].
    supports: claim
  - section: Lateralization
    page: 4
    quote: Unfortunately, handedness was often not tested, and language impairment was often assessed
      in patients with left-sided thalamic lesions only, limiting these results [24, 38].
    supports: limitation
---

# Thalamic Aphasia Review

This entry synthesizes the clinical presentation and neuroanatomy of thalamic aphasia as reviewed by Fritsch et al. (2022). The disorder is characterized primarily by lexical-semantic retrieval deficits (anomia) and is typically associated with left-hemisphere thalamic damage, though phenotypes vary by specific nucleus involved.
