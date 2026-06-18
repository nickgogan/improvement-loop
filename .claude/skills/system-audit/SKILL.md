---
name: system-audit
description: >-
  Full consistency check for the IL system — agent constitutions, skill contracts,
  governance compliance, fractal pattern completeness, cross-reference integrity,
  and feedback processing status. The comprehensive version of /system-health.
  Produces a structured audit report written to operations/. Use for periodic deep
  reviews, before milestone completions, or when systemic issues are suspected.
  DD-86 Owner responsibility.
user-invocable: true
allowed-tools: Read Grep Glob Bash Write
argument-hint: ""
---

# System Audit

Comprehensive consistency check for the Improvement Loop. Examines every structural, governance, and documentation surface. The Owner agent's deep inspection skill.

## When to Use This Skill

- Periodic deep review (monthly or at milestone boundaries)
- When `/system-health` flags multiple issues and you want the full picture
- Before sharing the system with a new collaborator
- When systemic issues are suspected (multiple things feel wrong)
- Before archiving a milestone to ensure the system is clean

## When NOT to Use This Skill

- **Quick check** — use `/system-health` instead (faster, lighter)
- **Fixing specific drift** — use `/maintain-docs --update`
- **Governance translation** — use `/translate-governance`
- **Processing feedback** — use `/process-feedback`

## Available Tools

| Tool | Purpose |
|------|---------|
| `Read` | Read all documentation, definitions, and governance files |
| `Grep` | Search for cross-references, broken links, and patterns |
| `Glob` | Count and list files for structural verification |
| `Bash` | Directory listings, structural analysis |
| `Write` | Write the audit report |

## Cognitive Disposition

You are the **Owner** performing a thorough inspection. This is Full Autonomy tier — read-only analysis producing a written report.

- **Exhaustive but scannable.** Check everything, but organize findings so Nick can scan the report in 2 minutes and drill into details as needed.
- **Evidence-based findings.** Every finding includes: what was expected, what was observed, and where to look.
- **Severity classification.** Not all findings are equal. A missing agent definition matters more than a cosmetic inconsistency in a folder README.
- **No fixes in the audit.** The audit produces findings. Fixes come from other skills or manual action. Mixing audit and repair compromises both.

---

## Procedure

### Step 1: Agent Completeness

For each agent listed in CLAUDE.md's agent table:

1. **Definition exists:** `Glob` for `agents/{name}/agent.md` — does the file exist?
2. **Definition is complete:** Read the file. Does it have all required sections?
   - Constitution (Core Truths, Boundaries, Vibe, Continuity)
   - Disposition
   - Scope (In Scope, Out of Scope)
   - Autonomy Table
   - Skill Inventory
   - Communication (Input/Output artifacts, Relationships)
   - Contract (Preconditions, Invariants, Governance, Recovery)
3. **Skill inventory matches reality:** Compare skills listed in the agent's inventory against actual SKILL.md files
4. **Communication paths valid:** Verify that Input Artifact paths and Output Artifact paths exist
5. **Source DD valid:** Check that `source_dd` references an existing DD file

**Findings format:**

| Agent | Definition | Complete | Skills Match | Paths Valid | DD Valid |
|-------|-----------|----------|-------------|-------------|---------|

### Step 2: Skill Contract Integrity

For each skill in `.claude/skills/*/SKILL.md`:

1. **Frontmatter valid:** Has `name`, `description`, `user-invocable`, `allowed-tools`
2. **Mapped to an agent:** Does some agent's skill inventory list this skill?
3. **Referenced paths exist:** `Grep` the skill for file paths — do they exist?
4. **Procedure references valid tools:** Are the tools mentioned in the procedure a subset of `allowed-tools`?
5. **Autonomy compliance:** Does the skill's stated autonomy tier match the Owner's autonomy table for that action type?

**Findings format:**

| Skill | Frontmatter | Agent Mapped | Paths Valid | Tools Valid | Autonomy |
|-------|-------------|-------------|-------------|------------|----------|

### Step 3: CLAUDE.md Accuracy

Read `CLAUDE.md` and verify every factual claim:

1. **Agent table:** Correct names, roles, dispositions, definition paths
2. **Skill tables:** Correct counts per role. Every skill listed exists. No unlisted skills.
3. **Directory table:** Every listed directory exists. No undocumented directories.
4. **Pipeline description:** Stages, skills, gates — still accurate?
5. **Hard constraints:** Still aligned with constitution and current practice?
6. **Data sources table:** Paths exist and are correct
7. **Fractal compliance table:** Accurate status for each folder

### Step 4: Governance Compliance

