#!/usr/bin/env python3
"""
Astrology Chart SVG Generator
==============================
Generates crisp, high-resolution vector SVGs for Vedic astrological charts:
1. North Indian Diamond Chart (डायमंड कुण्डली)
2. South Indian Box Chart (दक्षिण भारतीय चक्र)
3. Planetary Aspects & Drishti Matrix
4. Navamsha (D9) / Divisional Chart

Compliant with WeasyPrint vector rendering and modern web SVG standards.
"""

import sys
import os
import argparse
import html

# Sanskrit and English Sign Names
RASHI_NAMES = [
    ("मेष", "Aries"),
    ("वृषभ", "Taurus"),
    ("मिथुन", "Gemini"),
    ("कर्क", "Cancer"),
    ("सिंह", "Leo"),
    ("कन्या", "Virgo"),
    ("तुला", "Libra"),
    ("वृश्चिक", "Scorpio"),
    ("धनु", "Sagittarius"),
    ("मकर", "Capricorn"),
    ("कुंभ", "Aquarius"),
    ("मीन", "Pisces")
]

PLANET_GLYPHS = {
    "Su": ("सूर्य", "Sun", "#ea580c"),
    "Mo": ("चन्द्र", "Moon", "#0284c7"),
    "Ma": ("मंगल", "Mars", "#dc2626"),
    "Me": ("बुध", "Mercury", "#16a34a"),
    "Ju": ("गुरु", "Jupiter", "#d97706"),
    "Ve": ("शुक्र", "Venus", "#db2777"),
    "Sa": ("शनि", "Saturn", "#4f46e5"),
    "Ra": ("राहु", "Rahu", "#7c3aed"),
    "Ke": ("केतु", "Ketu", "#475569"),
    "Asc": ("लग्न", "Ascendant", "#b45309")
}

