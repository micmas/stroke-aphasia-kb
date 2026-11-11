import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from prepare_dual_batch import prepare


def test_all_statuses_and_doi_aliases_with_missing_sources(tmp_path):
    (tmp_path/'papers').mkdir(); (tmp_path/'screening').mkdir()
    (tmp_path/'citations.md').write_text('## @A2020 [extracted]\ndoi:10.1234/a\n## @B2021 [seed]\ndoi:10.1234/b\n## @C2022 [cited]\n## @D2023 [refused]\n')
    (tmp_path/'screening/licences.yaml').write_text('papers: {}\n')
    (tmp_path/'screening/candidates.yaml').write_text('candidates:\n- doi: 10.1234/b\n  pdf_file: C002_B2021.pdf\n')
    for name in ['A2020.pdf','C002_B2021.pdf','D2023.pdf','A2020_annotated.pdf']:
        (tmp_path/'papers'/name).write_bytes(b'pdf')
    result = prepare(tmp_path, tmp_path/'manifest.json')
    assert [p['key'] for p in result['papers']] == ['A2020','B2021']
    assert [p['key'] for p in result['pending']] == ['C2022','D2023']
    assert not result['unregistered_pdf_stems_requiring_identification']
    assert result['papers'][0]['licence_evidence'] == {'category':'unknown'}
    with pytest.raises(ValueError, match='frozen'):
        prepare(tmp_path, tmp_path/'manifest.json')
