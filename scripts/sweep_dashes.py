import re, html, urllib.request

PAGES = [("home", "/"), ("services", "/services"), ("testimonials", "/testimonials"),
         ("contact", "/contact"), ("privacy", "/privacy-policy"),
         ("terms", "/terms-and-conditions")]

DASH = re.compile(r'[–—]')  # en dash, em dash


def fetch(p):
    r = urllib.request.Request("https://jhpropertypartners.com" + p,
                               headers={"User-Agent": "jhp-sweep"})
    return urllib.request.urlopen(r, timeout=45).read().decode("utf-8", "replace")


def visible_text(raw):
    """Rendered DOM only, tags stripped, entities resolved."""
    cut = raw.find('<script type="application/json"')
    if cut < 0:
        cut = raw.find('window.__NUXT__')
    dom = raw[:cut] if cut > 0 else raw
    dom = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', dom, flags=re.S)
    dom = re.sub(r'<(h[1-6]|p|li|div|section|span|a|td|summary)\b[^>]*>', r'\n<\1>', dom)
    dom = re.sub(r'<[^>]+>', ' ', dom)
    out = []
    for ln in dom.split('\n'):
        s = ' '.join(html.unescape(ln).split())
        if len(s) > 2:
            out.append(s)
    return out


total = 0
for name, path in PAGES:
    raw = fetch(path)
    lines = visible_text(raw)
    hits, seen = [], set()
    for s in lines:
        if DASH.search(s):
            k = s.lower()[:80]
            if k in seen:
                continue
            seen.add(k)
            hits.append(s)
    # entity form inside custom-code blocks (renders as a dash)
    ent = len(re.findall(r'&#8212;|&mdash;|&#8211;|&ndash;', raw))
    print(f"\n{'=' * 78}\n{name.upper()}  ({len(hits)} visible lines with a dash"
          f" | {ent} entity refs in source)\n{'=' * 78}")
    for h in hits:
        total += 1
        print(f"  - {h[:260]}")

print(f"\n\n>>> {total} distinct visible lines carrying an em/en dash <<<")
