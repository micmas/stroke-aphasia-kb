# Production chapter sites

`stroke-kb.app` hosts the landing page and both chapter explorers. `dysphagia-kb.app`
opens the Dysphagia chapter. Existing `aphasia-kb.app` URLs and hash permalinks stay
on GitHub Pages; the review portal remains at `review.aphasia-kb.app`.

Build with `python scripts/build_stroke_staging.py --public`. The historical script
name is retained for staging compatibility. `--reuse-exports` uses existing exports
instead of regenerating them. The public build never reads OneDrive search exports
and refuses to publish any `records*.json` or screening directory. Dysphagia screening
links point to the authenticated review portal at `/dysphagia/`.

Deploy with `portal/node_modules/.bin/wrangler deploy --config deployment/public-site/wrangler.toml`.
The `stroke-kb-public` workflow rebuilds on main. It requires Workers Scripts and
custom-domain deployment permissions in the Cloudflare Actions token.

The review workflow fetches versioned original screening bundles from the private
`stroke-aphasia-kb-pdfs/private/dysphagia-screening/` R2 prefix. The D1 database retains
its historical `dysphagia-screening-staging` name deliberately: saved decisions and
append-only audit events remain intact. It is bound only to the authenticated review
portal and previews, never to the public Worker. Both interfaces display the same
per-reviewer saved decisions. Unsaved browser-local choices should be saved in the
original staging browser before switching hosts.
