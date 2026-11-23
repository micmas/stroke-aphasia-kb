"""Exact character geometry must retain unusual PDF symbols without guessing."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from annotate_paper import _exact_character_rects


class Page:
    def __init__(self, lines):
        self.lines = lines

    def get_text(self, mode):
        assert mode == 'rawdict'
        return {'blocks': [{'lines': [
            {'spans': [{'chars': [{'c': c, 'bbox': (x, y*10, x+1, y*10+5)}
                                  for x, c in enumerate(line)]}]}
            for y, line in enumerate(self.lines)
        ]}]}


def test_exact_symbols_and_wrapped_quote():
    page = Page(['Task \x05', 'Intelligibility interaction'])
    rects, label = _exact_character_rects(page, 'Task \x05\nIntelligibility interaction')
    assert len(rects) == 2
    assert 'full quote' in label
    assert not _exact_character_rects(page, 'Task + Intelligibility interaction')[0]
    assert not _exact_character_rects(page, 'Task \x05 Intelligibility interaction invented')[0]


def test_repeated_quote_is_not_assigned_arbitrarily():
    assert not _exact_character_rects(Page(['same quote', 'same quote']), 'same quote')[0]
