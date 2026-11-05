#!/usr/bin/env python3
"""
portal_dev.py — try the review portal on this computer, without Cloudflare or GitHub.

    python scripts/publish_portal.py                     # build portal/dist/ first (PDFs, exports, queue)
    python scripts/portal_dev.py --by you@uq.edu.au      # serve it at http://127.0.0.1:8768/
    python scripts/portal_import.py                      # then: what you sent, as the maintainer would see it

Serves portal/dist/ and stands in for the two Pages Functions: /api/me answers with
the email given by --by (the hosted portal gets it from Cloudflare Access), and
POST /api/reviews writes each record into logs/portal/inbox/ with the same file name
the hosted function would commit to GitHub. Nothing leaves this computer; the
Access token check and the GitHub write are the only parts not exercised — they
have their own test (cd portal && npm test).

Records written here are real: apply them with portal_import.py or delete them
from logs/portal/inbox/ when you were only trying things out.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repository root (this file lives in scripts/)
DIST = ROOT / "portal" / "dist"
INBOX = ROOT / "logs" / "portal" / "inbox"
APPLIED = ROOT / "logs" / "portal" / "applied"
KINDS = {"screen", "verdict", "edit", "mark", "comment"}


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

        def do_GET(self):  # noqa: N802
            if self.path == "/api/me":
                return self._json({"email": email, "name": name, "repo": "(local)", "branch": "(local)"})
            if self.path.startswith("/api/reviews"):
                return self._json({"inbox": sorted(p.name for p in INBOX.glob("*.json")) if INBOX.is_dir() else [],
                                   "applied": sorted(p.name for p in APPLIED.glob("*.json")) if APPLIED.is_dir() else []})
            if self.path.startswith("/api/"):
                return self._json({"error": "not found"}, 404)
            return super().do_GET()

        def do_POST(self):  # noqa: N802
            if not self.path.startswith("/api/reviews"):
                return self._json({"error": "not found"}, 404)
            n = int(self.headers.get("Content-Length") or 0)
            try:
                body = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
            except ValueError:
                return self._json({"error": "JSON body expected"}, 400)
            kind, cid = str(body.get("kind") or ""), str(body.get("id") or "")
            if kind not in KINDS or not cid:
                return self._json({"error": "kind and id are required"}, 400)
            now = dt.datetime.now(dt.timezone.utc)
            stamp = now.strftime("%Y%m%dT%H%M%SZ") + f"{now.microsecond // 1000:03d}"
            rec = {**body, "kind": kind, "id": cid, "reviewer": email, "reviewer_name": name,
                   "submitted": now.isoformat(timespec="seconds"), "portal": "local"}
            fname = f"{stamp}_{kind}_{_slug(email.split('@')[0])}_{_slug(cid.replace('drafts/', '').replace('.md', ''))}.json"
            INBOX.mkdir(parents=True, exist_ok=True)
            (INBOX / fname).write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            return self._json({"ok": True, "file": f"logs/portal/inbox/{fname}", "commit": "local"})

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
