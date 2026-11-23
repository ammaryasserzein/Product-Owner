---
title: PO 30-Day AI Catchup (Brief)
date: 2026-11-16
tags: [ai-news, product-owner, catchup-30d, brief]
model: Gemini 4 Hydrogen (XHigh)
---

# PO 30-Day AI Catchup — Brief Edition (2026-10-17 to 2026-11-16)

> [!info] Style Rules
> Every item below uses **1 to 3 plain sentences**: what changed, why it helps a Product Owner without coding, and the source link.

---

## 1. Matt Pocock (`aihero.dev` & `mattpocock/skills`)

- **The Home Repo Pattern (Nov 12, 2026):** Keep one central folder holding your shared `AGENTS.md`, glossary, and reusable Skills, with one-line pointers to your other project folders. For a PO, starting every AI chat inside one main vault like `Schoolvoice-PO` keeps your product rules and vocabulary consistent without duplicating files. [aihero.dev](https://www.aihero.dev/the-home-repo-pattern)
- **`mattpocock/skills` `v1.3.2` (Oct 29, 2026):** Shipped 20 fixes across skills, including wording `/grilling` questions so `"yes"` accepts the recommendation, reading `SKILL.md` first in `ask-matt`, and renaming `CONTEXT.md` to `GLOSSARY.md`. As a non-coder, `/grill-me`, `/to-spec`, `/to-tickets`, `/to-questionnaire`, `/wait-what`, and `/research` directly speed up requirements and backlog writing. [GitHub v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2)
- **`chief-of-staff` Wiki & `software-factory` Beta (Oct 19 – Nov 12, 2026):** `chief-of-staff` now stores cross-session memory in a dated Markdown wiki (`index.md` plus topic pages), while the new `software-factory` beta skill outlines how autonomous task runners enforce review brakes before shipping. For POs, keeping dated decision notes stops AI assistants from treating old, overridden choices as current truth. [chief-of-staff](https://github.com/mattpocock/skills/blob/main/skills/in-progress/chief-of-staff/SKILL.md) · [software-factory](https://github.com/mattpocock/skills/blob/main/skills/in-progress/software-factory/SKILL.md)
- **Evalite & AI SDK v6 Deprecated (Nov 6–9, 2026):** Deprecated `mattpocock/evalite` and made the AI SDK v6 Crash Course free, recommending Langfuse instead for monitoring AI behavior. [evalite](https://github.com/mattpocock/evalite)

---

## 2. Claude (Anthropic)

- **Claude Whiteboards, Sheets, Data & Interactive Connectors (Nov 10, 2026):** Added Whiteboards (beta) for clustering notes into timelines, Sheets (beta) for multi-tab workbooks with formulas, Claude Data (GA) for connecting Amplitude or Snowflake metrics, and side-by-side Interactive Connectors for apps like Jira and Confluence. You can group user interview notes, score a sprint backlog, and inspect live tickets in one window. [Claude Resources](https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors)
- **Claude Meetings (Beta, Nov 10, 2026):** Lets Claude join Google Meet calls as a visible participant on Team and Enterprise plans to take notes, answer questions, and build live docs or whiteboards during the call. This removes manual post-call cleanup after discovery sessions and sprint reviews. [Claude Meetings](https://claude.com/resources/articles/claude-meetings)
- **Claude Duet (Research Preview, Oct 21, 2026):** A proactive assistant (currently on a US Pro/Max/Ultra waitlist) that sends morning briefings from connected email, calendar, and project tools. It pauses with an Approval Card before sending messages or changing files. [Claude Duet](https://claude.com/resources/articles/claude-duet)
- **Open `SKILL.md` Standard & Claude Fable 5.2 (Oct 22 & Nov 9, 2026):** Anthropic donated the `SKILL.md` playbook format to the Linux Foundation's Agentic AI Foundation so one skill file works across tools, and launched Claude Fable 5.2 with 30% faster generation for long documents. [Anthropic News](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation) · [Claude Fable 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)

---

## 3. Google Gemini & Google Workspace

- **Gemini Skills in Google Workspace (Nov 9, 2026):** Google began rolling out modular `/` Skills (replacing Gems) across Gmail, Docs, Slides, Drive, and Chat, letting teams draft and test shared Skills inside Google Docs and stack multiple Skills in one prompt. Skills do not yet work in Google Sheets or Meet, and personal Gemini Skills do not yet auto-sync with Workspace accounts. [Workspace Updates](https://workspaceupdates.googleblog.com/2026/11/skills-in-workspace.html)
- **`@Gemini Notebook` in Gemini Chat (Oct 23, 2026):** Typing `@Gemini Notebook` inside any Gemini conversation lets you create notebooks, send chat text into a notebook, or pull cited answers from existing sources. This bridges open brainstorming and source-grounded discovery without switching tabs. [Workspace Updates](https://workspaceupdates.googleblog.com/2026/10/take-actions-on-your-notebooks-from-Gemini-Notebook-directly-in-the-Gemini-app.html)
- **Sheets Canvas Links & Chat 1-Click Scheduling (Nov 2026):** Google Sheets Canvas mini-apps (trackers, kanbans, dashboards) can now be shared via standalone read-only links, and Google Chat added 1-click meeting scheduling for groups up to five. [Workspace Updates](https://workspaceupdates.googleblog.com/2026/)

---

## 4. Google Antigravity

- **Knowledge Work Interface Layout (Nov 9, 2026):** Choosing Knowledge Work in `Settings > General > Interface Layout` hides Git branches, code diffs, and terminal panes, showing a clean progress line and plain-language permission prompts instead. You can open `Schoolvoice-PO` in this layout to draft PRDs and run research without developer UI clutter. [Antigravity Blog](https://antigravity.google/blog/antigravity-for-knowledge-work/)
- **Voice Mode (Nov 6, 2026):** Added two-way voice chat (`v2.29`) so you can speak instructions, hear short updates, and verbally approve actions hands-free. This works well for turning post-meeting thoughts directly into structured notes. [Antigravity Voice Mode](https://antigravity.google/blog/antigravity-voice-mode/)
- **Hydrogen, Carbon, `/swarm` & Dynamic Workflows (Oct 29 – Nov 13, 2026):** Launched the Plugin Marketplace (Oct 29), Gemini 4 Carbon and `/swarm` parallel subagents (`v2.31.0`, Nov 10), Gemini 4 Hydrogen with Orchestrator routing (Nov 12), and `v2.32.0` Dynamic Workflows plus tighter browser download and frame safety checks (Nov 13). [Antigravity Changelog](https://antigravity.google/docs/changelog/)

---

## 5. Gemini Notebook (formerly NotebookLM)

- **Steerable Slide Decks & Video Overviews (Oct 19, 2026):** Turning on the **Review** toggle lets you edit slide outlines or video producer notes before generating the final stakeholder presentation or video. [Google Blog](https://blog.google/innovation-and-ai/products/gemini-notebook/co-create-slides-videos/)
- **Classroom Insight Summaries & K-12 Controls (Oct–Nov 2026):** Added teacher insight summaries for student engagement and Trusted Domains sharing in Oct 2026, then set Gemini Notebook off by default for K-12 student accounts unless admins opt in (Nov 2026). This provides a clear EdTech benchmark for Schoolvoice permissions and educator insights. [Workspace Updates](https://workspaceupdates.googleblog.com/2026/10/teacher-led-gemini-notebook-in-google-Classroom-now-offers-insight-summaries-for-educators-and-updated-sharing-settings-for-admins-including-trusted-domains.html)

---

## 6. Obsidian (`obsidian-skills` & Core App)

- **`obsidianmd/obsidian-skills` `v1.1.0` (Nov 11, 2026):** Moved officially from `kepano/obsidian-skills` to `obsidianmd/obsidian-skills` as one unified plugin covering Markdown, Bases, JSON Canvas, CLI, `defuddle`, and `knap`. Installing or updating this keeps AI assistants from breaking your wikilinks, tables, or YAML properties. [GitHub Releases](https://github.com/obsidianmd/obsidian-skills/releases)
- **Obsidian `v1.15.0` & `v1.15.1` (Nov 2 & Nov 12, 2026):** Added faster zoomable Mermaid diagrams, draggable Bases filters, append-under-heading for CLI/URI, Relevance-sorted accent-insensitive search, iOS voice Quick Capture, and the mobile Web viewer plugin. These make finding bilingual notes and viewing process diagrams inside your vault much faster. [Desktop Changelog](https://obsidian.md/changelog/2026-11-12-desktop-v1.15.1/)

---

## 7. ChatGPT / OpenAI (Lowest Priority)

- **GPT-6.1 Terra (Oct 26, 2026):** A faster model focused on everyday business writing, reading UI screenshots/mockups, and executing browser or desktop actions. [OpenAI](https://openai.com/index/introducing-gpt-6-1-terra/)
- **ChatGPT "Dots" Updates (Late Oct – Nov 13, 2026):** Always-on background assistants gained custom behavioral instructions and a US Pro beta for iMessage and RCS texting. [OpenAI Help](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)
