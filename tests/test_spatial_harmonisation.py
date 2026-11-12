import copy
import json
from pathlib import Path
import sys
import numpy as np
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from spatial_harmonisation import Atlas, crosswalk, map_evidence, point_lookup, report


def atlas(data, name='coarse', affine=None, **overrides):
    metadata=dict(atlas_id=name,version='synthetic-v1',space='synthetic:shared-RAS',
                  template_reference='synthetic unit-test grid',source='generated fixture',
                  licence='CC0',representation='deterministic_labels',units='mm',world_axes='RAS+',
                  image_file_sha256='synthetic-'+name)
    metadata.update(overrides)
    return Atlas(np.array(data),np.eye(4) if affine is None else affine,metadata,
                 {int(i):f'{name} ROI {i}' for i in np.unique(data) if i})


def test_one_roi_to_five_does_not_claim_five_equivalent_regions():
    a=atlas(np.ones((10,2,2)))
    b=atlas(np.repeat(np.arange(1,6),2)[:,None,None]*np.ones((1,2,2)),name='fine')
    m=crosswalk(a,b)
    assert len(m['edges'])==5
    for e in m['edges']:
        assert e['source_fraction']==pytest.approx(.2)
        assert e['target_fraction']==1
        assert e['dice']==pytest.approx(1/3)
    assert sum(e['source_fraction'] for e in m['edges'])==pytest.approx(1)
    r=dict(evidence_id='study-analysis-1',citation='@Example',source_location='Table 2',
           kind='atlas_roi',atlas=a.identity(),roi_id=1,statistics={'beta':2.1,'p':.02})
    mapped=map_evidence([r],m)
    assert len(mapped['findings'])==1
    assert len(mapped['findings'][0]['spatial_candidates'])==5
    assert mapped['findings'][0]['original']==r
    assert mapped['findings'][0]['cohort_check']=='required'
    assert '20.00 | 100.00' in report(m)


def test_background_is_not_renormalised_and_volume_uses_affine():
    a=atlas(np.ones((2,2,2)),affine=np.diag([2,3,4,1]))
    data=np.zeros((2,2,2));data[0]=1
    b=atlas(data,'partial',affine=a.affine)
    m=crosswalk(a,b);e=m['edges'][0]
    assert e['overlap_mm3']==pytest.approx(96)
    assert e['source_fraction']==.5 and e['target_fraction']==1
    assert m['source_coverage'][0]['unmapped_fraction']==.5
    assert crosswalk(a,atlas(np.zeros((2,2,2)),'empty',affine=a.affine))['source_coverage'][0]['unmapped_fraction']==1


def test_reversing_crosswalk_swaps_directional_fractions():
    a=atlas(np.ones((2,2,2)));b=atlas(np.array([[[1,1],[1,1]],[[2,2],[2,2]]]),'fine')
    forward=crosswalk(a,b);reverse=crosswalk(b,a)
    for x,y in zip(forward['edges'],reverse['edges']):
        assert x['source_fraction']==y['target_fraction']
        assert x['target_fraction']==y['source_fraction']
        assert x['dice']==y['dice']


def test_identical_names_do_not_override_geometry_or_space():
    a=atlas(np.ones((2,2,2)))
    with pytest.raises(ValueError,match='template spaces'):crosswalk(a,atlas(a.data,space='synthetic:other'))
    shifted=np.eye(4);shifted[0,3]=1
    with pytest.raises(ValueError,match='grids'):crosswalk(a,atlas(a.data,affine=shifted))
    with pytest.raises(ValueError,match='grids'):crosswalk(a,atlas(np.ones((3,2,2))))
    with pytest.raises(ValueError,match='generic'):atlas(a.data,space='MNI')


@pytest.mark.parametrize('data',[np.full((2,2,2),.5),np.full((2,2,2),np.nan),np.full((2,2,2),-1),np.ones((2,2,2,2))])
def test_probabilities_and_invalid_label_arrays_are_refused(data):
    with pytest.raises(ValueError):atlas(data)


def test_coordinate_uses_affine_and_preserves_peak_scope():
    affine=np.diag([-2,2,2,1]);affine[0,3]=10
    a=atlas(np.ones((2,2,2)),affine=affine)
    r=point_lookup(a,[8,0,0],a.metadata['space'])
    assert r['voxel']==[1,0,0] and r['evidence_kind']=='reported_peak'
    assert point_lookup(a,[30,0,0],a.metadata['space'])['status']=='outside_field_of_view'
    with pytest.raises(ValueError):point_lookup(a,[8,0,0],'MNI')


def test_labels_alone_unknown_versions_and_modified_crosswalk_remain_unresolved():
    a=atlas(np.ones((2,2,2)));m=crosswalk(a,a)
    r=dict(evidence_id='1',citation='@Example',source_location='p3',kind='label_only',label='IFG')
    assert map_evidence([r],m)['findings'][0]['status']=='unresolved'
    r.update(kind='atlas_roi',roi_id=1,atlas={**a.identity(),'version':'unknown'})
    assert map_evidence([r],m)['findings'][0]['status']=='unresolved'
    with pytest.raises(ValueError,match='Duplicate'):map_evidence([r,r],m)
    damaged=copy.deepcopy(m);damaged['edges'][0]['source_fraction']=.1
    with pytest.raises(ValueError,match='integrity'):map_evidence([r],damaged)


def test_nifti_loader_provenance_and_conflicting_transforms(tmp_path):
    nib=pytest.importorskip('nibabel')
    from spatial_harmonisation import load_atlas
    image=nib.Nifti1Image(np.ones((2,2,2),dtype=np.int16),np.eye(4));image.header.set_xyzt_units('mm')
    image.set_qform(np.eye(4),1);image.set_sform(np.eye(4),1);nib.save(image,tmp_path/'atlas.nii.gz')
    spec={**atlas(np.ones((2,2,2))).metadata,'image':'atlas.nii.gz','labels':{'1':'region'}}
    p=tmp_path/'atlas.json';p.write_text(json.dumps(spec));loaded=load_atlas(p)
    assert len(loaded.identity()['image_file_sha256'])==64
    shift=np.eye(4);shift[0,3]=10;image.set_qform(shift,1);nib.save(image,tmp_path/'atlas.nii.gz')
    with pytest.raises(ValueError,match='qform/sform'):load_atlas(p)


def test_crossing_partitions_are_many_to_many():
    source=np.ones((4,4,2));source[2:]=2
    target=np.ones((4,4,2));target[:,2:]=2
    m=crosswalk(atlas(source),atlas(target,'crossing'))
    assert len(m['edges'])==4
    assert all(e['source_fraction']==.5 and e['target_fraction']==.5 for e in m['edges'])
    assert all(c['unmapped_fraction']==0 for c in m['source_coverage']+m['target_coverage'])
