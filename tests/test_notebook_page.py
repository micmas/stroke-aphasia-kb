#!/usr/bin/env python3
"""
test_notebook_page.py — build_notebook_page.py turns a notebook into a readable page: markdown
rendered with a contents list, code folded, long output folded, the notebook's own checkpoints
shown as pauses and real errors flagged, widgets drawn from saved state or replaced by a note,
launch links in the form Neurodesk's tutorials use, and a check on which data the run names.

    python tests/test_notebook_page.py
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

VIEW = "application/vnd.jupyter.widget-view+json"


def code(source, *outputs):
    return {"cell_type": "code", "metadata": {}, "execution_count": 1, "source": source, "outputs": list(outputs)}


NB = {"nbformat": 4, "nbformat_minor": 5, "metadata": {}, "cells": [
    {"cell_type": "markdown", "metadata": {}, "source": "# Title\n\n## Setup\nSome *text* and a table:\n\n| a | b |\n|---|---|\n| 1 | 2 |\n"},
    code("# Configuration for the run\nCONFIG = {'dataset': 'ds004884'}", {"output_type": "stream", "name": "stdout", "text": "\x1b[32mok\x1b[0m sub-M2051\n"}),
    code("print_many()", {"output_type": "stream", "name": "stdout", "text": "\n".join(f"line {i}" for i in range(30))}),
    {"cell_type": "markdown", "metadata": {}, "source": "## Setup\nA second heading with the same name."},
    code("show()", {"output_type": "display_data", "metadata": {}, "data": {"text/html": "<table><tr><td>Brain: 1,396 ml</td></tr></table>", "text/plain": "<x>"}},
         {"output_type": "display_data", "metadata": {}, "data": {VIEW: {"model_id": "abc", "version_major": 2, "version_minor": 0}, "text/plain": "VBox()"}}),
    code("checkpoint()", {"output_type": "error", "ename": "StopExecution", "evalue": "Choose a participant and click Run.", "traceback": []}),
]}


class Page(unittest.TestCase):
    def build(self, nb):
        import build_notebook_page as B
        return B.build(nb, "T", "repo · nb.ipynb", "body{}")

    def test_page(self):
        page, info = self.build(NB)
        self.assertIn('<h2 id="setup">Setup</h2>', page); self.assertIn('<h2 id="setup-2">Setup</h2>', page)      # anchors are unique
        self.assertIn('<a class="toc-2" href="#setup-2" data-ch="setup-2">Setup</a>', page)
        self.assertIn('<p class="eyebrow">Title</p>', page); self.assertNotIn('<h1 id="title">', page)   # the notebook's own title tops the page once
        self.assertIn('class="nb-toc"', page); self.assertIn("toc.classList.add('js')", page)
        self.assertIn("<table>", page)
        self.assertIn('<details class="code"><summary>Show code: Configuration for the run</summary>', page)
        self.assertNotIn("\x1b[", page); self.assertIn("ok sub-M2051", page)                               # terminal colour codes removed
        self.assertIn("Show log (30 lines)", page)
        self.assertIn("Brain: 1,396 ml", page)
        self.assertIn("Interactive panel.", page); self.assertNotIn("embed-amd.js", page)                 # no saved state: a note, no widget scripts
        self.assertIn("The notebook pauses here.", page); self.assertEqual(info["errors"], 0); self.assertEqual(info["pauses"], 1)
        self.assertEqual(info["datasets"], ["ds004884"]); self.assertEqual(info["subjects"], ["sub-M2051"]); self.assertEqual(info["unknown"], [])
        self.assertIn("https://play-america.neurodesk.org/hub/user-redirect/git-pull?repo=https%3A//github.com/micmas/calmar"
                      "&amp;urlpath=lab/tree/calmar/calmar-guided.ipynb&amp;branch=main", page)
        self.assertIn('href="https://aphasia-kb.app/"', page); self.assertNotIn('href="../', page)        # own subdomain: no relative links to the explorer

    def test_long_code_labels_are_cut_at_a_word(self):
        import copy
        nb = copy.deepcopy(NB)
        nb["cells"][1]["source"] = "# " + "word " * 30 + "\nx = 1"
        page, _ = self.build(nb)
        self.assertRegex(page, r"<summary>Show code: (word ){10,}word…</summary>")

    def test_a_notebook_saved_without_output_says_so(self):
        import copy
        nb = copy.deepcopy(NB)
        for c in nb["cells"]:
            if c["cell_type"] == "code":
                c["outputs"] = []
        page, info = self.build(nb)
        self.assertEqual(info["outputs"], 0)
        self.assertIn("saved without its results", page); self.assertNotIn("This is a saved run", page)
        self.assertIn("Show code: Configuration for the run", page)                                       # the steps and the code are still there
        page, info = self.build(NB)
        self.assertGreater(info["outputs"], 0); self.assertIn("This is a saved run", page)

    def test_saved_widgets_real_errors_and_unknown_data(self):
        import copy
        nb = copy.deepcopy(NB)
        nb["metadata"]["widgets"] = {"application/vnd.jupyter.widget-state+json": {"version_major": 2, "version_minor": 0, "state": {"abc": {"model_name": "VBoxModel"}}}}
        nb["cells"].append(code("boom()", {"output_type": "error", "ename": "ValueError", "evalue": "bad ds009999", "traceback": ["Traceback…"]}))
        page, info = self.build(nb)
        self.assertIn('<script type="application/vnd.jupyter.widget-state+json">', page); self.assertIn("embed-amd.js", page)
        self.assertIn('"model_id": "abc"', page); self.assertEqual(info["widgets"], 1); self.assertNotIn("Interactive panel.", page)
        self.assertIn("This cell stopped with an error: ValueError", page); self.assertEqual(info["errors"], 1)
        self.assertEqual(info["unknown"], ["ds009999"])                                                   # a dataset nobody said is open


if __name__ == "__main__":
    unittest.main(verbosity=1)
