# Delete Message (1:1 Chat) — User Stories

*Source Draft: [Delete Message - User Stories By Youssif.md](../../reference/Delete%20Message%20-%20User%20Stories%20By%20Youssif.md)*  
*Upstream Reference: [03 - Chat & Voice Calls.md](../../reference/Master-Document-School-Persona/03%20-%20Chat%20%26%20Voice%20Calls.md) (formal PRD pending in `docs/01-prd/`)*  
*Domain Terms: [CONTEXT.md](../../CONTEXT.md)*

---

## 0. Scope & Shared Rules (Mobile and Web)

To keep Mobile (Story 1) and Web (Story 2) consistent, all rules that apply to both platforms live here.

### 0.1 What Is Included & Excluded
- **Included**:
  - `"Delete for everyone"` for sent messages in **1:1 Chat** (Mobile and Web).
  - `"Copy"` for text messages in **1:1 Chat** and **Chat Channels** (Mobile and Web).
  - First-time tip on Mobile.
  - Viewing deleted messages in Admin **Chat Review** and **Authorized Chat Extraction**.
- **Excluded**:
  - `Actionable Messages` (handled separately by `Message Recall` / `Message Delete` in [CONTEXT.md](../../CONTEXT.md)).
  - Deleting messages inside `Chat Channels`.
  - `"Delete for me"` (local-only delete).
  - Deleting `Call Logs`.
  - **Not removed after delete (accepted for launch — Mobile & Web)**: Push or browser notifications already sent to a device keep their old preview text; images, videos, or files already saved/downloaded stay on the user's device.

### 0.2 Shared Rules
1. **Sender only & no time limit**: Only the person who sent a message can delete it, at any time after sending.
2. **Ask before deleting**: Picking `"Delete for everyone"` opens a confirmation pop-up before the message is deleted *(needs Figma design — see §4)*.
3. **Works when Chat Availability is off**: A user can delete their sent messages even when their `Chat Availability` status is off, as long as they have an internet connection.
4. **Keep deleted messages for Admin Review**: Deleting a message hides it from the sender and the recipient only. The original text, media files, and delete time must still be kept for authorized Admins in `Chat Review` and `Authorized Chat Extraction` *(how the data is saved is up to the developers)*.
5. **Sync across all devices**: When a message is deleted, all open sessions for both the recipient and the sender (Mobile and Web) update right away without refreshing. If a device is offline, it shows the deleted state the next time the user opens the chat.
6. **Chat list order & unread count**:
   - Deleting a message does **not** move the chat to the top of the chat list; it keeps the original message time.
   - If the deleted message was the only message in the chat, the chat stays in the list.
   - If an unread message is deleted before the recipient opens the chat, the unread count stays **unread**.
7. **No actions on deleted messages**: A deleted message keeps its original sent time, has no delivery or read ticks, has no menu, and has no `Translate` option (any active translation is cleared).
8. **Stop open or playing media**: If a voice note is playing or an image/video is open when deleted, playback stops and the media closes right away for both the sender and the recipient.
9. **Deleting the same message from two devices**: If a user opens the menu on one device, deletes the message on another device, and then confirms delete on the first device, the app simply shows the deleted message with no error and no duplicate tracking event.

### 0.3 Available Actions by Message Type (Mobile & Web)

| Message | Available Actions |
| :--- | :--- |
| Text message I sent in 1:1 Chat (sent successfully) | `Copy`, `Delete for everyone` |
| Image, video, file, or voice note I sent in 1:1 Chat (sent successfully) | `Delete for everyone` |
| Text message I received in 1:1 Chat | `Copy` |
| Image, video, file, or voice note I received in 1:1 Chat | No menu |
| Text message inside a `Chat Channel` (sent or received) | `Copy` |
| Image, video, file, or voice note inside a `Chat Channel` | No menu |
| Message still sending or failed to send | No menu (same as today) |
| `Call Logs` | No menu |
| Message already deleted | No menu |

