# Baseline audit — jhpropertypartners.com
### Measured on production, 2026-08-01, BEFORE any changes

This is the "what was true when we started" record. Do not edit it later to
reflect fixes; add fixes to `docs/TODO.md` and the session log instead.

Method: raw HTML fetched with `Cache-Control: no-cache`, never the rendered DOM.

---

## Platform

**GoHighLevel**, same as BizRevGrowth (LeadConnector, filesafe.space and
msgsndr references throughout). Served through Cloudflare. So the entire GHL
landmine list in `GHL_Site_Launch_Playbook.md` applies here.

## Pages

| Page | HTTP | Size |
|---|---|---|
| `/` | 200 | 407 KB |
| `/services` | 200 | 263 KB |
| `/testimonials` | 200 | 252 KB |
| `/contact` | 200 | 310 KB |
| `/privacy-policy` | 200 | 93 KB |
| `/terms-and-conditions` | 200 | 101 KB |
| `/home-750690` | 200 | 407 KB |

## SEO fields

| Page | title | desc | canonical | schema | og:image | robots |
|---|---|---|---|---|---|---|
| home | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| services | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| testimonials | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| contact | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| privacy-policy | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| terms-and-conditions | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| home-750690 | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |

**This is a much better starting point than BizRevGrowth had.** Titles, meta
descriptions and schema are already present on every page, and they read as
deliberately written rather than template junk.

Existing titles:
- `/` and `/home-750690` — *JH PROPERTY PARTNERS | Sell Your House Fast for Cash*
- `/services` — *JH PROPERTY PARTNERS | Property Buying services*
- `/testimonials` — *JH PROPERTY PARTNERS | Reviews & Testimonials | Real Sellers*
- `/contact` — *JH PROPERTY PARTNERS | Get a Fair Cash Offer for Your House*
- `/privacy-policy`, `/terms-and-conditions` — straightforward

## Assets

**16 unique images on the homepage, all returning 200.** No dead URLs found.
(BizRevGrowth had two 404s, including its favicon and header logo, so this was
worth checking explicitly.)

## Homepage schema

Nodes present: `Organization`, `RealEstateAgent`, `Service`, `WebPage`,
`Review`, `Review`.

⚠️ **Two `Review` nodes need a conversation before anything else is done with
them.** Review markup placed by a business on its own site about itself is
"self-serving" — Google has not shown it as a rich result since 2019, and if
the reviews are not genuine and substantiable it is a manual-action risk. The
FTC's 2024 consumer-review rule also applies to this industry. **Action: ask
John whether these are real, attributable reviews he can evidence.** Do not
remove or defend them until that is answered.

---

## 🔴 Problems found

### 1. `www` returns 403
```
https://www.jhpropertypartners.com/   ->  403
```
An entire hostname is dead. Not a redirect, not a 404, a hard 403. Anyone
typing "www" gets an error page. On BizRevGrowth the equivalent was a 404 and
GHL had a one-click fix under Settings > Domains.

### 2. Duplicate homepage, no canonical anywhere
`/home-750690` returns 200 and serves the homepage's content with the **same
title**. With no canonical tag on any page, Google sees the homepage twice.
This is the same internal-path pattern BizRevGrowth had (`/home-584399`).

### 3. Every unknown URL 301s to the homepage
```
/definitely-not-a-page  ->  301  ->  https://jhpropertypartners.com/
```
That is a **soft 404**, and it is the more harmful variant: redirecting all
unknown URLs to the homepage is a pattern Google names explicitly. A missing
page should return 404 or 410, or at minimum land on a real error page.

### 4. Site-level files are empty
| File | Status |
|---|---|
| `robots.txt` | 200, **0 bytes** |
| `sitemap.xml` | 200, **0 bytes** |
| `llms.txt` | 200, **0 bytes** |

Identical to BizRevGrowth's starting state. A blank sitemap is worse than none.

### 5. No `og:image` on any page
Every link shared to Facebook, LinkedIn or iMessage renders with no picture.
For a business where trust is the whole sale, that is a real cost.

---

## Not yet checked

- Colour and font consistency (Phase 1 of the playbook)
- Desktop vs mobile twins
- Copy quality against a voice/banned-word standard **that does not exist yet**
- Whether a custom 404 page exists
- Form behaviour, and where leads actually go
- Whether the reviews on `/testimonials` match the schema `Review` nodes
