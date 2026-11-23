# Message Translation — Presenter Notes

> **Companion Cheat-Sheet** for live walkthrough of the 5-story Message Translation specification (Section 3).
> Source stories remain verbatim and separate. Terminology aligns strictly with `Schoolvoice/GLOSSARY.md`.

## At-a-Glance Feature Summary

| Dimension | Approved Spec Baseline |
| :--- | :--- |
| **Platform** | Mobile App (iOS & Android) |
| **`Message Translation Scope`** | Body text only of `Actionable Messages` — **excludes** `Emergency Alert`, `Chat`, and `Stories` |
| **Supported `Translation Language` Options (5)** | `Arabic` (`العربية`), `English` (`English`), `French` (`Français`), `Hindi` (`हिन्दी`), `Urdu` (`اردو`) — any source language translates into any of the 5 |
| **AI Engine** | Pinned `openai/gpt-4o-mini-2024-07-18` · `temperature: 0` · [System Prompt](https://drive.google.com/file/d/1u3znYVyDVkYuBoOHW-jBAj2n3c-loc0-/view) |
| **`Daily Translation Quota`** | `10` AI translations / user / day · server-enforced · resets midnight UAE (`GMT+4`) · `Device Translation Cache` hits exempt |
| **Design Reference** | [SV- Wireframes Overview](https://www.figma.com/design/u80rNkcoLIUYWp8dPpxbal/SV--Wireframes?node-id=427-3015) |

---

## 1. `[tech validate]` Engineering Decision Table

Use this table to drive live technical alignment across all four `[tech validate]` callouts in Stories 1–5.

| # | Story Ref | `[tech validate]` Topic | Question for Engineering | Recommended Decision Prompt | Resolved |
| :-: | :--- | :--- | :--- | :--- | :-: |
| **1** | **Story 1**<br>*(System Prompt)* | **System prompt caching** | Does the system prompt meet OpenAI's prompt-caching threshold, and is the `system` role kept strictly static (with `Target Language` isolated in the `user` turn) so repeated calls hit cached tokens? | Confirm prompt caching is active and measurable via API usage (`cached_tokens`); keep `Target Language` strictly in the `user` turn so the `system` prefix never varies. | `[ ]` |
| **2** | **Story 1**<br>*(Response Quality & Safety Checks)* | **Failed validation quota protection** | When a model completion fails server-side validation (**Non-Empty**, **Refusal**, or **URL Integrity**), is `Daily Translation Quota` debited only *after* validation passes (or rolled back atomically)? | Debit `Daily Translation Quota` strictly post-validation (or refund atomically on failure) so a rejected output showing `"An error has occurred. Please try again."` never consumes quota. | `[ ]` |
| **3** | **Story 2**<br>*(Translating — `⋮` & Long-Press)* | **Same-language client bypass** | Since `"Translate to [Language]"` stays always visible/interactive, can the client reliably detect a body already in the user's `Translation Language` to skip the AI call and save tokens—without mishandling mixed-language school notices? | Bypass client-side only with high-confidence detection (or authoritative source-language metadata) and never skip mixed-language bodies; otherwise let the server/model handle it (Story 1 returns same-language text unchanged). Confirm a client bypass consumes zero `Daily Translation Quota`. | `[ ]` |
| **4** | **Story 4**<br>*(Quota Consumption Rules)* | **Failed API / network request quota debit** | Do failed API calls caused by network drops, timeouts, or server/model errors count against the user's `Daily Translation Quota`? | **No — do not count failed requests.** Align with Story 1: debit `Daily Translation Quota` only upon delivering a validated translation (or atomically release on failure). | `[ ]` |

---

## 2. Story-by-Story Presenter Cues (Stories 1–5)

### Story 1: Translation Engine *(Backend — no wireframe)*

* **Pinned & Deterministic**: `openai/gpt-4o-mini-2024-07-18` at `temperature: 0` so repeated taps never produce drifting wording.
* **Prompt Structure & Injection Safety**:
  * Static prompt in `system` role; `user` turn strictly formatted as `Target Language: <full English name>` + `<message_to_translate> [Body] </message_to_translate>`.
  * Text inside `<message_to_translate>` is treated strictly as data—embedded instructions are translated, never obeyed.
* **Output Quality Guarantees**:
  * Raw translated body only (no preamble, labels, or quotes).
  * Preserves line breaks, paragraph structure, emoji, and exact URLs/emails character-for-character.
  * Personal names transliterated phonetically into the target script (never translated).
  * Arabic output uses **Modern Standard Arabic** (never regional dialect); **Western numerals (`0-9`)** used across all 5 languages.
  * Sensitive school topics (illness, behaviour, safeguarding, fees) translated faithfully, never refused; same-language body returned unchanged.
* **Server-Side `[VALIDATE]` Gate (3 Checks)**:
  1. **Non-Empty**: Not null or whitespace-only.
  2. **Refusal**: Rejects model refusal phrases (e.g., `"I'm sorry, but I cannot..."`, `"As an AI language model..."`).
  3. **URL Integrity**: Every input URL appears identically in the output.
  * Any failure → request marked failed → client shows `"An error has occurred. Please try again."` → **must not debit `Daily Translation Quota`** *(Decision #2)*.

### Story 2: Translate a Message *([Wireframes](https://www.figma.com/design/u80rNkcoLIUYWp8dPpxbal/SV--Wireframes?node-id=1991-30823))*

* **`Message Translation Scope` (Key Boundary)**:
  * Applies only to `Actionable Messages` — **excludes** `Emergency Alert`, `Chat`, and `Stories`.
  * **Body-only translation**: Feed translates the shown message body; Message Details translates the full message body. *(Confirm with Engineering how Feed preview syncs cleanly into Message Details via `Device Translation Cache`.)*
  * Empty body (e.g., photo-only Moments) → no-op; card stays in its original state.
* **Entry Points**:
  * **`⋮` More Options Menu** (3 identical surfaces): Recipient Feed (card top-right), Recipient Message Details (card top-right), and Sender/Staff Message Details (`Sent Messages` → Card → `⋮`).
  * **Long-Press Bottom Sheet** (**Feed only**): Exact same items and order as `⋮`; tap outside or drag down dismisses.
* **Menu Row Label**:
  * Shows `"Translate to [Language]"` + edit pencil icon; always visible/interactive even if body matches `Translation Language` *(Decision #3)*.
  * Target language name in this menu row is **localized to `App UI Language`** (EN UI → `"Translate to Urdu"`; AR UI → `"الترجمة إلى أردو"`).
* **Loading & Error Handling**:
  * Tap closes menu immediately; card dims with a centered spinner (Feed disables CTA button and `⋮`).
  * On error: spinner dismisses, card restores original text and `"Translate to [Language]"`.
  * Toasts: Offline → `"No internet connection. Please check your connection and try again."` | Server/timeout → `"An error has occurred. Please try again."`.
* **`Device Translation Cache`**:
  * Persistent local store keyed by `message_id` + `target_language`.
  * Syncs **Feed ↔ Message Details**, survives **app kill/restart**, and serves instant re-translations after `Show Original` with zero network calls and zero `Daily Translation Quota` usage.
* **RTL/LTR & Secondary Actions**:
  * **Menu chrome** mirrors with `App UI Language` (Arabic RTL: icon on right, label to its left, edit pencil at far left).
  * **Body text direction** strictly follows the **translated language**, independent of `App UI Language` (`Arabic`/`Urdu` → RTL; `English`/`French`/`Hindi` → LTR); spinner always stays centered.
  * **`Read` (TTS) & `Copy`**: Act on whichever text is currently visible on screen (original vs. translated).

### Story 3: Revert to Original Message *([Wireframes](https://www.figma.com/design/u80rNkcoLIUYWp8dPpxbal/SV--Wireframes?node-id=2002-51819))*

* **Menu State Swap**: On a translated card, the first row in both `⋮` and Feed long-press changes to **`Show Original`** with the **edit pencil icon hidden**; `"Copy"` and `"Read"` stay unchanged.
* **Pure Client-Side Toggle**: Tapping `Show Original` closes the menu and restores original source text immediately — **zero spinner, zero network calls, zero AI tokens, zero quota cost**. Menu row reverts to `"Translate to [Language]"` with edit pencil restored.
* **Persistence & Blast Radius**:
  * Translation stays stored in `Device Translation Cache` (re-translating to the same language is instant and free).
  * Reversion affects **only that single message card**.

### Story 4: Daily Translation Quota *(Server-enforced limit)*

* **Quota Policy**: `10` messages/user/day, tracked **entirely server-side**, resetting at **midnight UAE time (`GMT+4`)**. Server validates quota before calling the AI engine.
* **Limit Reached UX**:
  * Zero AI call, no card dimming, no loading spinner; body stays in original text; row stays `"Translate to [Language]"`.
  * Toast: `"You have reached your translation quota for today."`
* **Exemptions & Open Check**:
  * `Show Original` (Story 3) → **exempt**.
  * `Device Translation Cache` hits (re-translating a previously cached message) → **exempt**.
  * Failed API/network requests → confirm zero debit with Engineering *(Decision #4)*.

### Story 5: Change Translation Language *([Wireframes](https://www.figma.com/design/u80rNkcoLIUYWp8dPpxbal/SV--Wireframes?node-id=1869-22368))*

* **Entry Point**: Tapping the **edit pencil icon** on `"Translate to [Language]"` (from any `⋮` menu or Feed long-press sheet) opens `"Select your translation language"`. *(Note: pencil is hidden while a card shows `Show Original`.)*
* **Modal & Fixed 5-Language Dropdown**:
  * Collapsed: modal title, top-right `"X"`, dropdown showing country flag + **native-script** name + right chevron, `"Cancel"` and `"Done"`.
  * Expanded (fixed order, active language highlighted with checkmark, row alignment follows `App UI Language` RTL/LTR):
    1. `العربية` (Saudi Arabia flag)
    2. `English` (United Kingdom flag)
    3. `Français` (France flag)
    4. `हिन्दी` (India flag)
    5. `اردو` (Pakistan flag)
  * **Key Label Contrast**: Dropdown names stay **static in their own native script** (never change with `App UI Language`), unlike Story 2's menu row which localizes to `App UI Language`.
* **Save, Cancel & Failure Behavior**:
  * **`Done`**: Saves `Translation Language` to user profile, closes modal, **keeps the `⋮` menu open** and updates the row immediately to `"Translate to [New Language]"`. Does **not** auto-translate the current message and leaves already-translated cards in the current session unchanged; applies to future translations.
  * **`Cancel` / `"X"` / tap outside**: Closes immediately and discards unsaved selection.
  * **Save error**: Closes modal, reverts to previously saved `Translation Language`, and displays the offline or generic error toast.

---

## 3. Quick-Glance Behavior & Directionality Matrix

### A. Directionality & Language Label Rules

| UI Element | Controlled By | Rule |
| :--- | :--- | :--- |
| **`⋮` menu & bottom sheet layout** | `App UI Language` | Mirrors in Arabic RTL (icon right → label → edit pencil far left) |
| **`"Translate to [Language]"` label** | `App UI Language` | Target language localized to UI (`"Translate to Urdu"` vs `"الترجمة إلى أردو"`) |
| **Language picker dropdown labels** | Fixed native script | Always static (`العربية`, `English`, `Français`, `हिन्दी`, `اردو`) regardless of `App UI Language` |
| **Language picker row alignment** | `App UI Language` | Follows app RTL / LTR layout |
| **Translated message body alignment** | `Translation Language` | `Arabic` & `Urdu` → RTL; `English`, `French`, `Hindi` → LTR (independent of `App UI Language`) |
| **Loading spinner** | Fixed | Always centered on card |

### B. Action Impact Matrix

| User Action | Network / AI Call | `Daily Translation Quota` | `Device Translation Cache` |
| :--- | :---: | :---: | :--- |
| **Translate (not cached)** | Yes | `-1` *(on success)* | Writes `(message_id, target_language)` |
| **Translate (already cached)** | No | `0` *(exempt)* | Reads locally (instant) |
| **`Show Original`** | No | `0` *(exempt)* | Preserved (not evicted) |
| **Quota exhausted** | Quota check only (no AI) | `0` | Unchanged |
| **Validation / network / server error** | Failed | `0` *(confirm Decisions #2 & #4)* | Not written |
| **Change `Translation Language` (`Done`)** | Save profile only (no AI) | `0` | Existing translations stay untouched |

---

## 4. Live Meeting Sign-Off Checklist

- [ ] **Decision #1 (Story 1)**: Confirmed system prompt caching strategy and `cached_tokens` observability.
- [ ] **Decision #2 (Story 1)**: Confirmed failed safety/URL/non-empty validation does **not** debit `Daily Translation Quota`.
- [ ] **Decision #3 (Story 2)**: Decided client-side same-language bypass approach (including mixed-language edge cases & quota behavior).
- [ ] **Decision #4 (Story 4)**: Confirmed failed API/network/timeout requests do **not** debit `Daily Translation Quota`.
- [ ] **Boundary Alignment**: Confirmed `Message Translation Scope` (`Actionable Messages` body-only; excludes `Emergency Alert`, `Chat`, `Stories`) and Feed-to-Details cache sync.
