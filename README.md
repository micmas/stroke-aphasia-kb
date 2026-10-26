# Stroke aphasia knowledge base

A curated, source-traceable literature base linking stroke lesion
locations to aphasia impairments, therapy responses and recovery
predictors. Every finding is one claim from one paper and carries the
verbatim passages that support it.

**This repository is being assembled.** The KB content — entries,
extraction and review scripts, governance documents and the extraction
log — still lives in [`micmas/calmar`](https://github.com/micmas/calmar)
under `aphasia-kb/` while a batch of entries is being written. It moves
here with its full git history by running `tools/migrate-from-calmar.sh`,
which also replaces that folder in CALMaR with a submodule at
`stroke-aphasia-kb/`. The KB's own README arrives with it and replaces
this file.

What is already here: the explorer site, the committed export the
JavaScript consumers read, and the JavaScript port of the evidence logic
with its parity test — see [`EXPLORER.md`](EXPLORER.md).

```bash
npm test                  # the JavaScript port against export/kb-parity.json
npm run explorer          # serve the repository root, then open /explorer/
```

Licence: MIT. Source PDFs are never redistributed.
