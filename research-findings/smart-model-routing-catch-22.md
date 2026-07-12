---
name: "Smart Model Routing: the Catch-22 and the Cache-Aware Switching Threshold"
summary: |-
  Per-request "smart" routing (grade each prompt's difficulty, send easy ones to a cheap
  model) has a structural catch-22: to reliably know a prompt is too hard for the cheap
  model, the router must understand it roughly as well as the expensive model would — the
  smarter the router, the more it becomes another big model in front of your big model.
  Evidence it still pays: RouteLLM held ~95% of frontier quality while sending only ~25%
  of requests to the frontier model, and the routing held when models were swapped.
  Second trap: mid-conversation model switches destroy the warm prompt cache — the cold
  reload can swallow the per-token savings, so routers must raise the switching bar once
  a model is warm. Rules-based ("dumb on purpose") routing remains the production
  default.
implementation_notes: null
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "ai-gateway-the-layer-every-ai-stack-eventually-needs.md"
related_findings:
  - file: "ai-gateway-model-traffic-layer.md"
    rel: "extends"
  - file: "no-mid-session-model-switching-subagent-handoff.md"
    rel: "same-problem"
  - file: "model-tier-routing-expensive-orchestrator-cheap-s.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

Two structural limits on dynamic per-request model routing, plus the quantified case for
doing it anyway:

**The catch-22.** A router that reliably grades prompt difficulty must understand the
prompt about as well as the expensive model it's protecting — and if it could, you
wouldn't need the expensive model. The smarter routing gets, the closer it creeps to
being another big model in front of your big model. Routing still pays because a lot of
traffic is *obviously* easy and a cheap check catches it — but there is no free lunch at
the hard end of the distribution.

**The evidence it pays.** The open RouteLLM research project reportedly held ~95% of a
frontier model's quality while sending only ~25% of requests to it, with the rest going
to a far cheaper model most users couldn't distinguish — and the routing held up when
different models were swapped in on both ends (transferability is why the result is taken
seriously).

**The cache-aware switching threshold.** Modern sessions lean on a warm provider-side
prompt cache. A router that switches models mid-conversation to save a few cents forces
the new model to re-read the entire conversation cold; that one-time reload can swallow
the per-token savings and more — price-per-token optimized, token count blown up. The
fix: make the router cache-aware — once a model is warm, raise the bar for switching away
so a jump happens only when savings clearly beat the cost of going cold. "Route to
whatever's cheapest" is worse advice than it sounds.

**The production default.** Most production systems run routing that is "dumb on
purpose": hand-written rules (cheap requests here, this customer there, fall back to that
model when the main one is down). Predictable and debuggable; smart routing is the
add-on, not the foundation.

## Why It Matters

The KB's routing findings to date are topology-level (expensive orchestrator, cheap
subagents; session-pinned models with subagent hand-off). This finding adds the limits
layer: why per-request dynamic routing cannot fully deliver its pitch, the one quantified
datapoint (RouteLLM 95%/25%) worth citing, and the cache-aware threshold rule any
routing design must respect. It independently corroborates the KB's
no-mid-session-model-switching finding from a second channel: same cache economics,
discovered at the gateway layer instead of the harness layer. Note the transcript's aside
that this routing "is also increasingly happening in your favorite frontier coding
harness" — the trade-offs follow it there.

## Why People Are Using It

Cost pressure makes routing the most-marketed gateway feature; RouteLLM gives the pitch
real numbers. The rules-based default persists precisely because practitioners keep
rediscovering the catch-22 and the cache trap in production.

## Potential Alternatives

- **Static topology routing** (existing KB pattern): assign models to roles/tasks ahead
  of time; no per-request grading at all.
- **Session-pinned model + subagent hand-off** (existing KB pattern): sidesteps the
  cache trap by making model choice a session-boundary decision.
- **Rules-only routing:** keep the dumb-on-purpose layer and skip difficulty grading
  entirely.

## Potential Improvements

- Cache-state as an explicit router input (warm-cache penalty term in the switch
  decision), not a heuristic bolt-on.
- Difficulty grading only at conversation/session start, never mid-stream — combining
  this finding with the KB's session-pinning rule.

## Potential Failure Modes

- **Router-as-second-big-model:** grading cost and latency creep until the router erases
  its own savings.
- **Cache-blind switching:** the headline failure — cheaper per token, more tokens.
- **Misrouted hard prompts:** the cheap model confidently mishandles the exact prompts
  the router couldn't recognize as hard (the catch-22 made operational).
- **Unverified datapoint:** the RouteLLM figures are as-reported by the source, not
  independently checked against the paper.
