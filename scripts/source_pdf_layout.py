"""Locate original PDF prose while auditing repeated margin furniture.

Only unambiguous leading/trailing repeated headers or page numbers may be
excluded from the image anchor. Original source text is never rewritten.
Captions, interior fragments and ambiguous body matches are not repaired.
"""
from __future__ import annotations
import re
import unicodedata

import pymupdf

VERSION = 'source-pdf-layout-v1'
MARGIN_TOP = 0.07      # fraction of page height: a furniture line must end above this
MARGIN_BOTTOM = 0.93   # ... or start below this
MIN_PAGES = 3          # a furniture pattern must repeat on at least this many pages
POSITION_TOLERANCE = 3.0  # points, for grouping a repeated line by its top-left corner


def norm(text: str) -> str:
    text = unicodedata.normalize('NFKC', text).replace('­', '')
    return ' '.join(text.split())


def pattern(text: str) -> str:
    return re.sub(r'\d+', '#', norm(text))


def page_lines(page):
    out = []
    for block in page.get_text('dict')['blocks']:
        if block.get('type') != 0:
            continue
        for line in block['lines']:
            text = ''.join(span['text'] for span in line['spans'])
            if text.strip():
                out.append({'text': text, 'bbox': tuple(line['bbox']), 'block': block['number'],
                            'size': round(line['spans'][0]['size'], 1)})
    return out


def furniture(doc):
    """Return {page_index: [furniture lines]} for patterns repeated in the margins."""
    candidates = {}
    for index, page in enumerate(doc):
        height = page.rect.height
        for line in page_lines(page):
            x0, y0, x1, y1 = line['bbox']
            if y1 <= MARGIN_TOP * height or y0 >= MARGIN_BOTTOM * height:
                key = (pattern(line['text']), round(x0 / POSITION_TOLERANCE), round(y0 / POSITION_TOLERANCE))
                candidates.setdefault(key, []).append((index, line))
    result = {}
    for key, hits in candidates.items():
        if len({index for index, _ in hits}) >= MIN_PAGES:
            for index, line in hits:
                result.setdefault(index, []).append({**line, 'pattern': key[0]})
    return result


def inside(box, outer, pad=1.0):
    return (box[0] >= outer[0] - pad and box[1] >= outer[1] - pad and
            box[2] <= outer[2] + pad and box[3] <= outer[3] + pad)


def explained_by_furniture(fragment, page, page_furniture, lines):
    """A whole furniture line, or a whole-token prefix/suffix of one, found nowhere else.

    Whole line: no non-furniture line on the page has the same text (so a page number
    '3' is excluded only as a separate line, never a '3' inside body text).
    Partial line: every occurrence of the fragment on the page lies inside furniture.
    """
    frag = norm(fragment)
    if not frag:
        return None
    furniture_boxes = [f['bbox'] for f in page_furniture]
    for line in page_furniture:
        full = norm(line['text'])
        tokens, ftokens = full.split(), frag.split()
        if full == frag:
            twins = [l for l in lines if norm(l['text']) == frag]
            if all(any(inside(l['bbox'], box) for box in furniture_boxes) for l in twins):
                return line
            continue
        if not (tokens[:len(ftokens)] == ftokens or tokens[-len(ftokens):] == ftokens):
            continue
        hits = page.search_for(frag)
        if hits and all(any(inside(tuple(h), box) for box in furniture_boxes) for h in hits):
            return line
    return None


def anchor(text, page, page_furniture):
    """Split the original text into excluded leading/trailing furniture and the anchor slice."""
    lines = page_lines(page)
    spans, position = [], 0
    for raw in text.split('\n'):
        spans.append((position, position + len(raw), raw))
        position += len(raw) + 1
    keep = [i for i, (_, _, raw) in enumerate(spans) if raw.strip()]
    excluded = []
    while keep:
        line = explained_by_furniture(spans[keep[0]][2], page, page_furniture, lines)
        if not line:
            break
        excluded.append({'where': 'leading', 'text': spans[keep[0]][2], 'furniture_line': line['text'],
                         'bbox': [round(v, 1) for v in line['bbox']], 'rule': 'repeated margin line'})
        keep.pop(0)
    while keep:
        line = explained_by_furniture(spans[keep[-1]][2], page, page_furniture, lines)
        if not line:
            break
        excluded.append({'where': 'trailing', 'text': spans[keep[-1]][2], 'furniture_line': line['text'],
                         'bbox': [round(v, 1) for v in line['bbox']], 'rule': 'repeated margin line'})
        keep.pop()
    if not keep:
        return None, excluded
    start, end = spans[keep[0]][0], spans[keep[-1]][1]
    return text[start:end], excluded


def locate(doc, page_number, text, furniture_by_page=None):
    """Return an audit record; status 'located' (with clip) or 'held' (with reason)."""
    furniture_by_page = furniture(doc) if furniture_by_page is None else furniture_by_page
    page = doc[page_number - 1]
    page_furniture = furniture_by_page.get(page_number - 1, [])
    record = {'version': VERSION, 'page': page_number, 'original_text': text, 'anchor_text': None,
              'excluded_fragments': [], 'boxes': [], 'clip': None, 'status': 'held', 'reason': None}
    anchor_text, excluded = anchor(text, page, page_furniture)
    record['excluded_fragments'] = excluded
    if anchor_text is None:
        record['reason'] = 'Passage consists only of page furniture'
        return record
    record['anchor_text'] = anchor_text
    # Same search as prepare(): exact slice first, then whitespace-normalised.
    boxes = page.search_for(anchor_text) or page.search_for(' '.join(anchor_text.split()))
    boxes = [tuple(b) for b in boxes]
    if not boxes:
        record['reason'] = 'Anchor text not located on its page'
        return record
    record['boxes'] = [list(b) for b in boxes]
    clip = pymupdf.Rect(boxes[0])
    for b in boxes[1:]:
        clip |= pymupdf.Rect(b)
    record['crop_area_fraction'] = round(clip.get_area() / page.rect.get_area(), 3)
    clip = (clip + (-3, -3, 3, 3)) & page.rect
    record.update(status='located', clip=list(clip),
                  reason='Located after excluding repeated page furniture' if excluded else 'Located without exclusions')
    return record


