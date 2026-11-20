---
schema_version: 2.8
id: left_temporobasal__Goldenberg1994
name: Left Temporobasal Cortex (basal temporal lobe / entorhinal–perisylvian junction)
kind: classical
status: approved
review_tier: legacy
created_by: agent:claude-opus-4-7
created_on: 2026-05-07
hemisphere: left
aliases:
- left basal temporal lobe
- left temporo-basal cortex
- basal portion of left temporal lobe
- left entorhinal cortex (adjacent)
networks:
- ventral_language
- hippocampal_perisylvian_disconnection
findings: []
source: curated
last_reviewed: 2026-05-07
notes: 'Goldenberg & Spatt 1994 (Brain Lang 47:684–698). Vienna cohort, n=18 chronic

  left-hemisphere stroke aphasia patients followed across three 8-week phases:

  spontaneous recovery, intensive language therapy (2 × 45 min × 5 days/wk),

  and post-therapy observation. Outcome = AAT mean profile level.


  This draft captures the paper''s *site*-specific finding: among the regions

  considered (Wernicke''s area, adjacent superior/middle temporal gyrus, inferior

  parietal lobe, and basal temporal lobe), only temporobasal damage produced a

  selective deficit in therapy benefit that survived lesion-size matching. The

  spontaneous-recovery phase was not impaired in this subgroup. The authors''

  proposed mechanism is hippocampal–perisylvian disconnection (via entorhinal

  cortex), blocking explicit/declarative learning of linguistic knowledge and

  compensatory strategies (procedural learning is presumed spared and to drive

  spontaneous recovery and the lesion-size effect).


  This is encoded as relationship: responder + direction: unlikely_responder

  because the claim is about a lesion pattern moderating *therapy gain* rather

  than a damage→impairment claim. The lesion-volume effect on overall recovery

  is captured in the companion predictor draft

  (drafts/predictors/lesion_volume__Goldenberg1994.md).


  Forward-looking target id `prognosis` is a top-level prognosis target — the

  paper''s outcome is "responsiveness to intensive language therapy" rather

  than a specific impairment.


  OCR caveats: the PDF text layer has scattered character errors typical of

  1994 scans; quotes are reproduced as the OCR rendered them so that the

  annotator''s `Ctrl+F` matching works against the same text layer.'
reviewer: cowork-claude:sonnet-4-6
reviewed_on: '2026-05-07'
---
# Left Temporobasal Cortex — therapy-responsiveness moderator (Goldenberg & Spatt 1994)

## Anatomical context

Basal portion of the left temporal lobe — the under-surface of the temporal
lobe abutting the parahippocampal gyrus. CT lesions in this region either
directly impinge on or sit very close to entorhinal cortex, the major relay
between neocortical association areas and the hippocampus. The authors
hypothesise that damage here disconnects the hippocampal formation from
perisylvian language cortex, blocking explicit (declarative) learning of
new or compensatory linguistic knowledge — while sparing procedural-learning
mechanisms presumed to drive spontaneous recovery.

## Key result by phase (Tables 4–6)

| Comparison                                      | Spontaneous     | Therapy         | Total           |
|-------------------------------------------------|-----------------|-----------------|-----------------|
| All temporobasal vs none (Table 4, 6 vs 12)     | 1.8 vs 4.1 ns   | 1.5 vs 4.6 **p=.002** | 2.2 vs 7.3 **p=.006** |
| Size-matched (Table 5, 5 vs 5)                  | 1.8 vs 2.9 ns   | 1.5 vs 4.5 **p=.02**  | 2.2 vs 5.3 p=.08      |
| Size + onset matched (Table 6, 3 vs 5)          | 2.4 vs 2.9 ns   | 1.9 vs 4.5 **p=.05**  | 3.1 vs 5.3 ns         |

The therapy-phase deficit survives both lesion-size matching and time-post-onset
matching; the spontaneous-recovery deficit does not.

## Subtest pattern (Table 7, size-matched groups)

The differential effect on therapy gain was strongest for Comprehension,
Repetition, and Written language; least for Naming and the Token Test.

## Caveats

- n=18 overall; the most stringent comparison rests on n=3 vs n=5.
- Multiple univariate tests, no multiple-comparisons correction (authors note).
- CT-based 2D template tracing; entorhinal involvement inferred from CT
  proximity rather than directly visualised.
- Disconnection mechanism is hypothesised, not demonstrated. The authors
  themselves describe the discussion as highly speculative.
