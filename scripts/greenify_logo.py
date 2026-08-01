#!/usr/bin/env python3
"""
Recolour the "Growth" half of the BizRevGrowth wordmark.

The wordmark is a SINGLE <path> whose `d` holds one subpath per letter (plus
counters), sitting inside a parent <g fill="#041442">. To colour only "Growth"
we split that path in two: "BizRev" keeps the inherited navy, "Growth" gets an
explicit fill.

"Growth" = G, r, o(+counter), w, t(+crossbar), h = the LAST 8 subpaths when
sorted left to right. That count is stable across all six logo variants.

    python3 scripts/greenify_logo.py <hex> <suffix>
    python3 scripts/greenify_logo.py '#1d8a4a' DeepGreen
"""

import re
import sys
import os

SRC_DIR = 'logos/svg'
OUT_DIR = 'logos/svg/growth-accent'
GROWTH_SUBPATHS = 8          # G r o(+counter) w t(+crossbar) h
EXPECTED_SUBPATHS = 18       # full "BizRevGrowth"


def subpaths_with_x(d):
    """Split d on M/m, return [(min_x, chunk), ...] tracking the pen for relative moves."""
    parts = [p for p in re.split(r'(?=[Mm])', d) if p.strip()]
    out, cx, cy = [], 0.0, 0.0
    for part in parts:
        nums = [float(x) for x in re.findall(r'-?\d*\.?\d+(?:e-?\d+)?', part)]
        if not nums:
            continue
        rel = part[0] == 'm'
        xs, x, y = [], cx, cy
        for i in range(0, len(nums) - 1, 2):
            if rel:
                x += nums[i]; y += nums[i + 1]
            else:
                x, y = nums[i], nums[i + 1]
            xs.append(x)
        if xs:
            out.append((min(xs), part))
            cx, cy = xs[-1], y
    return out


def process(path, green, suffix):
    s = open(path, encoding='utf-8').read()
    paths = list(re.finditer(r'<path([^>]*?)d="([^"]+)"([^>]*?)>', s))

    target = None
    for m in paths:
        subs = subpaths_with_x(m.group(2))
        if len(subs) == EXPECTED_SUBPATHS:
            target = (m, subs)
            break
    if not target:
        counts = [len(subpaths_with_x(m.group(2))) for m in paths]
        return f"SKIP {os.path.basename(path)} (no {EXPECTED_SUBPATHS}-subpath wordmark; found {counts})"

    m, subs = target
    ordered = sorted(subs, key=lambda z: z[0])
    growth = {id(c) for _, c in ordered[-GROWTH_SUBPATHS:]}

    biz_d = ''.join(c for _, c in subs if id(c) not in growth)
    gro_d = ''.join(c for _, c in subs if id(c) in growth)

    pre, post = m.group(1), m.group(3)
    replacement = (f'<path{pre}d="{biz_d}"{post}>'
                   f'</path>'
                   f'<path{pre}d="{gro_d}" fill="{green}"{post}>')
    s = s[:m.start()] + replacement + s[m.end():]

    os.makedirs(OUT_DIR, exist_ok=True)
    base = os.path.basename(path).replace('.svg', f'_{suffix}.svg')
    out = os.path.join(OUT_DIR, base)
    open(out, 'w', encoding='utf-8').write(s)
    biz = EXPECTED_SUBPATHS - GROWTH_SUBPATHS
    return f"OK   {base}  (BizRev={biz} subpaths, Growth={GROWTH_SUBPATHS}, fill={green})"


def main():
    green = sys.argv[1] if len(sys.argv) > 1 else '#1d8a4a'
    suffix = sys.argv[2] if len(sys.argv) > 2 else 'GreenGrowth'
    files = sorted(f for f in os.listdir(SRC_DIR) if f.endswith('.svg'))
    for f in files:
        print(process(os.path.join(SRC_DIR, f), green, suffix))


if __name__ == '__main__':
    main()
