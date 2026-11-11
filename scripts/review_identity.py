"""Normalise recorded extraction/review identities without guessing unknown formats."""
import re


def model_tag(value: str | None) -> str | None:
    value = str(value or '').strip().lower()
    for prefix in ('agent:', 'model:'):
        if value.startswith(prefix):
            value = value[len(prefix):]
            break
    for prefix in ('ollama-extract-cli/', 'ollama-refocus-cli/'):
        if value.startswith(prefix):
            value = value[len(prefix):]
            break
    # A tag needs an explicit version; an unversioned tool/agent label cannot
    # establish independence. Ollama namespace/model:tag names are supported.
    return value if re.fullmatch(r'[a-z0-9][a-z0-9._/-]*:[a-z0-9][a-z0-9._-]*', value) else None


def independent(extractor: str | None, reviewer: str) -> bool:
    left, right = model_tag(extractor), model_tag(reviewer)
    return bool(left and right and left != right)
