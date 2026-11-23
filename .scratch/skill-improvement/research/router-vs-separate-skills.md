# Architectural Patterns for AI Documentation Pipelines: Router vs. Separate Commands

## Executive Summary
When building AI agent systems for "lossless" software documentation pipelines (e.g., transforming Product Requirement Documents (PRDs) into Technical Specifications), a critical architectural decision is whether to use multiple separate agent commands or a single "Router" command with internal orchestration. Research into orchestration patterns (LangGraph, AutoGen) and cognitive load management suggests that a **single Router command with explicit human-in-the-loop (HITL) checkpoints** is the superior approach. It minimizes human cognitive load while utilizing structured artifacts to ensure lossless context transfer between discovery and formulation phases.

---

## 1. Router vs. Separate Agent Commands

### The Case for Separate Commands (/stakeholder-docs -> manual -> /developer-docs)
- **Pros:** Offers granular control and explicit phase boundaries. It forces the human to review the intermediate state before initiating the next phase.
- **Cons:** High cognitive load. It demands the user explicitly manage the pipeline's state, remember the correct sequence of commands, and manually pass context (e.g., file paths or session IDs) between agents. This "manual handoff" causes friction and breaks the seamless agentic experience.

### The Case for a Single Router Command (/po-raw-to-spec)
- **Pros:** Reduces the initial cognitive load by providing a single entry point (the "Switchboard" pattern). The agent system takes responsibility for intent classification, state management, and workflow progression. 
- **Cons:** Requires robust internal state management to prevent the AI from racing ahead and hallucinating without human validation.
- **The Ideal Pattern: Stateful Router with Checkpoints.** 
  Frameworks like **LangGraph** excel here by treating the workflow as a state machine. The router orchestrates the discovery agent, explicitly pauses execution (checkpointing), generates an intermediate artifact (e.g., a markdown summary or BDD scenarios), asks for human approval, and upon approval, routes the state directly to the formulation (developer-docs) agent.

---

## 2. Ensuring "Lossless" Context Transfer

A major challenge in AI pipelines is "lost in the middle" syndrome or context degradation when transitioning from discovery (understanding business intent) to formulation (technical execution). Passing an entire unstructured context window is expensive and error-prone. Top engineering teams use the following strategies:

### Structured Artifacts (The "Narrow Waist" Protocol)
Instead of relying on the agent's internal memory or unstructured chat history, context is externalized into a **durable, structured format**. 
- The discovery agent synthesizes its findings into a strict schema—such as a JSON state file or a structured Markdown artifact (e.g., ADRs or BDD Given/When/Then scenarios).
- This artifact acts as the "source of truth." The formulation agent reads this structured document rather than the raw conversation history. 

### Behavior-Driven Development (BDD) as an Intermediate Language
BDD scenarios bridge the gap between Product Owners and Developers. By having the discovery phase output BDD scenarios, the system creates a lossless translation layer. The intent is explicitly captured in a structured format that the formulation agent can easily translate into technical specs or test-driven development (TDD) scaffolding.

### Context Pruning and External Storage
Rather than passing everything, systems use Context Engineering or Lossless Context Management (LCM). This involves offloading older history and bulky tool results to a filesystem or database (like a untime.db or a memory/ directory) and only passing the synthesized structured metadata to the specialized sub-agent.

---

## 3. Orchestration Patterns: LangGraph vs. AutoGen

- **LangGraph (Graph-based / Flow-centric):** Best suited for documentation pipelines. It defines agents as nodes and transitions as edges, allowing for explicit control over the workflow. Its built-in checkpointers make it trivial to implement the "pause for human review" pattern between the PRD and Tech Spec phases, ensuring state is reliably persisted and passed losslessly.
- **AutoGen (Conversational / Agent-centric):** Focuses on agents talking to each other dynamically. While excellent for open-ended brainstorming or emergent problem-solving, its conversational nature can make strict, lossless phase transitions harder to enforce without careful governance, risking unpredictable behavior in rigid documentation pipelines.

---

## 4. Managing Cognitive Load

While AI automation reduces the extraneous cognitive load of writing boilerplate, it introduces new "metacognitive demands" (AI fatigue)—the mental effort required to verify AI-generated output.
- **Avoid "Workslop":** Do not let the AI generate a massive, monolithic Tech Spec directly from a PRD in one shot. The human verification burden becomes too high.
- **Iterative Checkpoints:** By breaking the router pipeline into smaller, artifact-driven checkpoints (e.g., PRD -> BDD Scenarios -> Tech Spec), the human only needs to validate incremental, structured steps. 
- **Living Documentation:** Treat the intermediate artifacts as living documentation that guides the AI, reducing the "intent debt" over time.

## Conclusion
For a "lossless" software documentation pipeline, adopt a **Stateful Router Architecture** (akin to LangGraph). Use a single command to initiate the workflow, but hardcode internal pauses where the system generates structured artifacts (like BDD scenarios). This offloads orchestration from the human, manages cognitive load through bite-sized verification steps, and uses structured data to guarantee lossless context transfer between specialized agents.
