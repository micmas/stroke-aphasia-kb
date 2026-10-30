"""Licence of each paper in the bibliography: what its published text may be reused under.

The knowledge base quotes short source passages and publishes them in the
explorer and the CALMaR webapp (docs/GOVERNANCE.md §6). This module records,
per citation key, the licence the paper is published under, from metadata
rather than from the extraction model:

  1. Crossref   the licence URLs the publisher deposited for the DOI, each with
                the version it covers (vor = published version, am = accepted
                manuscript, tdm = text and data mining only) and a start date;
  2. Unpaywall  whether a free copy exists, its OA status and licence
                (needs an e-mail address: --email or UNPAYWALL_EMAIL);
  3. the PDF    the first and last pages of papers/<Key>.pdf, for a Creative
                Commons statement or a rights notice, when the two are silent.

Each paper gets one category:

  cc               the published version is under a Creative Commons licence (or CC0)
  cc_manuscript    only the accepted manuscript is (green OA); the published version is not
  free_to_read     a free copy exists without an open licence (publisher OA terms, bronze)
  rights_reserved  publisher terms only (a TDM licence is not a reuse licence)
  unknown          no metadata and nothing in the PDF

The record lives in screening/licences.yaml, keyed by @Key. Network access is
needed for 1 and 2 (run it on your own machine); nothing here edits the
register or citations.md.
"""
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

CATEGORIES = ("cc", "cc_manuscript", "free_to_read", "rights_reserved", "unknown")
CATEGORY_TEXT = {
    "cc": "Creative Commons (published version)",
    "cc_manuscript": "Creative Commons (accepted manuscript only)",
    "free_to_read": "free to read, no open licence",
    "rights_reserved": "publisher terms (rights reserved)",
    "unknown": "not known",
}
USER_AGENT = "stroke-aphasia-kb licences (https://github.com/micmas/stroke-aphasia-kb)"

_CC = re.compile(r"creativecommons\.org/(licenses|licences|publicdomain)/([a-z\-]+)(?:/(\d(?:\.\d)?))?", re.I)
_CC_TEXT = re.compile(
    r"(?:creative\s+commons\s+(?:attribution(?:[\s\-]+(?:non[\s\-]?commercial|no[\s\-]?derivatives?|share[\s\-]?alike))*"
    r"|cc\s*0|zero)[^.\n]{0,40}?(\d\.\d)?)|\bCC[\s\-]?BY(?:[\s\-](?:NC|ND|SA)){0,2}(?:\s*(\d\.\d))?|\bCC0\b",
    re.I)
_OPEN_TEXT = re.compile(r"\bthis is an open[\s\-]access article\b", re.I)


def cc_label(url_or_text: str) -> str | None:
    """'CC BY 4.0', 'CC BY-NC-ND', 'CC0' … from a creativecommons.org URL or a licence statement; None if not CC."""
    s = str(url_or_text or "")
    m = _CC.search(s)
    if m:
        kind, ver = m.group(2).lower(), m.group(3)
        if m.group(1).lower() == "publicdomain":
            return "CC0" if kind == "zero" else "Public domain"
        return f"CC {kind.upper()}" + (f" {ver}" if ver else "")
    low = s.lower().strip()
    m = re.fullmatch(r"cc[\s\-_]?(by(?:[\s\-_](?:nc|nd|sa)){0,2}|0|zero)", low)
    if m:
        part = m.group(1)
        return "CC0" if part in ("0", "zero") else "CC " + re.sub(r"[\s_]", "-", part).upper()
    return None


def cc_from_text(text: str) -> str | None:
    """A Creative Commons licence named in running text (the PDF's first or last pages)."""
    url = _CC.search(text or "")
    if url:
        return cc_label(url.group(0))
    m = _CC_TEXT.search(text or "")
    if not m:
        return None
    t = (text[m.start(): m.end() + 60]).lower()
    if "cc0" in t.replace(" ", "") or "zero" in t:
        return "CC0"
    parts = ["BY"]
    if re.search(r"non[\s\-]?commercial|\bnc\b", t):
        parts.append("NC")
    if re.search(r"no[\s\-]?derivative|\bnd\b", t):
        parts.append("ND")
    if re.search(r"share[\s\-]?alike|\bsa\b", t):
        parts.append("SA")
    ver = re.search(r"^[^.\n]{0,80}?(\d\.\d)", t)
    return "CC " + "-".join(parts) + (f" {ver.group(1)}" if ver else "")


def publisher_label(url: str) -> str:
    """A short name for a non-CC licence URL."""
    u = (url or "").lower()
    if "tdm" in u or "text-and-data-mining" in u or "textmining" in u:
        return "publisher TDM licence (text mining only)"
    if "open-access/userlicense" in u or "openaccess" in u.replace("-", ""):
        return "publisher open-access user licence"
    host = urllib.parse.urlparse(url).netloc.replace("www.", "") if url else ""
    return f"publisher terms ({host})" if host else "publisher terms"


