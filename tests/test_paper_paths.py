import hashlib
import json
import sys
from pathlib import Path

import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from paper_paths import citation_stem, resolve_paper, paper_filename
from batch_dual_extract import load_manifest


def test_prefix_preserves_citation_identity_and_rejects_ambiguous_sources(tmp_path):
    p = tmp_path / 'C0042_Smith2020.pdf'
    p.write_bytes(b'%PDF source')
    assert citation_stem(p) == 'Smith2020'
    assert citation_stem('C0042_Smith2020_annotated.pdf') == 'Smith2020'
    assert resolve_paper(tmp_path, 'Smith2020.pdf') == p
    assert paper_filename({'id': 'C0042', 'key': '@Smith2020'}) == p.name
    (tmp_path / 'C0043_Smith2020.pdf').write_bytes(b'other')
    with pytest.raises(ValueError, match='Ambiguous'):
        resolve_paper(tmp_path, 'Smith2020.pdf')


def test_old_manifest_resolves_renamed_pdf_but_still_checks_bytes(tmp_path):
    p = tmp_path / 'C0042_Smith2020.pdf'
    p.write_bytes(b'%PDF unchanged')
    row = dict(key='Smith2020', citation='@Smith2020', licence_evidence='unknown',
               pdf='Smith2020.pdf', pdf_sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    manifest = tmp_path / 'manifest.json'
    manifest.write_text(json.dumps(dict(source_scope='main_paper_only', papers=[row])))
    assert load_manifest(manifest)['papers'][0]['pdf'] == str(p)
    p.write_bytes(b'%PDF modified')
    with pytest.raises(ValueError, match='checksum mismatch'):
        load_manifest(manifest)


def test_rename_alias_cannot_escape_papers(tmp_path):
    (tmp_path / '.filename-aliases.json').write_text(json.dumps({'old.pdf': '../outside.pdf'}))
    assert resolve_paper(tmp_path, 'old.pdf') == tmp_path / 'old.pdf'
