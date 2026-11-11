# The review portal

## Upload a paper for screening

On **PDFs**, use **Upload any paper**. Choose or drop a main PDF, then check its
title and DOI. Metadata is read in the browser; no external model receives the PDF.
The portal checks the complete screening register and pending uploads by DOI,
then normalized title. Ambiguous matches require selection; conflicting DOIs
require correction. An unrecognized title or missing DOI can still need a later
manual duplicate check.

A matching paper keeps its screening decisions and receives priority if still
awaiting screening. An unmatched paper enters title/abstract screening as a record
from another source, with its uploaded PDF available to reviewers immediately.
Uploading never includes a paper automatically. PDFs stay in the private upload
bucket; only bibliographic metadata and intake records enter GitHub.

The normal **Apply** operation registers the paper and preserves its priority.
PDF retrieval still happens on the maintainer's machine through `portal_import.py`;
CI deliberately skips PDF retrieval. New upload identifiers start with `U` and
remain stable; if a concurrent registration already exists, the importer retains
an alias so earlier PDF links and screening decisions still resolve.


The review portal is where collaborators help check the knowledge base.
You sign in with your email, read a draft next to the paper it came from,
and say whether you agree. You can also sort new papers in or out, and
send us a PDF we don't have. Nothing you do there changes the KB
directly: your decisions come back to the maintainer, who applies them
under your name.

