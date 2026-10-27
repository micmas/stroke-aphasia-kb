#!/usr/bin/env python3
"""
review_app.py — the review workbench: a draft's findings on the left, the
whole paper on the right with every source passage highlighted, and edits
written straight back into the draft.

    python scripts/review_app.py                                   # index of every draft, pick one
    python scripts/review_app.py --draft drafts/regions/left_angular_gyrus__Breining2022.md
    python scripts/review_app.py --citation Breining2022            # every draft of that paper
    python scripts/review_app.py --port 8766 --no-open

What the page does
------------------
* Left: each finding with its claim, direction, relationship, strength,
  confidence, flags and author limitations — all editable — and its
  source passages, each with the grade quote_check.py gives it
  (exact / elided / table / anchored / near / absent), the page it was
  found on, and a button that scrolls the paper to it. A passage's
  quote, page and `supports` tag can be changed; a passage can be removed.
* Right: every page of the PDF, rendered with PyMuPDF, with the passages
  highlighted in the same colours as the annotated PDF (aphasia_kb.
  SUPPORTS_COLORS). Select words by dragging across them: the exact text
  of the PDF's text layer becomes a quote you can attach to a finding
  (choosing what it supports) or **mark for re-extraction** with a note —
  marks are saved under the draft as `reviewer_marks` and
  `python scripts/refocus.py <draft>` asks the local model to write findings for
  exactly those passages.
* Save (button or Ctrl/Cmd-S) validates against docs/schema.md, keeps a copy of
  the previous version in drafts/_backup/, rewrites the draft, stamps an
  `edits` record on each changed finding, appends REVIEW-EDITED to
  logs/extraction_log.md and regenerates papers/<Key>_annotated.pdf so the file
  on disk matches what you see.

Only drafts can be edited — never the canonical folders; promote.py stays
the one way in. The server binds to 127.0.0.1 only and needs no
dependency beyond PyMuPDF and PyYAML.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import shutil
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # sibling modules in scripts/
from annotate_paper import _find_quote_rects, annotate  # noqa: E402
from aphasia_kb import (CONFIDENCE_VOCAB, DIRECTION_VOCAB, METHOD_VOCAB, RELATIONSHIP_VOCAB,  # noqa: E402
                        STRENGTH_VOCAB, SUPPORTS_COLORS, SUPPORTS_VOCAB, TARGET_KIND_VOCAB,
                        THERAPY_RELATIONSHIPS, _validate_v2_entry, parse_markdown)
from quote_check import PaperText, find_paper, grade_quote  # noqa: E402

DRAFTS = ROOT / "drafts"
PAPERS = ROOT / "papers"
BACKUP = DRAFTS / "_backup"
LOG = ROOT / "logs/extraction_log.md"
BUCKETS = ("regions", "impairments", "therapies", "predictors", "reviews")
DPI = 120
EDITABLE_FIELDS = ("claim", "direction", "relationship", "strength", "author_limitations",
                   "target", "target_kind", "method", "therapy")
EDITABLE_PROVENANCE = ("confidence", "flags")


def _open_pdf(path: Path):
    try:
        import pymupdf as fitz
    except ImportError:  # pragma: no cover
        import fitz
    return fitz.open(str(path))


# ---------------------------------------------------------------------------
# Draft access
# ---------------------------------------------------------------------------

def draft_path(rel: str) -> Path:
    """drafts/<bucket>/<file>.md, refusing anything outside drafts/."""
    p = (DRAFTS / rel).resolve()
    if p.suffix != ".md" or DRAFTS.resolve() not in p.parents or p.parent.name not in BUCKETS:
        raise PermissionError(f"not a draft: {rel}")
    if not p.exists():
        raise FileNotFoundError(rel)
    return p


def list_drafts() -> list[dict]:
    out = []
    for b in BUCKETS:
        d = DRAFTS / b
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            try:
                fm, _ = parse_markdown(p)
            except Exception as e:  # noqa: BLE001
                out.append({"rel": f"{b}/{p.name}", "error": str(e).splitlines()[0]})
                continue
            findings = [f for f in fm.get("findings") or [] if isinstance(f, dict)]
            cite = next((str(f.get("citation")) for f in findings if f.get("citation")), "")
            pdf = find_paper(cite, PAPERS)
            out.append({"rel": f"{b}/{p.name}", "bucket": b, "id": fm.get("id"), "name": fm.get("name"),
                        "status": fm.get("status"), "citation": cite, "findings": len(findings),
                        "marks": sum(1 for m in fm.get("reviewer_marks") or [] if m.get("status", "pending") == "pending"),
                        "pdf": bool(pdf and pdf.suffix.lower() == ".pdf"), "created_by": fm.get("created_by")})
    return out


def entry_ids() -> dict:
    """Known ids per kind (canonical + drafts), for the target and therapy pickers."""
    out: dict[str, dict[str, str]] = {"impairment": {}, "region": {}, "therapy": {}, "predictor": {}}
    kind_of = {"regions": "region", "impairments": "impairment", "therapies": "therapy", "predictors": "predictor"}
    for b, kind in kind_of.items():
        for folder in (ROOT / b, DRAFTS / b):
            if not folder.is_dir():
                continue
            for p in sorted(folder.glob("*.md")):
                try:
                    fm, _ = parse_markdown(p)
                except Exception:  # noqa: BLE001
                    continue
                if fm.get("id"):
                    out[kind].setdefault(str(fm["id"]), str(fm.get("name") or ""))
    return out


def _write_draft(path: Path, fm: dict, body: str) -> None:
    yaml_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)
    path.write_text(f"---\n{yaml_text}---\n{body}", encoding="utf-8")


class Session:
    """One open draft: its PDF, page renders, words and passage locations, cached."""

    def __init__(self, rel: str):
        self.rel = rel
        self.path = draft_path(rel)
        self.fm, self.body = parse_markdown(self.path)
        findings = [f for f in self.fm.get("findings") or [] if isinstance(f, dict)]
        self.citation = next((str(f.get("citation")) for f in findings if f.get("citation")), "")
        self.pdf = find_paper(self.citation, PAPERS)
        if self.pdf is None or self.pdf.suffix.lower() != ".pdf":
            raise FileNotFoundError(f"no PDF for {self.citation or '(no citation)'} in papers/")
        self.doc = _open_pdf(self.pdf)
        self.paper = PaperText.from_pdf(self.pdf)
        self.lock = threading.Lock()
        self._png: dict[int, bytes] = {}
        self._words: dict[int, list] = {}

    def reload(self) -> None:
        self.fm, self.body = parse_markdown(self.path)

    def pages(self) -> list[dict]:
        return [{"w": p.rect.width, "h": p.rect.height} for p in self.doc]

    def png(self, n: int, dpi: int = DPI) -> bytes:
        with self.lock:
            if n not in self._png:
                pix = self.doc[n].get_pixmap(dpi=dpi, alpha=False)
                self._png[n] = pix.tobytes("png")
            return self._png[n]

    def words(self, n: int) -> list:
        with self.lock:
            if n not in self._words:
                self._words[n] = [[round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1), w]
                                  for x0, y0, x1, y1, w, *_ in self.doc[n].get_text("words")]
            return self._words[n]

    def locate(self, quote: str, hint_page) -> tuple[int | None, list]:
        order = list(range(self.doc.page_count))
        if isinstance(hint_page, int) and 0 <= hint_page - 1 < self.doc.page_count:
            order = [hint_page - 1] + [p for p in order if p != hint_page - 1]
        for pno in order:
            rects, _ = _find_quote_rects(self.doc[pno], quote)
            if rects:
                return pno, [[round(r.x0, 1), round(r.y0, 1), round(r.x1, 1), round(r.y1, 1)] for r in rects]
        return None, []

    def passage_info(self, quote: str, hint_page) -> dict:
        pno, rects = self.locate(quote, hint_page)
        return {"page": (pno + 1) if pno is not None else None, "rects": rects,
                "grade": grade_quote(quote, self.paper) if quote else "absent"}

    def payload(self) -> dict:
        findings = [f for f in self.fm.get("findings") or [] if isinstance(f, dict)]
        located = {}
        for f in findings:
            for i, p in enumerate(f.get("source_passages") or []):
                if isinstance(p, dict):
                    located[f"{f.get('id')}/{i}"] = self.passage_info(str(p.get("quote") or ""), p.get("page"))
        marks = {}
        for m in self.fm.get("reviewer_marks") or []:
            if isinstance(m, dict):
                marks[str(m.get("id"))] = self.passage_info(str(m.get("quote") or ""), m.get("page"))
        return {"rel": self.rel, "citation": self.citation, "pdf": self.pdf.name, "pages": self.pages(),
                "frontmatter": self.fm, "body": self.body, "located": located, "marks": marks,
                "issues": _issues(self.fm, self.rel),
                "colors": SUPPORTS_COLORS, "entryIds": entry_ids(),
                "vocab": {"supports": sorted(SUPPORTS_VOCAB), "direction": sorted(DIRECTION_VOCAB),
                          "relationship": sorted(RELATIONSHIP_VOCAB), "strength": sorted(STRENGTH_VOCAB),
                          "confidence": sorted(CONFIDENCE_VOCAB), "target_kind": sorted(TARGET_KIND_VOCAB),
                          "method": sorted(METHOD_VOCAB), "therapy_relationships": sorted(THERAPY_RELATIONSHIPS)}}


# ---------------------------------------------------------------------------
# Saving
# ---------------------------------------------------------------------------

def _changed_fields(old: dict, new: dict) -> list[str]:
    out = []
    for k in EDITABLE_FIELDS:
        if old.get(k) != new.get(k):
            out.append(k)
    for k in EDITABLE_PROVENANCE:
        if (old.get("provenance") or {}).get(k) != (new.get("provenance") or {}).get(k):
            out.append(f"provenance.{k}")
    if (old.get("source_passages") or []) != (new.get("source_passages") or []):
        out.append("source_passages")
    return out


def _issues(fm: dict, src: str) -> list[str]:
    issues: list[str] = []
    check = dict(fm)
    check["_path"] = src
    _validate_v2_entry(check, src, issues)
    return [i.split(": ", 1)[-1] for i in issues]


def apply_save(session: Session, new_fm: dict, by: str) -> dict:
    """Validate, back up, write, log, re-annotate. Returns the fresh payload."""
    if not by or by.lower().startswith(("model", "agent")):
        raise ValueError("the reviewer must be a named person")
    if new_fm.get("status") not in ("draft", "in_review", None):
        raise ValueError("only drafts can be edited here")
    today = dt.date.today().isoformat()
    old_by_id = {f.get("id"): f for f in session.fm.get("findings") or [] if isinstance(f, dict)}
    changed_total: list[str] = []
    for f in new_fm.get("findings") or []:
        if not isinstance(f, dict):
            continue
        for p in f.get("source_passages") or []:
            if isinstance(p, dict):
                if p.get("supports") not in SUPPORTS_VOCAB:
                    raise ValueError(f"{f.get('id')}: supports must be one of {sorted(SUPPORTS_VOCAB)}")
                if not str(p.get("quote") or "").strip():
                    raise ValueError(f"{f.get('id')}: a passage has an empty quote")
                if p.get("page") in ("", None):
                    p["page"] = None
                else:
                    p["page"] = int(p["page"])
        if isinstance(f.get("method"), str) and "," in f["method"]:
            f["method"] = [m.strip() for m in f["method"].split(",") if m.strip()]
        th = f.get("therapy")
        if isinstance(th, dict):
            th = {k: str(v).strip() for k, v in th.items() if str(v or "").strip()}
            f["therapy"] = th if th.get("name") else None
            if f["therapy"] is None:
                f.pop("therapy")
        old = old_by_id.get(f.get("id"))
        changed = _changed_fields(old, f) if old else ["new"]
        if changed:
            f.setdefault("edits", []).append({"by": f"human:{by}", "date": today, "fields": changed})
            changed_total.append(f"{f.get('id')}:{','.join(changed)}")
    for m in new_fm.get("reviewer_marks") or []:
        if isinstance(m, dict):
            m.setdefault("by", f"human:{by}")
            m.setdefault("date", today)
            m.setdefault("status", "pending")
    if not new_fm.get("reviewer_marks"):
        new_fm.pop("reviewer_marks", None)
    # A draft may already carry validation issues (extract.py saves them anyway for review);
    # an edit must not add new ones, and the remaining ones are reported back to the page.
    before = _issues(session.fm, session.rel)
    after = _issues(new_fm, session.rel)
    new_issues = [i for i in after if i not in before]
    if new_issues:
        raise ValueError("schema: " + "; ".join(i.split(": ", 1)[-1] for i in new_issues[:6]))
    BACKUP.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(session.path, BACKUP / f"{session.path.stem}.{stamp}.md")
    _write_draft(session.path, new_fm, session.body)
    session.reload()
    old_marks = {m.get("id") for m in session.fm.get("reviewer_marks") or [] if isinstance(m, dict)}
    n_marks = len(old_marks)
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"{today} | REVIEW-EDITED | {session.citation or '?'} | {session.fm.get('id')} | "
                 f"{'; '.join(changed_total) or 'no finding changed'} | {n_marks} reviewer mark(s) pending | "
                 f"reviewer: human:{by}\n")
    annotated = None
    try:
        drafts = [p for p in session.path.parent.parent.glob(f"*/*__{session.citation.lstrip('@')}.md")]
        annotate(drafts or [session.path], session.pdf, add_legend=True)
        annotated = session.pdf.with_name(f"{session.pdf.stem}_annotated.pdf").name
    except SystemExit as e:  # annotate() raises SystemExit on empty drafts
        annotated = f"not regenerated: {e}"
    except Exception as e:  # noqa: BLE001
        annotated = f"not regenerated: {str(e)[:80]}"
    out = session.payload()
    out["saved"] = {"backup": f"drafts/_backup/{session.path.stem}.{stamp}.md", "annotated": annotated,
                    "changed": changed_total}
    return out


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

SESSIONS: dict[str, Session] = {}
SESSIONS_LOCK = threading.Lock()


def get_session(rel: str) -> Session:
    with SESSIONS_LOCK:
        s = SESSIONS.get(rel)
        if s is None:
            s = SESSIONS[rel] = Session(rel)
        return s


class Handler(BaseHTTPRequestHandler):
    server_version = "stroke-aphasia-kb-review/1.0"

    def log_message(self, fmt, *args):  # quieter console
        if "/api/page/" not in (args[0] if args else ""):
            sys.stderr.write("  %s\n" % (fmt % args))

    def _send(self, status: int, body: bytes, ctype: str = "application/json; charset=utf-8") -> None:
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, status: int = 200) -> None:
        self._send(status, json.dumps(obj, ensure_ascii=False, default=str).encode("utf-8"))

    def _error(self, e: Exception, status: int = 400) -> None:
        self._json({"error": f"{type(e).__name__}: {e}"}, status)

    def do_GET(self):  # noqa: N802
        u = urlparse(self.path)
        q = parse_qs(u.query)
        try:
            if u.path == "/":
                return self._send(200, index_page().encode("utf-8"), "text/html; charset=utf-8")
            if u.path.startswith("/review/"):
                rel = unquote(u.path[len("/review/"):])
                draft_path(rel)
                return self._send(200, app_page(rel).encode("utf-8"), "text/html; charset=utf-8")
            if u.path.startswith("/api/draft/"):
                return self._json(get_session(unquote(u.path[len("/api/draft/"):])).payload())
            m = re.match(r"^/api/page/(.+)/(\d+)\.png$", u.path)
            if m:
                s = get_session(unquote(m.group(1)))
                return self._send(200, s.png(int(m.group(2)), int(q.get("dpi", [DPI])[0])), "image/png")
            m = re.match(r"^/api/words/(.+)/(\d+)$", u.path)
            if m:
                return self._json(get_session(unquote(m.group(1))).words(int(m.group(2))))
            if u.path == "/api/drafts":
                return self._json(list_drafts())
            return self._json({"error": "not found"}, 404)
        except (FileNotFoundError, PermissionError) as e:
            return self._error(e, 404)
        except Exception as e:  # noqa: BLE001
            return self._error(e, 500)

    def do_POST(self):  # noqa: N802
        u = urlparse(self.path)
        try:
            n = int(self.headers.get("Content-Length") or 0)
            data = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
            if u.path.startswith("/api/save/"):
                s = get_session(unquote(u.path[len("/api/save/"):]))
                return self._json(apply_save(s, data.get("frontmatter") or {}, str(data.get("by") or "").strip()))
            if u.path.startswith("/api/locate/"):
                s = get_session(unquote(u.path[len("/api/locate/"):]))
                return self._json(s.passage_info(str(data.get("quote") or ""), data.get("page")))
            return self._json({"error": "not found"}, 404)
        except (FileNotFoundError, PermissionError) as e:
            return self._error(e, 404)
        except ValueError as e:
            return self._error(e, 400)
        except Exception as e:  # noqa: BLE001
            return self._error(e, 500)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def index_page() -> str:
    rows = []
    for d in list_drafts():
        if d.get("error"):
            rows.append(f"<tr><td colspan=6 class=err>{html.escape(d['rel'])}: {html.escape(d['error'])}</td></tr>")
            continue
        link = (f"<a href=\"/review/{html.escape(d['rel'])}\">{html.escape(d['rel'])}</a>" if d["pdf"]
                else f"<span class=muted title=\"no PDF in papers/\">{html.escape(d['rel'])}</span>")
        rows.append(f"<tr><td>{link}</td><td>{html.escape(str(d.get('name') or ''))}</td><td>{html.escape(d['citation'])}</td>"
                    f"<td class=num>{d['findings']}</td><td class=num>{d['marks'] or ''}</td><td>{html.escape(str(d.get('status')))}"
                    f"{'' if d['pdf'] else ' · <span class=err>no PDF</span>'}</td></tr>")
    return (f"<!doctype html><html lang=en><head><meta charset=utf-8><title>Review workbench</title><style>{CSS}</style></head>"
            f"<body class=index><header><h1>Review workbench</h1><span class=muted>drafts/ · pick one</span></header>"
            f"<main><table><thead><tr><th>Draft</th><th>Entry</th><th>Paper</th><th class=num>Findings</th><th class=num>Marks</th><th>Status</th></tr></thead>"
            f"<tbody>{''.join(rows)}</tbody></table></main></body></html>")


def app_page(rel: str) -> str:
    return (f"<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content=\"width=device-width\">"
            f"<title>Review · {html.escape(rel)}</title><style>{CSS}</style></head>"
            f"<body data-rel=\"{html.escape(rel)}\"><div id=app><p class=muted style=\"padding:1rem\">Loading…</p></div>"
            f"<script>{JS}</script></body></html>")


CSS = r"""
:root{--grape:#52489c;--blue:#4062bb;--cyan:#59c3c3;--cyan-ink:#1f7f7f;--pink:#f45b69;--ink:#2b2b3a;--ink2:#5a5a66;--line:#ebebeb;--line2:#d6d6d6;--panel:#f7f7f7}
*{box-sizing:border-box}
body{margin:0;font:14px/1.45 Inter,"Helvetica Neue",Arial,sans-serif;color:var(--ink);background:#fff}
body.index main{max-width:1100px;margin:0 auto;padding:1rem}
header{display:flex;align-items:center;gap:1rem;padding:.5rem 1rem;border-bottom:1px solid var(--line);background:#fff;position:sticky;top:0;z-index:10}
h1{font-size:1.05rem;color:var(--grape);margin:0}
h2{font-size:.95rem;color:var(--grape);margin:.2rem 0}
a{color:var(--blue);text-decoration:none}a:hover{text-decoration:underline}
.muted{color:var(--ink2)}.small{font-size:.82rem}.err{color:var(--pink)}
table{border-collapse:collapse;width:100%;font-size:.9rem}th,td{text-align:left;padding:.35rem .5rem;border-bottom:1px solid var(--line);vertical-align:top}th{font-size:.75rem;text-transform:uppercase;color:var(--ink2)}.num{text-align:right}
button{font:inherit;font-size:.82rem;padding:.25rem .6rem;border:1px solid var(--line2);border-radius:5px;background:#fff;color:var(--ink);cursor:pointer}button:hover{border-color:var(--blue);color:var(--blue)}
button.primary{background:var(--grape);border-color:var(--grape);color:#fff}button.primary:hover{color:#fff;filter:brightness(1.1)}button.primary:disabled{opacity:.5;cursor:default}
button.danger:hover{border-color:var(--pink);color:var(--pink)}
select,input[type=text],input[type=number],textarea{font:inherit;font-size:.86rem;padding:.2rem .35rem;border:1px solid var(--line2);border-radius:4px;color:var(--ink);background:#fff}
textarea{width:100%;resize:vertical;min-height:2.6em;line-height:1.35}
#app{display:grid;grid-template-columns:minmax(380px,46%) 1fr;height:100vh}
#left{overflow:auto;border-right:1px solid var(--line);display:flex;flex-direction:column}
#left .body{padding:.6rem .8rem 3rem}
#right{overflow:auto;background:#e9e9ee;position:relative}
.toolbar{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap;padding:.45rem .8rem;border-bottom:1px solid var(--line);position:sticky;top:0;background:#fff;z-index:5}
.toolbar .status{margin-left:auto;font-size:.8rem;color:var(--ink2)}
.toolbar .dirty{color:var(--pink);font-weight:600}
.finding{border:1px solid var(--line);border-radius:6px;padding:.55rem .7rem;margin:.55rem 0;background:#fff}
.finding.active{border-color:var(--grape);box-shadow:0 0 0 3px rgba(82,72,156,.12)}
.finding .head{display:flex;gap:.5rem;align-items:baseline;flex-wrap:wrap}
.finding .head .id{font-family:ui-monospace,Menlo,monospace;font-size:.78rem;background:var(--panel);border:1px solid var(--line2);border-radius:4px;padding:0 .35rem}
.finding .head .route{font-size:.82rem;color:var(--ink2);display:flex;gap:.3rem;align-items:center;flex-wrap:wrap}
.finding .head input.target{font-weight:600;color:var(--ink);width:16em}
.finding .head input.target.unknown{border-color:var(--pink);border-style:dashed}
.row.therapy{background:var(--panel);border-radius:5px;padding:.3rem .45rem}
.row.therapy.missing{border:1px dashed var(--pink)}
.row{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;margin:.3rem 0;font-size:.82rem}
.row label{color:var(--ink2)}
.row select{max-width:170px}
.list{font-size:.84rem}.list .item{display:flex;gap:.3rem;align-items:flex-start;margin:.15rem 0}.list .item input{flex:1}
.passage{border-left:4px solid var(--line2);padding:.35rem .55rem;margin:.4rem 0;background:var(--panel);border-radius:0 5px 5px 0}
.passage.active{outline:2px solid var(--grape)}
.passage .meta{display:flex;gap:.45rem;align-items:center;flex-wrap:wrap;font-size:.78rem;color:var(--ink2);margin-bottom:.2rem}
.grade{padding:0 .4rem;border-radius:999px;font-weight:600;border:1px solid transparent}
.grade-exact,.grade-elided,.grade-table{background:var(--cyan);color:#10303a}
.grade-anchored,.grade-near{background:rgba(64,98,187,.12);color:var(--ink);border-color:var(--blue)}
.grade-absent,.grade-no_pdf{background:rgba(244,91,105,.12);color:var(--ink);border-color:var(--pink)}
.marks{border:1px dashed var(--pink);border-radius:6px;padding:.5rem .7rem;margin:.8rem 0;background:rgba(244,91,105,.05)}
.mark{display:grid;grid-template-columns:1fr auto;gap:.3rem .6rem;align-items:start;margin:.3rem 0;font-size:.84rem;border-bottom:1px solid var(--line);padding-bottom:.3rem}
.mark .quote{font-style:italic}
.page{position:relative;margin:12px auto;background:#fff;box-shadow:0 1px 4px rgba(0,0,0,.2);user-select:none}
.page img{display:block;width:100%;height:auto;pointer-events:none}
.page .pno{position:absolute;top:4px;right:6px;font-size:.72rem;color:var(--ink2);background:rgba(255,255,255,.8);padding:0 .3rem;border-radius:3px}
.hl{position:absolute;border-radius:2px;opacity:.42;cursor:pointer;mix-blend-mode:multiply}
.hl.active{outline:2px solid var(--grape);opacity:.6}
.hl.mark{background:var(--pink)!important;opacity:.35;border:1px dashed var(--pink)}
.w{position:absolute;cursor:text}
.w.sel{background:rgba(82,72,156,.35)}
#seltool{position:fixed;z-index:20;background:#fff;border:1px solid var(--line2);border-radius:6px;box-shadow:0 4px 16px rgba(0,0,0,.18);padding:.5rem .65rem;max-width:420px;font-size:.84rem}
#seltool .q{font-style:italic;max-height:5.5em;overflow:auto;margin:.2rem 0 .4rem;color:var(--ink2)}
#seltool .actions{display:flex;gap:.4rem;flex-wrap:wrap;align-items:center}
.notice{background:var(--panel);border:1px solid var(--line2);border-radius:6px;padding:.5rem .7rem;font-size:.84rem;margin:.4rem 0}
.zoom{display:inline-flex;gap:.2rem;align-items:center}
kbd{font:inherit;font-size:.75rem;border:1px solid var(--line2);border-bottom-width:2px;border-radius:3px;padding:0 .3rem;background:var(--panel)}
@media (max-width:900px){#app{grid-template-columns:1fr;height:auto}#left{max-height:50vh}}
"""

JS = r"""
const REL = document.body.dataset.rel;
const api = (p) => `/api/${p}/${encodeURI(REL)}`;
const state = { data: null, fm: null, dirty: false, active: null, zoom: 1, sel: null, by: localStorage.getItem('review-by') || '' };
const h = (tag, attrs = {}, ...kids) => { const el = document.createElement(tag); for (const [k, v] of Object.entries(attrs)) { if (v === null || v === undefined || v === false) continue; if (k === 'class') el.className = v; else if (k === 'text') el.textContent = v; else if (k.startsWith('on')) el.addEventListener(k.slice(2), v); else if (k === 'style') el.style.cssText = v; else el.setAttribute(k, v === true ? '' : v); } for (const c of kids.flat(Infinity)) if (c !== null && c !== undefined && c !== false) el.append(c instanceof Node ? c : document.createTextNode(String(c))); return el; };
const esc = (s) => String(s ?? '');
const findings = () => (state.fm.findings || []).filter((f) => f && typeof f === 'object');
const marks = () => (state.fm.reviewer_marks = state.fm.reviewer_marks || []);
const setDirty = (v = true) => { state.dirty = v; const s = document.getElementById('status'); if (s) { s.textContent = v ? 'unsaved changes' : 'saved'; s.classList.toggle('dirty', v); } document.getElementById('saveBtn').disabled = !v; };
window.addEventListener('resize', () => { if (state.data) layoutPages(); });
window.addEventListener('beforeunload', (e) => { if (state.dirty) { e.preventDefault(); e.returnValue = ''; } });

async function load() {
  const res = await fetch(api('draft'));
  const data = await res.json();
  if (data.error) { document.getElementById('app').replaceChildren(h('div', { class: 'notice err', style: 'margin:1rem', text: data.error })); return; }
  state.data = data; state.fm = data.frontmatter;
  render();
}

function render() {
  const app = document.getElementById('app');
  app.replaceChildren(left(), right());
  layoutPages();
  setDirty(state.dirty);
}
// After an edit that changes structure (passage or mark added/removed): rebuild the
// left pane and redraw the highlights, keeping the rendered pages and both scroll positions.
function refresh() {
  const leftEl = document.getElementById('left'); const top = leftEl ? leftEl.scrollTop : 0;
  leftEl.replaceWith(left());
  document.getElementById('left').scrollTop = top;
  document.querySelectorAll('.page').forEach((el) => drawHighlights(el, Number(el.dataset.n) + 1, Number(el.dataset.scale)));
  setDirty(state.dirty);
}

function left() {
  const d = state.data;
  const tb = h('div', { class: 'toolbar' },
    h('a', { href: '/', class: 'small', text: '← drafts' }),
    h('b', { text: `${state.fm.id || ''}` }), h('span', { class: 'small muted', text: `${d.citation} · ${d.pdf} · ${d.pages.length} pages` }),
    h('label', { class: 'small muted' }, 'reviewer ', h('input', { type: 'text', value: state.by, placeholder: 'your name', size: 10, oninput: (e) => { state.by = e.target.value.trim(); localStorage.setItem('review-by', state.by); } })),
    h('button', { id: 'saveBtn', class: 'primary', onclick: save, text: 'Save' }),
    h('span', { id: 'status', class: 'status', text: 'saved' }));
  const body = h('div', { class: 'body' });
  body.append(h('p', { class: 'small muted' }, h('b', { text: esc(state.fm.name) }), ` · ${esc(state.fm.status)} · ${esc(state.fm.created_by)}. Drag across words in the paper to quote them; `, h('kbd', { text: '⌘/Ctrl S' }), ' saves. Edits are stamped with your name; promote.py still decides what enters the KB.'));
  if (d.issues?.length) body.append(h('div', { class: 'notice' }, h('b', { text: `${d.issues.length} validation issue(s) promote.py will refuse:` }), h('ul', { class: 'small' }, d.issues.map((x) => h('li', { text: x })))));
  body.append(marksPanel());
  for (const f of findings()) body.append(findingCard(f));
  return h('div', { id: 'left' }, tb, body);
}

function marksPanel() {
  const ms = marks();
  const pending = ms.filter((m) => (m.status || 'pending') === 'pending');
  const box = h('div', { class: 'marks' }, h('h2', { text: `Reviewer marks for re-extraction (${pending.length} pending)` }),
    h('p', { class: 'small muted', text: 'Passages no finding covers yet. After saving, run  python scripts/refocus.py <draft>  and the local model writes findings for exactly these; they come back here as new drafts to review.' }));
  if (!ms.length) box.append(h('p', { class: 'small muted', text: 'None yet — select words in the paper and choose "Mark for re-extraction".' }));
  for (const m of ms) {
    const loc = state.data.marks[m.id];
    box.append(h('div', { class: 'mark' },
      h('div', {}, h('div', { class: 'quote', text: `“${esc(m.quote)}”` }),
        h('div', { class: 'small muted' }, `${m.id} · page ${esc(m.page)} · ${esc(m.status || 'pending')}${m.by ? ` · ${m.by}` : ''}`, loc?.page ? h('button', { style: 'margin-left:.4rem', onclick: () => goTo(loc.page, loc.rects, `mark:${m.id}`), text: 'show' }) : null),
        h('input', { type: 'text', value: m.note || '', placeholder: 'note for the extractor (what this passage shows)', style: 'width:100%;margin-top:.2rem', oninput: (e) => { m.note = e.target.value; setDirty(); } })),
      h('div', {}, h('button', { class: 'danger', onclick: () => { state.fm.reviewer_marks = ms.filter((x) => x !== m); setDirty(); refresh(); }, text: 'remove' }))));
  }
  return box;
}

function findingCard(f) {
  const v = state.data.vocab;
  const prov = (f.provenance = f.provenance || {});
  const sel = (key, obj, options, label) => h('label', {}, `${label} `, h('select', { onchange: (e) => { obj[key] = e.target.value; setDirty(); if (key === 'relationship') refresh(); } }, options.map((o) => h('option', { value: o, selected: obj[key] === o ? '' : null, text: o })), options.includes(obj[key]) ? null : h('option', { value: obj[key] ?? '', selected: '', text: `${obj[key] ?? '(unset)'}` })));
  const listEditor = (key, obj, label) => {
    const items = Array.isArray(obj[key]) ? obj[key] : (obj[key] ? [String(obj[key])] : []);
    obj[key] = items;
    const box = h('div', { class: 'list' }, h('div', { class: 'row' }, h('label', { text: label }), h('button', { onclick: () => { items.push(''); setDirty(); refresh(); }, text: '+ add' })));
    items.forEach((it, i) => box.append(h('div', { class: 'item' }, h('input', { type: 'text', value: it, oninput: (e) => { items[i] = e.target.value; setDirty(); } }), h('button', { class: 'danger', onclick: () => { items.splice(i, 1); setDirty(); refresh(); }, text: '×' }))));
    return box;
  };
  const ids = state.data.entryIds || {};
  const targetList = h('datalist', { id: `targets-${f.id}` }, Object.entries(ids[f.target_kind] || {}).map(([id, name]) => h('option', { value: id, text: name })));
  const therapyList = h('datalist', { id: `therapies-${f.id}` }, Object.entries(ids.therapy || {}).map(([id, name]) => h('option', { value: id, text: name })));
  const needsTherapy = (state.data.vocab.therapy_relationships || []).includes(f.relationship) || f.target_kind === 'therapy';
  const th = (f.therapy && typeof f.therapy === 'object') ? f.therapy : (f.therapy = {});
  const knownTarget = Boolean((ids[f.target_kind] || {})[f.target]);
  const card = h('div', { class: `finding${state.active === f.id ? ' active' : ''}`, id: `finding-${f.id}`, onclick: () => { if (state.active !== f.id) { state.active = f.id; document.querySelectorAll('.finding').forEach((el) => el.classList.toggle('active', el.id === `finding-${f.id}`)); } } },
    h('div', { class: 'head' }, h('span', { class: 'id', text: f.id }),
      h('span', { class: 'route' }, '→ ', h('input', { type: 'text', list: `targets-${f.id}`, value: esc(f.target), title: knownTarget ? `${ids[f.target_kind][f.target]} (entry exists)` : 'no entry with this id yet (forward-looking id)', class: knownTarget ? 'target' : 'target unknown', oninput: (e) => { f.target = e.target.value.trim(); setDirty(); } }), targetList,
        ' ', h('select', { title: 'target kind', onchange: (e) => { f.target_kind = e.target.value; setDirty(); refresh(); } }, state.data.vocab.target_kind.map((o) => h('option', { value: o, selected: f.target_kind === o ? '' : null, text: o }))),
        ` · ${esc(f.citation)} · `, h('input', { type: 'text', value: Array.isArray(f.method) ? f.method.join(', ') : esc(f.method), title: `method (comma-separated): ${state.data.vocab.method.join(', ')}`, style: 'width:11em', oninput: (e) => { f.method = e.target.value; setDirty(); } }))),
    h('div', { class: `row therapy${needsTherapy && !th.name ? ' missing' : ''}` },
      h('label', { text: needsTherapy ? 'therapy (required for this relationship)' : 'therapy' }),
      h('input', { type: 'text', value: esc(th.name || ''), placeholder: 'as the paper names it, e.g. cueing hierarchy anomia treatment', style: 'flex:1;min-width:200px', oninput: (e) => { th.name = e.target.value; setDirty(); } }),
      h('input', { type: 'text', list: `therapies-${f.id}`, value: esc(th.id || ''), placeholder: 'entry id (optional)', style: 'width:14em', oninput: (e) => { th.id = e.target.value.trim(); setDirty(); } }), therapyList,
      h('input', { type: 'text', value: esc(th.dose || ''), placeholder: 'dose', style: 'width:9em', oninput: (e) => { th.dose = e.target.value; setDirty(); } })),
    h('textarea', { rows: 3, oninput: (e) => { f.claim = e.target.value; setDirty(); } }, esc(f.claim)),
    h('div', { class: 'row' }, sel('direction', f, v.direction, 'direction'), sel('relationship', f, v.relationship, 'relationship'), sel('strength', f, v.strength, 'strength'), sel('confidence', prov, v.confidence, 'confidence')),
    listEditor('flags', prov, 'flags'), listEditor('author_limitations', f, 'author limitations'),
    h('div', { class: 'row' }, h('label', { text: `source passages (${(f.source_passages || []).length})` }), h('button', { onclick: () => { (f.source_passages = f.source_passages || []).push({ section: '', page: null, quote: '', supports: 'claim' }); setDirty(); refresh(); }, text: '+ passage (type it)' }), h('span', { class: 'small muted', text: 'or select words in the paper' })));
  (f.source_passages || []).forEach((p, i) => card.append(passageCard(f, p, i)));
  return card;
}

function passageCard(f, p, i) {
  const key = `${f.id}/${i}`;
  const loc = state.data.located[key] || { page: null, rects: [], grade: 'absent' };
  const colour = state.data.colors[p.supports] || '#ccc';
  const card = h('div', { class: `passage${state.active === key ? ' active' : ''}`, id: `p-${key.replace('/', '-')}`, style: `border-left-color:${colour}` },
    h('div', { class: 'meta' },
      h('span', { class: `grade grade-${loc.grade}`, text: loc.grade }),
      h('label', {}, 'supports ', h('select', { onchange: (e) => { p.supports = e.target.value; setDirty(); refresh(); } }, state.data.vocab.supports.map((o) => h('option', { value: o, selected: p.supports === o ? '' : null, text: o })))),
      h('label', {}, 'page ', h('input', { type: 'number', min: 1, value: p.page ?? '', style: 'width:4.5em', oninput: (e) => { p.page = e.target.value === '' ? null : Number(e.target.value); setDirty(); } })),
      loc.page && loc.page !== p.page ? h('span', { class: 'err', text: `found on ${loc.page}` }) : null,
      loc.page ? h('button', { onclick: () => goTo(loc.page, loc.rects, key), text: 'show in paper' }) : h('span', { class: 'err small', text: 'not found in the PDF' }),
      h('button', { onclick: () => relocate(f, p, i), text: 'check' }),
      h('button', { class: 'danger', onclick: () => { f.source_passages.splice(i, 1); setDirty(); refresh(); }, text: 'remove' })),
    h('textarea', { rows: 2, oninput: (e) => { p.quote = e.target.value; setDirty(); } }, esc(p.quote)),
    h('input', { type: 'text', value: p.section || '', placeholder: 'section (e.g. Results)', style: 'width:100%;margin-top:.2rem', oninput: (e) => { p.section = e.target.value; setDirty(); } }));
  return card;
}

async function relocate(f, p, i) {
  const res = await fetch(api('locate'), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ quote: p.quote, page: p.page }) });
  const info = await res.json();
  state.data.located[`${f.id}/${i}`] = info;
  refresh();
  if (info.page) goTo(info.page, info.rects, `${f.id}/${i}`);
}

// ---------------- paper pane ----------------
function right() {
  const pane = h('div', { id: 'right' });
  const bar = h('div', { class: 'toolbar' },
    h('span', { class: 'small muted', text: `${state.data.pdf}` }),
    h('span', { class: 'zoom' }, h('button', { onclick: () => setZoom(state.zoom - 0.15), text: '−' }), h('span', { class: 'small muted', id: 'zoomLabel', text: `${Math.round(state.zoom * 100)}%` }), h('button', { onclick: () => setZoom(state.zoom + 0.15), text: '+' })),
    h('span', { class: 'small muted', text: 'colours: ' }, Object.entries(state.data.colors).map(([k, c]) => h('span', { class: 'small', style: `background:${c};padding:0 .35rem;border-radius:3px;margin-right:.25rem`, text: k }))),
    h('span', { class: 'small', style: 'background:rgba(244,91,105,.25);padding:0 .35rem;border-radius:3px;border:1px dashed var(--pink)', text: 'reviewer mark' }));
  pane.append(bar, h('div', { id: 'pages' }));
  pane.addEventListener('mousedown', selStart); pane.addEventListener('mousemove', selMove); document.addEventListener('mouseup', selEnd);
  return pane;
}
// Pages are laid out once the pane is in the document, so their width is the pane's real width.
function layoutPages() {
  const pane = document.getElementById('right'); const wrap = document.getElementById('pages');
  wrap.replaceChildren(...state.data.pages.map((pg, n) => pageEl(pg, n)));
  const io = new IntersectionObserver((entries) => { for (const e of entries) if (e.isIntersecting) ensurePage(e.target); }, { root: pane, rootMargin: '600px 0px' });
  wrap.querySelectorAll('.page').forEach((el) => io.observe(el));
}
function pageWidth() { return Math.min(900, (document.getElementById('right')?.clientWidth || 800) - 40) * state.zoom; }
function pageEl(pg, n) {
  const w = pageWidth(); const scale = w / pg.w;
  const el = h('div', { class: 'page', id: `page-${n + 1}`, 'data-n': n, 'data-scale': scale, style: `width:${w}px;height:${pg.h * scale}px` }, h('span', { class: 'pno', text: `p. ${n + 1}` }));
  drawHighlights(el, n + 1, scale);
  return el;
}
function setZoom(z) { state.zoom = Math.max(0.5, Math.min(2.5, z)); const r = document.getElementById('right'); const frac = r.scrollTop / document.getElementById('pages').scrollHeight; layoutPages(); document.getElementById('zoomLabel').textContent = `${Math.round(state.zoom * 100)}%`; r.scrollTop = frac * document.getElementById('pages').scrollHeight; }
async function ensurePage(el) {
  if (el.dataset.loaded) return; el.dataset.loaded = '1';
  const n = Number(el.dataset.n);
  el.prepend(h('img', { src: `${api('page')}/${n}.png`, alt: `page ${n + 1}`, draggable: false }));
  const words = await (await fetch(`${api('words')}/${n}`)).json();
  const scale = Number(el.dataset.scale);
  const layer = h('div', { class: 'words' });
  words.forEach(([x0, y0, x1, y1, t], i) => layer.append(h('span', { class: 'w', 'data-i': i, 'data-t': t, 'data-p': n + 1, style: `left:${x0 * scale}px;top:${y0 * scale}px;width:${(x1 - x0) * scale}px;height:${(y1 - y0) * scale}px` })));
  el.append(layer);
}
function drawHighlights(el, pageNo, scale) {
  el.querySelectorAll('.hl').forEach((x) => x.remove());
  for (const f of findings()) (f.source_passages || []).forEach((p, i) => {
    const key = `${f.id}/${i}`; const loc = state.data.located[key];
    if (!loc || loc.page !== pageNo) return;
    for (const [x0, y0, x1, y1] of loc.rects) el.append(h('div', { class: `hl${state.active === key ? ' active' : ''}`, 'data-key': key, title: `${f.id} · ${p.supports}`, style: `left:${x0 * scale}px;top:${y0 * scale}px;width:${(x1 - x0) * scale}px;height:${(y1 - y0) * scale}px;background:${state.data.colors[p.supports] || '#ccc'}`, onclick: (e) => { e.stopPropagation(); focusPassage(key); } }));
  });
  for (const m of marks()) { const loc = state.data.marks[m.id]; if (!loc || loc.page !== pageNo) continue; for (const [x0, y0, x1, y1] of loc.rects) el.append(h('div', { class: 'hl mark', title: `reviewer mark ${m.id}`, style: `left:${x0 * scale}px;top:${y0 * scale}px;width:${(x1 - x0) * scale}px;height:${(y1 - y0) * scale}px` })); }
}
function focusPassage(key) {
  state.active = key;
  document.querySelectorAll('.passage').forEach((el) => el.classList.toggle('active', el.id === `p-${key.replace('/', '-')}`));
  document.querySelectorAll('.hl').forEach((el) => el.classList.toggle('active', el.dataset.key === key));
  const card = document.getElementById(`p-${key.replace('/', '-')}`); if (card) card.scrollIntoView({ block: 'center', behavior: 'smooth' });
}
function goTo(pageNo, rects, key) {
  const el = document.getElementById(`page-${pageNo}`); if (!el) return;
  ensurePage(el);
  const scale = Number(el.dataset.scale); const y = rects.length ? rects[0][1] * scale : 0;
  const right = document.getElementById('right');
  right.scrollTo({ top: el.offsetTop + y - 160, behavior: 'smooth' });
  if (key) { state.active = key; document.querySelectorAll('.hl').forEach((x) => x.classList.toggle('active', x.dataset.key === key)); }
}

// ---------------- word selection ----------------
function wordAt(e) { const t = e.target; return t && t.classList && t.classList.contains('w') ? t : null; }
function selStart(e) { const w = wordAt(e); clearSel(); if (!w || e.button !== 0) return; state.sel = { page: w.dataset.p, a: Number(w.dataset.i), b: Number(w.dataset.i), layer: w.parentElement }; paintSel(); e.preventDefault(); }
function selMove(e) { if (!state.sel) return; const w = wordAt(e); if (!w || w.parentElement !== state.sel.layer) return; state.sel.b = Number(w.dataset.i); paintSel(); }
function paintSel() { const { a, b, layer } = state.sel; const lo = Math.min(a, b); const hi = Math.max(a, b); layer.querySelectorAll('.w').forEach((x) => { const i = Number(x.dataset.i); x.classList.toggle('sel', i >= lo && i <= hi); }); }
function selEnd(e) {
  if (!state.sel) return;
  const { a, b, layer, page } = state.sel; state.sel = null;
  const lo = Math.min(a, b); const hi = Math.max(a, b);
  const words = [...layer.querySelectorAll('.w')].filter((x) => { const i = Number(x.dataset.i); return i >= lo && i <= hi; });
  const quote = words.map((x) => x.dataset.t).join(' ').replace(/-\s+(?=[a-z])/g, '');
  if (!quote.trim()) { clearSel(); return; }
  showSelTool(e.clientX, e.clientY, quote, Number(page));
}
function clearSel() { document.querySelectorAll('.w.sel').forEach((x) => x.classList.remove('sel')); document.getElementById('seltool')?.remove(); }
function showSelTool(x, y, quote, page) {
  document.getElementById('seltool')?.remove();
  const fs = findings(); const v = state.data.vocab;
  const fsel = h('select', {}, fs.map((f) => h('option', { value: f.id, selected: state.active && String(state.active).split('/')[0] === f.id ? '' : null, text: `${f.id} · ${String(f.claim || '').slice(0, 50)}` })));
  const ssel = h('select', {}, v.supports.map((o) => h('option', { value: o, text: o })));
  const note = h('input', { type: 'text', placeholder: 'note for the extractor (optional)', style: 'width:100%;margin-top:.3rem' });
  const tool = h('div', { id: 'seltool', style: `left:${Math.min(x, window.innerWidth - 440)}px;top:${Math.min(y + 12, window.innerHeight - 170)}px` },
    h('div', { class: 'small muted', text: `page ${page} · ${quote.split(' ').length} words` }), h('div', { class: 'q', text: quote }),
    h('div', { class: 'actions' }, fs.length ? ['attach to ', fsel, ' as ', ssel, h('button', { class: 'primary', onclick: () => { attach(fsel.value, ssel.value, quote, page); }, text: 'Attach' })] : h('span', { class: 'small muted', text: 'no finding to attach to' })),
    note,
    h('div', { class: 'actions', style: 'margin-top:.3rem' }, h('button', { onclick: () => { addMark(quote, page, note.value); }, text: 'Mark for re-extraction' }), h('button', { onclick: () => { navigator.clipboard?.writeText(quote); }, text: 'Copy' }), h('button', { onclick: clearSel, text: 'Cancel' })));
  document.body.append(tool);
}
async function attach(fid, supports, quote, page) {
  const f = findings().find((x) => x.id === fid); if (!f) return;
  (f.source_passages = f.source_passages || []).push({ section: '', page, quote, supports });
  const i = f.source_passages.length - 1;
  const info = await (await fetch(api('locate'), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ quote, page }) })).json();
  state.data.located[`${fid}/${i}`] = info;
  setDirty(); clearSel(); refresh(); focusPassage(`${fid}/${i}`);
}
async function addMark(quote, page, note) {
  const ms = marks(); const n = ms.reduce((m, x) => Math.max(m, Number(String(x.id || '').replace(/^m/, '')) || 0), 0) + 1;
  const m = { id: `m${n}`, page, quote, note: note || '', status: 'pending' };
  ms.push(m);
  state.data.marks[m.id] = await (await fetch(api('locate'), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ quote, page }) })).json();
  setDirty(); clearSel(); refresh();
}

// ---------------- save ----------------
async function save() {
  if (!state.by) { alert('Give your name in the reviewer box first: edits are stamped with it.'); return; }
  const btn = document.getElementById('saveBtn'); btn.disabled = true; btn.textContent = 'Saving…';
  try {
    const res = await fetch(api('save'), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ frontmatter: state.fm, by: state.by }) });
    const data = await res.json();
    if (data.error) { alert(`Not saved — ${data.error}`); btn.disabled = false; btn.textContent = 'Save'; return; }
    state.data = data; state.fm = data.frontmatter; state.dirty = false;
    refresh();
    document.getElementById('status').textContent = `saved · backup ${data.saved.backup.split('/').pop()} · ${data.saved.annotated || ''}`;
  } catch (e) { alert(`Not saved — ${e.message}`); btn.disabled = false; btn.textContent = 'Save'; }
}
document.addEventListener('keydown', (e) => { if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 's') { e.preventDefault(); if (state.dirty) save(); } if (e.key === 'Escape') clearSel(); });
load();
"""


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--draft", type=Path, help="open this draft")
    ap.add_argument("--citation", help="open the first draft of this paper (@Key or Key)")
    ap.add_argument("--port", type=int, default=8766)
    ap.add_argument("--no-open", action="store_true", help="do not open the browser")
    args = ap.parse_args(argv)
    start = "/"
    if args.draft:
        rel = str(args.draft.resolve().relative_to(DRAFTS.resolve()))
        draft_path(rel)
        start = f"/review/{rel}"
    elif args.citation:
        key = args.citation.lstrip("@")
        hits = [d for d in list_drafts() if d.get("citation", "").lstrip("@") == key]
        if not hits:
            print(f"no draft cites @{key}", file=sys.stderr)
            return 1
        start = f"/review/{hits[0]['rel']}"
        if len(hits) > 1:
            print(f"{len(hits)} drafts cite @{key}; opening {hits[0]['rel']} (the index lists the others)")
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}{start}"
    print(f"Review workbench at {url}  (Ctrl-C to stop)")
    if not args.no_open:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