*Option order:* `Copy` first (text messages only), then `Delete for everyone` (sender's 1:1 messages only).

### 0.4 Exact Text & Translations (EN / AR)

| Where Used | English | Arabic |
| :--- | :--- | :--- |
| Menu: Copy | `Copy` | `نسخ` *(Confirm AR)* |
| Menu: Delete | `Delete for everyone` | `حذف لدى الجميع` *(Confirm AR)* |
| Confirm Pop-up — Title | `Delete message?` *(Confirm text)* | `حذف الرسالة؟` *(Confirm AR)* |
| Confirm Pop-up — Body | `This message will be permanently deleted for everyone in this chat.` *(Confirm text)* | `سيتم حذف هذه الرسالة نهائياً لدى الجميع في هذه المحادثة.` *(Confirm AR)* |
| Confirm Pop-up — Buttons | `Cancel` / `Delete for everyone` | `إلغاء` / `حذف لدى الجميع` *(Confirm AR)* |
| Toast after Copy (Mobile & Web) | `Copied` | `تم النسخ` *(Confirm AR)* |
| Deleted Bubble & Preview (Sender) | `You deleted this message.` | `لقد حذفت هذه الرسالة.` |
| Deleted Bubble & Preview (Recipient) | `This message was deleted.` | `تم حذف هذه الرسالة.` |
| First-Time Tip — Title (Mobile) | `Delete message update` | `تحديث حذف الرسائل` *(Confirm AR)* |
| First-Time Tip — Body (Mobile) | `Tip: press and hold a message to copy it or delete it.` | `نصيحة: اضغط مطولاً على الرسالة لنسخها أو حذفها.` *(Confirm AR)* |
| First-Time Tip — Button (Mobile) | `Got it` | `حسناً` *(Confirm AR)* |
| Error: No Internet | `No internet connection. Please check your connection and try again.` | `لا يوجد اتصال بالإنترنت. يرجى التحقق من اتصالك والمحاولة مرة أخرى.` *(Confirm AR)* |
| Error: Server / General Error | `An error has occurred. Please try again.` | `حدث خطأ. يرجى المحاولة مرة أخرى.` *(Confirm AR)* |
| Admin Review & Export Label | `Deleted by sender` *(+ delete time)* | `محذوفة من قِبل المرسل` *(Confirm AR)* |

### 0.5 Analytics Tracking (NFR)
- **Event name**: `message_deleted` — sent once when `"Delete for everyone"` succeeds. Do not send if the user cancels, if the delete fails, or if the message was already deleted on another device.
- **Fields**:
  - `message_type`: `text` | `image` | `video` | `file` | `voice_note`
  - `platform`: `mobile` | `web`
  - `user_type`: `Guardian` | `Staff`
- *(Tracking tool and setup details are up to the developers.)*

---

## Story 1: Delete a Message I Sent for Everyone (Mobile App)

**Platform:** Mobile App  
**Designs:**
- Overview: [Mobile App screens 2.0 — Delete Flow](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-14821&t=Uqkk0on6FcITJcDt-4)
- Menu: [Mobile App screens 2.0 — Dropdown](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-14822&t=Uqkk0on6FcITJcDt-4)
- First-Time Tip: [Mobile App screens 2.0 — Tooltip](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-15785&t=Uqkk0on6FcITJcDt-4)
- Deleted Bubble: [Mobile App screens 2.0 — Deleted State](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-15345&t=Uqkk0on6FcITJcDt-4)
- Chat List Preview: [Mobile App screens 2.0 — Preview](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-15586&t=Uqkk0on6FcITJcDt-4)

**As a** Guardian or Staff member,  
**I want to** delete a message I sent in a 1:1 chat for everyone (and quickly copy text messages by pressing and holding),  
**So that** the other person can no longer see messages I sent by mistake or with wrong information.

### Mobile Interaction Notes (Colors, Icons & Layout Follow Figma)
- **How to open the menu**: Press and hold a message to open the menu next to it. If there is not enough space below the message, the menu opens above it instead. Tapping anywhere outside closes the menu with no changes.
- **Look and feel**: Deleted bubble styles, icons, and the dimmed background behind the first-time tip follow the Figma links above.

### Acceptance Criteria

```gherkin
Rule: Confirming delete removes a sent 1:1 message for both users, with no time limit

  Scenario: Sender confirms delete while the other person has the chat open
    Given Teacher Layla sent "Meet me at Gate 2" to Omar's Guardian in a 1:1 chat 4 days ago
    When Layla presses and holds that message, taps "Delete for everyone", and confirms
    Then Layla sees "You deleted this message." with the original time and no delivery or read ticks
    And Omar's Guardian sees "This message was deleted." right away without refreshing
    And neither user can open a menu on or translate the deleted message

  Scenario: Sender cancels delete in the confirmation pop-up
    Given Teacher Layla taps "Delete for everyone" on a message she sent to Omar's Guardian
    When Layla taps "Cancel"
    Then the message stays unchanged for both users

  Scenario: Sender deletes a message while Chat Availability is off
    Given Teacher Layla has her Chat Availability status turned off and is connected to the internet
    When Layla taps "Delete for everyone" on a sent 1:1 message and confirms
    Then the message is deleted for both Layla and Omar's Guardian

Rule: Menu options match the message type in 1:1 Chats and Chat Channels

  Scenario: User copies a text message inside a Chat Channel without seeing a delete option
    Given Omar's Guardian views a text message inside the "Tuition" Chat Channel
    When Omar's Guardian presses and holds the message and taps "Copy"
    Then the full message text is copied to the clipboard and a "Copied" toast appears
    And "Delete for everyone" is not shown in the menu

  Scenario: User presses and holds a message that has no menu options
    Given a 1:1 chat has a received voice note, a failed message, a call log, and an already-deleted message
    When the user presses and holds any of those items
    Then no menu opens

Rule: Chat list preview and unread status stay accurate without moving the chat

  Scenario: Sender deletes the latest unread message in a 1:1 chat
    Given Teacher Layla sent "Homework updated" as the latest message and Omar's Guardian has 1 unread message
    When Layla deletes that message for everyone
    Then Layla's chat list preview shows "You deleted this message."
    And Omar's Guardian's chat list preview shows "This message was deleted." and stays unread
    And the chat stays in its original place in the list

  Scenario: Sender deletes an older message while the recipient is offline
    Given Omar's Guardian is offline and there is a newer message after the one being deleted
    When Layla deletes the older message and Omar's Guardian opens the app later
    Then the chat list preview still shows the latest message
    And the older message inside the chat shows "This message was deleted."

Rule: Playing or translated content clears right away when deleted

  Scenario: A voice note is playing or a message is translated when deleted
    Given Omar's Guardian is playing a voice note from Layla (or reading a translated text message)
    When Layla deletes that message for everyone
    Then the voice note stops playing and the original and translated content are replaced by "This message was deleted."

Rule: First-time tip appears once per app install on a sent text message

  Scenario: User opens a 1:1 chat with a sent text message for the first time after updating
    Given Omar's Guardian has not seen the delete tip on this app install
    When they open a 1:1 chat that has a text message they sent
    Then the "Delete message update" tip points to that sent text message
    And tapping "Got it" or tapping outside closes it and it does not show again

  Scenario: User opens a 1:1 chat with no sent text messages yet
    Given Omar's Guardian has only received messages or sent media in their 1:1 chat
    When they open the chat for the first time after updating
    Then the tip does not show until they have a sent text message in a 1:1 chat

Rule: Delete handles connection errors and multi-device conflicts safely

  Scenario: Sender tries to delete with no internet connection
    Given Teacher Layla has no internet connection
    When she taps "Delete for everyone" and confirms
    Then the message stays unchanged
    And she sees "No internet connection. Please check your connection and try again."

  Scenario: A server error happens during delete
    Given a temporary server error stops the delete request
    When Teacher Layla confirms "Delete for everyone"
    Then the message stays unchanged so she can try again
    And she sees "An error has occurred. Please try again."

  Scenario: Message was already deleted from another device
    Given Teacher Layla opened the menu on Mobile and deleted the same message on Web
    When she confirms "Delete for everyone" on Mobile
    Then the message shows "You deleted this message." with no error message
```

---

## Story 2: Delete a Message I Sent for Everyone (Web — New Chat App)

**Platform:** Web (New Chat App)  
**Design:** [Demo Chat App](https://demo-chat.schoolvoice.com/chat?conversation=c16)  
**Shared Rules:** Follows all shared rules, options table, exact text, launch exclusions, and analytics in **§0**.

**As a** Guardian or Staff member using the Web Chat App,  
**I want to** delete a message I sent in a 1:1 chat for everyone (and copy text messages from the message menu),  
**So that** the other person can no longer see messages I sent by mistake or with wrong information on Web too.

### Web Interaction Notes (Look & Feel Follow Demo App / Figma)
- **How to open the menu**: Hovering over a message with actions shows a down-arrow (chevron) inside the bubble. Clicking the chevron or right-clicking the message opens the menu.
- **Normal right-click on other messages**: Messages with no menu show no chevron and keep the browser's normal right-click menu.
- **How to close the menu**: Clicking outside the menu or pressing `Esc` closes it with no changes.
- **No first-time tip**: The Mobile tip is not part of Web Story 2.

### Acceptance Criteria

```gherkin
Rule: Web message actions match the shared options table and desktop controls

  Scenario: Sender deletes a sent 1:1 message using the chevron or right-click and confirms
    Given Teacher Layla hovers over or right-clicks a message she sent to Omar's Guardian on Web
    When she clicks "Delete for everyone" and confirms
    Then Layla's Web and Mobile sessions both show "You deleted this message." with the original time and no ticks
    And Omar's Guardian sees "This message was deleted." right away without refreshing
    And the deleted bubble has no chevron, no menu, and no Translate option

  Scenario: User copies a text message on Web
    Given Teacher Layla opens the menu on a text message in a 1:1 Chat or the "Tuition" Chat Channel
    When she clicks "Copy"
    Then the full message text is copied to the clipboard, the menu closes, and a "Copied" toast appears

  Scenario: User hovers or right-clicks a message with no menu options on Web
    Given Omar's Guardian hovers over a received image, a call log, or an already-deleted message
    Then no chevron is shown
    And right-clicking opens the browser's normal right-click menu

Rule: Web matches Mobile on chat previews, unread counts, media stopping, and errors

  Scenario: Latest unread message is deleted on Web
    Given Teacher Layla deletes the latest message in her chat with Omar's Guardian before it is read
    Then Layla's chat list preview shows "You deleted this message." and the Guardian's shows "This message was deleted."
    And the Guardian's chat stays unread and stays in its original place in the list

  Scenario: Web delete fails because of lost internet or a server error
    Given Teacher Layla loses her internet connection on Web and confirms "Delete for everyone"
    Then the message stays unchanged
    And she sees "No internet connection. Please check your connection and try again."
```

---

## Story 3: See Deleted Messages in Chat Review & Chat Extraction (Admin Web)

**Platform:** Web (Admin Dashboard)  
**Design:** [Admin Chat Review Demo](https://demo-admin.schoolvoice.com/chat/review?lang=en&brand=schoolvoice&theme=light&trial=as-shipped&staff=1&guardian=1) *(Figma link for deleted bubble style and delete time is pending — see §4)*

**As a** School Admin,  
**I want to** still read messages that were deleted for everyone — along with when they were deleted — in Chat Review and Authorized Chat Extraction,  
**So that** I can review the full conversation with no missing messages.

### Access & Rules
- Uses the same `Chat Review` and `Authorized Chat Extraction` permissions and audit logs as today (no new permission needed).
- `Chat Review` stays read-only: no chevron, no menu, and no delete option on any message.
- Applies to messages from **both** Guardians and Staff across all message types (`text`, `image`, `video`, `voice note`, `file`).

### What the Admin Sees (Examples)

| Message Type | What the Admin Sees |
| :--- | :--- |
| Text | `"Deleted by sender"` + delete time, then the full original text |
| Image | `"Deleted by sender"` + delete time, then the original image |
| Video | `"Deleted by sender"` + delete time, then the playable original video |
| Voice note | `"Deleted by sender"` + delete time, then the playable original voice note |
| File | `"Deleted by sender"` + delete time, then the original file to open or download |

*(Bubble outline, icon, and muted text style follow the Figma design.)*

### Acceptance Criteria

```gherkin
Rule: Admins can read deleted messages and see when they were deleted

  Scenario: Admin opens a 1:1 chat with deleted messages from both sides
    Given Teacher Layla deleted a text message at 2:15 PM and Omar's Guardian deleted a voice note at 2:20 PM
    When an authorized School Admin opens their chat in Chat Review
    Then both messages stay in their original place in the chat with their original sent times
    And each deleted message shows "Deleted by sender" and its delete time above the full original content
    And the voice note can still be played and no menu or delete option is shown

  Scenario: Non-deleted messages stay unchanged
    Given a chat has both normal messages and deleted messages
    When an authorized School Admin opens Chat Review
    Then normal messages look and work the same as today

Rule: Chat Review shows newly deleted messages after refresh

  Scenario: A message is deleted while an Admin has Chat Review open
    Given an authorized School Admin is viewing Layla and Omar's Guardian's chat in Chat Review
    When Layla deletes a message for everyone and the Admin refreshes the page
    Then that message updates to show "Deleted by sender" and the delete time while keeping its original content

Rule: Authorized Chat Extraction includes deleted messages and delete times

  Scenario: Admin exports a chat that contains deleted messages
    Given a 1:1 chat has messages deleted for everyone by a Guardian or Staff member
    When an authorized School Admin runs Authorized Chat Extraction on that chat
    Then the exported file includes the deleted messages with their original content, "Deleted by sender", and the delete time
```

---

## 4. Items to Align Before the Sprint (Design & Team)

Check these quick items with Design and Engineering before Sprint start:

1. **Figma — Confirmation Pop-up (Stories 1 & 2)**: Add Mobile and Web designs for the `"Delete for everyone"` pop-up and confirm its wording.
2. **Figma — Admin Deleted Bubble & Delete Time (Story 3)**: Add the missing Figma link (left blank in the original draft) showing the outlined bubble and where the delete time appears.
3. **Arabic Translations**: Confirm all Arabic texts marked `*(Confirm AR)*` in §0.4.
4. **Quick Team Checks (if supported in Chat today)**:
   - **Quoted replies, chat search & shared media**: Make sure deleted messages are removed from quoted reply previews, search results, and shared media tabs.
   - **Media with captions**: If a photo/video/file can have a text caption, confirm whether `Copy` shows for the caption and that delete removes both.
   - **AI-flagged messages**: Confirm whether users can delete a message flagged by AI moderation and that Admin sees both the flag and `"Deleted by sender"`.
   - **District Admins**: Confirm whether District Admins viewing school chats also see deleted messages like Story 3.
   - **Shared devices (Mobile tip)**: Confirm whether showing the tip `"once per app install"` is fine for shared school tablets or if it should be once per user account.

---

## Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| v1.0 | 2026-11-19 | Reviewed from Youssif's draft | Merged shared rules (§0) to stop Mobile/Web drift; rewrote ACs in declarative BRIEF Gherkin; clarified `Chat Availability` vs. no internet; added confirmation pop-up, unread-stays-unread rule, Admin retention rule, delete time in Chat Review, `Authorized Chat Extraction` export support, Web `"Copied"` toast, voice-note stop rule, and EN/AR text table. Kept Copy + Text-Only Tip inside Stories 1 & 2. |
| v1.1 | 2026-11-19 | Reviewed from Youssif's draft | Rewrote the entire document in simple, plain English while keeping all rules, edge cases, and BRIEF Gherkin scenarios intact. |
