# AI-Native Proposer–Architect Pipeline Design

> **Context**: This document synthesizes prior-art research (human-domain patterns: MITRE ATT&CK/CAR, GRADE/WHO EtD, NIST OSCAL, MLflow Model Cards, Pharma CTD) with AI-native architectural patterns into actionable implementation guidance. Use this as a design spec for the artifact contract between the Researcher/Proposer and the per-system Architect in a knowledge-management pipeline for AI agent systems.

---

## The Core Contracts

### ResearchFinding (Proposer Output)

```yaml
# finding_store/{id}.yaml
id: "finding_{uuid}"
created_at: "ISO-8601"
source:
  url: "https://..."
  type: "paper | blog | repo | talk"
  extracted_at: "ISO-8601"

# Core content
description: "One-paragraph plain-language description of the finding"
evidence_refs:
  - quote: "exact quote from source"
    location: "section/page ref"
    weight: "high | medium | low"

# Form signal (proposer suggests, Router decides)
candidate_form: "pattern | skill | rule | template | persona"
candidate_form_rationale: "why this form was suggested"
confidence: 0.0–1.0  # self-reported; Router uses logprobs, not this field

# Multi-target scope
affected_systems:
  - system_id: "sys_abc"
    relevance: "high | medium | low"
    notes: "system-specific caveat if any"

# Mandatory exclusion fields (prevents ML-mismatch-style hidden assumptions)
excluded_evidence:
  - description: "what was excluded"
    reason: "why it was excluded or downweighted"
scope_constraints:
  - "explicit boundary the finding does NOT cover"
```

**Design rationale**:
- `candidate_form` is a *signal* to the Form Router, not a binding decision. The Router overrides it with a logged reason trail.
- `excluded_evidence` and `scope_constraints` are **first-class required fields**, not optional notes — this is the AI-native equivalent of GRADE's "reasons for downgrading certainty" and prevents tacit-knowledge-loss failure mode.
- `confidence` is self-reported for human readability. The Router uses its own logprob-based score.

---

### FormAssignment (Router Output → Architect Input)

```yaml
# state_store/assignments/{finding_id}.yaml
finding_id: "finding_{uuid}"
assigned_form: "pattern | skill | rule | template | persona"
router_confidence: 0.0–1.0          # logprob-derived, not self-reported
reason_codes:
  - "matches_reusable_solution_context"
  - "applies_across_systems"
  - "not_platform_specific"
proposer_candidate_form: "pattern"  # what the Proposer suggested
overridden: false                   # true if router diverged from candidate_form
override_justification: ""          # required if overridden: true
tier: "autonomous | guided | hitl"  # escalation tier (see Confidence Tiers below)
assigned_at: "ISO-8601"
reviewer_id: ""                     # populated if tier = hitl
```

**Design rationale**:
- Write-locked before Architect workers spawn — canonical binding point for multi-target fan-out.
- `tier` drives the approval workflow: autonomous findings skip human review; guided shows router reasoning for optional redirect; hitl blocks until approved.

---

### CodifiedArtifact (Architect Output)

```yaml
# artifact_store/{form}/{id}.yaml
id: "artifact_{uuid}"
form: "pattern | skill | rule | template | persona"

# Provenance — permanent link to upstream evidence
source_finding_id: "finding_{uuid}"
assignment_id: "assignment_{uuid}"
target_system: "sys_abc"            # which system this artifact is for

# Content (schema varies per form — see Per-Form Schemas below)
content: {}

# Validation record
validation:
  structural_pass: true
  semantic_pass: true
  llm_judge_score: 0.0–1.0
  llm_judge_notes: ""
  promoted_at: "ISO-8601"

# Behavioral contract (ContractSpec / ABC model)
contract:
  preconditions:
    - "condition that must hold before this artifact is applied"
  invariants:
    - "condition that must hold while this artifact is active"
  governance:
    - "constraint on how downstream agents may use this artifact"
  recovery:
    - "what to do if the artifact produces unexpected output"
```

---

## Per-Form Schemas

### Pattern

```yaml
content:
  name: "PascalCase pattern name"
  context: "when this pattern applies"
  problem: "the recurring problem it solves"
  forces:
    - "competing tension the pattern resolves"
  solution: "the canonical solution structure"
  consequences:
    positive:
      - ""
    negative:
      - ""
  known_uses:
    - system_id: ""
      description: ""
  related_patterns:
    - artifact_id: ""
```

### Skill

```yaml
content:
  name: "verb_noun format"
  description: "what this skill enables an agent to do"
  trigger_conditions:
    - "when the agent should invoke this skill"
  inputs:
    - name: ""
      type: ""
      required: true
  outputs:
    - name: ""
      type: ""
  steps:
    - "ordered execution step"
  failure_modes:
    - condition: ""
      handling: ""
```

### Rule

```yaml
content:
  name: "SCREAMING_SNAKE_CASE"
  type: "constraint | policy | heuristic"
  scope: "agent_id | system_id | global"
  condition: "IF condition expression"
  action: "THEN action or constraint"
  priority: 1–100
  hard_constraint: true   # if false, can be overridden with justification
```

