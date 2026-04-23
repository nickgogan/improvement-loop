---
name: solicit-proposals
description: >-
  Run an IL reflection round. Check reflection freshness for each IL agent (Owner,
  Researcher, Codifier, Librarian); prompt stale agents to self-reflect using the
  shared reflection prompt; then prompt each agent to draft proposals based on
  their fresh reflection plus optional Nick-gated focus areas. Proposals land in
  governance/proposals/; accepted proposals become IB items via Owner follow-up.
  DD-86 Owner responsibility. Use when running a periodic self-improvement round
  or when Nick invokes a specific reflection + proposal cycle.
user-invocable: true
allowed-tools: Read Write Glob Grep Bash
argument-hint: "[--focus \"area1,area2\"] [--agents owner,researcher,codifier,librarian] [--force-refresh]"
---

# Solicit Proposals

An Owner-owned skill that runs a full reflection round: freshness check → reflection triggering → focus-area dispatch → proposal collection. The substrate is `agents/{name}/reflections/` for each agent; the output is proposal files in `governance/proposals/`.

## When to Use This Skill

- Periodic self-improvement round (e.g., every ~3 Owner sessions, or on a time-boxed cadence Nick decides).
- Nick explicitly invokes a reflection cycle with specific focus areas.
- After a significant system change where agent perspectives are valuable (e.g., post-migration, post-new-skill-deploy).

## When NOT to Use This Skill

- **Agent-initiated proposals:** If an agent has a proposal it wants to file independently, it writes directly to `governance/proposals/` without this skill. The skill is for Owner-orchestrated rounds.
- **System drift detection:** Use `/system-health` or `/system-audit` instead — those check for structural drift, not agent perspective.
- **Consumer-to-producer feedback:** Use `feedback/` directly — that channel is for one agent flagging gaps in another's output.

## Available Tools

| Tool | Purpose |
|------|---------|
| `Read` | Read existing reflections, agent constitutions, governance, focus-area input |
| `Write` | Write new reflections (by each agent during its self-reflection step); write proposals |
| `Glob` | Find existing reflections per agent |
| `Grep` | Check reflection freshness timestamps and focus-area fields |
| `Bash` | Directory listings, date math for freshness checks |

## Cognitive Disposition

You are the **Owner**, orchestrating a reflection round. Your role is organizer and collector — not reviewer or judge of the reflections themselves.

- **Respect the privacy convention.** Reflections are agent-private. The Owner reads them *during* a solicitation round to inform proposal drafting prompts. Do not editorialize reflection content or summarize across agents.
- **Do not gate reflections.** An agent's reflection is its own honest self-assessment; a shallow reflection is not a failure — it may be accurate. Don't push an agent to re-reflect because their reflection felt "thin".
- **Proposals, not decrees.** The skill's output is a set of Nick-gated proposal drafts. Nick decides what becomes an IB item.
- **Focus areas require Nick's gate before the round begins.** The skill refuses to run without either (a) `--focus` arguments, or (b) explicit acknowledgment that this is an open-reflection round (no focus areas).

---

## Procedure

### Step 0: Parse arguments and gate focus areas

1. Parse `$ARGUMENTS`:
   - `--focus "area1,area2"` — comma-separated focus-area list (optional)
   - `--agents owner,researcher,codifier,librarian` — which agents participate (default: all four)
   - `--force-refresh` — ignore freshness; re-reflect everyone

2. If `--focus` is present: present the focus-area list to Nick and ask for approval before proceeding. Do not skip this gate.

3. If `--focus` is absent: confirm with Nick that this is an open-reflection round (no focus areas). An open round is valid; first rounds are often open by design.

### Step 1: Reflection freshness check

For each in-scope agent:

1. `Glob` for `agents/{name}/reflections/*.md` — find existing reflections.
2. If zero reflections exist → agent is stale; needs to reflect.
3. If reflections exist → read frontmatter of most recent one:
   - If `updated` is older than 21 days OR three Owner sessions have passed since reflection → stale.
   - If `--focus` areas are a superset of the reflection's `focus_areas` → stale (focus has sharpened).
   - If `--force-refresh` is set → stale regardless.
4. Produce a per-agent status table:

```
| Agent | Fresh? | Last reflection | Action |
|-------|--------|-----------------|--------|
| owner | yes | 2026-04-15 | reuse |
| researcher | no | (none) | reflect |
| codifier | no | 2026-03-10 (stale > 21d) | reflect |
| librarian | yes | 2026-04-10 | reuse |
```

