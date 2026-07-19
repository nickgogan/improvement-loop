---
title: "No Adoption Without Eval Evidence"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "skill-popularity-vs-measured-efficacy"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "eval-driven-improvement-loops.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams or individuals considering installing a third-party skill, prompt, agent, or MCP server that claims to improve agent performance"
    - "roster-triage processes that use popularity signals (stars, downloads, name recognition) as part of an adoption decision"
    - "maintainers of a watched-library or marketplace-style intake pipeline for external agentic artifacts"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "low — an installed skill becomes always-consulted context (its description loads every session) and a trust/security surface (its instructions execute on invocation); uninstalling reverses the direct cost but not any decisions or artifacts already produced under its influence"
  auditability: "high — the check is binary and checkable before install: does published rigorous evaluation exist, or has a local with/without baseline been run? Either can be pointed to as evidence."
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Motivated by a measured counterexample: a skill from a 177k-star repository, benchmarked with an end-to-end program-building eval, used 5% more tokens and produced worse results than no skill at all — popularity signals were anti-correlated with value in this case. No adoption recorded in this system yet."
contract:
  preconditions: "A third-party skill, prompt, agent, or MCP server is being considered for adoption into a live workflow. The artifact makes an explicit or implicit performance claim (it exists to make the agent better at something)."
  invariants: "No such artifact is adopted on the strength of popularity signals alone (stars, downloads, name recognition) — those measure virality, not efficacy, and can be anti-correlated with it. Adoption requires either published rigorous evaluation results from the artifact's author/community, or a locally run with/without baseline comparison before the artifact is trusted in a live workflow. Security vetting is a separate, additional requirement — passing the efficacy check does not substitute for it, since any installed artifact can instruct the agent to execute arbitrary actions."
  governance: "Owner: whoever runs the intake/triage process for external skills, prompts, agents, or MCP servers (a watched-library maintainer, an import-review process, or the individual doing the install). Popularity metadata may still be tracked as a roster signal, but must not be treated as sufficient evidence on its own; intake tooling that surfaces star counts should surface eval status alongside it."
  recovery: "If an artifact is already adopted and no eval evidence exists → run a local with/without baseline retroactively; if it underperforms baseline, deprecate or remove it. If published eval evidence is later found to be non-rigorous or contradicted by local measurement → treat the artifact as unvetted and re-run the local baseline before continued reliance. If the rule is blocking adoption of an artifact whose author simply never published evals (rather than one known to underperform) → the remedy is running your own baseline, not blanket rejection; do not let the rule become a de facto ban on unbenchmarked-but-plausibly-good artifacts."
tags:
  - "extracted-artifact"
  - "rule"
  - "evaluation"
  - "skill-adoption"
  - "third-party-artifacts"
---

# No Adoption Without Eval Evidence

**Source:** [[skill-popularity-vs-measured-efficacy]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A third-party skill, prompt, agent, or MCP server is being considered for adoption into a live workflow, and it claims (explicitly or by its existence) to improve agent performance.

## Action

**Required:** Before adopting, confirm one of: (a) the artifact's author or community has published rigorous evaluation results supporting the performance claim, or (b) a local with/without baseline comparison has been run and shows the artifact outperforms no-artifact on a representative task.

**Forbidden:** Adopting the artifact on the strength of popularity signals alone — star counts, download counts, or the reputation of the name attached to the repository. These measure virality, not efficacy, and are not a substitute for evaluation evidence.

## Boundary

Enforced at the point of adoption decision — before the artifact becomes part of a live workflow's always-consulted context or execution surface. Applies to intake/triage processes for external skills, prompts, agents, and MCP servers (watched-library reviews, import pipelines, ad hoc installs).

## Enforcement

- **Mechanism:** Intake/triage checklists or tooling require an eval-evidence field (published results link, or local baseline results) before an artifact's adoption status can move past "candidate."
- **Check (decidable):** `(published_rigorous_eval_exists == true) OR (local_with_without_baseline_run == true AND artifact_outperforms_baseline == true)`. If false, adoption does not proceed.
- **Violation response:** Artifact remains in candidate/unvetted status. Popularity metadata may still be recorded, but is explicitly marked as non-substitutive for the eval-evidence field.

## Rationale

Skills and similar artifacts are the primary distribution unit of agent capability, and the default vetting signal most people reach for — stars, virality, big-name association — is measurably uncorrelated with value and can be anti-correlated with it. A concrete measurement backs this: a skill from a 177k-star repository, evaluated end-to-end, consumed more tokens and produced worse results than using no skill at all. A skill is also always-consulted context plus arbitrary instructions on invocation — a bad one taxes every session it's loaded in, independent of any security risk. Popularity told the adopter nothing about either cost.

## Failure Modes

- **Over-application blocks genuinely useful, simply-unbenchmarked artifacts.** The remedy for an artifact with no published eval is to run a local baseline, not to reject it outright — the rule targets adoption without *any* evidence, not adoption without *published* evidence specifically.
- **Local evals can mismeasure fit.** An artifact can lose on a generic benchmark but win on the specific workflow it was built for; a single local baseline is directional evidence, not a guarantee, and results should be interpreted against the artifact's intended use case.
- **One benchmark is thin grounds for a permanent verdict.** A single measured underperformance (or overperformance) on one task is anecdote-strength evidence about the direction of the effect, not its magnitude or generality — re-evaluate if the artifact changes materially or the workflow shifts.
- **Efficacy evidence is not security evidence.** Passing this rule's check says nothing about whether the artifact is safe to run — a separate security vetting step (instructions can execute arbitrary actions) is required regardless of measured efficacy.

## Contract

### Preconditions
A third-party skill, prompt, agent, or MCP server is being considered for adoption into a live workflow. The artifact makes an explicit or implicit performance claim (it exists to make the agent better at something).

### Invariants
No such artifact is adopted on the strength of popularity signals alone (stars, downloads, name recognition) — those measure virality, not efficacy, and can be anti-correlated with it. Adoption requires either published rigorous evaluation results from the artifact's author/community, or a locally run with/without baseline comparison before the artifact is trusted in a live workflow. Security vetting is a separate, additional requirement — passing the efficacy check does not substitute for it, since any installed artifact can instruct the agent to execute arbitrary actions.

### Governance
Owner: whoever runs the intake/triage process for external skills, prompts, agents, or MCP servers (a watched-library maintainer, an import-review process, or the individual doing the install). Popularity metadata may still be tracked as a roster signal, but must not be treated as sufficient evidence on its own; intake tooling that surfaces star counts should surface eval status alongside it.

### Recovery
If an artifact is already adopted and no eval evidence exists → run a local with/without baseline retroactively; if it underperforms baseline, deprecate or remove it. If published eval evidence is later found to be non-rigorous or contradicted by local measurement → treat the artifact as unvetted and re-run the local baseline before continued reliance. If the rule is blocking adoption of an artifact whose author simply never published evals (rather than one known to underperform) → the remedy is running your own baseline, not blanket rejection; do not let the rule become a de facto ban on unbenchmarked-but-plausibly-good artifacts.
