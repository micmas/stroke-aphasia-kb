"""Resource limit for automatic extraction; never truncate a source to fit."""
import pymupdf

MAX_AUTOMATIC_PAGES = 50


def page_count(pdf):
    with pymupdf.open(pdf) as document:
        return len(document)


def source_hold(pdf, allow_long_paper=False):
    pages = page_count(pdf)
    if pages > MAX_AUTOMATIC_PAGES and not allow_long_paper:
        return {'status': 'source_selection_required', 'pdf_pages': pages,
                'reason': f'{pages} pages exceeds the {MAX_AUTOMATIC_PAGES}-page automatic limit. Select a shorter separately registered publication, or explicitly allow the complete long paper. No pages were dropped.'}
    return None
