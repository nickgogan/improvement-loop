---
title: "Form Classification Rubric — Router Decision Spec"
type: "reference"
category: "knowledge-management"
target_system:
  - "improvement-loop"
  - "cross-system"
stage: "draft"
created: "2026-04-11"
updated: "2026-04-11"
author: "claude"
tags:
  - "form-router"
  - "proposer-architect-pipeline"
  - "classification"
  - "decision-spec"
aliases:
  - "Router rubric"
  - "Per-form inclusion criteria"
---

# Form Classification Rubric

Per-form inclusion and exclusion criteria for the (future) Form Router. Produced from five paper exercises — pattern (prior session), and rule / template / skill / agent (this session). This document is the decision spec the Router will use to classify a `ResearchFinding` into exactly one `assigned_form`.

**Status:** draft. Design not yet locked — see DD candidates at the end.

**Form taxonomy (5-form Router classification space):**

| Form | Shape | Lives in |
|---|---|---|
| `pattern` | Compositional primitive — reusable design approach | `meta-system/knowledge/patterns/` |
| `skill` | Procedure with inputs/outputs/steps | `.claude/skills/` or `{system}/.claude/skills/` |
| `rule` | Binary constraint enforced at a boundary | `.claude/rules/` or `{system}/governance/` |
| `template` | Scaffold with variables and a body | `meta-system/knowledge/templates/` |
| `agent` | Persona with cognitive disposition and durable scope | `meta-system/knowledge/templates/agent-templates/` (system instantiations in `{system}/agents/`) |

**Out of scope for the Router:** `guide` — produced at synthesis time by `/synthesize-guide` (IB-146) from aggregated patterns. Guides are end-directed; the 5 Router forms are all compositional.

---

## How the Router uses this rubric

```
ResearchFinding (from Proposer)
  │
  ▼
┌──────────────────────────────────────────────────┐
│  FORM ROUTER                                     │
│  1. Score the finding against each form's        │
│     inclusion signals (this rubric, §1–5)        │
│  2. Apply exclusion tests to eliminate forms     │
│  3. Derive router_confidence from logprobs on    │
│     the constrained classification output        │
│  4. Check proposer candidate_form vs assigned    │
│     form — set overridden:true if diverged       │
│  5. Dispatch to tier (autonomous / guided / hitl)│
└──────────────────────────────────────────────────┘
          │
          ▼
   FormAssignment (→ per-Form Architect)
```

**Tier dispatch logic:**

| Condition | Tier |
|---|---|
| `router_confidence ≥ HIGH` AND `overridden = false` AND no unresolved scope-constraint conflicts | autonomous |
| `router_confidence ≥ HIGH` AND `overridden = true` | guided (any override drops out of autonomous regardless of confidence) |
| `MEDIUM ≤ router_confidence < HIGH` | guided |
| `router_confidence < MEDIUM` OR form is ambiguous across two or more forms OR cross-artifact contract conflict detected | hitl |

The rubric is designed so that the **exclusion criteria do most of the work**. Most findings match at most one form's inclusion test cleanly; the exclusion criteria catch the residual ambiguity. The tier gates add a second layer: even a HIGH-confidence autonomous finding can be pulled into GUIDED if the Proposer's candidate differs from the Router's call, because override-worthy reasoning is exactly what humans should see.

**Calibration path (per aiAgentsFocus report):** derive `HIGH` and `MEDIUM` thresholds from logprob distributions over ~50–100 manually classified findings. Do not use self-reported model confidence. Track `override_rate` as an operational health metric; target 5–15% as evidence reviewers are genuinely inspecting.

**Confidence measures form-classification certainty, not evidence strength.** `router_confidence` answers "how certain is the Router that this finding belongs to this form?" — not "how well-supported is the finding's evidence?" A single-source finding can have HIGH classification confidence if no other form is a plausible fit. Evidence strength is already captured in the finding's `evidence_strength` field and gates `priority`, not `router_confidence`. The per-form confidence signals below describe conditions that affect form-classification certainty specifically. _(Amendment: batch 1, rows 6–15. Surfaced when single-source findings had unambiguous form classification but rubric's "multiple independent known uses" criterion for HIGH conflated evidence with form certainty.)_

---

## §1 Pattern

**Shape:** compositional primitive. "Here is a reusable *shape* for solving a recurring problem."

