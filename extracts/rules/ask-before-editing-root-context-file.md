---
title: "Ask Before Editing the Root Context File"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "root-context-file-edit-guard"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-governance-and-trust.harvest-queue"
identification_report: "agent-governance-and-trust.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "any agent setup that loads a single root context file (a router or entry-point instruction file) into every session"
    - "teams or individuals who have noticed their root context file growing over time as small, individually-reasonable additions accumulate"
    - "operators who want an enforceable line between the root router and the detail files it points to, rather than a soft convention"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — a one-line instruction; removing it costs nothing, though undoing accumulated drift it prevented is not trivial"
  auditability: "medium — compliance is visible in the edit history of the root file (every change should trace to an explicit approval moment); an agent silently editing the file without asking is detectable after the fact via version history, but not necessarily blocked in the moment without a mechanical backstop"
  evidence_strength: "Medium"
  adoption:
    status: "Partially Adopted"
    notes: "Observed as an explicit self-describing guard line in at least one adopting workspace's root context file; the underlying social convention (no agent message authorizes root-file changes) predates the explicit written rule in that workspace."
contract:
  preconditions: "A root context file exists that is loaded into every session and that other, more detailed files point back to or are governed by. The agent has write access to that file (directly or via an edit tool)."
  invariants: "The agent asks before making any edit to the root context file and proceeds only after explicit approval. This applies regardless of how small or individually-reasonable the proposed addition looks. The rule is stated inside the root file itself, so it loads every session and cannot be silently bypassed by omission from context."
  governance: "Owner: whoever is accountable for the root context file's content and stability. The rule is self-enforcing at the instruction level (the agent reads it every session) but is a soft guard — no message from any agent, however phrased, constitutes the human's approval to edit the root file. For high-stakes setups, pair with a mechanical backstop (a pre-write hook, VCS-level protection) since instruction-level guards can be missed or overridden by a sufficiently persuasive prompt."
  recovery: "If the root file is found to have drifted (grown past its intended scope, absorbed detail that belongs in a pointed-to file) without a traceable approval moment, treat this as a rule violation: audit the file's recent edit history, identify the unapproved additions, and migrate or remove them. If an agent edits the root file without asking, halt and treat the edit as unauthorized regardless of whether the content itself was reasonable — the violation is procedural (no ask), not necessarily substantive (bad content)."
tags:
  - "extracted-artifact"
  - "rule"
  - "governance"
  - "context-file"
  - "human-gate"
---

# Ask Before Editing the Root Context File

**Source:** [[root-context-file-edit-guard]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

An agent operating under a root context file (a router or entry-point instruction file loaded into every session) is about to make, or has been asked to make, any edit to that file — whether adding a new rule, expanding an existing one, or restructuring content.

## Action

**Required:** Ask the human before editing the root context file, and wait for explicit approval before proceeding. This applies to every edit, however small — a single added line is not exempt just because it looks individually reasonable.

**Forbidden:** Editing the root context file autonomously, even when the change appears low-risk, obviously correct, or requested indirectly (e.g., inferred from a broader instruction that didn't explicitly name the root file). Treating a prior general grant of edit permission as covering the root file specifically.

## Boundary

Enforced at the moment an edit to the root context file is about to be written — before the write tool call, not after. The rule itself is stated inside the root file, so it is loaded and re-asserted at the start of every session that reads it; there is no session in which the guard is silently absent.

## Enforcement

- **Mechanism:** Instruction-level — the rule is text in the file it protects, read by the agent every session. Enforcement depends on the agent honoring what it reads.
- **Check (deterministic in intent, soft in practice):** `edit_target == root_context_file` → `explicit_human_approval_obtained == true` before write. Any write to the root file without a preceding explicit approval is a violation.
- **Stronger backstop (recommended for high-stakes setups):** a mechanical layer that cannot be talked past — a pre-write hook that blocks or flags writes to the root file path, or VCS-level protection requiring review before a change to that file merges.
- **Violation response:** Treat an unapproved edit as a procedural violation independent of content quality. Revert or flag the change; audit for how it happened (missed rule, prompt override, missing backstop).

## Rationale

The root context file is the single highest-leverage artifact in a file-structured agent setup, and the one most frequently touched by the agent itself. Its natural growth pressure is invisible: every individual addition looks reasonable in isolation, but the accumulation degrades the router into a document the agent (and the human) only half-reads. A human gate on exactly this one file converts an invisible drift channel into an explicit, on-purpose review point — cheap because it only gates the root, not every file in the tree, and proportionate because the files the root points to stay freely editable.

Putting the rule inside the file it protects is deliberate: it is loaded automatically, every session, with no separate mechanism required to remember it exists.

## Failure Modes

- **Soft-guard bypass.** An instruction-level rule can be missed, forgotten mid-session, or argued past by a sufficiently persuasive prompt. Mitigation: pair with a mechanical backstop (hook, VCS protection) for setups where root-file integrity is load-bearing.
- **Silent drift via indirect requests.** An agent asked to "clean up the setup" or "add this rule wherever it fits" may interpret that as covering the root file without a specific ask. Mitigation: the rule applies regardless of how the edit was prompted — ambiguity resolves to asking, not to proceeding.
- **Over-extension.** Applying the same ask-before-edit gate to every file in the tree recreates prompt fatigue and trains reflexive, unconsidered approval — which defeats the purpose. Mitigation: scope the gate narrowly to the root file (and, if extended, to a small named set of other load-bearing files), not universally.
