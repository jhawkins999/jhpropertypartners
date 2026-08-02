# JH Property Partners — Operator Observations

Durable, reusable lessons. **Not a session log** (that is `docs/Session_Log.md`)
and not a task list (that is `docs/TODO.md`). If a lesson only makes sense in the
context of one session, it belongs in the session log instead.

Append a new numbered section each session that produces one; grep the last
`## Section N` first so numbering continues. Changelog at the bottom.

---

## ⚠️ Provenance of Section 1

**Section 1 was ported from the BizRevGrowth repo on 2026-08-01, before this
project had run a real working session.** Everything in it is a property of
**GoHighLevel or of verification method**, not of a brand, which is why it
transfers. It has been earned on a live GHL site, just not on *this* one.

**Nothing about BRG's audience, offer, pricing, voice, banned words or
positioning came across, and none of it applies here.**

Sections 2 onward should come from this project's own sessions.

---

## Section 1 — GoHighLevel and verification (ported 2026-08-01)

### 1a · Verification

**A tool's self-report is not evidence.** GHL's Ask AI reported inserting a
content block that did not exist in the layer tree or in production, and the
block it described contained a retired brand name and the wrong legal entity
type. Verify any claim against the artifact.

**Verify the thing users get, not the thing you edited.** Four pages once sat
saved-but-never-published for an entire session while returning HTTP 200 the
whole time, because an older published version was still being served. **A 200
is not proof your change shipped.**

**Raw-text greps give FALSE NEGATIVES on rendered HTML.** A check for em dashes
reported three pages clean; they were not. HTML stores the character as
`&#8212;`. Whenever a check says "already done," ask what encoding the haystack
is in before believing it.

**Correct markup can still render wrong.** An image with valid HTML, a verified
200 URL and correct classes rendered badly stretched, because it carried
`width`/`height` attributes while the CSS set `width:100%` with no
`height:auto`, so the height attribute won. **A source grep said everything was
fine.** For anything visual, measure the rendered element.

**Verify an image URL by DECODING it, not by status code alone.** The real check
is three-part: HTTP 200, a `content-type` of `image/*`, and it decodes as an
image of the expected size. These CDNs answer a missing file with a small XML
`NoSuchKey` body, which passes a naive "did it respond?" test. This is how a
favicon and a header logo were both dead at once while looking fine.

**Swap order for any asset:** upload new, verify the new URL returns 200,
update the reference, and **only then** delete the old file. Never delete first.

**A stale preview can look like a real difference.** A page-list thumbnail
showed an old colour long after the element had been changed. Trust production
HTML over any preview image.

### 1b · Finding what hides

**Content can be produced by something that is not the content.** A homepage
rendered a brand name that appeared nowhere in the builder, because the builder
held `{{location.name}}` and the merge tag resolved at publish time. Names also
hide split across tags (`Sniper<b>Path</b>` defeats a search for the whole
word). **Search the RENDERED output for the symptom, then trace backwards.**

**Pinning a check to an exact phrase on one page hides a whole class.** An audit
checked three exact phrases on one page and a fourth violation on that same page
survived every pass. Check for the CLASS, not the instance you know about.

**Duplicate variants drift apart silently.** A page served both an old line and
its replacement in different viewports. One was fixed, the other never touched,
and nothing surfaced the inconsistency. Where a thing exists twice, check both,
and expect the WORDS to differ, not just the layout.

### 1c · Working in the builder

**The builder canvas is cross-origin:** no accessibility tree, no scripting.
Targeting is screenshot coordinates only, and opening a settings panel reflows
the canvas, so coordinates captured before a click are stale after it.

**Selection behaviour is inconsistent. Verify before typing.** Triple-click
grabbed the wrong element once and only one of three lines another time.
`cmd+A` inside an element is more reliable. **Screenshot the selection before
typing over it** — one near-miss had the page headline selected.

**Prefer ONE custom-HTML block for a new section.** It removes the
desktop/mobile twin problem, is one element instead of dozens, and cannot leave
a half-built section on a live page. **Keep it pure ASCII**: `pbcopy` mangles
UTF-8 into CodeMirror (smart quotes became `,Äú`).

**Typing `?` can fire a keyboard shortcut instead of entering text** (shift+/
opens GHL's shortcut help) when focus is not truly inside a text element. If
typed text does not appear, check focus before retyping.

### 1d · Rules and canon

**An inferred rule enforced long enough starts to look like canon.** On the
other project a banned-word list was compiled from general direction, written
into canon, and enforced across four files for days. When the owner finally saw
it he cut it to two phrases. **Record WHO decided a rule and WHEN; mark inferred
rules INFERRED and get them ruled on.**

**A test beats a list.** The same list kept growing and still missed the actual
problem, because the problem was never vocabulary. The replacement rule was:
*every sentence names a concrete mechanism or a concrete result, or it gets
cut.*

**Being under-informed about the owner produces confidently wrong advice.** A
too-narrow biography in canon caused active, repeated advice AGAINST claims that
were true. **This matters here: most of this project's CLAUDE.md is UNKNOWN.**
Ask rather than infer.

### 1e · Tool boundaries

**The browser file-upload tool only accepts files the user has explicitly shared
with the session**, and clicking a native upload button opens an OS dialog that
cannot be driven. Uploading to GHL Media Storage is therefore always John's
step. Hand him the file and ask for the URL rather than discovering the wall
halfway through.

**Some domains are blocked for browser navigation** even when reachable by
`curl`. Verify page content with `curl` + parsing; use the browser only when
rendering or computed style genuinely matters.

---

## Changelog

- **2026-08-01** — File created. Section 1 ported from the BizRevGrowth repo:
  GoHighLevel platform behaviour and verification method only, with an explicit
  note that no brand or content canon came with it.