**Inclusion signals:**
- Frames a recurring problem with competing forces
- Describes a solution *shape*, not specific steps or named roles
- Multiple known uses across unrelated projects confirm the shape but instances vary in detail
- The finding answers "how should I structure this?" rather than "how do I do this?" or "what is forbidden?"
- Has consequences (positive and negative tradeoffs) — an "it depends" character
- Composable — other patterns can build on it, and it can be instantiated as skills / rules / agents / templates downstream

**Exclusion signals:**
- Has ordered steps with defined inputs/outputs → **skill**
- Is a binary "MUST/MUST NOT" enforced at a boundary → **rule**
- Is a scaffold with variables to fill in → **template**
- Describes one durable role with a specific cognitive disposition → **agent**
- Is end-directed ("how do I do X specifically") with a specified outcome → **guide** (out of Router scope)
- Single-source evidence with no convergent adoption → not yet ready; leave as finding at P3

**Router confidence signals:**
- **HIGH** — multiple independent known uses, explicit forces/tradeoffs in source, no ordered procedure, no single canonical role
- **MEDIUM** — one strong source plus related_findings, shape is clear but downstream instantiation is ambiguous
- **LOW** — single source, looks like a pattern but could also be read as a skill or agent description

**Prior-session exemplars (from session 20 pattern exercise):**
- `think-tool-scratchpad` → pattern (shape: "reserve an ephemeral scratchpad as a distinct tool"; instances vary)
- `programmatic-tool-calling` → pattern (shape: "compile tool orchestration into code, not prose"; instances span vendors)
- `mcp-as-code-api-progressive-discovery` → pattern (shape: "expose MCP surface through code API with progressive disclosure"; conceptual framing)

---

## §2 Skill

**Candidate walked:** `agentic-harness-self-assessment-skill.md`

**Shape:** a procedure. "Here is the ordered sequence an agent follows to produce a defined output from defined inputs."

**Inclusion signals:**
- Has defined **inputs** and **outputs** (even if the output is a report)
- Has ordered **steps** that can be followed without ongoing cognitive judgment beyond the procedure
- Explicit invocation — slash command, trigger phrase, or API call
- Stateless per invocation — no long-lived identity, borrows the caller's disposition
- Two or three "modes" indicate **parameterization of one skill**, not multiple skills
- Has **failure modes** that describe how the procedure degrades — a signal the author thought about the skill as an operation

**Exclusion signals:**
- Requires a cognitive disposition that persists across invocations → **agent**
- Is a binary constraint fired on an event with no returned output → **rule** (likely paired with a hook)
- Describes *how to think* about a class of problem with no procedure → **pattern**
- Is a scaffold with variables → **template**

**Router confidence signals:**
- **HIGH** — explicit inputs/outputs, ordered steps, explicit invocation, stateless per run
- **MEDIUM** — has steps and outputs but cognitive disposition is baked into the procedure (borderline skill/agent)
- **LOW** — steps present but no clear output; could be pattern prose in procedural clothing

**Tier note:** a HIGH-confidence skill can drop to GUIDED when the skill encodes an opinionated *framework* — the framework itself may deserve codification as a pattern first, with the skill as a downstream consumer. This was the call on the self-assessment skill exercise.

---

## §3 Rule

**Candidate walked:** `hook-based-enforcement-for-agent-outputs.md`

**Shape:** a binary constraint. "Under condition X, action Y is mandatory / forbidden, enforced at boundary Z."

**Inclusion signals:**
- Language of the finding uses "must / must not / always / never"
- Anti-pattern findings ("never do X", "this technique degrades performance") are natural rule candidates when the anti-pattern is expressible as a deterministic check at a named boundary _(Amendment 2: batch 3, row 34)_
- The invariant is expressible as a **deterministic check** (regex, enum, cardinality, format)
- There is a clear **enforcement boundary** — tool call, commit, session start, pre-deploy gate
- No multi-step procedure; the action is immediate (reject, block, warn, accept)
- No cognitive disposition required — the rule is mechanical
- Hard-gate semantics (binary pass/fail) rather than graded or advisory

**Exclusion signals:**
- Requires ordered steps to evaluate → **skill**
- Requires a persona to judge ambiguity → **agent**
- Describes *when and why* the constraint matters across cases → **pattern** (rule may be the instantiation)
- Is a scaffold with slots to fill → **template**

**Router confidence signals:**
- **HIGH** — binary, deterministic, boundary-enforced, no judgment
- **MEDIUM** — constraint language but check is ambiguous or requires context
- **LOW** — feels rule-like but has procedural or cognitive elements — likely a skill-with-constraints or a pattern

