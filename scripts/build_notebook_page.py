#!/usr/bin/env python3
"""
build_notebook_page.py — turn an executed CALMaR notebook into a page people can read, with
buttons that open the notebook in a Neurodesk Play session. The page is live at
https://calmar.aphasia-kb.app.

    python scripts/build_notebook_page.py --calmar ../calmar --out site/calmar
        # reads ../calmar/lesion-interpretation-pipeline.ipynb (the saved run) and writes
        # site/calmar/index.html, one self-contained file

    python scripts/build_notebook_page.py --open
        # the same from ../calmar into site/calmar, then opens the page in the browser (local test)

Who publishes it: the calmar repository, not this one. Its workflow
(.github/workflows/notebook-page.yml in github.com/micmas/calmar) runs whenever a notebook is
pushed there: it checks out this repository for this script and the explorer's styles, builds
the page and publishes it with GitHub Pages under calmar.aphasia-kb.app. A change to this
script or to the styles reaches the page at the next notebook push, or at once with
"Run workflow" on that workflow.

What the page shows, cell by cell:
  markdown        rendered as written (headings feed the contents list on the left)
  code            folded behind "Show code": the page is for reading, the code is one click away
  tables, HTML    shown as the notebook displayed them
  printed output  short output shown, long output folded behind "Show log"
  widgets         when the notebook was saved with its widget state (JupyterLab → Settings →
                  "Save Widget State Automatically"), each panel is drawn again in the browser
                  with the values it had: tabs, accordions and sliders that work in the browser
                  keep working; buttons and menus that need Python do nothing here, because a
                  page has no kernel. Without saved state a panel becomes a short note with the
                  launch button — the live version is one click away in Neurodesk Play.
  checkpoints     the notebook's own "stop until you click a button" cells (StopExecution) are
                  shown as a pause, not as an error; a real error is shown folded and flagged

The launch buttons use the same link Neurodesk's own tutorials use: it copies the calmar
repository into the visitor's Play session and opens the notebook there.

Only open data may be published: the page prints the participant ids and dataset names it
found so you can see at a glance that the run used the public examples (OpenNeuro ds004884,
ISLES 2022) and nothing else. `--allow-dataset` names further datasets that are fine.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import html
import json
import re
import sys
import webbrowser
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
EXPLORER_CSS = ROOT / "explorer" / "styles.css"
PAGE_CSS = ROOT / "explorer" / "notebook.css"
PIPELINE = "lesion-interpretation-pipeline.ipynb"
GUIDED = "calmar-guided.ipynb"
REPO = "https://github.com/micmas/calmar"
KB_SITE = "https://aphasia-kb.app/"            # the knowledge base explorer: the page links back to it
PAGE_SITE = "https://calmar.aphasia-kb.app/"   # where this page is published
PLAY = (("Americas", "https://play-america.neurodesk.org"), ("Europe", "https://play-europe.neurodesk.org"))
OPEN_DATASETS = ("ds004884", "ISLES", "ISLES 2022")
WIDGET_VIEW = "application/vnd.jupyter.widget-view+json"
WIDGET_STATE = "application/vnd.jupyter.widget-state+json"
# What draws saved widgets in a page without a kernel (the same two scripts nbconvert uses), pinned.
WIDGET_SCRIPTS = ["https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.js",
                  "https://cdn.jsdelivr.net/npm/@jupyter-widgets/html-manager@1.0.14/dist/embed-amd.js"]
ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")
LONG_LOG = 8                               # printed output longer than this many lines is folded


def launch_url(server: str, notebook: str, repo: str = REPO, branch: str = "main") -> str:
    """The nbgitpuller link Neurodesk's tutorials use: copy the repository into the visitor's
    session, then open the notebook in JupyterLab."""
    name = repo.rstrip("/").split("/")[-1]
    return (f"{server}/hub/user-redirect/git-pull?repo={quote(repo, safe='/')}"
            f"&urlpath={quote(f'lab/tree/{name}/{notebook}', safe='/')}&branch={quote(branch)}")


# ------------------------------------------------------------------ pieces
def md_renderer():
    try:
        from markdown_it import MarkdownIt
    except ImportError:
        raise SystemExit("build_notebook_page needs markdown-it-py:  pip install markdown-it-py") from None
    return MarkdownIt("commonmark", {"html": True, "linkify": False}).enable(["table", "strikethrough"])


def slugify(text: str, seen: dict[str, int]) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", html.unescape(re.sub(r"<[^>]+>", "", text)).lower()).strip("-") or "section"
    seen[base] = seen.get(base, 0) + 1
    return base if seen[base] == 1 else f"{base}-{seen[base]}"


def render_markdown(md, source: str, seen: dict[str, int], toc: list[tuple[int, str, str]]) -> str:
    out = md.render(source)

    def heading(m: re.Match) -> str:
        level, inner = int(m.group(1)), m.group(2)
        anchor = slugify(inner, seen)
        toc.append((level, anchor, html.unescape(re.sub(r"<[^>]+>", "", inner)).strip()))
        return f'<h{level} id="{anchor}">{inner}</h{level}>'

    out = re.sub(r"<h([1-4])>(.*?)</h\1>", heading, out, flags=re.S)
    return out.replace("<a href=\"http", "<a target=\"_blank\" rel=\"noopener\" href=\"http")


def text_of(x) -> str:
    return "".join(x) if isinstance(x, list) else str(x or "")


def pre(text: str, cls: str = "") -> str:
    return f'<pre class="{cls}">{html.escape(ANSI.sub("", text).rstrip())}</pre>'


def render_output(o: dict, have_state: bool, counters: dict) -> str:
    kind = o.get("output_type")
    if kind == "stream":
        text = ANSI.sub("", text_of(o.get("text"))).rstrip()
        if not text:
            return ""
        lines = text.count("\n") + 1
        if lines > LONG_LOG:
            return f'<details class="log"><summary>Show log ({lines} lines)</summary>{pre(text)}</details>'
        return pre(text, "stream" + (" stderr" if o.get("name") == "stderr" else ""))
    if kind == "error":
        name, value = str(o.get("ename") or ""), str(o.get("evalue") or "")
        if name == "StopExecution":            # the notebook's own checkpoint, not a failure
            counters["pauses"] += 1
            return f'<p class="pause"><b>The notebook pauses here.</b> {html.escape(value)}</p>'
        counters["errors"] += 1
        trace = ANSI.sub("", "\n".join(o.get("traceback") or []))
        return (f'<details class="error"><summary>This cell stopped with an error: {html.escape(name)}: {html.escape(value[:160])}</summary>'
                f'{pre(trace)}</details>')
    data = o.get("data") or {}
    if WIDGET_VIEW in data:
        view = data[WIDGET_VIEW]
        if have_state:
            counters["widgets"] += 1
            return f'<div class="widget"><script type="{WIDGET_VIEW}">{json.dumps(view)}</script></div>'
        counters["panels"] += 1
        return '<p class="panel-note"><b>Interactive panel.</b> In the running notebook this is a set of buttons, menus or an image viewer. <a href="#launch">Launch the notebook</a> to use it.</p>'
    for mime in ("image/svg+xml", "image/png", "image/jpeg", "image/gif"):
        if mime in data:
            counters["images"] += 1
            if mime == "image/svg+xml":
                return f'<div class="out-image">{text_of(data[mime])}</div>'
            b64 = text_of(data[mime]).replace("\n", "")
            base64.b64decode(b64[:64] + "=" * (-len(b64[:64]) % 4))          # raises on something that is not base64
            return f'<div class="out-image"><img alt="Figure produced by this cell" src="data:{mime};base64,{b64}"></div>'
    if "text/html" in data:
        return f'<div class="out-html">{text_of(data["text/html"])}</div>'
    if "text/markdown" in data:
        return f'<div class="out-md">{md_renderer().render(text_of(data["text/markdown"]))}</div>'
    if "text/plain" in data:
        return pre(text_of(data["text/plain"]), "plain")
    return ""


def render_cell(md, cell: dict, have_state: bool, seen: dict, toc: list, counters: dict) -> str:
    source = text_of(cell.get("source"))
    if cell.get("cell_type") == "markdown":
        return f'<section class="md">{render_markdown(md, source, seen, toc)}</section>' if source.strip() else ""
    if cell.get("cell_type") != "code":
        return ""
    outs = "".join(render_output(o, have_state, counters) for o in cell.get("outputs") or [])
    if not source.strip() and not outs:
        return ""
    first = next((ln.lstrip("# ").strip() for ln in source.splitlines() if ln.strip().startswith("#")), "")
    if len(first) > 90:                                            # cut at a word, and say so
        first = first[:90].rsplit(" ", 1)[0].rstrip(" ,;:—-") + "…"
    label = f"Show code{': ' + html.escape(first) if first else ''}"
    code = f'<details class="code"><summary>{label}</summary>{pre(source, "source")}</details>' if source.strip() else ""
    return f'<section class="cell">{code}{outs}</section>'


def launch_block(with_id: bool = True) -> str:
    rows = []
    for title, nb, blurb in (("Guided version", GUIDED, "a form and buttons: fill it in and follow the steps; best for a first try"),
                             ("Full notebook", PIPELINE, "every step visible and editable, the one shown on this page")):
        links = " ".join(f'<a class="btn" target="_blank" rel="noopener" href="{html.escape(launch_url(server, nb))}">{region}</a>' for region, server in PLAY)
        rows.append(f'<div class="launch-row"><div><b>{title}</b><span class="muted small"> — {blurb}</span></div><div class="launch-links">{links}</div></div>')
    anchor = ' id="launch"' if with_id else ""
    return (f'<div class="launch"{anchor}><h2>Run it yourself in Neurodesk Play</h2>'
            '<p class="small">Neurodesk Play is a free browser session with the imaging tools installed (it asks you to sign in). '
            'Each button copies the CALMaR repository into your session and opens the notebook; pick the server nearer to you.</p>'
            + "".join(rows) + '</div>')


def data_check(nb: dict, allowed: tuple[str, ...]) -> dict:
    """Participant ids and dataset names found anywhere in the notebook, and whether every
    dataset named is one of the open ones."""
    blob = json.dumps(nb)
    subjects = sorted(set(re.findall(r"\bsub-[A-Za-z]*\d[A-Za-z0-9]*", blob)))
    names = set()
    for m in re.findall(r"\bds\d{6}\b|\bISLES[- ']?(?:20)?22\b|\bISLES\b", blob, flags=re.I):
        names.add(m.lower() if m.lower().startswith("ds") else ("ISLES 2022" if "22" in m else "ISLES"))
    if "ISLES 2022" in names:
        names.discard("ISLES")
    ok = {re.sub(r"[^a-z0-9]", "", a.lower()) for a in allowed}
    unknown = sorted(d for d in names if re.sub(r"[^a-z0-9]", "", d.lower()) not in ok)
    return {"subjects": subjects, "datasets": sorted(names), "unknown": unknown}


# ------------------------------------------------------------------ the page
def pull_title(cells: list[dict]) -> tuple[list[dict], str]:
    """The notebook's own '# Title' line (first markdown cell) becomes the page's eyebrow instead of
    a second, competing title in the body."""
    cells = [dict(c) for c in cells]
    for c in cells:
        src = text_of(c.get("source"))
        if c.get("cell_type") != "markdown" or not src.strip():
            continue
        m = re.match(r"\s*#\s+(.+?)\s*(?:\n|$)", src)
        if m:
            c["source"] = src[m.end():]
            return cells, re.sub(r"\s*\|\s*CALMaR\s*$", "", m.group(1)).strip()
        break
    return cells, ""


def toc_html(toc: list[tuple[int, str, str]]) -> str:
    """Sections (h2) always listed; their sub-headings (h3, h4) carry the section they belong to,
    so the page script can show only those of the section being read."""
    out, chapter = ['<a class="toc-2" href="#top" data-ch="top">Overview</a>'], "top"
    for level, anchor, text in toc:
        if level == 2:
            chapter = anchor
            out.append(f'<a class="toc-2" href="#{anchor}" data-ch="{anchor}">{html.escape(text)}</a>')
        elif level in (3, 4):
            out.append(f'<a class="toc-{level} toc-sub" href="#{anchor}" data-ch="{chapter}">{html.escape(text)}</a>')
    return "".join(out)


TOC_SCRIPT = """<script>
(() => {
  // Contents: highlight the heading being read and show only its section's sub-headings.
  const toc = document.querySelector('.nb-toc'), box = toc && toc.querySelector('details');
  if (!toc) return;
  toc.classList.add('js');
  if (box && matchMedia('(max-width: 860px)').matches) box.open = false;
  const links = [...toc.querySelectorAll('a[href^="#"]')];
  const byId = new Map(links.map((a) => [a.getAttribute('href').slice(1), a]));
  const heads = [...document.querySelectorAll('.nb h2[id], .nb h3[id], .nb h4[id]')].filter((h) => byId.has(h.id));
  let current = null;
  const show = (a) => {
    if (!a || a === current) return;
    if (current) current.classList.remove('active');
    a.classList.add('active'); current = a;
    toc.dataset.open = a.dataset.ch;
    links.forEach((l) => l.classList.toggle('open', l.dataset.ch === a.dataset.ch));
    if (!box || box.open) { const r = a.getBoundingClientRect(), t = toc.getBoundingClientRect(); if (r.top < t.top || r.bottom > t.bottom) a.scrollIntoView({ block: 'nearest' }); }
  };
  const update = () => {
    let a = byId.get('top');
    for (const h of heads) { if (h.getBoundingClientRect().top < 120) a = byId.get(h.id); else break; }
    show(a);
  };
  addEventListener('scroll', () => requestAnimationFrame(update), { passive: true });
  update();
})();
</script>"""


def build(nb: dict, title: str, source_note: str, css: str, allowed: tuple[str, ...] = OPEN_DATASETS, version: str = "") -> tuple[str, dict]:
    md = md_renderer()
    state = (nb.get("metadata") or {}).get("widgets", {}).get(WIDGET_STATE)
    have_state = bool(state and state.get("state"))
    seen: dict[str, int] = {}
    toc: list[tuple[int, str, str]] = []
    counters = {"widgets": 0, "panels": 0, "images": 0, "errors": 0, "pauses": 0}
    cells, nb_title = pull_title(nb.get("cells") or [])
    body = "".join(render_cell(md, c, have_state, seen, toc, counters) for c in cells)
    check = data_check(nb, allowed)
    outputs = sum(len(c.get("outputs") or []) for c in nb.get("cells") or [] if c.get("cell_type") == "code")
    if outputs:
        intro = ("This is a saved run of the CALMaR notebook: from a routine MRI to a lesion map and a report that cites the "
                 f'<a href="{KB_SITE}">stroke aphasia knowledge base</a>. Read it like a report; the code behind every step is one click away, '
                 "and the buttons below open the same notebook in a live session.")
        caveat = f"The run shown here uses open example data only ({html.escape(', '.join(check['datasets']) or 'no dataset named')}); nothing on this page is clinical advice."
    else:                                  # the notebook was pushed with its output cleared: say so instead of promising results
        intro = ("This is the CALMaR notebook, step by step: from a routine MRI to a lesion map and a report that cites the "
                 f'<a href="{KB_SITE}">stroke aphasia knowledge base</a>. The copy published here was saved without its results, so the page shows what each step does and the code behind it; '
                 "tables and figures appear here once a completed run is saved. The buttons below open the notebook in a live session.")
        caveat = "The examples it runs on are open data only; nothing on this page is clinical advice."
    nav = toc_html(toc)
    sections = sum(1 for lv, _, _ in toc if lv == 2)
    nb_path = source_note.split(" · ")[-1]
    nb_link = f"{REPO}/blob/{version or 'main'}/{nb_path}"
    facts = [f'<li><span class="k">Data</span> open only: {html.escape(", ".join(check["datasets"]) or "none named")}</li>',
             f'<li><span class="k">Notebook</span> <a href="{html.escape(nb_link)}" target="_blank" rel="noopener">{html.escape(nb_path)}</a>'
             + (f' at <code>{html.escape(version[:7])}</code>' if version else "") + "</li>",
             f'<li><span class="k">Sections</span> {sections}</li>',
             (f'<li><span class="k">Results</span> {counters["images"]} figures, {outputs} outputs</li>' if outputs
              else '<li class="warn"><span class="k">Results</span> not saved in this copy</li>')]
    facts_html = "".join(facts)
    eyebrow = f'<p class="eyebrow">{html.escape(nb_title)}</p>' if nb_title else ""
    widget_scripts = ""
    if have_state:
        widget_scripts = (f'<script type="{WIDGET_STATE}">{json.dumps(state)}</script>'
                          f'<script src="{html.escape(WIDGET_SCRIPTS[0])}"></script>'
                          f'<script src="{html.escape(WIDGET_SCRIPTS[1])}" crossorigin="anonymous"></script>')
    panels = (f"{counters['widgets']} interactive panels are drawn with the values they had; the ones that need Python respond only in a running session."
              if have_state else
              (f"{counters['panels']} interactive panels (buttons, menus, image viewers) are not drawn here, because this run was saved without their state; they work in a running session."
               if counters["panels"] else ""))
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="canonical" href="{PAGE_SITE}">
<meta name="description" content="A saved run of the CALMaR lesion mapping and reporting notebook on open data, readable in the browser, with buttons to run it in Neurodesk Play.">
<style>
{css}
</style>
</head>
<body class="nbpage">
<a class="skip" href="#main">Skip to content</a>
<header class="app-header">
  <a class="brand" href="{PAGE_SITE}"><span>CALMaR</span><span class="sub">notebook</span></a>
  <nav class="nav" aria-label="Site"><a href="#launch">Run it</a><a href="{KB_SITE}">Knowledge base</a><a href="{REPO}" target="_blank" rel="noopener">Code ↗</a></nav>
</header>
<div class="nb-layout">
<aside class="nb-toc" aria-label="Contents"><details open><summary class="toc-title">Contents</summary><nav>{nav}</nav></details></aside>
<main id="main" class="nb-main">
<header class="hero" id="top">
{eyebrow}
<h1>{html.escape(title)}</h1>
<p class="lead">{intro}</p>
<ul class="facts">{facts_html}</ul>
</header>
{launch_block()}
<p class="caveat">A research development built to support clinicians' reasoning, not to replace it. {caveat}</p>
{f'<p class="small muted">{panels}</p>' if panels else ''}
<article class="nb">
{body}
</article>
{launch_block(with_id=False)}
</main>
</div>
<footer class="app-footer">
  <span>Built {dt.date.today().isoformat()} from {html.escape(source_note)}{html.escape(f" at version {version[:7]}" if version else "")}</span>
  · <a href="{KB_SITE}">Stroke aphasia knowledge base</a> · <a href="{REPO}" rel="noopener">CALMaR source</a> · <a href="https://webapps.neurodesk.org/calmar/" rel="noopener">CALMaR webapp</a>
</footer>
{TOC_SCRIPT}
{widget_scripts}
</body>
</html>
"""
    return page, {**counters, "cells": len(nb.get("cells") or []), "outputs": outputs, "headings": len(toc), "widget_state": have_state, **check}


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--calmar", type=Path, default=ROOT.parent / "calmar", help="a checkout of the calmar repository (default ../calmar)")
    ap.add_argument("--notebook", default=PIPELINE, help=f"the executed notebook inside it (default {PIPELINE})")
    ap.add_argument("--out", type=Path, default=ROOT / "site" / "calmar", help="folder to write index.html into (default site/calmar)")
    ap.add_argument("--allow-dataset", action="append", default=[], metavar="NAME", help="another open dataset the run may name")
    ap.add_argument("--strict", action="store_true", help="exit with an error when the run names a dataset that is not known to be open (the workflow then publishes nothing, so the page that is live stays)")
    ap.add_argument("--source-commit", default="", metavar="SHA", help="the calmar commit the page is built from; recorded in build.json and in the page's footer")
    ap.add_argument("--widget-scripts", nargs=2, metavar=("REQUIRE_JS", "EMBED_JS"), help="other addresses for the two widget scripts (for an offline test)")
    ap.add_argument("--open", action="store_true", help="open the page in the browser afterwards")
    args = ap.parse_args(argv)
    path = args.calmar / args.notebook
    if not path.exists():
        print(f"build_notebook_page: {path} not found", file=sys.stderr)
        return 2
    if args.widget_scripts:
        WIDGET_SCRIPTS[:] = args.widget_scripts
    nb = json.loads(path.read_text(encoding="utf-8"))
    css = EXPLORER_CSS.read_text(encoding="utf-8") + "\n" + PAGE_CSS.read_text(encoding="utf-8")
    title = "CALMaR: from an MRI to a cited report"
    page, info = build(nb, title, f"micmas/calmar · {args.notebook}", css, OPEN_DATASETS + tuple(args.allow_dataset), args.source_commit)
    args.out.mkdir(parents=True, exist_ok=True)
    out = args.out / "index.html"
    out.write_text(page, encoding="utf-8")
    # what this page was built from; the explorer reads this file to know the page exists before linking to it
    (args.out / "build.json").write_text(json.dumps({
        "notebook": args.notebook, "notebook_commit": args.source_commit, "built": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "cells": info["cells"], "outputs": info["outputs"], "widgets": info["widgets"], "panels_without_state": info["panels"], "figures": info["images"],
        "datasets": info["datasets"]}, indent=1) + "\n", encoding="utf-8")
    print(f"{out}: {info['cells']} cells, {info['headings']} headings, {info['images']} figures, "
          + (f"{info['widgets']} widgets drawn from saved state" if info["widget_state"] else f"{info['panels']} interactive panels without saved state (shown as notes)")
          + f", {info['pauses']} checkpoints, {info['errors']} errors · {len(page) // 1024} KB")
    print(f"  data named in the run: {', '.join(info['datasets']) or 'none'} · participants: {', '.join(info['subjects'][:12]) or 'none'}"
          + (f" … {len(info['subjects'])} in all" if len(info["subjects"]) > 12 else ""))
    if not info["outputs"]:
        print("  ⚠ this notebook was saved without any output: the page shows the text and the code only")
    if info["errors"]:
        print(f"  ⚠ {info['errors']} cell(s) ended in an error (shown folded on the page)")
    if info["unknown"]:
        print(f"  ⚠ names a dataset not known to be open: {', '.join(info['unknown'])} (add --allow-dataset NAME if it is)")
    if args.open:
        webbrowser.open(out.resolve().as_uri())
    return 1 if (info["unknown"] and args.strict) else 0


if __name__ == "__main__":
    sys.exit(_cli())
