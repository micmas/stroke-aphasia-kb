// portal-mailer — a Worker with one job: email the maintainers when someone asks, on the
// portal's welcome page, to become a reviewer. Pages Functions cannot send mail themselves,
// so the portal calls this Worker through a service binding (MAILER in portal/wrangler.toml).
//
// It has no public address (workers_dev = false, no route): only the portal can reach it.
// Mail goes out through Cloudflare Email Routing, which delivers only to destination
// addresses that have been verified on the account, so even a mistake here cannot write to
// a stranger. Set-up: docs/PORTAL.md, "Reviewer requests by email".
import { EmailMessage } from 'cloudflare:email';

const line = (s) => String(s ?? '').replace(/[\r\n]+/g, ' ').trim();
const b64 = (s) => btoa(String.fromCharCode(...new TextEncoder().encode(s)));
const encoded = (s) => (/^[\x20-\x7e]*$/.test(s) ? s : `=?UTF-8?B?${b64(s)}?=`);

export function compose(from, to, request, portalUrl, now = new Date()) {
  const name = line(request.name), email = line(request.email);
  const body = [
    `${name} <${email}> would like to become a reviewer of the stroke aphasia knowledge base.`,
    '',
    `Name:        ${name}`,
    `Email:       ${email}`,
    `Affiliation: ${line(request.affiliation) || '(not given)'}`,
    `Sent:        ${line(request.requested) || now.toISOString()}`,
    '',
    'What they wrote:',
    String(request.note || '(nothing)').replace(/\r\n?/g, '\n'),
    '',
    'To accept: add the email to the Access policy of the review portal (Cloudflare Zero Trust,',
    'Access, Applications) and to portal/reviewers.yaml, then remove the request from the list on',
    `the portal's Home page: ${line(portalUrl)}`,
    '',
  ].join('\n');
  const headers = [
    `From: Stroke aphasia KB review portal <${from}>`,
    `To: ${to}`,
    `Reply-To: ${encoded(name).replace(/[<>,;"]/g, '')} <${email}>`,
    `Subject: ${encoded(`Reviewer request: ${name}`)}`,
    `Date: ${now.toUTCString().replace('GMT', '+0000')}`,
    `Message-ID: <${crypto.randomUUID()}@${from.split('@')[1]}>`,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=utf-8',
    'Content-Transfer-Encoding: base64',
  ];
  return `${headers.join('\r\n')}\r\n\r\n${b64(body).replace(/(.{76})/g, '$1\r\n')}\r\n`;
}

export default {
  async fetch(request, env) {
    if (request.method !== 'POST') return new Response('POST only', { status: 405 });
    let data;
    try { data = await request.json(); } catch { return new Response('expected JSON', { status: 400 }); }
    const to = (Array.isArray(data.to) ? data.to : []).map(line).filter((a) => /^[^\s@]+@[^\s@]+$/.test(a));
    if (!to.length || !data.request?.email) return new Response('nothing to send', { status: 400 });
    const failures = [];
    for (const address of to) {
      try {
        await env.MAIL.send(new EmailMessage(env.FROM, address, compose(env.FROM, address, data.request, data.portalUrl)));
      } catch (e) { failures.push(`${address}: ${e.message}`); }
    }
    return failures.length === to.length
      ? new Response(JSON.stringify({ error: failures.join('; ') }), { status: 502, headers: { 'Content-Type': 'application/json' } })
      : Response.json({ ok: true, sent: to.length - failures.length });
  },
};
