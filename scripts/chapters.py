"""Chapter identity shared by evidence loading and screening.

Legacy, unlabelled records belong to aphasia. Membership never implies approval.
"""
CHAPTERS = {
    "aphasia": {"name": "Aphasia", "url": "https://aphasia-kb.app/"},
    "dysphagia": {"name": "Dysphagia", "url": "https://dysphagia-kb.app/"},
}


def membership(record, parent=None):
    """Finding membership overrides an entry default; missing legacy data is aphasia."""
    if "chapters" in record:
        value = record["chapters"]
    elif parent is not None and "chapters" in parent:
        value = parent["chapters"]
    else:
        return ["aphasia"]
    if (not isinstance(value, list) or not value
            or any(not isinstance(c, str) or c not in CHAPTERS for c in value)
            or len(set(value)) != len(value)):
        raise ValueError("chapters must be a non-empty list of unique aphasia/dysphagia IDs")
    return list(value)


def select_entry(entry, chapter):
    """Copy an entry and select its findings without changing stored evidence."""
    if chapter not in (*CHAPTERS, "all"):
        raise ValueError(f"Unknown chapter: {chapter}")
    own = membership(entry)
    findings = [{**f, "chapters": membership(f, entry)} for f in entry.get("findings") or []]
    selected = [f for f in findings if chapter == "all" or chapter in f["chapters"]]
    if chapter != "all" and chapter not in own and not selected:
        return None
    return {**entry, "chapters": own, **({"findings": selected} if "findings" in entry else {})}


def screening_record(candidate, chapter):
    """Return a chapter-specific view; unlabelled historical decisions are aphasia only.

    Shared bibliographic identity and duplicate links are retained. This read adapter
    does not enable dysphagia writes through the existing aphasia-only portal.
    """
    if chapter not in CHAPTERS:
        raise ValueError(f"Unknown chapter: {chapter}")
    if chapter not in membership(candidate):
        return None
    decisions = [d for d in candidate.get("screening") or []
                 if d.get("chapter", "aphasia") == chapter]
    result = {**candidate, "screening": decisions}
    if chapter != "aphasia":
        result.pop("suggestion", None)
        result.pop("skip_title_abstract", None)
    return result
