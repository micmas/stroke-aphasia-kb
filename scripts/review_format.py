"""Constrained local-review response formats and non-correcting quote diagnostics."""
from quote_check import PaperText, grade_quote


def response_schema(units, citation, reconciliation=False):
    text = {'type': 'string'}
    def array(item): return {'type': 'array', 'items': item}
    def obj(properties):
        return {'type': 'object', 'properties': properties,
                'required': list(properties), 'additionalProperties': False}
    texts = array(text)
    evidence = array(obj({'source_id': {'type': 'string', 'enum': list(units)}, 'quote': text}))
    analysis = obj(dict(id=text, outcome=text, outcome_timing=text, method=text,
                        predictors=texts, selected_predictors=texts, covariates=texts,
                        result=text, estimates=array(obj(dict(term=text, statistic=text, value=text, p=text))),
                        evidence=evidence, uncertainties=texts))
    inventory = obj({'citation': {'type': 'string', 'enum': [citation]}, 'outcomes': texts,
                     'analyses': array(analysis), 'discrepancies': array(obj(dict(description=text, evidence=evidence))),
                     'coverage_notes': texts})
    if not reconciliation: return inventory
    return obj(dict(inventory=inventory,
                    decisions=array(obj({'arm': {'type': 'string', 'enum': ['A', 'B']},
                                         'analysis_id': text,
                                         'action': {'type': 'string', 'enum': ['retain', 'correct', 'reject']},
                                         'final_ids': texts, 'reason': text, 'evidence': evidence})),
                    coverage=array(obj({'source_id': {'type': 'string', 'enum': list(units)},
                                        'status': {'type': 'string', 'enum': ['covered', 'not_substantive', 'unresolved']},
                                        'final_ids': texts, 'reason': text})),
                    study_context=text, summary=text, unresolved=texts))


QUOTE_RULES = '''
QUOTE CONTRACT: quote fields are copied evidence, not explanations. Copy a short,
contiguous passage from the exact source_id shown in SOURCE. Do not add table
headings, join nonadjacent cells, insert labels/punctuation, expand abbreviations,
or silently repair signs, numbers or PDF glyphs. Put interpretation in result,
reason or summary instead. Use separate evidence items for separate spans. If
no faithful text span supports a claim, flag it as unresolved/needs visual review;
do not manufacture a quote. Short quotes must still retain necessary negations,
qualifiers and context. Source IDs are local unit identifiers, not page numbers.
Emit each object field exactly once. Never repeat a decisions field for another
arm: both arms belong in the single decisions array.
Keep outcomes internally consistent: every analysis.outcome must exactly match
an entry in outcomes. A predictor or covariate is not an outcome unless a separate
analysis actually models it as the dependent variable. Do not add analysis rows
merely to fill a mistaken outcome list; correct the list against the source.
'''


def quote_diagnostics(result, units):
    """Locate exact alternatives but never silently repair quotes or references."""
    papers = {sid: PaperText.from_text(unit['text']) for sid, unit in units.items()}
    findings = []
    def walk(value, path):
        if isinstance(value, dict):
            if 'quote' in value and 'source_id' in value:
                quote, sid = value['quote'], value['source_id']
                if not isinstance(quote, str) or not quote.strip():
                    grade, matches = 'invalid_quote', []
                else:
                    grade = grade_quote(quote, papers[sid]) if isinstance(sid, str) and sid in papers else 'unknown_source_id'
                    if grade == 'exact': return
                    matches = [key for key, paper in papers.items() if grade_quote(quote, paper) == 'exact']
                findings.append({'path': path, 'declared_source_id': sid, 'declared_grade': grade,
                                 'classification': 'exact_in_other_unit' if matches else 'not_exact_in_any_unit',
                                 'exact_candidate_source_ids': matches, 'automatic_correction': False})
            else:
                for key, child in value.items(): walk(child, f'{path}.{key}')
        elif isinstance(value, list):
            for i, child in enumerate(value): walk(child, f'{path}[{i}]')
    walk(result, '$')
    return findings