Present table to Nick.

### Step 2: Trigger reflections for stale agents

For each stale agent:

1. Load the shared reflection prompt: `.claude/skills/solicit-proposals/reflection-prompt.md`.
2. Inject `--focus` areas (if any) into the prompt's focus-area section.
3. Invoke the agent (by adopting that agent's disposition per the agent.md definition) with the prompt.
4. The agent produces a reflection file at `agents/{name}/reflections/{YYYY-MM-DD}-{name}-reflection.md`.
5. Reflection frontmatter includes: `agent`, `period_covered`, `trigger.kind: "owner-solicited"`, `focus_areas`, `source_activity`, `proposals_derived: []` (populated later), `stage: "current"`.
6. Mark prior reflections `stage: "superseded"` in their frontmatter (append-only file retention; just flag status).

If an agent refuses, errors, or produces an empty reflection:
- Log the event in the round's SL entry.
- Mark that agent as having no fresh reflection; skip its proposal step.
- Do NOT retry autonomously.

### Step 3: Collect proposals from each agent

For each agent with a fresh reflection:

1. Prompt the agent with:
   > "Based on your current reflection (`{path}`) and these focus areas (`{list}` or 'open'), draft zero or more proposals for changes that would improve you or the IL system. Proposals go to `governance/proposals/`. Frontmatter includes `derives_from_reflection: {path}`. Zero proposals is valid."
2. Agent writes proposal files.
3. For each proposal written, back-populate `proposals_derived` in the reflection's frontmatter.

**Proposal file naming:** `governance/proposals/{YYYY-MM-DD}-{agent}-{short-descriptive-name}.md`.

**Proposal frontmatter required fields (in addition to standard):**
- `derives_from_reflection: {path or null}` — path to source reflection or null if agent-initiated-outside-round
- `trigger: "owner-solicited"` | `"agent-initiated"`
- `author: "{agent}"` — which agent produced it

### Step 4: Write round SL entry

Write `operations/system-log/{YYYY-MM-DD}-solicit-proposals-round.md` capturing:

- Participating agents
- Focus areas used (or "open")
- Reflections produced (paths; linked)
- Proposals drafted (paths; linked)
- Round failures (agents that refused, errored, or produced empty reflections)
- Next steps: Nick reviews proposals; Owner files IB items for accepted ones

### Step 5: Present round summary

Output to conversation:

```
## Solicit-proposals round — {date}

**Focus areas:** {list or "open"}
**Agents participating:** {list}

### Reflections
- {agent}: {path} ({fresh|re-reflected})

### Proposals drafted
- {path} — {short description} — by {agent}

### Next
Nick reviews proposals in `governance/proposals/`. Accepted proposals become IB items via Owner follow-up.
```

---

## Rules

1. **Autonomy tier: Guarded.** Focus areas are Nick-gated up-front (Step 0); proposal acceptance is Nick-gated downstream (Step 5 instructs Nick). Intermediate steps (reflections, proposal drafting) run autonomously between the two gates.
2. **Privacy boundary enforced by disposition.** Other agents' reflections are not surfaced in any agent's proposal-drafting prompt unless Nick explicitly authorizes cross-agent reading.
3. **No coercion of reflection depth.** If an agent produces a shallow reflection, accept it. Don't prompt re-reflection because the output felt thin.
4. **Reflection prompt is immutable per-run.** The shared prompt is loaded once at Step 2; do not modify it mid-round.
5. **Sequential agent invocation (default).** Process agents one at a time. Parallel is a future optimization; keep it sequential until the baseline is calibrated.
6. **Fail soft.** One agent's reflection failure does not block other agents. The SL entry captures failures; the round continues.
7. **No IB filing inside this skill.** Proposal → IB conversion happens after Nick's acceptance, via Owner follow-up. This skill stops at proposal drafting.

## Calibration Notes

- Early rounds (first 3) typically run open (no focus areas). They establish a baseline of what each agent naturally reflects on. Focus areas come after that baseline is visible.
- Freshness threshold (21 days / 3 Owner sessions) is an initial guess. Calibrate after 5-10 rounds.
- Expect zero-proposal rounds. A round where nothing changes is a valid outcome — it means agents had no improvement insights worth filing.
- Watch for reflection fatigue: identical complaints across 3+ consecutive reflections without corresponding proposals suggests the proposal pathway is blocked. Flag to Nick.
