"""Experimental geometric crosswalks. Never distribute effects or approve findings."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import numpy as np

VERSION = 'spatial-crosswalk-v1'
LIMITATIONS = [
    'Geometric overlap is not functional equivalence or evidence of an effect in each target parcel.',
    'One original finding remains one evidence unit regardless of the number of mapped parcels.',
    'No effect sizes, p-values, sample sizes or study counts are apportioned by overlap.',
    'No registration, probabilistic-atlas conversion, clinical prediction or approval is performed.',
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


@dataclass
class Atlas:
    data: np.ndarray
    affine: np.ndarray
    metadata: dict
    labels: dict

    def __post_init__(self):
        self.data = np.asarray(self.data)
        self.affine = np.asarray(self.affine, dtype=float)
        for field in ('atlas_id', 'version', 'space', 'template_reference', 'source', 'licence'):
            if not isinstance(self.metadata.get(field), str) or not self.metadata[field].strip():
                raise ValueError(f'Explicit atlas metadata required: {field}')
        if self.metadata['space'].strip().lower() in ('mni', 'mni152', 'unknown', 'not_reported', 'talairach'):
            raise ValueError('Specify the exact template/coordinate convention; generic space names are insufficient')
        if self.metadata.get('representation') != 'deterministic_labels' or self.metadata.get('units') != 'mm':
            raise ValueError('Only deterministic integer labels in millimetres are supported')
        if self.metadata.get('world_axes') != 'RAS+':
            raise ValueError('Explicit RAS+ world coordinates required')
        if self.data.ndim != 3 or not all(self.data.shape) or not np.isfinite(self.data).all():
            raise ValueError('Expected a finite, nonempty 3D label image')
        if np.any(self.data < 0) or np.any(self.data != np.floor(self.data)):
            raise ValueError('Labels must be nonnegative integers; probabilities must not be rounded')
        if np.max(self.data) > np.iinfo(np.int32).max:
            raise ValueError('Label IDs exceed supported integer range')
        self.data = self.data.astype(np.int32)
        if (self.affine.shape != (4,4) or not np.isfinite(self.affine).all()
                or not np.allclose(self.affine[3], [0,0,0,1], atol=1e-9, rtol=0)
                or abs(np.linalg.det(self.affine[:3,:3])) < 1e-12):
            raise ValueError('Invalid voxel-to-world affine')
        converted = {int(k): v for k,v in self.labels.items()}
        if len(converted) != len(self.labels):
            raise ValueError("Duplicate numeric label IDs")
        self.labels = converted
        present = set(int(v) for v in np.unique(self.data)) - {0}
        if not present.issubset(self.labels) or any(not isinstance(v,str) or not v.strip() for v in self.labels.values()):
            raise ValueError('Every nonzero image label needs an explicit name')

    def identity(self):
        return {**self.metadata, 'shape': list(self.data.shape), 'affine': self.affine.tolist(),
                'label_image_sha256': sha(self.data.astype('<i4').tobytes()),
                'labels_sha256': sha(json.dumps(self.labels, sort_keys=True).encode())}


def load_atlas(manifest):
    """Load only locally supplied atlas files; downloads/licensing remain explicit."""
    manifest = Path(manifest)
    m = json.loads(manifest.read_text())
    import nibabel as nib
    path = manifest.parent / m['image']
    image = nib.load(path)
    if image.header.get_xyzt_units()[0] != 'mm':
        raise ValueError('NIfTI spatial units must explicitly be mm')
    q, qc = image.get_qform(coded=True); s, sc = image.get_sform(coded=True)
    if not qc and not sc:
        raise ValueError('NIfTI requires a coded spatial transform')
    if qc and sc and not np.allclose(q,s,atol=1e-4,rtol=0):
        raise ValueError('Conflicting qform/sform: resolve the spatial definition explicitly')
    meta = {k:v for k,v in m.items() if k not in ('image','labels')}
    meta.update(image_file_sha256=sha(path.read_bytes()), manifest_sha256=sha(manifest.read_bytes()), nibabel_version=nib.__version__)
    return Atlas(np.asanyarray(image.dataobj), image.affine, meta, m['labels'])


def crosswalk(source, target):
    if source.metadata['space'] != target.metadata['space']:
        raise ValueError('Different template spaces: a validated registration is required first')
    if source.data.shape != target.data.shape or not np.allclose(source.affine,target.affine,atol=1e-6,rtol=0):
        raise ValueError('Different grids: explicit, documented alignment is required first')
    volume = float(abs(np.linalg.det(source.affine[:3,:3])))
    source_sizes = dict(zip(*np.unique(source.data,return_counts=True)))
    target_sizes = dict(zip(*np.unique(target.data,return_counts=True)))
    mask = (source.data != 0) & (target.data != 0)
    pairs, counts = np.unique(np.column_stack((source.data[mask],target.data[mask])),axis=0,return_counts=True)
    edges = []
    for (a,b),n in zip(pairs,counts):
        ns,nt = int(source_sizes[a]),int(target_sizes[b]);n=int(n)
        edges.append(dict(source_id=int(a),source_label=source.labels[a],target_id=int(b),target_label=target.labels[b],
                          overlap_voxels=n,overlap_mm3=n*volume,source_fraction=n/ns,target_fraction=n/nt,
                          dice=2*n/(ns+nt),jaccard=n/(ns+nt-n)))
    def coverage(sizes, side, labels):
        result=[]
        for value,n in sizes.items():
            if not value:continue
            matched=sum(e['overlap_voxels'] for e in edges if e[side+'_id']==value)
            result.append(dict(id=int(value),label=labels[value],voxels=int(n),volume_mm3=int(n)*volume,
                               mapped_fraction=matched/int(n),unmapped_fraction=1-matched/int(n)))
        return result
    result=dict(version=VERSION,implementation={'module_sha256':sha(Path(__file__).read_bytes()),'numpy_version':np.__version__},status='geometric_only_requires_review',approved=False,
                source=source.identity(),target=target.identity(),edges=edges,
                source_coverage=coverage(source_sizes,'source',source.labels),
                target_coverage=coverage(target_sizes,'target',target.labels),
                limitations=LIMITATIONS,method='Exact same-grid label intersections; zero is background; no threshold or renormalisation')
    result['crosswalk_sha256']=sha(json.dumps(result,sort_keys=True).encode())
    return result


def point_lookup(atlas, xyz_mm, space):
    if space != atlas.metadata['space']:
        raise ValueError('Coordinate space does not exactly match the atlas; no implicit transform')
    xyz = np.asarray(xyz_mm,dtype=float)
    if xyz.shape != (3,) or not np.isfinite(xyz).all():raise ValueError('Three finite RAS+ millimetre coordinates required')
    voxel = (np.linalg.inv(atlas.affine) @ np.r_[xyz,1])[:3]
    result=dict(version=VERSION,approved=False,atlas=atlas.identity(),xyz_mm=xyz.tolist(),
                continuous_voxel=voxel.tolist(),evidence_kind='reported_peak',
                limitation='Point-in-parcel lookup only. Does not establish cluster extent, parcel-wide effects or coordinate uncertainty.')
    if np.any(voxel < -.5) or np.any(voxel >= np.array(atlas.data.shape)-.5):
        return {**result,'status':'outside_field_of_view'}
    index=np.floor(voxel+.5).astype(int);value=int(atlas.data[tuple(index)])
    return {**result,'status':'labelled' if value else 'background','label_id':value,
            'label':atlas.labels.get(value),'voxel':index.tolist(),
            'method':'Nearest voxel centre; exact half-voxel ties go to the higher index'}


def map_evidence(records, mapping):
    """Attach spatial candidates to the original finding; never create finer-grained findings."""
    check=dict(mapping);fingerprint=check.pop('crosswalk_sha256',None)
    if sha(json.dumps(check,sort_keys=True).encode()) != fingerprint:
        raise ValueError('Crosswalk integrity check failed')
    seen=set();out=[]
    for r in records:
        for field in ('evidence_id','citation','source_location','kind'):
            if not r.get(field):raise ValueError(f'Evidence requires {field}')
        if r['evidence_id'] in seen:raise ValueError('Duplicate evidence ID')
        seen.add(r['evidence_id'])
        mapped={'original':r,'spatial_candidates':[],'status':'unresolved','approved':False}
        if r['kind']=='atlas_roi':
            identity=r.get('atlas',{})
            if all(identity.get(k)==mapping['source'][k] for k in ('atlas_id','version','space','image_file_sha256')) and identity.get('image_file_sha256'):
                candidates=[e for e in mapping['edges'] if e['source_id']==r.get('roi_id')]
                coverage=next((c for c in mapping['source_coverage'] if c['id']==r.get('roi_id')),None)
                if coverage and isinstance(r.get('roi_id'),int) and not isinstance(r.get('roi_id'),bool):
                    mapped.update(status='geometric_candidates_only',spatial_candidates=candidates,source_coverage=coverage)
                else:mapped['reason']='ROI ID is absent from the source image'
            else:mapped['reason']='Exact atlas identity/version/space/image hash is unverified'
        else:mapped['reason']='Label-only, peak and cluster evidence cannot be treated as a whole atlas ROI'
        mapped['cohort_check']='required' if not r.get('cohort_id') else 'identifier supplied; independence still needs review'
        out.append(mapped)
    return dict(version=VERSION,approved=False,crosswalk_sha256=fingerprint,findings=out,limitations=LIMITATIONS)


def report(mapping):
    lines=['# Spatial overlap report (experimental)', '',
           f"{mapping['source']['atlas_id']} → {mapping['target']['atlas_id']}", '',
           'These are geometric correspondences, not equivalent effects or independent findings.', '',
           '| Source ROI | Target ROI | % of source | % of target | Dice |',
           '|---|---|---:|---:|---:|']
    safe=lambda s:str(s).replace('|','\\|').replace('\n',' ')
    for e in mapping['edges']:
        lines.append(f"| {safe(e['source_label'])} | {safe(e['target_label'])} | {100*e['source_fraction']:.2f} | {100*e['target_fraction']:.2f} | {e['dice']:.3f} |")
    lines += ['', 'Unmapped source fractions (including target background):']
    lines += [f"- {safe(c['label'])}: {100*c['unmapped_fraction']:.2f}%" for c in mapping['source_coverage']]
    lines += ['', 'Limitations:']+[f'- {v}' for v in LIMITATIONS]
    lines += ['', f"Crosswalk SHA-256: {mapping['crosswalk_sha256']}"]
    return '\n'.join(lines)+'\n'


def main():
    p=argparse.ArgumentParser(description=__doc__);commands=p.add_subparsers(dest='command',required=True)
    c=commands.add_parser('crosswalk');c.add_argument('--source',type=Path,required=True);c.add_argument('--target',type=Path,required=True);c.add_argument('--report',type=Path)
    c=commands.add_parser('point');c.add_argument('--atlas',type=Path,required=True);c.add_argument('--space',required=True);c.add_argument('--xyz',type=float,nargs=3,required=True)
    c=commands.add_parser('evidence');c.add_argument('--crosswalk',type=Path,required=True);c.add_argument('--records',type=Path,required=True)
    for c in commands.choices.values():c.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    if a.output.exists() or (getattr(a,'report',None) and a.report.exists()):p.error('Output exists; choose a new path to preserve provenance')
    if a.command=='crosswalk':result=crosswalk(load_atlas(a.source),load_atlas(a.target))
    elif a.command=='point':result=point_lookup(load_atlas(a.atlas),a.xyz,a.space)
    else:result=map_evidence(json.loads(a.records.read_text()),json.loads(a.crosswalk.read_text()))
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
    if getattr(a,'report',None):a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(report(result))


if __name__=='__main__':main()
