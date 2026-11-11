import json
import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import dual_extract as d


def fake_run(pdf,citation,out,model):
    out.mkdir();(out/'meta.json').write_text(json.dumps({'model':model,'citation':citation,
        'pdf_sha256':'frozen','prompt_sha256':'same'}))
    (out/'raw.json').write_text(json.dumps({'analyses':[{'model':model}]}))
    (out/'source-units.json').write_text('{"P1-S1":{"page":1,"text":"source"}}')
    return 1  # Evidence warnings must stay available to the reviewer.


def test_pair_uses_same_source_and_keeps_both_answers(tmp_path,monkeypatch):
    calls=[]
    def tracked(*args): calls.append(args);return fake_run(*args)
    monkeypatch.setattr(d,'run',tracked)
    pdf=tmp_path/'source.pdf';pdf.write_bytes(b'source')
    out=tmp_path/'pair'
    assert d.run_pair(pdf,'@Example2020',out,['one','two'])==0
    assert [c[0] for c in calls]==[pdf,pdf]
    packet=json.loads((out/'review/packet.json').read_text())
    assert not packet['approved']
    assert [x['extraction']['analyses'][0]['model'] for x in packet['arms']]==['one','two']
    with pytest.raises(FileExistsError):d.run_pair(pdf,'@Example2020',out,['one','two'])


def test_mismatched_papers_refuse_review_packet(tmp_path):
    a,b=tmp_path/'a',tmp_path/'b'
    fake_run(None,'@One2020',a,'one');fake_run(None,'@Two2020',b,'two')
    with pytest.raises(ValueError,match='citation'):d.prepare_review(a,b,tmp_path/'review')
    assert not (tmp_path/'review').exists()
