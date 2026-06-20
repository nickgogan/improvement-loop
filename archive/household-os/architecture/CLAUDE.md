---
notion_id: "30f1e08b-9b34-8176-9be1-db43abc21d15"
title: "Architecture"
parent: "Meta-System"
extracted: "2026-04-04"
---

> **For agents:** This section contains the system design documentation for the Household Operating System across all four systems. Each child page covers a distinct system's architecture. For governance rules (Constitution, Vocabulary, Codified Practices, Agent/Skills Architecture), see [System Governance](32b1e08b-9b34-818e-a5bb-c44a38c76b37) (peer section under Meta-System). Per DD-42, the Design Decisions and Implementation Backlog databases are **top-level peers** in the Household Teamspace (Governance Infrastructure layer), not children of this page.

The Household Operating System spans four distinct systems (S1-S4) plus a meta-system (Improvement Loop). This Architecture section documents the design rationale for each system.

---

# System Sections

[Four-System Separation Model](3251e08b-9b34-8197-967f-e07f13f62500)

Defines the four systems (S1-S4), ownership boundaries, boundary rules, and the three Teamspace layers (DD-42). Read this first to understand how the systems relate.

[S2: Notion Operations Architecture](32b1e08b-9b34-81e2-8808-e76052c53179)

The running operational system -- ICOR framework, orchestrators, lifecycle workflows, domain specs, and workspace structure. The largest and most mature system.

[S3: Claude Code Build Architecture](32b1e08b-9b34-813a-8096-fafec33b8e61)

The builder system -- vault architecture, skill definitions, and schema modification workflows. S3 produces the schema that S2 consumes.

[Improvement Loop Architecture](32b1e08b-9b34-815c-808e-dce34af87d8f)

The meta-system that researches, proposes, evaluates, enhances, and codifies improvements to S2, S3, and itself.