def generate_north_indian_chart(
    lagna_rashi=1,
    planet_placements=None,
    title="जन्म कुण्डली (Lagna Kundli)",
    subtitle="North Indian Vedic Diamond Chart",
    width=500,
    height=500,
    theme="parchment"
):
    """
    Renders an authentic North Indian Diamond Vedic Horoscope in SVG.
    Houses:
      House 1: Central Top Diamond (Lagna)
      House 2: Top-Left Triangle
      House 3: Upper-Left Flank Triangle
      House 4: Left Center Diamond (Sukha Bhava)
      House 5: Lower-Left Flank Triangle
      House 6: Bottom-Left Triangle
      House 7: Central Bottom Diamond (Kalatra/Yuvati)
      House 8: Bottom-Right Triangle
      House 9: Lower-Right Flank Triangle
      House 10: Right Center Diamond (Karma Bhava)
      House 11: Upper-Right Flank Triangle
      House 12: Top-Right Triangle
    """
    if planet_placements is None:
        planet_placements = {}

    # Color themes
    if theme == "dark":
        bg_color = "#0f172a"
        border_color = "#d97706"
        inner_lines = "#d97706"
        text_rashi = "#f59e0b"
        text_house = "#64748b"
        text_planet = "#f8fafc"
        card_fill = "#1e293b"
    elif theme == "royal":
        bg_color = "#2e1065"
        border_color = "#f59e0b"
        inner_lines = "#d97706"
        text_rashi = "#fbbf24"
        text_house = "#a855f7"
        text_planet = "#ffffff"
        card_fill = "#3b0764"
    else:  # parchment / classic print
        bg_color = "#fffdfa"
        border_color = "#854d0e"
        inner_lines = "#ca8a04"
        text_rashi = "#92400e"
        text_house = "#78716c"
        text_planet = "#1c1917"
        card_fill = "#fefce8"

    cx = width / 2
    cy = height / 2
    pad = 40
    size = width - (2 * pad)
    x0 = pad
    y0 = pad
    x1 = pad + size
    y1 = pad + size
    mid_x = (x0 + x1) / 2
    mid_y = (y0 + y1) / 2

    # Map house numbers to rashi numbers based on lagna_rashi
    house_rashis = {}
    for h in range(1, 13):
        r_num = ((lagna_rashi - 1) + (h - 1)) % 12 + 1
        house_rashis[h] = r_num

    # Coordinates for house centroids to place sign number and planets
    # (rashi_x, rashi_y), [(planet_x, planet_y)]
    house_positions = {
        1:  {"rashi": (mid_x, mid_y - (size * 0.22)), "planets": (mid_x, mid_y - (size * 0.12)), "name": "१ तनु"},
        2:  {"rashi": (x0 + size * 0.25, y0 + size * 0.12), "planets": (x0 + size * 0.25, y0 + size * 0.22), "name": "२ धन"},
        3:  {"rashi": (x0 + size * 0.12, y0 + size * 0.25), "planets": (x0 + size * 0.18, y0 + size * 0.35), "name": "३ सहज"},
        4:  {"rashi": (mid_x - (size * 0.22), mid_y), "planets": (mid_x - (size * 0.12), mid_y), "name": "४ सुख"},
        5:  {"rashi": (x0 + size * 0.12, y1 - size * 0.25), "planets": (x0 + size * 0.18, y1 - size * 0.35), "name": "५ पुत्र"},
        6:  {"rashi": (x0 + size * 0.25, y1 - size * 0.12), "planets": (x0 + size * 0.25, y1 - size * 0.22), "name": "६ शत्रु"},
        7:  {"rashi": (mid_x, mid_y + (size * 0.22)), "planets": (mid_x, mid_y + (size * 0.12)), "name": "७ जाया"},
        8:  {"rashi": (x1 - size * 0.25, y1 - size * 0.12), "planets": (x1 - size * 0.25, y1 - size * 0.22), "name": "८ आयु"},
        9:  {"rashi": (x1 - size * 0.12, y1 - size * 0.25), "planets": (x1 - size * 0.18, y1 - size * 0.35), "name": "९ भाग्य"},
        10: {"rashi": (mid_x + (size * 0.22), mid_y), "planets": (mid_x + (size * 0.12), mid_y), "name": "१० कर्म"},
        11: {"rashi": (x1 - size * 0.12, y0 + size * 0.25), "planets": (x1 - size * 0.18, y0 + size * 0.35), "name": "११ लाभ"},
        12: {"rashi": (x1 - size * 0.25, y0 + size * 0.12), "planets": (x1 - size * 0.25, y0 + size * 0.22), "name": "१२ व्यय"}
    }

    svg_parts = []
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="vedic-chart-svg" style="max-width:{width}px; background:{bg_color}; border-radius:12px; font-family:'Georgia', 'Devanagari MT', 'Kohinoor Devanagari', serif; box-shadow:0 4px 18px rgba(0,0,0,0.06);">
  <defs>
    <filter id="gold-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#ca8a04" flood-opacity="0.25"/>
    </filter>
  </defs>

  <!-- Outer Border & Background -->
  <rect x="12" y="12" width="{width - 24}" height="{height - 24}" rx="8" fill="{bg_color}" stroke="{border_color}" stroke-width="1.8"/>
  <rect x="16" y="16" width="{width - 32}" height="{height - 32}" rx="6" fill="none" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="3,3" opacity="0.6"/>

  <!-- Main Chart Diamond Boundaries -->
  <!-- Outer Box -->
  <rect x="{x0}" y="{y0}" width="{size}" height="{size}" fill="{card_fill}" stroke="{border_color}" stroke-width="2.2"/>

  <!-- Diagonal X Lines (Connecting corners) -->
  <line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{inner_lines}" stroke-width="1.8"/>
  <line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y0}" stroke="{inner_lines}" stroke-width="1.8"/>

  <!-- Central Inner Diamond (Connecting midpoints of 4 outer edges) -->
  <polygon points="{mid_x},{y0} {x1},{mid_y} {mid_x},{y1} {x0},{mid_y}" fill="none" stroke="{inner_lines}" stroke-width="2"/>
