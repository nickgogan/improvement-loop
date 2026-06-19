---
name: maintain-docs
description: >-
  Two modes: update (detect drift between docs and reality, refresh existing
  documentation) and create (interview the user to produce new docs from scratch
  when none exist). Covers CLAUDE.md, agent definitions, skill contracts, knowledge
  docs, and operational references. Use when docs feel stale, after structural
  changes, or when a new area needs documentation. DD-86 Owner responsibility.
user-invocable: true
allowed-tools: Read Grep Glob Write Edit
argument-hint: "--update | --create [target]"
---

# Maintain Docs

Detect documentation drift and fix it (update mode), or interview the user to produce new documentation from scratch (create mode). The Owner agent's documentation maintenance skill.

## When to Use This Skill

- After structural changes (new agents, skills, directories) to update CLAUDE.md and indexes
- When a `/system-health` or `/system-audit` report flags documentation drift
- When the user wants to document a new area of the system that has no docs
- Periodically to verify docs still match reality
- When onboarding a new collaborator who needs accurate documentation

## When NOT to Use This Skill

- **Writing research findings** — that's Researcher's domain
- **Creating governance translations** — use `/translate-governance`
- **Proposing structural changes** — the Owner proposes those directly, not through a docs skill
- **Creating DDs or IB items** — those have their own governance processes

## Available Tools

| Tool | Purpose |
|------|---------|
| `Read` | Read current docs and system state files |
| `Grep` | Search for references, counts, and cross-references |
| `Glob` | Find files by pattern to verify documented structure |
| `Write` | Create new documentation files |
| `Edit` | Update existing documentation |

## Cognitive Disposition

You are the **Owner** — maintaining documentation as a system steward.

- **Reality is the spec.** When docs contradict the filesystem, the filesystem wins. Update the docs, don't pretend reality is wrong.
- **Precision over prose.** A table with correct counts and paths is worth more than a paragraph describing the general idea.
- **Interview with purpose.** In create mode, ask focused questions that produce structured docs. Don't ask open-ended questions that produce rambling narrative.
- **Minimal viable documentation.** Document what agents and humans need to find things and understand boundaries. Don't document what's obvious from reading the code.

---

## Procedure: Update Mode (`--update`)

### Step 1: Determine Scope

If a target is specified (e.g., `--update CLAUDE.md`, `--update agents`), scope to that area. Otherwise, check all documentation surfaces:

| Surface | File(s) | What to verify |
|---------|---------|---------------|
| System CLAUDE.md | `CLAUDE.md` | Agent table, skill tables, directory table, hard constraints, data sources |
| Agent definitions | `agents/*/agent.md` | Skill inventories, scope, communication tables |
| Skill contracts | `.claude/skills/*/SKILL.md` | Tools listed, procedures, paths referenced |
| Governance docs | `governance/*.md` | Aligned with current source governance |
| Operational refs | `operations/references/*.md` | Still accurate |

### Step 2: Read Current Documentation

For each surface in scope, read the document.

### Step 3: Read Actual System State

For each surface, read the actual filesystem state:

- **Skill tables:** `Glob` for `.claude/skills/*/SKILL.md` — count them, list them
- **Agent table:** `Glob` for `agents/*/agent.md` — count them, list them
- **Directory table:** `ls` equivalent via `Glob` for top-level directories
- **Cross-references:** `Grep` for paths, filenames, and counts mentioned in docs

### Step 4: Produce Drift Report

For each surface, compare documented state vs. actual state:

```markdown
## Documentation Drift Report — {date}

### {Surface Name}
- **Status:** Aligned | Drifted | Missing
- **File:** {path}
- **Issues:**
  - {specific drift: "Says N skills, actually M"}
  - {specific drift: "References path/that/moved.md"}
  - {specific drift: "Missing entry for new-agent"}
```

### Step 5: Apply Fixes

For drifted documentation:

1. **Counts and lists:** Fix directly via `Edit`. These are Guarded tier — act then report.
2. **Structural descriptions:** Fix directly if the change is factual (a directory exists that isn't listed). Propose if the description needs rewriting.
3. **Cross-references:** Fix broken paths. Flag if the referenced artifact is missing (not just renamed).
4. **Missing documentation:** Flag as a gap. Don't create new docs in update mode — that's what create mode is for.

### Step 6: Report

Output what was fixed and what needs human attention:

```
## Docs Update Complete

**Surfaces checked:** {N}
**Fixes applied:** {list of edits}
**Gaps flagged:** {list of missing docs that need create mode}
**No action needed:** {list of aligned surfaces}
```

---

## Procedure: Create Mode (`--create [target]`)

### Step 1: Determine What to Document

If a target is specified (e.g., `--create knowledge-guide`, `--create system-overview`), scope to that. Otherwise, identify gaps:

1. Read `CLAUDE.md` — are there areas described but not documented?
2. Read `governance/_index.md` — any gaps noted?
3. Read agent definitions — any agents without adequate context docs?
4. Check `knowledge/` — does this system have any knowledge docs?

Present the gaps and ask the user which to create first.

### Step 2: Interview

For the selected target, ask focused questions. Tailor to the document type:

**System Overview Doc:**
1. What is the system's primary purpose in one sentence?
2. Who operates it? (humans, agents, both)
3. What are the inputs and outputs?
4. What are the key constraints or boundaries?
5. What changed recently that prompted this documentation need?

**Knowledge Guide:**
1. What process or workflow does this guide cover?
2. Who is the audience? (agents, humans, both)
3. What are the steps in the process?
4. What are the common mistakes or failure modes?
5. Are there existing examples or prior art to reference?

**Operational Reference:**
1. What data or configuration does this document?
2. How often does it change?
3. Who updates it?
4. What breaks if it's wrong?

Ask all relevant questions in a single message. Don't drip-feed one question at a time.

### Step 3: Draft Document

Based on the answers, draft the document with:
- Proper frontmatter (per `_schema.yaml`)
- Clear structure with headers
- Tables where appropriate
- References to related docs

### Step 4: Present for Review

Present the draft to the user. This is Proposal-First tier — structural documentation shapes how agents understand the system. Wait for approval before writing.

### Step 5: Write

After approval:
1. Write the document to the appropriate directory
2. If the new doc affects CLAUDE.md references, note that for the next `--update` run

---

## Rules

1. **Update mode is Guarded tier.** Apply factual fixes (counts, lists, paths) directly. Report what changed.
2. **Create mode is Proposal-First tier.** Draft new docs and present for approval before writing.
3. **Never fabricate system state.** If you can't verify something by reading files, say "unable to verify" rather than guessing.
4. **Don't rewrite docs for style.** Update mode fixes factual errors. It doesn't rewrite prose, add commentary, or reorganize sections unless factual accuracy requires it.
5. **Preserve document ownership.** Some docs are authored by Nick. Update factual details but don't change voice or intent.
6. **Workspace-root constitutional docs are out of scope.** If drift is found in workspace-root governance (`CHARTER.md`, root `CLAUDE.md`, `.claude/rules/`), flag it but don't fix it — that's workspace law, Human-Required tier. This skill maintains engine docs under `systems/improvement-loop/`.

## Calibration Notes

- The most common drift: skill counts in CLAUDE.md and agent definitions after new skills are added. Run `--update` after any skill creation session.
- Create mode works best when Nick has a specific documentation need. Don't speculatively create docs.
- This skill complements `/translate-governance` (which maintains governance translations) and `/system-health` (which detects drift). This skill is the fix mechanism.
