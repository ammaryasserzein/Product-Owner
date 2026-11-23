# Schoolvoice Discovery Notes (School Persona & PO Onboarding)

- **Source Master Document**: `Master Document - Persona: School` (Google Doc ID `1Pc3ZklC-CE0nURaoT34AqI0Wh_rmZxAv7rhPXetab7o`, owner `ali.binyahia@schoolvoice.com`, last modified `2026-09-12`)
- **Related External References**: Master Document Index (`1boYrzUG4ewozJA5X48lFTy28VUaGoZiTzxVVrZvwi9o`), XMind Mind Map (`https://xmind.ai/MdJa1HAY?xid=5sBt8BfT`), Delete Messages User Stories Draft (`1cRC-rV93BxC6wtY_mpF2JZgu90E1z7sfNgV0n69aeOI`)
- **Obsidian Vault Copy**: Adapted from `C:\Users\L\OneDrive\Schoolvoice-PO\Master-Document-School-Persona\`

---

## Core Architecture & Product Loops

Schoolvoice bridges the gap between uncontrolled consumer chat apps (WhatsApp number leaks, zero audit trail) and low-engagement school portals (monthly-only opens) via **3 interconnected loops**:

1. **Daily Habit Loop (Retention)**: `Stories` + `Teachers Drive` + `Schoolvoice Live` draw parents into the app daily for classroom life and study resources.
2. **Structured Decision Loop (Flagship)**: `Actionable Messages` turn notices into 1-tap CTA cards backed by `Approval Workflow`, `Message Merge`, timed `Fallback SMS` (e.g., 10 min for offline devices), non-responder-only `Smart Reminders`, `Action Deadlines`, and `Message Recall`.
3. **Two-Way & Safeguarding Loop (Control)**: `1:1 Chat`, RBAC `Department Chat Channels` (private per-parent threads), `Authorized Chat Extraction` (with audit trail), and `100% Recorded In-App VoIP Voice Calls` keep all talk inside school-owned infrastructure.

---

## Core Module Specifications (Verified from Master Document)

### Actionable Messages
- **7-Part Card Anatomy**: Sender name/photo/logo, date & urgency badge, summary, child's photo, bottom CTA button(s), urgency/reminder badges, attachments.
- **8 Action Types**:
  1. `Announcement` (`Read`)
  2. `Approval Request` (`Approve` / `Reject` + **parent PIN** confirmation)
  3. `Acknowledge Request` (`Acknowledge`)
  4. `Reply Request` (`Reply`, configurable as `1-to-many` private or `many-to-many` shared)
  5. `Payment Request` (`Pay [amount]` in-app)
  6. `Absence & Tardiness Note` (`Submit Absence/Tardiness Reason` with editable templates, predefined reasons, and Doctor's Note / Official Excuse upload)
  7. `Moment Message` (`View Moment` photo/video highlights)
  8. `Emergency Alerts` (`Call` with full-screen takeover, silent-mode bypass sound, simultaneous all-guardian ring)
- **Targeting & Scale**: Multi-criteria filtering (Grade/Section/Group), 4 selection modes (autocomplete, `Grade → Section → Student` dropdown, comma-separated IDs, CSV upload), `Staff CC` (omits CTA buttons), `#variables` + `Message Merge` (auto-attaches matching external files e.g. report cards), `Sender Name Selection` (School vs. Individual), Drafts, Scheduling, Urgent flag, Post-send action button manual toggle, `View Other Sent Messages`, `Action Status` & `Read & Delivery` charts + per-student action history (PDF/CSV export), Co-guardian `Other parent action` notifications.

### Instant Messaging (Chat) & Voice Calls (In-App VoIP)
- **Chat**: Mobile + Web, zero phone numbers exposed, built-in translation, multimedia + voice notes, contact/student context, teacher availability toggle, real-time AI moderation, management oversight.
- **Chat Channels**: Unlimited department queues (Tuition, Academic Advising, Bus, Admissions, Events, Special Needs Support, Wellbeing & Counselling, IT Support) with shared staff replies, strict per-parent thread isolation, and RBAC on sensitive channels.
- **Chat Extraction**: Regular 1:1 chats stay private from management by default; designated admins can extract specific threads on demand with a mandatory audit log.
- **Voice Calls**: 1:1 Chat only (no broadcasts); school toggle + per-staff permission; default hours Mon–Fri `12:00 PM – 5:00 PM` (parent sees local timezone + `"Message Teacher"` outside hours; staff can call out anytime); tied to chat availability; relationship-aware caller ID (`"Ahmed – Teacher of Omar"`); 100% recorded with admin review dashboard; inline call logs (`Completed`, `Missed`, `Declined`, `Busy`, `Failed`); missed-call push alerts; configurable monthly school call quota. *(Note: VoIP has a full body section but is absent from the doc's top 6-module list).*

### Stories, Teachers Drive & Schoolvoice Live
- **Stories**: Private to authorized parents; teachers post only for their own students' parents; likes + local saves; AI moderation + parent reporting + admin filter dashboard.
- **Teachers Drive**: Teacher-profile cloud folders by subject/topic/class with `Public` vs. `Private` folder visibility.
- **Video Live Broadcasting (`Schoolvoice Live`)**: Whole-school or class broadcasts with per-teacher admin permission, interactive Q&A, and automatic in-app notifications (no external meeting links).

### Reports & District Management
- **Installation Report**: Guardians/staff/students install %, Android vs. iOS split, user/device/OS/app build table (PDF/CSV).
- **Reach Report**: Student counts as **reached** if `>= 1` guardian is active; lists student, total guardians, active guardians (PDF/CSV).
- **District Management**: `District → Branches/Operators → Schools → Grades/Sections/Groups`; cross-school messaging, cross-school delete/recall oversight, filtered analytics.

---

## Active PO Field Notes & Onboarding Context
*(Carried over from `C:\Users\L\OneDrive\Schoolvoice-PO` — excluding credentials and raw PNG binaries)*

- **Stakeholder Priority Ranking**: Administration & Parents = `#1`; Teachers & Students = `#2`.
- **Active PO Tasks**:
  - Author/review User Stories for **Delete Messages** (`https://docs.google.com/document/d/1cRC-rV93BxC6wtY_mpF2JZgu90E1z7sfNgV0n69aeOI/edit?tab=t.0`) — directly resolves empty Master Doc heading #16.
  - Test `Message Merge` behavior in the app.
- **Observed UI Polish Notes (`Notes-To-improve-the-product`)**:
  - Save button icon looks like a camera (`save button logo is Camera!.png` in Obsidian vault).
  - Logo placement note (`SV logo on the box.png` in Obsidian vault).
- **Sales / Messaging Note (`Daily-Check-out`)**: Video 3 Value Propositions note — *"Naming the professor and the number of students would be more effective"*.

---

## Unresolved Spec Gaps & TBAs (For Stakeholder Discovery)

1. **9 Admin Modules Marked `TBA`**:
   - Contact management, Permission management, Challenges management, Absence management, School structure management, School profile management, Modules management, SMS settings, Admin logs.
2. **Overview vs. Body Discrepancies**:
   - `Rewards and Challenges` is listed #4 at the top of the Master Document but has no body section (only `Challenges management: TBA`).
   - `Voice Calls` has a full specification in the body but is missing from the top 6-module list.
3. **Empty Feature Placeholders**:
   - `Message delete` (Cross Actionable Features #16 — no text).
   - `Parent feedback attachment:` (Actionable Messages Reports — no description).
   - `Views:` (Stories interactive features — no description).
