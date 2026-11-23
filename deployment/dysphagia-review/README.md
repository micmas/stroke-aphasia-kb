# Dedicated Dysphagia review

`review.dysphagia-kb.app` is a separate Worker, Access application and private R2
bucket (`dysphagia-kb-private`). It does not use the Aphasia review register, bucket
or inbox. The review page and every asset require a valid Dysphagia Access JWT.
With no Access audience configured, the Worker refuses all requests with 503.

Build with `python scripts/build_dysphagia_review.py`; deploy with
`portal/node_modules/.bin/wrangler deploy --config deployment/dysphagia-review/wrangler.toml`.
The `dysphagia-review` workflow rebuilds after relevant changes on main.

Screening bundles live under `screening/` in this chapter's private R2 bucket.
Future PDFs/uploads belong in this bucket too. The existing Dysphagia-only D1
database retains the historical name `dysphagia-screening-staging` to preserve
saved decisions and audit events. The preview and production review see the same
per-reviewer saved decisions. Save unsent browser-local choices on the original
preview before switching hosts.

Original exports remain unchanged in OneDrive. No extracted findings or included
papers are created by deploying this review workspace.
