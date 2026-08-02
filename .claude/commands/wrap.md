---
description: Close the JH Property Partners session cleanly.
---

Close the JH Property Partners session cleanly. Do all of the following, in
order, following the existing conventions in each file (read the most recent
example first so format and numbering match). Today's date: run `date +%F`.

This is a LIGHT wrap. No content vault, no dated handoff files. One lean
checklist (`docs/TODO.md`) — keep it current, do not let it grow into prose.

1. **Session log.** Prepend a new dated entry at the top of the "Sessions" list
   in `docs/Session_Log.md` (newest first). What changed, what was decided, what
   is still open. A tight paragraph.

2. **`docs/TODO.md`.** Check off ([x]) what finished, delete what is obsolete,
   add new next-session tasks with enough context to act on without re-reading
   the log. **Re-verify anything you mark as still-open against live production
   first.** Leaving a stale to-do in this file wastes John's time directly; it
   has happened before on the sister project and he called it out.

3. **`CLAUDE.md`.** Update if any of these changed: something moved from
   **UNKNOWN to KNOWN** (the most important case on this project), a locked
   decision, the brand kit, the banned-language list, a new landmine, or the
   open items. **Record WHO decided a new rule and WHEN.** If a rule is your
   inference rather than John's decision, mark it INFERRED and flag it for a
   ruling. Never let an inference harden into canon.

4. **Operator Observations.** If the session produced a *durable, reusable*
   lesson, append a new numbered section to `docs/Operator_Observations.md`
   (grep the last `## Section N` first) and add a dated changelog line.
   **Principles, not a task log.** Skip entirely if nothing durable surfaced.

5. **Commit and push.** Author is John Hawkins, **no Co-Authored-By trailers**
   (every commit, not just the wrap commit), no em dashes in commit messages.
   Use the noreply email form `237903452+jhawkins999@users.noreply.github.com`.
   Then verify the push actually landed:
   ```
   git rev-parse HEAD
   git ls-remote origin main | cut -f1
   ```
   They must match. A push is not a deploy, and a silent failure looks like
   success.

6. **Next-session opening prompt.** Write `docs/Next_Session_Prompt.md`
   (overwrite; it is a rolling file). A ready-to-paste opener with: priorities in
   order, what to read first, current live state, open decisions John owes, and
   the gotchas that would otherwise be rediscovered. Paste it into the chat reply
   too, so John can copy it without opening the file.

**Report:** a bullet list of every file written or updated, and the commit(s).

**Do not:** apply BizRevGrowth or Triwise canon, run `/canon`, write a dated
handoff file, fill an UNKNOWN section from inference, or touch anything in
`~/projects/bizrevgrowth`, `~/projects/triwise-fm` or `~/projects/triwise-content`.
