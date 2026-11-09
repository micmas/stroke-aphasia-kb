# The review portal

The review portal is where collaborators help check the knowledge base.
You sign in with your email, read a draft next to the paper it came from,
and say whether you agree. You can also sort new papers in or out, and
send us a PDF we don't have. Nothing you do there changes the KB
directly: your decisions come back to the maintainer, who applies them
under your name.

If you have been invited, start with **[For reviewers](#for-reviewers)**
below. If you maintain the KB, the one-time setup is in §2 and the
weekly routine in §3.

![The review portal: what moves where. The maintainer's machine publishes annotated PDFs (by licence), the exports and the screening queue to a private Cloudflare Pages site; reviewers sign in with a one-time code and review, screen and upload there; every decision comes back as a record in logs/portal/inbox/ on GitHub, and uploaded PDFs wait in a private bucket, until the maintainer applies them with portal_import.py.](figures/portal-flow.svg)

*The maintainer's machine on the left, the portal in the middle, the
public explorer on the right. Content goes out with `publish_portal.py`;
decisions come back as records; only `portal_import.py`, on the
maintainer's machine, writes anything into the KB.*

## For reviewers

**Getting in.** The maintainer adds your email to the portal's allow-list
(and to the Reviewer team, `portal/reviewers.yaml`). Open
https://stroke-aphasia-kb-review.pages.dev, type your email, and enter
the code that arrives. No account, no password; the sign-in lasts a week.

**What you can do**

| Page | What you do there | What happens to it |
|---|---|---|
| **Drafts** | Open a draft beside the annotated PDF (the highlights are its passages). For each finding: agree, disagree (say why) or unsure. For each passage: checked, not sure, or a problem (not in the paper, wrong page, does not support the claim, altered). Fix a field the paper contradicts. Select words in the PDF to add a passage, or to mark something the extractor missed. Give an overall verdict. | Comes back as records; the maintainer applies them to the draft. If you are an approver, your verdict runs `promote.py` under your name. |
| **Title/abstract** | Read a title and abstract, decide include / exclude (with a reason) / unsure. Keys `i` `e` `u`. The queue is the prioritised head of the register, 300 at a time. | Written into the screening register under your name. |
| **Full text** | Read the paper itself and decide. The paper's PDF must exist first; if nobody has it, upload it. | Same. |
| **Upload a PDF** | On any card or draft whose paper the portal lacks. PDF only, up to 60 MB. | Goes to a private bucket, then to the maintainer's papers folder; never to the public site. |
| **PDFs** | Every annotated PDF this build holds, with its licence, and the uploads waiting for the maintainer. | — |
| **My reviews** | What you sent, and whether it has been applied yet. | — |

Your decisions stay in your browser until you press **Send**; sending
writes them to the repository (one commit each, a second or two per
record) and the page confirms. What you leave as "not checked" stays
open for another reviewer.

**Who approves.** Everyone on the Reviewer team can review; those marked
`approver: true` can approve, and are the accountable person for what
they approve ([GOVERNANCE.md](GOVERNANCE.md) §2). An approve from anyone
else is kept as an opinion the maintainer reads.

**The papers.** Creative-Commons papers are served openly and linked from
the explorer. Every other annotated PDF is behind the sign-in, for the
Reviewer team only, like a shared folder with a lock. Please don't pass
them on.

## 1. How it is built

Three rules shape the design.

**Nothing enters the KB from the web.** The portal can only append JSON
records to `logs/portal/inbox/`. A person applies them with
`portal_import.py`, and `promote.py` stays the only way into the
canonical folders.

**Reviewers are identified by Cloudflare Access.** Access checks the
email before the portal's code runs; the API checks the signed token
again and stamps every record with that email.

**Licences decide what is public.** Annotated PDFs of Creative-Commons
papers (`screening/licences.yaml`: `cc`, `cc_manuscript`) are served
openly on the `cc/` path and linked from the explorer; all other annotated
PDFs need the sign-in. Source PDFs are never published; `papers/` stays
local.

Record kinds, and what the import does with them:

| Record | From | Applied as |
|---|---|---|
| `screen` | a screening decision | `screening/candidates.yaml`, `by: <name>` |
| `verdict` | per-finding answers + overall verdict | the draft's `portal_reviews`; `promote.py` when the reviewer is an approver and `--promote` is given |
| `edit` | a changed field, added passages | the finding, stamped `edits: {by, date, fields, via: portal}`; skipped as stale if the field changed since |
| `mark` | a passage no finding covers | the draft's `reviewer_marks`, for `refocus.py` |
| `comment` | free text | `portal_comments` |
| `pdf` | an uploaded paper | pulled from the bucket into `papers/<Key>.pdf` (or `<Cid>_<name>.pdf`, linked to the candidate), checksum verified, then deleted from the bucket |

## 2. One-time setup (maintainer)

1. **Cloudflare account** (free). *Workers & Pages → Create → Pages →
   Direct upload*, project `stroke-aphasia-kb-review` (or change
   `pagesProject` / `portalUrl` in `portal/portal.config.json`).
2. **Zero Trust → Access → Applications → Add → Self-hosted.** Domain
   `stroke-aphasia-kb-review.pages.dev`, plus
   `*.stroke-aphasia-kb-review.pages.dev` for preview deployments.
   Policy *Allow*, rule *Emails* = the reviewers (or *Emails ending in*
   `@uq.edu.au` plus named externals). Identity: the default one-time PIN
   needs nothing else. Note the **AUD tag** and the **team name**
   (`<team>.cloudflareaccess.com`).
3. **A second Access application** for the same domain with path `cc/*`
   and one *Bypass* policy (*Everyone*): that is what makes the
   Creative-Commons PDFs public.
4. **GitHub token.** Fine-grained, this repository only, *Contents: read
   and write*. It is the only secret.
5. **Variables.** `ACCESS_TEAM_DOMAIN` (the team name), `ACCESS_AUD`,
   `GITHUB_REPO`, `GITHUB_BRANCH` in `portal/wrangler.toml`; the token as
   a secret: `npx wrangler pages secret put GITHUB_TOKEN --project-name
   stroke-aphasia-kb-review`.
6. **Reviewer team.** `portal/reviewers.yaml`: each email → `human:<name>`
   and `approver: true/false`. The Access policy decides who may *enter*;
   this file decides what their verdicts *do*.
7. **Tools.** `cd portal && npm install` (pdf.js, wrangler), then
   `npx wrangler login` once.
8. **Uploads bucket** (optional): `npx wrangler r2 bucket create
   stroke-aphasia-kb-uploads`, then redeploy. The binding is already in
   `wrangler.toml`. Without it the upload control is hidden. The bucket is
   private; the only reader is `portal_import.py` on your machine.

### Trying it on your own computer first

```bash
python scripts/publish_portal.py
python scripts/portal_dev.py --by you@uq.edu.au
python scripts/portal_import.py
```

`portal_dev.py` serves the built portal at http://127.0.0.1:8768/ as the
email you pass, standing in for Access, the GitHub write and the bucket:
records go to `logs/portal/inbox/` under the same names, uploads to
`portal/.uploads/`. Apply them with `--execute` or delete them after a
trial. `cd portal && npm test` covers the Access token check and the
upload function with fakes.

## 3. The weekly routine

Publish, after extracting or re-annotating, or when the queue should move
on:

```bash
python scripts/export_webapp.py --out export/stroke-aphasia-kb.json --fixtures export --indent 1
python scripts/export_webapp.py --include approved,in_review,draft --out export/stroke-aphasia-kb-drafts.json
python scripts/publish_portal.py --deploy
```

`publish_portal.py` reads `papers/` here, so it runs on this machine,
never in CI. `--pdfs-only` refreshes just the PDF folders; `--ta-limit N`
changes how much of the title/abstract queue is offered.

Apply, when records have arrived (each is a commit under
`logs/portal/inbox/`):

```bash
git pull
python scripts/portal_import.py
python scripts/portal_import.py --execute --promote
python scripts/refocus.py --all --execute
python scripts/intake_papers.py --execute
git add screening drafts logs && git commit -m "Portal reviews applied" && git push
python scripts/publish_portal.py --deploy
```

The first line is a dry run and lists any email not yet in the Reviewer
team. `--promote` runs `promote.py` for approvers' approve / reject.
`refocus.py` is for marks, `intake_papers.py` for uploaded PDFs; skip them
when there were none. Redeploy last, so reviewers see "applied" and the
new state. The log gets one `PORTAL-APPLIED` line per run.

## 4. Files

```
portal/web/                    the portal page: index.html, app.js, portal.css (the explorer's stylesheet is reused)
portal/functions/              Pages Functions: _middleware.js (Access check), api/me.js, api/reviews.js, api/upload.js
portal/lib/github.js           the one GitHub write, shared by the functions
portal/functions/test/         node --test: token check (generated key pair), upload (fake bucket)
portal/portal.config.json      project name, portal URL, explorer URL
portal/reviewers.yaml          the Reviewer team: email → human:<name>, approver yes/no
portal/wrangler.toml           Pages project settings, non-secret variables, the R2 binding
portal/package.json            pdfjs-dist (vendored into dist/ at build) and wrangler
portal/dist/, portal/.uploads/ built site and local uploads — git-ignored (they hold PDFs)
scripts/publish_portal.py      assemble dist/ and deploy
scripts/portal_dev.py          serve dist/ locally
scripts/portal_import.py       apply the records
logs/portal/inbox/, applied/   records waiting; records applied (the audit trail)
tests/test_portal.py           the Python side
```

## 5. Limits and choices

One commit per record: simple and fully attributed; forty screening
decisions are forty small commits. If that gets noisy the function can
batch per send; the import does not care.

The portal is a snapshot of the build; "My reviews" is live. Redeploy
after applying reviews.

Access free tier: 50 users; Microsoft or Google sign-in can be added to
the Zero Trust team. Preview deployments (`--branch` other than `main`)
get their own URL under the same Access rules.

Copyright: the private site is a shared folder with a lock for named
collaborators. Do not add a Bypass policy to `pdf/`. Uploaded PDFs travel
the other way on the same footing and never reach the public path; their
licence decides that at the next build like every other paper. One upload
per paper; the uploader may replace it, nobody else can until the
maintainer has pulled it.
