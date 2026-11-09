# From a PDF to an approved entry

This is the walk through one paper: it arrives as a PDF, a local model
drafts its findings, the drafts are checked, a person (or, for routine
findings, a second model) reads them against the paper, and what holds
up is approved into the knowledge base. Six steps; the first three are
mostly automatic and take minutes, the last three are where you spend
judgement.

Which papers get this treatment is decided before this page starts:
papers are found and chosen under the screening protocol
([SCREENING.md](SCREENING.md)), and `screen.py register` writes the
bibliography entry for each one included. Every command here is listed
with all its options in [COMMANDS.md](COMMANDS.md); the rules on who may
approve what are in [GOVERNANCE.md](GOVERNANCE.md).

Everything runs on your own machine. The paper's text goes to a local
model through Ollama and nowhere else; there is no API key and no
per-paper cost.

## In short

```bash
cp ~/Downloads/Foo2024.pdf papers/
python scripts/intake_papers.py --execute
python scripts/extract.py --pdf papers/Foo2024.pdf
python scripts/aphasia_kb.py --check drafts/
python scripts/auto_review.py --all --llm-review --require-pdf-match
python scripts/review_app.py --citation Foo2024
python scripts/promote.py --approve drafts/<bucket>/<entry>__Foo2024.md --reviewer michele
git add -A && git commit -m "Foo2024 extraction" && git push
```

The rest of this page says what each step does and what to look at.

## 1. The PDF

Drop it into `papers/` under any name. `papers/` is the OneDrive folder
`calmar-papers` on the maintainer's machine and is never committed; the
PDFs are copyright. Then:

```bash
python scripts/intake_papers.py --execute
```

This gives the paper a bibliography entry if it has none (from its DOI,
via Crossref), renames the file to `<Key>.pdf`, strips publisher cover
sheets and OCRs scanned pages, so the extractor reads text and not
pixels. Every step is a dry run without `--execute`, and every step is
safe to repeat.

## 2. Extract

```bash
python scripts/extract.py --pdf papers/Foo2024.pdf
```

The script reads the PDF, sends the extraction instructions
([EXTRACTION_SKILL.md](EXTRACTION_SKILL.md)), the schema and the paper's
text to the local model, and writes one draft per entry the paper speaks
to into `drafts/<bucket>/<entry>__Foo2024.md`. It then highlights every
quoted passage in a copy of the PDF, `papers/Foo2024_annotated.pdf`, and
appends a line to `logs/extraction_log.md`. Expect 20–40 minutes per
paper on the 31B model.

**Which model.** The choice lives in `models.yaml`, one line per role:
`extract` (the hard one: a 50 000-token paper in, structured findings
out; currently Gemma 4 31B, `gemma4:31b-it-q8_0`), `review` (the
independent second reading; Gemma 4 26B) and `rag` (writes the report
prose). [MODELS.md](MODELS.md) explains the choice and how to test a
new candidate with `benchmark_models.py`. To try a model without
editing anything: `APHASIA_LOCAL_MODEL=<tag> python scripts/extract.py …`,
or `--pick-model` to choose from the models you have pulled. Every
script prints which model it resolved and why.

**Watching it run.** A background monitor prints one line when the
model returns, e.g. `GPU offload min 100% / avg 100% · RAM peak 63% ✓
stayed fully on GPU`. The number that matters is the GPU offload: below
100 % the model has spilled to CPU and everything is ten times slower.
If that happens, lower `num_ctx` for the role in `models.yaml` or use a
smaller model. (`ollama ps` shows the same thing live; its CONTEXT
column reflects whatever last used the model and does not limit these
scripts, which set the context size on every request.)

**When something goes wrong**

| You see | It means | Do |
|---|---|---|
| `Couldn't reach Ollama` | the server is not running | `ollama serve` |
| 404 on the model | not pulled | `ollama pull <tag>` |
| "prompt filled num_ctx" | the paper was cut off | raise `--num-ctx` |
| "0 drafts returned" | the model ignored the JSON contract, or the paper was cut off | read `_last_extraction_response_*.txt`; raise `--num-ctx` |
| process killed, empty reply | out of memory | lower `--num-ctx` or use a smaller model |
| "output hit num_predict" | the answer was cut off | raise `--max-tokens` |
| very slow, `ollama ps` not `100% GPU` | the context no longer fits in memory | lower `num_ctx` in `models.yaml` |

Do one paper before a batch, to see the real timing on your machine.

## 3. Check the drafts

```bash
python scripts/aphasia_kb.py --check drafts/
```

The validator names every file, finding and field that breaks the
schema; the expected output is `issues: 0`. Fix what it names in your
editor and run it again. Re-extracting a paper overwrites its drafts,
so commit any hand edits first.

## 4. Review

Two automatic passes, then a person.

```bash
python scripts/auto_review.py --all
python scripts/auto_review.py --all --llm-review --require-pdf-match
```