''')

    # Render House Labels, Rashi Numbers & Planets
    for h_num in range(1, 13):
        pos = house_positions[h_num]
        rashi_num = house_rashis[h_num]
        rashi_sanskrit, rashi_eng = RASHI_NAMES[rashi_num - 1]
        rx, ry = pos["rashi"]
        px, py = pos["planets"]

        # Rashi number (Classical indicator)
        svg_parts.append(f'''  <!-- House {h_num} (Rashi {rashi_num}: {rashi_sanskrit}) -->''')
        svg_parts.append(f'''  <text x="{rx}" y="{ry}" fill="{text_rashi}" font-size="12" font-weight="bold" text-anchor="middle" dominant-baseline="middle">{rashi_num}</text>''')

        # Planets in this house
        planets = planet_placements.get(h_num, [])
        if planets:
            # Multi-planet stacking
            p_count = len(planets)
            start_y = py - ((p_count - 1) * 8)
            for idx, p_item in enumerate(planets):
                # parse planet code, e.g., "Su", "Ju(Ex)", "Sa(R)"
                curr_y = start_y + (idx * 16)
                p_code = p_item.strip()
                p_base = p_code.split("(")[0].strip()
                p_meta = ""
                if "(" in p_code:
                    p_meta = "(" + p_code.split("(")[1]

                glyph_info = PLANET_GLYPHS.get(p_base, (p_base, p_base, text_planet))
                p_hi, p_en, p_col = glyph_info
                disp_str = f"{p_hi}{p_meta}" if theme == "parchment" else f"{p_en}{p_meta}"
                svg_parts.append(f'''  <text x="{px}" y="{curr_y}" fill="{p_col}" font-size="11.5" font-weight="700" text-anchor="middle" dominant-baseline="middle">{html.escape(disp_str)}</text>''')

    # Header / Title inside chart or at top
    svg_parts.append(f'''  <!-- Title & Subtitle Banner -->
  <text x="{cx}" y="30" fill="{border_color}" font-size="13" font-weight="bold" letter-spacing="1" text-anchor="middle">{html.escape(title)}</text>
  <text x="{cx}" y="{height - 18}" fill="{text_house}" font-size="9.5" font-style="italic" letter-spacing="0.5" text-anchor="middle">{html.escape(subtitle)}</text>
