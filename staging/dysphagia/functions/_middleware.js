// Require the existing Cloudflare Access identity for every staging asset and API.
const certsCache = { keys: null, at: 0 };

function b64url(s) {
  s = s.replace(/-/g, '+').replace(/_/g, '/');
  while (s.length % 4) s += '=';
  return Uint8Array.from(atob(s), (c) => c.charCodeAt(0));
}

async function publicKeys(teamDomain) {
  if (certsCache.keys && Date.now() - certsCache.at < 3600_000) return certsCache.keys;
  const res = await fetch(`https://${teamDomain}.cloudflareaccess.com/cdn-cgi/access/certs`);
  if (!res.ok) throw new Error(`certs ${res.status}`);
  const data = await res.json();
  const keys = new Map();
  for (const jwk of data.keys || []) {
    keys.set(jwk.kid, await crypto.subtle.importKey('jwk', jwk, { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['verify']));
  }
  certsCache.keys = keys; certsCache.at = Date.now();
  return keys;
}

export async function verifyAccessJwt(token, env) {
  const [h, p, s] = token.split('.');
  if (!h || !p || !s) throw new Error('malformed token');
  const header = JSON.parse(new TextDecoder().decode(b64url(h)));
  const payload = JSON.parse(new TextDecoder().decode(b64url(p)));
  const keys = await publicKeys(env.ACCESS_TEAM_DOMAIN);
  const key = keys.get(header.kid);
  if (!key) throw new Error('unknown key id');
  const ok = await crypto.subtle.verify({ name: 'RSASSA-PKCS1-v1_5' }, key, b64url(s), new TextEncoder().encode(`${h}.${p}`));
  if (!ok) throw new Error('bad signature');
  const aud = Array.isArray(payload.aud) ? payload.aud : [payload.aud];
  if (!aud.includes(env.ACCESS_AUD)) throw new Error('wrong audience');
  if (!payload.exp || payload.exp * 1000 < Date.now()) throw new Error('expired');
  if (!payload.email) throw new Error('no email in token');
  return payload;
}

export async function onRequest({ request, env, data, next }) {
  const url = new URL(request.url);
  const isApi = url.pathname.startsWith('/api/');
  const refuse = (msg) => (isApi
    ? new Response(JSON.stringify({ error: msg }), { status: 401, headers: { 'Content-Type': 'application/json' } })
    : new Response(msg, { status: 401 }));
  const token = request.headers.get('Cf-Access-Jwt-Assertion');
  try {
    if (token) {
      const payload = await verifyAccessJwt(token, env);
      data.reviewer = { email: String(payload.email).toLowerCase(), name: payload.name || null };
    } else if (env.DEV_REVIEWER && url.hostname === 'localhost') {
      data.reviewer = { email: String(env.DEV_REVIEWER).toLowerCase(), name: 'dev' };
    } else {
      return refuse('not signed in through Cloudflare Access');
    }
  } catch (e) {
    return refuse(`access token rejected: ${e.message}`);
  }
  return next();
}
