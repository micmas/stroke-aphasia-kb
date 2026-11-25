// Deployment exports can be ordinary JSON or a manifest of exact UTF-8 parts.
// Return the original text so review bindings still hash the original export.
export async function loadExportText(url, options = {}, fetcher = fetch) {
  const response = await fetcher(url, options);
  if (!response.ok) throw new Error(`Export download failed: ${response.status}`);
  const text = await response.text();
  const manifest = JSON.parse(text);
  if (manifest._kb_json_parts === undefined) return text;
  if (manifest._kb_json_parts !== 1 || !Array.isArray(manifest.parts) ||
      !manifest.parts.length || !Number.isSafeInteger(manifest.bytes) || manifest.bytes < 0 ||
      !/^[a-f0-9]{64}$/.test(manifest.sha256) ||
      manifest.parts.some((part) => typeof part !== 'string' || !/^[\w.-]+\.txt$/.test(part))) {
    throw new Error('Invalid export download manifest');
  }
  const base = response.url || new URL(url, globalThis.location?.href).href;
  const chunks = await Promise.all(manifest.parts.map(async (part) => {
    const result = await fetcher(new URL(part, base).href, options);
    if (!result.ok) throw new Error(`Export part download failed: ${result.status}`);
    return result.text();
  }));
  const joined = chunks.join('');
  const bytes = new TextEncoder().encode(joined);
  if (bytes.length !== manifest.bytes) throw new Error('Incomplete export download');
  const hash = await crypto.subtle.digest('SHA-256', bytes);
  const hex = Array.from(new Uint8Array(hash), (b) => b.toString(16).padStart(2, '0')).join('');
  if (hex !== manifest.sha256) throw new Error('Export download integrity check failed');
  return joined;
}