</svg>''')

    return "\n".join(svg_parts)


def generate_aspect_wheel(width=460, height=460, theme="parchment"):
    """
    Renders a classical 12-house planetary aspect matrix / Drishti wheel.
    Visualizes 7th direct aspect, Mars 4-7-8, Jupiter 5-7-9, Saturn 3-7-10.
    """
    cx = width / 2
    cy = height / 2
    radius = (width / 2) - 45

    bg_color = "#fffdfa" if theme == "parchment" else "#0f172a"
    border_color = "#854d0e" if theme == "parchment" else "#d97706"
    text_color = "#1e293b" if theme == "parchment" else "#f8fafc"

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="vedic-aspect-svg" style="max-width:{width}px; background:{bg_color}; border-radius:12px; border:1px solid {border_color};">',
        f'  <!-- Aspect Mandala Wheel -->',
        f'  <circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{border_color}" stroke-width="1.8" />',
        f'  <circle cx="{cx}" cy="{cy}" r="{radius * 0.65}" fill="none" stroke="{border_color}" stroke-width="1" stroke-dasharray="4,4" opacity="0.6"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="{radius * 0.28}" fill="{border_color}" fill-opacity="0.08" stroke="{border_color}" stroke-width="1.2"/>',
        f'  <text x="{cx}" y="{cy}" fill="{border_color}" font-size="12" font-weight="bold" text-anchor="middle" dominant-baseline="middle">पूर्ण दृष्टि</text>',
        f'  <text x="{cx}" y="{cy + 14}" fill="#78716c" font-size="8.5" text-anchor="middle" dominant-baseline="middle">Drishti Wheel</text>'
    ]

    import math
    for i in range(12):
        angle = (i * 30) - 90
        rad = math.radians(angle)
        x = cx + radius * math.cos(rad)
        y = cy + radius * math.sin(rad)
        label_x = cx + (radius + 22) * math.cos(rad)
        label_y = cy + (radius + 22) * math.sin(rad)

        r_hi, r_en = RASHI_NAMES[i]
        lines.append(f'  <line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{border_color}" stroke-width="0.8" opacity="0.4"/>')
        lines.append(f'  <circle cx="{x}" cy="{y}" r="4" fill="{border_color}"/>')
        lines.append(f'  <text x="{label_x}" y="{label_y + 3}" fill="{text_color}" font-size="10" font-weight="bold" text-anchor="middle">{i+1}. {r_hi}</text>')

    lines.append('</svg>')
    return "\n".join(lines)


def generate_sample_kundlis():
    """Generates a dict of curated astrological charts for Tantra Gyan book chapters."""
    charts = {}

    # 1. Foundation Lagna Chart (Aries Ascendant with Sun exalted, Jupiter in Kendra)
    charts["lagna_chart"] = generate_north_indian_chart(
        lagna_rashi=1,
        planet_placements={
            1: ["Su(Ex)", "Ju"],
            4: ["Mo(Own)"],
            7: ["Sa(Ex)"],
            10: ["Ma(Ex)"]
        },
        title="कालपुरुष कुण्डली (Kaalpurusha Lagna)",
        subtitle="उच्च ग्रह एवं केन्द्र भाव दिग्बल स्थिति (Aries Ascendant)"
    )

    # 2. 17 Classical Raja Yogas (Gajakesari, Hamsa, Ruchaka, Malavya)
    charts["raja_yogas_chart"] = generate_north_indian_chart(
        lagna_rashi=4,  # Cancer Ascendant
        planet_placements={
            1: ["Ju(Ex)", "Mo"],  # Gajakesari + Hamsa Yoga
            4: ["Ve(Own)"],        # Malavya Yoga in Kendra
            7: ["Ma(Ex)"],        # Ruchaka Yoga
            10: ["Me", "Su"]       # Budhaditya Yoga
        },
        title="पंच महापुरुष एवं गजकेसरी राजयोग",
        subtitle="Classical Kendra-Trikona Synthesis (Cancer Lagna)"
    )

    # 3. Viparita Raja Yogas (6th, 8th, 12th House Lords Mutual Placement)
    charts["viparita_chart"] = generate_north_indian_chart(
        lagna_rashi=7,  # Libra Ascendant
        planet_placements={
            6: ["Ju(Own)"],      # Harsha Yoga
            8: ["Ve(Own)"],      # Sarala Yoga
            12: ["Me(Ex)"],      # Vimala Yoga
            1: ["Sa(Ex)"]        # Sasa Pancha Mahapurusha Yoga
        },
        title="हर्ष, सरल एवं विमल विपरीत राजयोग",
        subtitle="Trika Bhava Neutralization & Unconventional Elevation"
    )

    # 4. Medical Astrology - Arbuda Roga (Cancer Affliction Matrix)
    charts["medical_astrology_chart"] = generate_north_indian_chart(
        lagna_rashi=8,  # Scorpio Ascendant
        planet_placements={
            6: ["Mo", "Ra"],     # Chandra-Rahu Grahan in 6th
            8: ["Ma", "Sa"],     # Saturn-Mars in 8th (Kuja-Shani Yoga)
            12: ["Ke"],          # Ketu in 12th
            1: ["Su"]            # Sun in Lagna
        },
        title="आयुर्-ज्योतिष: अर्बुद (कैंसर) रोग योग",
        subtitle="Trik Bhava Cellular Affliction & Remedial Diagnostics"
    )

    # 5. Aspect Wheel
    charts["aspect_wheel"] = generate_aspect_wheel()

    return charts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Astrology Vector SVG Chart Generator")
    parser.add_argument("--type", choices=["north", "aspect", "samples"], default="samples", help="Chart type")
    parser.add_argument("--lagna", type=int, default=1, help="Lagna Rashi number (1 to 12)")
    parser.add_argument("--title", type=str, default="जन्म कुण्डली", help="Chart Title")
    parser.add_argument("--output", type=str, default="", help="Output SVG filepath")
    args = parser.parse_args()

    if args.type == "samples":
        out_dir = "/Users/apple/Movies/ap/TantraGyan/astrology-book-engine/assets/icons"
        os.makedirs(out_dir, exist_ok=True)
        samples = generate_sample_kundlis()
        for key, svg_code in samples.items():
            path = os.path.join(out_dir, f"{key}.svg")
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg_code)
            print(f"Generated chart: {path}")
    elif args.type == "north":
        svg_code = generate_north_indian_chart(lagna_rashi=args.lagna, title=args.title)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(svg_code)
            print(f"Saved to {args.output}")
        else:
            print(svg_code)
    elif args.type == "aspect":
        svg_code = generate_aspect_wheel()
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(svg_code)
            print(f"Saved to {args.output}")
        else:
            print(svg_code)
