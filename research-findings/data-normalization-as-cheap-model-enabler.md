---
name: "Data Normalization as Cheap-Model Enabler"
summary: |-
  Plain English: the expensive model is usually compensating for dirty data — clean,
  normalized, addressable data lets lightweight/open-source models do the same high-trust
  work. "When dates are dates and every claim has an address, you stop needing the most
  expensive model for most of the work." The upstream investment (ingest, chunk, normalize,
  store with citations — including making missing documents explicit records) is what
  makes model choice flexible downstream; the source frames it as the same play Apple runs
  with on-device models. Inverts the usual routing question: instead of "which model is
  smart enough for this mess," ask "how clean does the data have to be before the cheap
  model suffices."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "General"
adopted_in: []
sources:
  - "i-pointed-my-agent-at-the-bills.md"
related_findings:
  - file: "nine-primitive-document-agent-skeleton.md"
    rel: "enabled-by"
  - file: "task-specific-model-routing-table-march-2026-bench.md"
    rel: "same-problem"
  - file: "context-curation-over-context-stuffing.md"
    rel: "same-problem"
  - file: "data-permanent-software-ephemeral-architecture.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# Data Normalization as Cheap-Model Enabler

## What It Is

A causal claim about model routing: data quality, not model intelligence, is the binding
constraint on most document-work tasks. Frontier models are effectively being paid to
compensate for unstructured mess — inferring which date is the deadline, which number is
the claim amount, which PDF is current. Normalize upstream (typed fields, explicit
missing-data records, source-addressed chunks in a local store) and the per-task
intelligence requirement drops enough that lightweight and open-source models handle the
work. The source's answer to "what's the cheapest model?" is "the open-source model —
once the data underneath is clean."

## Why It Matters

It connects two KB threads that usually run separately: context engineering (curation,
structure) and model economics (routing, tier selection). The practical consequence: cost
optimization should often be spent on ingest/normalize pipelines rather than on smarter
routing over dirty data. This also gives the tier-routing findings their enabling
precondition — downshift routing tables silently assume the cheap model receives clean
inputs.

## Why People Are Using It

Demonstrated across the source's three builds (the tax build runs mostly on structure, not
reasoning); echoed by the platform trend it names (Apple's on-device strategy). Pairs with
frontier-access volatility: clean data is the asset that survives model churn.

## Potential Improvements

Quantify the effect (same task, same model tiers, clean vs raw inputs); define minimum
normalization contracts per task class so routing tables can key on data-cleanliness as an
input.

## Potential Failure Modes

Normalization itself needs intelligence — garbage normalization by a cheap model poisons
everything downstream (use the strong model at ingest time, or verify). Over-normalization
ossifies: schemas tuned for today's queries drop information tomorrow's task needs. The
claim is directional practitioner wisdom, not yet benchmarked.
