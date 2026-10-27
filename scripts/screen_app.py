#!/usr/bin/env python3
"""
screen_app.py — the screening workbench: title/abstract and full-text screening in
the browser, one record at a time, keyboard first (docs/SCREENING.md §4).

    python scripts/screen_app.py --by michele                      # title/abstract, ranked (§4.1)
    python scripts/screen_app.py --by michele --stage ft           # full text (opens papers/<Key>.pdf when present)
    python scripts/screen_app.py --by alex --check --sample 0.2    # second screener's blind sample

Runs on this computer only (127.0.0.1) and needs no network: abstracts come from
the local cache, ranking is local. Each decision is written at once to a journal
(screening/_sheet/app_journal.jsonl) and the register (screening/candidates.yaml)
is saved a few seconds after you stop typing, and on quit (Ctrl-C). The ranking
is redone in the background every --rerank decisions. Do not run other commands
that write the register while the app is open; if the register changes on disk,
the app stops saving and says so (your decisions stay in the journal and are
replayed the next time it starts).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random
import sys
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import screen as SC  # noqa: E402
import screening as S  # noqa: E402

JOURNAL = ROOT / "screening" / "_sheet" / "app_journal.jsonl"
STAGE = {"ta": "title_abstract", "title_abstract": "title_abstract", "ft": "full_text", "full_text": "full_text"}


class Store:
    def __init__(self, by: str, stage: str, check: bool, sample: float, seed: int, rerank: int):
        if not by or by.lower() in ("model", "legacy", "agent", "unknown"):
            raise SystemExit("--by must name a person")
        self.by, self.stage, self.check, self.sample, self.seed, self.rerank = by, stage, check, sample, seed, rerank
        self.lock = threading.RLock()
        self.path = ROOT / "screening" / "candidates.yaml"
        self.candidates = S.load_candidates()
        self.by_id = {c["id"]: c for c in self.candidates}
        self.strategies = S.load_strategies()
        self.abstracts = SC.load_abstracts()
        self.mtime = self.path.stat().st_mtime if self.path.exists() else 0
        self.session: list[tuple[str, dict]] = []
        self.dirty, self.last_change, self.unsaved, self.error = False, 0.0, 0, ""
        self.seq = SC._next_seq(self.candidates)
        self.queue: list[str] = []
        self.rank_info: dict = {}
        self.ranking = False
        self.since_rank = 0
        self._replay_journal()
        self._build_queue(initial=True)

    # -- journal ---------------------------------------------------------------------
    def _journal(self, entry: dict) -> None:
        JOURNAL.parent.mkdir(parents=True, exist_ok=True)
        with JOURNAL.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def _replay_journal(self) -> None:
        if not JOURNAL.exists():
            return
        n = 0
        for line in JOURNAL.read_text(encoding="utf-8").splitlines():
            try:
                e = json.loads(line)
            except ValueError:
                continue
            c = self.by_id.get(e.get("id"))
            if c is None:
                continue
            hist = c.setdefault("screening", [])
            if e.get("op") == "decide" and e["rec"] not in hist:
                hist.append(e["rec"])
                n += 1
            elif e.get("op") == "undo" and e["rec"] in hist:
                hist.remove(e["rec"])
                n += 1
        if n:
            print(f"replayed {n} journal entries from an earlier session; saving the register")
            self.seq = SC._next_seq(self.candidates)
            self.dirty, self.unsaved = True, n
            self.save(force=True)
        else:
            JOURNAL.unlink()

    # -- queue -----------------------------------------------------------------------
    def _todo_ids(self) -> list[str]:
        rows = S.enrich(self.candidates, {})
        if self.check:
            pool = [c["id"] for c in self.candidates
                    if (d := S.last_decision(c, self.stage)) and str(d.get("by")).lower() != "legacy"
                    and not S.last_decision(c, self.stage, role=S.CHECK_ROLE)]
            random.Random(self.seed).shuffle(pool)
            k = round(len(pool) * self.sample) if self.sample < 1 else int(self.sample)
            return pool[:k]
        want = {"title_abstract": ("awaiting_ta", "unsure_ta"), "full_text": ("awaiting_ft", "unsure_ft")}[self.stage]
        return [r["id"] for r in rows if r["stage"] in want]

    def _build_queue(self, initial: bool = False) -> None:
        todo = self._todo_ids()
        if self.stage == "title_abstract" and not self.check:
            if initial:
                print(f"ranking {len(todo)} records …", flush=True)
                t = time.time()
                self.queue, self.rank_info = SC.rank_order(self.candidates, todo, self.abstracts, self.strategies)
                self.rank_info["seconds"] = round(time.time() - t, 1)
                print(f"ranked in {self.rank_info['seconds']} s", flush=True)
            else:
                self._rerank_async()
        else:
            self.queue = sorted(todo)

    def _rerank_async(self) -> None:
        if self.ranking:
            return
        self.ranking = True

        def work():
            try:
                with self.lock:
                    snapshot = json.loads(json.dumps(self.candidates))
                    todo = self._todo_ids()
                t = time.time()
                order, info = SC.rank_order(snapshot, todo, self.abstracts, self.strategies)
                info["seconds"] = round(time.time() - t, 1)
                with self.lock:
                    decided = {cid for cid in todo if self._decided(cid)}
                    self.queue = [i for i in order if i not in decided]
                    self.rank_info = info
                    self.since_rank = 0
            finally:
                self.ranking = False
        threading.Thread(target=work, daemon=True).start()

    def _decided(self, cid: str) -> bool:
        """Done for this queue: decided by a person — an earlier "unsure" comes back, one from
        this session does not."""
        c = self.by_id[cid]
        if self.check:
            return bool(S.last_decision(c, self.stage, role=S.CHECK_ROLE))
        d = S.last_decision(c, self.stage)
        if not d or str(d.get("by")).lower() == "legacy":
            return False
        return d.get("decision") != "unsure" or any(rec is d for _, rec in self.session)

    def next(self, n: int, skip: set[str]) -> list[dict]:
        with self.lock:
            out = []
            for cid in self.queue:
                if cid in skip or self._decided(cid):
                    continue
                out.append(self.card(cid))
                if len(out) >= n:
                    break
            return out

    def card(self, cid: str) -> dict:
        c = self.by_id[cid]
        blind = self.stage == "title_abstract" or self.check
        srcs = [s.get("search") for s in c.get("sources") or [] if isinstance(s, dict) and s.get("search")]
        if not blind:
            srcs += [S.SOURCE_KINDS.get(s.get("kind"), s.get("kind")) for s in c.get("sources") or []
                     if isinstance(s, dict) and s.get("kind")]
        pdf = None
        if self.stage == "full_text" and c.get("key"):
            stem = str(c["key"]).lstrip("@")
            if (ROOT / "papers" / f"{stem}.pdf").exists():
                pdf = f"/pdf/{stem}.pdf"
        sug = c.get("suggestion") if (self.stage == "title_abstract" and not self.check) else None
        prev = None
        if self.stage == "full_text" and not self.check:
            d = S.last_decision(c, "title_abstract")
            prev = d.get("decision") if d else None
        return {"id": cid, "title": c.get("title") or "", "year": c.get("year"), "journal": c.get("journal") or "",
                "authors": (c.get("authors") or "")[:200], "doi": c.get("doi"), "pmid": c.get("pmid"),
                "abstract": self.abstracts.get(cid, ""), "sources": srcs, "key": None if blind else c.get("key"),
                "pdf": pdf, "suggestion": sug, "previous": prev}

    # -- decisions -------------------------------------------------------------------
    def decide(self, cid: str, decision: str, reason: str | None, note: str | None) -> dict:
        with self.lock:
            c = self.by_id.get(cid)
            if c is None:
                return {"error": f"{cid}: not in the register"}
            seq = None if self.check else self.seq
            err = SC._apply_decision(c, self.stage, decision, reason or None, self.by, note or None,
                                     dt.date.today().isoformat(), role=S.CHECK_ROLE if self.check else None, seq=seq)
            if err:
                return {"error": err}
            rec = c["screening"][-1]
            if seq:
                self.seq += 1
            self._journal({"op": "decide", "id": cid, "rec": rec})
            self.session.append((cid, rec))
            self.dirty, self.last_change, self.unsaved = True, time.time(), self.unsaved + 1
            self.since_rank += 1
            if self.stage == "title_abstract" and not self.check and self.since_rank >= self.rerank:
                self._rerank_async()
            return {"ok": True, "state": self.state()}

    def undo(self) -> dict:
        with self.lock:
            if not self.session:
                return {"error": "nothing to undo in this session"}
            cid, rec = self.session.pop()
            hist = self.by_id[cid].get("screening") or []
            if rec in hist:
                hist.remove(rec)
            self._journal({"op": "undo", "id": cid, "rec": rec})
            self.dirty, self.last_change, self.unsaved = True, time.time(), self.unsaved + 1
            if cid in self.queue:
                self.queue.remove(cid)
            self.queue.insert(0, cid)
            return {"ok": True, "card": self.card(cid), "state": self.state()}

    def save(self, force: bool = False) -> None:
        with self.lock:
            if not self.dirty:
                return
            now = self.path.stat().st_mtime if self.path.exists() else 0
            if now != self.mtime and not force:
                self.error = ("screening/candidates.yaml changed on disk since the app loaded it — not saving. "
                              "Quit (Ctrl-C) and start the app again: your decisions are kept in the journal.")
                return
            S.save_candidates(self.candidates)
            self.mtime = self.path.stat().st_mtime
            self.dirty, self.unsaved, self.error = False, 0, ""
            if JOURNAL.exists():
                JOURNAL.unlink()

    def log_session(self) -> None:
        """One log line for the session, written on quit."""
        if not self.session:
            return
        n: dict[str, int] = {}
        for _, rec in self.session:
            n[rec.get("decision")] = n.get(rec.get("decision"), 0) + 1
        SC._log("SCREENED", f"{self.stage} (screen_app{' check' if self.check else ''})",
                f"{len(self.session)} decisions: " + ", ".join(f"{k} {v}" for k, v in sorted(n.items())) + f" | by: {self.by}")

    def saver(self) -> None:
        while True:
            time.sleep(1.0)
            if self.dirty and time.time() - self.last_change > 3:
                try:
                    self.save()
                except Exception as e:  # noqa: BLE001
                    self.error = f"saving failed: {e}"

    def state(self) -> dict:
        with self.lock:
            st = S.stopping_state(self.candidates, self.strategies) if self.stage == "title_abstract" else None
            left = sum(1 for cid in self.queue if not self._decided(cid))
            session_counts: dict[str, int] = {}
            for _, rec in self.session:
                session_counts[rec.get("decision")] = session_counts.get(rec.get("decision"), 0) + 1
            reasons = [(k, v["label"]) for k, v in S.REASONS.items()
                       if (self.stage == "full_text" or not v["ft_only"]) and k != "not_screened_stopping_rule"]
            return {"stage": self.stage, "check": self.check, "by": self.by, "left": left, "stopping": st,
                    "session": session_counts, "sessionTotal": len(self.session), "ranking": self.ranking,
                    "rank": self.rank_info, "sinceRank": self.since_rank, "rerank": self.rerank,
                    "saved": not self.dirty, "error": self.error, "reasons": reasons}


STORE: Store | None = None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code: int = 200) -> None:
        self._send(code, json.dumps(obj, ensure_ascii=False).encode(), "application/json; charset=utf-8")

    def do_GET(self):  # noqa: N802
        u = urlparse(self.path)
        if u.path == "/":
            return self._send(200, PAGE.encode(), "text/html; charset=utf-8")
        if u.path == "/api/state":
            return self._json(STORE.state())
        if u.path == "/api/next":
            q = parse_qs(u.query)
            n = int((q.get("n") or ["8"])[0])
            skip = set((q.get("skip") or [""])[0].split(",")) - {""}
            return self._json({"cards": STORE.next(n, skip)})
        if u.path.startswith("/pdf/"):
            name = Path(unquote(u.path[5:])).name
            p = ROOT / "papers" / name
            if p.suffix.lower() == ".pdf" and p.exists():
                return self._send(200, p.read_bytes(), "application/pdf")
        return self._send(404, b"not found", "text/plain")

    def do_POST(self):  # noqa: N802
        n = int(self.headers.get("Content-Length") or 0)
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except ValueError:
            return self._json({"error": "bad request"}, 400)
        if self.path == "/api/decide":
            return self._json(STORE.decide(str(body.get("id")), str(body.get("decision")), body.get("reason"), body.get("note")))
        if self.path == "/api/undo":
            return self._json(STORE.undo())
        if self.path == "/api/save":
            STORE.save()
            return self._json(STORE.state())
        return self._json({"error": "unknown"}, 404)


PAGE = r"""<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Screening workbench</title>
<style>
:root{--bg:#fff;--fg:#2b2b3a;--muted:#5a5a66;--line:#e6e6ea;--accent:#52489c;--inc:#2f7d4f;--exc:#b23b3b;--uns:#9a6b00;--card:#fafafc}
@media (prefers-color-scheme:dark){:root{--bg:#17171c;--fg:#e8e8ee;--muted:#a3a3ad;--line:#2c2c35;--accent:#9b90e6;--inc:#5cc08a;--exc:#e57373;--uns:#e0b44c;--card:#1e1e25}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 Inter,"Helvetica Neue",Arial,sans-serif}
header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:.6rem 1rem;z-index:3}
.row{display:flex;gap:1rem;align-items:center;flex-wrap:wrap}.muted{color:var(--muted)}.small{font-size:.85rem}
h1{font-size:1rem;margin:0;color:var(--accent)}
.bar{position:relative;height:8px;background:var(--line);border-radius:4px;flex:1;min-width:160px;overflow:hidden}
.bar i{position:absolute;left:0;top:0;bottom:0;background:var(--accent)}.bar b{position:absolute;top:-2px;bottom:-2px;width:2px;background:var(--fg);opacity:.5}
.chk{font-variant-numeric:tabular-nums}.ok{color:var(--inc)}
main{max-width:900px;margin:0 auto;padding:1.2rem 1rem 12rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:1.2rem 1.4rem}
.title{font-size:1.25rem;font-weight:650;line-height:1.35;margin:0 0 .4rem}
.meta{font-size:.88rem;color:var(--muted)}.meta a{color:var(--accent)}
.abstract{margin:.9rem 0 0;white-space:pre-wrap}
.sug{margin-top:.8rem;font-size:.88rem;border-left:3px solid var(--accent);padding:.3rem .7rem;color:var(--muted)}
.actions{position:fixed;left:0;right:0;bottom:0;background:var(--bg);border-top:1px solid var(--line);padding:.6rem 1rem;box-shadow:0 -6px 16px rgba(0,0,0,.06)}
.actions .row{max-width:900px;margin:0 auto;gap:.45rem}
button{font:inherit;font-size:.88rem;border-radius:7px;border:1px solid var(--line);background:var(--card);color:var(--fg);padding:.35rem .65rem;cursor:pointer}
button kbd{font-family:ui-monospace,Menlo,monospace;font-size:.78rem;opacity:.7;margin-right:.3rem}
button.inc{border-color:var(--inc);color:var(--inc);font-weight:600}button.uns{border-color:var(--uns);color:var(--uns)}
button.exc{border-color:color-mix(in srgb,var(--exc) 50%,var(--line))}button.exc:hover{border-color:var(--exc)}
#note{flex:1;min-width:180px;font:inherit;font-size:.88rem;padding:.35rem .5rem;border:1px solid var(--line);border-radius:7px;background:var(--bg);color:var(--fg)}
.flash{position:fixed;top:4.2rem;right:1rem;padding:.4rem .8rem;border-radius:7px;color:#fff;font-weight:600;opacity:0;transition:opacity .2s}
.err{background:#b23b3b;color:#fff;padding:.4rem .8rem;border-radius:6px;margin-top:.4rem}
.done{text-align:center;padding:4rem 1rem}
</style></head><body>
<header><div class=row><h1 id=h1>Screening</h1><div class=bar title="screened / records; mark = minimum share"><i id=bar></i><b id=floor></b></div>
<span class="chk small" id=checks></span></div>
<div class="row small muted" id=sub></div><div id=err></div></header>
<main><div id=card></div></main>
<div class=actions><div class=row id=btns></div></div>
<div class=flash id=flash></div>
<script>
let S=null, Q=[], cur=null, busy=false;
const $=id=>document.getElementById(id);
const el=(t,a={},...k)=>{const e=document.createElement(t);for(const[x,y] of Object.entries(a)){if(x==='text')e.textContent=y;else if(x==='html')e.innerHTML=y;else if(x.startsWith('on'))e.addEventListener(x.slice(2),y);else e.setAttribute(x,y)}for(const c of k)if(c)e.append(c);return e};
async function api(p,b){const r=await fetch(p,b?{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)}:{});return r.json()}
function flash(t,c){const f=$('flash');f.textContent=t;f.style.background=c;f.style.opacity=1;setTimeout(()=>f.style.opacity=0,500)}
function renderState(){
  const st=S.stopping, mode=S.check?'second screener (blind check)':(S.stage==='full_text'?'full text':'title / abstract');
  $('h1').textContent='Screening · '+mode+' · '+S.by;
  if(st){const f=st.records?st.screened/st.records:0;$('bar').style.width=(100*f).toFixed(1)+'%';$('floor').style.left=(100*st.stop.min_screened_fraction)+'%';
    const m=ok=>ok?'<span class=ok>✓</span>':'·';
    $('checks').innerHTML=`${m(st.checks.screened)} ${st.screened.toLocaleString()} / ${st.records.toLocaleString()} screened &nbsp; ${m(st.checks.consecutive)} ${st.consecutiveExclusions} / ${st.stop.consecutive_exclusions} excl. in a row &nbsp; ${m(st.checks.validation)} validation ${st.validationScreened}/${st.validation}`+(st.met?' &nbsp;<b class=ok>stopping rule met — run screen.py stop</b>':'');}
  else{$('bar').style.width='0';$('checks').textContent=S.left+' to assess';}
  const s=S.session, r=S.rank||{};
  $('sub').textContent=`this session: ${s.include||0} included · ${s.exclude||0} excluded · ${s.unsure||0} unsure · ${S.left.toLocaleString()} left`+
    (S.stage==='title_abstract'&&!S.check?` · ranking: ${S.ranking?'updating…':`learned from ${r.relevant||0} relevant / ${r.excluded||0} excluded, next update in ${Math.max(0,S.rerank-S.sinceRank)}`}`:'')+(S.saved?' · saved':' · saving…');
  $('err').innerHTML='';if(S.error)$('err').append(el('div',{class:'err',text:S.error}));
}
function renderButtons(){
  const b=$('btns');b.innerHTML='';
  b.append(el('button',{class:'inc',onclick:()=>decide('include')},el('kbd',{text:'i'}),'Include'));
  b.append(el('button',{class:'uns',onclick:()=>decide('unsure')},el('kbd',{text:'u'}),'Unsure'));
  S.reasons.forEach(([k,l],n)=>{const key=k==='other'?'0':(n<9?String(n+1):'');b.append(el('button',{class:'exc',title:'Exclude: '+l,onclick:()=>decide('exclude',k)},key?el('kbd',{text:key}):'',l))});
  b.append(el('input',{id:'note',placeholder:'note (n) — needed for Other / duplicate'}));
  b.append(el('button',{onclick:undo,title:'undo the last decision'},el('kbd',{text:'z'}),'Undo'));
}
function renderCard(){
  const box=$('card');box.innerHTML='';
  if(!cur){box.append(el('div',{class:'done'},el('h2',{text:'Nothing left in this queue.'}),el('p',{class:'muted',text:S.stopping&&S.stopping.met?'The stopping rule is met: close the pass with screen.py stop.':'Restart the app later, or switch stage.'})));return}
  const c=cur, meta=el('div',{class:'meta'});
  meta.append([c.year,c.journal,c.authors].filter(Boolean).join(' · '));
  if(c.doi){meta.append(' · ',el('a',{href:'https://doi.org/'+c.doi,target:'_blank',rel:'noopener',text:'doi'}))}
  if(c.pmid){meta.append(' · ',el('a',{href:'https://pubmed.ncbi.nlm.nih.gov/'+c.pmid,target:'_blank',rel:'noopener',text:'PubMed'}))}
  if(c.pdf){meta.append(' · ',el('a',{href:c.pdf,target:'_blank',text:'PDF'}))}
  meta.append(el('span',{class:'small',text:'  ['+c.id+(c.key?' '+c.key:'')+(c.sources.length?' · '+c.sources.join(', '):'')+(c.previous?' · title/abstract: '+c.previous:'')+']'}));
  const card=el('div',{class:'card'},el('p',{class:'title',text:c.title}),meta,el('div',{class:'abstract',text:c.abstract||'(no abstract)'}));
  if(c.suggestion){card.append(el('div',{class:'sug',text:`Model suggests ${c.suggestion.decision}${c.suggestion.reason&&c.suggestion.reason!=='none'?' ('+c.suggestion.reason+')':''} — ${c.suggestion.rationale||''} [suggestion, not a decision]`}))}
  box.append(card);window.scrollTo(0,0);
}
async function fill(){if(Q.length<4){const skip=[cur&&cur.id,...Q.map(x=>x.id)].filter(Boolean).join(',');const r=await api('/api/next?n=10&skip='+encodeURIComponent(skip));for(const x of r.cards)if(!Q.find(y=>y.id===x.id)&&(!cur||cur.id!==x.id))Q.push(x)}}
async function advance(){await fill();cur=Q.shift()||null;renderCard();fill()}
async function decide(d,reason){
  if(!cur||busy)return;const note=$('note').value.trim();
  if(d==='exclude'&&(reason==='other'||reason==='duplicate_report')&&!note){$('note').focus();flash('add a note first','#9a6b00');return}
  busy=true;const r=await api('/api/decide',{id:cur.id,decision:d,reason,note});busy=false;
  if(r.error){flash(r.error,'#b23b3b');return}
  flash(d==='include'?'included':d==='unsure'?'unsure':'excluded',d==='include'?'#2f7d4f':d==='unsure'?'#9a6b00':'#b23b3b');
  $('note').value='';S=r.state;renderState();advance();
}
async function undo(){const r=await api('/api/undo',{});if(r.error){flash(r.error,'#b23b3b');return}if(cur)Q.unshift(cur);cur=r.card;S=r.state;renderState();renderCard();flash('undone','#52489c')}
document.addEventListener('keydown',e=>{
  if(e.target.id==='note'){if(e.key==='Escape'||e.key==='Enter'){e.target.blur();e.preventDefault()}return}
  if(e.metaKey||e.ctrlKey||e.altKey)return;
  if(e.key==='i')decide('include');else if(e.key==='u')decide('unsure');else if(e.key==='z')undo();
  else if(e.key==='n'){$('note').focus();e.preventDefault()}
  else if(/^[1-9]$/.test(e.key)){const r=S.reasons[Number(e.key)-1];if(r&&r[0]!=='other')decide('exclude',r[0])}
  else if(e.key==='0'){if($('note').value.trim())decide('exclude','other');else{$('note').focus();flash('Other: write the note, then press 0','#9a6b00')}}
});
function pad(){const h=document.querySelector('.actions').offsetHeight;document.querySelector('main').style.paddingBottom=(h+32)+'px'}
new ResizeObserver(pad).observe(document.querySelector('.actions'));window.addEventListener('resize',pad);
setInterval(async()=>{S=await api('/api/state');renderState()},4000);
(async()=>{S=await api('/api/state');renderState();renderButtons();pad();await advance()})();
</script></body></html>"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--by", required=True, help="the person screening")
    ap.add_argument("--stage", default="ta", choices=sorted(STAGE), help="ta (title/abstract, default) or ft (full text)")
    ap.add_argument("--check", action="store_true", help="second screener: a blind sample of already-decided records")
    ap.add_argument("--sample", type=float, default=0.2, help="with --check: fraction (0.2) or number (50)")
    ap.add_argument("--seed", type=int, default=1, help="with --check: random seed (report it)")
    ap.add_argument("--rerank", type=int, default=50, help="re-rank after this many decisions (title/abstract)")
    ap.add_argument("--port", type=int, default=8766)
    ap.add_argument("--no-browser", action="store_true")
    args = ap.parse_args(argv)
    global STORE
    STORE = Store(args.by, STAGE[args.stage], args.check, args.sample, args.seed, args.rerank)
    threading.Thread(target=STORE.saver, daemon=True).start()
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}/"
    print(f"screening workbench at {url}  (Ctrl-C to save and quit)", flush=True)
    if not args.no_browser:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        STORE.save()
        if not STORE.error:
            STORE.log_session()
        print("saved." if not STORE.error else STORE.error)
    return 0


if __name__ == "__main__":
    sys.exit(main())
