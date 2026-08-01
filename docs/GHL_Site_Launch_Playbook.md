# GHL Site Launch Playbook
### The repeatable process, extracted from the BizRevGrowth rebuild (2026-07-31 / 2026-08-01)

**Purpose:** run this end to end on any GoHighLevel site. Written so the next
site (jhpropertypartners.com) does not have to rediscover any of it.

**How to use:** work top to bottom. Phases 0 to 3 are diagnosis and cheap wins.
Phase 4 is the grind. Phase 5 is verification. Do not skip Phase 0: it is what
stops you touching the same element twice.

---

## PHASE 0 · Instrument before you touch anything

Copy `scripts/audit_site.py` and `scripts/sweep_dashes.py` into the new repo and
repoint `BASE` and the CHECKS list. **Never audit by eye and never trust the
rendered DOM.**

Rules that cost us time before we learned them:

- **Fetch RAW HTML, not the rendered page.** Cloudflare caches ~60s and query
  strings do not bust it. Send `Cache-Control: no-cache` and check
  `last-modified`.
- **Every element appears TWICE** in GHL raw HTML: once rendered, once in the
  page payload. A count of 2 means ONE thing to fix, not two.
- **Grep fragments, not whole words.** A brand name split across a tag
  (`Sniper<b>Path</b>`) is invisible to a search for the whole word.
- **Grep colours in every notation.** `#e63946` AND `rgb(230,57,70)` AND
  `rgba(...)`. A hex-only sweep missed 18 instances, including a red box-shadow.
- **Class names are not proof of rendering.** A page can carry `c-nav-menu`
  CSS classes with no nav on it. Check *visible text*.

Baseline to capture on day one: per page, counts of the old brand name, every
retired colour, wrong fonts, banned words, and which SEO fields are empty.

---

## PHASE 1 · The high-leverage edits (do these first)

Colour and font problems are almost never per-element. Find the shared
definitions first.

1. **Theme colour variables.** One variable drove ~34 usages across 5 pages.
   Find them (`--color-<hash>: #<oldhex>`) and change them at the theme level.
2. **Global header/footer CSS.** One hover rule appeared 4x on every page.
3. **`--headlinefont` per page.** It is set per page, not globally.

**Map colours by ROLE, not by what the old colour was:**

| Slot drives | Use |
|---|---|
| Text on white, links, button backgrounds | primary (must pass AA on white) |
| Hover/active, icons, large decorative accents | secondary/bright |
| Body copy, headings | dark neutral |

We got this wrong once: assigned the bright accent to a slot that drove link
text, which fails AA at body size. **Check what the variable actually drives
before assigning.**

---

## PHASE 2 · Hunt dead assets

Every image URL on the site should be fetched and status-checked. On BRG we
found **two 404s**: the favicon (so the site had no tab icon at all) and the
header logo (so the desktop header showed a broken image). Both were casualties
of an asset swap where the old file was deleted and the reference never
repointed.

```
curl -sS -o /dev/null -w "%{http_code}" <every image URL on the page>
```

A 404 from these CDNs returns a small XML `NoSuchKey` body with a 200-looking
size, so **check the status code, not the byte count.**

---

## PHASE 3 · Site-level (cheap, high value, often completely missing)

Check all of these on production before assuming any exist:

- [ ] `www.<domain>` **redirects** to apex. Ours returned a hard **404**. GHL
      offers a one-click fix under Settings > Domains.
- [ ] Old/parked domains 301 to the new one, **Entire Domain (/\*)** so paths
      carry over. Note: the Domains list showed our old domain as
      "Connected Products: None" while it was actively serving the whole site.
      **Do not trust that column.**
- [ ] `robots.txt` has content (allow + Sitemap directive)
- [ ] `sitemap.xml` lists the real pages. Ours served 200 with **zero bytes**,
      then a valid-but-empty `<urlset>`. A generated sitemap may also include a
      **`/test_path?item=123` placeholder** that 301s to the error page: delete it.
- [ ] `llms.txt` written (the AI-crawler file: what the business is, prices,
      pages, contact, plus a "notes for answer engines" block)