def classify(crossref: list[dict] | None, unpaywall: dict | None, pdf_text: str | None = None) -> dict:
    """One record from the three sources. `crossref` is message.license (may be None), `unpaywall`
    the Unpaywall object (may be None), `pdf_text` the text of the PDF's first and last pages."""
    rec = {"category": "unknown", "label": None, "url": None, "version": None, "source": None}
    vor_cc, am_cc, other = None, None, []
    for lic in crossref or []:
        url = lic.get("URL") or ""
        ver = (lic.get("content-version") or "").lower()
        label = cc_label(url)
        if label and ver in ("vor", "unspecified", ""):
            vor_cc = vor_cc or (label, url, ver or "vor")
        elif label and ver == "am":
            am_cc = am_cc or (label, url, ver)
        elif not label:
            other.append((publisher_label(url), url, ver))
    if vor_cc:
        rec.update(category="cc", label=vor_cc[0], url=vor_cc[1], version="published", source="crossref")
        return rec
    up = unpaywall or {}
    best = up.get("best_oa_location") or {}
    # A CC licence on any free copy counts; the published version first.
    locs = [best] + [x for x in up.get("oa_locations") or [] if x is not best]
    with_cc = [x for x in locs if cc_label(x.get("license") or "")]
    if with_cc:
        best = next((x for x in with_cc if x.get("version") == "publishedVersion"), with_cc[0])
    up_label = cc_label(best.get("license") or "")
    up_version = {"publishedVersion": "published", "acceptedVersion": "accepted manuscript",
                  "submittedVersion": "preprint"}.get(best.get("version") or "", None)
    if up_label and up_version == "published":
        rec.update(category="cc", label=up_label, url=best.get("url_for_landing_page") or best.get("url"),
                   version="published", source="unpaywall")
        return rec
    pdf_label = cc_from_text(pdf_text or "") if pdf_text else None
    if pdf_label:
        rec.update(category="cc", label=pdf_label, version="published (as in the PDF)", source="pdf")
        return rec
    if am_cc:
        rec.update(category="cc_manuscript", label=am_cc[0], url=am_cc[1], version="accepted manuscript", source="crossref")
        return rec
    if up_label:
        rec.update(category="cc_manuscript", label=up_label, url=best.get("url_for_landing_page") or best.get("url"),
                   version=up_version or "other version", source="unpaywall")
        return rec
    if up.get("is_oa") or (pdf_text and _OPEN_TEXT.search(pdf_text)):
        rec.update(category="free_to_read", label=(best.get("license") or "free to read").replace("-", " "),
                   url=best.get("url_for_landing_page") or best.get("url"), version=up_version,
                   source="unpaywall" if up.get("is_oa") else "pdf")
        return rec
    if other:
        reuse = [o for o in other if "tdm" not in o[0]] or other
        rec.update(category="rights_reserved", label=reuse[0][0], url=reuse[0][1], version=reuse[0][2] or None,
                   source="crossref")
        return rec
    if unpaywall is not None:   # Unpaywall knows the DOI and finds no free copy
        rec.update(category="rights_reserved", label="no open copy known", source="unpaywall")
    return rec


# ---------------------------------------------------------------------------
# Fetching (network) and the PDF (local)
# ---------------------------------------------------------------------------

def _get_json(url: str, timeout: int = 20) -> dict | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return {}
        raise


def crossref_licences(doi: str, mailto: str | None = None) -> list[dict] | None:
    """message.license for a DOI ([] when Crossref has none, None when the DOI is not in Crossref)."""
    q = f"?mailto={urllib.parse.quote(mailto)}" if mailto else ""
    data = _get_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}{q}")
    if not data:
        return None
    return (data.get("message") or {}).get("license") or []


def unpaywall(doi: str, email: str) -> dict | None:
    data = _get_json(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={urllib.parse.quote(email)}")
    return data or None


def pdf_text(pdf: Path, first: int = 3, last: int = 1) -> str | None:
    """Text of the first and last pages of a PDF (where licence statements sit), or None."""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        return None
    try:
        with fitz.open(pdf) as doc:
            pages = list(range(min(first, doc.page_count))) + list(range(max(first, doc.page_count - last), doc.page_count))
            return "\n".join(doc[i].get_text() for i in pages)
    except Exception:  # noqa: BLE001
        return None


def check(key: str, doi: str | None, pdf: Path | None, email: str | None, pause: float = 0.12) -> dict:
    """Look up one paper; returns the record to store (with `checked` and the sources consulted)."""
    errors = []
    cr = up = None
    if doi:
        try:
            cr = crossref_licences(doi, mailto=email)
        except Exception as err:  # noqa: BLE001
            errors.append(f"crossref: {err}")
        time.sleep(pause)
        if email:
            try:
                up = unpaywall(doi, email)
            except Exception as err:  # noqa: BLE001
                errors.append(f"unpaywall: {err}")
            time.sleep(pause)
    text = pdf_text(pdf) if pdf and pdf.exists() else None
    rec = classify(cr, up, text)
    rec.update({"doi": doi, "checked": date.today().isoformat(),
                "consulted": [s for s, ok in (("crossref", cr is not None), ("unpaywall", up is not None), ("pdf", text is not None)) if ok]})
    if errors:
        rec["errors"] = errors
    return {k: v for k, v in rec.items() if v not in (None, [], "")}


def load(path: Path) -> dict:
    import yaml
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data.get("papers") or {}


def save(path: Path, papers: dict) -> None:
    import yaml
    header = ("# Licence of each paper in the bibliography — written by `screen.py licences` (scripts/licences.py)\n"
              "# from Crossref, Unpaywall and the PDF's own pages. Categories: cc, cc_manuscript, free_to_read,\n"
              "# rights_reserved, unknown. Do not edit by hand; re-run with --refresh to update.\n")
    body = yaml.safe_dump({"papers": dict(sorted(papers.items()))}, sort_keys=False, allow_unicode=True, width=120)
    path.write_text(header + body, encoding="utf-8")


def summary(papers: dict) -> dict[str, int]:
    out = {c: 0 for c in CATEGORIES}
    for rec in papers.values():
        out[rec.get("category", "unknown")] = out.get(rec.get("category", "unknown"), 0) + 1
    return out
