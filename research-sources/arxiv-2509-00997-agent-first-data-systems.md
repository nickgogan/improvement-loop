---
name: "Supporting Our AI Overlords: Redesigning Data Systems to be Agent-First"
source_type: "Research Paper"
status: "Done"
key_takeaways: "Position paper arguing data systems must adapt to LLM-agent workloads, which the authors call 'agentic speculation' — high-throughput exploration and solution formulation. Four characteristics of agentic workloads: scale, heterogeneity, redundancy, steerability. Proposes new research directions across query interfaces, query processing, and agentic memory stores. No benchmarks; vision paper from UC Berkeley and collaborators."
relevance: "Medium"
added_by: "Nick"
tags:
  - "memory"
  - "orchestration"
  - "data-systems"
  - "agentic-workloads"
  - "research-direction"
url: "https://arxiv.org/abs/2509.00997"
authority:
  - "uc-berkeley-epic-lab.md"
findings:
  - "agentic-speculation-four-characteristics-data-system-redesign.md"
date_added: "2026-04-20"
date_processed: "2026-04-20"
---

# Supporting Our AI Overlords: Redesigning Data Systems to be Agent-First

arXiv:2509.00997. v1 submitted 31 Aug 2025; v2 on 6 Dec 2025. Authors: Shu Liu, Soujanya Ponnapalli, Shreya Shankar, Sepanta Zeighami, Alan Zhu, Shubham Agarwal, Ruiqi Chen, Samion Suwito, Shuo Yuan, Ion Stoica, Matei Zaharia, Alvin Cheung, Natacha Crooks, Joseph E. Gonzalez, Aditya G. Parameswaran. Categories: cs.AI, cs.DB.

## Abstract (Verbatim)

"Large Language Model (LLM) agents, acting on their users' behalf to manipulate and analyze data, are likely to become the dominant workload for data systems in the future. When working with data, agents employ a high-throughput process of exploration and solution formulation for the given task, one we call agentic speculation. The sheer volume and inefficiencies of agentic speculation can pose challenges for present-day data systems. We argue that data systems need to adapt to more natively support agentic workloads. We take advantage of the characteristics of agentic speculation that we identify, i.e., scale, heterogeneity, redundancy, and steerability - to outline a number of new research opportunities for a new agent-first data systems architecture, ranging from new query interfaces, to new query processing techniques, to new agentic memory stores."

## Four Characteristics of Agentic Speculation

1. **Scale** — volume of exploratory queries per task dwarfs traditional query workloads
2. **Heterogeneity** — queries cross modalities, schemas, and data systems
3. **Redundancy** — repeated or near-duplicate exploration paths within and across tasks
4. **Steerability** — queries can be redirected mid-flight based on intermediate findings

## Proposed Research Directions

- New query interfaces adapted to agent-first workloads
- New query processing techniques exploiting redundancy/steerability
- New agentic memory stores

## Resources

- PDF: https://arxiv.org/pdf/2509.00997
- HTML: https://arxiv.org/html/2509.00997v2
