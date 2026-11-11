"""Reject duplicate fields instead of silently losing research evidence."""
import json
import yaml


class DuplicateKeyError(ValueError):
    pass


class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        seen = set()
        for key_node, _ in node.value:
            if key_node.tag == 'tag:yaml.org,2002:merge':
                continue  # Explicit YAML merge/override is distinct from duplicate fields.
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in seen
                seen.add(key)
            except TypeError:
                continue  # Let SafeLoader report an unhashable mapping key.
            if duplicate:
                raise DuplicateKeyError(f'Duplicate YAML field {key!r} at line {key_node.start_mark.line + 1}')
        return super().construct_mapping(node, deep=deep)


def load_yaml(text):
    return yaml.load(text, Loader=UniqueKeyLoader)


def load_json(text):
    def unique_pairs(pairs):
        result = {}
        for key,value in pairs:
            if key in result:
                raise DuplicateKeyError(f'Duplicate JSON field {key!r}')
            result[key] = value
        return result
    return json.loads(text, object_pairs_hook=unique_pairs)
