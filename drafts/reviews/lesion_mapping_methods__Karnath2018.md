---
schema_version: 2.8
id: lesion_mapping_methods__Karnath2018
name: Mapping Human Brain Lesions and Their Functional Consequences
kind: review
status: draft
created_by: agent:ollama-extract-cli/gemma4:31b-it-q8_0
created_on: 2026-10-30
findings:
- id: f1
  target: severity_metric
  target_kind: predictor
  claim: There is a strong coupling between impairment and lesion size in stroke, meaning larger lesions
    are generally more likely to affect critical anatomical structures.
  direction: likely
  relationship: synthesis
  citation: '@Karnath2018'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  author_limitations:
  - Exceptions exist, such as basal ganglia injury associated with lacunar infarction.
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Potential limitations of the mass-univariate approach, page 3
    confidence: high
    flags: []
  source_passages:
  - section: Potential limitations of the mass-univariate approach
    page: 3
    quote: as a rule of thumb there is a strong coupling between impairment and lesion size.
    supports: claim
  - section: Potential limitations of the mass-univariate approach
    page: 3
    quote: We note that there can be exceptions to this, for example when a critical region is connected
      with blood vessels associated with small lesions (e.g., basal ganglia injury can be associated with
      lacunar infarction).
    supports: limitation
- id: f2
  target: severity_metric
  target_kind: predictor
  claim: Voxel-based lesion behavior mapping (VLBM) results can be biased by misplacing inferred critical
    regions towards areas of greater general lesion affection due to the spatial distribution of collateral
    stroke damage.
  direction: likely
  relationship: synthesis
  citation: '@Karnath2018'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  author_limitations: []
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Potential limitations of the mass-univariate approach, page 3
    confidence: high
    flags: []
  source_passages:
  - section: Potential limitations of the mass-univariate approach
    page: 3
    quote: They observed a bias within the lesion-deﬁcit maps, displacing inferred critical regions from
      their true anatomical locations towards areas of greater general lesion affection.
    supports: claim
- id: f3
  target: severity_metric
  target_kind: predictor
  claim: The combined use of correction factors for lesion size and sufficient lesion affection markedly
    reduces the misplacement bias in VLBM results.
  direction: likely
  relationship: synthesis
  citation: '@Karnath2018'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  author_limitations: []
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Potential limitations of the mass-univariate approach, page 3
    confidence: high
    flags: []
  source_passages:
  - section: Potential limitations of the mass-univariate approach
    page: 3
    quote: Sperber and Karnath (2017) observed that the combined use of correction factor 'sufﬁcient lesion
      affection' with correction factor 'lesion size' reduced misplacement markedly and in an additive
      manner, compared to uncorrected VLBM.
    supports: claim
- id: f4
  target: severity_metric
  target_kind: predictor
  claim: Multivariate lesion-behavior mapping is superior to mass-univariate counterparts when a cognitive
    function is organized in multiple, separate brain regions (networks).
  direction: likely
  relationship: synthesis
  citation: '@Karnath2018'
  method: narrative_review
  design: narrative-review
  evidence_quality: narrative-review
  strength: moderate
  author_limitations: []
  provenance:
    extracted_by: agent
    extracted_on: 2026-01-01
    paper_section: Multivariate lesion analysis with machine learning algorithms, page 7
    confidence: high
    flags: []
  source_passages:
  - section: Multivariate lesion analysis with machine learning algorithms
    page: 7
    quote: The authors observed that multivariate lesion-behaviour mapping is superior to its mass-univariate
      counterparts in brain networks, i.e., if a cognitive function is organized in multiple, separate
      brain regions.
    supports: claim
---

This review discusses the evolution of lesion-behavior mapping, contrasting traditional mass-univariate VLBM with emerging multivariate and connectome-based approaches. It highlights critical methodological pitfalls in stroke research, specifically the spatial bias introduced by vasculature and the necessity of controlling for lesion volume.
