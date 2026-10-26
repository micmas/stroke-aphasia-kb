# Contributing

The knowledge base grows one paper at a time. There are three ways to
help, in increasing order of effort.

## 1. Report a problem with an entry

Open an issue naming the entry file (for example
`regions/left_arcuate_fasciculus.md`) and the finding id, and say what
is wrong: a quote that is not in the paper, a claim that overstates the
paper, a missing confounder. Every finding carries its `source_passages`
and page numbers, so point at those.

## 2. Review a draft

Drafts wait in `drafts/<bucket>/`. Reviewing one means reading the
paper (fetch it through your own access; `citations.md` has the DOI,
drop it in `papers/<Key>.pdf`) and checking each finding against it.

```bash
python scripts/promote.py --list                       # what is waiting, and at which tier
python scripts/review_sheet.py --all --fix-pages       # one HTML page per draft, every quote on its page
python scripts/review_app.py --draft drafts/<bucket>/<file>.md   # the workbench: edit the draft beside the whole paper
python scripts/promote.py --approve drafts/<bucket>/<file>.md --reviewer human:<your name>
python scripts/promote.py --reject  drafts/<bucket>/<file>.md --reviewer human:<your name> --reason "..."
```

Who may approve what is in [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md):
an independent local model may clear routine (Tier A) findings after
re-reading the PDF; therapies, strong claims, new entries and reviews
(Tier B) need a person. Your name goes on what you approve.

## 3. Add a paper

Papers are chosen under the screening protocol in
[`docs/SCREENING.md`](docs/SCREENING.md), so the first step is to
register the paper there (or make sure it already is). Then:

```bash
cp ~/Downloads/<paper>.pdf papers/                      # any file name
python scripts/intake_papers.py --execute               # register, rename to <Key>.pdf, strip covers, OCR
python scripts/extract.py --pdf papers/<Key>.pdf        # local model writes drafts + annotated PDF
python scripts/aphasia_kb.py --check drafts/            # schema validation
python scripts/auto_review.py --all --llm-review --require-pdf-match
```

then review as in step 2. The full walkthrough with what to look for
at each step is [`docs/HOWTO.md`](docs/HOWTO.md); every command and
option is in [`docs/COMMANDS.md`](docs/COMMANDS.md).

## Ground rules

- Run everything from the repository root with the virtual environment
  active (`pip install -r requirements.txt`). Commands that rename or
  rewrite files are dry runs until you add `--execute`.
- Never write directly into `regions/`, `impairments/`, `therapies/`,
  `predictors/`, `reviews/` or `ingredients/`. `promote.py` is the only
  way in; it stamps the reviewer and writes the log line.
- Never commit `papers/`: PDFs are copyright. The folder is git-ignored.
- Every model step runs locally through Ollama. Do not point
  `OLLAMA_HOST` at a remote machine.
- Changing the schema means changing [`docs/schema.md`](docs/schema.md)
  and `scripts/aphasia_kb.py` together; changing who may approve what
  means changing `docs/GOVERNANCE.md` and the scripts that enforce it
  together.
- Before pushing: `python scripts/kb_status.py`, `npm test` (the
  JavaScript port's parity test) and, if you touched the screening or
  review code, `python tests/test_screening.py` and
  `python tests/test_review_guardrails.py`.

## After pushing

CALMaR pins this repository as a submodule. After your change lands on
`main`, bump the pointer there:
`git submodule update --remote stroke-aphasia-kb && git add stroke-aphasia-kb && git commit`.
The webapp re-exports with `apps/calmar/scripts/sync_kb.py --kb <this checkout>`.
