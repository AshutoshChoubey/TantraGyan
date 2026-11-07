#!/usr/bin/env python3
"""
Astrology Chart SVG Generator
==============================
Generates enterprise-grade vector SVGs based directly on
/Users/apple/Movies/ap/vedic-astrology-kundali-studio:
1. Enterprise North Indian Diamond Kundali (Parashara & AstroSage layout with 3D Base64 icons)
2. Planetary Aspects & Drishti Wheel
3. Navamsha & Divisional Charts
"""

import sys
import os
import argparse
import html

# Ensure local visualizer is accessible
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

from visualizer.diamond_chart import generate_diamond_chart_svg
from visualizer.specialized_charts import (
    generate_elements_diamond_chart,
    generate_upachaya_diamond_chart,
    generate_kendra_trikona_diamond_chart,
    generate_nakshatra_mandala_wheel,
    generate_bhava_karaka_diamond_chart,
    generate_kalpurush_bhavas_diamond_chart,
    generate_panch_mahapurush_rajyogas_chart
)

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


def generate_enterprise_kundli(
    lagna_sign_idx=0, # 0 = Aries, 3 = Cancer, etc.
    occupants=None,
    chart_title="D1 • जन्म कुण्डली (LAGNA CHAKRA)",
    birth_meta=None,
    width=540,
    height=615
):
    """
    Invokes the enterprise North Indian Diamond SVG visualizer from
    vedic-astrology-kundali-studio.
    """
    if occupants is None:
        occupants = {}
    if birth_meta is None:
        birth_meta = {
            "name": "आशुतोष कुमार चौबे (Ashutosh Kumar Choubey)",
            "dob": "1994-10-28",
            "tob": "03:45:00",
            "place": "Garhwa, Jharkhand, India",
            "ayanamsa": "Lahiri (Chitrapaksha)"
        }

    return generate_diamond_chart_svg(
        house_occupants=occupants,
        lagna_sign_idx=lagna_sign_idx,
        chart_title=chart_title,
        birth_meta=birth_meta,
        width=width,
        height=height
    )


generate_north_indian_chart = generate_enterprise_kundli


def generate_aspect_wheel(width=500, height=500, theme="parchment"):
    """
    Renders an authentic 12-house planetary aspect matrix / Drishti wheel.
    Visualizes 7th direct aspect, Mars 4-7-8, Jupiter 5-7-9, Saturn 3-7-10.
    """
    cx = width / 2
    cy = height / 2
    radius = (width / 2) - 45

    bg_color = "#fffdf7"
    border_color = "#854d0e"
    text_color = "#1e293b"

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" class="vedic-aspect-svg" style="max-width:{width}px; background:{bg_color}; border-radius:12px; border:1.8px solid {border_color}; box-shadow:0 4px 18px rgba(0,0,0,0.06);">',
        f'  <!-- Aspect Mandala Wheel -->',
        f'  <circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{border_color}" stroke-width="2" />',
        f'  <circle cx="{cx}" cy="{cy}" r="{radius * 0.65}" fill="none" stroke="{border_color}" stroke-width="1.2" stroke-dasharray="4,3" opacity="0.6"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="{radius * 0.28}" fill="{border_color}" fill-opacity="0.08" stroke="{border_color}" stroke-width="1.5"/>',
        f'  <text x="{cx}" y="{cy - 5}" fill="{border_color}" font-family="\'Noto Sans Devanagari\', \'Devanagari MT\', \'Kohinoor Devanagari\', sans-serif" font-size="13" font-weight="bold" text-anchor="middle" dominant-baseline="middle">पूर्ण दृष्टि चक्र</text>',
        f'  <text x="{cx}" y="{cy + 13}" fill="#78716c" font-family="\'Cinzel\', \'Georgia\', serif" font-size="9" text-anchor="middle" dominant-baseline="middle">Aspect Mandala</text>'
    ]

    import math
    for i in range(12):
        angle = (i * 30) - 90
        rad = math.radians(angle)
        x = cx + radius * math.cos(rad)
        y = cy + radius * math.sin(rad)
        label_x = cx + (radius + 24) * math.cos(rad)
        label_y = cy + (radius + 24) * math.sin(rad)

        r_hi, r_en = RASHI_NAMES[i]
        lines.append(f'  <line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{border_color}" stroke-width="0.8" opacity="0.35"/>')
        lines.append(f'  <circle cx="{x}" cy="{y}" r="4.5" fill="{border_color}"/>')
        lines.append(f'  <text x="{label_x}" y="{label_y + 3}" fill="{text_color}" font-family="\'Noto Sans Devanagari\', \'Devanagari MT\', \'Kohinoor Devanagari\', sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">{i+1}. {r_hi}</text>')

    lines.append('</svg>')
    return "\n".join(lines)