**Tier note:** rules tend to be autonomous-tier eligible because their blast radius at the artifact level is small (they codify a *shape*, not a deployment). The blast radius appears when the rule is adopted into a system's governance — which is a read-side concern per DD-46.

**Pattern/rule co-occurrence:** many findings describe both a pattern ("why enforce at tool boundary") and a rule ("the specific invariant"). Per session-20 decision (secondary forms dropped from schema), the Router picks the primary form and the secondary form is harvested later by `/extract-artifacts` (IB-147). For hook-based enforcement the primary form is rule, because the finding's center of gravity is the mechanism, not the framing.

---

## §4 Template

**Candidate walked:** `template-generated-skills-multi-host.md`

**Shape:** a scaffold. "Here is a structural backbone with named variables and a body, rendered into variants."

**Inclusion signals:**
- The finding itself describes a scaffold, generator, or rendering process
- Identifiable **variables** and a **body** — the fundamental structure of the template form
- Repeatable generation — not a one-off design decision
- Output is a **build artifact**, not hand-authored
- Variation axis is explicit (hosts, systems, projects, model vendors, etc.)

**Exclusion signals:**
- "Here's how to *think about* variation" with no named variables → **pattern**
- "Here's the *procedure* to produce variants" without a named backbone → **skill**
- Only enforces what can / cannot appear in rendered output → **rule** (may pair with a template)
- Describes a persona that writes variants → **agent**

**Router confidence signals:**
- **HIGH** — explicit template files, named variables, build step, generator
- **MEDIUM** — backbone + variation pattern clear but no formal generator
- **LOW** — feels structured but has no variable/body decomposition

**Template/pattern distinction:** a pattern says "here is how to structure X"; a template provides the structure *pre-filled with slots*. If you can write the finding's insight in `{{VARIABLE}} → body` form without loss, it's a template. If that form loses the insight (the *why* of the shape), it's a pattern.

---

## §5 Agent

**Candidate walked:** `specialized-parallel-agent-roles.md` — **overridden from agent to pattern**.

**Shape:** a persona. "Here is a named role with a cognitive disposition and durable responsibilities."

**Inclusion signals:**
- Single-role identity with a named disposition ("thinks like a skeptical analyst," "optimizes for duplication")
- "How it thinks" is the most important part of the finding — not what it does
- Long-lived scope — owns a responsibility area across invocations
- Read/write scope definable per role (DD-53)
- Communicates with other roles via artifacts (DD-63)
- Evidence converges on a *specific* persona, not just the shape of having specialists

**Exclusion signals (the stress test):**
- Describes a **system of roles** rather than one role → **pattern**
- Cross-source confirmations converge on *shape* but diverge on *role names* → **pattern**
- Role set is project-specific with no canonical instance → **pattern**
- Has ordered steps and explicit invocation → **skill**
- Is "how to think about structuring roles" → **pattern**

**Router confidence signals:**
- **HIGH** — single named role, specific disposition, consistent scope across sources
- **MEDIUM** — role is named but sources use different names / scopes for the same shape (override to pattern likely)
- **LOW** — multiple candidate roles blur together; codify the shape as pattern first, instantiate agents downstream

**Key diagnostic from the walked exercise:** when a finding's cross-source confirmations converge on *shape* (parallel specialists alongside main agents) but diverge on *role names* (Anthropic's dedup/perf/codegen vs gstack's vs ultra-review's), the pattern is the stable layer and the agents are instantiations. Codify the pattern; downstream `/extract-artifacts` (IB-147) or system owners can instantiate specific agent templates.

**Proposer candidate vs Router assignment:** the agent form is the most likely form for override-to-pattern, because agent-shaped language is easy to use loosely ("the dedup agent," "the perf agent") when the underlying insight is structural. The Router should be biased toward pattern when role count > 1 in the finding.

---

## Open questions surfaced during the exercises

1. **Co-occurrence handling — RESOLVED.** Rule and pattern co-occur in the hook-based-enforcement finding; pattern and template co-occur in the gstack finding. **Resolution:** the Router picks one form, full stop. Co-occurrence is resolved at read time by downstream consumers, not flagged forward in FormAssignment metadata. No secondary-form hints, no pending-edge backlog. `/extract-artifacts` (IB-147) — if built — operates on already-codified artifacts by scanning their bodies for harvestable secondary content, not on Router metadata. Rationale: forward-flagging creates maintenance edges that go stale with primary artifact drift (same failure mode as cross-finding prerequisite tracking, killed in session 20).