If you have been invited, start with **[For reviewers](#for-reviewers)**
below. If you maintain the KB, the one-time setup is in §2 and the
routine, most of which runs itself, in §3.

![The review portal: what moves where. The maintainer's machine publishes annotated PDFs (by licence), the exports and the screening queue to a private Cloudflare Pages site; reviewers sign in with a one-time code and review, screen and upload there; every decision comes back as a record in logs/portal/inbox/ on GitHub, and uploaded PDFs wait in a private bucket, until the maintainer applies them with portal_import.py.](figures/portal-flow.svg)

*The maintainer's machine on the left, the portal in the middle, the
public explorer on the right. Annotated PDFs go out with
`publish_portal.py --sync`; decisions come back as records; only
`portal_import.py` — run by the apply workflow, or by hand — writes
anything into the KB.*

## For reviewers

**Getting in.** Open https://review.aphasia-kb.app. Someone who is not
signed in sees a welcome page with two choices. **I'd like to become a
reviewer** is a short form (name, email, affiliation, a line about your
background); it goes to the maintainer, who adds your email to the
portal's allow-list (and to the Reviewer team, `portal/reviewers.yaml`)
and writes back. **I'm already an approved reviewer** signs you in: type
your email and enter the code that arrives. No account, no password; the
sign-in lasts a week.

**What you can do**

| Page | What you do there | What happens to it |
|---|---|---|
| **Drafts** | Open a draft beside the annotated PDF (the highlights are its passages). For each finding: agree, disagree (say why) or unsure. For each passage: checked, not sure, or a problem (not in the paper, wrong page, does not support the claim, altered). Fix a field the paper contradicts. Select words in the PDF to add a passage, or to mark something the extractor missed. Give an overall verdict. | Comes back as records; the maintainer applies them to the draft. If you are an approver, your verdict runs `promote.py` under your name. |
| **Title/abstract** | Read a title and abstract, decide include / exclude (with a reason) / unsure. Keys `i` `e` `u`. The queue is the prioritised head of the register, 300 at a time. | Written into the screening register under your name. |
| **Full text** | One paper at a time, its PDF beside the decision (keys: i include · e exclude · u unsure · s skip · ← →). Including needs the PDF: if the portal has none, upload it (drop it on the PDF side) or skip the paper for now; skipped papers wait at the end of the queue. | Same. |
| **Upload a PDF** | On any card or draft whose paper the portal lacks. PDF only, up to 60 MB. | Goes to a private bucket, then to the maintainer's papers folder; never to the public site. |
| **PDFs** | The papers included at title/abstract that nobody has a PDF for yet (with links to find them, and an upload control), every annotated PDF this build holds with its licence, and the uploads waiting for the maintainer. | — |
| **My reviews** | What you sent, and whether it has been applied yet. | — |

Your decisions stay in your browser until you press **Send**; sending
writes them to the repository as one commit (one file per decision) and
the page confirms. What you leave as "not checked" stays open for
another reviewer.

The portal is a snapshot: it is rebuilt a few minutes after what
reviewers sent has been applied, which the maintainer does with one
button and which also happens on its own every six hours. Your decisions
reach the repository the moment you send them, but the queues change at
the next build; a paper you included at title/abstract shows up under
**Full text** then, not immediately.

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
records to `logs/portal/inbox/`. They are applied by `portal_import.py`
— in GitHub Actions when the maintainer presses **Apply now** (or every
six hours), or by hand — and `promote.py` stays the only way into the
canonical folders. The button starts a workflow; it does not write.

**Reviewers are identified by Cloudflare Access.** Access checks the
email before the portal's code runs; the API checks the signed token
again and stamps every record with that email.

**Licences decide what is public.** Annotated PDFs of papers whose
published version is Creative Commons (`screening/licences.yaml`: `cc`)
are served openly on the `cc/` path and linked from the explorer. A
`cc_manuscript` paper (only the accepted manuscript is openly licensed)
stays behind the sign-in, because the copy in `papers/` may be the
publisher's version, until a person checks that file and runs
`python scripts/publish_portal.py --confirm-public-copy @Key --by <name>`
(open both the source PDF and its annotated copy first): that records
the checksums of both files, and changing either one later, including
re-annotating it, makes it private again. All other annotated PDFs need the sign-in. The open path
serves only the files the current build lists in `public-pdfs.json`, and
public responses are not cached, so a licence correction takes effect at
the next deploy even if removing the object from the bucket failed
(`--sync` keeps retrying such deletions, listed as `pending_deletions` in
`portal/papers.json`, and exits with an error until they succeed).
Source PDFs are not public: `papers/` stays local, except that the PDF
of a paper awaiting full-text screening is uploaded to the private
`pdf/` path so signed-in reviewers can read it.

**The PDFs live in a bucket, not in git and not in the deployment.**
`publish_portal.py --sync`, on the maintainer's machine, mirrors the
annotated PDFs into a private R2 bucket (`cc/`, `pdf/`) and writes
`portal/papers.json`, an index of names, licences and checksums that is
committed. Two small functions serve the files from the bucket. Because
the build only needs the index, GitHub Actions rebuilds and deploys the
portal on every push, exactly as it does the explorer.

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
2. **Zero Trust → Access → Applications → Add → Self-hosted.** Domains
   `review.aphasia-kb.app` and `stroke-aphasia-kb-review.pages.dev`, plus
   `*.stroke-aphasia-kb-review.pages.dev` for preview deployments.
   Policy *Allow*, rule *Emails* = the reviewers (or *Emails ending in*
   `@uq.edu.au` plus named externals). Identity: reviewers sign in with a
   **one-time PIN** sent to their email, so they need no account. A new
   Zero Trust organisation may start with *Sign in with Cloudflare* only,
   which would make every reviewer create a Cloudflare account: add
   *One-time PIN* under *Integrations → Identity providers*, then in this
   application's *Login methods* switch off *Accept all available identity
   providers*, choose *One-time PIN* and leave *Apply instant
   authentication* on (the sign-in then asks for the email straight
   away). Note the **AUD tag** and the **team name**
   (`<team>.cloudflareaccess.com`).
3. **A second Access application** for the same domains with path `cc/*`
   and one *Bypass* policy (*Everyone*): that is what makes the
   Creative-Commons PDFs public.
4. **GitHub token.** Fine-grained, this repository only, *Contents: read
   and write* and *Actions: read and write* (the second is what lets the
   Apply button start the workflow). It is the portal's only secret.
5. **Variables.** `ACCESS_TEAM_DOMAIN` (the team name), `ACCESS_AUD`,
   `GITHUB_REPO`, `GITHUB_BRANCH`, `MAINTAINERS` (who may press Apply) in
   `portal/wrangler.toml`; the token as a secret: `npx wrangler pages
   secret put GITHUB_TOKEN --project-name stroke-aphasia-kb-review`.
6. **Reviewer team.** `portal/reviewers.yaml`: each email → `human:<name>`,
   `approver: true/false`, and `maintainer: true` for whoever should see
   the Apply button (the same email goes in `MAINTAINERS`). The Access
   policy decides who may *enter*; this file decides what their verdicts
   *do*.
7. **Tools.** `cd portal && npm install` (pdf.js, wrangler), then
   `npx wrangler login` once.
8. **Buckets.** `npx wrangler r2 bucket create stroke-aphasia-kb-pdfs`
   (the annotated PDFs and the abstracts cache; `publish_portal.py --sync`
   fills it) and, optionally, `npx wrangler r2 bucket create
   stroke-aphasia-kb-uploads` (PDFs reviewers upload; without it the upload
   control is hidden). Both bindings are already in `wrangler.toml`. Both
   buckets are private: the portal's functions read the first, and only
   `portal_import.py` on your machine reads the second.
9. **Domain** (optional). The project answers at
   `<project>.pages.dev` from the start; the public address is a custom
   domain added under *Workers & Pages → the project → Custom domains*
   (`review.aphasia-kb.app`; Cloudflare writes the DNS record when the
   zone is in the same account). The explorer's own domain,
   `aphasia-kb.app`, is GitHub Pages: a `CNAME` file in the Pages
   artifact (written by `.github/workflows/pages.yml`), the domain set
   in the repository's *Settings → Pages* with *Enforce HTTPS*, and in
   the Cloudflare zone four `A` records at the apex pointing at GitHub
   Pages (185.199.108–111.153). They were *DNS only* at first, so GitHub
   could issue its certificate, and are *Proxied* since 10 November 2026
   (with SSL/TLS mode *Full*), because a network filter was cutting
   direct connections to the new domain. With the proxy came three zone
   settings that keep updates immediate: *Browser Cache TTL: Respect
   existing headers*, a cache rule that bypasses Cloudflare's cache for
   the GitHub-hosted names, and a response-header rule that sets
   `Cache-Control: no-cache` on them, so a browser asks for a new
   version at every visit. Both addresses live in
   `portal/portal.config.json`; the export and the portal build read
   them from there.

10. **Let CI build and deploy.** In Cloudflare, *My profile → API tokens →
    Create*: *Cloudflare Pages: Edit* and *Workers R2 Storage: Edit* on
    this account. In the repository, *Settings → Secrets and variables →
    Actions*: `CLOUDFLARE_API_TOKEN` (that token),
    `CLOUDFLARE_ACCOUNT_ID`, and `PORTAL_PUSH_TOKEN`: a second
    fine-grained GitHub token (this repository, *Contents: read and
    write*) that the apply workflow pushes with, because `main` is a
    protected branch that only the maintainer's own token may bypass. A
    push made with it also starts the builds, so both sites refresh after
    an apply. From then on every push to `main` runs
    `.github/workflows/portal.yml`, which fetches the abstracts cache from
    the bucket, assembles the portal and deploys it; and
    `portal-apply.yml` applies the inbox when asked (the button) or every
    six hours. `publish_portal.py --deploy` from your machine still works
    and is the fallback.

11. **The welcome page.** Everything on the portal is behind the sign-in
    except `/welcome/`. Two settings make that so:
    - *Zero Trust → Access → Applications*: a third application for
      `review.aphasia-kb.app` with path `welcome` and one *Bypass* policy
      (*Everyone*). Only that path: never `pdf/`, `api/` or the site root.
    - *Rules → Redirect Rules* on the zone: when the host is
      `review.aphasia-kb.app`, the path is `/` and there is no
      `CF_Authorization` cookie, redirect (302) to
      `https://review.aphasia-kb.app/welcome/`. Cloudflare applies
      redirect rules before Access, so a visitor without a session sees
      the welcome page and a signed-in reviewer goes straight in.

    The page's **Sign in** button points at `/api/signin`, which is behind
    Access like the rest of `/api/`: Cloudflare asks for the email and the
    code, then the reviewer lands on the portal. Its form posts to
    `/welcome/request`, the portal's only public endpoint. A request is
    kept in the private uploads bucket under `requests/` (never in this
    repository, which is public) and shown to maintainers on the portal's
    Home, under **Reviewer requests**.

12. **Reviewer requests by email** (optional). Without it, a new request
    starts `.github/workflows/portal-request.yml`, which opens an issue
    saying one is waiting (no name, no email), and GitHub notifies you.
    To get the request itself in your inbox instead:
    - *Email → Email Routing* on the zone: **Onboard domain** (Cloudflare
      adds the mail records), then **Destination addresses**: add each
      address in `MAINTAINERS` and click the link Cloudflare sends to it.
    - `cd portal/mailer && npx wrangler deploy` once: a small Worker with
      no public address that sends through Email Routing, only to those
      verified addresses, from `review-portal@aphasia-kb.app`.
    - In `portal/wrangler.toml`, uncomment the `[[services]]` block that
      binds it as `MAILER`, commit and push.

    Email Routing writes only to your own verified addresses, so the
    portal cannot write to the person who asked: the **Write to them**
    button beside a request opens a ready-written welcome in your own
    mail program.
### Trying it on your own computer first

```bash
python scripts/publish_portal.py
python scripts/portal_dev.py --by you@uq.edu.au
python scripts/portal_import.py
```

`portal_dev.py` serves the built portal at http://127.0.0.1:8768/ as the
email you pass, standing in for Access, the GitHub write and the buckets:
PDFs come straight from `papers/`, records go to `logs/portal/inbox/`
under the same names, uploads to `portal/.uploads/`. Apply them with
`--execute` or delete them after a trial. `cd portal && npm test` covers
the Access token check, the batched write, the upload, the PDF routes and
the Apply endpoint with fakes.

## 3. The routine

Most of it runs itself. A reviewer presses **Send**; the records land in
`logs/portal/inbox/` as one commit. You press **Apply now** on the
portal's Home (it appears for the emails in `MAINTAINERS`), or wait: the
apply workflow also runs every six hours when the inbox is not empty. It
applies the records with `portal_import.py --execute --promote
--skip-pdf`, commits under `portal-apply`, pushes, and starts the explorer
and portal builds, so a few minutes later both sites show the new state
and reviewers see "applied" under **My reviews**. Nothing on your machine
is involved.

The sites are built once per apply, not once per decision. What a
reviewer sends, and each PDF they upload, is a small file committed to
`logs/portal/inbox/`; a push that only adds such files starts no build
and no test (`paths-ignore` in `pages.yml`, `portal.yml` and `test.yml`),
because nothing on either site changes until the records are applied.
The portal itself shows what has been sent and uploaded straight away;
it asks GitHub and the bucket, not the build. The "Papers ready to
extract" notice follows the same idea: it reacts to an apply or to your
own push, and looks for newly uploaded PDFs four times a day instead of
after each upload.

**Extraction** is the one step the portal cannot do: it runs the local
model on the PDFs in OneDrive. Everything up to it is online: full-text
screening and PDF uploads in the portal, citation keys in the apply
workflow (`screen.py register`). When included papers wait for
extraction, the `extract-notice` workflow opens the issue *Papers ready
to extract*, assigned to you, so GitHub emails it, with the list and one
command to paste into Terminal:

```bash
cd ~/GITHUB/stroke-aphasia-kb && git pull && python scripts/extract_ready.py --execute
```

It takes the PDFs uploaded in the portal into papers/, registers keys and
renames PDFs, extracts each paper that has its PDF (20–30 min each), syncs
the annotated PDFs and the PDFs of papers awaiting full-text screening
(served privately as `pdf/<id>_fulltext.pdf`, so the full-text screen can
show them; `publish_portal.py --sync` alone does just this part), commits only what it wrote and pushes. The drafts then
show in the portal's Drafts queue and the issue closes itself once nothing
is left (it is commented on, so emailed again, whenever the list changes).
`python scripts/extract_ready.py` alone lists what is waiting. Make sure
GitHub sends you email for issues assigned to you (Settings →
Notifications).

Otherwise, two things still happen here, because they need the papers folder:

```bash
python scripts/publish_portal.py --sync
git add portal/papers.json && git commit -m "Annotated PDFs synced" && git push
```

after extracting or re-annotating (`--dry-run` first if you like): it
uploads only the PDFs whose checksum changed, moves a PDF between `cc/`
and `pdf/` when its licence category changed, deletes what is gone, and
refreshes the abstracts cache in the bucket. And, when reviewers have
uploaded PDFs (the apply workflow leaves `pdf` records in the inbox):

```bash
git pull
python scripts/portal_import.py --execute --kind pdf
python scripts/intake_papers.py --execute
python scripts/refocus.py --all --execute
git add -A && git commit -m "Uploaded PDFs taken in" && git push
```

`refocus.py` is for the passage marks reviewers sent, which need the
local model; skip it when there were none. A dry run (`portal_import.py`
without `--execute`) lists any email not yet in the Reviewer team.

**When someone asks to become a reviewer** you are told (by email or by
GitHub, see step 12) and the request is on the portal's Home under
**Reviewer requests**. To accept: **Add in Cloudflare** copies the email
and opens the edit page of the *Reviewers* policy (the address is
`accessPolicyUrl` in `portal/portal.config.json`): paste the email into
the *Emails* box and save. Then add a block for the person in
`portal/reviewers.yaml` and push, **Write to them**, and **Remove from
list**. Removing only clears the request; it does not write to anyone.

## 4. Files

```
portal/web/                    the portal page: index.html, app.js, portal.css (the explorer's stylesheet is reused)
portal/web/welcome/            the public welcome page: sign in, or ask to become a reviewer
portal/functions/              Pages Functions: _middleware.js (Access check on api/ and pdf/), api/me.js, api/reviews.js,
                               api/upload.js, api/apply.js (the button), cc/ and pdf/ (PDFs from the bucket),
                               welcome/request.js (the public form), api/signin.js, api/requests.js (the maintainer's list)
portal/lib/requests.js         reviewer requests: checking, keeping them in the bucket, telling the maintainer
portal/mailer/                 the optional mail Worker (Email Routing), deployed by hand: npx wrangler deploy
portal/lib/github.js           the GitHub writes (one record, or a batch as one commit), shared by the functions
portal/lib/pdfs.js             serving a PDF from the bucket
portal/functions/test/         node --test: token check (generated key pair), reviews, upload, pdfs, apply, requests (fakes)
portal/papers.json             the index of the annotated PDFs in the bucket (written by --sync, committed)
portal/portal.config.json      project name, bucket name, portal URL, explorer URL
portal/reviewers.yaml          the Reviewer team: email → human:<name>, approver yes/no, maintainer yes/no
portal/wrangler.toml           Pages project settings, non-secret variables, the two R2 bindings
.github/workflows/portal.yml   build + deploy on every push; portal-apply.yml: apply the inbox (button, or every 6 h);
                               portal-request.yml: flag a waiting reviewer request as an issue
portal/package.json            pdfjs-dist (vendored into dist/ at build) and wrangler
portal/dist/, portal/.uploads/ built site and local uploads — git-ignored
scripts/publish_portal.py      --sync the PDFs to the bucket; assemble dist/; deploy
scripts/portal_dev.py          serve dist/ locally
scripts/portal_import.py       apply the records
logs/portal/inbox/, applied/   records waiting; records applied (the audit trail)
tests/test_portal.py           the Python side
```

## 5. Limits and choices

One commit per **Send**: every record is its own file in the inbox,
fully attributed, but a send of forty screening decisions is one commit
(the git data API builds one tree), so the explorer's Pages workflow
rebuilds once per send rather than forty times. The import does not
care how the files arrived.

The portal is a snapshot of the build; "My reviews" and the maintainer's
inbox count are live. The apply workflow redeploys after applying.

Access free tier: 50 users; Microsoft or Google sign-in can be added to
the Zero Trust team. Preview deployments (`--branch` other than `main`)
get their own URL under the same Access rules.

Copyright: the private site is a shared folder with a lock for named
collaborators. Do not add a Bypass policy to `pdf/`. Uploaded PDFs travel
the other way on the same footing and never reach the public path; their
licence decides that at the next build like every other paper. One upload
per paper; the uploader may replace it, nobody else can until the
maintainer has pulled it.
