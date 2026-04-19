---
title: "Poka-Yoke Error-Proof Tool Interface Design"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "poka-yoke-error-proof-tool-interfaces"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A tool interface exists that agents invoke with parameters. The tool has been used enough to identify common error classes. At least one recurring error class is caused by parameter ambiguity rather than logic errors."
  invariants: "Every tool parameter that has a known error-prone representation uses the structurally safe alternative. Structural constraints are enforced at the interface boundary, not through prompt instructions. The error-proof constraint cannot be bypassed by the calling agent."
  governance: "Tool interfaces are audited for poka-yoke opportunities when new error classes are discovered. Structural constraints are documented in the tool's schema, not in separate instructions. Changes to constraints require testing against the error class they address."
  recovery: "If a structural constraint blocks a legitimate use case, evaluate whether the constraint is too narrow. If so, widen the constraint while still preventing the original error class. Do not remove the constraint and fall back to instructional prevention."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Poka-Yoke Error-Proof Tool Interface Design

**Source:** [[poka-yoke-error-proof-tool-interfaces]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agents make systematic errors when tool interfaces allow ambiguous parameter representations. Instructions telling the agent "always use absolute paths" or "never pass null" are forgotten, misapplied, or overridden by competing context. The same error classes recur across sessions because the interface permits the error structurally, relying on the agent's memory and discipline to prevent it.

## Forces

- **Flexibility vs. error prevention:** Permissive interfaces accept a wider range of inputs but also accept common mistakes. Restrictive interfaces prevent errors but may block legitimate edge cases.
- **Prompt instructions vs. structural enforcement:** Instructions are cheap to write but unreliable -- they compete with other context for the agent's attention. Structural constraints are reliable but require interface redesign.
- **Tool design effort vs. prompt tuning effort:** Teams default to adding prompt instructions because it is faster than redesigning the tool interface. But the instruction approach creates ongoing maintenance and debugging burden.
- **Generality vs. specificity:** A tool that accepts relative and absolute paths is more general, but the generality enables an entire class of errors that a more specific interface eliminates.

## Solution

Apply manufacturing's poka-yoke (error-proofing) philosophy to agent tool interfaces: restructure parameters so that common errors are structurally impossible, rather than instructionally discouraged.

**Process:**

1. **Identify recurring error classes.** Audit tool usage logs or session transcripts for errors that recur across sessions. Focus on errors caused by parameter ambiguity (relative vs. absolute paths, optional vs. required fields, string vs. enum types).

2. **Redesign the parameter to eliminate the error.** For each recurring error class, change the interface so the error cannot be expressed:
   - Relative filepath errors → require absolute filepaths (reject inputs not starting with `/`)
   - Enum mismatches → use a closed enum type instead of free-text strings
   - Missing required context → make the parameter mandatory with validation, not optional with instructions
   - Ambiguous ordering → use named parameters instead of positional arguments

3. **Enforce at the interface boundary.** The constraint lives in the tool's schema or input validation, not in the system prompt. The agent cannot bypass it regardless of prompt content or reasoning.

4. **Prioritize tool design over prompt engineering.** Invest more time refining tool interfaces than crafting instructions. The SWE-bench team spent more time on tool refinement than prompt engineering and achieved state-of-the-art results.

**Canonical example:** Anthropic's SWE-bench agent used relative filepaths. After directory changes, models consistently produced incorrect paths. Switching to mandatory absolute filepaths -- rejected at the schema level if not absolute -- eliminated path errors entirely. No prompt changes were needed.

## Consequences

**Positive:**
- Eliminates entire classes of errors permanently -- the error literally cannot be made
- No ongoing prompt maintenance to remind the agent about the constraint
- Works across model versions and providers -- structural constraints are model-agnostic
- Shifts the reliability investment from per-session prompt tuning to one-time interface design
- Validated at scale: SWE-bench state-of-the-art results attributed partly to tool interface quality

**Negative:**
- Over-constraining tools reduces flexibility for legitimate edge cases (some tasks genuinely need relative paths or free-text inputs)
- Requires upfront analysis to distinguish "prevent common errors" from "prevent all non-standard usage"
- Interface redesign has a higher upfront cost than adding a prompt instruction
- Not all error classes are amenable to structural prevention -- logic errors within valid parameters are not addressed

## Known Uses

- Anthropic's SWE-bench agent: absolute filepath requirement eliminated path errors entirely
- Claude Code's Edit tool: requires absolute file paths, rejects relative paths at the schema level
- MetaSystem skill parameters: several skills already enforce absolute paths and required fields
- Manufacturing poka-yoke: decades of production evidence that structural error prevention outperforms training and instructions

## Contract

### Preconditions
A tool interface exists that agents invoke with parameters. The tool has been used enough to identify common error classes (at least 3-5 occurrences of the same error type). At least one recurring error class is caused by parameter ambiguity rather than logic errors within valid parameters. The tool's schema or validation layer supports the proposed structural constraint.

### Invariants
Every tool parameter that has a known error-prone representation uses the structurally safe alternative. Structural constraints are enforced at the interface boundary (schema validation, input rejection), not through prompt instructions. The error-proof constraint cannot be bypassed by the calling agent -- it is enforced before the tool executes. Instructions are never the sole prevention mechanism for a known recurring error class.

### Governance
Tool interfaces are audited for poka-yoke opportunities when new error classes are discovered or reported. Each structural constraint is documented in the tool's schema definition alongside the error class it prevents. Changes to structural constraints require testing against the original error class to confirm the error is still prevented. New tools undergo a poka-yoke review before deployment: are any parameters ambiguous in ways that will produce recurring errors?

### Recovery
If a structural constraint blocks a legitimate use case: evaluate whether the constraint is overly narrow. If so, widen the constraint to permit the legitimate case while still preventing the original error class (e.g., allow both absolute paths and explicit relative-to-cwd notation, but reject bare relative paths). Do not remove the constraint and fall back to instructional prevention -- that re-opens the error class. If the error class changes (e.g., models stop making the original error but make a new one), update the constraint to address the current error class.