The first pass runs deterministic checks on every draft (schema, every
quote found in the PDF, no low-confidence findings, no "verify me"
flags) and sorts it into a tier. Nothing is approved by these checks;
they can only pass a draft on, defer it or reject it. The second pass
is the second reading: an independent local model (a different model
from the extractor, `review` in `models.yaml`) re-reads the paper's text
and answers, finding by finding, whether each passage is there, supports
the field it is tagged for, whether the relationship and strength are
faithful, whether the numbers match and the authors' limitations are
captured. Each draft gets a worksheet in `logs/auto_review/<draft>.yaml`.

**Tiers.** Tier A can be approved by the model: the draft adds findings
to an existing region, impairment or predictor entry, every passage
matched exactly, confidence is high or medium, there are no flags,
strength is weak or moderate, and the evidence is primary quantitative
data. Everything else is Tier B and waits for a person; that is always
the case for therapies, ingredients, reviews, new entries, strong claims
and anything flagged (including `abstract_only`).

**How the model's approval is kept safe.** It counts only if the draft
is Tier A, the reviewer model differs from the extractor, the paper's
text was available, and three independent runs agree; a `reject` is
always honoured; anything else is recorded and left for you. Everything
that fires is written under `llm_review.guardrails` in the worksheet.
A wrong approval is the most expensive mistake in the pipeline, so every
net fails towards "a person looks".

**Auditing.** After every twenty model approvals, or monthly, a person
re-reads a random fifth (at least three) against the PDFs and logs
`AUDIT | pass|fail`. One real failure pauses model approval
(`--no-model-approve`) and sends the entries since the last clean audit
back to a person. The report marks model-approved findings and can be
told to use only human-approved ones.

**The reading itself**, draft and paper side by side:

```bash
python scripts/review_app.py --draft drafts/<bucket>/<entry>__Foo2024.md
```

Findings on the left, every page of the paper on the right with the
passages highlighted in the colour of what they support. Fix a quote,
page or tag in place; remove a passage that does not say what the
finding claims; change claim, direction, relationship, strength or
confidence when the paper says otherwise. Drag across words in the paper
to quote them into a finding. When you read something no finding covers,
select it and mark it for re-extraction with a note; then

```bash
python scripts/refocus.py drafts/<bucket>/<entry>__Foo2024.md --execute
```

has the model write findings for exactly those passages, which land in
the same draft for you to review. Saving stamps your name on each
finding you changed, logs `REVIEW-EDITED` and regenerates the annotated
PDF. A draft with a pending mark cannot be approved.

Two things to check on every finding: the **target** (a naming score
targets `anomia`; a syndrome such as `anomic_aphasia` only when the
paper classified patients that way) and, for treatment findings, the
**therapy** box, which names the intervention as the paper does.

Collaborators do the same step in the browser through the review
portal ([PORTAL.md](PORTAL.md)); their decisions arrive as records you
apply with `portal_import.py`.

## 5. Decide

For a draft you have read:

```bash
python scripts/promote.py --approve drafts/<bucket>/<entry>__Foo2024.md --reviewer michele
python scripts/promote.py --reject  drafts/<bucket>/<entry>__Foo2024.md --reviewer michele --reason "…"
```

For many deferred drafts at once, a worksheet: `auto_review.py --all
--emit-worksheet worksheet.yaml` lists each draft with its findings and
their claim passages; you fill in `verdict: approve | agree_defer |
reject` and a rationale (and, if you like, a note per finding), then
`auto_review.py --apply-verdicts worksheet.yaml --reviewer michele` runs
`promote.py` for each `approve`. The verdict must be spelled exactly
`approve`.

`promote.py` is the only way into the approved folders. It validates
once more, stamps `status: approved`, your name, the date, the tier and
a `review` block on every finding, moves the draft into its bucket (or
merges its findings into the entry that already exists, renumbering
them), removes the draft and writes an `APPROVED` line to the log. It
refuses the automatic checker, a model on Tier B, and a model reviewing
its own extraction.

## 6. Check and commit

```bash
python scripts/aphasia_kb.py --check
git status
git add -A && git commit -m "Foo2024 extraction (3 approved, 1 rejected)" && git push
```

`--check` over the whole KB confirms the merged entries are still
valid. `git status` should show the new or changed entry, the removed
draft, the log and `citations.md`; never anything under `papers/`. The
annotated PDF reaches reviewers through the portal
(`publish_portal.py --deploy`), not through git.

## If something is odd

- **The model never approves anything.** Look at the worksheet's
  `tier_reasons`: most often a new entry id or `strength: strong` makes
  the draft Tier B, or the reviewer tag equals the extractor's, or the
  PDF was missing, or the three votes disagreed. All of these are by
  design.
- **Everything defers after a run.** Usually the extraction, not the
  review: a `num_ctx` truncation warning means the paper was cut off,
  and a cut-off paper yields plausible drafts whose quotes don't match.
- **`pdf_quote_match` is `null`.** The source PDF is not on this
  machine; the annotated copy alone is not enough for that check.
- **Re-extracting lost my edits.** Drafts are rewritten by
  `extract.py`; commit hand edits before re-extracting.
- **`OLLAMA_HOST` points somewhere else.** The scripts warn, but the
  warning is easy to miss in a batch. `echo $OLLAMA_HOST`; it should be
  unset or local.
- **`promote.py --approve` refuses.** Run the validator on that one file;
  it names the broken field.
