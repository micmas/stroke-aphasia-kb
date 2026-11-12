import json
import sys
from pathlib import Path
import pymupdf
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from source_limits import source_hold
import dual_extract
from prepare_dual_batch import prepare


def pdf(path, pages):
    with pymupdf.open() as doc:
        for _ in range(pages): doc.new_page()
        doc.save(path)


def test_limit_is_strictly_over_50_and_override_is_explicit(tmp_path):
    p=tmp_path/'source.pdf';pdf(p,50)
    assert source_hold(p) is None
    p.unlink();pdf(p,51)
    assert source_hold(p)['pdf_pages']==51
    assert source_hold(p,True) is None


def test_old_manifest_cannot_send_long_source_to_models(tmp_path,monkeypatch):
    p=tmp_path/'source.pdf';pdf(p,51)
    monkeypatch.setattr(dual_extract,'run',lambda *a,**k:pytest.fail('model must not start'))
    out=tmp_path/'run'
    assert dual_extract.run_pair(p,'@Long2026',out,['a','b'])==1
    assert json.loads((out/'status.json').read_text())['status']=='source_selection_required'
    assert not (out/'A').exists()


def test_preparation_retains_long_paper_as_pending(tmp_path):
    (tmp_path/'papers').mkdir();(tmp_path/'screening').mkdir()
    (tmp_path/'citations.md').write_text('## @Long2026 [seed]\n')
    (tmp_path/'screening/licences.yaml').write_text('papers: {}\n')
    pdf(tmp_path/'papers/Long2026.pdf',51)
    result=prepare(tmp_path,tmp_path/'manifest.json')
    assert result['papers']==[] and result['pending'][0]['status']=='source_selection_required'
    override=prepare(tmp_path,tmp_path/'override.json',allow_long_papers=True)
    assert override['papers'][0]['allow_long_paper'] is True
