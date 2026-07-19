---
title: "Name a Single Principal Domain Expert"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "principal-domain-expert-single-ownership"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-design-patterns.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "organizations embedding a subject-matter expert's judgment into an AI product's quality review-and-improvement loop"
    - "teams designing who is accountable for AI-quality decisions in a domain where trust matters (clinical, legal, editorial, or similar judgment calls)"
    - "any single-human-gate review role being considered for expansion into multiple co-equal reviewers"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "medium — reorganizing from co-equal reviewers to one named owner is a personnel and role-design change, not a code change; it can be reversed but carries real transition cost (redefining who has final say, possible role friction)"
  auditability: "checklist-grade, not machine-lintable — verifiable by inspecting the org chart or decision-rights documentation for exactly one named accountable person per AI-quality domain; no automated check applies to a human-organizational rule"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Stated as a leverage rule by a practitioner who has built and observed multiple production AI-quality programs, with one company's documented counter-example (two co-equal senior reviewers, no named owner) as the negative case; no adoption in this scaffold's consuming context yet."
contract:
  preconditions: "A domain expert's judgment is being embedded into an AI product's quality loop (in any mode — personally assessing and improving output, defining metrics for others to act on, or designing a self-improving system). More than one person could plausibly hold accountability for the resulting quality decisions."
  invariants: "Exactly one individual is named as accountable for AI-quality decisions in the domain at any given time — not a committee, not co-equal reviewers with overlapping scope. That person holds real decision-making ownership (a seat at the table when decisions happen), not an advisory role consulted after the fact. Splitting ownership by clearly partitioned sub-domain (each owner accountable for a non-overlapping slice) is distinct from splitting ownership over the same decisions — the rule targets the latter."
  governance: "Owner: whoever designs or approves the organizational structure around an AI-quality review role — a product or engineering lead, or the current principal domain expert defining a successor. Any proposal to move from a single named owner to co-equal reviewers over the same decisions should be treated as a structural change requiring explicit justification, not a routine staffing choice."
  recovery: "If ownership is currently diffused across co-equal reviewers with no named final say → name one principal owner before the next quality-affecting decision, even if the choice is provisional; provisional-but-named beats unnamed-but-fair. If the current sole owner departs → treat their departure as an active risk, not a solved problem — the rule concentrates decision quality but also concentrates departure risk; a succession candidate should be identified before it becomes urgent. If partitioned co-ownership (several owners, each with a clean non-overlapping slice) is being confused with the co-equal-reviewer failure mode → check for decision overlap; partition clarity is what distinguishes a safe split from the failure case, not the number of people involved."
tags:
  - "extracted-artifact"
  - "rule"
  - "agent-design"
  - "organizational-design"
  - "ai-quality"
  - "accountability"
---

# Name a Single Principal Domain Expert

**Source:** [[principal-domain-expert-single-ownership]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

An organization is embedding a domain expert's judgment into an AI product's quality review-and-improvement loop, in any mode of that loop (personally reviewing and fixing output, defining measurable quality for others to act on, or designing a system that measures and improves itself). More than one person is available or being considered for that accountability.

## Action

**Required:** Name exactly one individual as the principal domain expert accountable for AI-quality decisions in the domain. Give that person real ownership — a seat at the decision table when quality-affecting choices are made — not an advisory role consulted after decisions are effectively final.

**Forbidden:** Installing two or more co-equal people with overlapping accountability for the same AI-quality decisions and no designated final say. Treating a domain expert as a consultant whose opinion is gathered but does not shape the decision.

## Boundary

Enforced at organizational-design and hiring time — when a review/improvement role is being staffed, restructured, or reconsidered — not at runtime and not machine-checkable. This is a human-organizational rule, not a code-level or session-level invariant.

## Enforcement

- **Mechanism:** Inspect the org chart or decision-rights documentation for the domain in question. Exactly one person should be named as accountable, with documented authority to make the final call.
- **Check (checklist-grade):** `count(individuals with final say over this domain's AI-quality decisions) == 1`. A count of 0 (nobody accountable) or ≥2 with overlapping scope (co-equal reviewers) both fail the check.
- **Violation response:** If the count is 0, name an owner before the next quality-affecting decision. If the count is ≥2 with overlapping scope, either designate one as principal (demoting the others to advisory or specialist-support roles) or repartition the domain into non-overlapping sub-domains each with its own single owner.
- **Cannot be automated end-to-end:** This is an organizational-design check, not a system invariant — it is verified by human review of role definitions and decision-rights documentation, not by a hook, linter, or runtime gate.

## Rationale

Diffused accountability is a documented, concrete failure mode, not just a theoretical inefficiency: one company installed two co-equal senior domain experts side by side with no principal owner. Decisions moved slowly because nobody had final say, and both people left the company within 12–18 months — attributed in part to not feeling they had real ownership. The organization lost the accumulated context both people had built, which a single named owner with real authority would more plausibly have retained.

The rule does not argue against multiple domain experts in an organization — it argues against multiple people holding overlapping, undifferentiated accountability for the same decisions. Partitioned co-ownership (each expert owning a clean, non-overlapping slice of the domain) is explicitly distinguished from the failure case: the failure is decision overlap with no tiebreaker, not headcount.

## Failure Modes

- **Consensus paralysis.** Two or more co-equal reviewers with overlapping scope and no named tiebreaker slow every quality-affecting decision, because nobody can unilaterally close it.
- **Attrition without retained context.** People installed in an ambiguous-ownership role are more likely to leave, and their departure costs more than an equivalent single-owner departure because their accumulated context was never clearly theirs to hand off.
- **Single point of failure (the flip side).** Concentrating ownership in one person makes their departure more costly if no successor has been identified — naming a principal owner does not remove the need to plan for their eventual replacement.
- **False positive on partitioned co-ownership.** Mistaking a clean, non-overlapping split of a domain (several owners, each with a distinct slice) for the diffused-accountability failure case. The distinguishing factor is whether decisions overlap between owners, not whether there is more than one owner in the organization.

## Contract

### Preconditions
A domain expert's judgment is being embedded into an AI product's quality loop (in any mode — personally assessing and improving output, defining metrics for others to act on, or designing a self-improving system). More than one person could plausibly hold accountability for the resulting quality decisions.

### Invariants
Exactly one individual is named as accountable for AI-quality decisions in the domain at any given time — not a committee, not co-equal reviewers with overlapping scope. That person holds real decision-making ownership (a seat at the table when decisions happen), not an advisory role consulted after the fact. Splitting ownership by clearly partitioned sub-domain (each owner accountable for a non-overlapping slice) is distinct from splitting ownership over the same decisions — the rule targets the latter.

### Governance
Owner: whoever designs or approves the organizational structure around an AI-quality review role — a product or engineering lead, or the current principal domain expert defining a successor. Any proposal to move from a single named owner to co-equal reviewers over the same decisions should be treated as a structural change requiring explicit justification, not a routine staffing choice.

### Recovery
If ownership is currently diffused across co-equal reviewers with no named final say → name one principal owner before the next quality-affecting decision, even if the choice is provisional; provisional-but-named beats unnamed-but-fair. If the current sole owner departs → treat their departure as an active risk, not a solved problem — the rule concentrates decision quality but also concentrates departure risk; a succession candidate should be identified before it becomes urgent. If partitioned co-ownership (several owners, each with a clean non-overlapping slice) is being confused with the co-equal-reviewer failure mode → check for decision overlap; partition clarity is what distinguishes a safe split from the failure case, not the number of people involved.
