# Schoolvoice Operational & Domain Context

All-in-one, privacy-first school–parent communication and engagement platform uniting daily engagement (`Stories`, `Teachers Drive`, `Schoolvoice Live`), one-tap `Actionable Messages`, and governed two-way communication (`Chat`, `Chat Channels`, `In-App VoIP`), backed by analytics and multi-school `District` oversight.

See [discovery-notes.md](./discovery-notes.md) for full capability notes and [reference/Master-Document-School-Persona/\_Master Document Hub.md](./reference/Master-Document-School-Persona/_Master%20Document%20Hub.md) for the complete Master Document breakdown.

## Stakeholder Priority

1. **Primary (#1)**: School Administration / Management and Parents / Guardians
2. **Secondary (#2)**: Teachers / Staff and Students
3. **Enterprise Scale**: District / Ministry / School Group Operators

## Language

**Actionable Message**:
Feed-style structured broadcast card displaying preset one-tap CTA buttons (`Read`, `Approve`/`Reject`, `Acknowledge`, `Reply`, `Pay`, `Submit Absence/Tardiness Reason`, `View Moment`, `Call`) rather than passive text.
_Avoid_: Notification blast, SMS blast, Newsletter

**PIN Approval**:
Security requirement where tapping `Approve` or `Reject` on an Approval Request card prompts the parent to enter their personal PIN code to confirm consent.
_Avoid_: Password confirmation, Email sign-off

**Reply Request (`1-to-many` vs. `many-to-many`)**:
Actionable Message CTA where `1-to-many` collects private individual parent responses while `many-to-many` opens a shared group discussion thread.
_Avoid_: Chat Channel, Direct Message

**Personalization Variables**:
Dynamic inline text tokens (`#parent_name`, `#student_name`, `#student_grade`, `#student_section`, `#student_grade_section`, `#sending date`) resolved per recipient at send time.
_Avoid_: Message Merge (which maps external files, not just text fields)

**Message Merge**:
Automated integration linking personalization variables to an external folder (e.g., Google Drive folder indexed by student ID) to auto-match and attach individualized documents such as report cards or certificates.
_Avoid_: Mail merge text only, Manual bulk upload

**Fallback SMS**:
Automated delivery safety net that checks app receipt after a configured interval (e.g., `10 minutes`) and sends an SMS strictly to guardians who did not receive the in-app message.
_Avoid_: Smart Reminder, Broadcast SMS

**Smart Reminder**:
Targeted follow-up push notification triggered for guardians who received a message but have not yet performed its CTA, bumping the card to the top of their feed and adding a reminder badge while skipping parents who already acted.
_Avoid_: Fallback SMS, Scheduled resend-to-all

**Approval Workflow (Pre-Send)**:
Routing gate splitting staff into `Direct Senders` (bypass review) and `Senders Requiring Approval` (queued in a `Pending Approval` inbox for `Approval Managers` to approve or reject with feedback).
_Avoid_: Post-send audit, District recall

**Message Recall**:
Post-send action that disables an erroneous message on parent devices, stamps it `"Recalled Message"`, and preserves the record for audit history.
_Avoid_: Message Delete (currently unspecified heading #16), Hard delete

**Message Delete**:
Unspecified capability listed as empty heading #16 in the School Persona Master Document and active PO user-story backlog item; do not assume hard vs. soft deletion semantics until clarified with stakeholders.
_Avoid_: Conflating with Message Recall

**Other Parent Action Alert**:
Automatic push notification alerting a co-guardian when the other parent completes an action on `Approval`, `Acknowledgment`, `Payment`, or `Attendance`.
_Avoid_: Reminder alert

**Chat Channel**:
Unlimited topic- or department-based inbound communication queue (e.g., `Tuition`, `Academic Advising`, `Bus`, `Special Needs Support`, `Wellbeing`) staffed by multiple team members under RBAC, where each parent sees only their own private thread.
_Avoid_: Group chat, Public forum

**Authorized Chat Extraction**:
On-demand governance action allowing specifically authorized administrators to export an otherwise private parent–teacher chat history, automatically generating an audit trail entry.
_Avoid_: Live spy mode, Open admin inbox

**In-App VoIP Availability Window**:
Configurable daily calling schedule per staff member (default `Monday–Friday, 12:00 PM – 5:00 PM`, displayed in the parent's local timezone); blocks parent-initiated calls outside hours while allowing staff outgoing calls, coupled with chat availability status and monthly school call quotas.
_Avoid_: Direct phone call, Personal SIM call

**Teachers Drive**:
Cloud file repository embedded on a teacher's Schoolvoice profile with `Public` (all parents/students) and `Private` (selected individuals/groups) folders organized by subject, topic, or class.
_Avoid_: Google Drive external share link

**Schoolvoice Live**:
Built-in live video broadcasting tool restricted by per-teacher admin permission that alerts targeted parents via in-app notification for live Q&A and school events.
_Avoid_: External Zoom/Meet link

**Reached Student (`Reach Report`)**:
Operational reachability definition where a student counts as reached if and only if at least one linked guardian has the app installed, connected, and able to receive messages.
_Avoid_: Installed User (`Installation Report`, which tracks individual account/device installs across Android and iOS)

**District Hierarchy**:
Four-tier multi-school organizational tree (`District → Branches/Operators → Schools → Grades/Sections/Groups`) enabling cross-school targeting, recall/delete enforcement, and filtered analytics.
_Avoid_: Single-school workspace

### Message Translation

**Message Translation Scope**:
The set of message types and content fields eligible for AI translation: strictly the body text of `Actionable Messages`, excluding `Emergency Alert`, `Chat`, and `Stories`.
_Avoid_: All messages, full-card translation

**Translation Language**:
User-level target language preference (`Arabic`, `English`, `French`, `Hindi`, `Urdu`) controlling message translation output independently of `App UI Language`.
_Avoid_: App Language, Device Language

**App UI Language**:
The interface language selected for Schoolvoice app menus, labels, and layout direction (`LTR` or `RTL`), independent of `Translation Language`.
_Avoid_: Translation Language, Device Language

**Daily Translation Quota**:
Server-enforced allowance of `10` AI translations per user per day resetting at midnight UAE time (`GMT+4`), exempting locally cached re-translations.
_Avoid_: Unlimited translation

**Device Translation Cache**:
On-device persistent store of translated message bodies keyed by message and target language, surviving app restarts and keeping the Feed and Message Details synchronized.
_Avoid_: Session-only cache

**Show Original**:
Client-side toggle reverting a translated message body to its original source text with zero network requests and zero quota consumption.
_Avoid_: Untranslate