### Template

```yaml
content:
  name: "descriptive-template-name"
  purpose: ""
  variables:
    - name: "{{VARIABLE}}"
      description: ""
      required: true
      default: ""
  body: |
    Template body with {{VARIABLE}} placeholders
  usage_notes: ""
```

### Persona

```yaml
content:
  name: "AgentPersonaName"
  role: "one-line role description"
  responsibilities:
    - ""
  tone_and_style:
    - ""
  scope_boundaries:
    in_scope:
      - ""
    out_of_scope:
      - ""
  skill_refs:
    - artifact_id: ""
  rule_refs:
    - artifact_id: ""
```

---

## Pipeline Architecture

```
[External Source]
      │
      ▼
┌─────────────────────────────────────────────────────┐
│  PROPOSER AGENT                                     │
│  • Ingests source (paper / blog / repo / talk)      │
│  • Extracts finding into ResearchFinding schema     │
│  • Writes full artifact to finding_store/           │
│  • Returns: pointer (finding_id) — NOT a summary    │
└─────────────────────┬───────────────────────────────┘
                      │ finding_id
                      ▼
┌─────────────────────────────────────────────────────┐
│  FORM ROUTER (orchestrator component)               │
│  • Reads finding from finding_store/{id}.yaml       │
│  • Classifies: finding → form using constrained     │
│    structured output + logprob confidence           │
│  • Writes canonical FormAssignment to state_store   │
│  • Dispatches to tier (autonomous / guided / hitl)  │
└─────┬───────────────┬───────────────┬───────────────┘
      │               │               │
  autonomous       guided           hitl
  (skip review)   (show reasoning, (blocking gate:
                  optional redirect) human must approve)
      │               │               │
      └───────────────┴───────────────┘
                      │ FormAssignment
                      ▼
┌─────────────────────────────────────────────────────┐
│  ARCHITECT AGENTS (parallel, one per target system) │
│  Each agent receives:                               │
│    • finding_id → dereferences full ResearchFinding │
│    • FormAssignment (form + reason_codes)           │
│    • system_context_{sys_id}.yaml                   │
│  Each agent writes: draft to draft_store/           │
└─────────────────────┬───────────────────────────────┘
                      │ draft artifact
                      ▼
┌─────────────────────────────────────────────────────┐
│  VALIDATION LAYER                                   │
│  1. Structural: JSON schema check (deterministic)   │
│  2. Semantic: domain constraint rules               │
│  3. LLM Judge: completeness + correctness score     │
│  → Pass all three → promote to artifact_store/      │
│  → Fail any → return to Architect with error report │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
              artifact_store/
              {form}/{artifact_id}.yaml
              (carries source_finding_id + ContractSpec)
```

---

## Confidence Tiers and Escalation

| Tier | Trigger | Behavior |
|------|---------|----------|
| **autonomous** | `router_confidence ≥ HIGH_THRESHOLD` AND `overridden = false` | Architect spawns immediately; no human gate |
| **guided** | `HIGH_THRESHOLD > router_confidence ≥ LOW_THRESHOLD` OR `overridden = true` | Human reviewer sees finding + router reasoning + reason_codes; can approve, redirect to different form, or add scope notes; non-blocking (reviewer has time window, defaults to approve on timeout) |
| **hitl** | `router_confidence < LOW_THRESHOLD` OR `form = null (novel type)` OR cross-system conflict detected | Blocking gate: pipeline pauses until human approves or redirects |

**Calibration notes**:
- Set `HIGH_THRESHOLD` and `LOW_THRESHOLD` from logprob distributions over a labeled sample of your own findings (~50–100 items). Do not use self-reported model confidence scores.
- Track `override_rate` as an operational health metric. Near-zero override rate at high volume = reviewers not engaging (governance theater). Target a non-trivial override rate (5–15%) as evidence reviewers are genuinely inspecting.
- Gate at the **form-decision boundary** (low-volume, high-leverage), not at the artifact output boundary (high-volume, rubber-stamp risk).

---

## Multi-Target Fan-Out

When `affected_systems` contains multiple entries:

1. Form Router writes **one** canonical `FormAssignment` (same form for all targets).
2. Orchestrator spawns **one Architect agent per target system in parallel**.
3. Each Architect reads:
   - Shared: `finding_store/{finding_id}.yaml`
   - Shared: `state_store/assignments/{finding_id}.yaml`
   - Target-specific: `system_contexts/{sys_id}.yaml`
4. Each Architect writes to `draft_store/{finding_id}/{sys_id}.yaml`.
5. Validation runs per artifact independently.
6. All promoted artifacts reference the same `source_finding_id`.

**Cross-system conflict detection**: If parallel Architects produce artifacts with contradictory `contract.invariants` for the same `source_finding_id`, a post-validation conflict checker flags the pair. Conflicts are written to `conflicts/{finding_id}.yaml` and escalate to hitl tier for human resolution. Do not merge or average conflicting constraints — expose the tension explicitly (OSCAL control-mapping model analogue).