- [ ] Custom **404 page** built and wired
- [ ] A nonsense URL behaves correctly

⚠️ **GHL implements a custom 404 as a 301 to the error page, which then returns
200.** That is a soft 404 by Google's definition. Tradeoff: a branded page for
humans versus a correct status code for crawlers. If you keep it, set the error
page **noindex** so those URLs never enter the index.

---

## PHASE 4 · Per page: copy, SEO, schema

For each page, in the page builder:

**A. Copy.** Do copy + colour + font in the SAME pass per element. Touching an
element twice is the expensive mistake.

**B. SEO panel** (the doc-with-magnifier icon, 10th in the toolbar):
- Title, meta description (both were entirely absent on several pages)
- Author (E-E-A-T signal)
- **Links & tags**: canonical, `og:image`
- **Schema markup** at the bottom

**C. Schema.** Click any schema chip, switch **Form view -> JSON view**, select
all, paste the full `@graph`, Validate & Save.

GHL schema-builder limits learned the hard way:
- A Product accepts **ONE `Offer` or an `AggregateOffer`, never an array.**
  An array silently collapses to the first item and then fails validation with
  a useless "Technical issue in JSON script".
- Product wants an **`image`**.
- Stick to well-known types (`WebPage`, not `PrivacyPolicy`).
- Both the "Add Schema" and "Edit Schema" dialogs accept a full pasted `@graph`.

**D. Save, then Publish.** They are separate. Saved work is invisible on
production, and it is easy to spend a session editing and think it shipped.

---

## PHASE 5 · Verify on production

Re-run the audit. Then by hand:

- [ ] Both viewports for anything with a desktop/mobile twin
- [ ] Any hidden UI (we had a Monthly/Annual toggle hiding a whole pricing row)
- [ ] Every page's title/description/canonical/schema present
- [ ] All sitemap URLs return 200
- [ ] Nav links resolve to the right domain and are not `target="_blank"`
      for internal pages

---

## THE GHL LANDMINE LIST

Carry this to every GHL site.

1. **Desktop and mobile are SEPARATE COPIES** of most text. Editing one does
   not touch the other. This was the single biggest source of bugs. Custom HTML
   with media queries is one copy and removes the whole class of problem.
2. **Global sections do NOT auto-attach to a new page.** A page you create is
   bare: no header, no footer. Add them deliberately.
3. **Save and Publish are different buttons.**
4. **`position: fixed` breaks inside GHL sections** (a transformed ancestor
   traps it). Inject fixed elements into `<body>` via JS.
5. **Raw logo exports carry 49-69% baked-in transparent padding.** Crop before
   uploading or the header gets mystery whitespace.
6. **The template hardcodes fonts and colours on elements**, so site-level CSS
   alone does not override them.
7. **A section's editor "name" is not its HTML id.** For anchors, inject a
   `<div id="...">`.
8. **`pbcopy` mangles UTF-8 into CodeMirror.** Smart quotes become garbage.
   Convert non-ASCII to HTML entities before pasting.
9. **CodeMirror has no find/replace.** Do not paste one giant block you will
   need to edit later. Use several medium blocks.
10. **The builder is heavy and unreliable on big pages.** It failed to load
    four times in one session, and on a brand-new empty page the Ask AI panel
    swallows clicks on "Blank Section" while Escape unloads the builder.

---

## ⛔ THE GHL "ASK AI" RULE

**Never let it write copy, and never believe its status reports.**

On this project it:
- emitted the retired brand name and the **wrong legal entity type**
  ("LLC" where the entity is an Inc.) into a *legal* page draft, and
- **claimed to have inserted a content block that did not exist.** The layer
  tree showed no such block and production showed no trace of it.

It is fine as a layout nudge. It is not fine anywhere near copy, legal text,
or a factual claim. Verify everything it says against the layer tree and
production HTML.

---

## WHAT "GOOD" LOOKS LIKE AT THE END

Per page: title, meta description, author, canonical, `og:image`, schema.
Site-wide: robots.txt, sitemap.xml, llms.txt, branded 404 (noindex),
www redirect, old-domain 301, zero dead asset URLs, zero retired-brand strings
in visible text, one brand palette, one font pair.
