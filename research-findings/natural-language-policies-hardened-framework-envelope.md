---
name: "Natural-Language Policies Inside a Hardened Framework Envelope"
summary: |-
  Omnigent lets policy authors write plain-English intent ("Deny if the user mentions Canada")
  while the framework owns everything that makes an LLM-judged policy safe to run: the
  JSON-schema response envelope, an injection guard instructing the classifier to treat the
  evaluated payload as data rather than commands, and a fail-closed error path where a
  classifier failure becomes DENY. For us the transferable insight is the division of labor —
  natural-language policies are only production-safe when the hardening lives in the framework,
  not in each author's prompt.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "policy-guarded-tool-execution.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
---

## What It Is

Omnigent's `prompt_policy` factory (`omnigent/policies/builtins/prompt.py`) turns a policy author's natural-language intent into an enforceable runtime gate. The author supplies only the intent sentence; the framework supplies the envelope: a hardened classifier prompt that instructs the judging LLM to treat the evaluated payload as data, not commands (anti-injection), a JSON-schema-constrained verdict format, and a fail-closed error path — if the classifier errors or returns something unparseable, the verdict is DENY, not ALLOW. The resulting policy plugs into the same six-phase ALLOW/ASK/DENY engine as function and CEL policies.

## Why It Matters

Natural-language policies are attractive (non-technical stakeholders can author constraints no schema can express) but naively implemented they are the most fragile guardrail type: the judge can be prompt-injected by the very content it evaluates, and a judge failure silently becomes a pass. Omnigent's answer is architectural: authors never touch the prompt scaffolding, so the injection guard and the fail-closed default cannot be forgotten per-policy. The safety properties are framework invariants rather than authoring discipline.

## Why People Are Using It

Observed in [omnigent](https://github.com/omnigent-ai/omnigent) v0.6.0.dev0 (alpha) — see [[omnigent-analysis]] for structural details. Fixture agents demonstrate the authoring surface (`"Deny if the user mentions Canada"` as a complete policy definition), and the fail-closed behavior is shared with the pre-execution phases' `FAIL_CLOSED_PHASES` constant.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Raw LLM-judge policies | Author writes the whole judge prompt | Prototyping; single-author systems where discipline substitutes for framework |
| Code-only policies | Function/CEL predicates, no LLM judge | Constraints that are structurally expressible; latency-sensitive paths |
| Post-hoc audit | Log and review violations after execution | Reversible actions only |

## Potential Improvements

- Shadow-mode evaluation (log verdicts without enforcing) to measure a new NL policy's false-positive rate before it gates anything
- Verdict-confidence thresholds routing borderline cases to ASK instead of binary ALLOW/DENY

## Potential Failure Modes

- **Judge unreliability persists:** the envelope removes injection and fail-open risk, not semantic misreading of ambiguous policies
- **Latency and cost:** every gated event adds a classifier inference
- **Envelope monoculture:** a flaw in the shared scaffolding affects every NL policy at once — the same centralization that makes it safe makes it a single point of failure
