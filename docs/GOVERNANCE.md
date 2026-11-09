# Governance of the aphasia knowledge base

Who decides what goes into the knowledge base, and how we know. In
short: a model reads each paper and drafts findings; a person (or, for
routine findings, a second, independent model) re-reads the paper and
agrees or not; a named person is accountable for everything that is
approved; the papers themselves never leave the project's hands; and
nothing the KB produces is clinical advice.

This file is the policy. [HOWTO.md](HOWTO.md) is the procedure and
[schema.md](schema.md) the data contract; when they disagree, this file
wins and the other two get fixed. Adopted October 2026, replacing the
earlier practice under which `auto_review.py` could promote drafts on
its own.

---

## 1. Principles

1. **Every finding traces to the page.** A finding exists only if each
   of its quoted passages can be found, word for word, in the paper. A
   paraphrase is not a passage, and a quote the checker cannot find
   makes the draft fail; it is not a matter of quality.
2. **Nothing is approved without a reader who re-opened the PDF.** The
   reader may be a person or an independent model (§3). Either way the
   review is a second reading of the paper, not a check that the draft
   is consistent with itself.
3. **A named person is accountable for everything in the canonical
   folders.** When a model approves, that is delegated review: the
   maintainer who enabled it owns those approvals and audits them (§4).
4. **Paper text and patient data stay under the project's control.**
   Extraction and lesion decoding run locally, on this machine's model;
   no paper text or patient data is ever sent to a third-party model or
   API. Source PDFs are never committed: the repository ships findings,
   quotations and DOIs. Paper text leaves this machine in exactly three
   ways, all into infrastructure the maintainer administers: the
   annotated PDFs are published to the project's Cloudflare Pages site,
   openly when the paper's licence allows it (Creative Commons) and
   otherwise only to signed-in members of the Reviewer team (§2); the
   screening queue's abstracts go to the same private site; and a PDF a
   reviewer uploads waits in the project's private bucket until the
   maintainer pulls it into `papers/` and deletes it there. Reviewers
   read the Cloudflare copies in a browser; nothing they send back
   contains more of a paper than the short quotations the KB already
   keeps. Patient data (lesion masks) never goes anywhere.
5. **The report may only say what the KB says.** Causal stays causal,
   correlational stays correlational, a review's synthesis is weighted
   separately, and every line cites an entry and a paper. A region with
   no approved findings is reported as a gap, never filled in.
6. **A research development built to support clinicians, not to replace
   their judgement.** The knowledge base and the reports drawn from it
   aim to help clinicians, in their everyday work, reason about a
   person's aphasia from their lesion: what the literature says, how
   strongly, and where it is silent. That is the goal the project works
   towards through the review and audit this policy describes; it is not
   something it claims today. At this stage, the outputs are not validated
   for clinical decision-making and none of them is clinical advice;
   every report carries that caveat, and no flag removes it.

---

## 2. Who may do what

The short version: the extractor model writes drafts and nothing else;
the automatic checks can only reject or defer; an independent model may
approve routine (Tier A) findings; a person may approve anything, and
is the only one who may approve therapies, strong claims and new
entries (Tier B). Through the portal, the Reviewer team does the same
under the same names.

| Actor | Identifier in `reviewer:` / log | May | May not |
|---|---|---|---|
| Extractor model | `created_by: agent:<model-tag>` | write to `drafts/`, `papers/*_annotated.pdf`, `logs/extraction_log.md`, `citations.md` | touch any canonical folder; review its own drafts |
| Deterministic checks (`auto_review.py`) | `auto-reviewer` | reject or defer a draft; emit a reviewer worksheet | approve anything |
| Independent reviewer model | `model:<model-tag>` | verify passages against the PDF, check interpretation, **approve Tier A drafts** (§3), defer or reject any draft | approve Tier B; edit a draft; review drafts from the same model tag that extracted them |
| Person | `human:<name>` | everything above; approve Tier B; audit model approvals; edit a draft in the review workbench (`review_app.py`: every change is stamped `edits: {by, date, fields}` and logged `REVIEW-EDITED`); mark passages for a focused re-extraction (`refocus.py`); change this policy | approve a draft without opening the annotated PDF; edit a canonical entry outside `promote.py` |
| Portal reviewer (the **Reviewer team**, `portal/reviewers.yaml`) | the email Cloudflare Access verified, mapped to `human:<name>` by `portal/reviewers.yaml` | send screening decisions, per-finding verdicts, field edits, passage marks, comments and PDFs as records (`logs/portal/inbox/`); approve or reject a draft **only if listed with `approver: true`** (then `promote.py` runs under their name when the maintainer applies the record) | write to the register, a draft or a canonical entry directly; approve without being an approver (their approve is kept as an opinion) |

