#!/usr/bin/env python3
"""
portal_dev.py — try the review portal on this computer, without Cloudflare or GitHub.

    python scripts/publish_portal.py                     # build portal/dist/ first (PDFs, exports, queue)
    python scripts/portal_dev.py --by you@uq.edu.au      # serve it at http://127.0.0.1:8768/
    python scripts/portal_import.py                      # then: what you sent, as the maintainer would see it

Serves portal/dist/ and stands in for the Pages Functions: /cc/ and /pdf/ serve the
annotated PDFs straight from papers/ (the hosted portal reads them from the R2 bucket),
/api/me answers with the email given by --by (the hosted portal gets it from Cloudflare Access), and
POST /api/reviews writes each record (one, or a {records: [...]} batch) into logs/portal/inbox/ with the same file name
the hosted function would commit to GitHub. Nothing leaves this computer; the
Access token check and the GitHub write are the only parts not exercised — they
have their own test (cd portal && npm test).

Records written here are real: apply them with portal_import.py or delete them
from logs/portal/inbox/ when you were only trying things out. A PDF uploaded
here lands in portal/.uploads/ (git-ignored) instead of the R2 bucket; the
import copies it into papers/ like a hosted upload.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
DIST = ROOT / "portal" / "dist"
INBOX = ROOT / "logs" / "portal" / "inbox"
APPLIED = ROOT / "logs" / "portal" / "applied"
UPLOADS = ROOT / "portal" / ".uploads"
PAPERS = ROOT / "papers"
KINDS = {"screen", "verdict", "edit", "mark", "comment"}
MAX_UPLOAD = 60 * 1024 * 1024


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(s or "").lower()).strip("-")[:40] or "x"


def make_handler(email: str, name: str):
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(DIST), **k)

        def log_message(self, fmt, *args):  # quiet
            if "/api/" in (args[0] if args else ""):
                sys.stderr.write("  %s\n" % (fmt % args))

        def _json(self, obj, status=200):
            body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _record(self, body: dict, kind: str, cid: str) -> str:
            now = dt.datetime.now(dt.timezone.utc)
            stamp = now.strftime("%Y%m%dT%H%M%SZ") + f"{now.microsecond // 1000:03d}"
            rec = {**body, "kind": kind, "id": cid, "reviewer": email, "reviewer_name": name,
                   "submitted": now.isoformat(timespec="seconds"), "portal": "local"}
            fname = f"{stamp}_{kind}_{_slug(email.split('@')[0])}_{_slug(cid.replace('drafts/', '').replace('.md', ''))}.json"
            INBOX.mkdir(parents=True, exist_ok=True)
            (INBOX / fname).write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            return f"logs/portal/inbox/{fname}"

        def _pdf(self):
            # the hosted functions/cc and functions/pdf serve these from the bucket; here, from papers/
            name_ = self.path.split("?")[0].split("/")[-1]
            if "/" in name_ or ".." in name_ or not name_.endswith(".pdf"):
                return self._json({"error": "not found"}, 404)
            f = PAPERS / name_
            ft = re.fullmatch(r"(C\d+)_fulltext\.pdf", name_)
            if ft:                                   # a full text to assess: the source PDF named in portal/papers.json
                try:
                    entry = json.loads((ROOT / "portal" / "papers.json").read_text(encoding="utf-8")).get("fulltext", {}).get(ft.group(1)) or {}
                except (OSError, ValueError):
                    entry = {}
                f = PAPERS / str(entry.get("file") or name_)
            if not f.is_file():
                self.send_response(404); self.end_headers(); return None
            data = f.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)
            return None

        def do_GET(self):  # noqa: N802
            if self.path.startswith(("/cc/", "/pdf/")):
                return self._pdf()
            if self.path == "/api/me":
                return self._json({"email": email, "name": name, "repo": "(local)", "branch": "(local)"})
            if self.path.startswith("/api/apply"):
                n = len(list(INBOX.glob("*.json"))) if INBOX.is_dir() else 0
                return self._json({"maintainer": True, "inbox": n, "run": None, "local": True})
            if self.path.startswith("/api/reviews"):
                return self._json({"inbox": sorted(p.name for p in INBOX.glob("*.json")) if INBOX.is_dir() else [],
                                   "applied": sorted(p.name for p in APPLIED.glob("*.json")) if APPLIED.is_dir() else []})
            if self.path.startswith("/api/upload?file="):          # one upload's bytes (functions/api/upload.js)
                cid = parse_qs(urlsplit(self.path).query).get("file", [""])[0]
                f = UPLOADS / f"{_slug(cid)}.pdf"
                if not cid or not f.is_file():
                    return self._json({"error": "not found"}, 404)
                data = f.read_bytes()
                self.send_response(200); self.send_header("Content-Type", "application/pdf")
                self.send_header("Content-Length", str(len(data))); self.send_header("Cache-Control", "no-store"); self.end_headers()
                self.wfile.write(data)
                return None
            if self.path.startswith("/api/upload"):
                ups = []
                for meta in sorted(UPLOADS.glob("*.json")) if UPLOADS.is_dir() else []:
                    try:
                        ups.append(json.loads(meta.read_text(encoding="utf-8")))
                    except ValueError:
                        continue
                return self._json({"uploads": ups})
            if self.path.startswith("/api/requests"):      # the hosted portal lists reviewer requests from its bucket
                return self._json({"requests": []})
            if self.path.startswith("/api/signin"):        # hosted: Cloudflare Access signs the reviewer in, then the portal
                self.send_response(302); self.send_header("Location", "/"); self.end_headers()
                return None
            if self.path.startswith("/api/"):
                return self._json({"error": "not found"}, 404)
            return super().do_GET()

        def do_POST(self):  # noqa: N802
            if self.path.startswith("/api/upload"):
                return self._upload()
            if self.path.startswith("/api/apply"):
                return self._json({"error": "no workflow here: run `python scripts/portal_import.py --execute` in a terminal"}, 501)
            if self.path.startswith("/welcome/request"):   # the welcome page's form: nothing is kept locally
                self.rfile.read(int(self.headers.get("Content-Length") or 0))
                print("  welcome page: a reviewer request was sent (local stand-in: not stored)")
                return self._json({"ok": True})
            if not self.path.startswith("/api/reviews"):
                return self._json({"error": "not found"}, 404)
            n = int(self.headers.get("Content-Length") or 0)
            try:
                body = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
            except ValueError:
                return self._json({"error": "JSON body expected"}, 400)
            batch = body.get("records") if isinstance(body.get("records"), list) else [body]
            if not batch:
                return self._json({"error": "no records"}, 400)
            for rec in batch:
                if not isinstance(rec, dict) or str(rec.get("kind") or "") not in KINDS or not str(rec.get("id") or ""):
                    return self._json({"error": "kind and id are required"}, 400)
            files = [self._record(rec, str(rec["kind"]), str(rec["id"])) for rec in batch]
            return self._json({"ok": True, "file": files[0], "files": files, "commit": "local"})

        def _upload(self):
            # the hosted function's twin (portal/functions/api/upload.js): the file goes to portal/.uploads/
            q = parse_qs(urlsplit(self.path).query)
            cid = (q.get("id") or [""])[0].strip()
            fname = re.sub(r"[^\w.() -]+", "_", (q.get("name") or [""])[0].strip())[:120] or "paper.pdf"
            citation = (q.get("citation") or [""])[0].strip() or None
            n = int(self.headers.get("Content-Length") or 0)
            if not cid:
                return self._json({"error": "id is required (the candidate id, or the citation key)"}, 400)
            if n > MAX_UPLOAD:
                return self._json({"error": f"file too large (the limit is {MAX_UPLOAD // 1048576} MB)"}, 413)
            data = self.rfile.read(n)
            if len(data) < 1024 or not data.startswith(b"%PDF-"):
                return self._json({"error": "that is not a PDF"}, 400)
            key = f"uploads/{_slug(cid)}.pdf"
            UPLOADS.mkdir(parents=True, exist_ok=True)
            local = UPLOADS / f"{_slug(cid)}.pdf"
            meta_path = UPLOADS / f"{_slug(cid)}.json"
            if meta_path.exists():
                try:
                    prev = json.loads(meta_path.read_text(encoding="utf-8"))
                    if prev.get("by") != email:
                        return self._json({"error": f"a PDF for {cid} was already uploaded by {prev.get('by')} and is waiting for the maintainer"}, 409)
                except ValueError:
                    pass
            local.write_bytes(data)
            sha = hashlib.sha256(data).hexdigest()
            uploaded = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
            meta_path.write_text(json.dumps({"object": key, "id": cid, "name": fname, "bytes": len(data), "by": email, "uploaded": uploaded, "sha256": sha}, indent=1), encoding="utf-8")
            rec = self._record({"citation": citation, "name": fname, "bytes": len(data), "sha256": sha, "bucket": "", "object": key,
                                "local_path": str(local.relative_to(ROOT)), "replaced": False}, "pdf", cid)
            return self._json({"ok": True, "file": rec, "commit": "local", "object": key, "bytes": len(data)})

    return Handler


def _cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--by", required=True, help="the email to act as (the hosted portal takes it from Cloudflare Access)")
    ap.add_argument("--name", default=None)
    ap.add_argument("--port", type=int, default=8768)
    ap.add_argument("--no-open", action="store_true")
    args = ap.parse_args(argv)
    if not (DIST / "index.html").exists() or not (DIST / "manifest.json").exists():
        print("portal/dist/ is not built: run  python scripts/publish_portal.py  first", file=sys.stderr)
        return 1
    if not (DIST / "vendor" / "pdf.min.mjs").exists():
        print("pdf.js is missing from the build: run  cd portal && npm install  then build again", file=sys.stderr)
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(args.by.lower(), args.name or args.by.split("@")[0]))
    url = f"http://127.0.0.1:{args.port}/"
    print(f"Review portal (local) at {url} as {args.by}; records go to logs/portal/inbox/. Ctrl-C to stop.")
    if not args.no_open:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
