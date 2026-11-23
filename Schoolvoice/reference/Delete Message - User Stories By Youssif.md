# **Delete Message \- User Stories**

## **\[Delete Message\] Story 1: Delete a message I sent, for everyone**

**Platform:** Mobile App  
 **Design:**[Mobile App  screens 2.0](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-14821&t=Uqkk0on6FcITJcDt-4)

As a Guardian or Staff member  
 I want to delete a message I sent  
 So that I can fix a message I sent by mistake or with wrong content

**Acceptance Criteria:**

**Rules:**

* Only the sender can delete a message  
* No time limit: a message can be deleted at any time after it was sent  
* **Delete for everyone** is the only delete option (no "Delete for me")  
* "Delete for everyone" applies to 1:1 chats only  
* Channels also have the dropdown, but it contains "Copy" only (text messages only), with no "Delete for everyone"  
  * other message types have no dropdown  
* The user can delete messages even if his status is off (offline)

**Entry Point:**

* User long-presses a message inside a 1:1 chat or a channel  
* A dropdown opens next to the message  
  * as per the design:[Mobile App  screens 2.0](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-14822&t=Uqkk0on6FcITJcDt-4)  
  * If there is no space below the message for the dropdown to open (eg: the message is near the bottom of the screen or above the keyboard), the dropdown flips and opens above the message instead  
  * Tapping anywhere outside the dropdown closes it and nothing changes

**First-Time Hint:**

* A one-time tooltip introduces the new long-press dropdown appears:  
  * first time the user opens any 1:1 chat after the update  
  * appears on the user's text message that he can delete  
    * if no messages for him don't show the tool tip till he has a message for the tip to appear pointing to  
    * if no space the tip appears flipped same as the dropdown behavior  
    * Background behind the tooltip and the message is dimmed  
  * as per the design:[Mobile App  screens 2.0](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-15785&t=Uqkk0on6FcITJcDt-4)  
* Content:  
  * Title: "Delete message update"  
  * Text: "Tip: press and hold a message to copy it or delete it."  
  * Button: "Got it"  
  * The tooltip points at a message in the chat  
  * Tapping "Got it" or clicking outside it closes the tooltip and it is not shown again  
* Shown once per install on the user local app data

**Dropdown Options \- Per Message:**

| Message | Dropdown options |
| ----- | ----- |
| Text message I sent (sent successfully) | Copy, Delete for everyone |
| Image, video, file or voice note I sent (sent successfully) | Delete for everyone |
| Text message I received | Copy |
| Image, video, file or voice note I received | No dropdown |
| Text message inside a channel (sent or received) | Copy |
| Image, video, file or voice note inside a channel | No dropdown |
| Message still sending or failed to send | No dropdown (current behavior unchanged) |
| Call logs | No dropdown |
| Message already deleted | No dropdown |

* Dropdown option order:  
  * "Copy"  
    * "Copy" is shown for text messages only  
    * If the user taps "Copy" on a text message  
      * The full text of the message is copied to his clipboard  
      * The dropdown closes  
      * **\[toast message:\]** "Copied"  
  * "Delete for everyone"  
    * on the user's messages only

**Delete for Everyone \- Flow:**

* User taps "Delete for everyone"  
  * The dropdown closes  
  * The message is deleted for both the sender and the recipient

**\[DELETE \- Sender View\]**

* The message is replaced in place by a deleted message bubble:  
  * Text: "You deleted this message."  
    * Ar: "لقد حذفت هذه الرسالة"  
  * Bubble background: same blue as the sender's other messages  
  * Text style: italic, muted text color  
  * Icon: prohibit icon before the text  
  * as per the design:[Mobile App  screens 2.0](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-15345&t=Uqkk0on6FcITJcDt-4)  
* The bubble keeps its original message time, with no delivery or read tick  
* The bubble has no dropdown and user cannot interact with  
* The original content (text, image, video, file or voice note) is no longer visible  
* **\[tech validate\]:** A voice note that is playing when deleted stops playing and shows the deleted message bubble  
  * preferred if easy to be done  
  * If we couldn’t do it the deleted message bubble show up and the voice note continue playing till it ends

