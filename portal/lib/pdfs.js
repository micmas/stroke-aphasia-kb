// The annotated PDFs are not part of the deployment: they live in the R2 bucket bound as
// PDFS (publish_portal.py --sync puts them there, under cc/ for Creative-Commons papers and
// pdf/ for the rest) and these two routes serve them. Access decides who reaches which path:
// cc/* has a Bypass policy (public, linked from the explorer); pdf/* is behind the sign-in,
// and _middleware.js verifies the Access token on pdf/* as it does for the API.

//
// cc/ is open to anyone, so it serves only what the deployed build says is public:
// public-pdfs.json, written by publish_portal.py from portal/papers.json on every build. A
// paper whose licence changed stops being served at the next deploy even if deleting its R2
// object failed, and nothing outside the list is served from cc/ whatever the bucket holds.
// No allowlist (or an unreadable one) means nothing is served: fail closed. Public responses
// are not cached (no-store), because the permission to serve them can be withdrawn.

const SAFE = /^[A-Za-z0-9][A-Za-z0-9._'\-]*\.pdf$/;
export const ALLOWLIST = '/public-pdfs.json';

export async function publicFiles(env, request) {
  if (!env.ASSETS) return null;
  try {
    const res = await env.ASSETS.fetch(new Request(new URL(ALLOWLIST, request.url)));
    if (!res.ok) return null;
    const data = await res.json();
    return Array.isArray(data?.files) ? new Set(data.files.map(String)) : null;
  } catch {
    return null;
  }
}

export async function servePdf(env, prefix, name, request) {
  if (!env.PDFS) return new Response('PDF storage is not configured on this portal', { status: 503 });
  const file = decodeURIComponent(name || '');
  if (!SAFE.test(file)) return new Response('not found', { status: 404 });
  if (prefix === 'cc') {
    const allowed = await publicFiles(env, request);
    if (!allowed || !allowed.has(file)) return new Response('not found', { status: 404, headers: { 'Cache-Control': 'no-store' } });
  }
  const key = `${prefix}/${file}`;
  const ifNoneMatch = request.headers.get('If-None-Match');
  const obj = await env.PDFS.get(key, ifNoneMatch ? { onlyIf: { etagDoesNotMatch: ifNoneMatch.replace(/^W\//, '').replace(/"/g, '') } } : undefined);
  if (!obj) return new Response('not found', { status: 404 });
  const headers = new Headers({
    'Content-Type': 'application/pdf',
    'Content-Disposition': `inline; filename="${file}"`,
    ETag: obj.httpEtag,
    'Cache-Control': prefix === 'cc' ? 'no-store' : 'private, no-store',
    'X-Robots-Tag': 'noindex',
  });
  if (!('body' in obj) || obj.body === undefined) return new Response(null, { status: 304, headers });   // onlyIf matched: not modified
  headers.set('Content-Length', String(obj.size));
  return new Response(request.method === 'HEAD' ? null : obj.body, { status: 200, headers });
}
