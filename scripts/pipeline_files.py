"""Filesystem boundaries shared by draft writers. No scientific content changes."""
import os
import re
import tempfile
from pathlib import Path

BUCKETS = ('regions','impairments','therapies','predictors','reviews','ingredients')


def safe_child(directory: Path, name: str) -> Path:
    if not isinstance(name,str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*\.md",name):
        raise ValueError(f'Unsafe Markdown filename: {name!r}')
    path=directory/name
    if path.resolve().parent != directory.resolve():
        raise ValueError('Destination escapes its directory')
    return path


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix='.'+path.name+'.',dir=path.parent)
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as f:
            f.write(text); f.flush(); os.fsync(f.fileno())
        os.replace(tmp,path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)


def human_work(fm: dict) -> bool:
    return (fm.get('status','draft') != 'draft'
            or any(fm.get(k) for k in ('portal_reviews','reviewer_marks','portal_comments','rereview_of','reviewer'))
            or not str(fm.get('created_by','')).startswith('agent:')
            or any(isinstance(f,dict) and any(f.get(k) for k in ('edits','review','portal_comments')) for f in fm.get('findings') or []))
