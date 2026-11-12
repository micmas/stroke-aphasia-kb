// GET /pdf/<Key>_annotated.pdf — every other annotated PDF, for signed-in reviewers only
// (Access in front, and the middleware's own token check).
import { servePdf } from '../../lib/pdfs.js';
export const onRequestGet = ({ request, env, params }) => servePdf(env, 'pdf', [params.path].flat().join('/'), request);
export const onRequestHead = onRequestGet;
