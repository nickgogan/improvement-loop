---
title: "Bash-Hook Injection-Vector Checklist"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "shell-injection-vector-taxonomy-agent-bash-security"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-safety-and-permissions.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams or individuals building agent harnesses that grant bash or shell execution capability, guarded by a command allowlist or hook"
    - "authors of a command-execution guard, hook, or middleware that inspects a command string before it runs"
    - "security reviewers auditing an existing bash-access agent's guard for completeness"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "secure"
  reversibility: "low — retrofitting enumerated vector checks into a guard that shipped with allowlist-only coverage requires redesigning the interception logic and revalidating prior sessions; damage from a bypass already exploited (arbitrary command execution) may be irreversible"
  auditability: "high when the guard module logs which named check blocked or passed a command, making vector coverage externally verifiable against the checklist; low when only an overall pass/fail result is retained without per-vector attribution"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The agentic system grants an agent bash or shell execution capability, gated by a command allowlist, hook, or equivalent guard. A point of interception exists before the command executes (hook, middleware, or shell wrapper) where the full command string can be inspected prior to execution."
  invariants: "Every proposed bash-access guard is checked against each of the following named injection-vector classes before it is trusted, not just a literal-string allowlist: (1) shell-expansion aliasing, where a shell builtin resolves a short token to the full path of a command, bypassing literal-string matching against the allowlist; (2) invisible or non-printing character insertion inside a command name, where the rendered text matches an allowed command but the underlying bytes do not; (3) field-separator or null-byte token splitting, where a blocked command name is reassembled at execution time from tokens that individually look safe; (4) parser edge cases that produce a malformed-but-executable token, of the kind surfaced through external security disclosure rather than internal design review. A guard consisting only of a pattern allowlist, with no enumerated defense against these vector classes, does not satisfy this rule."
  governance: "Owner: whoever authors or maintains a bash-access hook, guard module, or command-execution gate for an agent harness. The vector checklist is reviewed at guard-authoring time and re-reviewed whenever the guard is materially changed (new shell support, new builtin coverage, allowlist restructuring). The checklist owner tracks the disclosure or bug-bounty channel relevant to the shell(s) in scope, since the vector list is not static."
  recovery: "If an existing bash-access guard is found to omit coverage for a named vector class: treat the guard as compromised until patched — a partial fix covering only the discovered instance is not sufficient; re-check the other vector classes against the same guard. If a new vector class is discovered (via disclosure, audit, or incident): add it to the enumerated checklist, patch the guard, and re-audit every other guard module that shares the same allowlist design. If the only enforcement in place is a pattern allowlist with no vector-specific checks: escalate immediately — a bash-execution capability without enumerated vector coverage is not secure by default."
tags:
  - "extracted-artifact"
  - "rule"
  - "security"
  - "sandboxing"
  - "shell-injection"
---

# Bash-Hook Injection-Vector Checklist

