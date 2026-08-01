#!/usr/bin/env python3
"""
JH Property Partners production site audit.

Fetches the live pages as RAW HTML (never the rendered DOM) and reports the
state of every SEO field, plus any strings we decide must not appear.

    python3 scripts/audit_site.py           # full report
    python3 scripts/audit_site.py --fails   # only what is still broken

Notes
-----
* GHL resolves custom values into the HTML at PUBLISH time, and Cloudflare
  caches ~60s. Query strings do NOT bust that cache. If a fix looks missing,
  check `last-modified` and re-run a minute later.
* Every element appears TWICE in GHL raw HTML (once rendered, once in the page
  payload). A count of 2 usually means ONE thing to fix, not two.
* Colour greps must cover rgb()/rgba() as well as hex. A hex-only sweep on the
  previous project missed 18 instances, including a box-shadow.
"""

import argparse
import re
import sys
import urllib.request

BASE = "https://jhpropertypartners.com"

PAGES = {
    "home":         "/",
    "services":     "/services",
    "testimonials": "/testimonials",
    "contact":      "/contact",
    "privacy":      "/privacy-policy",
    "terms":        "/terms-and-conditions",
    "home-dupe":    "/home-750690",
}

# (label, page, needle, expected_count)
# EMPTY ON PURPOSE. Fill in once the brand kit and banned-language list exist.
# Do NOT copy BizRevGrowth's list here: different business, different rules.
CHECKS = []

# Plain substring sweeps: retired brand strings, retired colours.
SWEEPS = []

# Regex sweeps: put rgb()/rgba() colour forms here.
RE_SWEEPS = []

SEO_FIELDS = [
    ("title",     r"<title[^>]*>([^<]+)</title>"),
    ("desc",      r'<meta name="description"'),
    ("canonical", r'rel="canonical"'),
    ("schema",    r"application/ld\+json"),
    ("og:image",  r"og:image"),
    ("robots",    r'<meta name="robots"'),
]


def fetch(path):
    req = urllib.request.Request(
        BASE + path,
        headers={"User-Agent": "jhp-audit/1.0", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace"), dict(r.headers), r.status


def unescape(raw):
    return (raw.replace("\\u003C", "<").replace("\\u003E", ">")
               .replace("\\u002F", "/").replace('\\"', '"').replace("\\n", "\n"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fails", action="store_true", help="only show failures")
    args = ap.parse_args()

    docs, fails = {}, 0
    print("Fetching %s ...\n" % BASE)
    for name, path in PAGES.items():
        try:
            raw, hdr, status = fetch(path)
        except Exception as e:                                   # noqa: BLE001
            print("  %-13s ERROR %s" % (name, e))
            continue
        docs[name] = (unescape(raw).lower(), raw)
        print("  %-13s %s  %9s B  modified=%s" % (
            name, status, format(len(raw), ","), hdr.get("last-modified", "?")))

    print("\n" + "=" * 78)
    print("SEO FIELDS PER PAGE   (Y = present)")
    print("=" * 78)
    print("  %-13s" % "page" + "".join("%-11s" % f for f, _ in SEO_FIELDS))
    for name in docs:
        raw = docs[name][1]
        row = "  %-13s" % name
        for field, pat in SEO_FIELDS:
            m = re.search(pat, raw)
            ok = bool(m) and (not m.groups() or bool(m.group(1).strip()))
            if not ok:
                fails += 1
            row += "%-11s" % ("Y" if ok else "-")
        print(row)

    if CHECKS:
        print("\n" + "=" * 78)
        print("CHECKLIST  (expect 0)")
        print("=" * 78)
        for label, page, needle, expect in CHECKS:
            if page not in docs:
                continue
            n = docs[page][0].count(needle.lower())
            ok = (n == expect)
            if not ok:
                fails += 1
            if args.fails and ok:
                continue
            print("  %-4s %-13s %-30s %s" % ("PASS" if ok else "FAIL", page, label, n))

    if SWEEPS or RE_SWEEPS:
        print("\n" + "=" * 78)
        print("SWEEPS")
        print("=" * 78)
        for page in docs:
            parts = []
            for label, needle, expect in SWEEPS:
                n = docs[page][0].count(needle.lower())
                if n != expect:
                    fails += 1
                parts.append("%s=%d" % (label, n))
            for label, pat, expect in RE_SWEEPS:
                n = len(re.findall(pat, docs[page][0]))
                if n != expect:
                    fails += 1
                parts.append("%s=%d" % (label, n))
            print("  %-13s %s" % (page, "  ".join(parts)))

    print("\n" + "=" * 78)
    print("  %d check(s) failing" % fails)
    print("=" * 78 + "\n")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
