// GET /cc/<Key>_annotated.pdf — a Creative-Commons paper's annotated PDF, public (Access Bypass on cc/*).
import { servePdf } from '../../lib/pdfs.js';
export const onRequestGet = ({ request, env, params }) => servePdf(env, 'cc', [params.path].flat().join('/'), request);
export const onRequestHead = onRequestGet;
