---
name: "Skills-Lock for Portable Agent Skills"
summary: "A lock file pattern (skills-lock.json) for managing shared agent skills across repositories. Managed by a CLI tool (npx skills), supports project vs global install targets, detects conflicts (skills in both locations), prevents silent overwrites between checkouts, verifies installed skills against the lock, and supports branch testing via environment variable."
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "supply-chain-hardening-for-agent-packages.md"
    rel: "same-problem"
  - file: "core-specialized-skill-inheritance-pattern.md"
    rel: "enables"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
pipeline_status: "synthesized"
consumed_by:
  - "designing-agent-tools.md"
---

# Skills-Lock for Portable Agent Skills

## Pattern

A dependency-management-style lock file for agent skills:

**`skills-lock.json`** — records which skills are installed and their versions:
- Managed by `npx skills@<version> update -p -y`
- Committed to repo (like package-lock.json)
- Read by install scripts during bootstrap

**Install targets:**
- `--project`: Skills installed in repo's `.agents/skills/`
- `--global`: Skills installed in `~/.agents/skills/`
- Non-interactive flows MUST specify target explicitly (no silent defaults)

**Safety properties:**
- Errors if skills exist in BOTH project and global (prevents confusion)
- Prevents global install pinned to one lock from being overwritten by another checkout's lock
- Verifies installed skills against lock after install or skip
- `WARP_COMMON_SKILLS_REF=<branch>` for testing remote skill branches

**Bootstrap integration:**
- Platform setup script (`./script/bootstrap`) triggers skill installation
- `--skip-common-skills` flag to opt out
- `--if-needed` flag for idempotent re-runs

## Why It Matters

As agent skills become shared infrastructure (like npm packages), they need the same dependency management rigor: version pinning, conflict detection, reproducible installs, and safe updates. Without a lock file, skill versions drift silently between team members' machines.

## How It Could Fail

- Lock file staleness if team doesn't update regularly
- Complexity of project vs global resolution (which takes precedence?)
- Skills with side effects that aren't captured by the lock (config files, runtime state)
- Version conflicts between repos sharing a global install

## Evidence

Warp (warpdotdev/warp) — `skills-lock.json` at repo root, `warpdotdev/common-skills/scripts/install_common_skills` installer script, bootstrap integration, documented in WARP.md. Production-tested across the Warp development team.
