---
schema_version: 2.8
id: left_middle_longitudinal_fasciculus
name: "Left Middle Longitudinal Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: left
findings:
  - id: f1
    target: form_to_meaning
    target_kind: impairment
    claim: "The middle longitudinal fasciculus, connecting the angular gyrus to the anterior superior temporal cortex, is proposed to be part of the ventral sound-to-meaning pathway."
    direction: likely
    relationship: synthesis
    citation: "@Dick2012"
    method: narrative_review
    design: narrative-review
    evidence_quality: narrative-review
    strength: weak
    primary_papers_cited:
      - "@Saur2008"
      - "@Wong2011"
    author_limitations:
      - "The pathway is less well-established in humans than in primates, and is absent from several contemporary human white matter atlases."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Middle longitudinal fasciculus: functional and clinical notions, page 12"
      confidence: high
      flags: []
    source_passages:
      - section: "Middle longitudinal fasciculus: functional and clinical notions"
        page: 12
        quote: "Saur and colleagues (2008, 2010) and Wong and colleagues (2011) recently identified the middle longitudinal fasciculus as part of the ventral sound-to-meaning pathway."
        supports: claim
      - section: "Middle longitudinal fasciculus"
        page: 12
        quote: "In contrast, the middle longitudinal fasciculus is less well-established in humans. It is absent in both historic... and contemporary atlases of white matter connectivity"
        supports: limitation
---
