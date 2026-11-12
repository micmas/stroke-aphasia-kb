export async function onRequestGet({ data, env }) {
  return Response.json({ email: data.reviewer.email, name: data.reviewer.name, repo: env.GITHUB_REPO, branch: env.GITHUB_BRANCH || 'main' });
}