**The Reviewer team.** `portal/reviewers.yaml` is the list of people who
take part through the portal, in two roles. A *reviewer* is listed with
the `human:<name>` their records are applied under; they may do every
step of screening and review, and their verdicts are kept as opinions
the maintainer reads. An *approver* is a reviewer with `approver: true`:
their `approve` or `reject` is executed by `promote.py` under their name,
which makes them the accountable person of principle 3 for that entry.
The explorer's *Get involved* page calls these levels 3 and 4. Someone
joins the team by being added to the portal's Access policy (so they can
sign in) and to this file (so their name is known); approver rights are
granted by the maintainer in the same file, and the git history of the
file is the record of who could approve when.

"Independent" means a different model tag from the extractor. Same
family at a different size counts (`gemma4:31b` reviewing `gemma4:26b`
drafts); the same tag does not. The log line records both.

---

## 3. The two review tiers

Every draft is classified **before** review by `auto_review.py` from
its frontmatter. The classification is logged and is not a judgement
call.

### Tier A — an independent model may approve

All of the following must hold:

- every `source_passage` matches the PDF text layer **exactly**
  (`--require-pdf-match`; near-matches are Tier B);
- schema valid with no warnings;
- `provenance.confidence` is `high` or `medium`, and `provenance.flags`
  is empty;
- the draft **appends findings to an existing canonical entry** (a new
  entry id is Tier B);
- `strength` is `weak` or `moderate`;
- `evidence_quality` is a primary quantitative class (not
  `narrative-review`, not `case-study`);
- the bucket is `regions`, `impairments` or `predictors`.

### Tier B — a person must approve

Anything not Tier A, and always:

- any `therapies/` or `ingredients/` entry — these become
  recommendations downstream;
- `strength: strong` or `definitive`;
- any new entry id, region consolidation, or alias change;
- `reviews/` entries (narrative synthesis);
- any draft the model reviewer did not fully agree with, on any field;
- any draft where the model reviewer and the deterministic checks
  disagree;
- single-case extractions, and anything with `provenance.flags`.

### What the reviewer model must actually do

The model reviewer gets the draft, the full text layer of the paper,
and the schema. For every finding it must report, per field:

| Check | Question answered |
|---|---|
| Passage location | Is each passage present verbatim? On which page? |
| Passage relevance | Does the passage support the field it is tagged for (claim / statistics / sample / limitation …), or only something nearby? |
| Direction and relationship | Does the paper itself make a *causal* claim, or has the draft upgraded a correlation? |
| Strength | Is `strength` at or below what the authors claim for their own result? |
| Numbers | Do n, effect size, thresholds and p-values match the text and tables exactly? |
| Limitations | Are the authors' stated limitations captured, including ones that weaken the finding? |
| Omission | Is there a result in the paper that contradicts or qualifies the finding and was left out? |

Output is schema-constrained (Ollama `format`): per-field
`agree | disagree | cannot_verify` with a one-line reason, and a verdict
`approve | defer | reject`. The reviewer never edits the draft; a
disagreement defers it to a person with the reasons attached. The
sidecar in `logs/auto_review/` keeps the full output.

`approve` is honoured only for Tier A. For Tier B it is recorded as
`agree_defer` and the draft goes to a person with the model's notes,
which is the current guardrail behaviour (`--allow-local-override`
stays off).

