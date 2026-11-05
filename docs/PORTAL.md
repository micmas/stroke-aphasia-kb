# The review portal

A private website where collaborators review drafts beside the annotated
PDFs, screen candidate papers and send their decisions back here — without
a copy of the repository, a terminal or a local model. It is the hosted
counterpart of the two local workbenches (`review_app.py`, `screen_app.py`).

```
                  explorer (GitHub Pages, public)         review portal (Cloudflare Pages, private)
                  ─────────────────────────────           ──────────────────────────────────────
  export/*.json ─► findings, papers, coverage …   ◄──────  the same exports
  papers/*_annotated.pdf ─┬─► cc/   (Creative Commons: public path, linked from the explorer)
                          └─► pdf/  (everything else: Cloudflare Access, allow-listed emails)
  screening queue (prioritised head + full text, with abstracts) ─► screening.json (private)

  reviewer ──sign-in (one-time code to an allow-listed email)──► portal ──POST /api/reviews──► GitHub
                                                                                  │
            logs/portal/inbox/<stamp>_<kind>_<reviewer>_<id>.json  ◄──────────────┘
                                   │
            python scripts/portal_import.py --execute   (on the maintainer's machine)
                                   ▼
            screening/candidates.yaml · drafts/*.md (edits, marks, verdicts, comments) · logs/
```

Three principles. **Nothing enters the KB from the web**: the portal can
only append JSON records to `logs/portal/inbox/`; a person applies them with
`portal_import.py`, and `promote.py` remains the only way into the canonical
folders. **Reviewers are identified by Cloudflare Access**, which verifies
the email before the portal's code runs; the API checks the signed token
again and stamps every record with that email. **Licences decide what is
public**: annotated PDFs of Creative-Commons papers (`screening/licences.yaml`,
categories `cc`, `cc_manuscript`) are served openly and linked from the
explorer; every other annotated PDF is only readable after sign-in.
Source PDFs are never published; `papers/` stays local.

## 1. What a reviewer can do

| In the portal | What is sent | What the maintainer applies |
|---|---|---|
| **Drafts** → open one beside its annotated PDF: agree / disagree / unsure per finding with a concern; flag a passage (not in the paper, wrong page, does not support the claim); fix claim, direction, relationship, strength, target; select words in the PDF to add a passage to a finding; mark passages no finding covers, with a note; an overall verdict (approve / keep for review / reject) with a rationale | `verdict`, `edit`, `mark` records | verdicts → the draft's `portal_reviews` (and `promote.py` when the reviewer may approve); edits → the finding, stamped `edits`; marks → `reviewer_marks` for `refocus.py` |
| **Title/abstract** → the next 300 records of the prioritised queue (SCREENING.md §4.1): include / exclude with a reason / unsure, note; keys `i` `e` `u` | `screen` records | `screening/candidates.yaml` via the same code as `screen.py decide`, as `by: <name>` |
| **Full text** → every record awaiting assessment, with the annotated PDF when the portal holds it | `screen` records (`stage: full_text`) | same |
| **My reviews** → what you sent and whether it has been applied | — | — |

Decisions are kept in the reviewer's browser until "Send"; sending writes
the records to GitHub at once (one commit each) and the page confirms.

## 2. One-time setup (maintainer)

1. **Cloudflare account** (free) → *Workers & Pages* → *Create* → *Pages* →
   *Direct upload*; name the project `stroke-aphasia-kb-review` (or change
   `pagesProject` / `portalUrl` in `portal/portal.config.json`). Upload any
   placeholder; the real content comes from the script below.
2. **Cloudflare Access** (*Zero Trust* → *Access* → *Applications* → *Add an
   application* → *Self-hosted*): application domain
   `stroke-aphasia-kb-review.pages.dev` (and `*.stroke-aphasia-kb-review.pages.dev`
   for preview deployments), session duration as you like. Policy *Allow* with
   rule *Emails* = the reviewers' addresses (or *Emails ending in* `@uq.edu.au`
   plus named externals). Identity provider: the default *One-time PIN* needs
   nothing else; Microsoft/Google login can be added. Copy the application's
   **Audience (AUD) tag** and the **team domain** (`<team>.cloudflareaccess.com`).
3. **Public path for the CC PDFs**: add a second Access application for the
   same domain with path `cc/*` and a single *Bypass* policy (*Everyone*), so
   `…/cc/<Key>_annotated.pdf` opens without sign-in. Everything else stays
   behind the first application.
4. **GitHub token**: a fine-grained personal access token for this repository
   only, permission *Contents: Read and write*, 1-year expiry, named
   `stroke-aphasia-kb-portal`. It is the only secret.
5. **Variables** (Pages project → *Settings* → *Variables and Secrets*,
   Production): `ACCESS_TEAM_DOMAIN` = `<team>` (the part before
   `.cloudflareaccess.com`), `ACCESS_AUD` = the AUD tag, `GITHUB_REPO` =
   `micmas/stroke-aphasia-kb`, `GITHUB_BRANCH` = `main`, and the secret
   `GITHUB_TOKEN`. The same four names are placeholders in
   `portal/wrangler.toml`; either place works, the dashboard wins.
