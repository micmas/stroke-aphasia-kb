# Contributing

Thank you for helping. The knowledge base grows one paper at a time,
and every paper needs a second pair of eyes. There is a way to take part
for almost any amount of time and skill; the explorer's
[Get involved](https://micmas.github.io/stroke-aphasia-kb/explorer/#/involve)
page shows them as five levels. This file is the practical side.

## Without installing anything

Most contributors never need a checkout.

**Spot something wrong?** Open an issue naming the entry (for example
`regions/left_arcuate_fasciculus.md`) and the finding id, and say what is
wrong: a quote that is not in the paper, a claim that says more than
the paper does, a confounder left out. Every finding shows its passages
and page numbers, so point at those.

**Have an hour?** Ask the maintainer to add your email to the review
portal ([docs/PORTAL.md](docs/PORTAL.md)). You sign in with a one-time
code, no account. There you can:

- screen new papers in or out from their title and abstract;
- read a draft next to the annotated PDF and say, finding by finding,
  whether you agree; fix a wrong field; add a passage the extractor
  missed;
- upload a PDF we do not have.

Everything you send arrives here as a record under your name, and the
maintainer applies it. Who may *approve* a draft, rather than give an
opinion on it, is a short list in
[portal/reviewers.yaml](portal/reviewers.yaml), the Reviewer team.

## With a checkout

```bash
git clone https://github.com/micmas/stroke-aphasia-kb.git
cd stroke-aphasia-kb
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Review a draft

Drafts wait in `drafts/<bucket>/`. Reviewing one means reading the
paper and checking each finding against it.

```bash
python scripts/promote.py --list                                  # what is waiting
python scripts/review_app.py --draft drafts/<bucket>/<file>.md    # draft beside the paper, in the browser
python scripts/promote.py --approve drafts/<bucket>/<file>.md --reviewer human:<your name>
python scripts/promote.py --reject  drafts/<bucket>/<file>.md --reviewer human:<your name> --reason "..."
```

The paper itself you fetch through your own access (`citations.md` has
the DOI) and drop into `papers/<Key>.pdf`; it stays on your machine.
Some drafts can be cleared by an independent local model, others need a
person; [docs/GOVERNANCE.md](docs/GOVERNANCE.md) says which. Your name
goes on what you approve.

### Add a paper

Papers come in through the screening protocol
([docs/SCREENING.md](docs/SCREENING.md)), so first make sure the paper
is registered there. Then:

```bash
cp ~/Downloads/<paper>.pdf papers/                 # any file name
python scripts/intake_papers.py --execute          # register, rename, strip covers, OCR
python scripts/extract.py --pdf papers/<Key>.pdf   # the local model writes drafts + an annotated PDF
python scripts/auto_review.py --all --llm-review --require-pdf-match
```

and review as above. The step-by-step guide is
[docs/HOWTO.md](docs/HOWTO.md); every command and option is in
[docs/COMMANDS.md](docs/COMMANDS.md).

## House rules

- Work from the repository root with the virtual environment active.
  Commands that change files are dry runs until you add `--execute`.
- The approved folders (`regions/`, `impairments/`, …) are written only
  by `promote.py`. It stamps the reviewer and writes the log line.
- `papers/` is never committed. PDFs are copyright.
- Models run locally through Ollama. Do not point `OLLAMA_HOST` at
  another machine.
- The schema lives in two places that move together:
  [docs/schema.md](docs/schema.md) and `scripts/aphasia_kb.py`. Likewise
  the governance rules and the scripts that enforce them.
- Before pushing: `python scripts/kb_status.py`, `npm test`, and the
  tests for whatever you touched (`python tests/<test>.py`).

## After pushing

CALMaR pins this repository as a submodule. Bump the pointer there once
your change is on `main`:

```bash
git submodule update --remote stroke-aphasia-kb
git add stroke-aphasia-kb && git commit -m "KB: bump"
```