2. **Framework-shaped skills.** The self-assessment-skill exercise exposed a case where a skill encodes an opinionated framework (12-primitive taxonomy). The framework itself arguably deserves pattern-form codification before the skill is built. **Open:** should the Router detect "skill wraps undocumented framework" as an auto-trigger for GUIDED tier? How does it detect it?

3. **Role-count discriminator for agent form.** The agent exercise showed that 5 specialist roles → pattern, because no canonical role. But 1 specialist role → agent. **Open:** is role-count a first-class discriminator, or is it downstream of the "how it thinks" test?

4. **Pattern/template collapse.** Some findings look like both patterns and templates (the pattern describes shape; the template pre-fills it). **Open:** does the Router always emit the pattern and let `/extract-artifacts` produce the template? Or does Router emit template when the finding already provides a fillable backbone?

5. **Dissenting findings pathway.** Only one exercise (skill) had a dissenting finding in `related_findings`. **Open:** when dissenting findings exist, should the Router auto-escalate to GUIDED? How does the Form Architect reflect the dissent in the ContractSpec?

6. **Cross-artifact contract conflicts.** The aiAgentsFocus report flagged cross-system contract conflicts as hitl triggers. With per-form architects producing system-agnostic artifacts, the failure mode shifts: two different findings could produce rules or patterns with contradictory invariants (e.g., "always advisory" vs "always hard-gate"). **Open:** is there a cross-artifact validation pass after codification? Where does it live?

7. **Evidence-strength gating.** All four exercises had Medium or Strong evidence. **Open:** does the Router refuse to classify Weak-evidence findings, or does it route them to hitl with the weakness as the reason?

---

## Schema drift from the aiAgentsFocus report

During the exercises, several departures from the aiAgentsFocus schema emerged. All drift is captured here with rationale.

### 1. `persona` → `agent`

**Drift:** the report uses `persona` as the fifth form. MetaSystem uses `agent`.
**Rationale:** locked in session 20. MetaSystem's 6-form vocabulary (`pattern | skill | rule | template | agent | guide`) is the prior-art. No reason to introduce new terminology.

### 2. `affected_systems`-driven fan-out → one system-agnostic artifact

**Drift:** the report specifies parallel Architect fan-out per target system. MetaSystem codifies one system-agnostic artifact per finding; system owners pull on the read side.
**Rationale:** locked in session 20. Per-system routing is a read-side concern (DD-46). Upstream separation of concerns matches Proposer/Router/Architect being form-focused, not system-focused.

### 3. `candidate_form`, `overridden`, `override_justification` kept

**Drift:** minor — the aiAgentsFocus report treats these as best-effort. This rubric makes them load-bearing: `overridden: true` alone forces GUIDED tier regardless of confidence.
**Rationale:** override reasoning is exactly what humans should see. Rubber-stamp prevention per aiAgentsFocus recommendation to gate at the form-decision boundary.

### 4. `excluded_evidence` / `scope_constraints` / `assumptions` required

**Drift:** the aiAgentsFocus report has `excluded_evidence` and `scope_constraints`. Session 20 added `assumptions` and `dissenting_findings` as also required.
**Rationale:** SEI ML Mismatch Descriptors + GRADE EtD dissent field. Prevents tacit-knowledge-loss failure mode. All four exercises used these fields; `"none"` is the explicit empty value.

### 5. `contract` = `preconditions` / `invariants` / `governance` / `recovery`

**Drift:** per the aiAgentsFocus report, anchored on arxiv 2602.22302 (ABC framework). Session 20 confirmed real; all exercises used this shape successfully.
**Rationale:** the ContractSpec shape held across all five forms, which is strong evidence it's the right universal layer. No drift — just confirmation.

### 6. `tier` dispatch — override always drops out of autonomous

**Drift:** the aiAgentsFocus report has `overridden: true` as a GUIDED trigger. This rubric tightens that to "override drops out of autonomous REGARDLESS of confidence score."
**Rationale:** a HIGH-confidence override is the *most important* case to show a human — it means the Router was confident about a call that disagreed with the Proposer. Auto-promoting that would be the worst-case silent failure.

### 7. `validation` block (structural / semantic / llm_judge) deferred

**Drift:** the aiAgentsFocus report mandates a three-layer validation before promoting a draft to artifact_store. Session 20 deferred this; no validation layer in the current design.
**Rationale:** deferred until the pipeline has enough throughput to justify it. Current codification is Nick-reviewed. When the Router goes autonomous, the validation layer must come online — this is on the deferred list.