**\[DELETE \- Recipient View\]**

* If the recipient has the chat open:  
  * the deleted message is replaced in real time, without refreshing  
  * Text: "This message was deleted."  
    * AR: "تم حذف هذه الرسالة."  
  * Bubble background: same grey as the recipient's other messages  
  * Text style and icon: same as the sender view  
  * Long-press on the deleted message does nothing  
* If the recipient is offline when the message is deleted:  
  * The next time they open the chat, the message already shows as "This message was deleted."

**Chat List Preview:**

* If the deleted message is the latest message in the conversation:  
  * Sender sees: "You deleted this message." with the prohibit icon before it  
  * Recipient sees: "This message was deleted." with the prohibit icon before it  
* If it is not the latest message, the preview shows the latest message as it's  
* The conversation stays in the list even if the deleted message was the only message in the chat  
* as per the design:[Mobile App  screens 2.0](https://www.figma.com/design/7NW16eJwRWuKERRjIXQSiO/Mobile-App--screens-2.0?node-id=10084-15586&t=Uqkk0on6FcITJcDt-4)

**Not Recalled After Deletion (accepted for launch):**

* A push notification that was already delivered keeps its text on the recipient's device  
* An image, video or file the recipient already saved to their device stays on their device

**\[Analytics:\]**

* Google Analytics event `message_deleted` when "Delete for everyone" succeeds  
  * **Parameters:**  
    * message type (text, image, video, file, voice note)  
    * platform (mobile)  
    * User type: (Guardian, Staff)  
  * The event is not sent if the delete fails

**\[DELETE \- App or Network Errors\]**

* If no internet connection:  
  * \[Message\]: "No internet connection. Please check your connection and try again."  
  * The message stays unchanged  
* If general server error:  
  * \[Message\]: "An error has occurred. Please try again."  
  * The message stays unchanged and the user can try again

---

## **\[Delete Message\] Story 2: Delete a message I sent, for everyone**

**Platform:** Web (New Chat app)  
**Design:** [Demo app](https://demo-chat.schoolvoice.com/chat?conversation=c16)

As a Guardian or Staff member  
 I want to delete a message I sent  
 So that I can fix a message I sent by mistake or with wrong content

**Acceptance Criteria:**

**Rules:**

* Only the sender can delete a message  
* No time limit: a message can be deleted at any time after it was sent  
* **Delete for everyone** is the only delete option (no "Delete for me")  
* "Delete for everyone" applies to 1:1 chats only  
  * Channels also have the chevron and dropdown, but it contains "Copy" only (text messages only), with no "Delete for everyone"  
  * Other message type that cannot be copied have no dropdown  
* The user can delete messages even if his status is off (offline)  
* Same rules as the mobile app (Story 1\)

**Entry Point:**

* User hovers over a message inside a 1:1 chat or a channel  
* A chevron (down arrow) button appears inside the message bubble  
* Clicking the chevron or Right-clicking anywhere on the message opens a dropdown below it  
  * On a message with no menu, no Chevron is shown and the browser's own right-click menu is shown as usual  
* Clicking anywhere outside the menu, or pressing Esc, closes it and nothing changes

**Menu Options \- Per Message:**

| Message | Chevron and menu options |
| ----- | ----- |
| Text message I sent (sent successfully) | Copy, Delete for everyone |
| Image, video, file or voice note I sent (sent successfully) | Delete for everyone |
| Text message I received | Copy |
| Image, video, file or voice note I received | No chevron, no menu |
| Text message inside a channel (sent or received) | Copy |
| Image, video, file or voice note inside a channel | No chevron, no menu |
| Message still sending or failed to send | No chevron, no menu (current behavior unchanged) |
| Call logs | No chevron, no menu |
| Message already deleted | No chevron, no menu |

* Menu option order:  
  * "Copy"  
    * "Copy" is shown for text messages only  
    * If the user clicks "Copy" on a text message  
      * The full text of the message is copied to the clipboard  
      * and the menu closes  
  * "Delete for everyone"  
    * on the user's messages only

**Delete for Everyone \- Flow:**

* User clicks "Delete for everyone"  
  * The menu closes  
  * The message is deleted for both the sender and the recipient

**\[DELETE \- Sender View\]**

* The message is replaced in place by a deleted message bubble:  
  * Text: "You deleted this message"  
  * Bubble background: same blue as the sender's other messages  
  * Text style: italic, muted text color  
  * Icon: prohibit icon before the text  
* The bubble keeps its original message time, with no delivery or read tick  
* The bubble has no chevron, no menu  
* The original content (text, image, video, file or voice note) is no longer visible

**\[DELETE \- Recipient View\]**

* If the recipient has the chat open:  
  * The deleted message is replaced in real time, without refreshing  
  * Text: "This message was deleted."  
  * Bubble background: same gray as the recipient's other messages  
  * Text style and icon: same as the sender view  
  * No chevron and no menu or translate option on the deleted message  
* If the recipient is offline when the message is deleted:  
  * The next time they open the chat, the message already shows as "This message was deleted."

**Chat List Preview:**

* If the deleted message is the latest message in the conversation:  
  * Sender sees: "You deleted this message" with the prohibit icon before it  
  * Recipient sees: "This message was deleted." with the prohibit icon before it  
* If it is not the latest message, the preview shows the latest message as is  
* The conversation stays in the list even if the deleted message was the only message in the chat

**\[Analytics:\]**  
 Google Analytics event `message_deleted` when "Delete for everyone" succeeds  
 \- **Parameters:**  
 \- message type: (text, image, video, file, voice note)  
 \- platform: (Web)  
 \- User type: (Guardian, Staff)  
 \- The event is not sent if the delete fails

**\[DELETE \- App or Network Errors\]**

* If no internet connection:  
  * \[Message\]: "No internet connection. Please check your connection and try again."  
  * The message stays unchanged  
* If general server error:  
  * \[Message\]: "An error has occurred. Please try again."  
  * The message stays unchanged and the user can try again

---

## **\[Delete Message\] Story 3: See Messages Deleted by the Sender in Chat Review**

**Platform:** Web (Admin Dashboard)  
 **Design:**[Chat review app](https://demo-admin.schoolvoice.com/chat/review?lang=en&brand=schoolvoice&theme=light&trial=as-shipped&staff=1&guardian=1)

As a School Admin  
 I want to still read a message that was deleted for everyone  
 So that I can review a conversation with the full picture and no messages missed

**Acceptance Criteria:**

**Entry Point:**

* Admin navigates to Chat \-\> Chat review  
* Selects a staff member and a guardian to read their conversation  
  * Same access and permissions as today. No new permission is needed  
* The messages load for the staff as it is with the deleted messages  
  * Messages deleted with "Delete for everyone" (Stories 1 and 2\) are kept in Chat review  
    * The original content is still shown  
    * The message is marked as deleted by the sender  
  * Chat review is read-only. There is no chevron, no dropdown and no delete option on any message  
  * Applies to every message type: text, image, video, voice note, file  
  * Applies to messages from both sides: the guardian's and the staff member's  
  * Everything else in Chat review is unchanged

**Deleted Message Display:**

* The message keeps its original content  
  * Text: the full text is shown  
  * Image or video: the media is shown  
  * Voice note: the player is shown and can be played  
  * File: the attachment chip is shown and can be opened or downloaded  
* The message bubble is shown with an outline and no background color  
  * as per the design:  
* A line is added at the top of the bubble, above the content:  
  * Icon: prohibit icon before the text  
  * Text: "Deleted by sender"  
  * Text style: muted text color  
* The bubble keeps its original content, its time and its place in the conversation  
* Messages that were not deleted are unchanged

**Deleted Message Display \- Examples:**

| Message type | What the admin sees |
| ----- | ----- |
| Text | "Deleted by sender" line, then the full text |
| Image | "Deleted by sender" line, then the image |
| Video | "Deleted by sender" line, then the video with its play button |
| Voice note | "Deleted by sender" line, then the voice note player |
| File | "Deleted by sender" line, then the file chip |

**Updates:**

* A message deleted while the admin has the conversation open updates on refresh

---

 