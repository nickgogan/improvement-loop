---
name: "Capability-Restricted Agent Spawning via Allowlist Syntax"
summary: "When an agent runs as the main thread with `claude --agent`, it can spawn subagents via the Agent tool. You can restrict WHICH subagent types it may spawn by declaring `tools: Agent(worker, researcher)` in its frontmatter — only those specific subagents can be invoked. Plain English: the main-thread agent gets a list of which subagents it's allowed to call, just like other tool allowlists. An unauthorized spawn attempt fails silently and the agent sees only the allowed types."
implementation_notes: "Syntax: `Agent(worker, researcher)` is an allowlist; `Agent` (no parens) allows any subagent; omitting `Agent` from tools entirely denies all subagent spawning. Only applies to agents running as the main thread; subagents can't spawn other subagents regardless."
category: "Governance"
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
  - file: tiered-permission-system-bash-safety.md
    rel: same-problem
  - file: tool-gateway-security-boundary.md
    rel: same-problem
  - file: agent-identity-governance-enforcement-layer.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-24"
pipeline_status: classified
consumed_by: []
---

## What It Is

A tools-field syntax in Claude Code subagent frontmatter that restricts which other subagent types the agent may spawn. Three configurations:

| Syntax | Effect |
|---|---|
| `tools: Agent(worker, researcher), Read, Bash` | Allowlist — can spawn only `worker` and `researcher` |
| `tools: Agent, Read, Bash` | Unrestricted — can spawn any subagent |
| `tools: Read, Bash` (no `Agent`) | Denied — cannot spawn any subagents |

Three behavioral properties:

1. **Allowlist, not denylist.** Listing types permits only those; everything else is blocked.
2. **Silent block with visible types.** Attempted spawn of a non-allowed type fails; the agent sees only the allowed types in its prompt, not the existence of others.
3. **Scope: main-thread only.** Only applies to agents running as `claude --agent <name>`. Subagents spawned through the normal Task/Agent tool cannot spawn other subagents regardless.

Compatible with `permissions.deny` in settings.json to block specific subagents at a different layer — the allowlist constrains what an agent *may* spawn; the deny list constrains what any agent *can* spawn globally.

## Why It Matters

Agent composability with guardrails. Coordinator agents often orchestrate worker agents to parallelize or specialize. Without allowlist syntax, a coordinator has access to every subagent on the system — including subagents that produce destructive writes, call expensive APIs, or carry security-sensitive tool access. The allowlist makes the coordinator's capability surface declarative: you can read its frontmatter and know exactly what it can spawn.

For MetaSystem:
- **Owner subagent orchestration.** If Owner ever calls Researcher/Codifier/Librarian as subagents (currently it doesn't — IL agent architecture is file-mediated), the `Agent(researcher, codifier, librarian)` allowlist would make the delegation graph explicit and auditable.
- **Hierarchical pipelines.** A plan-phase agent that orchestrates implementer agents benefits from declaring which implementers it can call — a whitelist analogue to role-based access control.
- **Security-sensitive workflows.** An agent that operates on untrusted input should NOT be able to spawn a subagent with write/edit tools. The allowlist makes this enforcement declarative.
- **Composes with [[tool-gateway-security-boundary]] and [[tiered-permission-system-with-destructive-command-safety-architecture]].** All three are governance primitives for capability scoping. This one specifically targets the agent-spawning axis.

The pattern inherits from well-established capability-based security models (object capabilities, SELinux labels) applied to agent orchestration.

## Why People Are Using It

Documented canonically at [Anthropic's Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents) — see [[anthropic-claude-code-subagents-docs]] for the source. Canonical example from the docs:

```yaml
---
name: coordinator
description: Coordinates work across specialized agents
tools: Agent(worker, researcher), Read, Bash
---
```

Anthropic's stated design rationale: the allowlist gives orchestrators bounded capability; unauthorized spawn attempts fail cleanly rather than invoking arbitrary system subagents. The `Note` on subagents-can't-spawn-subagents is a deliberate design choice to prevent infinite nesting and bound the recursive depth of any agentic call tree at one level.

The pattern is new (2026 Claude Code update); adoption-in-the-wild is early.

## Potential Alternatives

- **Unrestricted spawning.** Any agent can spawn any subagent. Maximum flexibility; minimum control. Default if Agent tool is present without parens.
- **Per-subagent explicit invocation** (`@worker-agent`). User controls which subagent runs; the main agent doesn't spawn autonomously. Different orchestration model; doesn't scale for complex pipelines.
- **Deny list at settings level.** `permissions.deny: ["Agent(bad-agent)"]`. Session-wide; coarser grain; orthogonal to per-agent allowlists.
- **Runtime permission prompts.** User approves each spawn. Interactive; interrupts flow; doesn't scale for long-running orchestration.
- **Capability token passing.** Coordinator receives tokens for specific subagents at invocation; tokens are scoped and revocable. More complex; more flexible; not natively supported.

## Potential Improvements

- **Typed capability inheritance.** A subagent's `Agent(...)` restrictions should propagate to any child orchestration contexts it creates. Prevents escalation through delegation.
- **Introspection tool.** An agent can query which subagent types it's authorized to spawn before attempting to spawn them. Reduces failed-attempt noise.
- **Audit log.** All spawn attempts (successful and blocked) logged with agent identity and target subagent. Enables security review post-hoc.
- **Compose with `permissionMode`.** If an agent is in `bypassPermissions` mode, allowlisting still applies — bypassing permissions shouldn't bypass capability restrictions.
- **Delegation policies.** Beyond "can spawn X," richer policies like "can spawn X, but only with max-turns ≤ 10" — bounds resource consumption per delegation.

## Potential Failure Modes

- **Allowlist staleness.** Coordinator lists 5 subagents; one gets renamed; coordinator's spawn attempts to the old name fail silently. Mitigation: rename-with-alias support; version-pin subagent names in allowlists.
- **Silent failures confusing the orchestrator.** "Spawn X" fails, agent doesn't know why, retries other approaches. Mitigation: clear error surfaced to the agent explaining the capability restriction.
- **Over-permissive defaults.** `tools: Agent` (no parens) is easy to write and disables the protection. Mitigation: linter / meta-skill that flags unrestricted Agent tools in coordinators.
- **Circular spawning via indirection.** Agent A allowed to spawn B; B's allowlist includes C; C's allowlist includes A — creates an indirect recursion path. Prevented today by "subagents can't spawn subagents" rule, but if that constraint loosens, cycle detection becomes necessary.
- **Escalation via plugin install.** Plugin installs a subagent named `worker` that coordinator's allowlist permits; plugin's worker has broader capabilities than expected. Mitigation: plugin subagents have their own capability cap (cannot set hooks/mcpServers/permissionMode); coordinator trust still requires vetting.
