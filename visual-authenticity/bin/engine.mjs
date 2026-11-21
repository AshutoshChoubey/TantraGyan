#!/usr/bin/env node
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';
import { spawnSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const REPO_ROOT = path.resolve(__dirname, '../../');
const TOOLKIT_CLI = path.resolve(REPO_ROOT, 'visual-authenticity/toolkit/cli/bin/cli.js');
const AUDIT_DIR = path.resolve(REPO_ROOT, 'visual-authenticity/audit');
const CONTEXT_DIR = path.resolve(REPO_ROOT, 'visual-authenticity/context');
const PROGRESS_DIR = path.resolve(REPO_ROOT, 'visual-authenticity/progress');

const args = process.argv.slice(2);
const command = args[0] || 'help';

function ensureDirectories() {
  [AUDIT_DIR, CONTEXT_DIR, PROGRESS_DIR].forEach(dir => {
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  });
}

function runDetector(targets = ['css', 'index.html', 'reader.html', 'bnn.html', 'bnn-reader.html', 'sadhana-reader.html'], options = {}) {
  ensureDirectories();
  const cliArgs = ['detect', '--json', ...targets];
  if (options.extra) cliArgs.push(...options.extra);

  console.log(`[Visual Authenticity Engine - TantraGyan] Running detector on: ${targets.join(', ')}...`);
  const result = spawnSync('node', [TOOLKIT_CLI, ...cliArgs], {
    cwd: REPO_ROOT,
    encoding: 'utf-8',
    maxBuffer: 20 * 1024 * 1024
  });

  let parsed = [];
  try {
    if (result.stdout && result.stdout.trim().startsWith('[')) {
      parsed = JSON.parse(result.stdout.trim());
    }
  } catch (err) {
    console.error('[Engine] Failed to parse JSON detector output:', err.message);
  }

  const outputPath = path.resolve(AUDIT_DIR, 'DETECTION_RESULTS.json');
  fs.writeFileSync(outputPath, JSON.stringify(parsed, null, 2), 'utf-8');
  console.log(`[Visual Authenticity Engine - TantraGyan] Wrote ${parsed.length} raw detector findings to ${outputPath}`);
  return { code: result.status, findings: parsed, stderr: result.stderr };
}

switch (command) {
  case 'detect':
    const targets = args.slice(1).length > 0 ? args.slice(1) : ['css', 'index.html', 'reader.html', 'bnn.html', 'bnn-reader.html', 'sadhana-reader.html'];
    const res = runDetector(targets);
    console.log(`Detector completed with exit code ${res.code}. Total findings: ${res.findings.length}`);
    process.exit(res.code === 2 ? 0 : res.code);
    break;

  case 'status':
    console.log(`Visual Authenticity Engine - TantraGyan`);
    console.log(`Project Root: ${REPO_ROOT}`);
    console.log(`Context Dir: ${CONTEXT_DIR}`);
    console.log(`Audit Dir: ${AUDIT_DIR}`);
    console.log(`Progress Dir: ${PROGRESS_DIR}`);
    break;

  case 'help':
  default:
    console.log(`Visual Authenticity Engine (Project: TantraGyan)`);
    console.log(`Usage: node visual-authenticity/bin/engine.mjs <command>`);
    console.log(`Commands:`);
    console.log(`  detect [targets...]  Scan frontend files using vendored Impeccable detector`);
    console.log(`  status               Show engine configuration and paths`);
    console.log(`  help                 Show this help message`);
    break;
}
