"""Page-aware extraction diagnostics, not scientific approval.

Never repair scientific claims or relocate quotations automatically. A matching
passage elsewhere is evidence for a reviewer, not proof of the intended source.
"""
from __future__ import annotations

import re
from quote_check import PaperText, grade_quote


def audit_finding(finding: dict, page_text: str) -> list[str]:
    chunks = re.split(r'^=== PAGE (\d+) ===\s*$', page_text, flags=re.M)
    pages = {int(chunks[i]): PaperText.from_text(chunks[i + 1])
             for i in range(1, len(chunks) - 1, 2)}
    issues = []
    passages = finding.get('source_passages')
    if not isinstance(passages, list) or not passages:
        return ['verify evidence: no source passages supplied']
    for index, passage in enumerate(passages, 1):
        prefix = f'verify evidence passage {index}'
        if not isinstance(passage, dict):
            issues.append(f'{prefix}: expected a passage mapping')
            continue
        quote = passage.get('quote')
        if not isinstance(quote, str) or not quote.strip():
            issues.append(f'{prefix}: missing quotation')
            continue
        number = passage.get('page')
        if type(number) is not int or number not in pages:
            issues.append(f'{prefix}: invalid one-based PDF page {number!r}')
        grade = grade_quote(quote, pages[number]) if type(number) is int and number in pages else 'absent'
        if grade != 'exact':
            matches = [n for n, p in pages.items() if grade_quote(quote, p) == 'exact']
            detail = f'; exact text on PDF page(s) {matches}' if matches else '; no exact single-page match (may reflect extraction/layout or edited wording)'
            issues.append(f'{prefix}: {grade} on cited page {number!r}{detail}')
    return issues


def flag_evidence(finding: dict, page_text: str) -> list[str]:
    issues = audit_finding(finding, page_text)
    passages = finding.get('source_passages')
    if isinstance(passages, list) and not any(
            isinstance(p, dict) and p.get('supports') == 'claim'
            and isinstance(p.get('quote'), str) and p['quote'].strip()
            for p in passages):
        issues.append('verify evidence: no passage explicitly supports the claim')
    if issues:
        if finding.get('provenance') is None:
            finding['provenance'] = {}
        prov = finding['provenance']
        if not isinstance(prov, dict):
            raise ValueError('provenance must be a mapping')
        if prov.get('flags') is None:
            prov['flags'] = []
        flags = prov['flags']
        if not isinstance(flags, list):
            raise ValueError('provenance.flags must be a list')
        flags.extend(issue for issue in issues if issue not in flags)
        if prov.get('confidence') != 'low':
            prov['confidence'] = 'medium'
    return issues
