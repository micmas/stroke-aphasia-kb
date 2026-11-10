#!/usr/bin/env python3
"""
test_extract_citation.py — a model that shortens the citation key it was given (gemma4:26b wrote
`@Alyahya2018` for `@Alyahya2018NounVerb`) has its drafts filed and cited under the given key, so
they join citations.md and benchmark runs find them; a different paper's key is never rewritten.

    python tests/test_extract_citation.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import extract as E  # noqa: E402
from aphasia_kb import parse_markdown  # noqa: E402



class Keys(unittest.TestCase):
    def test_same_paper_key(self):
        yes = [("@Alyahya2018", "@Alyahya2018NounVerb"), ("@alyahya2018nounverb", "@Alyahya2018NounVerb"), ("Robson2019", "@Robson2019a")]
        no = [("@Robson2019", "@Robson2019"), ("@Smith2018", "@Alyahya2018NounVerb"), ("@Alyahya2019", "@Alyahya2018NounVerb"),
              ("@Alyahya2018Noun", "@Alyahya2018NounVerb"), ("", "@Alyahya2018NounVerb")]
        for a, b in yes:
            self.assertTrue(E._same_paper_key(a, b), (a, b))
        for a, b in no:
            self.assertFalse(E._same_paper_key(a, b), (a, b))

    def test_save_drafts_uses_the_given_key(self):
        content = ("---\nid: left_angular_gyrus\nname: Left angular gyrus\nfindings:\n"
                   "- id: f1\n  citation: '@Alyahya2018'\n  target: semantics\n"
                   "- id: f2\n  citation: '@Smith2020'\n  target: anomia\n---\n")
        with tempfile.TemporaryDirectory() as tmp:
            saved = E.save_drafts([{"bucket": "regions", "filename": "left_angular_gyrus__Alyahya2018.md", "content": content}],
                                  Path(tmp), citation="@Alyahya2018NounVerb")
            self.assertEqual([p.name for p in saved], ["left_angular_gyrus__Alyahya2018NounVerb.md"])
            fm, _ = parse_markdown(saved[0])
            self.assertEqual([f["citation"] for f in fm["findings"]], ["@Alyahya2018NounVerb", "@Smith2020"])


if __name__ == "__main__":
    unittest.main()
