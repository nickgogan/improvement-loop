#!/usr/bin/env node
/**
 * UserPromptSubmit hook — hub/role awareness backstop.
 *
 * Reads the incoming prompt, scores it against the context-hub role registry
 * (roles/registry.json), and — when a role matches confidently — injects a
 * short note naming the role and the skills that should auto-load for that
 * persona. This is the runtime safety net for skill drift: even if the active
 * skill (or a brand-new skill) isn't hub-aware, the matched role's auto-skills
 * still surface here.
 *
 * Matching is a yes/no GATE (not a ranked list), so it uses whole-word token
 * matching + stopword filtering + a phrase bonus — substring matching would
 * fire on incidental hits (e.g. "in" inside "testing") and inject noise.
 *
 * Guarantees:
 *  - Reads the registry straight from disk — no local-server dependency, no MCP
 *    handshake, no npm deps (fast cold start).
 *  - ALWAYS exits 0. Any error → silent no-op. Never blocks a prompt (exit 2),
 *    never injects on a weak/no match.
 *
 * Config via env:
 *  - CONTEXT_HUB_DIR      override hub repo path
 *  - HUB_HOOK_THRESHOLD   override the min role score to inject (default 10)
 *
 * Provenance: anonymized copy of a hook from a private enterprise context-hub
 * repo, shared by its author with Nick 2026-07-12. Org, author, product, tool
 * prefixes, and paths replaced with neutral placeholders before this vault was
 * shared publicly; logic is unchanged.
 */

import { readFileSync } from 'node:fs';
import path from 'node:path';

const HUB_DIR = process.env.CONTEXT_HUB_DIR
  || '/path/to/context-hub';
const THRESHOLD = Number(process.env.HUB_HOOK_THRESHOLD || 10);

const STOP = new Set([
  'the', 'and', 'for', 'with', 'this', 'that', 'you', 'your', 'our', 'are', 'was',
  'can', 'will', 'into', 'via', 'per', 'from', 'has', 'have', 'not', 'all', 'any',
  'use', 'using', 'make', 'get', 'set', 'add', 'fix', 'run', 'new', 'how', 'what',
  'why', 'when', 'who', 'please', 'help', 'need', 'want', 'should', 'would', 'could'
]);

const norm = (s) => String(s || '').toLowerCase();
const tokenize = (s) => norm(s).split(/[^a-z0-9]+/i).filter((t) => t.length >= 3);

function readStdin() {
  try { return readFileSync(0, 'utf8'); } catch { return ''; }
}

function roleIndex(role) {
  const tok = (s) => new Set(tokenize(s));
  const tags = [...(role.aliases || []), ...(role.keywords || []), ...(role.autoSkills || [])];
  return {
    id: tok(role.id),
    title: tok(role.title),
    persona: tok(role.personaPrompt),
    desc: tok(role.description),
    tags: new Set(tags.flatMap((t) => tokenize(t))),
    phrases: [...(role.aliases || []), ...(role.keywords || [])].map(norm).filter((p) => p.includes(' '))
  };
}

// Whole-word matching only. Each significant term scores once, at the
// highest-weight field it appears in. Multi-word curated phrases that appear
// verbatim in the prompt earn a strong bonus.
function scoreRole(role, sigTerms, promptNorm) {
  const idx = roleIndex(role);
  let score = 0;
  const matched = new Set();
  for (const t of sigTerms) {
    let w = 0;
    if (idx.id.has(t)) w = 5;
    else if (idx.title.has(t)) w = 4;
    else if (idx.persona.has(t)) w = 3;
    else if (idx.tags.has(t)) w = 3;
    else if (idx.desc.has(t)) w = 2;
    if (w) { score += w; matched.add(t); }
  }
  for (const p of idx.phrases) {
    if (promptNorm.includes(p)) { score += 5; matched.add(p); }
  }
  return { score, matched: [...matched] };
}

function main() {
  let prompt = '';
  try {
    const data = JSON.parse(readStdin() || '{}');
    prompt = data.prompt || data.user_prompt || '';
  } catch { /* not JSON — leave prompt empty */ }
  if (!prompt || prompt.trim().length < 4) return;

  let roles;
  try {
    roles = JSON.parse(readFileSync(path.join(HUB_DIR, 'roles', 'registry.json'), 'utf8'));
  } catch { return; } // registry missing/corrupt → silent no-op
  if (!Array.isArray(roles) || roles.length === 0) return;

  const promptNorm = norm(prompt);
  const sigTerms = [...new Set(tokenize(prompt))].filter((t) => !STOP.has(t));
  if (sigTerms.length === 0) return;

  let best = null;
  for (const role of roles) {
    const { score } = scoreRole(role, sigTerms, promptNorm);
    if (score > 0 && (!best || score > best.score)) best = { role, score };
  }
  if (!best || best.score < THRESHOLD) return;

  const r = best.role;
  const skills = (r.autoSkills || []).join(', ');
  const note =
    `[hub-context] This prompt matches the "${r.title}" role (context-hub role registry, score ${best.score}). `
    + `Consider loading the role's auto-skills where relevant — in addition to any query-specific skills: ${skills}. `
    + `Call hub_role_resolve_skills("${r.id}", <task>) for the full merged set.`;

  process.stdout.write(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'UserPromptSubmit',
      additionalContext: note
    }
  }));
}

try { main(); } catch { /* never block a prompt */ }
process.exit(0);
