# Spatial evidence harmonisation (experimental)

This separate layer measures spatial correspondences between explicitly identified
atlas images. It does not replace the curated atlas-to-KB mappings, change running
extractions/reviews, or approve findings. Synthetic tests establish the geometry;
real Harvard–Oxford/AAL correspondence and clinical validity are **not yet validated**.

## Many-to-many correspondence

For source parcel A and target parcel B, retain every nonzero intersection:

- Source fraction: volume(A ∩ B) / volume(A).
- Target fraction: volume(A ∩ B) / volume(B).
- Dice: 2 volume(A ∩ B) / (volume(A) + volume(B)).
- Jaccard: volume(A ∩ B) / volume(A ∪ B).

These fractions are directional. If A contains five equal target parcels, each
edge has 20% source coverage and 100% target coverage, with Dice 1/3. This does
not establish five parcel-specific effects. Attach all five candidates to the
**one original finding**. Do not copy effect sizes, p-values, participants or
study counts into five inferred findings. Preserve outcome, method, timing,
adjustment, null results and cohort identity in the original evidence record.
Shared participants still need independent checking; a cohort ID is not proof
of independence.

Background is label 0. Unmapped fractions are reported explicitly, never
renormalised away. No arbitrary overlap threshold drops small intersections.
Overlap fractions describe geometry, not statistical confidence. Matching names
alone do not establish matching parcels.

## Inputs and scope

The prototype supports deterministic 3D integer-label NIfTI images. Probabilistic
and overlapping-channel atlases are refused: thresholding or taking an argmax
would change the definition and must be a separate documented operation.

Both atlases must have the exact same declared template space, image shape and
voxel-to-world affine. It performs **no registration or resampling**. Different
voxel grids require explicit alignment first; different templates require a
validated transform. Resampling is not registration. Future alignment must retain
original image hashes, template identities, transform provenance, interpolation,
analysis grid and sensitivity to grid choice. Nearest-neighbour interpolation
preserves discrete labels but does not eliminate discretisation error.

Generic `MNI`/`MNI152`, unspecified versions and guessed atlas identities are not
acceptable for spatial mapping. Specify the actual template, such as
`MNI152NLin6Asym`, only if supported by the source provenance. NIfTI header units
must be mm; missing transforms and conflicting qform/sform are refused. Manifest
metadata are declarations needing source verification, not facts certified by
this tool. Atlas distribution permissions remain those of the atlas provider.

A reported peak can be looked up in the atlas in the *same* declared space using
RAS+ millimetres. Its result is a nearest-voxel point assignment; it is not a
cluster, a parcel-wide finding, a localisation confidence interval or a substitute
for checking coordinate rounding and proximity to anatomical boundaries. There is
no implicit Talairach-to-MNI transform or default uncertainty sphere.

## Use

Dependencies (`numpy`, `nibabel`) are already listed in the project requirements.
Install missing dependencies only when no processing job is using that environment,
or use a separate environment for this tool.

Each atlas has a JSON manifest beside its local NIfTI file:

```json
{
  "atlas_id": "EXACT_PROVIDER_ATLAS_ID",
  "version": "EXACT_RELEASE_AND_VARIANT",
  "space": "EXACT_TEMPLATE_ID",
  "template_reference": "Template source/version reference",
  "source": "Atlas provider URL or publication",
  "licence": "Actual licence or distribution terms",
  "representation": "deterministic_labels",
  "units": "mm",
  "world_axes": "RAS+",
  "image": "atlas.nii.gz",
  "labels": {"1": "Exact provider label"}
}
```

Every nonzero image value needs a label. Record threshold and lateralisation
variant in the version when relevant; do not substitute the same named atlas from
another release. The tool records image and manifest SHA-256 hashes, the affine,
shape, label-table hash and all declared metadata.

```bash
python scripts/spatial_harmonisation.py crosswalk \
  --source /path/source-atlas.json --target /path/target-atlas.json \
  --output /path/crosswalk.json --report /path/crosswalk.md

python scripts/spatial_harmonisation.py point \
  --atlas /path/target-atlas.json --space EXACT_TEMPLATE_ID \
  --xyz -48 20 12 --output /path/point.json

python scripts/spatial_harmonisation.py evidence \
  --crosswalk /path/crosswalk.json --records /path/findings.json \
  --output /path/mapped-findings.json
```

Outputs must not already exist. Keep development/pilot reports outside GitHub.
`findings.json` is a list of original records. Required fields are `evidence_id`,
`citation`, `source_location` and `kind`. For `kind: atlas_roi`, additionally provide
`roi_id` and `atlas` with `atlas_id`, `version`, `space`, `image_file_sha256` matching
the reviewed source atlas. Keep all other scientific fields in the same record;
the mapping preserves them verbatim. If the paper does not identify the exact
atlas image, do not invent its hash: mapping remains unresolved until verified.
`cohort_id` can help track shared datasets but is not used to count studies here.
Label-only or other evidence kinds remain unresolved by the ROI crosswalk.

## Next validation gate

Before using this in a report about actual scans:

1. Obtain licensed, versioned Harvard–Oxford and AAL distributions and verify their
   actual templates, resolutions, variants, hemispheres and label tables.
2. Independently check selected frontal, temporal, insular and boundary parcels,
   including one-to-many, many-to-one, partial and absent correspondences.
3. Test grid-resolution sensitivity and any necessary registered transforms.
4. Source-check a small set of papers: ROI definitions, coordinates and masks,
   including ambiguous versions and missing coordinate conventions.
5. Review narrative claims for ecological inference: an effect for a broad ROI
   does not localise that effect to its smaller overlapping subregions.

Current output is a geometric audit aid, not a meta-analysis or patient-level
prediction. The existing report generator does not consume it automatically.

Method references: [BIDS spatial coordinate identifiers](https://bids-specification.readthedocs.io/en/stable/glossary.html)
and [Nilearn resampling documentation](https://nilearn.github.io/dev/modules/generated/nilearn.image.resample_to_img.html).
