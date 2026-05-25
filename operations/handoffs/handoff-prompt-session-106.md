# Session 106 Handoff

## IDENTITY AND SOUL

You are operating in the **Improvement Loop** subsystem of MetaSystem. Your default disposition is **Owner** — read `agents/owner/agent.md` for the full agent definition.

**Your working relationship:** Nick gives direction; you execute with high autonomy. Present delta reports, not play-by-play. Don't show things he didn't ask for.

**Project context:** MetaSystem is an Obsidian-vault governance layer. The Improvement Loop is the research-to-codification pipeline. Session 105 completed a post-extraction health check after the largest artifact production period in IL history (sessions 102-104). The system is now consistent — all guides, back-annotations, cross-references, and routing table verified clean.

## SESSION 105 RESULTS

**Completed — health check:**
- Guide corpus: 13 active guides confirmed (was incorrectly listed as 14). G2 properly deprecated. All source_findings counts match routing table.
- G1 source_findings: 2 phantom entries removed (`stop-rules-as-agent-autonomy-limits`, `agent-constitution-soul-as-disposition-layer` — files never existed). Count corrected 11 → 9.
- G2a/G2b cross-references: 5 stale references fixed (wrong G2b title in G2a body, stale G2 refs in G2b body).
- synthesize-guide SKILL.md: 2 deprecated G2 examples updated.
- Changelogs: Created initial changelogs for G2a and G2b (missing from session 104).
- SL entry: Created `session-104-owner-g2-bifurcation.md` (missing from session 104).
- Back-annotations: 32 findings across G1/G2a/G3/G4/G5/G10/G11 repaired — consumed_by fields now point to correct guides.

**KB maintenance landscape identified:**
- 19 classified-pending findings (not yet extracted)
- 238 raw findings (not yet classified)
- LINKS.md repo intake still pending (session 88)
- 68 rules + 24 templates + 27 skills staged in extracts/ awaiting Nick's deployment

## YOUR TASK

**Owner — build Owner agent skills using Librarian + Perplexity research.**

PROGRESS.md logged-for-future item 1 says: "Create Owner agent skills: skill-assessment, skill-extraction, agent-assessment, agent-extraction. Check if these exist already."

### Step 0: Check existing coverage

Before building anything, check what already exists:
- `/assess-agent` — IL skill at `.claude/skills/assess-agent/SKILL.md`
- `/assess-prompt` — IL skill at `.claude/skills/assess-prompt/SKILL.md`
- `/assess-skill` — referenced in IL CLAUDE.md skill table (if it exists)
- Any other Owner skills that might overlap

Determine which of the 4 desired skills (skill-assessment, skill-extraction, agent-assessment, agent-extraction) are already covered, partially covered, or missing. Report the gap to Nick before building.

### Step 1: For each skill that needs building

Use this workflow:

1. **Formulate a Librarian query.** Spawn the Librarian subagent (`.claude/agents/librarian.md`) with a specific question about best practices for the skill you're building. The Librarian has read access to the entire IL KB — guides, findings, patterns. Ask it for:
   - Relevant guidance from IL guides (G1 for spec writing, G5 for tool design, G10 for agent design patterns, etc.)
   - Any findings or patterns that inform what this skill should do
   - Anti-patterns to avoid

2. **Research externally if needed.** Use Perplexity (`mcp__perplexity__perplexity_search` or `mcp__perplexity__perplexity_ask`) to research current best practices for the skill's domain (e.g., "best practices for AI agent self-assessment" or "skill extraction patterns in agentic systems").

3. **Draft the skill.** Combine Librarian KB guidance + Perplexity research + Owner system knowledge to draft the SKILL.md. Follow the existing IL skill contract format (read any existing `.claude/skills/*/SKILL.md` for the pattern).

4. **Present to Nick for approval.** Show the draft, explain design choices, wait for gate.

### Design intent

These skills should be **Owner-scoped** — they help the Owner agent assess and extract skills/agents as part of system stewardship. They are NOT the same as the Codifier's `/identify-artifacts` and `/extract-artifacts` (which work on research findings → staged artifacts). These are for:
- **assess-skill / assess-agent:** Auditing existing skill/agent definitions against IL best practices
- **extract-skill / extract-agent:** Creating new skill/agent definitions from a specification or need

Nick wants the Owner to be self-sufficient in building its own tools, using the Librarian as a knowledge partner.

## RULES

- **Read-before-acting.** Read PROGRESS.md and the relevant agent definitions.
- **Check existing skills first.** Don't build what already exists.
- **Librarian-first.** Consult the Librarian before Perplexity — the KB is the primary knowledge source. Perplexity supplements.
- **Nick gates each skill.** Present drafts for approval before writing to disk.
- **PROGRESS.md update:** Once at session end via `/session-handoff`.

## CURRENT STATE

**Extracts corpus:** 68 rules, 24 templates, 27 skills, 13 active guides — all staged in `extracts/`, none deployed.

**KB:** ~739 findings, ~179 sources, 31 watched libraries, 30 analysis docs. All 13 active guides current. System verified consistent (session 105).

## PENDING ITEMS

- **Staged artifacts awaiting deployment** — 68 rules, 24 templates, 27 skills in `extracts/` (Nick deploys manually)
- **LINKS.md repo intake** — Nick adding ~6 GH repos for watched-libraries intake (from session 88 handoff; not yet actioned)
- **19 classified-pending findings** — not yet extracted
- **IL harness aspiration** (PROGRESS.md logged-for-future item 2) — not yet actioned

## KEY REFERENCES

| Entity | Path |
|---|---|
| IL CLAUDE.md | `systems/improvement-loop/CLAUDE.md` |
| Current progress | `systems/improvement-loop/PROGRESS.md` |
| Owner agent definition | `systems/improvement-loop/agents/owner/agent.md` |
| Librarian agent definition | `systems/improvement-loop/agents/librarian/agent.md` |
| Librarian subagent | `.claude/agents/librarian.md` |
| Existing /assess-agent | `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md` |
| Existing /assess-prompt | `systems/improvement-loop/.claude/skills/assess-prompt/SKILL.md` |
| Guide G1 (Agent Specs) | `systems/improvement-loop/extracts/guides/writing-agent-specifications.md` |
| Guide G5 (Tool Design) | `systems/improvement-loop/extracts/guides/designing-agent-tools.md` |
| Guide G10 (Agent Design) | `systems/improvement-loop/extracts/guides/agent-design-patterns.md` |

## SESSION 105 TELEMETRY

```yaml
model: claude-opus-4-7[1m]
tokens_consumed: heavy (4 parallel back-annotation subagents + 3 Explore subagents)
context_window_size: 1000000
subagents: 7 (3 Explore for health check + 4 general-purpose for back-annotation)
capture_quality: estimated
harness: claude-code-cli-cursor-macos
```

## RULES

**Read-before-acting:**
- Read `PROGRESS.md` for current state
- Read the relevant agent definition for disposition
- Read the relevant SKILL.md before invoking any skill

**PROGRESS.md update:** Once at session end via `/session-handoff`.
