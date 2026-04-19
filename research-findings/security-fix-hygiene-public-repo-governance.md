---
name: "Security Fix Hygiene as Public Repo Governance"
summary: "n8n has explicit rules for security-related work in a public repository: neutral branch names, commit messages, test descriptions, and code comments. Never expose the attack vector or vulnerability type in any public-facing artifact. A governance pattern for open-source projects where attackers monitor repo activity."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - {file: "structural-vs-psychological-vs-economic-governance.md", rel: "extends"}
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "raw"
consumed_by: []
---

## What It Is

n8n maintains a dedicated security fix template (`.github/claude-templates/security-fix.md`) with explicit rules for how security-related work should be conducted in a public repository:

- **Branch names must be neutral** — no vulnerability type, no CVE numbers, no attack surface hints
- **Commit messages must be neutral** — describe the fix functionally, not the vulnerability
- **Test descriptions must be neutral** — test names describe expected behavior, not the exploit being prevented
- **Code comments must be neutral** — explain what the code does, not what attack it prevents
- **PR descriptions use private notes** — security context goes in private Linear tickets, not public GitHub

The core principle: "Never expose the attack vector or vulnerability type in any public-facing artifact." This is because attackers actively monitor public repositories of popular open-source projects for commit patterns that signal exploitable vulnerabilities.

## Why It Matters

In open-source projects, every commit, branch name, and PR description is public. A branch named `fix-sql-injection-in-webhook-handler` tells an attacker exactly where to look and what to try — potentially before the fix is deployed to all users. Security researchers have documented cases of "patch gap" exploitation where attackers weaponize vulnerability fixes from public commits.

This governance pattern turns security discipline into an explicit, teachable rule set — particularly relevant for AI agents that might naively name a branch after the vulnerability they're fixing.

## Why People Are Using It

Observed in [n8n](https://github.com/n8n-io/n8n) v2.16.0 — see [[n8n-analysis]] for structural details. n8n is a widely-used open-source workflow automation platform with ~100K+ GitHub stars, making it a high-value target for attackers monitoring public repositories.

## Potential Alternatives

Private security fork for all security work (more secure but harder to manage). Delayed disclosure with batched security releases (reduces window but adds coordination). Pre-commit hooks that scan for security-related keywords in branch names and commit messages (automated enforcement).

## Potential Improvements

Automated scanning for security-indicative keywords in public artifacts (branch names, commit messages, PR titles). Integration with AI agents so they follow security hygiene rules by default when working on security-tagged tickets.

## Potential Failure Modes

Overly vague commit messages that make future debugging harder ("fix edge case" tells no one anything). Security context lost when the private ticket is closed or the team member leaves. Inconsistent application — one developer follows the rules, another names the branch `fix-xss`.
