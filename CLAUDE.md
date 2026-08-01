# CLAUDE.md — JH Property Partners
# Read this file at the start of every session.

> **⚠️ THIS FILE IS A SKELETON, SEEDED 2026-08-01.** Most of it is marked
> **UNKNOWN**. That is deliberate. Nothing here was inferred, assumed, or
> carried over from another project. Fill each section in only from what John
> actually says or what is verifiable on the live site. **Do not guess, and do
> not let a blank section become an invented one.**

## WHAT THIS IS
JH Property Partners buys houses for cash. The live site's own words:
**"Sell Your House Fast for Cash."**

- Domain: **jhpropertypartners.com** — LIVE, and it is a **GoHighLevel site**
  (LeadConnector / filesafe / msgsndr all present in the HTML). Not custom code.
- Six real pages: `/`, `/services`, `/testimonials`, `/contact`,
  `/privacy-policy`, `/terms-and-conditions`. Plus `/home-750690`, which is the
  homepage's internal path and currently serves duplicate content.
- Owner: John Hawkins (same person as the BizRevGrowth and Triwise projects).

**UNKNOWN and needed:** the offer in John's own words, the buy criteria/market,
the geography, how leads are worked after the form, what happens to a house
after purchase, and whether this is his own operation or a partnership.

## ⛔ SEPARATE FROM BIZREVGROWTH AND TRIWISE
Different business, different audience, different offer.

**Neither BizRevGrowth canon nor Triwise canon governs this project.** Do not
import: BRG's pricing tiers, its "never the actor" rule, its banned-word list,
its no-testimonials rule, its brand palette, the $50K guarantee, or anything
from `~/projects/triwise-fm`. Do not run `/canon` here.

What DOES carry over is **process, not content**:
`docs/GHL_Site_Launch_Playbook.md` and the four scripts in `scripts/`.

⚠️ Note one concrete difference already visible: this site HAS a
`/testimonials` page. BizRevGrowth banned testimonials because it had zero
clients. **That rule does not apply here** — but before relying on any of them,
confirm with John that they are real and that he can substantiate them. The
FTC's 2024 rule on consumer reviews applies to this industry too.

## AUDIENCE — UNKNOWN
The seller is presumably a homeowner who wants speed or certainty over price
(probate, inherited, distressed, tired landlord, relocation). **This is an
inference from the category, not something John has said. Confirm before
writing a word of copy against it.**

## OFFER / PRICING — UNKNOWN
Not stated anywhere yet. Do not invent numbers, timelines ("close in 7 days"),
fee structures, or guarantees.

## BRAND — UNKNOWN
No brand kit supplied. Colours, fonts, and logo files have not been audited.
Run the Phase 1 sweep in the playbook and record what is actually on the site
before proposing changes.

## VOICE / BANNED LANGUAGE — UNKNOWN
No list agreed yet. Two rules John has applied to his other projects that are
worth ASKING about rather than assuming:
- no em dashes in client-facing copy
- outcome-focused copy: say what the person GETS, not what the process is

⚠️ **This industry has real compliance sensitivity.** Cash-offer marketing
attracts scrutiny around pressure tactics, unsubstantiated "we buy any house"
claims, and how offers are characterised. Do not write claims about price,
speed, or fees that John has not confirmed he can stand behind.

## INVENT NOTHING
Same discipline as the other projects, for the same reason. No fabricated
testimonials, no invented close times, no made-up statistics, no compliance
claims. If a number or claim is not verifiable, it does not go on the site.

## ⛔ NEVER USE GHL'S "ASK AI"
Carried over as a hard rule because it is a property of the platform, not of a
brand. On the previous project it emitted a retired brand name and the **wrong
legal entity type** into a legal page, and it **claimed to have inserted a
content block that did not exist**. Fine as a layout nudge; never near copy,
legal text, or a factual claim. Verify anything it says against the layer tree
and raw production HTML.

## BASELINE (measured 2026-08-01, before any changes)
Full detail: `docs/Baseline_Audit_2026-08-01.md`. Headlines:

**Better than expected:** every page already has a title, a meta description,
and schema. That is further along than BizRevGrowth was at the same point.

**Missing or broken:**
- **No canonical on any page**, and `/home-750690` serves the homepage's
  content under a second URL with the same title. That is live duplicate
  content.
- **No `og:image` anywhere** — every shared link renders with no picture.
- **`www.jhpropertypartners.com` returns 403.** An entire hostname is dead.
- **`robots.txt`, `sitemap.xml`, `llms.txt` all return 200 with ZERO bytes.**
- No `robots` meta anywhere; no custom 404 verified yet.

## KEY FILES
- **`docs/GHL_Site_Launch_Playbook.md` — the process. Read it before touching
  the site.** Carries the full GHL landmine list.
- `docs/Baseline_Audit_2026-08-01.md` — what was true before we started
- `docs/TODO.md` — the live checklist, read first
- `docs/Session_Log.md` — rolling session log, newest first
- `scripts/audit_site.py` — SEO state per page; CHECKS/SWEEPS are empty until
  the brand kit and banned-word list are decided
- `scripts/sweep_dashes.py` — em/en dash sweep across all pages
- `scripts/greenify_logo.py`, `scripts/crop_logos.py` — logo tooling, reusable

## WORKING RULES (carried over, platform-level)
- **Verify on PRODUCTION by fetching RAW HTML, never the rendered DOM.**
  Cloudflare caches ~60s and query strings do not bust it.
- **Every element appears TWICE** in GHL raw HTML (rendered + payload).
  A count of 2 means ONE thing to fix.
- **Save and Publish are different buttons.**
- **Desktop and mobile are separate copies** of most text in GHL templates.
- **Global sections do NOT auto-attach** to a newly created page.
