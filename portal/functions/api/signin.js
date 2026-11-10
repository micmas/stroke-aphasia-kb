// GET /api/signin — "I'm already an approved reviewer" on the welcome page points here.
// Everything under /api/ sits behind Cloudflare Access, so arriving without a session
// shows the Access sign-in; once signed in (the middleware has checked the token) the
// reviewer is sent on to the portal itself.
export const onRequestGet = ({ request }) => Response.redirect(new URL('/', request.url).toString(), 302);
