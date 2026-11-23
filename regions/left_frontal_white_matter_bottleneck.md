---
schema_version: 2.7
id: left_frontal_white_matter_bottleneck
name: Left Frontal White Matter Bottleneck
kind: tract
status: approved
review_tier: legacy
created_by: agent:claude-sonnet-4-6
created_on: 2026-05-06
hemisphere: left
aliases:
- left deep frontal white matter
- left periinsular white matter (medial to insula, lateral to basal ganglia)
- left uncinate/IFOF/ATR convergence zone
- Anterior corona radiata L
- Anterior corona radiata left
- Posterior limb of internal capsule L
- Posterior limb of internal capsule left
- Anterior limb of internal capsule L
- Anterior limb of internal capsule left
networks:
- ventral_semantic
- frontal_semantic_control
notes: 'Draft created 2026-05-06 from Mirman et al. 2015 (Nat Commun 6:6762).

  This entry captures the VLSM finding for the Semantic Recognition factor:

  damage to a white matter region medial to the insula and lateral to the

  basal ganglia (where the uncinate fasciculus, inferior fronto-occipital

  fasciculus, and anterior thalamic radiations converge) is associated with

  multimodal semantic recognition deficits. The authors call this a "frontal

  white matter bottleneck." MNI coordinates from Figure 3: cluster at

  approximately x = -19, z = 4, y = 28 (from panel labels in Figure 3 legend).

  This is a DISTINCT region from the left ATL — the two findings are

  dissociated in the same dataset.

  '
findings: []
source: draft
last_reviewed: '2026-10-22'
reviewer: claude-cowork
reviewed_on: '2026-05-06'
---
# Left Frontal White Matter Bottleneck

## Anatomical context

A region of deep white matter in the left hemisphere, medial to the insula
and lateral to the basal ganglia. Three major white matter tracts converge
here: the uncinate fasciculus (connecting temporal and frontal cortex), the
inferior fronto-occipital fasciculus (connecting frontal to occipital/temporal
cortex), and the anterior thalamic radiations (connecting thalamus to frontal
cortex). The superior longitudinal fasciculus / arcuate fasciculus passes
dorsally to this region and was NOT included in the identified cluster.

This region is NOT the same as the left ATL finding. In the same dataset,
lesions of the left ATL predicted semantic error production, while lesions of
this white matter bottleneck predicted multimodal semantic recognition deficits.
The two findings were statistically dissociated.

## Lesion-symptom evidence

Finding f1 (Mirman et al. 2015, n = 99, VLSM at relaxed FDR q = 0.1): damage
to this convergence zone impairs verbal and non-verbal semantic recognition.
The authors interpret this as disruption of frontal connectivity with the
distributed semantic network, consistent with a semantic control account
(Jefferies & Lambon Ralph 2006) or a multimodal semantic integration account.

## Key mechanistic interpretation

The authors propose two possible mechanisms for the bottleneck effect:
(1) disruption of multimodal integration critical for semantic cognition, or
(2) disruption of frontal semantic control and selection. The paper does not
distinguish between these mechanisms — both remain viable.
