
This is a summary of what I think we can do about this feature (I typed it all by myself, btw, and didn't involve AI so I could think clearly—maybe I'll just have it fix some vocab, but that's it 😁—so please review it and tell me which parts are helpful and what we need to rethink about).

Edge Cases:
- Given a parent uploaded an excuse at time X before the end of the attendance day
  When the parent deletes it after the end of the attendance day
  Then ----
	1. They won't be able to delete it after the end of the attendance day. (Could be bad UX)
	2. They can delete it, and if that causes them to cross the number of days that triggers the automated message, then just send the automated message.
	   (Could lead to duplicate messages if there are 2 automated messages configured for 2 consecutive days.
		   - Solution:
		     1. Send only the automated message for the highest number of days.
			 2. Send only the automated message for the highest number of days + 
			 +a notification to the admin that the parent deleted the old excuse.
			 3. Send only the automated message for the highest number of days + save a log in the database showing that the parent deleted the old excuse (good for tracking).
			 4. We can enforce that the chosen days must have a +/-2 day difference from the nearest automated message trigger (for example, if the last one is set to 3 days total, then the next has to be 1 or 5 days). (Not the best CX, and I think it will lead to complicated logic later, but I'm keeping it here so I don't revisit it later.))


- Personally, I don't think a school would set up automated messages for two consecutive days, especially since at the end of the attendance day, guardians are usually on their way to pick up their children from school, so they wouldn't be uploading excuses then.

- It's a really rare test case (unprofessional from the school's side, and rare on the guardians' side), so it shouldn't lead to the bug we're worried about.

My personal suggestion after all:
- Given the time limit to delete is 30 mins (ending at the attendance day cutoff), if a guardian uploads an excuse within that window (30 - X mins before the attendance day ends), we pop up a message notifying them that they can only delete it during the remaining time, though they can still edit it—and if they want time to rethink, they should just upload it after the attendance day ends so they'll have the full 30 mins to delete it if they want.
> (Or simply the same message telling them to upload after the attendance day ends, or they won't be able to remove the excuse—since it's a rare test case.)


