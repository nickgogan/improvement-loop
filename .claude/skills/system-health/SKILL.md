---
name: system-health
description: >-
  Drift detection — compare documented intent vs observed state across the IL
  system. Reads agent constitutions, skill contracts, CLAUDE.md, governance docs,
  and recent SL entries, then compares against actual file structure and cross-references.
  Produces a scannable drift report. Use for quick system checks, after structural
  changes, or as a pre-flight before major work. DD-86 Owner responsibility.
user-invocable: true
allowed-tools: Read Grep Glob Bash
argument-hint: "[--focus agents|skills|governance|structure|all]"
---

# System Health

Quick drift detection for the Improvement Loop. Compares what documentation says against what the filesystem shows. The Owner agent's diagnostic skill.

## When to Use This Skill

- Quick system check before starting a session
- After structural changes to verify nothing was missed
- When something "feels off" and you want a diagnostic
- As pre-flight before running `/system-audit` (which is more comprehensive)
- When a collaborator asks "is the IL system in good shape?"

## When NOT to Use This Skill

- **Full consistency audit** — use `/system-audit` instead
- **Fixing drift** — use `/maintain-docs --update` to fix what this skill finds
- **Governance alignment** — use `/translate-governance --check-only` for governance-specific drift
- **Processing feedback** — use `/process-feedback`

## Available Tools

| Tool | Purpose |
|------|---------|
| `Read` | Read documentation files and agent/skill definitions |
| `Grep` | Search for cross-references, counts, and specific terms |
| `Glob` | Count and list files to compare against documented counts |
| `Bash` | Directory listings, file counts, structural checks |

## Cognitive Disposition

You are the **Owner** running a diagnostic. This is Full Autonomy tier — read-only analysis.

- **Report state as it is.** Don't editorialize. "CLAUDE.md says 12 Researcher skills; filesystem has 11" is a fact, not a judgment.
- **Scannable output.** The drift report should take 30 seconds to read. Use tables and status indicators.
- **Prioritize actionable drift.** A missing skill directory matters more than a slightly outdated timestamp.
- **Don't fix — detect.** This skill's job is diagnosis. Fixes come from `/maintain-docs` or manual action.

---

## Procedure

### Step 0: Determine Focus

Parse the `--focus` argument:

| Focus | What to check |
|-------|--------------|
| `agents` | Agent definitions vs reality |
| `skills` | Skill contracts and counts vs reality |
| `governance` | Governance docs vs source governance |
| `structure` | Fractal pattern compliance |
| `all` (default) | Everything |

### Step 1: Skill Count Check

1. `Glob` for `.claude/skills/*/SKILL.md` — count actual skill files
2. Read `CLAUDE.md` — extract documented skill counts per agent role
3. Read each `agents/*/agent.md` — extract skill inventory counts
4. Compare: do CLAUDE.md counts = agent.md counts = filesystem counts?

**Output per agent role:**

| Role | CLAUDE.md says | agent.md says | Filesystem has | Status |
|------|---------------|---------------|----------------|--------|
| Researcher | ? | ? | ? | Aligned / Drifted |
| Codifier | ? | ? | ? | Aligned / Drifted |
| Owner | ? | ? | ? | Aligned / Drifted |
| Librarian | ? | ? | ? | Aligned / Drifted |

### Step 2: Agent Definition Check

For each agent in `agents/`:
1. Read `agent.md` — extract scope, skill inventory, communication tables
2. Verify skills listed in inventory actually exist as SKILL.md files
3. Verify communication table paths (input/output artifacts) exist
4. Check that agent's `source_dd` references a valid DD file

### Step 3: Governance Alignment Check

1. Read `governance/` files — note their `source_governance` and `updated` dates
2. Read the referenced source files — note their `updated` dates
3. If source is newer than translation: flag as potentially drifted
4. If `.claude/rules/governance.md` references concepts not covered in `governance/`: flag gap

### Step 4: Structural Check (Fractal Pattern)

Compare IL directory structure against the fractal pattern:

| Required Folder | Exists? | Contents? |
|----------------|---------|-----------|
| `app/` | ? | ? |
| `governance/` | ? | ? |
| `knowledge/` | ? | ? |
| `agents/` | ? | ? |
| `project-management/` | ? | ? |
| `operations/` | ? | ? |
| `archive/` | ? | ? |

Also check:
- Are there top-level files that should be in a subdirectory?

### Step 5: Recent SL Entries Check

Read the 5 most recent entries in `operations/system-log/`. Look for:
- Unresolved issues or follow-ups
- Changes that might have created drift
- Patterns of recurring problems

### Step 6: Produce Report

Output to conversation (not written to file — this is a diagnostic):

```markdown
## IL System Health Report — {date}

### Overall: {Healthy | {N} issues detected}

### Skill Counts
{table from Step 1}

### Agent Definitions
{findings from Step 2}

### Governance
{findings from Step 3}

### Structure
{table from Step 4}

### Recent SL Items
{findings from Step 5}

### Recommended Actions
1. {action} — fix via {skill or manual}
2. {action} — fix via {skill or manual}
```

---

## Rules

1. **Autonomy tier: Full Autonomy.** This is a read-only diagnostic. No writes, no proposals, no fixes.
2. **Output to conversation only.** Don't write report files — this is a quick check, not an audit artifact.
3. **Be specific about drift.** "Skills drifted" is useless. "CLAUDE.md says 12 Researcher skills but filesystem has 11 — missing: dimension-rebalance" is actionable.
4. **Don't flag cosmetic issues.** Minor doc typos are not health issues. Focus on structural, count, and reference accuracy.
5. **Stay in scope.** Only check IL system state. If you notice issues in other systems, ignore them — the Owner's scope is IL only.

## Calibration Notes

- This is the "quick check" complement to `/system-audit`. It should complete in under 2 minutes of conversation.
- The most common drift after a skill-building session: CLAUDE.md skill counts and agent.md skill inventories not updated.
- Governance alignment drift is expected after MetaSystem governance updates — flag it and recommend `/translate-governance`.
- Fractal pattern gaps (missing `app/`, `archive/`) are known (IB-138, IB-139) — report them but note they're tracked IB items.
