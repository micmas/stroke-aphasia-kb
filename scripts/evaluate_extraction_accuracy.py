"""Read-only schema and page-evidence report for a frozen extraction run.

This does not score scientific claim accuracy: pair the output with an
independent source review and a predeclared coverage rubric. Zero findings
is an incomplete run, never perfect precision.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from aphasia_kb import parse_markdown, _validate_v2_entry
from extract import _extract_pdf_text
from extraction_evidence import audit_finding
from quote_check import PaperText, grade_quote


def evaluate(draft_dir: Path, pdf: Path) -> dict:
    page_text, page_count = _extract_pdf_text(pdf)
    paper = PaperText.from_text(re.sub(r"^=== PAGE \d+ ===\s*$", "", page_text, flags=re.M))
    report = {'pdf': pdf.name, 'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
              'pages': page_count, 'drafts': [], 'findings': 0, 'passages': 0,
              'whole_paper_exact': 0, 'declared_page_exact': 0, 'page_issues': 0, 'schema_issues': 0}
    for path in sorted(draft_dir.rglob('*.md')):
        parse_error = None
        try:
            fm, _ = parse_markdown(path)
        except Exception as exc:
            fm, parse_error = None, str(exc)
        row = {'path': str(path.relative_to(draft_dir)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'findings': []}
        problems = []
        if not isinstance(fm, dict):
            problems.append(parse_error or 'No frontmatter mapping')
        else:
            _validate_v2_entry(fm, str(path), problems)
            for finding in fm.get('findings') or []:
                if not isinstance(finding, dict):
                    continue
                issues = audit_finding(finding, page_text)
                passages = finding.get('source_passages') or []
                grades = [grade_quote(p['quote'], paper) if isinstance(p.get('quote'), str) else 'absent' for p in passages if isinstance(p, dict)]
                row['findings'].append({'id': finding.get('id'), 'claim': finding.get('claim'),
                                        'target': finding.get('target'), 'whole_paper_quote_grades': grades,
                                        'page_issues': issues})
                report['findings'] += 1
                report['passages'] += len(grades)
                report['whole_paper_exact'] += grades.count('exact')
                report['declared_page_exact'] += sum(
                    not audit_finding({'source_passages': [p]}, page_text)
                    for p in passages if isinstance(p, dict))
                report['page_issues'] += len(issues)
        row['schema_issues'] = problems
        report['schema_issues'] += len(problems)
        report['drafts'].append(row)
    report['complete_nonempty'] = report['findings'] > 0
    return report


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--draft-dir', type=Path, required=True)
    p.add_argument('--pdf', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    result = evaluate(args.draft_dir, args.pdf)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, default=str) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'drafts'}, indent=2))
    raise SystemExit(0 if result['complete_nonempty'] else 1)