def generate_sample_kundlis():
    """Generates a dict of curated enterprise astrological charts for Tantra Gyan book chapters."""
    charts = {}

    # 1. Foundation Lagna Chart (Aries Ascendant / Sign index 0)
    charts["lagna_chart"] = generate_enterprise_kundli(
        lagna_sign_idx=0,
        occupants={
            1: [
                {"symbol": "Su", "dms": "10°00'", "dignity_code": "EXALTED"},
                {"symbol": "Ju", "dms": "12°30'", "dignity_code": "FRIEND"}
            ],
            4: [
                {"symbol": "Mo", "dms": "03°15'", "dignity_code": "OWN"}
            ],
            7: [
                {"symbol": "Sa", "dms": "20°00'", "dignity_code": "EXALTED", "is_retrograde": True}
            ],
            10: [
                {"symbol": "Ma", "dms": "28°00'", "dignity_code": "EXALTED"}
            ]
        },
        chart_title="D1 • कालपुरुष कुण्डली (KAALPURUSHA LAGNA)",
        birth_meta={
            "name": "तंत्र ज्ञान • शास्त्रीय आदर्श कुण्डली (Classical Standard)",
            "dob": "शास्त्रीय विन्यास",
            "tob": "प्रातः काल",
            "place": "उज्जयिनी (Ujjain, India)",
            "ayanamsa": "Lahiri (Chitrapaksha)"
        }
    )

    # 2. Pancha Mahapurusha & Gajakesari Raja Yogas (Comprehensive Master Chart)
    charts["raja_yogas_chart"] = generate_panch_mahapurush_rajyogas_chart()

    # 3. Viparita Raja Yogas (Libra Ascendant / Sign index 6)
    charts["viparita_chart"] = generate_enterprise_kundli(
        lagna_sign_idx=6,
        occupants={
            1: [
                {"symbol": "Sa", "dms": "20°00'", "dignity_code": "EXALTED"}
            ],
            6: [
                {"symbol": "Ju", "dms": "15°30'", "dignity_code": "OWN"}
            ],
            8: [
                {"symbol": "Ve", "dms": "08°45'", "dignity_code": "OWN"}
            ],
            12: [
                {"symbol": "Me", "dms": "15°00'", "dignity_code": "EXALTED"}
            ]
        },
        chart_title="हर्ष, सरल एवं विमल विपरीत राजयोग",
        birth_meta={
            "name": "त्रिक भाव (6, 8, 12) राजयोग समन्वय",
            "dob": "तुला लग्न विन्यास",
            "tob": "सायं काल",
            "place": "प्रयागराज (Prayagraj, India)",
            "ayanamsa": "Lahiri (Chitrapaksha)"
        }
    )

    # 4. Medical Astrology - Arbuda Roga (Scorpio Ascendant / Sign index 7)
    charts["medical_astrology_chart"] = generate_enterprise_kundli(
        lagna_sign_idx=7,
        occupants={
            1: [
                {"symbol": "Su", "dms": "12°00'", "dignity_code": "FRIEND"}
            ],
            6: [
                {"symbol": "Mo", "dms": "22°10'", "dignity_code": "DEBILITATED"},
                {"symbol": "Ra", "dms": "14°30'"}
            ],
            8: [
                {"symbol": "Ma", "dms": "18°20'"},
                {"symbol": "Sa", "dms": "24°10'"}
            ],
            12: [
                {"symbol": "Ke", "dms": "14°30'"}
            ]
        },
        chart_title="आयुर्-ज्योतिष: अर्बुद (कैंसर) रोग योग",
        birth_meta={
            "name": "कोशिका असंतुलन एवं त्रिक भाव ग्रह दोष",
            "dob": "वृश्चिक लग्न विन्यास",
            "tob": "रात्रि काल",
            "place": "अयोध्या (Ayodhya, India)",
            "ayanamsa": "Lahiri (Chitrapaksha)"
        }
    )

    # 5. Aspect Wheel
    charts["aspect_wheel"] = generate_aspect_wheel()

    # 6. Four Elements Diamond Kundali (Tattva Chakra)
    charts["elements_diamond_chart"] = generate_elements_diamond_chart()

    # 7. Upachaya Houses Growth & Compounding Kundali
    charts["upachaya_diamond_chart"] = generate_upachaya_diamond_chart()

    # 8. Kendra & Trikona Divine Geometry (Lakshmi-Narayana Yoga)
    charts["kendra_trikona_diamond_chart"] = generate_kendra_trikona_diamond_chart()

    # 9. 360° Circular Nakshatra & Pada Mandala Wheel
    charts["nakshatra_mandala_wheel"] = generate_nakshatra_mandala_wheel()

    # 10. Bhava Karakatva & Planetary Rulers Diamond Chart
    charts["bhava_karaka_diamond_chart"] = generate_bhava_karaka_diamond_chart()

    # 11. Kalpurush Bhava Classification Master Diamond Chart
    charts["kalpurush_bhavas_diamond_chart"] = generate_kalpurush_bhavas_diamond_chart()

    return charts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enterprise Astrological Diamond Chart Generator")
    parser.add_argument("--samples", action="store_true", default=True, help="Generate all sample SVGs")
    args = parser.parse_args()

    engine_dir = os.path.dirname(CURRENT_DIR)
    root_dir = os.path.dirname(engine_dir)

    out_dirs = [
        os.path.join(engine_dir, "assets", "icons"),
        os.path.join(engine_dir, "dist", "pdf", "assets", "icons"),
        os.path.join(root_dir, "assets", "icons")
    ]
    for d in out_dirs:
        os.makedirs(d, exist_ok=True)

    samples = generate_sample_kundlis()
    for key, svg_code in samples.items():
        for d in out_dirs:
            path = os.path.join(d, f"{key}.svg")
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg_code)
        print(f"Generated enterprise astrological chart: {key}.svg in all icon targets")
