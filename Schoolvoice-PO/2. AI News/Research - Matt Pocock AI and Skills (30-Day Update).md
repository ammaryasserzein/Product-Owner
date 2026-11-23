---
title: "Research - Matt Pocock AI and Skills (30-Day Update)"
date: 2026-11-16
tags: [ai-research, matt-pocock, skills, 30d-update]
model: Gemini 4 Hydrogen (XHigh)
---

# Matt Pocock AI Ecosystem & `mattpocock/skills` — 30-Day Research Update (2026-10-17 to 2026-11-16)

> **Research Scope & Primary Sources:** Verified directly against the [`mattpocock/skills`](https://github.com/mattpocock/skills) repository (Git tree, `README.md`, `CHANGELOG.md`, `SKILL.md` files, commits, releases, and PRs), [`mattpocock/dictionary-of-ai-coding`](https://github.com/mattpocock/dictionary-of-ai-coding), [`mattpocock/sandcastle`](https://github.com/mattpocock/sandcastle), [`mattpocock/evalite`](https://github.com/mattpocock/evalite), [`aihero.dev`](https://www.aihero.dev/) (`sitemap.xml`, `rss.xml`, `llms.txt`, `skills.md`, articles, cohort pages), Matt Pocock's official YouTube RSS feed (`@mattpocockuk`), and `arXiv:2610.34938`.
> **Observed Scale (as of 2026-11-16):** `mattpocock/skills` sits at **325,655+ GitHub stars**, `mattpocock/sandcastle` at **9,110 stars**, and `mattpocock/dictionary-of-ai-coding` at **5,504 stars**.

---

## 1. Verified Updates in the Last 30 Days (2026-10-17 – 2026-11-16)

Matt Pocock's focus over the past 30 days centered on four major shifts: **(1) multi-repo & persistent-wiki orchestration** (the **Home Repo Pattern** and `chief-of-staff` wiki architecture), **(2) software factory design & npm distribution** (`software-factory` skill, Cohort 005, Sandcastle hardening, and `@mattpocock/skills` npm packaging PR), **(3) subagent context isolation** (fresh context windows instead of forked conversations), and **(4) deprecating older eval/v6 workshop tooling** in favor of Langfuse and production agent engineering.

### 1.1 Timeline of Verified Releases, Commits, Articles & Videos

| Date (UTC) | Surface | What Happened (Primary Source) |
| :--- | :--- | :--- |
| **2026-10-19** | `mattpocock/skills` (`in-progress`) | **Commit [`5beb35b`](https://github.com/mattpocock/skills/commit/5beb35b040e3de97e54fa9e386d7e42d15c295c2) / PR #1304:** `chief-of-staff` moved its cross-session memory into an **LLM wiki** (`index.md` + one page per topic maintained via **Ingest**, **Query**, **Lint**), written strictly as a dated, commit-cited historical record. |
| **2026-10-26** | Academic Paper (`arXiv`) | **Paper [`arXiv:2610.34938`](https://arxiv.org/abs/2610.34938):** Christoph Treude & Sebastian Baltes published *"How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation"*, specifically studying Matt's `/retro` skill on 30 SWE-bench Verified issues (125 proposals coded, 24 implemented, 12 evaluated). |
| **2026-10-27** | `mattpocock/skills` (Engineering) | **Commit [`ed0de59`](https://github.com/mattpocock/skills/commit/ed0de59eb5de8c2730a650cc69f588ffa64c1040) / PR #1228:** `setup-matt-pocock-skills` now verifies/wires a reachable git remote before configuring GitHub/GitLab trackers, offers `git mv` for legacy `CONTEXT.md` → `GLOSSARY.md` files, and fixes GitHub/GitLab tracker templates (`comment-then-close`, PR body reads, native `gh` blocking flags, open-blocker counts, `glab -O json`). |
| **2026-10-27** | `mattpocock/skills` (Governance) | **Commit [`59db609`](https://github.com/mattpocock/skills/commit/59db609eb1e18aaf59b63284d0e52255aff0c63c) / PR #1169:** Added `CONTRIBUTING.md`, disabled blank GitHub issues, routed questions/new-skill ideas to Discussions, and updated `issue-tracker-github.md` so agents never file issues into `mattpocock/skills` instead of the user's own repo. |
| **2026-10-29** | `mattpocock/skills` (Cross-Skill) | **Commit [`7739eae`](https://github.com/mattpocock/skills/commit/7739eaed7f8f3915437a8def198a6d0d7206dbc7) / PR #1341:** Updated `CLAUDE.md` and 8 subagent-using skills (`implement-spec`, `code-review`, `codebase-design`, `improve-codebase-architecture`, `wayfinder`, `research`, `grilling`, `chief-of-staff`) to **start subagents with a fresh context window, not a fork** (fixing Codex's default fork behavior). |
| **2026-10-29** | `mattpocock/skills` (**Release `v1.3.2`**) | **[Release `v1.3.2`](https://github.com/mattpocock/skills/releases/tag/v1.3.2) (`d1478fc`, PR #1161):** Bundled 20 patch improvements spanning Oct 6–29, including `ask-matt` reading each skill's `SKILL.md` before summarizing/skipping (#1194), `grilling` wording questions so `"yes"` accepts the recommendation (#1193), `code-review` foreground subagents & standards discovery (#1208), `diagnosing-bugs` mutation diff checks (#1209), `to-tickets` native sub-issues (#1188), `wayfinder` fixes (#1181), `teach` workspace anchoring (#1183), and `wizard` template fixes (#1198, #1237). |
| **2026-10-29** | `mattpocock/skills` (Engineering) | **Commit [`a496f55`](https://github.com/mattpocock/skills/commit/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa) / PR #1342 (post-`v1.3.2`, unreleased on `main`):** `implement-spec` updated to spawn a fresh implementer subagent per ticket. |
| **2026-10-31** | `mattpocock/skills` (`in-progress`) | **Commit [`5ae4816`](https://github.com/mattpocock/skills/commit/5ae481693d13b37d4d2c2c92d0b66d299c93e695) / PR #1363 (unreleased):** `chief-of-staff` updated to check for an existing shared wiki first, run `/retro` on ~1-in-5 subagent runs, and reference `retro`, `to-spec`, `to-tickets`, and `implement-spec` as relative sibling procedures. |
| **2026-10-31** | `mattpocock/skills` (**New Beta Skill**) | **Commit [`4ae2317`](https://github.com/mattpocock/skills/commit/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d) / PR #1316 (unreleased):** Added **`software-factory`** to `skills/in-progress/`—a canonical vocabulary & slot-survey skill for designing agent factories (`SKILL.md` + `EXAMPLE-TASKS.md`, `TICKET-TRACKERS.md`, `GIT-HOSTS.md`, `RUNNERS.md`, `OBSERVABILITY-PLATFORMS.md`). |
| **2026-11-04** | YouTube (`@mattpocockuk`) | **Short:** [Junior engineers: don't wait for permission](https://www.youtube.com/shorts/Z1saoyb_98M). |
| **2026-11-05** | YouTube (`@mattpocockuk`) | **Short:** [Is vibe coding an insult?](https://www.youtube.com/shorts/Jy8vX_CIsBw). |
| **2026-11-06** | YouTube + `aihero.dev` | **Short:** [Someone wrote a PAPER about my skill](https://www.youtube.com/shorts/KJr1Q-k-yH0) (covering `arXiv:2610.34938` on `/retro`). Same day (`lastmod: 2026-11-06`), [AI SDK v6 Crash Course](https://www.aihero.dev/workshops/ai-sdk-v6-crash-course) was updated as **deprecated and free for everyone**, advising **Langfuse** over Evalite. |
| **2026-11-09** | `aihero.dev` + `evalite` | **Cohort 005 Launch:** [Software Factories for Real Engineers](https://www.aihero.dev/cohorts/software-factories-for-real-engineers) 2-week cohort started Nov 9, 2026 (prepared via `cohort-005-project-fork-2` on Oct 21 & `fork-3` on Oct 28). Same day, PR #409 ([`4129d73`](https://github.com/mattpocock/evalite/commit/4129d73)) formally deprecated [`mattpocock/evalite`](https://github.com/mattpocock/evalite) with Langfuse migration notes. |
| **2026-11-11** | YouTube + `mattpocock/skills` | **Livestream:** [LIVE: Writing code that doesn't suck with the creators of Pi](https://www.youtube.com/watch?v=ZBTegd8DUZM) (with Mario Zechner & Armin Ronacher). Commit [`d18183f`](https://github.com/mattpocock/skills/commit/d18183fe9d96e1240105a8534e53591e9b49afd7) (merged **2026-11-12** via PR [#1416](https://github.com/mattpocock/skills/pull/1416), `5863806`) refined `software-factory` from Cohort 005 student feedback (rejecting `"job"` for `"task"`, and ensuring the `explore` task reproduces claims and leaves findings). |
| **2026-11-12** | `aihero.dev` + YouTube + Dictionary | **Major Launch — The Home Repo Pattern:** Published [The Home Repo Pattern](https://www.aihero.dev/the-home-repo-pattern) (with a 4-step copy-paste setup prompt), full video [The Home Repo: The effortless multi-repo agent setup](https://www.youtube.com/watch?v=hWe-j78vNpc), and Short [The Home Repo Pattern](https://www.youtube.com/shorts/zyQxyNQZ8B4). Same day, PR #34 ([`8a56b8a`](https://github.com/mattpocock/dictionary-of-ai-coding/commit/8a56b8a)) added **[Home Repo](https://www.aihero.dev/ai-coding-dictionary/home-repo)** to `dictionary-of-ai-coding`, refreshing all 72 dictionary entries in `aihero.dev/rss.xml` and `sitemap.xml`. |
| **2026-11-01 – 2026-11-13** | `mattpocock/skills` (**Open PRs in Flight**) | Active unmerged PRs reveal immediate roadmap priorities: **[#1368](https://github.com/mattpocock/skills/pull/1368)** (publish promoted skills to npm as `@mattpocock/skills` with OIDC provenance so **Sandcastle** & factories can pin versions; updated Nov 13), **[#1422](https://github.com/mattpocock/skills/pull/1422) & [#1429](https://github.com/mattpocock/skills/pull/1429)** (`animatic` & `setup-animatic` in-progress skills for narrated still-frame PR/topic videos; updated Nov 13), **[#1369](https://github.com/mattpocock/skills/pull/1369)** (`chief-of-staff: work toward a revisable destination`, noting it *"may replace `wayfinder`"*; updated Nov 6), and **[#1343](https://github.com/mattpocock/skills/pull/1343)** (`chore: version skills` pending next release; updated Nov 12). |
| **Through 2026-11-16** | `mattpocock/sandcastle` | Ongoing daily development (`pushed_at: 2026-11-16T12:14:10Z`, PRs #1656–#1659) on **Sandcastle**, his TypeScript sandboxed coding-agent orchestrator (`sandcastle.run()`). |

> **Pre-Window Context (Early October 2026 — Before Oct 17):**
> To avoid date confusion, note that **`v1.3.0` / `v1.3.1`** (which graduated `/implement-spec`, `/pr`, and `/retro`, retired `resolving-merge-conflicts`, and renamed `CONTEXT.md` → `GLOSSARY.md`) shipped on **2026-10-04** ([aihero.dev v1.3 changelog](https://www.aihero.dev/skills/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md) published `2026-10-05`), and the **`README.md` update** leading with self-updating native plugin installs for Codex and GitHub Copilot landed on **2026-10-08** (`b0618bc` / PR #1218; [ADR-0002](https://github.com/mattpocock/skills/blob/main/.agents/adr/0002-ship-as-a-claude-code-plugin.md)). Meanwhile, `software-factory` and `dark-factory` entries were originally committed to `dictionary-of-ai-coding` on **2026-09-24** (`813001a`), though the whole dictionary was republished in `aihero.dev/rss.xml` on **2026-11-12**.

### 1.2 Deep-Dive on the Three Biggest Recent Patterns (Oct–Nov 2026)

1. **The Home Repo Pattern (`2026-11-12`)** — [aihero.dev/the-home-repo-pattern](https://www.aihero.dev/the-home-repo-pattern)
   - **Problem:** When work spans multiple repos, starting an agent inside one repo blinds it to the others and causes skills, `AGENTS.md`, and docs to duplicate and drift.
   - **Pattern:** Create one central **Home Repo** holding shared skills, `AGENTS.md`/`CLAUDE.md`, shared docs (glossaries, standards, ADRs, personal wiki), and optional CLI tooling—plus one-line **context pointers** (`<name> (<what it is>): <local path>. Clone from <remote> if missing.`) pointing at child repos. You start all sessions from the Home Repo.
   - **Scale limits explicitly documented:** Works flat up to ~20 repos; around ~400 repos, replace flat lines with **progressive disclosure** (`repos/<area>.md`); at thousands of repos, switch to a skills marketplace. (Old rejected names: `"agent repo"`, `"meta-repo"`.)
2. **`chief-of-staff` + Persistent Dated LLM Wiki (`2026-10-19` & `2026-10-31`)** — [`skills/in-progress/chief-of-staff/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/in-progress/chief-of-staff/SKILL.md)
   - Acts as a long-running orchestrator doing all work in fresh-context subagents via sparse context pointers, thinking simultaneously on **Tactical** (immediate task) and **Strategic** (environment/pit-of-success) tracks.
   - Stores memory in a shared markdown **wiki** (`index.md` + topic pages maintained via **Ingest**, **Query**, **Lint**) where **every claim is dated** and code claims cite repo + commit SHA—never rewriting old claims, only marking them superseded.
   - Open PR #1369 explicitly explores merging `wayfinder`'s `Destination` + `Fog of war` + `Out of scope` tracking into `chief-of-staff`, noting `chief-of-staff` may supersede `wayfinder` because its wiki outlives single sessions.
3. **`software-factory` Skill (`2026-10-31`, refined `2026-11-11/12`)** — [`skills/in-progress/software-factory/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/in-progress/software-factory/SKILL.md)
   - Defines an opinionated architecture vocabulary for autonomous/AFK agent pipelines:
     - **Tasks & Runs:** `Task` (avoid *job/workflow/action*), `Trigger`, `Run` (black-box execution that never waits mid-run for a human; avoid *session*), `Runner` (disposable machine; avoid *server/box/sandbox*).
     - **Services (6 slots):** `Ticket tracker` (human interface), `Ticket source`, `Git host`, `Orchestrator`, `Runner`, `Observability platform` (optional).
     - **The Golden Rule — Accelerators vs. Brakes:** *"Every trigger is an accelerator. Accelerators without brakes make a slop cannon."* Enforces **3 brakes**: (1) Automated checks (types/lint/tests), (2) Automated cold-diff review, and (3) Human PR review, throttled slowly at rollout.

---

## 2. Complete Breakdown of Matt Pocock's Skills & Workflows

### 2.1 Architecture, Invocation Model & Installation

As documented in [`.agents/invocation.md`](https://github.com/mattpocock/skills/blob/main/.agents/invocation.md), [`.claude-plugin/plugin.json`](https://github.com/mattpocock/skills/blob/main/.claude-plugin/plugin.json), and [`README.md`](https://github.com/mattpocock/skills/blob/main/README.md), the repository contains **39 skills on `main`** across 4 buckets:
- **User-invoked skills** (`disable-model-invocation: true` in `SKILL.md`, `policy.allow_implicit_invocation: false` in `agents/openai.yaml`): Only run when the user types `/skill` (or `$skill` in Codex). They **orchestrate** workflows and may call model-invoked skills via `Call the Skill tool with "<name>"`, but **never** call another user-invoked skill.
- **Model-invoked skills**: Can be called explicitly by the user OR loaded automatically by the agent when its description matches. They hold reusable discipline and vocabulary.

#### Installation Paths (per `README.md` & `skills/in-progress/README.md`)
- **Self-updating Plugins (Promoted 27 skills — 20 Engineering + 7 Productivity):**
  - **Claude Code:** `claude plugin install mattpocock-skills@claude-plugins-official`
  - **Codex:** `codex plugin marketplace add mattpocock/skills` then `codex plugin add mattpocock-skills@mattpocock`
  - **GitHub Copilot (CLI / VS Code):** `copilot plugin marketplace add mattpocock/skills` + `copilot plugin install mattpocock-skills@mattpocock` (plus `autoUpdate: true` in `~/.copilot/settings.json`), or VS Code `Chat: Install Plugin From Source` → `https://github.com/mattpocock/skills`.
- **Manual / Editable Copies (Cursor, OpenCode, Windsurf, Gemini CLI, Antigravity, etc.):**
  - Universal: `npx skills@latest add mattpocock/skills -a <agent>` (update via `npx skills@latest update`).
  - Gemini CLI: `gemini skills install https://github.com/mattpocock/skills.git --path skills/engineering` (and `--path skills/productivity`).
  - Beta `in-progress` skills (excluded from plugins): `npx skills@latest add mattpocock/skills --skill=<name>`.

---

### 2.2 The Main Workflow Spine (`ask-matt` Map)

From [`skills/engineering/ask-matt/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md) and [`PHASE-BOUNDARIES.md`](https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/PHASE-BOUNDARIES.md):

1. **Setup once per workspace:** `/setup-matt-pocock-skills`
2. **Idea → Ship Spine:**
   - **Step 1 (Sharpen):** `/grill-with-docs` (in a workspace/repo — stateful, writes `GLOSSARY.md` + ADRs) OR `/grill-me` (stateless, no repo/docs).
   - **Step 2 (Optional Runnable Question Detour):** `/handoff` → `/prototype` (single HTML logic demo or multi-variant UI route) → `/handoff` back.
   - **Step 3 (Build):** Keep steps 1–3 in one unbroken context window inside the **smart zone** (~150k tokens) until ticketing finishes:
     - *Multi-session build:* `/to-spec` → `/to-tickets` → then either `/implement` per ticket (with `/clear` between tickets) OR `/implement-spec` (parallel subagent worktrees across the task graph).
     - *Single-session build:* `/implement` directly.
     - *Underneath:* `/tdd` (red-green vertical slices) → `/code-review` (parallel Standards + Spec subagents) → `/pr` (visual summary + before/after evidence + one-way/two-way door risk).
   - **Step 4 (Close the Loop):** `/retro` (run before `/clear`, proposing environment/lint/doc fixes, never code fixes).
3. **On-Ramps into the Main Flow:**
   - Raw incoming bugs/requests → `/triage` → `/implement`
   - Hard/flaky bugs → `/diagnosing-bugs` → `/retro`
   - Huge multi-session foggy initiatives → `/wayfinder` (decision tickets) → `/to-spec` → `/to-tickets`
4. **Phase Boundary Decision Tree (`PHASE-BOUNDARIES.md`):** At every phase boundary (never mid-phase), ask in strict order: (1) Continue in session (preserve primary source if within smart zone)? → (2) `/clear` (context irrelevant)? → (3) `/handoff` (switching harness, directory, colleague, or mid-phase fork)? → (4) Subagent (AFK-capable)? → (5) `/compact` (last-resort default).

---

### 2.3 Complete Skill-by-Skill Catalog (All 39 Skills on `main` + Pending PRs)

#### A. Engineering Bucket (20 Promoted Skills)
| Skill | Invocation | What It Actually Does (`SKILL.md`) |
| :--- | :--- | :--- |
| **`/ask-matt`** | User | Official router over all user-invoked skills and `PHASE-BOUNDARIES.md`; reads target `SKILL.md` before explaining or skipping steps. |
| **`/setup-matt-pocock-skills`** | User | Run once per workspace/repo. Detects git remote, legacy `CONTEXT.md`, and monorepo signals; configures `CLAUDE.md`/`AGENTS.md` + `docs/agents/issue-tracker.md` (GitHub, GitLab, **Local Markdown `.scratch/`**, or **Other freeform** like Jira/Linear), `triage-labels.md`, and `domain.md`. |
| **`/grill-with-docs`** | User | Calls `grilling` + `domain-modeling` together: relentless design-tree interview that simultaneously builds `GLOSSARY.md` and `docs/adr/`. |
| **`/to-spec`** | User | Synthesizes current conversation into a structured spec (**no interview**) — Problem Statement, Solution, extensive User Stories, Implementation Decisions (no stale file paths), Testing Decisions, Out of Scope — checks test seams with user, and publishes to the configured tracker as `ready-for-agent`. |
| **`/to-tickets`** | User | Breaks a spec/plan into **tracer-bullet vertical slices** (complete user-facing end-to-end paths sized for one fresh context window, using expand–contract only for wide mechanical refactors), declares `Blocked by` edges, quizzes granularity with the user, and writes per-ticket files (`.scratch/<slug>/issues/NN-slug.md`) or native sub-issues. |
| **`/wayfinder`** | User | Plans huge multi-session efforts ("fog of war") as a `wayfinder:map` issue with child **decision tickets** (`research`, `prototype`, `grilling`, `task`), tracking `Decisions so far`, `Not yet specified` (fog), and `Out of scope`. Resolves max 1 HITL ticket per session, then hands off to `/to-spec`. |
| **`/triage`** | User | State machine (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`) for incoming issues/external PRs. Checks for redundancy and `.out-of-scope/*.md`, reproduces claims before grilling, and writes durable agent briefs or `.out-of-scope/` rejections. |
| **`/implement`** | User | Builds a single ticket or spec: fetches ticket title, invokes `tdd` at pre-agreed seams, runs checks/tests, invokes `code-review`, and commits. |
| **`/implement-spec`** | User | Orchestrates an entire spec on an integration branch: reads tickets as a task graph, dispatches fresh-context implementer subagents in isolated git worktrees across the unblocked frontier, merges via merger subagents, and closes with `code-review`. |
| **`/improve-codebase-architecture`** | User | Scans git hotspots via fresh subagent for shallow modules ("deletion test"), generates a self-contained Tailwind+Mermaid HTML report in `%TEMP%`/`$TMPDIR` with `Strong`/`Worth exploring`/`Speculative` badges, then grills the chosen candidate. |
| **`/retro`** | User | Reviews session logs/history and proposes environment improvements ranked by severity: Navigation, Automated checks, Coding standards (mechanical → deterministic lint/CI; judgement calls → `CODING_STANDARDS.md`), Global `AGENTS.md`, Tool economy, No-ops, Information access. |
| **`prototype`** | Model | Builds throwaway evidence on a `prototype/<name>` branch: **Logic branch** produces a single double-clickable HTML file with free-play buttons & tabbed guided walkthroughs; **UI branch** builds multiple radically different UI variations toggleable on one route. |
| **`diagnosing-bugs`** | Model | 6-phase strict bug loop: (1) Build a tight red-capable feedback loop, (2) Reproduce & minimize, (3) 3–5 ranked falsifiable hypotheses, (4) One-variable instrumentation (`[DEBUG-xxxx]`), (5) Regression test + fix (with forced-mutation `diff` proof), (6) Cleanup (redacts secrets throughout). |
| **`research`** | Model | Spins up a background fresh-context agent to investigate against **primary sources** (official docs, source code, specs, first-party APIs) and save a single cited Markdown file matching repo conventions. |
| **`tdd`** | Model | Vertical-slice red → green loop at pre-agreed public seams (with one-line notes on what each seam catches/misses). Prohibits horizontal test slicing, tautological tests, and implementation-coupled mocks. |
| **`domain-modeling`** | Model | Active discipline for building `GLOSSARY.md` (zero implementation details) and `docs/adr/`: challenges glossary conflicts, sharpens overloaded words, tests edge-case scenarios, cross-references code, and adds ADRs only when hard-to-reverse + surprising + real trade-off. |
| **`codebase-design`** | Model | Shared architecture vocabulary (**Module, Interface, Implementation, Depth, Seam, Adapter, Leverage, Locality**) + Ousterhout/Feathers principles (`DEEPENING.md`, `DESIGN-IT-TWICE.md`). |
| **`code-review`** | Model | Two-axis parallel review (**Standards** including a 12-item Martin Fowler smell baseline vs. **Spec** faithfulness) run in separate foreground fresh-context subagents so neither axis pollutes the other. |
| **`pr`** | Model | Structures PR bodies into 3 tight sections: **Summary** (smallest visual: pseudocode, call/file/component tree, Mermaid, or diff — credited to Dex Horthy's `show-me`), **Evidence** (before/after screenshots or test outputs), and **Merge Danger** (one-way vs. two-way door + blast radius). |
| **`wizard`** | Model | Generates an interactive bash script (`template.sh`) that guides humans through strictly manual steps (opening URLs, hidden `.env` secret capture, `gh secret` writes, confirmation gates). |

#### B. Productivity Bucket (7 Promoted Skills — General / Non-Code Workflows)
| Skill | Invocation | What It Actually Does (`SKILL.md`) |
| :--- | :--- | :--- |
| **`/grill-me`** | User | Calls `grilling`: stateless relentless interview for plans, designs, or writing when not inside a project repo. |
| **`/handoff`** | User | Writes a compact, redacted portable handoff Markdown file in `%TEMP%`/`$TMPDIR` (referencing artifacts by path/URL, plus suggested skills) to move harnesses, directories, or colleagues. |
| **`/teach`** | User | Stateful multi-session tutor using the current folder (`MISSION.md`, `RESOURCES.md`, `./learning-records/`, `./lessons/*.html`, `./reference/*.html`, `./assets/`) grounded in fluency vs. storage strength and Zone of Proximal Development. |
| **`/to-questionnaire`** | User | Inverse of `/grill-me`: when knowledge sits in someone else's head, interviews you only about the **send** (who it's for + what you need back) and generates `to-questionnaire-<slug>.md` targeting the gap for async or meeting completion. |
| **`/wait-what`** | User | 3-line jargon stopper: fire when an agent's message doesn't land; re-pitches the message with missing context in `ASD-STE100` Simplified Technical English using your `GLOSSARY.md`. |
| **`grilling`** | Model | Core interview primitive: maps decisions as a tree, queries the **frontier** in numbered rounds with `❓`/`➡️` recommended answers worded so `"yes"` accepts, and dispatches fresh-context subagents for facts so the user only answers decisions. |
| **`writing-for-agents`** | Model | Authoring discipline for `AGENTS.md`, `CLAUDE.md`, and skills: context pointers, context vs. cognitive load, information hierarchy & progressive disclosure, completion criteria, leading words vs. negative-prompting traps, and no-op pruning. |

#### C. In-Progress Bucket (8 Beta Skills on `main` + 2 in Open PR #1422)
- **`/chief-of-staff`** *(in `skills/in-progress/`, omitted from `in-progress/README.md`)*: Long-running goal orchestrator using fresh background subagents, sparse context pointers, dated commit-cited LLM wiki (`index.md` + topic pages), and strategic environment upgrades.
- **`/software-factory`**: Canonical language & 6-slot architecture survey for automated agent pipelines + 3 brakes against "slop cannons".
- **`/loop-me`**: Stateful `/grilling` session that maps recurring life/work **loops** into deterministic `workflows/*.md` specs (`Trigger`, `Checkpoint`, `Push right` to defer human involvement, `Brief` for fast checkpoint review).
- **`/writing-fragments`**, **`/writing-shape`**, **`/writing-beats`**: Three-part writing system separating **Explore** (`writing-fragments` — interview-driven heterogeneous raw nuggets + leading words) from **Exploit** (`writing-shape` paragraph-by-paragraph argument/format shaping, or `writing-beats` choose-your-own-adventure beats grounding concepts sequentially).
- **`/claude-handoff`**: Writes a handoff summary and spawns `claude --bg --name "..."` immediately in the background.
- **`/setup-ts-deep-modules`**: Wires `dependency-cruiser` into TypeScript packages to enforce root entry-point boundaries and hidden `lib/` internals.
- *Pending PR #1422:* **`animatic`** (model-invoked) & **`/setup-animatic`** (user-invoked) — turns topics or PRs into narrated still-frame videos.

#### D. Misc Bucket (4 Frozen / Unmaintained Skills)
`git-guardrails-claude-code` (hook blocking dangerous git commands), `migrate-to-shoehorn`, `scaffold-exercises`, `setup-pre-commit`. (Deprecated bucket is currently empty.)

---

## 3. PO / Non-Coder Translation: What to Adopt vs. Skip

### 3.1 Strict Separation: Developer-Only vs. High-Value PO / BA Skills

| Tier | Skills | Verdict for a Product Owner / Non-Coder |
| :--- | :--- | :--- |
| **Tier 1: Daily PO / BA Power Tools (Zero Coding Required)** | **`/grill-me`**, **`/grill-with-docs`**, **`/to-questionnaire`**, **`/to-spec`**, **`/to-tickets`**, **`/wait-what`**, **`/domain-modeling`**, **`/wayfinder`**, **`/research`**, **`/teach`**, **`/handoff`**, **`loop-me`**, **`writing-*`**, **`chief-of-staff`** | **Adopt immediately.** Directly solve PO pain points: ambiguous stakeholder requests, cross-team jargon mismatch, oversized epics, async stakeholder discovery, and recurring operational workflows. |
| **Tier 2: Hybrid / PO + Tech Lead Collaboration** | **`/setup-matt-pocock-skills`**, **`/ask-matt`**, **`prototype`** (Logic HTML & UI variants), **`/triage`**, **`software-factory`** | **Use selectively / with Engineering.** Configure `/setup-matt-pocock-skills` with **Local Markdown (`.scratch/`)** or **"Other" (Jira/Linear/Obsidian)** so you never touch GitHub CLI. Use `prototype` to ask engineers/agents for clickable HTML state demos before coding starts. |
| **Tier 3: Developer-Only (Skip as a PO)** | **`/implement`**, **`/implement-spec`**, **`/tdd`**, **`/diagnosing-bugs`**, **`/code-review`**, **`/pr`**, **`/improve-codebase-architecture`**, **`/codebase-design`**, **`/retro`** (code/linter focus), **`/wizard`**, `setup-ts-deep-modules`, `claude-handoff`, all 4 `misc/` skills | **Leave to engineers.** These enforce TypeScript/code seams, test suites, git worktrees, bash setup scripts, and PR diffs. *(Exception: borrow `/retro`'s habit of refining your own `AGENTS.md` / prompts when an AI misbehaves.)* |

---

### 3.2 Practical PO Playbooks Using Matt's Skills

1. **Interrogating Messy Requirements (`/grill-me` vs. `/grill-with-docs`):**
   - When a stakeholder drops a vague request (*"We need parent messaging announcements by grade"*), start `/grill-with-docs` inside your PO vault (or `/grill-me` in a quick ad-hoc chat).
   - Because `grilling` asks only the unblocked **frontier** in rounds and phrases every question so **"yes" accepts the recommended answer**, you rapidly surface permissions, edge cases, moderation rules, and out-of-scope boundaries without staring at a blank PRD.
   - Meanwhile, `domain-modeling` quietly builds your **`GLOSSARY.md`** (e.g., locking exact definitions of *Guardian* vs. *Parent*, *Broadcast* vs. *Thread*, *Campus* vs. *School*)—preventing developers from naming database tables and UI labels differently from product language.
2. **Extracting Answers from Stakeholders or Clients (`/to-questionnaire`):**
   - Stop asking AI to guess answers only a principal, compliance officer, or backend lead knows. Run `/to-questionnaire`: the AI interviews *you* in 2 quick steps (who is receiving it + what decisions you need back) and outputs a crisp, async-friendly discovery Markdown file with `"Why this matters"` cues.
3. **Writing Decision-Ready Specs & PRDs (`/to-spec`):**
   - Run `/to-spec` immediately after grilling (in the same session before `/compact` or `/clear`) so it synthesizes *everything agreed* without re-asking you.
   - **PO Adaptation Tip:** `/to-spec` includes `Implementation Decisions` and `Testing Decisions` sections plus a seam check. As a non-coder PO, instruct the agent during setup or in your `AGENTS.md`: *"When running `/to-spec` for product specs, keep Problem Statement, Solution, extensive User Stories, Acceptance Criteria, and Out of Scope complete, and leave technical implementation/testing seams as placeholders (`TBD with Engineering`)."*
4. **Splitting Epics into Vertical Tracer-Bullet Backlog Items (`/to-tickets`):**
   - Most teams fail by writing horizontal tickets (*"Ticket 1: DB schema, Ticket 2: API, Ticket 3: UI"*), which deliver zero testable product value until the sprint ends. `/to-tickets` enforces **tracer bullets**—thin end-to-end slices that actually work and can be demoed—plus explicit `Blocked by` ordering and a granularity check before writing individual Markdown ticket files or Linear/Jira items.
5. **Breaking Down Massive Multi-Week Initiatives (`/wayfinder` + `chief-of-staff`):**
   - For huge cross-team projects (e.g., launching a new billing module or district-wide onboarding), use `/wayfinder` to separate **decisions to settle** from **known fog (`Not yet specified`)** and **consciously excluded scope (`Out of scope`)**—never accidentally turning unresolved product questions into premature dev tickets. For ongoing PO operations (weekly stakeholder updates, continuous backlog grooming, product memory across months), watch `chief-of-staff`'s **dated LLM wiki** (`index.md` + topic pages).
6. **Stopping Technical Jargon Mid-Chat (`/wait-what`) & Reviewing Logic Before Engineering (`/prototype`):**
   - Whenever an engineer's note or AI explanation feels dense, invoke `/wait-what` to force a plain-English re-explanation grounded in your `GLOSSARY.md`.
   - Before engineering builds complex workflows (approval states, attendance rules, notification cascades), ask your agent or engineer to produce a **`prototype` (Logic branch)**—it outputs **one standalone HTML file** you double-click in your browser with interactive buttons and guided walkthrough scenarios written in plain product language.
7. **Automating PO Routines (`loop-me`) & Memo Drafting (`writing-fragments` / `writing-shape`):**
   - Use `loop-me` (`in-progress`) to turn recurring PO chores (daily triage, sprint review prep, release-note assembly) into clear workflow specs built around **pushing checkpoints right** and presenting 30-second **Briefs**. Use `writing-fragments` + `writing-shape` to turn scattered voice-note insights into crisp stakeholder memos or product strategy posts.

---

### 3.3 Applying the "Home Repo" Pattern to Knowledge Work & an Obsidian PO Vault

Matt's **Home Repo Pattern** (Nov 12, 2026) solves the exact problem non-coders and POs face when juggling separate folders, tools, and chats: **context fragmentation and instruction drift**. Translated to a PO Knowledge-Work Hub (such as an Obsidian vault like `Schoolvoice-PO`):

| Engineering Home Repo Concept | Knowledge-Work / PO Equivalent | Why It Matters for a PO |
| :--- | :--- | :--- |
| **Home Repo root** | Your central PO Obsidian Vault / Git repo | Start **every** AI session here so every chat inherits your product brain. |
| **`AGENTS.md` / `CLAUDE.md`** | Central AI operating manual + **context pointers** | Holds your PO persona, PRD overrides for `/to-spec`, and 1-line pointers to Stakeholders, Personas, Competitors, Meeting Notes, and (optionally read-only) Engineering repos. |
| **Shared `GLOSSARY.md`** | Canonical Product & Domain Dictionary | Single source of truth for domain terms—used by `/grill-with-docs`, `/to-spec`, `/to-tickets`, and `/wait-what`. |
| **Shared `skills/` folder** | Installed PO-relevant skills (`grill-me`, `to-questionnaire`, `to-spec`, `to-tickets`, `wait-what`, `research`) | Edit a skill or prompt once; zero divergence across initiatives or projects. |
| **Progressive Disclosure (>20 pointers)** | Index files per product area (`areas/messaging.md`, `areas/attendance.md`) | Keeps your root `AGENTS.md` lean inside the ~150k-token **smart zone** instead of dumping 100 notes into every session. |
| **Dated LLM Wiki (`chief-of-staff`)** | `Decisions/` or `Wiki/index.md` + dated ADR notes | Prevents AI from hallucinating old product decisions as current truth (*"On 2026-10-12 we agreed X; superseded 2026-11-10 by Y"*). |

---

## 4. Verified Official Channels & URLs for Daily Tracking

### 4.1 Machine-Readable Feeds & Endpoints (Ideal for Automated Daily Digests)

| Source | Verified URL | Format | What It Tracks |
| :--- | :--- | :--- | :--- |
| **AI Hero Full RSS** | `https://www.aihero.dev/rss.xml` | RSS 2.0 XML | All new/updated articles, guides, dictionary updates, workshops, and changelogs on `aihero.dev`. |
| **AI Hero Skills RSS** | `https://www.aihero.dev/skills/rss.xml` | RSS 2.0 XML | Dedicated feed for Skills releases, changelogs, and skill guides. |
| **AI Hero `llms.txt` & `sitemap.md`** | `https://www.aihero.dev/llms.txt` · `https://www.aihero.dev/sitemap.md` | Plain Text / Markdown | Official machine discovery index (plus `.md` twins on posts/pages, e.g. `https://www.aihero.dev/the-home-repo-pattern.md`). |
| **`mattpocock/skills` Releases Atom** | `https://github.com/mattpocock/skills/releases.atom` | Atom XML | Official tagged version releases (`v1.3.2`, etc.). |
| **`mattpocock/skills` Commits Atom** | `https://github.com/mattpocock/skills/commits/main.atom` | Atom XML | Every commit merged to `main` (catches `in-progress` and unreleased updates before release tags). |
| **`dictionary-of-ai-coding` Commits Atom** | `https://github.com/mattpocock/dictionary-of-ai-coding/commits/main.atom` | Atom XML | New terms and edits to the AI Coding Dictionary. |
| **YouTube Channel RSS (`@mattpocockuk`)** | `https://www.youtube.com/feeds/videos.xml?channel_id=UCswG6FSbgZjbWtdf_hMLaow` | Atom XML | Every new YouTube video, livestream, and Short with exact timestamps and descriptions. |

### 4.2 Official Websites, Repositories & Social Profiles

| Channel | Verified URL | Notes |
| :--- | :--- | :--- |
| **AI Hero (Main Hub)** | `https://www.aihero.dev/` | Courses, guides, cohorts, and search (`https://www.aihero.dev/posts`, `/videos`, `/open-source`). |
| **Personal Site** | `https://www.mattpocock.com/` | Canonical personal site linking directly to `aihero.dev`. |
| **AI Hero Skills Hub** | `https://www.aihero.dev/skills` (Markdown: `https://www.aihero.dev/skills.md`) | Skill catalog, featured workflows, and release changelogs. |
| **Skills Email Newsletter** | `https://www.aihero.dev/skills/subscribe` (shortlink: `https://www.aihero.dev/s/skills-newsletter`) | Free 7-lesson email course + ongoing skill updates (~60,000 subscribers cited in `README.md`). |
| **AI Coding Dictionary** | `https://www.aihero.dev/ai-coding-dictionary` · `https://www.aicodingdictionary.com/` | 72 plain-English AI engineering definitions across 7 sections. |
| **GitHub — Profile** | `https://github.com/mattpocock` | All open-source work (225 public repos). |
| **GitHub — Skills Repo** | `https://github.com/mattpocock/skills` (Installer listing: `https://www.skills.sh/mattpocock/skills`) | Core skills repo (`ENGINEERING`, `PRODUCTIVITY`, `IN-PROGRESS`, `MISC`) + Discussions/PRs. |
| **GitHub — Dictionary Repo** | `https://github.com/mattpocock/dictionary-of-ai-coding` | Markdown source for the AI Coding Dictionary. |
| **GitHub — Sandcastle Repo** | `https://github.com/mattpocock/sandcastle` | TypeScript sandboxed agent orchestrator (`sandcastle.run()`). |
| **YouTube** | `https://www.youtube.com/@mattpocockuk` | Deep-dives, livestreams, and daily Shorts (`Channel ID: UCswG6FSbgZjbWtdf_hMLaow`). |
| **X (Twitter)** | `https://x.com/mattpocockuk` (also `https://twitter.com/mattpocockuk`) | Verified handle via GitHub profile & `aihero.dev` HTML metadata. |
| **Bluesky** | `https://bsky.app/profile/mattpocock.com` | Verified handle (`@mattpocock.com`) linked from `aihero.dev` share metadata. |
| **LinkedIn** | `https://www.linkedin.com/in/mapocock/` | Profile URL observed via search results (automated scraping blocked with HTTP 999). |
| **Discord** | `https://www.aihero.dev/discord` | Community Discord link referenced across Matt's YouTube video descriptions. |

---

## 5. Methodology & Observed Gaps

- **Directly Verified:** All GitHub commits, PRs, releases, `SKILL.md` contents, `README.md`, `CHANGELOG.md`, `aihero.dev` XML/RSS/sitemap/HTML/Markdown-twin endpoints, `arxiv.org/abs/2610.34938`, and YouTube RSS entries were fetched directly and inspected during this session (`2026-11-16`).
- **Known Gaps (Unverified Social Timelines):**
  - **X (`@mattpocockuk`)** returned HTTP 200 shell HTML without server-rendered tweet timelines, and **LinkedIn (`linkedin.com/in/mapocock/`)** returned HTTP `999` anti-bot rejection. Therefore, standalone X threads or LinkedIn posts published between `2026-10-17` and `2026-11-16` that were not mirrored to GitHub, `aihero.dev`, or YouTube could not be inspected directly.
  - **Private / Unlisted Cohorts & Email Newsletters:** Email-only dispatches to `skills-newsletter` subscribers and private Cohort 005 materials inside `aihero.dev` (other than public landing pages and public GitHub commits referencing Cohort 005) are gated behind subscriber/learner auth.