1. **Governance docs exist:** Does `governance/` have content beyond its folder README?
2. **Source alignment:** Run the same checks as `/translate-governance --check-only` — are translations current?
3. **Rule enforcement:** For each governance rule in `governance/`, search for evidence of compliance or violation in agent definitions and skill contracts
4. **`.claude/rules/governance.md`:** Consistent with `governance/` docs?

### Step 5: Fractal Pattern Compliance

Check against the canonical structure in `systems/improvement-loop/knowledge/reference/fractal-pattern.md`:

| Required | Path | Exists | Has Content |
|----------|------|--------|-------------|
| `app/` | `app/` | ? | ? |
| `governance/` | `governance/` | ? | ? |
| `knowledge/` | `knowledge/` | ? | ? |
| `agents/` | `agents/` | ? | ? |
| `project-management/` | `project-management/` | ? | ? |
| `operations/` | `operations/` | ? | ? |
| `archive/` | `archive/` | ? | ? |

Also check knowledge vault subdirectories: `patterns/`, `guides/`, `templates/`, `reference/`.

### Step 6: Cross-Reference Integrity

1. **Handoff protocol:** Read `agents/handoff-protocol.md` (or `il-agent-handoff-protocol.md`). Verify it references current agents and current artifact paths.
2. **DD references:** `Grep` for `DD-` references across all IL files. Verify each referenced DD exists.
3. **IB references:** `Grep` for `IB-` references. Verify each exists and note status (open vs. closed).
4. **Inter-file links:** `Grep` for markdown links (`](`) and wiki-links (`[[`). Spot-check that targets exist.

### Step 7: Feedback Processing Status

1. Read `feedback/` — are there unprocessed items?
2. For processed items (with `triage_status`), are the proposed actions taken?
3. Are there systemic patterns across feedback items?

### Step 8: Recent History

Read the 10 most recent SL entries in `operations/system-log/`:
1. Are there unresolved follow-ups?
2. Do recent changes correlate with drift found in earlier steps?
3. Are there SL entries that should have triggered governance updates?

### Step 9: Produce Audit Report

Write the report to `systems/improvement-loop/operations/audit-reports/{date}-system-audit.md`:

```markdown
---
title: "IL System Audit — {date}"
type: "audit-report"
target_system:
  - "improvement-loop"
created: "{YYYY-MM-DD}"
author: "agent"
tags:
  - "audit"
  - "system-health"
---

# IL System Audit — {date}

## Executive Summary

- **Overall status:** {Clean | {N} findings}
- **Critical findings:** {N}
- **Warnings:** {N}
- **Info:** {N}

## Findings by Category

### Agents
{table and details from Step 1}

### Skills
{table and details from Step 2}

### CLAUDE.md
{findings from Step 3}

### Governance
{findings from Step 4}

### Structure
{table from Step 5}

### Cross-References
{findings from Step 6}

### Feedback
{findings from Step 7}

### Recent History
{findings from Step 8}

## Prioritized Remediation

| # | Finding | Severity | Fix Via | Effort |
|---|---------|----------|---------|--------|
| 1 | {description} | Critical/Warning/Info | {skill or manual} | Low/Med/High |

## Comparison with Previous Audit

{If a previous audit report exists, compare: what was fixed? What's new? What persists?}
```

### Step 10: Create `operations/audit-reports/` if Needed

If the directory doesn't exist, create it.

---

## Rules

1. **Autonomy tier: Full Autonomy.** Read-only analysis producing a written report. The audit does not fix anything.
2. **Write the report.** Unlike `/system-health` (conversation-only), this skill writes a persistent audit artifact.
3. **Severity classification is mandatory.** Every finding gets Critical (blocks work or causes data quality issues), Warning (should be fixed soon), or Info (improvement opportunity).
4. **No fixes during audit.** If you spot something obviously broken, resist the urge to fix it. Record it in the report. Mixing audit and repair is a known anti-pattern — it compromises audit completeness.
5. **Compare with prior audits.** If a previous audit report exists, compare. Persistent findings are more important than new ones.
6. **Stay in IL scope.** Audit the IL system only. Cross-system issues go in an "Out of Scope Observations" section.

## Calibration Notes

- A full audit should take 5-10 minutes of agent work. If it's taking significantly longer, scope may have expanded beyond IL.
- The first audit will have many findings — that's expected for a system that hasn't been audited before. Subsequent audits should show improvement.
- Known gaps (IB-138, IB-139 for fractal completion) should be reported as Info, not Critical — they're already tracked.
- This skill produces the most context-heavy output of all Owner skills. Keep findings concise and use tables to maximize scannability.
- The remediation table is the most actionable section. Prioritize it.
