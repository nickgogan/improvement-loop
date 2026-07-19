---
title: "Reference Bundled Skill Scripts via ${CLAUDE_SKILL_DIR}, Never a Hard-Coded Relative Path"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "code-as-deterministic-tool-inside-skills"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "designing-agent-tools.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "authors of a packaged skill artifact that bundles one or more scripts alongside its instructions"
    - "packaged capabilities that may be invoked from a working directory other than their own directory — a project subdirectory, a different repository root, or an orchestrator-launched subprocess"
  platform_coupling: "specific:claude-code"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — rewriting a path reference to route through the resolved-skill-directory variable is a small, local edit with no migration cost beyond retesting invocation from another working directory"
  auditability: "high — bundled-script path references are lintable text; a scan for relative path literals in script-invoking instructions that don't route through the resolved-skill-directory mechanism is deterministic. Whether the fix actually behaves correctly still needs a real invocation from a non-home working directory"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A packaged skill bundles one or more scripts (executable or reference) under a scripts/ or similarly named subdirectory, and its instructions or invocation code reference those scripts by path. The skill may be invoked from a process whose current working directory differs from the skill's own directory."
  invariants: "Every reference to a bundled script's path in the skill's instructions or invocation code resolves through the platform's resolved-skill-directory mechanism (${CLAUDE_SKILL_DIR} on Claude Code) rather than a bare relative path assumed to match the invoking process's working directory. The resolved path is stable across invocations regardless of the calling process's current working directory."
  governance: "Owner: whoever authors or maintains a skill that bundles scripts. Skill-authoring guidance and any skill-linting or audit tooling should check bundled-script path references for the anchored form. Authors targeting more than one deployment surface additionally record, in the skill's compatibility declaration, whether an equivalent resolved-directory mechanism exists on each target surface."
  recovery: "If a bundled script is not found, or a different file is silently picked up, when the skill is invoked from an unexpected working directory: treat it as an authoring defect, not an environment bug; rewrite the reference to route through the resolved-skill-directory mechanism and retest invocation from a working directory other than the skill's own. If porting the skill to a surface with no equivalent resolved-directory variable: implement or document a surface-specific resolution strategy rather than assuming the Claude Code mechanism carries over unchanged."
tags:
  - "extracted-artifact"
  - "rule"
  - "skill-authoring"
  - "tool-integration"
  - "portability"
---

# Reference Bundled Skill Scripts via ${CLAUDE_SKILL_DIR}, Never a Hard-Coded Relative Path

**Source:** [[code-as-deterministic-tool-inside-skills]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A skill bundles one or more scripts (executable or reference) in a `scripts/` subdirectory or similar bundled-file location, and its SKILL.md instructions or invocation code reference those scripts by path. The skill may be invoked from a working directory other than its own — a project subdirectory, a different repository root, or an orchestrator-launched subprocess with an unrelated current working directory.

## Action

**Required:** Reference a bundled script's path using `${CLAUDE_SKILL_DIR}` (Claude Code's resolved-skill-directory environment variable, or the equivalent platform-provided mechanism where one exists) so the resolved path is anchored to the skill's own directory, independent of the invoking process's current working directory.

**Forbidden:** Hard-coding a bundled script's path as a bare relative reference (e.g., `scripts/foo.py`) whose correctness depends on the invoking process's working directory happening to match the skill's own directory.

## Boundary

Enforced at skill-authoring time — when SKILL.md or its invocation code is written — and reviewable at audit time: any bundled-script path reference that doesn't route through the resolved-skill-directory mechanism is a candidate flag. Scoped to Claude Code specifically: `${CLAUDE_SKILL_DIR}` is that platform's own resolved-directory variable. A skill targeting additional surfaces needs a surface-appropriate equivalent, or an explicit declaration that the surface lacks one; this rule's mechanism does not port unchanged.

## Enforcement

- **Mechanism:** Lint or grep every SKILL.md and any script-invocation code for bundled-script path literals that don't include `${CLAUDE_SKILL_DIR}` (or a documented platform equivalent). Flag bare relative paths pointing into the skill's own bundled-file directory.
- **Check (deterministic):** For each bundled script path reference: `path is anchored via ${CLAUDE_SKILL_DIR} (or a documented platform equivalent) OR path is otherwise anchored to the skill's own directory regardless of CWD`. False → violation.
- **Violation response:** Rewrite the hard-coded relative path to the anchored form; verify the skill executes correctly when invoked from a working directory other than the skill's own before considering the fix complete.
- **Cannot be self-certified by code inspection alone when porting cross-surface:** a path resolving correctly on Claude Code because `${CLAUDE_SKILL_DIR}` is defined there does not confirm the same skill works on a surface lacking that variable. Cross-surface skills need either a surface-conditional resolution strategy or an explicit declared dependency on the Claude Code mechanism.

## Rationale

A relative path reference silently assumes the invoking process's working directory matches the skill's own directory. That assumption holds when a skill happens to be invoked from its home directory, and breaks the first time it runs from a project subdirectory, a different repository, or an orchestrator subprocess with an unrelated CWD. The failure surfaces at the worst possible time — a bundled script silently not found, or worse, a different file at that same relative location silently picked up instead — rather than at authoring time when it would be cheap to catch. `${CLAUDE_SKILL_DIR}`, where the runtime resolves and sets it, decouples the script's location from wherever the calling process happens to be running, making path resolution correct by construction instead of correct by accident of invocation context.

## Failure Modes

- **Authored and tested only from the skill's home directory.** The skill works throughout development because the author always invokes it from the same place the scripts live. It breaks the first time it's invoked from an unrelated CWD. Mitigation: test invocation from a working directory other than the skill's own before considering the skill done.
- **Cross-surface porting assumes `${CLAUDE_SKILL_DIR}` exists everywhere.** A target surface without an equivalent resolved-skill-directory variable either leaves the bundled script unreachable or silently falls back to CWD-relative resolution. Mitigation: treat the variable as Claude-Code-specific; implement or document an equivalent for other target surfaces, or declare the dependency explicitly in the skill's compatibility metadata.
- **Silent wrong-file pickup.** A bare relative path like `scripts/foo.py` can resolve to some unrelated file that happens to exist at that relative location from the actual CWD, rather than failing loudly with a not-found error. Mitigation: prefer a resolution mechanism that fails loudly on a genuine miss; anchoring the path removes the ambiguity that makes silent wrong-file pickup possible in the first place.