---

## 4. Accountability for model approvals

- **Log line.** `MODEL-APPROVED | @Cite | entry | reviewer: model:<tag> |
  extractor: agent:<tag> | tier: A`. Never `APPROVED` and never a
  person's name.
- **Entry stamp.** `reviewer: model:<tag>`, `reviewed_on`, and
  `review_tier: A` (schema v2.5 adds `review_tier` and `audited_by` as
  optional fields; older entries load unchanged).
- **Audit.** After every 20 model approvals, or monthly, whichever
  comes first, a person re-reviews a random 20 % (minimum 3) against
  the annotated PDFs and logs `AUDIT | pass|fail | entries…`. One
  substantive failure (a wrong number, an upgraded relationship, a
  passage that does not support its field) pauses model approval; all
  `MODEL-APPROVED` entries since the last clean audit return to
  `in_review` until a person has read them.
- **Downstream.** `aphasia_kb_rag.py` marks model-approved and
  pre-policy findings in the report and accepts `--human-approved-only`;
  the same switch for code is `KnowledgeBase(..., review_kinds=("human",))`.
  The notebook's clinical-interpretation cell should load the KB with it
  (follow-up: wire and test in Neurodesk).
- **Revocation.** A person can reject any approved entry at any time
  with `promote.py --reject --reviewer human:<name> --reason`; the log
  keeps the history, the file moves back to `drafts/`.

---

## 5. Legacy entries (approved before this policy)

As of 2026-10-16, 33 of the 59 canonical entries with a reviewer field
were approved by `auto-reviewer` or a model without a PDF-verified
second reading, and several more carry `AUTO-APPROVED` log lines under
a person's name. They remain loadable but are tagged
`review_tier: legacy` and are excluded by `--human-approved-only`
until re-reviewed through §3. Order of re-review: `therapies/` first
(they drive recommendations), then entries with `strength: strong`,
then the rest.

The re-review runs through the ordinary draft review: `rereview.py`
moves a legacy entry back into `drafts/`, one draft per paper, with the
old approval kept as `previous_review`, and logs `REREVIEW`. Reviewers
then read it beside the PDF (portal or `review_app.py`) and an approver
promotes it; the first approval re-creates the canonical entry and the
others merge into it. While it is out for re-review the entry is absent
from the approved export.

---

## 6. Sources and rights

- Papers are obtained through the maintainer's institutional access,
  open licences, or a Reviewer-team member's upload through the portal;
  `papers/` is git-ignored. A paper is redistributed only as its licence
  allows: Creative-Commons papers openly on the portal's `cc/` path, all
  others solely to named collaborators behind the portal's sign-in — the
  footing of a shared folder with a lock, for checking claims.
- `source_passages` are short attributed quotations for verification.
  They are not a substitute for the paper and the KB links the DOI.
- Each paper's licence is recorded from metadata (`screen.py licences` →
  `screening/licences.yaml`: Crossref, Unpaywall, the PDF's own licence
  statement) and shown in the explorer. Under a Creative Commons
  licence the passages are reused under that licence's terms (attribution
  is the citation and DOI); for `rights_reserved` and `free_to_read`
  papers they stay short quotations for verification, nothing more.
- Extraction of copyrighted PDFs runs on the local model only. The
  cloud-API path is retired; `OLLAMA_HOST` pointing off-machine is a
  configuration error, and the scripts warn.
- Lesion masks used with `aphasia_kb_rag.py` are patient-derived data
  and are processed locally only; nothing about a lesion is written to
  the KB or the log.
- The KB is MIT-licensed as part of CALMaR. Model licences are noted
  in `MODELS.md` (OpenMDW for Nemotron, Apache 2.0 for Granite, Gemma
  terms for Gemma).

---

## 7. Changing this policy

Open a pull request that edits this file and, in the same PR, the code
that enforces it (`auto_review.py` tier classification, `promote.py`
stamps, `aphasia_kb_rag.py` filters). A policy the scripts do not
enforce is not a policy. Record the change and date at the top.
