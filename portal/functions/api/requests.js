// The maintainer's side of "I'd like to become a reviewer" (lib/requests.js).
//   GET    /api/requests           the requests waiting: {requests: [{id, name, email, affiliation, note, requested}]}
//   DELETE /api/requests?id=<id>   remove one, once the person has been added (or declined)
// Only emails in MAINTAINERS may read or remove them; other reviewers get 403.
import { isMaintainer } from './apply.js';
import { listRequests, removeRequest } from '../../lib/requests.js';

const guard = (env, data) => {
  if (!isMaintainer(env, data.reviewer?.email)) return Response.json({ error: 'only a maintainer can see reviewer requests' }, { status: 403 });
  if (!env.UPLOADS) return Response.json({ error: 'requests are not set up on this portal (no R2 bucket bound)', requests: [] }, { status: 503 });
  return null;
};

export async function onRequestGet({ env, data }) {
  return guard(env, data) || Response.json({ requests: await listRequests(env) });
}

export async function onRequestDelete({ request, env, data }) {
  const refused = guard(env, data);
  if (refused) return refused;
  const id = new URL(request.url).searchParams.get('id') || '';
  return (await removeRequest(env, id)) ? Response.json({ ok: true }) : Response.json({ error: 'no such request' }, { status: 404 });
}
