---
schema_version: 2.8
id: language_mapping_methods__Wilson2019
name: Language Mapping Methods in Aphasia
kind: classical
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: semantics
  target_kind: impairment
  claim: Adaptive semantic matching paradigms are feasible, reliable, and valid for mapping core perisylvian
    language regions in individuals with aphasia, outperforming narrative comprehension and picture naming.
  direction: likely
  relationship: synthesis
  citation: '@Wilson2019'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Wilson2018'
  author_limitations:
  - Validity was assessed in neurologically normal participants because there is no ground truth for language
    organization in aphasia.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Results, page 3937; An Adaptive Semantic Matching Paradigm, page 3941
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: We found that the adaptive semantic matching paradigm could be performed by most individuals
      with aphasia and yielded reliable and valid maps of core perisylvian language regions in each individual
      participant.
    supports: claim
  - section: Abstract
    page: 1
    quote: The psychometric properties of this paradigm were superior to those of other commonly used
      paradigms such as narrative comprehension and picture naming.
    supports: claim
  - section: An Adaptive Semantic Matching Paradigm
    page: 3
    quote: It is difficult to evaluate validity directly in individuals with aphasia, because the nature
      of their language organization is unknown. That is, there is no ground truth against which to assess
      validity.
    supports: limitation
- id: f2
  target: phonological_production
  target_kind: impairment
  claim: Adaptive rhyme judgment paradigms can reliably identify left-lateralized fronto-parietal regions,
    specifically the supramarginal gyrus and ventral precentral gyrus, involved in phonological encoding.
  direction: likely
  relationship: synthesis
  citation: '@Wilson2019'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Yen2019'
  author_limitations:
  - Syllable counting was found to be less reliable than rhyme judgment.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Identification of Phonological Encoding Regions, page 3941
    confidence: high
    flags: []
  source_passages:
  - section: Abstract
    page: 1
    quote: The adaptive rhyme judgment paradigm was capable of identifying fronto-parietal phonological
      encoding regions in individual participants.
    supports: claim
  - section: Identification of Phonological Encoding Regions
    page: 7
    quote: 'Both phonological paradigms activated the two key phonological encoding regions that have
      been motivated by the prior literature: the left supramarginal gyrus and the left ventral precentral
      gyrus...'
    supports: claim
  - section: Identification of Phonological Encoding Regions
    page: 7
    quote: We found that the rhyme judgment paradigm was comparable in reliability to the semantic matching
      paradigm, whereas the syllable counting paradigm was somewhat less reliable.
    supports: limitation
---

This review summarizes the development and validation of adaptive fMRI paradigms for language mapping in aphasia, emphasizing the superiority of adaptive semantic matching and rhyme judgment tasks over traditional paradigms.