6. **Reviewers table**: `portal/reviewers.yaml` maps each email to the
   `human:<name>` used in the KB and says who may approve
   (GOVERNANCE.md §2). The Access policy decides who may *enter*; this file
   decides what their verdicts *do*.
7. **Tools on the Mac**: `cd portal && npm install` (pdf.js for the viewer,
   wrangler to deploy) and `npx wrangler login` once.

## 2b. Trying it on your own computer first

```bash
python scripts/publish_portal.py                 # build portal/dist/ (needs `npm install` in portal/ once, for pdf.js)
python scripts/portal_dev.py --by you@uq.edu.au  # serve it at http://127.0.0.1:8768/ as that reviewer
python scripts/portal_import.py                  # what you sent, as the maintainer would see it (then --execute, or delete the records)
```

`portal_dev.py` stands in for Cloudflare Access and the GitHub write: the
email you pass is the signed-in reviewer, and each record you send is
written to `logs/portal/inbox/` under the same file name the hosted
function would commit. The only parts it does not exercise are the Access
token check and the GitHub API call; `cd portal && npm test` covers the
former with a generated key pair. `npx wrangler pages dev dist` (in
`portal/`) runs the real Functions locally instead, with `DEV_REVIEWER=<email>`
in a `portal/.dev.vars` file standing in for Access — but a `GITHUB_TOKEN`
there would make real commits.

## 3. Publishing and the review cycle

```bash
python scripts/export_webapp.py --out export/stroke-aphasia-kb.json --fixtures export --indent 1
python scripts/export_webapp.py --include approved,in_review,draft --out export/stroke-aphasia-kb-drafts.json
python scripts/publish_portal.py --deploy      # assemble portal/dist/ (PDFs by licence, exports, queue) and deploy
```

`publish_portal.py` reads `papers/` on this machine, so it is run here, not
in CI: the PDFs never pass through git. Re-run it after re-annotating,
after extracting new papers, or when the queue should move on. `--pdfs-only`
refreshes only the PDF folders; `--ta-limit N` changes how much of the
title/abstract queue is offered (default 300, in the prioritised order).

When reviews have arrived (each is a commit on `main` under
`logs/portal/inbox/`):

```bash
git pull
python scripts/portal_import.py                # what each record would do, and any unknown reviewer email
python scripts/portal_import.py --execute      # apply; records move to logs/portal/applied/
python scripts/portal_import.py --execute --promote   # also run promote.py for approvers' approve / reject
python scripts/refocus.py --all --execute      # marks → findings, if any were sent
git add screening drafts logs && git commit -m "Portal reviews applied" && git push
python scripts/publish_portal.py --deploy      # so reviewers see "applied" and the new state
```

Everything applied is attributed: screening decisions carry `by: <name>`;
edits get `edits: {by, date, fields, via: portal}`; verdicts land in the
draft's `portal_reviews` with the per-finding answers; the log gets one
`PORTAL-APPLIED` line per run. An `approve` from someone not listed as an
approver is kept as an opinion, never promoted. An edit whose field changed
since the reviewer saw it is reported as stale and not applied.

## 4. Files

```
docs/PORTAL.md                 this page
portal/web/                    the portal page (index.html, app.js, portal.css); the explorer's stylesheet is reused
portal/functions/              Cloudflare Pages Functions: _middleware.js (Access token check), api/me.js, api/reviews.js
portal/functions/test/         node --test: the token check against a generated key pair
portal/portal.config.json      project name, portal URL (the explorer links public PDFs through it), explorer URL
portal/reviewers.yaml          email → human:<name>, approver yes/no
portal/wrangler.toml           Pages project settings; non-secret variables
portal/package.json            pdfjs-dist (vendored into dist/ at build) and wrangler
portal/dist/                   the built site — git-ignored (it contains PDFs)
scripts/publish_portal.py      assemble dist/ and deploy
scripts/portal_dev.py          serve dist/ locally, standing in for Access and the GitHub write
scripts/portal_import.py       apply the records in logs/portal/inbox/
logs/portal/inbox/             records sent by reviewers, waiting
logs/portal/applied/           records applied (kept: they are the audit trail of who decided what)
tests/test_portal.py           the Python halves
```

## 5. Limits and choices

* **One commit per record.** Simple and fully attributed; a reviewer who
  sends forty screening decisions makes forty small commits. If that gets
  noisy, the function can batch per send — the import does not care.
* **The portal is a snapshot.** It shows the exports and queue it was built
  with; "My reviews" is live (it lists the repository folders). Redeploy after
  applying reviews so the state catches up.
* **Preview deployments** (`--branch` other than `main`) get their own URL
  under the same Access rules when the wildcard domain is in the application.
* **Access free tier**: 50 users. The one-time-PIN login needs no account;
  a reviewer can also be let in through Microsoft or Google if that provider
  is added to the Zero Trust team.
* **Copyright**: the private site is a shared folder with a lock, used by
  named collaborators for checking claims — the same footing as the OneDrive
  folder. Do not add a Bypass policy to `pdf/`.
