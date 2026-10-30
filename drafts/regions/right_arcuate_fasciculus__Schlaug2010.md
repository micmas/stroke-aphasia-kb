---
schema_version: 2.8
id: right_arcuate_fasciculus
name: "Right Arcuate Fasciculus"
kind: tract
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
hemisphere: right

findings:
  - id: f1
    target: melodic_intonation_therapy
    target_kind: therapy
    claim: "Intense melodic intonation therapy is associated with an increase in the size and fiber length of the right arcuate fasciculus."
    direction: likely
    relationship: treatment_response
    citation: "@Schlaug2010"
    method: DTI
    design: case-series
    strength: moderate
    evidence_quality: cohort
    sample:
      n: 1
      population: "patient treated with MIT"
      time_post_onset: not_reported
      phase: chronic
      age_range: not_reported
      handedness: not_reported
      language: not_reported
    statistics:
      threshold: not_reported
      effect_size: not_reported
      p_value: not_reported
    confounders_controlled: []
    confounders_not_controlled: []
    region_definition:
      kind: tract
      description: "Right arcuate fasciculus (AF)"
    imaging_details:
      reference_space: not_reported
      atlases_used: []
      preprocessing_pipeline: not_reported
    author_limitations:
      - "The most likely explanation for these imaging results are changes in myelination... however, changes in axon diameter... are also possible."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Results, page 659"
      confidence: high
      flags: ["n=1 for DTI finding"]
    source_passages:
      - section: "Results"
        page: 659
        quote: "There is a visible increase in the size (number of fibers and volume of tract) and length of fibers of the right arcuate fasciculus when the acquisition before therapy (A) is compared with the acquisition after therapy (B)."
        supports: claim
      - section: "Results"
        page: 659
        quote: "The most likely explanation for these imaging results are changes in myelination [48-50]; however, changes in axon diameter owing to changes in myelin or axon density, themselves owing to axonal sprouting, are also possible [51-53]."
        supports: limitation
    therapy:
      id: melodic_intonation_therapy
      name: "Melodic Intonation Therapy"
      dose: "up to 1.5 h/day, 5 days/week over a period of several months"
---
