---
notion_id: 30f1e08b-9b34-812c-a684-d74217f0e26c
title: "Framework Integration Map"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# Framework Integration Map

> **For agents:** This is the definitive reference for which productivity framework operates in which ICOR stage. Before modifying any workflow, database schema, or automation, consult this table to understand which framework "owns" that functionality.

## The Master Mapping

| Framework | ICOR Stage(s) | Primary Role | How It Maps In |
|-----------|---------------|--------------|----------------|
| **ICOR** | Meta-framework | The operating system. Unifies all others. | Input → Control → Output → Refine is the master flow. Every other framework is an application running on top of ICOR. |
| **PARA** | All stages | Structural taxonomy — WHERE information lives. | Projects (Output), Areas (all stages, as Key Elements), Resources (Control/PKM), Archives (Refine). Answers "where does this go?" after the Control routing question. |
| **CODE** | Input + Control + Output | Knowledge lifecycle — how raw information becomes usable knowledge. | Capture (Input), Organize + Distill (Control), Express (Output). The knowledge pathway within ICOR, running parallel to the action pathway. |
| **Zettelkasten** | Input + Control + Refine | Deep knowledge layer — atomic, evergreen, connected notes. | Fleeting Notes (Input), Literature + Permanent Notes (Control depth), Evergreen refinement (Refine). Lives in Heptabase (Phase 2), bridged to Notion via Project Notes. |
| **OKR** | Control + Output + Refine | Goal architecture — why we do what we do. | Vision (frames the Capturing Beast), Key Results (Control routing priority), Projects/Tasks (Output structure), Quarterly/Annual Reviews (Refine). The strategic skeleton of Output. |
| **GTD-Lite** | All stages | Execution mechanics — friction-free task handling. | Capture (Input), Clarify + Organize (Control), Engage (Output), Weekly Reflect (split: system reflection = Refine; inbox processing = Control). The friction-reduction layer. |
| **OODA** | All stages (micro-loop) | Decision engine — how judgment is applied. | Observe (Input), Orient + Decide (Control), Act (Output), loop back (Refine). OODA is not a separate framework — it IS the ICOR flow at micro-scale. Every ICOR cycle runs an OODA loop. |

---

## Key Insight

A framework appearing in multiple ICOR stages is not a flaw — it means the framework provides capabilities relevant at different moments in the flow. OODA and GTD-Lite appear in all stages because they describe **mechanics** (decision-making, friction-reduction) rather than content types.

---

## Overlaps Resolved

Seven structural tensions between frameworks were identified and resolved in WS1. The binding resolutions:

1. **Capture duplication (CODE vs GTD vs ICOR Input):** ICOR Input is the stage name. GTD/CODE Capture are the same implementation step described twice. Use ICOR as the canonical term.
2. **Organize duplication (CODE vs GTD Clarify):** GTD asks the routing QUESTION ("actionable?"). CODE determines the DESTINATION. Both happen in Control.
3. **Knowledge processing (CODE Distill vs Zettelkasten vs OODA Orient):** Three DEPTHS of processing. OODA Orient = fast/in-the-moment. CODE Distill = medium extraction. Zettelkasten = deep synthesis. All coexist in Control.
4. **Goal hierarchy (OKR vs GTD vs Execution Beast):** OKR = strategic layer (why→what). Execution Beast = tactical layer (what→how→when). GTD is demoted to execution mechanics only.
5. **PARA vs ICOR Domains:** Orthogonal taxonomies. PARA = content type. ICOR Domains = ownership + purpose. PARA nests INSIDE ICOR domains.
6. **Weekly Review (GTD Reflect vs ICOR Refine):** Family Meeting is split: first ~20 min = Control work (inbox processing). Last ~10 min = Refine work (system health).
7. **OODA as parallel vs. part of ICOR:** OODA IS ICOR at micro-scale. Observe=Input, Orient+Decide=Control, Act=Output, feedback=Refine. Label the Control decision-making logic "OODA" when precision is needed.

---

*Source: WS1_ICOR_Integration_Map.docx, Section 2 and Section 4*