### 8. Proposer `confidence: 0.0–1.0` → discrete `HIGH/MEDIUM/LOW`

**Drift:** the rubric uses discrete confidence levels (`HIGH/MEDIUM/LOW`) rather than the float. The Router still uses logprob distributions internally; the discrete mapping is for human-readable FormAssignment.
**Rationale:** the report explicitly says the float is for human readability and the Router uses logprobs. Discretizing early avoids fake-precision in the human-facing output. Thresholds are calibrated once and mapped from logprob ranges.

---

## What the rubric revealed about the design (findings for conversation)

1. **The exclusion criteria do most of the work.** Inclusion signals are often overlapping (a skill and a rule both live "at a boundary"; a pattern and a template both describe reusable shapes). The binary discriminators in the exclusion tables are what actually resolve classifications. The Router should weight exclusion more heavily than inclusion.

2. **Override-to-pattern is the common case.** The agent exercise showed that loose agent-shaped language in findings maps to pattern-shaped structure in codified artifacts. Expect 10-30% of proposer-candidate `agent` findings to override to `pattern`. Track this rate.

3. **Rules are the cleanest form.** The rule exercise had no ambiguity — binary constraint, clear boundary, condition/action shape. Rules are likely safe for autonomous tier at HIGH confidence.

4. **Templates are the rarest.** Template-form findings require the finding itself to describe a scaffolding process. Most findings describe *what* or *how*, not *here's a backbone with variables*. Expect templates to be under 10% of classified output.

5. **Patterns are the default.** When a finding's shape is stable but its instantiation is project-specific, the form is pattern. The other four forms handle the cases where the instantiation *is* the insight (a specific procedure, a specific constraint, a specific scaffold, a specific persona).

6. **Framework-shaped skills are a trap.** The self-assessment-skill finding looked skill-shaped but its real value was the 12-primitive framework it wrapped. The Router needs to detect "skill is a consumer of an uncodified pattern" and route to GUIDED so the pattern gets codified first.

---

## Design Decisions (filed session 22)

| DD | Name | Summary |
|---|---|---|
| DD-75 | Override drops to guided | `overridden: true` forces `tier = guided` regardless of confidence |
| DD-76 | Role-count discriminator | role_count > 1 biases toward pattern, not agent |
| DD-77 | Single-form classification | Router picks one form; no secondary-form metadata. Co-occurrence resolved at read time. |
| DD-78 | ContractSpec universal layer | Every CodifiedArtifact carries `preconditions / invariants / governance / recovery` |
| DD-79 | Required finding fields | `assumptions`, `scope_constraints`, `excluded_evidence`, `dissenting_findings` — explicit `"none"` for empty |

All DDs filed in `systems/improvement-loop/project-management/design-decisions/`.

---

## IB candidates surfaced (NOT filing — surface only)

### IBc-1: Router calibration set

Hand-classify 50–100 existing findings against this rubric, then derive logprob thresholds for `HIGH` / `MEDIUM` / `LOW` on a constrained classification LLM call. Prerequisite to any automated Form Router build.

### IBc-2: `/rubric-apply` dry-run skill

A skill that runs a finding through this rubric manually (no LLM classification) and returns the expected form + reason codes. Useful for validating the rubric before automating the Router. Could become the calibration data generator for IBc-1.

### IBc-3: Form Architect stubs

One stub agent definition per form (pattern, skill, rule, template, agent). Stubs carry only the input schema (FormAssignment) and output schema (CodifiedArtifact for that form). Full procedures fleshed out incrementally. Unblocks end-to-end plumbing without waiting for all 5 Architects to be built at once.

### IBc-4: Cross-artifact contract conflict detector

Post-codification pass that scans ContractSpec invariants for contradictions across artifacts sharing any source. Escalates to hitl tier. Addresses open question #6.

### IBc-5: Validation layer (structural + semantic + llm_judge)

The three-layer validation pass from the aiAgentsFocus report. Deferred until Router goes autonomous. Pre-requisite for removing Nick-as-reviewer on codification.

---

## Calibration findings (from 50-finding calibration set)

Calibration data: [[2026-04-11-router-calibration-set]]. 50 findings classified across 4 batches. 2 rubric amendments applied during classification (see above: confidence clarification, anti-pattern rule signal).

### 1. Pattern dominance is structural, not miscalibration

