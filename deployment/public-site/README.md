# Production chapter sites

`stroke-kb.app` hosts the landing page and both chapter explorers. `dysphagia-kb.app`
opens Dysphagia. Existing `aphasia-kb.app` URLs and hash permalinks stay on GitHub
Pages. Its review portal at `review.aphasia-kb.app` remains exclusively Aphasia.
Dysphagia has its own review site at `review.dysphagia-kb.app`.

Build with `python scripts/build_stroke_staging.py --public`. The historical script
name is retained for staging compatibility. `--reuse-exports` uses existing exports
instead of regenerating them. The public build never reads OneDrive search exports
and refuses to publish any `records*.json` or screening directory.

Deploy with `portal/node_modules/.bin/wrangler deploy --config deployment/public-site/wrangler.toml`.
The `stroke-kb-public` workflow rebuilds from main and requires Workers deployment
permissions in the Cloudflare Actions token.

See `../dysphagia-review/README.md` for the isolated Dysphagia review storage.
