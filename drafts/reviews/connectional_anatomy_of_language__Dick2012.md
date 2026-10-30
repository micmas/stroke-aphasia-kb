---
schema_version: 2.8
id: connectional_anatomy_of_language__Dick2012
name: Consensus and Controversy in the Connectional Anatomy of Language
kind: review
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: left_arcuate_fasciculus
  target_kind: region
  claim: The arcuate fasciculus is traditionally viewed as the primary connection between Wernicke's area
    in the posterior superior temporal cortex and Broca's area in the inferior frontal gyrus, supporting
    the dorsal stream's role in mapping speech sounds to articulatory representations.
  direction: likely
  relationship: synthesis
  citation: '@Dick2012'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Geschwind1965'
  - '@Hickok2007'
  author_limitations:
  - There is no consensus model of SLF/AF connectivity, with conflicting accounts from DTI and primate
    tract-tracing studies.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Fibre pathways of the dorsal stream, pages 5-6
    confidence: high
    flags: []
  source_passages:
  - section: Fibre pathways of the dorsal stream
    page: 5
    quote: This model proposes a dorsal stream for mapping auditory speech sounds to articulatory (motor)
      representations... An emphasis has been placed on superior longitudinal fasciculus/arcuate fasciculus
      (SLF/AF) connectivity for the dorsal stream
    supports: claim
  - section: Superior longitudinal fasciculus/arcuate fasciculus
    page: 5
    quote: the arcuate fasciculus connecting Broca's area... with Wernicke's area (in the posterior superior
      temporal cortex, including the gyrus and sulcus).
    supports: claim
  - section: Summary and concluding remarks
    page: 14
    quote: With respect to the dorsal stream, controversy surrounds... the existence of direct posterior
      temporal-inferior frontal (i.e. Wernicke-Broca) connectivity
    supports: limitation
- id: f2
  target: left_extreme_capsule
  target_kind: region
  claim: The extreme capsule is proposed as a key component of the ventral language stream, connecting
    the anterior inferior frontal gyrus with the middle-to-posterior superior and middle temporal cortex
    to support sound-to-meaning processing.
  direction: likely
  relationship: synthesis
  citation: '@Dick2012'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Saur2008'
  - '@Duffau2005'
  author_limitations:
  - DTI results are inconsistent, with some studies failing to dissociate the extreme capsule from the
    claustrum and external capsule.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: 'Extreme capsule: functional and clinical notions, page 11'
    confidence: high
    flags: []
  source_passages:
  - section: 'Extreme capsule: functional and clinical notions'
    page: 11
    quote: The extreme capsule links the anterior part of the inferior frontal gyrus... with the middle-to-posterior
      portion of the superior and middle temporal cortex... it has therefore been suggested that the extreme
      capsule functions as part of the ventral language system for processing sound-to-meaning
    supports: claim
  - section: Extreme capsule
    page: 11
    quote: Notably, though, the extreme capsule is absent in several other DTI studies... they could not
      dissociate it from the claustrum and external capsule
    supports: limitation
- id: f3
  target: conduction_aphasia
  target_kind: impairment
  claim: While classically attributed to a disconnection of the arcuate fasciculus, conduction aphasia
    is often associated with damage to surrounding grey matter in the insula, superior temporal cortex,
    and inferior parietal lobule, and can occur even in cases of complete SLF/AF agenesis.
  direction: mixed
  relationship: synthesis
  citation: '@Dick2012'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Wernicke1874'
  - '@Bernal2010'
  author_limitations:
  - The diversity of findings may be related to the complex symptomatology of the disorder, including
    repetition deficits, word-finding issues, and phonemic paraphasias.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: 'Superior longitudinal fasciculus/arcuate fasciculus: functional and clinical notions,
      page 8'
    confidence: high
    flags: []
  source_passages:
  - section: 'Superior longitudinal fasciculus/arcuate fasciculus: functional and clinical notions'
    page: 8
    quote: Lesions resulting in conduction aphasia are rarely focal and occur concomitant with damage
      to surrounding grey matter in the insula, superior temporal cortex, and/or inferior parietal lobule...
      even complete agenesis of the left SLF/AF is not associated with conduction aphasic symptoms
    supports: claim
  - section: 'Superior longitudinal fasciculus/arcuate fasciculus: functional and clinical notions'
    page: 9
    quote: This apparent diversity of findings across subtypes of conduction aphasia may be related to
      the complex symptomatology of the disorder
    supports: limitation
- id: f4
  target: left_uncinate_fasciculus
  target_kind: region
  claim: The uncinate fasciculus connects the anterior temporal lobe (including the temporal pole) to
    the inferior frontal cortex and is implicated in semantic processing and auditory working memory.
  direction: likely
  relationship: synthesis
  citation: '@Dick2012'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  primary_papers_cited:
  - '@Papagno2011'
  author_limitations:
  - The specific functional role of the uncinate fasciculus remains to be fully clarified.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: 'Uncinate fasciculus: functional and clinical correlates, page 10'
    confidence: high
    flags: []
  source_passages:
  - section: Uncinate fasciculus
    page: 9
    quote: The uncinate fasciculus is a relatively short pathway connecting anterior temporal to inferior
      frontal areas.
    supports: claim
  - section: 'Uncinate fasciculus: functional and clinical correlates'
    page: 10
    quote: 'there is suggestive evidence for involvement of the uncinate fasciculus in at least two language-related
      functions: semantic processing and auditory working memory/sound recognition.'
    supports: claim
  - section: 'Uncinate fasciculus: functional and clinical correlates'
    page: 10
    quote: what remains to be clarified is its specific function.
    supports: limitation
---
