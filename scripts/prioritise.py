#!/usr/bin/env python3
"""
prioritise.py — prioritised (active-learning) title/abstract screening for the
screening register (docs/SCREENING.md §4.1). Pure Python, no dependencies.

The model is the one ASReview used as its default for years: TF-IDF features
with a multinomial Naive Bayes classifier. It is retrained on every call from
what is known at that moment:

* positives — the *prior* half of the benchmark (legacy includes, split by a
  seeded hash so the split is reproducible and recorded) plus every candidate a
  person has included;
* negatives — every candidate a person has excluded; while there are fewer
  than ``MIN_NEGATIVES`` of those, a seeded random sample of unscreened records
  stands in for them (relevant records are rare, so an unscreened record is
  very probably irrelevant — the usual cold-start heuristic).

The other half of the benchmark is the *validation* set: the model never sees
it as positive, so how early those papers surface estimates how well the
ordering finds relevant records — one of the three parts of the stopping rule.
Nothing here decides anything: the ranking only orders the screening sheet.
"""
from __future__ import annotations

import collections
import hashlib
import math
import random
import re

MIN_NEGATIVES = 50
PSEUDO_NEGATIVES = 1000

_WORD = re.compile(r"[a-z][a-z0-9\-]{2,}")
_STOP = set("""the and for with from that this were was are have has had not but all any can our their which these
those into than then them they its also been being between both each more most other some such only over after
before under while where when who whom whose using used use based study studies patients patient results result
methods method conclusion conclusions background objective objectives aim aims however whether among within across
here there one two three may might could would should did does doing per via vs versus""".split())


def tokens(text: str) -> list[str]:
    """Lower-cased words of three letters or more, minus stop words, plus word bigrams."""
    w = [t for t in _WORD.findall((text or "").lower()) if t not in _STOP]
    return w + [f"{a}_{b}" for a, b in zip(w, w[1:])]


def is_prior(cid: str, seed, fraction: float) -> bool:
    """Seeded, reproducible split of the benchmark: True → prior knowledge, False → validation."""
    h = int(hashlib.sha256(f"{seed}:{cid}".encode()).hexdigest()[:12], 16) / float(16 ** 12)
    return h < fraction


def _features(texts: dict[str, str]) -> tuple[dict[str, dict[str, float]], dict[str, float]]:
    """TF-IDF (sublinear tf) per document, and the idf table."""
    counts = {cid: collections.Counter(tokens(t)) for cid, t in texts.items()}
    df = collections.Counter()
    for c in counts.values():
        df.update(c.keys())
    n = max(1, len(counts))
    idf = {t: math.log((1 + n) / (1 + d)) + 1.0 for t, d in df.items() if d >= 2}
    feats = {cid: {t: (1.0 + math.log(k)) * idf[t] for t, k in c.items() if t in idf} for cid, c in counts.items()}
    return feats, idf


def rank(texts: dict[str, str], positives: set[str], negatives: set[str], pool: list[str], seed=1) -> list[tuple[str, float]]:
    """Score every id in ``pool`` (most likely relevant first).

    ``texts``: id → title + abstract for every candidate the model may use.
    ``positives`` / ``negatives``: ids labelled so far (priors included)."""
    feats, _ = _features(texts)
    pos = [i for i in positives if i in feats]
    neg = [i for i in negatives if i in feats and i not in positives]
    if len(neg) < MIN_NEGATIVES:
        unl = sorted(i for i in feats if i not in positives and i not in negatives)
        rnd = random.Random(seed)
        neg = neg + rnd.sample(unl, min(PSEUDO_NEGATIVES, len(unl)))
    if not pos:                                     # nothing to learn from yet: keep the given order
        return [(i, 0.0) for i in pool]
    vocab = set()
    for i in pos + neg:
        vocab.update(feats[i])
    alpha = 0.1

    def class_logp(ids):
        tot = collections.Counter()
        for i in ids:
            for t, w in feats[i].items():
                tot[t] += w
        denom = sum(tot.values()) + alpha * len(vocab)
        return {t: math.log((tot.get(t, 0.0) + alpha) / denom) for t in vocab}

    lp_pos, lp_neg = class_logp(pos), class_logp(neg)
    weight = {t: lp_pos[t] - lp_neg[t] for t in vocab}
    prior = math.log(len(pos) / len(neg)) if neg else 0.0
    scored = []
    for i in pool:
        f = feats.get(i) or {}
        norm = math.sqrt(sum(v * v for v in f.values())) or 1.0
        scored.append((i, prior + sum(w * weight.get(t, 0.0) for t, w in f.items()) / norm))
    scored.sort(key=lambda x: (-x[1], x[0]))
    return scored
