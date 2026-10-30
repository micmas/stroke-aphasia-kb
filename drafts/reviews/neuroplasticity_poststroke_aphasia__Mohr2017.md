---
schema_version: 2.8
id: neuroplasticity_poststroke_aphasia_mohr2017
name: "Neuroplasticity and Functional Recovery after Intensive Language Therapy in Chronic Post Stroke Aphasia"
kind: classical
status: draft
created_by: "agent:ollama-extract-cli/gemma4:31b-it-q8_0"
created_on: 2026-10-30
findings:
  - id: f1
    target: neuroplasticity
    target_kind: impairment
    claim: "Intensive aphasia treatment in chronic patients leads to reorganization of both functional and structural language networks in both the left and right hemispheres."
    direction: likely
    relationship: synthesis
    citation: "@Mohr2017"
    method: narrative_review
    design: narrative-review
    evidence_quality: narrative-review
    strength: moderate
    author_limitations:
      - "Findings are inconsistent due to heterogeneity of patient-specific variables (lesion size, site, severity) and non-patient factors (imaging method, task, therapy intensity)."
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Neuroplastic Changes in the Left and Right Hemisphere following Intensive Short-Term Aphasia Therapy"
      confidence: high
      flags: []
    source_passages:
      - section: "Neuroplastic Changes in the Left and Right Hemisphere following Intensive Short-Term Aphasia Therapy"
        page: 3
        quote: "Overall, evidence suggests that intensive aphasia treatment in chronic PSA leads to reorganization of the functional and structural language network in both hemispheres."
        supports: claim
      - section: "The Relevance of Neuroscience-Based Treatment for Post Stroke Aphasia"
        page: 1
        quote: "The reasons for the heterogeneity of previous results may be attributed to patient-specific variables such as lesion size and site, symptom severity, etc. [\dots] the specific impact of non-patient factors (e.g., neuroimaging method, language task, therapy method, intensity, amount, and duration) has rarely been addressed."
        supports: limitation

  - id: f2
    target: massed_practice
    target_kind: therapy
    claim: "High intensity and massed practice facilitate cortical plasticity and learning by strengthening synaptic contacts and correlating neuronal activity."
    direction: likely
    relationship: synthesis
    citation: "@Mohr2017"
    method: narrative_review
    design: narrative-review
    evidence_quality: narrative-review
    strength: moderate
    author_limitations: []
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Neuroplasticity After Intensive Aphasia Treatment Methods"
      confidence: high
      flags: []
    source_passages:
      - section: "Neuroplasticity After Intensive Aphasia Treatment Methods"
        page: 2
        quote: "The efficacy of intensive therapies can be explained by neuroscientific principles of learning and memory: high intensity and massed practice facilitates and enhances learning and cortical plasticity by correlated neuronal activity and by strengthening of synaptic contacts between neurons."
        supports: claim

  - id: f3
    target: severity_metric
    target_kind: predictor
    claim: "Symptom severity is a relevant factor that may explain the variability of neuroplastic changes following therapy."
    direction: likely
    relationship: synthesis
    citation: "@Mohr2017"
    method: narrative_review
    design: narrative-review
    evidence_quality: narrative-review
    strength: weak
    author_limitations: []
    provenance:
      extracted_by: "agent"
      extracted_on: 2026-01-01
      paper_section: "Neuroplastic Changes in the Left and Right Hemisphere following Intensive Short-Term Aphasia Therapy"
      confidence: high
      flags: []
    source_passages:
      - section: "Neuroplastic Changes in the Left and Right Hemisphere following Intensive Short-Term Aphasia Therapy"
        page: 2
        quote: "Several factors might explain this variability of previous findings and could be relevant for interpreting treatment-related data and for identifying predictors of recovery. These factors include the phase of PSA [\dots], symptom severity (Lazar et al., 2010), or education and cognitive reserve."
        supports: claim
---

This is a narrative review discussing the factors influencing neuroplasticity after intensive aphasia therapy in chronic stroke patients. It synthesizes evidence regarding the role of intensity, therapy method, and patient variables.
