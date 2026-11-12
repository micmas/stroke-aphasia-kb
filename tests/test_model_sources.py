#!/usr/bin/env python3
"""
test_model_sources.py — the Models page says where each model comes from: model_sources.yaml is
well formed, `ollama show` output is parsed, and the published summary carries the provenance
without losing facts recorded on the machine that ran the benchmark.

    python tests/test_model_sources.py
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import benchmark_models as BM  # noqa: E402

SHOW = """  Model
    architecture        gemma4
    parameters          30.7B
    context length      262144
    embedding length    5376
    quantization        Q4_K_M

  Capabilities
    completion
    vision

  License
    Apache License
    Version 2.0, January 2004
"""


class Sources(unittest.TestCase):
    def test_yaml_entries_are_complete(self):
        sourcing, srcs = BM.model_sources()
        self.assertIn("ollama pull", sourcing)
        self.assertTrue(srcs)
        for tag, s in srcs.items():
            for key in ("developer", "licence", "library", "upstream", "checked"):
                self.assertIn(key, s, f"{tag}: {key} missing")
            for key in ("library", "upstream", "licence_url"):
                if key in s:
                    self.assertTrue(s[key].startswith("https://"), f"{tag}: {key}")
            self.assertTrue(s["library"].startswith("https://ollama.com/library/"), tag)

    def test_published_models_are_documented(self):
        pub = ROOT / "export" / "model-benchmark.json"
        if not pub.is_file():
            self.skipTest("nothing published")
        _, srcs = BM.model_sources()
        missing = [m["model"] for m in json.loads(pub.read_text(encoding="utf-8")).get("models", []) if m["model"] not in srcs]
        self.assertEqual(missing, [], "add these models to model_sources.yaml")

    def test_parse_ollama_show(self):
        f = BM.parse_ollama_show(SHOW)
        self.assertEqual(f, {"architecture": "gemma4", "parameters": "30.7B", "context_length": "262144", "quantization": "Q4_K_M"})

    def test_attach_keeps_earlier_local_facts(self):
        data = {"models": [{"model": "gemma4:31b", "local": {"digest": "abc"}}, {"model": "made-up:1b", "source": {"x": 1}}]}
        with mock.patch.object(BM, "ollama_facts", return_value={}):
            BM.attach_sources(data, "http://localhost:11434")
        a, b = data["models"]
        self.assertEqual(a["source"]["developer"], "Google DeepMind")
        self.assertEqual(a["local"], {"digest": "abc"})          # Ollama unreachable: kept
        self.assertNotIn("source", b)                             # not curated: nothing invented
        self.assertIn("sourcing", data)
        with mock.patch.object(BM, "ollama_facts", return_value={"digest": "def", "quantization": "Q4_K_M"}):
            BM.attach_sources(data, "http://localhost:11434")
        self.assertEqual(a["local"]["digest"], "def")

    def test_ollama_absent_is_quiet(self):
        with mock.patch.object(BM.subprocess, "run", side_effect=FileNotFoundError("ollama")):
            self.assertEqual(BM.ollama_facts("gemma4:31b", "http://localhost:11434"), {})


if __name__ == "__main__":
    unittest.main()
