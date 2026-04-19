---
name: process-feedback
description: >-
  Read the feedback/ folder, triage items by blast radius and urgency, investigate
  root causes, and propose actions with autonomy tier classification. For each
  feedback class, asks whether a linter, hook, or schema could prevent recurrence.
  Produces a triage report with proposed next steps. DD-86 Owner responsibility.
user-invocable: true
allowed-tools: Read Grep Glob Write Edit
argument-hint: "[feedback-file.md]"
---

# Process Feedback

Read feedback items, investigate root causes, and propose actions. The Owner agent's continuous improvement intake skill.

## When to Use This Skill

- New items appear in `feedback/`
- Periodic review of accumulated feedback
- After a session where problems were encountered
- When a `/system-health` or `/system-audit` report references feedback items
- When the user says "process feedback" or "check feedback"

## When NOT to Use This Skill

- **System-wide diagnostics** — use `/system-health` or `/system-audit`
- **Governance drift** — use `/translate-governance --check-only`
- **Documentation updates** — use `/maintain-docs`
- **Creating feedback items** — anyone can write to `feedback/`, no skill needed

## Available Tools

| Tool | Purpose |
|------|---------|
| `Read` | Read feedback items, agent definitions, skill contracts, governance docs |
| `Grep` | Search for related issues, prior feedback, patterns |
| `Glob` | Find related files across the system |
| `Write` | Write triage reports |
| `Edit` | Update feedback items with triage status |

## Cognitive Disposition

You are the **Owner** — investigating problems with analytical rigor.

- **Root causes over symptoms.** "The skill failed" is a symptom. "The skill references a path that was renamed in session 29" is a root cause.
- **Prevention over patching.** For every issue, ask: can a structural change (hook, linter, schema, convention) prevent this entire class of problem? If yes, that's the real recommendation.
- **Blast radius matters.** A broken cross-reference in one `_index.md` is low blast radius. A wrong path in an agent's constitution is high blast radius — every invocation of that agent uses wrong context.
- **Proportional response.** Don't propose a DD for a typo. Don't propose an `Edit` for an architectural gap.

---

## Procedure

### Step 1: Read Feedback Items

If a specific file is provided, read that one. Otherwise, read all files in `systems/improvement-loop/feedback/` (excluding `_index.md`).

For each item, extract:
- What happened (the problem or observation)
- When it happened (date, session)
- Who reported it (Nick, agent, which agent)
- What system area is affected

### Step 2: Classify Each Item

For each feedback item, assign:

**Blast Radius:**

| Level | Meaning | Examples |
|-------|---------|---------|
| **High** | Affects multiple agents, sessions, or system integrity | Wrong agent constitution, broken handoff protocol, governance violation |
| **Medium** | Affects one agent or workflow | Skill procedure gap, missing edge case handling |
| **Low** | Cosmetic or isolated | `_index.md` drift, minor terminology inconsistency |

**Urgency:**

| Level | Meaning | Examples |
|-------|---------|---------|
| **Now** | Blocking current work or causing data quality issues | Skill writes to wrong directory, agent reads stale governance |
| **Soon** | Should be fixed before next major session | Drift accumulation, unclear procedures |
| **Later** | Improvement opportunity, not currently harmful | Better error messages, optional automation |

### Step 3: Investigate Root Causes

For each item (prioritized by blast radius x urgency):

1. **Read the referenced files.** Does the problem actually exist? (Feedback can be stale.)
2. **Search for related issues.** `Grep` for similar patterns — is this an isolated case or a systemic issue?
3. **Trace the chain.** If a skill failed, read the skill definition. If a path is wrong, find where it was renamed. If governance is violated, read the governance doc.
4. **Identify the root cause category:**

| Category | Description |
|----------|-------------|
| **Stale reference** | A path, count, or cross-reference wasn't updated after a change |
| **Missing procedure** | A skill or workflow doesn't cover this case |
| **Governance gap** | No rule exists for this situation |
| **Design flaw** | The current design doesn't handle this scenario |
| **Human error** | One-off mistake, not structural |
| **External change** | Something outside IL changed and IL didn't adapt |

### Step 4: Propose Actions

For each item, propose an action with autonomy tier:

| Autonomy Tier | Action Type | Examples |
|---------------|-------------|---------|
| **Full Autonomy** | Read-only investigation, append to existing logs | "Confirmed: this is a stale reference" |
| **Guarded** | Fix a reference, update a doc, create an SL entry | "Edit skill X to fix path Y" |
| **Proposal-First** | New skill, structural change, CLAUDE.md update | "Propose adding a validation step to the handoff protocol" |
| **Human-Required** | DD creation, cross-system change, architecture decision | "This needs a DD to resolve the ambiguity" |

### Step 5: Systemic Prevention Check

For each feedback item, ask and answer:

> **Can a linter, hook, or schema make this class of issue impossible?**

Examples:
- "Path references could be validated by a pre-commit hook that checks all `Read` paths exist"
- "Skill count drift could be prevented by generating counts from filesystem at session start"
- "No structural prevention possible — this requires human judgment"

Record the prevention assessment for each item.

### Step 6: Produce Triage Report

Write the report to conversation (for quick triage) or to `operations/feedback-triage-reports/{date}-triage.md` (for formal processing):

```markdown
## Feedback Triage Report — {date}

### Summary
- **Items processed:** {N}
- **High blast radius:** {N}
- **Actionable now:** {N}

### Items (sorted by blast radius x urgency)

#### {Item Title}
- **Source:** `feedback/{filename}`
- **Blast radius:** High | Medium | Low
- **Urgency:** Now | Soon | Later
- **Root cause:** {category} — {explanation}
- **Proposed action:** {action} (Autonomy: {tier})
- **Prevention:** {can a structural change prevent this class?}

### Systemic Patterns

{If multiple items share a root cause category, note the pattern.}

### Recommended Next Steps

1. {highest priority action}
2. {next action}
```

### Step 7: Update Feedback Items

For each processed item, use `Edit` to add a triage status to the frontmatter:

```yaml
triage_status: "processed"
triage_date: "{YYYY-MM-DD}"
triage_action: "{proposed action summary}"
```

---

## Rules

1. **Autonomy tier: Guarded.** Investigate and report. Apply fixes only for items clearly within Guarded tier (stale references, doc updates). Propose everything else.
2. **Don't close feedback items.** Triage them, propose actions, but don't mark them as resolved until the action is actually taken.
3. **Don't create DDs.** If a feedback item needs a DD, say so in the report. DD creation is Human-Required.
4. **Verify before reporting.** Read the actual files. Don't trust feedback descriptions alone — the issue might already be fixed.
5. **Stay in IL scope.** If feedback references other systems, flag for human routing. Don't investigate cross-system issues.
6. **Prevention is the priority output.** The most valuable part of this skill's report is the systemic prevention analysis. A fix solves one instance; prevention solves the class.

## Calibration Notes

- Empty `feedback/` is a valid state — it means no feedback has been filed. Report that and exit.
- Feedback items may not have consistent frontmatter. Some might be plain markdown notes. Handle both structured and unstructured formats.
- The prevention check is aspirational for early sessions. As the system matures, more classes of issues should have structural prevention.
- This skill feeds into `/system-audit` — unprocessed feedback is an audit finding.
