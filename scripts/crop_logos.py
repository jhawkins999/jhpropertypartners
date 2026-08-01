#!/usr/bin/env python3
"""
Render the Growth-accent SVGs to PNG and trim the dead border.

Canon: the vendor's raw logo exports carry 49-69% baked-in padding, which is
what caused the header whitespace bug. qlmanage renders square, so it is worse.
This trims to the actual ink and writes a small transparent margin back.

    python3 scripts/crop_logos.py
"""

import glob
import os
import subprocess
import sys

from PIL import Image

SRC = 'logos/svg/growth-accent'
OUT = 'logos/growth-accent-upload'
TMP = '/tmp/brg_logo_render'
RENDER_PX = 2400
MARGIN_PCT = 0.02          # small breathing room, not the vendor's 50%


def render(svg, outdir):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(['qlmanage', '-t', '-s', str(RENDER_PX), '-o', outdir, svg],
                   capture_output=True)
    p = os.path.join(outdir, os.path.basename(svg) + '.png')
    return p if os.path.exists(p) else None


def trim(img):
    """Trim fully transparent border; fall back to white-background trim."""
    img = img.convert('RGBA')
    alpha = img.split()[-1]
    box = alpha.getbbox()
    if box and (box[2] - box[0]) < img.width * 0.98:
        return img.crop(box)
    # opaque render: trim near-white instead
    rgb = img.convert('RGB')
    bg = Image.new('RGB', rgb.size, (255, 255, 255))
    from PIL import ImageChops
    diff = ImageChops.difference(rgb, bg).convert('L').point(lambda v: 255 if v > 8 else 0)
    box = diff.getbbox()
    return img.crop(box) if box else img


def main():
    svgs = sorted(glob.glob(f'{SRC}/*DeepGreen.svg'))
    if not svgs:
        print(f"no DeepGreen SVGs in {SRC}", file=sys.stderr)
        return 1
    os.makedirs(OUT, exist_ok=True)
    for svg in svgs:
        raw = render(svg, TMP)
        if not raw:
            print(f"  RENDER FAILED  {svg}")
            continue
        im = trim(Image.open(raw))
        m = int(max(im.size) * MARGIN_PCT)
        canvas = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m), (0, 0, 0, 0))
        canvas.paste(im, (m, m), im)
        name = os.path.basename(svg).replace('_DeepGreen.svg', '.png')
        dest = os.path.join(OUT, name)
        canvas.save(dest)
        before = Image.open(raw).size
        print(f"  {name:52} {before[0]}x{before[1]} -> {canvas.width}x{canvas.height}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
