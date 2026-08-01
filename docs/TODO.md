# JH Property Partners TODO
Live next-session checklist. Checkboxes, not prose. Context lives in
`CLAUDE.md`; history in `docs/Session_Log.md`; process in
`docs/GHL_Site_Launch_Playbook.md`.

> ⚠️ **BizRevGrowth comes first** (John, 2026-08-01). This repo is seeded and
> ready, but the BRG site pass finishes before real work starts here.

---

## 🟡 PHASE 0 — QUESTIONS FOR JOHN (blocks almost everything else)

Nothing meaningful can be written until these are answered. **Do not infer
them.**

- [ ] **What is the offer, in your words?** Cash offer on what kind of property,
      in what condition, in what geography?
- [ ] **Who is the seller you want?** Probate, inherited, tired landlord,
      pre-foreclosure, relocation, something else?
- [ ] **What can we actually claim?** Close times, fees, "as-is", who pays what.
      Anything we put on the site has to be substantiable.
- [ ] **Are the testimonials real and attributable?** There is a `/testimonials`
      page AND two `Review` nodes in the homepage schema. See the warning in
      the baseline audit: self-serving review markup is a manual-action risk if
      it is not genuine, and the FTC's 2024 review rule applies here.
- [ ] **Is there a brand kit?** Colours, fonts, logo files.
- [ ] **Any banned language?** Carry over "no em dashes" and outcome-focused
      copy from the other projects, or start fresh?
- [ ] **What legal entity is behind this**, for schema, terms, and any A2P work?
- [ ] **Is SMS in play?** If yes, A2P registration becomes a critical path item.

## 🔴 QUICK WINS — verified broken, safe to fix without any of the above

- [ ] **`www.jhpropertypartners.com` returns 403.** A whole hostname is dead.
      GHL Settings > Domains had a one-click redirect fix on the last project.
- [ ] **`/home-750690` duplicates the homepage** (same content, same title, no
      canonical). Add canonicals site-wide pointing each page at itself.
- [ ] **Unknown URLs 301 to the homepage** = soft 404. Should 404/410 or land on
      a real error page. Decide which, then build it.
- [ ] **`robots.txt` is empty** (200, 0 bytes). Needs allow + Sitemap directive.
- [ ] **`sitemap.xml` is empty.** List the 6 real pages. Exclude `/home-750690`
      and any error page. Watch for a generated `/test_path?item=123`
      placeholder: that appeared on the last project and 301'd to the error page.
- [ ] **`llms.txt` is empty.** Write it once the offer is known, not before.
- [ ] **No `og:image` on any page.** Needs one brand image, then the tag on all 6.

## ⬜ PHASE 1 — audit before editing
- [ ] Run `python3 scripts/audit_site.py` and `scripts/sweep_dashes.py`
- [ ] Colour/font sweep: find the shared theme variables FIRST (they drove ~34
      usages on the last project), not element by element
- [ ] Check for desktop/mobile twins
- [ ] Status-check every image URL (homepage came back clean; other pages not
      yet checked)
- [ ] Confirm whether a custom 404 exists

## ⬜ PHASE 2 — copy
- [ ] Only after Phase 0 answers. Outcome-focused: what the SELLER gets, not
      what the process is.
- [ ] Verify every claim about price, speed and fees is substantiable.

## ⬜ LATER
- [ ] Per-page canonical, og:image, robots where needed
- [ ] Review the existing schema rather than replacing it: it is already richer
      than BRG's was (`RealEstateAgent`, `Service`)
- [ ] Decide on `LocalBusiness`/`RealEstateAgent` detail: service area, hours,
      phone, address

---

## ⛔ STANDING RULES
- **Never use GHL's "Ask AI"** for copy, legal text, or status. It fabricated
  both on the last project.
- **Verify on production, raw HTML, never the rendered DOM.**
- **Save and Publish are different buttons.**
- **BizRevGrowth canon does NOT govern this project.** Process carries over;
  content does not.
