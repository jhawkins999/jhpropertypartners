# JH Property Partners Session Log

Rolling log, newest first. One tight entry per session. Locked decisions live
in `CLAUDE.md`, not here. If a decision only appears in this log, the next
session will miss it.

## Sessions (newest first)

- **2026-08-01 (1st) — Repo seeded and baseline captured.** Created the project
  and ran the Phase 0 audit from `docs/GHL_Site_Launch_Playbook.md` before
  writing anything. **The site is live and is a GoHighLevel build** (same
  platform as BizRevGrowth, so the whole landmine list applies). Six real pages
  plus `/home-750690`, which duplicates the homepage. **Starting point is
  notably better than BRG's:** every page already has a title, meta description
  and schema, all 16 homepage images resolve, and the homepage schema is
  genuinely rich (`Organization`, `RealEstateAgent`, `Service`, `WebPage`, and
  two `Review` nodes). **Five real problems found:** `www` returns a hard
  **403** so an entire hostname is dead; **no canonical on any page** while
  `/home-750690` serves the homepage's content under a second URL with the same
  title; **every unknown URL 301s to the homepage**, which is the harmful
  variant of a soft 404; `robots.txt`, `sitemap.xml` and `llms.txt` all return
  **200 with zero bytes**; and there is **no `og:image` anywhere**. ⚠️ **Flagged
  for John, not acted on:** the two `Review` nodes in homepage schema are
  self-serving review markup, which Google has not surfaced as a rich result
  since 2019 and which is a manual-action risk if not genuine, with the FTC's
  2024 review rule also in play. **`CLAUDE.md` was deliberately seeded as a
  SKELETON** with most sections marked UNKNOWN: the offer, audience, pricing,
  brand kit and banned-language list are all unstated, and nothing was inferred
  or carried across from BizRevGrowth. Only PROCESS carried over (the playbook
  and four scripts, repointed and smoke-tested). **BRG finishes first** per
  John's stated priority; this repo is staged and waiting.
