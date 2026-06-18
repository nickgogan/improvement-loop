---
name: "Supply-Chain Hardening for Agent Packages"
summary: "Agent harness treats npm dependency changes as reviewed code changes. Exact-pinned versions, min-release-age=2 (avoids same-day npm releases), generated shrinkwrap for the distributed package, pre-commit lockfile guards (blocked unless explicit env var), and no lifecycle scripts by default during install."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "mcp-tool-poisoning-attack-surface.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
pipeline_status: "extracted"
consumed_by:
  - "skills/supply-chain-hardening-for-agent-packages.md"
---

# Supply-Chain Hardening for Agent Packages

## Pattern

Treat dependency management with the same rigor as code review:

1. **Exact-pinned versions**: Direct external deps pinned to exact versions (not ranges). Internal workspace packages can use ranges.
2. **min-release-age=2**: `.npmrc` setting that avoids resolving npm packages published in the last 2 days (mitigates same-day supply chain attacks).
3. **Generated shrinkwrap**: The distributed CLI package gets a generated `npm-shrinkwrap.json` that locks the entire dependency tree for end users.
4. **Pre-commit lockfile guard**: `package-lock.json` changes are blocked by pre-commit hook unless `PI_ALLOW_LOCKFILE_CHANGE=1` is explicitly set.
5. **No lifecycle scripts**: `--ignore-scripts` by default during install. Lifecycle scripts in new deps require explicit review and allowlist entry.
6. **Verification script**: `npm run check` validates pinned deps, TypeScript imports, and shrinkwrap freshness.

## Why It Matters

Agent harnesses are high-value supply chain targets — they run with user permissions, access code, execute commands. A compromised dependency in an agent CLI tool could exfiltrate secrets, inject malicious code, or tamper with the agent's behavior. Standard npm best practices (semver ranges, auto-install scripts) are insufficient for this threat model.

## How It Could Fail

- Exact-pinning creates maintenance burden (manual updates)
- min-release-age delays legitimate security patches
- Shrinkwrap must be regenerated on every dep change (can drift)
- Allowlist for lifecycle scripts requires judgment about what's safe

## Evidence

Pi agent harness (earendil-works/pi) — `.npmrc` with `save-exact=true` and `min-release-age=2`, `scripts/generate-coding-agent-shrinkwrap.mjs`, pre-commit hook in `.husky/pre-commit`, `AGENTS.md` documenting the policy. Install command: `npm install --ignore-scripts`.

## Extraction Note — 2026-05-24
Extracted as **skill**: [[supply-chain-hardening-for-agent-packages]] in `extracts/skills/`
