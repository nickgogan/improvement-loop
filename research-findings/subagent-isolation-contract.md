---
name: "Subagent Isolation Contract: Fresh Context, Explicit Skills, No Nesting"
summary: "Claude Code subagents honor a strict isolation contract: fresh context window at spawn (no parent conversation history), explicit skill preloading required (no automatic inheritance from parent), and no subagent-can-spawn-other-subagents (nesting prevented by design). What the subagent sees is exactly what its frontmatter declares plus basic environment. Plain English: a subagent isn't a subset of its parent. It's a separate assistant with its own context and its own tools. If you want it to have something, put it in the frontmatter."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Strong (documented, first-party Anthropic canonical spec)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "anthropic-claude-code-subagents-docs.md"
related_findings:
  - file: inline-scoped-mcp-servers-per-subagent.md
    rel: same-problem
  - file: capability-restricted-agent-spawning-via-allowlist.md
    rel: same-problem
  - file: subagent-persistent-memory-directory.md
    rel: same-problem
  - file: agent-architecture-layer-impermanence.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-24"
pipeline_status: classified
consumed_by: []
---

## What It Is

A three-part isolation contract that Claude Code enforces on every subagent invocation:

1. **Fresh context window.** The subagent starts with only its own system prompt (from frontmatter body) plus basic environment details (working directory, etc.). It does NOT inherit the parent's conversation history, tool results, or any accumulated context.
2. **Explicit skill preloading.** Skills are available to a subagent only if listed in the `skills:` frontmatter field. The full skill content is injected at startup. Subagents do NOT inherit skills from the parent conversation. Missing or disabled skills are skipped with a warning.
3. **No recursive spawning.** Subagents cannot spawn other subagents. If your workflow needs nested delegation, you must use Skills or chain-from-main-thread patterns. Infinite-nesting is prevented by design.

Corollaries of this contract:

- Skills available in the main session (e.g., `/research-loop`, `/identify-artifacts`) must be re-declared in the subagent's `skills` field if the subagent needs them.
- A subagent's `cd` commands don't persist between Bash calls and don't affect the parent's working directory.
- Working directory inheritance exists (subagent starts in parent's cwd) but is the only parent state that crosses the boundary.
- `isolation: worktree` frontmatter makes the subagent run against a temporary git worktree — even the shared filesystem boundary is severed.

## Why It Matters

The isolation contract is the architectural backbone that makes subagents usable for their core purpose: context preservation. If subagents inherited parent context, they wouldn't solve the token-budget problem they exist to solve. If they could spawn nested subagents, the recursion depth would be unbounded and unreasonable to reason about. If they inherited skills, their tool surfaces would depend on what the parent happened to invoke — non-deterministic behavior.

For MetaSystem:
- **IL agent architecture alignment.** The IL's four agents (Owner, Researcher, Codifier, Librarian) are currently file-mediated, not Claude-Code-subagent-mediated. If they ever become subagents, the isolation contract dictates that each needs explicit skills declaration (Researcher: 12 skills; Codifier: 4 skills; Owner: 6 skills; Librarian: 0 skills currently). File-mediated handoffs are IL's way of respecting the same isolation principle without the Claude Code subagent mechanism.
- **Skill discoverability vs. isolation tradeoff.** Skills auto-discover in a main session (Claude sees descriptions); in subagents, all content is loaded upfront. Trade: subagent has full skill content immediately but pays the token cost at startup.
- **Design discipline transfer.** The "explicit declaration required" pattern generalizes beyond subagents — any capability-scoped component (a Librarian invocation with specific context, a `/research-query` instance with particular sources) benefits from the same isolation-by-default posture.

The pattern is deeply related to [[agent-architecture-layer-impermanence]]: impermanent things get explicit, versioned, re-declarable contracts. Subagents don't get to "inherit" because their parent's context is impermanent; explicit re-declaration is the durability mechanism.

## Why People Are Using It

Documented canonically at [Anthropic's Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents) — see [[anthropic-claude-code-subagents-docs]] for the source. Key quotes from the docs:

- On fresh context: *"Subagents receive only this system prompt (plus basic environment details like working directory), not the full Claude Code system prompt."*
- On explicit skills: *"Subagents don't inherit skills from the parent conversation; you must list them explicitly."*
- On no nesting: *"Subagents cannot spawn other subagents. If your workflow requires nested delegation, use Skills or chain subagents from the main conversation."*

The design choices are stated affirmatively ("this is how it works") rather than as warnings ("don't do X"). Anthropic treats the isolation contract as a foundational property, not an opt-in discipline.

## Potential Alternatives

- **Context inheritance.** Subagent gets the full parent conversation. Loses the main token-saving benefit; also couples subagent behavior to parent state.
- **Partial inheritance** (recent N turns, or specific summary). Middle ground; implementation complexity high; non-determinism risk.
- **Skill broadcast.** Parent conversation's active skills propagate to subagents automatically. Easier for user; harder to reason about what's in scope.
- **Recursive spawning with depth limits.** Subagents spawn subagents up to depth K. More composable; harder governance; quickly intractable.
- **Ambient capabilities.** Parent grants capabilities to subagent dynamically at spawn time. More flexible than frontmatter declaration; requires runtime capability-passing protocol.

## Potential Improvements

- **Explicit "include parent context" opt-in.** For the specific case where parent context IS needed (e.g., conversational continuity), an opt-in import mechanism with size budget. Preserves default isolation; enables exceptional cases.
- **Skill-bundle references.** Instead of listing 12 skills individually, reference a skill-bundle file. Reduces frontmatter duplication.
- **Parent-state snapshot on spawn.** A one-line summary of the parent's purpose attached to the subagent's startup — not full history, just a breadcrumb. Preserves isolation; reduces "why was I spawned" confusion.
- **Spawn-time skill resolution.** Allow `skills: $SESSION_SKILLS` to inherit parent skills at spawn time (resolved once, not dynamic). Compromise between explicit and inheriting.
- **Isolation violation telemetry.** Log any cases where subagent behavior correlates with parent context — could be a sign the isolation contract has edge-case leakage.

## Potential Failure Modes

- **Orphaned knowledge.** Subagent doesn't know facts the parent discovered in the same session. User has to re-state context every spawn. Mitigation: encode re-usable knowledge in skills or memory; don't rely on cross-spawn implicit sharing.
- **Skills declaration drift.** Skill added/removed from project without updating subagents that declared them. Subagent silently loses or keeps stale skill. Mitigation: linter / audit that checks subagent skill declarations against actual skill inventory.
- **Token cost surprise.** Six skills preloaded = 6× the skill content in the subagent's startup context. Can exceed budgets for large skills. Mitigation: per-skill size warnings; tiered loading.
- **No-nesting as a forcing function.** Complex workflows that WOULD benefit from depth-2 orchestration must be flattened into Skills or main-thread-chained patterns. Adds implementation complexity in specific cases. Mitigation: document the common flattening patterns so developers don't reinvent them.
- **`isolation: worktree` costs.** Git worktrees are not free — setup latency, disk usage. Overuse bloats session resource consumption. Mitigation: opt-in only when the subagent truly needs filesystem isolation.