92% of findings classified as pattern. This is correct — the KB extracts design approaches and architectural shapes from research sources. Findings are written at the philosophy/approach level, which maps to pattern form. The other four forms emerge at the mechanism/artifact level, which is downstream of pattern codification.

**Implication for the Router:** do not treat 90%+ pattern classification as evidence of a broken rubric. The Router's exclusion criteria are working correctly — they eliminate non-pattern forms, and most findings genuinely are patterns.

### 2. Non-pattern forms are primarily downstream artifacts

- **Rules** surfaced as co-occurrences in 6 pattern-classified findings. Each contained a specific constraint ("never prescribe reasoning steps", "every promotion must be policy-gated") embedded inside a broader design approach. The one standalone rule (row 34) was an anti-pattern finding with natural "never do X" constraint language at the mechanism level.
- **Templates** surfaced as co-occurrences in 4 pattern-classified findings. Each contained a scaffold structure (YAML workflow, SOUL.md sections, routing table) embedded inside a broader architecture description. The one standalone template (row 21) was a fillable governance artifact with named variables.
- **Skills** appeared when findings described specific procedural artifacts with defined inputs, outputs, and ordered steps.
- **Agents** never appeared. Every multi-role finding resolved to pattern via DDc-2.

**Implication for the pipeline:** `/extract-artifacts` (IB-147) is critical infrastructure. Most rules, templates, and agent definitions will be *derived* from codified patterns, not classified directly by the Router. The Router classifies the primary form; `/extract-artifacts` harvests secondary forms from codified artifact bodies.

### 3. The Router's primary value is the ~10% non-pattern + gating

The Router adds value in three ways:
1. **Catching the ~8–10% non-pattern cases** — findings that are genuinely skills, rules, or templates at their center of gravity.
2. **Override detection** — flagging when the proposer's candidate form disagrees with the Router's assignment. Non-diagnostic in calibration (45/50 candidates were `-`), but load-bearing once `/research-proposer` populates `candidate_form`.
3. **Confidence gating** — routing MED/LOW-confidence classifications to guided/hitl tiers. 14% guided in calibration, 0% hitl.

The Router should NOT be optimized for even form distribution. 90%+ pattern is the expected steady state.

### 4. Level-of-abstraction is the key discriminator

The single most useful diagnostic across all 50 classifications: **at what level of abstraction does the finding operate?**

| Level | Form | Example |
|---|---|---|
| Philosophy / design approach | pattern | "Make errors structurally impossible" (poka-yoke) |
| Heuristic / decision framework | pattern | "Three properties that survive model updates" |
| Mechanism / specific constraint | rule | "Never prescribe reasoning steps to reasoning models" |
| Scaffold / fillable structure | template | "Tech/version/rationale pinning table" |
| Procedure / ordered steps | skill | "4-agent pipeline: planner→critic→refiner→finalizer" |
| Named role / durable disposition | agent | (none in this sample) |

Most KB findings operate at the philosophy/heuristic level → pattern. The level-of-abstraction test resolves ambiguity faster than running through all 5 form exclusion tests.

## Next steps

Path B (calibration) is complete. The rubric is empirically validated against 50 findings. Recommended next actions:

1. **Lock the rubric** — convert DDc-1 through DDc-5 to formal DDs. The calibration provides the evidence base.
2. **Build `/extract-artifacts`** (IB-147) — the calibration confirms this is the primary mechanism for producing non-pattern forms. Higher priority than previously estimated.
3. **Populate `candidate_form`** — update `/research-proposer` to emit a candidate form per finding, enabling override detection.
4. **Build Form Architect stubs** (IBc-3) — pattern Architect is the urgent one given 92% pattern classification.

---

## Links

- Session 20 artifact-design decisions: `PROGRESS.md` entries 1–11
- AI-native prior art (primary anchor): [[2026-04-10-architect-handoff-deep-research-results-aiAgentsFocus]]
- Human-domain prior art: [[2026-04-10-architect-handoff-deep-research-results.md]]
- Deep research prompt: [[2026-04-10-architect-handoff-deep-research-prompt]]
- Capability type selection pattern: [[capability-type-selection]]
- Research-to-codification pipeline guide: [[research-to-codification-pipeline]]
- IB-146 `/synthesize-guide` — pattern → guide synthesis (deferred)
- IB-147 `/extract-artifacts` — secondary form harvesting (deferred)
- IB-148 `/session-handoff-review` — handoff audit (deferred)
