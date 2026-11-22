#!/usr/bin/env python3
"""Render entry.png: 'THE WORLD IN ONE FRAME' — Saturday 21 November 2026.

Pure Pillow primitives only. No network, no randomness, no timestamps, so the
PNG is byte-identical on every run.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (243, 240, 232)
INK = (24, 24, 28)
GREY = (110, 108, 102)
RULE = (200, 196, 186)
CARD = (252, 251, 247)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FONT_DIR + "DejaVuSerif-Bold.ttf"
SANS = FONT_DIR + "DejaVuSans.ttf"
SANS_B = FONT_DIR + "DejaVuSans-Bold.ttf"

# Stories: (tag, tag_color, headline, body, icon_key)
STORIES = [
    (
        "STRAIT OF HORMUZ",
        (12, 92, 140),
        "Iran runs a tanker convoy",
        "More than 14 tankers wait at Kharg Island, crews and flags "
        "assigned, to test the US naval blockade; oil revenue is set to "
        "reach zero by mid-December.",
        "tanker",
    ),
    (
        "THE HAGUE",
        (96, 44, 120),
        "ICJ: Myanmar guilty of genocide",
        "For the first time a court holds a state responsible for genocide "
        "against the Rohingya, and orders Myanmar to investigate.",
        "court",
    ),
    (
        "LUBLIN, POLAND",
        (172, 44, 44),
        "Russian missile lands in Poland",
        "An X-101 missile fell in a village in Lublin Voivodeship; the "
        "defence minister said nobody was injured.",
        "missile",
    ),
    (
        "WASHINGTON",
        (30, 112, 72),
        "Trump puts Iran strikes on hold",
        "The president said he is in no rush and will take up new strikes "
        "after the New Year; Israel keeps pressing for action.",
        "calendar",
    ),
]


def wrap(draw, text, font, maxw):
    """Greedy word-wrap measured with draw.textlength so nothing overflows."""
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        trial = w if not cur else cur + " " + w
        if draw.textlength(trial, font=font) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_w(draw, s, font):
    return draw.textlength(s, font=font)


def draw_icon(draw, key, x, y, s, color):
    """Small drawn icon of size s x s with top-left at (x, y)."""
    if key == "tanker":
        # blockade line (dashed) across the middle
        wl = y + s * 0.55
        for i in range(0, int(s), 10):
            draw.line([(x + i, wl), (x + min(i + 6, s), wl)], fill=color, width=2)
        # hull
        hull = [(x + s * 0.18, wl - 2), (x + s * 0.82, wl - 2),
                (x + s * 0.70, y + s * 0.34), (x + s * 0.30, y + s * 0.34)]
        draw.polygon(hull, fill=color)
        # deckhouse
        draw.rectangle([x + s * 0.40, y + s * 0.18, x + s * 0.60, y + s * 0.34],
                       fill=color)
        # mast
        draw.line([(x + s * 0.50, y + s * 0.06), (x + s * 0.50, y + s * 0.18)],
                  fill=color, width=2)
    elif key == "court":
        # roof
        draw.polygon([(x + s * 0.10, y + s * 0.34), (x + s * 0.90, y + s * 0.34),
                      (x + s * 0.50, y + s * 0.12)], fill=color)
        # columns
        for cx in (0.20, 0.42, 0.58, 0.80):
            draw.rectangle([x + s * (cx - 0.04), y + s * 0.36,
                            x + s * (cx + 0.04), y + s * 0.74], fill=color)
        # base
        draw.rectangle([x + s * 0.10, y + s * 0.76, x + s * 0.90, y + s * 0.84],
                       fill=color)
        # scales: post + beam + two pans
        draw.line([(x + s * 0.50, y + s * 0.20), (x + s * 0.50, y + s * 0.33)],
                  fill=color, width=2)
        draw.line([(x + s * 0.38, y + s * 0.23), (x + s * 0.62, y + s * 0.23)],
                  fill=color, width=2)
    elif key == "missile":
        # diagonal trail from top-left toward impact
        ix, iy = x + s * 0.70, y + s * 0.66
        draw.line([(x + s * 0.12, y + s * 0.14), (ix, iy)], fill=color, width=3)
        # impact burst
        import math
        for a in range(0, 360, 45):
            r = s * 0.16
            dx = math.cos(math.radians(a)) * r
            dy = math.sin(math.radians(a)) * r
            draw.line([(ix, iy), (ix + dx, iy + dy)], fill=color, width=2)
        draw.ellipse([ix - 3, iy - 3, ix + 3, iy + 3], fill=color)
    elif key == "calendar":
        # body
        draw.rounded_rectangle([x + s * 0.16, y + s * 0.16, x + s * 0.84, y + s * 0.86],
                               radius=6, fill=color)
        # header band
        draw.rectangle([x + s * 0.16, y + s * 0.16, x + s * 0.84, y + s * 0.34],
                       fill=(255, 255, 255))
        # binding rings
        draw.line([(x + s * 0.34, y + s * 0.08), (x + s * 0.34, y + s * 0.22)],
                  fill=color, width=3)
        draw.line([(x + s * 0.66, y + s * 0.08), (x + s * 0.66, y + s * 0.22)],
                  fill=color, width=3)
        # pause sign (two bars)
        draw.rectangle([x + s * 0.40, y + s * 0.44, x + s * 0.47, y + s * 0.72],
                       fill=(255, 255, 255))
        draw.rectangle([x + s * 0.53, y + s * 0.44, x + s * 0.60, y + s * 0.72],
                       fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    f_title = ImageFont.truetype(SERIF_B, 54)
    f_date = ImageFont.truetype(SANS_B, 24)
    title = "THE WORLD IN ONE FRAME"
    tw = text_w(d, title, f_title)
    d.text(((W - tw) / 2, 34), title, font=f_title, fill=INK)

    date = "SATURDAY 21 NOVEMBER 2026"
    dw = text_w(d, date, f_date)
    d.text(((W - dw) / 2, 102), date, font=f_date, fill=GREY)

    # rules around date
    d.line([(60, 116), (W - 60, 116)], fill=INK, width=2)

    # ---- grid geometry ----
    MARGIN = 40
    GAP = 24
    TOP = 140
    BOT = H - MARGIN
    cols, rows = 2, 2
    cw = (W - 2 * MARGIN - (cols - 1) * GAP) // cols
    ch = (BOT - TOP - (rows - 1) * GAP) // rows

    f_tag = ImageFont.truetype(SANS_B, 19)
    f_head = ImageFont.truetype(SERIF_B, 28)
    f_body = ImageFont.truetype(SANS, 19)

    PAD = 22
    inner_w = cw - 2 * PAD

    for idx, (tag, tcol, head, body, icon) in enumerate(STORIES):
        r, c = divmod(idx, cols)
        px = MARGIN + c * (cw + GAP)
        py = TOP + r * (ch + GAP)

        # card + colored top bar
        d.rectangle([px, py, px + cw, py + ch], fill=CARD, outline=RULE, width=2)
        d.rectangle([px, py, px + cw, py + 6], fill=tcol)

        cx = px + PAD
        cy = py + PAD + 6

        # tag
        d.text((cx, cy), tag, font=f_tag, fill=tcol)
        cy += 26

        # headline (wrap to inner_w)
        hlines = wrap(d, head, f_head, inner_w)
        for ln in hlines:
            d.text((cx, cy), ln, font=f_head, fill=INK)
            cy += 34
        cy += 6

        # body
        blines = wrap(d, body, f_body, inner_w)
        for ln in blines:
            d.text((cx, cy), ln, font=f_body, fill=(55, 55, 60))
            cy += 24

        # icon bottom-right of the card
        isz = 74
        ix = px + cw - PAD - isz
        iy = py + ch - PAD - isz
        draw_icon(d, icon, ix, iy, isz, tcol)

    img.save("entry.png", "PNG")


if __name__ == "__main__":
    main()