---

## Failure Modes and Mitigations

| Failure Mode | Trigger | Mitigation |
|---|---|---|
| **Hallucination cascade** | Proposer fabricates source claim → flows to artifact store | RAV layer: re-verify all `evidence_refs` against source documents before finding is promoted past Proposer stage |
| **Confidence collapse** | Router outputs `confidence = 1.0` on all items; hitl never fires | Use logprob distributions, not self-reported scores; calibrate thresholds on labeled sample; monitor hitl rate — sustained 0% = signal |
| **Agent state desync (fan-out)** | Parallel Architects read stale/different system_context versions | Write-lock FormAssignment before spawning workers; version-pin system_context files at spawn time |
| **Rubber-stamp human gates** | High-volume HITL queue → reviewers approve without examining | Gate at form-decision boundary, not output boundary; measure override rate; flag reviewers with 100% approval rate |
| **Tacit assumption loss** | Proposer's implicit exclusions not in output | `excluded_evidence` and `scope_constraints` are required fields in ResearchFinding; validation fails if empty without explicit `"none"` value |
| **Template-fitting bias** | Architect agent has all form schemas in context → picks wrong form | Each Architect agent is form-specific; Pattern Architect has no Skill schema in context; form taxonomy enforced by Router, not the Architect |
| **Too abstract to implement** | Pattern/Skill content is correct but not executable | LLM Judge validation step checks for concrete `steps` / `solution` fields; artifacts with only abstract prose fail semantic check |

---

## System Context File (per target system)

Each system the Architect serves needs one authored-once context file:

```yaml
# system_contexts/{sys_id}.yaml
system_id: "sys_abc"
name: "Human-readable system name"
description: "What this system does"

constraints:
  - "must be compatible with X framework"
  - "no external API calls at inference time"

existing_artifact_inventory:
  patterns:
    - artifact_id: ""
      name: ""
  skills:
    - artifact_id: ""
      name: ""
  rules:
    - artifact_id: ""
      name: ""

preferred_forms:
  - form: "rule"
    when: "for platform-specific constraints"
  - form: "skill"
    when: "for reusable agent capabilities"

schema_overrides: {}   # form-specific field overrides for this system
```

---

## What This Eliminates vs. Human-Process Overhead

| Human-Process Step | Replaced By |
|---|---|
| Panel deliberation on every finding's form | Form Router (automated for high-confidence; human only for ambiguous boundary cases) |
| Per-artifact Trusted Committer review | Validation layer: structural + semantic + LLM judge (automated) |
| Manual provenance tracing | `source_finding_id` on every artifact; filesystem handoff — no summaries |
| Manual coverage gap tracking | Coverage map: `finding → form_assignment → artifact_id[]`; null entries = gaps |
| Multi-target per-human authorship | Parallel Architect workers; one finding → N artifacts |
| Stage-gate sign-off meetings | Confidence-tiered HITL; sign-off only on low-confidence or novel-type findings |

## What Still Requires Human Authorship (Once)

1. **Form taxonomy** — define `pattern | skill | rule | template | persona` + classification examples (seed set for Router calibration)
2. **System context files** — one per downstream system
3. **Validation rules** — structural schemas (JSON Schema) and semantic constraint rules per artifact type
4. **Form Router calibration set** — 50–100 manually classified findings to derive logprob thresholds
5. **Conflict resolution policy** — what happens when cross-system invariants contradict (escalate to which role, time SLA, override authority)

---

## Prior Art References

| Pattern | Domain Analogue | Source |
|---|---|---|
| Form Router (form-agnostic Proposer) | MITRE ATT&CK deliberate separation of threat description from detection form | https://car.mitre.org |
| Filesystem handoff with pointer | Anthropic multi-agent research system (June 2025) | https://www.anthropic.com/engineering/multi-agent-research-system |
| Dissent / override trail | GRADE EtD dissenting views field; ACIP minority opinion requirement | https://www.who.int/publications/i/item/9789240011908 |
| Multi-target fan-out via reference | NIST OSCAL "map once, comply many" (Catalog → multiple SSPs) | https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/ssp/ |
| Compiled AI validation layer | Stanford arXiv 2604.05150 — deterministic artifact from LLM generation | https://arxiv.org/abs/2604.05150 |
| ContractSpec / ABC behavioral contracts | arXiv 2602.22302 — formal agent behavioral contracts | https://arxiv.org/abs/2602.22302 |
| excluded_evidence required field | CMU SEI ML Mismatch Descriptors (data-distribution + API mismatch) | https://www.sei.cmu.edu/library/characterizing-and-detecting-mismatch-in-machine-learning-enabled-systems/ |
| Confidence-tiered HITL | Codebridge HITL regulated workflows (2026) | https://www.codebridge.tech/articles/human-in-the-loop-ai-where-to-place-approval-override-and-audit-controls-in-regulated-workflows |
