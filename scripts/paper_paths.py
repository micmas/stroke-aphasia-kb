"""Resolve screening-prefixed PDFs without changing citation identities."""
from pathlib import Path
import re
import json
from functools import lru_cache


def citation_stem(path):
    return re.sub(r"^C\d+_", "", Path(path).stem).removesuffix("_annotated")


def resolve_paper(directory, name):
    """Accept a citation filename, a recorded filename, or an old manifest path."""
    directory = Path(directory)
    name = Path(name).name
    exact = directory / name
    if exact.exists():
        return exact
    aliases = directory / ".filename-aliases.json"
    if aliases.is_file():
        target = json.loads(aliases.read_text()).get(name)
        if target and (directory / target).resolve().is_relative_to(directory.resolve()):
            return directory / target
    matches = list(directory.glob("C*_" + name))
    matches = [p for p in matches if re.match(r"^C\d+_", p.name)]
    if len(matches) > 1:
        raise ValueError(f"Ambiguous PDF for {name}: {[p.name for p in matches]}")
    return matches[0] if matches else exact


@lru_cache(maxsize=4)
def _registered_names(path, mtime):
    from strict_data import load_yaml
    rows = load_yaml(Path(path).read_text()).get("candidates", [])
    return {str(c["key"]).lstrip("@"): c for c in rows if c.get("key") and re.fullmatch(r"C\d+", c["id"])}


def canonical_paper(directory, key, suffix=".pdf"):
    key = str(key).lstrip("@")
    current = resolve_paper(directory, key + suffix)
    registry = Path(__file__).resolve().parents[1] / "screening/candidates.yaml"
    if registry.exists():
        c = _registered_names(str(registry), registry.stat().st_mtime_ns).get(key)
        if c:
            return Path(directory) / (c["id"] + "_" + key + suffix)
    return current


def paper_filename(candidate, annotated=False):
    """A record keeps its screening ID even after it enters the bibliography."""
    key = str(candidate.get("key") or "").lstrip("@")
    if not key:
        author = re.sub(r"[^A-Za-z0-9]", "", str(candidate.get("first_author") or "Paper"))
        key = author + str(candidate.get("year") or "")
    return f"{candidate['id']}_{key}{'_annotated' if annotated else ''}.pdf"
