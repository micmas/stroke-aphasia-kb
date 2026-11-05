// The Access token check of the portal's API, against a key pair made here:
// a valid token passes and names the reviewer; a wrong audience, a bad signature
// or an expired token is refused. Run: node --test portal/functions/test/
import test from 'node:test';
import assert from 'node:assert/strict';
import { webcrypto } from 'node:crypto';
import { verifyAccessJwt, onRequest } from '../_middleware.js';

const subtle = webcrypto.subtle;
const b64 = (buf) => Buffer.from(buf).toString('base64url');
const enc = (obj) => b64(Buffer.from(JSON.stringify(obj)));

const pair = await subtle.generateKey({ name: 'RSASSA-PKCS1-v1_5', modulusLength: 2048, publicExponent: new Uint8Array([1, 0, 1]), hash: 'SHA-256' }, true, ['sign', 'verify']);
const jwk = await subtle.exportKey('jwk', pair.publicKey);
jwk.kid = 'k1'; jwk.alg = 'RS256'; jwk.use = 'sig';
delete jwk.ext; delete jwk.key_ops;
const env = { ACCESS_TEAM_DOMAIN: 'test-team', ACCESS_AUD: 'aud-123' };
globalThis.fetch = async (url) => {
  assert.equal(url, 'https://test-team.cloudflareaccess.com/cdn-cgi/access/certs');
  return { ok: true, json: async () => ({ keys: [jwk] }) };
};
async function token(payload, header = { alg: 'RS256', kid: 'k1' }, key = pair.privateKey) {
  const data = `${enc(header)}.${enc(payload)}`;
  const sig = await subtle.sign({ name: 'RSASSA-PKCS1-v1_5' }, key, Buffer.from(data));
  return `${data}.${b64(sig)}`;
}
const future = Math.floor(Date.now() / 1000) + 600;

test('a valid Access token names the reviewer', async () => {
  const p = await verifyAccessJwt(await token({ aud: ['aud-123'], email: 'Alex@Example.org', exp: future }), env);
  assert.equal(p.email, 'Alex@Example.org');
});

test('wrong audience, expiry and bad signature are refused', async () => {
  await assert.rejects(verifyAccessJwt(await token({ aud: 'other', email: 'a@b', exp: future }), env), /audience/);
  await assert.rejects(verifyAccessJwt(await token({ aud: 'aud-123', email: 'a@b', exp: 1 }), env), /expired/);
  const other = await subtle.generateKey({ name: 'RSASSA-PKCS1-v1_5', modulusLength: 2048, publicExponent: new Uint8Array([1, 0, 1]), hash: 'SHA-256' }, true, ['sign', 'verify']);
  await assert.rejects(verifyAccessJwt(await token({ aud: 'aud-123', email: 'a@b', exp: future }, { alg: 'RS256', kid: 'k1' }, other.privateKey), env), /signature/);
  await assert.rejects(verifyAccessJwt(await token({ aud: 'aud-123', exp: future }), env), /email/);
});

test('the API refuses requests without a token and lets static files through', async () => {
  const next = async () => new Response('ok');
  const r1 = await onRequest({ request: new Request('https://portal.example/api/me'), env, data: {}, next });
  assert.equal(r1.status, 401);
  const r2 = await onRequest({ request: new Request('https://portal.example/manifest.json'), env, data: {}, next });
  assert.equal(r2.status, 200);
  const data = {};
  const r3 = await onRequest({ request: new Request('https://portal.example/api/me', { headers: { 'Cf-Access-Jwt-Assertion': await token({ aud: 'aud-123', email: 'Alex@Example.org', exp: future }) } }), env, data, next });
  assert.equal(r3.status, 200);
  assert.equal(data.reviewer.email, 'alex@example.org');
});