**Source:** [[shell-injection-vector-taxonomy-agent-bash-security]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

An agent harness grants (or is being designed to grant) an agent bash or shell execution capability, and that capability is gated by some form of command guard — an allowlist, a hook, or middleware that inspects the command string before it runs. This rule fires whenever such a guard is proposed, authored, or materially changed.

## Action

**Required:** Before trusting any bash-access guard, confirm it defends against each of the following named injection-vector classes, not merely a literal-string allowlist:

1. **Shell-expansion aliasing** — a shell builtin resolves a short token to a command's full resolved path, bypassing an allowlist that only matches the literal command name.
2. **Invisible-character insertion** — non-printing or zero-width characters inserted inside a command name render visually identical to an allowed command but fail literal byte-matching (and can also be used the other way: to *evade* a blocklist while still executing the intended command).
3. **Field-separator / null-byte token splitting** — a blocked command name is reassembled at execution time from tokens that individually appear safe to a naive scanner.
4. **Parser edge cases** — malformed-but-executable tokens that a guard's parser fails to normalize before matching, of the kind typically surfaced through external security disclosure rather than caught in design review.

**Forbidden:** Treating a pattern allowlist (matching literal command names or fixed regexes) as sufficient bash-access defense on its own. Shipping or approving a bash-access guard without checking it against each vector class above. Assuming the vector list is closed — new vectors are discovered through ongoing disclosure, not just at initial design time.

## Boundary

Enforced at guard-authoring time: before any new bash-access hook, guard module, or command-execution gate is approved for use. Re-enforced whenever an existing guard is materially changed — new shell support added, new builtins covered, or the allowlist restructured. Applies to any shell the guard supports (the specific vector mechanics above are shell-dependent; the enumerate-don't-just-allowlist discipline is not).

## Enforcement

- **Mechanism:** The guard-authoring reviewer (human or an audit skill) checks the guard's implementation against the enumerated vector list and records which vectors are covered.
- **Check (deterministic):** `covers_shell_expansion_aliasing AND covers_invisible_character_insertion AND covers_token_splitting AND covers_parser_edge_cases`. Any term false → the guard is incomplete.
- **Violation response:** A guard missing coverage for any vector is treated as unapproved for production use until patched. The gap is documented against the checklist so the specific missing vector is traceable, not just "guard failed review."
- **Cannot be self-certified by design intent alone:** allowlist-only guards routinely look complete by inspection of their rule list; coverage must be checked against the enumerated vector classes, not against the guard author's own sense of thoroughness.

## Rationale

A pattern allowlist answers "does this command's literal text match a known-safe entry?" — but shell interpreters offer multiple ways to make a dangerous command's literal text look like something else, or make a blocked command's text reassemble only at execution time. A production-grade bash guard (the kind Anthropic ships in Claude Code's bash tool, and the kind any team building bash-access agents eventually needs) is built around an *enumerated* vector list precisely because "allowlist plus common sense" has repeatedly been defeated by exactly these mechanisms — including at least one vector found and reported through an external bug-bounty disclosure process, which is itself evidence the list evolves over time and isn't something a single design pass can close out.

The rule is deliberately framed as an enumerate-and-check discipline rather than a fixed list of forbidden strings: the specific vectors will change as shells evolve and new bypasses are found, but the obligation to check against a maintained, named list — instead of trusting an allowlist's apparent completeness — does not.

## Failure Modes

- **New vectors outpace the checklist.** The enumerated list is a point-in-time snapshot; a shell feature or parser quirk not yet catalogued can still bypass the guard. Mitigation: treat the checklist as a floor, not a ceiling, and track the relevant disclosure channel.
- **Overly aggressive blocking breaks legitimate use.** Closing every vector too bluntly (e.g., blocking all variants of a common command) can make the guard unusable for real workflows. Mitigation: scope fixes to the specific vector mechanism, not the whole command family.
- **Guard bypass via a path that skips the hook entirely.** If any execution path (a different shell, a subprocess spawn, an unguarded tool) reaches a shell without passing through the guarded interception point, vector coverage in the guard itself is moot. Mitigation: verify the guard is the sole path to shell execution, not just that the guard itself is thorough.

## Contract

### Preconditions
The agentic system grants an agent bash or shell execution capability, gated by a command allowlist, hook, or equivalent guard. A point of interception exists before the command executes (hook, middleware, or shell wrapper) where the full command string can be inspected prior to execution.

### Invariants
Every proposed bash-access guard is checked against each of the following named injection-vector classes before it is trusted, not just a literal-string allowlist: (1) shell-expansion aliasing, where a shell builtin resolves a short token to the full path of a command, bypassing literal-string matching against the allowlist; (2) invisible or non-printing character insertion inside a command name, where the rendered text matches an allowed command but the underlying bytes do not; (3) field-separator or null-byte token splitting, where a blocked command name is reassembled at execution time from tokens that individually look safe; (4) parser edge cases that produce a malformed-but-executable token, of the kind surfaced through external security disclosure rather than internal design review. A guard consisting only of a pattern allowlist, with no enumerated defense against these vector classes, does not satisfy this rule.

### Governance
Owner: whoever authors or maintains a bash-access hook, guard module, or command-execution gate for an agent harness. The vector checklist is reviewed at guard-authoring time and re-reviewed whenever the guard is materially changed (new shell support, new builtin coverage, allowlist restructuring). The checklist owner tracks the disclosure or bug-bounty channel relevant to the shell(s) in scope, since the vector list is not static.

### Recovery
If an existing bash-access guard is found to omit coverage for a named vector class: treat the guard as compromised until patched — a partial fix covering only the discovered instance is not sufficient; re-check the other vector classes against the same guard. If a new vector class is discovered (via disclosure, audit, or incident): add it to the enumerated checklist, patch the guard, and re-audit every other guard module that shares the same allowlist design. If the only enforcement in place is a pattern allowlist with no vector-specific checks: escalate immediately — a bash-execution capability without enumerated vector coverage is not secure by default.
