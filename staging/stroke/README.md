# Stroke KB staging hub

Shared landing page and chapter explorers, deployed only to the `stroke-kb-staging`
preview branch of the existing private review Pages project. Source lives on
`feat/dysphagia-screening-staging` (draft PR #15). Production domains stay unchanged.

```sh
python scripts/build_stroke_staging.py --exports /path/to/search-exports/dysphagia/2026-11-23
cd staging/stroke
wrangler pages deploy dist --project-name stroke-aphasia-kb-review --branch stroke-kb-staging
```

- `/`: shared landing page.
- `/aphasia/`: existing explorer and regenerated Aphasia exports, with draft labels.
- `/dysphagia/`: matching chapter sections with no evidence export or Aphasia data.
- `/dysphagia/search/`: query builder and pilot search log, including corrected Cochrane syntax.
- `/dysphagia/screening/`: existing screening queue with durable decisions in the same
  isolated staging D1 database as the earlier Dysphagia preview.

The shared chapter selector and staging banner are added at build time. Chapter
pages share one explorer template and styles. All paths require existing Cloudflare
Access authentication. The original Dysphagia screening alias stays deployed.

Aphasia's active review portal is not redeployed or copied: its link in the staging
Review hub is explicitly labelled production. Dysphagia draft/full-text/PDF sections
are empty states; they do not pretend that extraction has run. Source exports remain
outside Git. Screening decisions are not automatically included in KB evidence.
