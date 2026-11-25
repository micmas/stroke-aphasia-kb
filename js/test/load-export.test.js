import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { loadExportText } from '../../explorer/load-export.js';

test('packaged UTF-8 export reconstructs exact bytes and review hash; packaging is idempotent', async () => {
  const dir = mkdtempSync(join(tmpdir(), 'kb-export-'));
  try {
    const original = JSON.stringify({ findings: [{ citation: '@Paper', claim: 'é🧠句'.repeat(50) }], provenance: 'unchanged' });
    const file = join(dir, 'kb.json');
    writeFileSync(file, original);
    const code = 'import sys;sys.path.insert(0,"scripts");from package_export import package_export;package_export(sys.argv[1],limit=100,part_bytes=17)';
    execFileSync('python3', ['-c', code, file], { env: { ...process.env, PYTHONDONTWRITEBYTECODE: '1' } });
    const manifestText = readFileSync(file, 'utf8');
    execFileSync('python3', ['-c', code, file], { env: { ...process.env, PYTHONDONTWRITEBYTECODE: '1' } });
    assert.equal(readFileSync(file, 'utf8'), manifestText);
    const manifest = JSON.parse(manifestText);
    for (const part of manifest.parts) assert.ok(readFileSync(join(dir, part)).length <= 17);
    const fetcher = async (url, options) => {
      assert.equal(options.cache, 'no-store');
      const name = new URL(url).pathname.split('/').pop();
      return { ok: true, url, text: async () => readFileSync(join(dir, name), 'utf8') };
    };
    const result = await loadExportText('https://example.test/export/kb.json', { cache: 'no-store' }, fetcher);
    assert.equal(result, original);
    assert.equal(createHash('sha256').update(result).digest('hex'), manifest.sha256);
    assert.deepEqual(JSON.parse(result), JSON.parse(original));
    const bad = async (url, options) => url.endsWith('.txt') ? { ok: false, status: 404 } : fetcher(url, options);
    await assert.rejects(loadExportText('https://example.test/export/kb.json', { cache: 'no-store' }, bad), /part download failed/);
    writeFileSync(join(dir, manifest.parts[0]), readFileSync(join(dir, manifest.parts[0]), 'utf8').replace('findings', 'fandings'));
    await assert.rejects(loadExportText('https://example.test/export/kb.json', { cache: 'no-store' }, fetcher), /integrity check failed/);
  } finally { rmSync(dir, { recursive: true, force: true }); }
});

test('ordinary exports remain unchanged; failed downloads and unsafe part paths are refused', async () => {
  const raw = '{"findings":[]}\n';
  assert.equal(await loadExportText('/kb.json', {}, async () => ({ ok: true, text: async () => raw })), raw);
  await assert.rejects(loadExportText('/kb.json', {}, async () => ({ ok: false, status: 500 })), /500/);
  const manifest = { _kb_json_parts: 1, parts: ['../private.txt'], bytes: 1, sha256: '0'.repeat(64) };
  await assert.rejects(loadExportText('/kb.json', {}, async () => ({ ok: true, text: async () => JSON.stringify(manifest) })), /Invalid export/);
});
