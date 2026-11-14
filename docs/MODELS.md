# Local models

The supported extraction workflow uses two independent local extractors, followed
by a separate local source reviewer. See [HOWTO](HOWTO.md) for the complete process.
Models run through Ollama on the local machine. Install the chosen model tags
before starting a batch; available hardware and context capacity constrain the
size of paper that can be processed.

| Role | Configuration | Current behavior |
|---|---|---|
| Extractor A and B | `kb.py extract --profile relationships --models MODEL_A MODEL_B` | Defaults: `gemma4:31b`, `qwen3.8:27b`; independent passage classification and table-image transcription, serial calls |
| Source reviewer | `kb.py review --model MODEL` | Required explicitly; the relationship reviewer selects a study frame and proposes source-linked relationships in small groups |
| Visual verification | Main PDF source review | Table images, figures, anatomy and source inconsistencies still require independent checking |

A reviewer must differ from both extractors. The reviewer checks model tags and
currently installed digests to reject aliases of the same weights. The experimental relationships profile records extraction-time identities. Historical
extraction runs did not record extraction-time digests, so current digest checks
cannot establish which weights a tag referred to in the past. Prefer a different
model family, record the chosen version, and inspect a small review pilot before
running the whole corpus. No reviewer is yet established as the most accurate.

The relationship profile caps extraction passage calls at 4,000 and table calls at
10,000 output tokens. Review caps the frame at 4,000 and relationship calls at
6,000, or a smaller requested `--max-output-tokens` budget. Calls record temperature,
seed, reasoning setting and actual model digest. Input capacity and output allowance
are different limits: increasing output tokens cannot fix an oversized input.
Relationship extraction creates small tasks internally; omit `--segment-chars`.
The review frame still reads the whole main-paper text and can reach an input
limit. Oversized or truncated calls fail instead of silently dropping pages.

Older `analyses` runs remain readable by the compatibility path, which uses its
own inventory reconciliation. Do not compare its output counts or timings directly
with the relationship method.

## What has been established

Manual source audits found complementary coverage from the two extractors and
errors shared by both. Reconciliation can identify omissions and disagreements,
but valid JSON, matching quotations and agreement do not establish semantic
accuracy. A controlled, source-verified comparison has not established a numerical
accuracy advantage over single-model extraction. The dual workflow is the current
corpus evaluation workflow, not a claim of validated superiority.

Compare methods against the same independently checked main PDFs, counting
unsupported or incorrect claims, omitted important results, and critical errors in
numbers, anatomy, adjustment or interpretation. Include difficult tables, null
results, long papers and diverse study designs. Keep the reference review separate
from the model outputs and report disagreements and uncertainty. Adopt a common
method across the KB once this comparison supports it; every replacement still
needs source verification and approval.

## Experimental relationship evidence

`kb.py extract --profile relationships` uses the same two independent local models
with small passage-classification calls and individual table-image calls. It
preserves original source evidence instead of accepting a freely written model
summary as a clinical finding. Population, personal-factor and adjustment passages are surfaced by
classifications and deterministic search tags, without a separate generated summary. No model has been selected as a universal winner.

Development source audits found that this approach retained important qualifiers
lost by earlier summaries: changes after adjustment, baseline-dependent effects,
non-significant comparisons, population restrictions and timing. The audits also
found a prior-study result misclassified by both models and persistent table-header
disagreements. Those failures demonstrate why source review remains necessary.
Evidence-location coverage is not the accuracy of a finished clinical relationship.

A two-paper fresh-source validation (OsaGarcia2020 and White2024) completed
with Qwen and Gemma using the same prompts. Summed model-call times were about
7 and 12 minutes per paper for both models combined, excluding source review.
These totals combine exact reused calls and new local calls; they are not fresh
end-to-end benchmarks. OsaGarcia's audit located all ten reference evidence
groups, but some coefficient-level evidence remained in an unresolved table.
White2024's blind-reference audit located all seven relationship groups and their
qualifiers; all six tables matched the checked source values. Its ROI rankings
still require interpretation as model importance, and its chronic outcome status
must not be recast as observed recovery. These audits used both PDF images and
text; they do not constitute exhaustive visual verification of every figure.
This supports further source-review testing, not a claim of complete automated
clinical extraction or a model ranking.

A selection-based source-review aid is available through `kb.py review`. It is
incomplete and does not map to the KB promotion schema. Checking every proposal
is not a completeness check; read all original Results passages, tables and figures. It requires a different recorded model digest from
both extractors; different sizes in the same model family can still share errors.
Do not treat successful calls,
complete ID coverage, or matching transcriptions as approval. Evaluate new papers
and the subsequent review step before a corpus migration. Timing depends on the
hardware, weights and source complexity; the saved run metadata is authoritative.

## Review evaluation and limits

The selected review-aid candidate is **gemma4:26b**, with reasoning disabled.
This is a practical choice for provisional triage, not a claim that it is the best
scientific reviewer. The prompt was tuned on OsaGarcia2020, then frozen for
White2024 against its existing blind reference.

| Review test | Time | Source-audit result |
|---|---|---|
| OsaGarcia2020 development regression | 56 seconds | 22 proposals; seven unflagged proposals correct. Flagged errors and missing proposals remained. |
| White2024 first review validation | 239 seconds | 39 proposals; three of seven relationship families covered, four partial. Of eight unflagged proposals, two were correct and six needed discarding. |

Every missing Results passage was retained in the coverage list. This supports
use as a **triage sheet over the complete literal evidence**, not as a complete
list of relationships to approve. Final code checks flag merged analyses and
model-metric directions, hold runaway context slots, and show timing/role guesses
as unverified beside their sources. Those diagnostic changes were checked on the
saved outputs; original model responses remain unchanged.

A matched eight-passage comparison took 19 seconds with Gemma 26B, 184 seconds
with Granite 30B and 73 seconds with Ornith 122B. Gemma had no critical error in
that narrow block but still had source-link and category problems; Granite merged
analyses incorrectly; Ornith failed verbatim-label requirements. These small tests
are not a whole-paper ranking. Ornith's subsequent full-paper frame hit the
4,000-token cap and did not complete. A Gemma reasoning-enabled probe exhausted
12,000 tokens in 150 seconds without an answer; plain JSON mode failed the category
schema in 23 seconds. Neither alternative was adopted.

Repeated calls differed despite identical prompt hashes, temperature 0 and seed 7;
the cause was not determined. Do not promise reproducible answers from settings
alone. Keep the raw responses, model digest and code/source hashes. Human review
time saved by the sheet has **not** been measured. Start review with about 20
papers and compare the aid with the evidence packet on five before scaling review.
No clinical findings were approved, replaced or published by these tests.

## Other configuration

`models.yaml` serves existing screening, report-generation and compatibility tools.
It does **not** choose the models for `kb.py extract` or `kb.py review`; those use
the command options above. Saved run settings, prompts and hashes are the record
of what was used. Do not modify code, prompts or settings underneath an active run.

Consult each model's own licence before deployment or redistribution. Repository
code licensing does not grant rights to model weights or source papers.
