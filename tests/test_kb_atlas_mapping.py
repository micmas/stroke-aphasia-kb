"""Validate curated links without automatically mapping new draft clusters."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import atlas_mapping


def test_mapping_references_real_units_and_labels():
    assert atlas_mapping.problems() == []


def test_verified_aliases_preserve_side_units_and_approximation_flag():
    _, regions, _ = atlas_mapping.load()
    aliases = {
        'left_slf': 'left_superior_longitudinal_fasciculus',
        'left_spgi': 'left_precentral_gyrus_insula',
        'left_precentral_gyrus_of_the_insula': 'left_precentral_gyrus_insula',
        'left_insular_precentral_gyrus_cluster': 'left_precentral_gyrus_insula',
        'superior_tip_precentral_gyrus_insula': 'left_precentral_gyrus_insula',
    }
    for alias, original in aliases.items():
        assert regions[alias]['side'] == regions[original]['side']
        assert regions[alias]['units'] == regions[original]['units']
        assert bool(regions[alias].get('review')) == bool(regions[original].get('review'))


def test_bottlenecks_are_not_replaced_with_whole_tracts():
    _, regions, unmapped = atlas_mapping.load()
    for name in ('anterior_bottleneck_cluster', 'anterior_bottleneck_roi', 'posterior_bottleneck_cluster'):
        assert name not in regions
        assert unmapped[name]
