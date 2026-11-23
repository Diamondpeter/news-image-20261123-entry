#!/usr/bin/env python3
"""Draw THE NEWS NETWORK: Monday 23 November 2026 as a metro map.

Five coloured lines (one per theme), twenty-five stations (one per story),
on a clean white page. Pure Pillow, no network, deterministic output.
Run:  python3 generate.py   -> writes entry.png beside this file.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
WHITE = (255, 255, 255)
INK = (17, 17, 17)
GREY = (110, 110, 110)
FAINT = (237, 237, 237)
RULE = (200, 200, 200)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# (colour, label, [(headline, caption), ...]) — 5 stations per line.
LINES = [
    ((198, 40, 40), "CLIMATE & PLANET", [
        ("COP31 COLLAPSES",
         "Antalya talks end with no deal — the longest climate summit ever breaks over two words: fossil fuels."),
        ("EU WALKS AWAY",
         "Brussels refuses to endorse a pact that never names fossil fuels, the key driver of warming."),
        ("MERCURY, REACHED",
         "Europe and Japan's BepiColombo spacecraft arrives at the smallest planet."),
        ("TANKERS HIT",
         "Projectiles strike two oil tankers in the Strait of Hormuz as regional tensions simmer."),
        ("DELHI'S AIR",
         "Authorities publish a report card on pollution measures across Delhi and its neighbours."),
    ]),
    ((23, 69, 110), "CONFLICT & SECURITY", [
        ("KYIV REGION HIT",
         "A Russian drone strike on a building leaves at least 14 people missing, Kyiv says."),
        ("SHIP ABLAZE",
         "A Russian cargo ship keeps burning off Finland after an attack at sea."),
        ("IRAN STRIKES",
         "Bahrain says a civilian industrial facility was struck by Iran."),
        ("KILLER-ROBOT TALKS",
         "Nations agree to keep negotiating rules for lethal AI weapons at the United Nations."),
        ("FBI INCIDENT",
         "America's intelligence chief confirms a Sunday incident at the FBI and urges upgrades."),
    ]),
    ((211, 84, 0), "POLITICS & POWER", [
        ("TRUMP CALLS KIM",
         "The US president tried to reach Kim Jong Un — and was ignored, reports say."),
        ("PENTAGON COOLS",
         "Washington limits military ties with Canada as relations strain."),
        ("ISRAEL TALKS RESUME",
         "Eisenkot's party restarts coalition talks; a minister calls settler violence 'Jewish terrorism'."),
        ("NEPAL'S NEW PM",
         "Balen Shah begins his first visit to India and sits down with Modi."),
        ("BORDER COOLED",
         "Indian and Chinese commanders meet in Arunachal to ease tensions."),
    ]),
    ((46, 125, 50), "MONEY & MARKETS", [
        ("BIG TECH TAX",
         "The EU proposes a levy on tech giants in its draft budget."),
        ("CHINA HITS BACK",
         "Beijing denounces the US ban on telecom companies."),
        ("CHIP TRAIL",
         "Fresh details link an Nvidia figure to a network diverting AI chips to China."),
        ("NIGERIA'S RATE CALL",
         "The central bank opens its two-day monetary policy meeting."),
        ("LISBON MARCHES",
         "Thousands take to the streets as the cost of living fuels anger."),
    ]),
    ((106, 63, 160), "SPORT, CULTURE & LIFE", [
        ("INDIA'S 720",
         "A record 720 for 9 declared in Wellington, with Rishabh Pant hitting 128."),
        ("PAKISTAN A WIN",
         "Tilak Varma's century is in vain as India A lose the Rising Stars Asia Cup clash."),
        ("GRAMMY CALL",
         "Six Nigerian stars — Davido, Burna Boy, Wizkid, Tems, Ayra Starr and Asake — are nominated."),
        ("KLOPP v FIFA",
         "Germany's manager calls Infantino's reign a regression for world football."),
        ("MEASLES TOLL RISES",
         "Deaths in Bangladesh's measles outbreak pass 1,350."),
    ]),
]

STATION_X = [131, 321, 511, 701, 891]  # column centres across 36..988
BAND_TOPS = [152, 310, 468, 626, 784]  # 158px bands
BAND_H = 158


def line_y_at(path, x):
    """Y of a polyline at a given x (piecewise linear)."""
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        if x1 <= x <= x2:
            if x2 == x1:
                return y1
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return path[-1][1]


def draw_text_block(draw, cx, top, headline, caption, max_w, colour):
    """Headline (bold, coloured) + caption (regular, ink), centred on cx."""
    f_head = font(FONTB, 14)
    f_cap = font(FONT, 11)
    y = top
    for ln in wrap(draw, headline, f_head, max_w):
        draw.text((cx - draw.textlength(ln, font=f_head) / 2, y),
                  ln, font=f_head, fill=colour)
        y += 17
    y += 2
    for ln in wrap(draw, caption, f_cap, max_w):
        draw.text((cx - draw.textlength(ln, font=f_cap) / 2, y),
                  ln, font=f_cap, fill=INK)
        y += 13
    return y


def draw():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    f_title = font(FONTB, 52)
    d.text((36, 26), "THE NEWS NETWORK", font=f_title, fill=INK)
    f_date = font(FONTB, 19)
    date = "MONDAY 23 NOVEMBER 2026"
    d.text((988 - d.textlength(date, font=f_date), 34), date,
           font=f_date, fill=INK)
    f_sub = font(FONT, 13)
    sub = "25 STORIES  ·  ONE DAY  ·  ONE MAP"
    d.text((988 - d.textlength(sub, font=f_sub), 60), sub,
           font=f_sub, fill=GREY)
    d.line([(36, 108), (988, 108)], fill=INK, width=2)

    # ---- Legend ---------------------------------------------------------
    f_leg = font(FONTB, 11)
    x = 36
    for i, (colour, label, _stories) in enumerate(LINES, start=1):
        d.rectangle([x, 121, x + 13, 134], fill=colour)
        txt = "%d · %s" % (i, label)
        d.text((x + 19, 120), txt, font=f_leg, fill=INK)
        x += 19 + d.textlength(txt, font=f_leg) + 14

    # ---- Faint column separators ---------------------------------------
    for i in range(1, 5):
        gx = 36 + i * 190
        d.line([(gx, 150), (gx, 944)], fill=FAINT, width=1)

    # ---- The five lines -------------------------------------------------
    for li, (colour, label, stories) in enumerate(LINES):
        top = BAND_TOPS[li]
        below = (li % 2 == 0)  # lines 1, 3, 5: line high, text below
        cy = top + 26 if below else top + 132
        dj = -10 if below else 10
        path = [(58, cy), (300, cy), (350, cy + dj),
                (690, cy + dj), (740, cy), (988, cy)]
        d.line(path, fill=colour, width=9, joint="curve")

        # Terminus badge: line number in a filled circle at the left end.
        d.ellipse([30, cy - 16, 62, cy + 16], fill=colour)
        num = str(li + 1)
        f_num = font(FONTB, 16)
        d.text((46 - d.textlength(num, font=f_num) / 2, cy - 11),
               num, font=f_num, fill=WHITE)
        d.ellipse([978, cy - 5, 988, cy + 5], fill=colour)

        for si, (headline, caption) in enumerate(stories):
            sx = STATION_X[si]
            sy = line_y_at(path, sx)
            lead = (li == 0 and si == 0)
            r = 18 if lead else 14
            d.ellipse([sx - r, sy - r, sx + r, sy + r],
                      fill=WHITE, outline=colour, width=5 if lead else 4)
            n = str(li * 5 + si + 1)
            f_station = font(FONTB, 14 if lead else 13)
            d.text((sx - d.textlength(n, font=f_station) / 2,
                    sy - 10 if lead else sy - 9),
                   n, font=f_station, fill=colour)
            # Text block: below the line, or above it for even lines.
            if below:
                draw_text_block(d, sx, top + 54, headline, caption,
                                178, colour)
            else:
                # Measure the block, then draw it ending just above the line.
                f_head = font(FONTB, 14)
                f_cap = font(FONT, 11)
                head_lines = wrap(d, headline, f_head, 178)
                cap_lines = wrap(d, caption, f_cap, 178)
                block_h = len(head_lines) * 17 + 2 + len(cap_lines) * 13
                draw_text_block(d, sx, top + 104 - block_h,
                                headline, caption, 178, colour)

    # ---- Footer ---------------------------------------------------------
    d.line([(36, 952), (988, 952)], fill=RULE, width=1)
    f_foot = font(FONT, 11)
    foot = ("Every story above happened, or was first reported, on Monday "
            "23 November 2026  ·  Compiled from the day's reporting  ·  "
            "make.fun entry news-image-20261123")
    d.text((512 - d.textlength(foot, font=f_foot) / 2, 962),
           foot, font=f_foot, fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    print("wrote %s (%d bytes)" % (OUT, os.path.getsize(OUT)))


if __name__ == "__main__":
    draw()
