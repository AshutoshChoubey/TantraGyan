#!/usr/bin/env python3
"""
Specialized Astrological Vector Chart Generators
=================================================
Produces publication-grade, scalable vector SVGs for Tantra Gyan:
1. Elements Diamond Kundali (चतुर्विध महाभूत कुण्डली चक्र - Tattva Chakra)
2. Upachaya Houses Growth & Compounding Kundali (उपचय भाव साधन चक्र - Upachaya Chakra)
3. Kendra & Trikona Divine Architecture (लक्ष्मी-नारायण राजयोग व केन्द्र-त्रिकोण चक्र)
4. 360° Circular Nakshatra & Pada Mandala Wheel (सप्तविंशति नक्षत्र महामण्डल चक्र)
5. 12 Houses Natural Karakatva & Planetary Rulers (द्वादश भाव कारकत्व व स्थिर ग्रह चक्र)
"""

import math
import html
from typing import Dict, List, Tuple, Any

# Geometric coordinates for 540x680 North Indian Diamond Chart:
# Outer frame X: 20..520 (width: 500), Y: 100..600 (height: 500), Center: (270, 350)
HOUSE_POLYGONS = {
    1:  "270,100 395,225 270,350 145,225", # Top Diamond (Lagna)
    2:  "20,100 270,100 145,225",          # Top-Left Triangle
    3:  "20,100 145,225 20,350",           # Left-Top Triangle
    4:  "20,350 145,225 270,350 145,475",  # Left Diamond
    5:  "20,350 145,475 20,600",           # Left-Bottom Triangle
    6:  "20,600 145,475 270,600",          # Bottom-Left Triangle
    7:  "270,350 395,475 270,600 145,475", # Bottom Diamond
    8:  "270,600 395,475 520,600",          # Bottom-Right Triangle
    9:  "520,600 395,475 520,350",          # Right-Bottom Triangle
    10: "270,350 395,225 520,350 395,475", # Right Diamond
    11: "520,350 395,225 520,100",          # Right-Top Triangle
    12: "520,100 395,225 270,100"           # Top-Right Triangle
}

HOUSE_CENTROIDS = {
    1:  (270.0, 225.0),
    2:  (145.0, 142.0),
    3:  (62.0,  225.0),
    4:  (145.0, 350.0),
    5:  (62.0,  475.0),
    6:  (145.0, 558.0),
    7:  (270.0, 475.0),
    8:  (395.0, 558.0),
    9:  (478.0, 475.0),
    10: (395.0, 350.0),
    11: (478.0, 225.0),
    12: (395.0, 142.0)
}

# Standard fonts string for SVGs
SVG_FONT_FAMILY = "'Noto Sans Devanagari', 'Noto Serif Devanagari', -apple-system, BlinkMacSystemFont, sans-serif"
SVG_SERIF_FAMILY = "'Noto Serif Devanagari', 'Georgia', serif"

# Authentic Planet Colors & Icons Palette
PLANETS_INFO = {
    "Su": {"name": "सूर्य (Sun)", "color": "#c2410c", "bg": "#fff7ed", "border": "#ea580c", "file": "sun.png"},
    "Mo": {"name": "चन्द्र (Moon)", "color": "#334155", "bg": "#f8fafc", "border": "#94a3b8", "file": "moon.png"},
    "Ma": {"name": "मंगल (Mars)", "color": "#dc2626", "bg": "#fef2f2", "border": "#ef4444", "file": "mars.png"},
    "Me": {"name": "बुध (Mercury)", "color": "#047857", "bg": "#f0fdf4", "border": "#10b981", "file": "mercury.png"},
    "Ju": {"name": "गुरु (Jupiter)", "color": "#b45309", "bg": "#fffbeb", "border": "#f59e0b", "file": "jupiter.png"},
    "Ve": {"name": "शुक्र (Venus)", "color": "#be185d", "bg": "#fdf2f8", "border": "#f43f5e", "file": "venus.png"},
    "Sa": {"name": "शनि (Saturn)", "color": "#1d4ed8", "bg": "#eff6ff", "border": "#3b82f6", "file": "saturn.png"},
    "Ra": {"name": "राहु (Rahu)", "color": "#09090b", "bg": "#f4f4f5", "border": "#27272a", "file": "rahu.png"},
    "Ke": {"name": "केतु (Ketu)", "color": "#52525b", "bg": "#f4f4f5", "border": "#71717a", "file": "ketu.png"}
}


# ==============================================================================
# 1. THE FOUR ELEMENTS DIAMOND KUNDALI (चतुर्विध महाभूत कुण्डली चक्र)
# ==============================================================================
def generate_elements_diamond_chart(width: int = 560, height: int = 700) -> str:
    """
    Renders an authoritative North Indian Diamond Kundali color-coded by the
    4 Primordial Vedic Elements (Agni, Prithvi, Vayu, Jala).
    Takes a full book page or web container.
    """
    elements_mapping = {
        # Fire (अग्नि) - Dharma Trikona: Houses 1, 5, 9
        1:  {"element": "agni", "name": "अग्नि तत्व", "en": "FIRE", "trikona": "धर्म त्रिकोण", "sign": "मेष (1)", "karakatva": "तनु / आत्मबल", "graha": "Ma/Su"},
        5:  {"element": "agni", "name": "अग्नि तत्व", "en": "FIRE", "trikona": "धर्म त्रिकोण", "sign": "सिंह (5)", "karakatva": "धी / पूर्वपुण्य", "graha": "Su/Ju"},
        9:  {"element": "agni", "name": "अग्नि तत्व", "en": "FIRE", "trikona": "धर्म त्रिकोण", "sign": "धनु (9)", "karakatva": "भाग्य / धर्म", "graha": "Ju/Su"},

        # Earth (पृथ्वी) - Artha Trikona: Houses 2, 6, 10
        2:  {"element": "earth", "name": "पृथ्वी तत्व", "en": "EARTH", "trikona": "अर्थ त्रिकोण", "sign": "वृषभ (2)", "karakatva": "धन / कुटुंब", "graha": "Ve/Ju"},
        6:  {"element": "earth", "name": "पृथ्वी तत्व", "en": "EARTH", "trikona": "अर्थ त्रिकोण", "sign": "कन्या (6)", "karakatva": "सेवा / विजय", "graha": "Me/Sa"},
        10: {"element": "earth", "name": "पृथ्वी तत्व", "en": "EARTH", "trikona": "अर्थ त्रिकोण", "sign": "मकर (10)", "karakatva": "कर्म / सत्ता", "graha": "Sa/Su"},

        # Air (वायु) - Kama Trikona: Houses 3, 7, 11
        3:  {"element": "air", "name": "वायु तत्व", "en": "AIR", "trikona": "काम त्रिकोण", "sign": "मिथुन (3)", "karakatva": "साहस / उद्यम", "graha": "Me/Ma"},
        7:  {"element": "air", "name": "वायु तत्व", "en": "AIR", "trikona": "काम त्रिकोण", "sign": "तुला (7)", "karakatva": "जाया / व्यापार", "graha": "Ve"},
        11: {"element": "air", "name": "वायु तत्व", "en": "AIR", "trikona": "काम त्रिकोण", "sign": "कुंभ (11)", "karakatva": "लाभ / मित्र", "graha": "Sa/Ju"},

        # Water (जल) - Moksha Trikona: Houses 4, 8, 12
        4:  {"element": "water", "name": "जल तत्व", "en": "WATER", "trikona": "मोक्ष त्रिकोण", "sign": "कर्क (4)", "karakatva": "सुख / मन", "graha": "Mo/Ve"},
        8:  {"element": "water", "name": "जल तत्व", "en": "WATER", "trikona": "मोक्ष त्रिकोण", "sign": "वृश्चिक (8)", "karakatva": "आयु / गूढ़", "graha": "Ma/Sa"},
        12: {"element": "water", "name": "जल तत्व", "en": "WATER", "trikona": "मोक्ष त्रिकोण", "sign": "मीन (12)", "karakatva": "मोक्ष / विसर्जन", "graha": "Ju/Ke"}
    }

    elem_styles = {
        "agni":  {"fill": "url(#gradFire)",  "stroke": "#ea580c", "text_dark": "#9a3412", "pill": "#ffedd5", "pill_border": "#fdba74", "symbol": "🔥"},
        "earth": {"fill": "url(#gradEarth)", "stroke": "#d97706", "text_dark": "#854d0e", "pill": "#fef9c3", "pill_border": "#fde047", "symbol": "⛰️"},
        "air":   {"fill": "url(#gradAir)",   "stroke": "#0284c7", "text_dark": "#075985", "pill": "#e0f2fe", "pill_border": "#7dd3fc", "symbol": "💨"},
        "water": {"fill": "url(#gradWater)", "stroke": "#0d9488", "text_dark": "#115e59", "pill": "#ccfbf1", "pill_border": "#5eead4", "symbol": "🌊"}
    }

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" class="astro-chart-svg astro-elements-chart">',
        '  <defs>',
        '    <!-- Background parchment gradient -->',
        '    <linearGradient id="parchmentBg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fffefb"/>',
        '      <stop offset="100%" stop-color="#faf5e8"/>',
        '    </linearGradient>',
        '    <!-- Element Gradients -->',
        '    <linearGradient id="gradFire" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fee2e2" stop-opacity="0.92"/>',
        '      <stop offset="100%" stop-color="#ffedd5" stop-opacity="0.92"/>',
        '    </linearGradient>',
        '    <linearGradient id="gradEarth" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.92"/>',
        '      <stop offset="100%" stop-color="#fef9c3" stop-opacity="0.92"/>',
        '    </linearGradient>',
        '    <linearGradient id="gradAir" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#e0f2fe" stop-opacity="0.92"/>',
        '      <stop offset="100%" stop-color="#eff6ff" stop-opacity="0.92"/>',
        '    </linearGradient>',
        '    <linearGradient id="gradWater" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ccfbf1" stop-opacity="0.92"/>',
        '      <stop offset="100%" stop-color="#e0f2fe" stop-opacity="0.92"/>',
        '    </linearGradient>',
        '    <!-- Drop Shadow Filter -->',
        '    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">',
        '      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.08"/>',
        '    </filter>',
        '  </defs>',

        '  <!-- Outer Plate Frame -->',
        f'  <rect x="6" y="6" width="{width-12}" height="{height-12}" rx="12" fill="url(#parchmentBg)" stroke="#c89d3d" stroke-width="2" filter="url(#shadow)"/>',
        f'  <rect x="12" y="12" width="{width-24}" height="{height-24}" rx="8" fill="none" stroke="#eab308" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>',

        '  <!-- Header Banner -->',
        f'  <rect x="24" y="20" width="{width-48}" height="66" rx="6" fill="#ffffff" stroke="#c89d3d" stroke-width="1.2"/>',
        f'  <text x="{width//2}" y="42" font-family="{SVG_SERIF_FAMILY}" font-size="16" font-weight="800" fill="#78350f" text-anchor="middle">चतुर्विध महाभूत कुण्डली चक्र • Tattva Chakra</text>',
        f'  <text x="{width//2}" y="60" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="600" fill="#92400e" text-anchor="middle">अग्नि (Fire), पृथ्वी (Earth), वायु (Air) एवं जल (Water) तत्वों का भाव समन्वय</text>',
        f'  <text x="{width//2}" y="74" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#78716c" text-anchor="middle">कालपुरुष लग्न विन्यास • धर्म, अर्थ, काम व मोक्ष त्रिकोण का संपूर्ण फलित दर्पण</text>',

        '  <!-- Diamond Kundali Outer Frame (X: 30 to 530, Y: 96 to 596) -->',
        '  <g transform="translate(10, 0)">'
    ]

    # Draw each house polygon with its authentic element fill
    for h in range(1, 13):
        poly = HOUSE_POLYGONS[h]
        info = elements_mapping[h]
        style = elem_styles[info["element"]]

        svg.append(f'    <!-- House {h}: {info["name"]} -->')
        svg.append(f'    <polygon points="{poly}" fill="{style["fill"]}" stroke="{style["stroke"]}" stroke-width="1.8"/>')

    # Draw Inner Accent Crossing Lines and Center Cross
    svg.extend([
        '    <polygon points="270,100 520,350 270,600 20,350" fill="none" stroke="#854d0e" stroke-width="1.5" opacity="0.75"/>',
        '    <line x1="20" y1="100" x2="520" y2="600" stroke="#854d0e" stroke-width="1.2" opacity="0.6"/>',
        '    <line x1="520" y1="100" x2="20" y2="600" stroke="#854d0e" stroke-width="1.2" opacity="0.6"/>',
        '    <circle cx="270" cy="350" r="4.5" fill="#c89d3d" stroke="#78350f" stroke-width="1.5"/>'
    ])

    # Overlay Text Labels on House Centroids
    for h in range(1, 13):
        cx, cy = HOUSE_CENTROIDS[h]
        info = elements_mapping[h]
        style = elem_styles[info["element"]]

        # Sizing and spacing
        is_diamond = h in [1, 4, 7, 10]
        y_shift = -18 if is_diamond else -14

        svg.append(f'    <!-- Text block for House {h} -->')
        # House & Sign number
        svg.append(f'    <text x="{cx}" y="{cy + y_shift}" font-family="{SVG_FONT_FAMILY}" font-size="12" font-weight="900" fill="{style["text_dark"]}" text-anchor="middle">')
        svg.append(f'      {info["sign"]}')
        svg.append(f'    </text>')

        # Element Pill
        svg.append(f'    <text x="{cx}" y="{cy + y_shift + 14}" font-family="{SVG_FONT_FAMILY}" font-size="10" font-weight="700" fill="{style["stroke"]}" text-anchor="middle">')
        svg.append(f'      {style["symbol"]} {info["name"]}')
        svg.append(f'    </text>')

        # Karakatva
        svg.append(f'    <text x="{cx}" y="{cy + y_shift + 26}" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="600" fill="#334155" text-anchor="middle">')
        svg.append(f'      {info["karakatva"]}')
        svg.append(f'    </text>')

        # Trikona Category
        svg.append(f'    <text x="{cx}" y="{cy + y_shift + 37}" font-family="{SVG_FONT_FAMILY}" font-size="8" fill="#64748b" text-anchor="middle">')
        svg.append(f'      {info["trikona"]}')
        svg.append(f'    </text>')

    svg.append('  </g>') # End transform

    # Footer Legend Cards (The 4 Tattvas Summary)
    svg.extend([
        f'  <!-- Element Breakdown Footer Legend -->',
        f'  <g transform="translate(24, 608)">',
        f'    <!-- Agni / Fire -->',
        f'    <rect x="0" y="0" width="120" height="74" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/>',
        f'    <text x="60" y="16" font-family="{SVG_FONT_FAMILY}" font-size="10.5" font-weight="800" fill="#9a3412" text-anchor="middle">🔥 अग्नि (Fire)</text>',
        f'    <text x="60" y="30" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="700" fill="#ea580c" text-anchor="middle">भाव 1, 5, 9 (Dharma)</text>',
        f'    <text x="60" y="44" font-family="{SVG_FONT_FAMILY}" font-size="8" fill="#475569" text-anchor="middle">आत्मबल • मेधा • भाग्य</text>',
        f'    <text x="60" y="58" font-family="{SVG_FONT_FAMILY}" font-size="8" font-weight="600" fill="#c2410c" text-anchor="middle">स्वामी: मंगल, सूर्य, गुरु</text>',

        f'    <!-- Prithvi / Earth -->',
        f'    <rect x="130" y="0" width="120" height="74" rx="6" fill="#fefce8" stroke="#d97706" stroke-width="1.2"/>',
        f'    <text x="190" y="16" font-family="{SVG_FONT_FAMILY}" font-size="10.5" font-weight="800" fill="#854d0e" text-anchor="middle">⛰️ पृथ्वी (Earth)</text>',
        f'    <text x="190" y="30" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="700" fill="#d97706" text-anchor="middle">भाव 2, 6, 10 (Artha)</text>',
        f'    <text x="190" y="44" font-family="{SVG_FONT_FAMILY}" font-size="8" fill="#475569" text-anchor="middle">धन • सेवा • साम्राज्य</text>',
        f'    <text x="190" y="58" font-family="{SVG_FONT_FAMILY}" font-size="8" font-weight="600" fill="#b45309" text-anchor="middle">स्वामी: शुक्र, बुध, शनि</text>',

        f'    <!-- Vayu / Air -->',
        f'    <rect x="260" y="0" width="120" height="74" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/>',
        f'    <text x="320" y="16" font-family="{SVG_FONT_FAMILY}" font-size="10.5" font-weight="800" fill="#075985" text-anchor="middle">💨 वायु (Air)</text>',
        f'    <text x="320" y="30" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="700" fill="#0284c7" text-anchor="middle">भाव 3, 7, 11 (Kama)</text>',
        f'    <text x="320" y="44" font-family="{SVG_FONT_FAMILY}" font-size="8" fill="#475569" text-anchor="middle">साहस • व्यापार • सर्वलाभ</text>',
        f'    <text x="320" y="58" font-family="{SVG_FONT_FAMILY}" font-size="8" font-weight="600" fill="#0369a1" text-anchor="middle">स्वामी: बुध, शुक्र, शनि</text>',

        f'    <!-- Jala / Water -->',
        f'    <rect x="390" y="0" width="122" height="74" rx="6" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.2"/>',
        f'    <text x="451" y="16" font-family="{SVG_FONT_FAMILY}" font-size="10.5" font-weight="800" fill="#115e59" text-anchor="middle">🌊 जल (Water)</text>',
        f'    <text x="451" y="30" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="700" fill="#0d9488" text-anchor="middle">भाव 4, 8, 12 (Moksha)</text>',
        f'    <text x="451" y="44" font-family="{SVG_FONT_FAMILY}" font-size="8" fill="#475569" text-anchor="middle">सुख • गूढ़ साधना • मोक्ष</text>',
        f'    <text x="451" y="58" font-family="{SVG_FONT_FAMILY}" font-size="8" font-weight="600" fill="#0f766e" text-anchor="middle">स्वामी: चन्द्र, मंगल, गुरु</text>',
        f'  </g>',

        '</svg>'
    ])

    return "\n".join(svg)


# ==============================================================================
# 2. UPACHAYA HOUSES GROWTH & COMPOUNDING KUNDALI (उपचय भाव साधन चक्र)
# ==============================================================================
def generate_upachaya_diamond_chart(width: int = 560, height: int = 700) -> str:
    """
    Renders an Upachaya Kundali with glowing growth arrows (↗) and milestone
    compounding ages on Houses 3, 6, 10, 11.
    """
    upachaya_houses = {
        3:  {"name": "सहज / पराक्रम भाव", "sign": "3 (मिथुन)", "karaka": "Mars (मंगल)", "age": "आयु 28+", "desc": "उद्यम, लेखन व पुरुषार्थ से उत्थान", "arrow": "↗ वृद्धि"},
        6:  {"name": "शत्रु / रोग / ऋण भाव", "sign": "6 (कन्या)", "karaka": "Mars / Saturn", "age": "आयु 32+", "desc": "बाधाओं व षडरिपुओं पर विजय", "arrow": "↗ विजय"},
        10: {"name": "कर्म / साम्राज्य भाव", "sign": "10 (मकर)", "karaka": "Sun / Saturn", "age": "आयु 36+", "desc": "राज्य पद, अधिकार व कीर्ति पराकाष्ठा", "arrow": "↗ उत्कर्ष"},
        11: {"name": "आय / एकादश लाभ भाव", "sign": "11 (कुंभ)", "karaka": "Jupiter (गुरु)", "age": "आयु 40+", "desc": "सर्व-मनोरथ सिद्धि व आर्थिक प्रचुरता", "arrow": "↗ सिद्धि"}
    }

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" class="astro-chart-svg astro-upachaya-chart">',
        '  <defs>',
        '    <linearGradient id="upachayaParchment" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fffdfa"/>',
        '      <stop offset="100%" stop-color="#fdf8ed"/>',
        '    </linearGradient>',
        '    <linearGradient id="upachayaActive" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.95"/>',
        '      <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.95"/>',
        '    </linearGradient>',
        '    <linearGradient id="upachayaPassive" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#f8fafc" stop-opacity="0.6"/>',
        '      <stop offset="100%" stop-color="#f1f5f9" stop-opacity="0.6"/>',
        '    </linearGradient>',
        '    <!-- Glow Filter for Arrows -->',
        '    <filter id="goldGlow" x="-20%" y="-20%" width="140%" height="140%">',
        '      <feGaussianBlur stdDeviation="3" result="blur"/>',
        '      <feComposite in="SourceGraphic" in2="blur" operator="over"/>',
        '    </filter>',
        '  </defs>',

        f'  <rect x="6" y="6" width="{width-12}" height="{height-12}" rx="12" fill="url(#upachayaParchment)" stroke="#b45309" stroke-width="2"/>',
        f'  <rect x="12" y="12" width="{width-24}" height="{height-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>',

        '  <!-- Header Banner -->',
        f'  <rect x="24" y="20" width="{width-48}" height="66" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.2"/>',
        f'  <text x="{width//2}" y="42" font-family="{SVG_SERIF_FAMILY}" font-size="16" font-weight="800" fill="#78350f" text-anchor="middle">उपचय भाव साधन चक्र • Upachaya Growth Mandala</text>',
        f'  <text x="{width//2}" y="60" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="600" fill="#b45309" text-anchor="middle">भाव 3, 6, 10, 11 — सतत संचय, संघर्ष से विजय एवं आयु अनुसार उत्थान</text>',
        f'  <text x="{width//2}" y="74" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#78716c" text-anchor="middle">क्रूर ग्रहों (शनि, मंगल, सूर्य, राहु) का स्वर्ण-तुल्य फल देने का शास्त्रीय रहस्य</text>',

        '  <!-- Diamond Kundali (X: 30 to 530, Y: 96 to 596) -->',
        '  <g transform="translate(10, 0)">'
    ]

    # Render house polygons
    for h in range(1, 13):
        poly = HOUSE_POLYGONS[h]
        if h in upachaya_houses:
            # Active glowing Upachaya house
            svg.append(f'    <!-- Upachaya House {h} -->')
            svg.append(f'    <polygon points="{poly}" fill="url(#upachayaActive)" stroke="#b45309" stroke-width="2.5"/>')
        else:
            # Passive dimmed house
            svg.append(f'    <polygon points="{poly}" fill="url(#upachayaPassive)" stroke="#cbd5e1" stroke-width="1.2"/>')

    # Draw Inner Accent Lines
    svg.extend([
        '    <polygon points="270,100 520,350 270,600 20,350" fill="none" stroke="#78350f" stroke-width="1.2" opacity="0.65"/>',
        '    <line x1="20" y1="100" x2="520" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <line x1="520" y1="100" x2="20" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <circle cx="270" cy="350" r="4" fill="#b45309"/>'
    ])

    # Connective Dynamic Growth Arrows: 3 -> 6 -> 10 -> 11
    svg.extend([
        '    <!-- Compounding Ladder Vectors -->',
        '    <path d="M 62 255 Q 80 400 145 525" fill="none" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="5,4" marker-end="url(#arrowhead)"/>',
        '    <path d="M 175 558 Q 300 530 395 385" fill="none" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="5,4"/>',
        '    <path d="M 395 320 Q 420 280 478 245" fill="none" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="5,4"/>'
    ])

    # Render Labels on all houses
    for h in range(1, 13):
        cx, cy = HOUSE_CENTROIDS[h]
        if h in upachaya_houses:
            u = upachaya_houses[h]
            # Prominent Upachaya Callout
            svg.append(f'    <!-- Upachaya House {h} Label -->')
            svg.append(f'    <rect x="{cx - 45}" y="{cy - 28}" width="90" height="20" rx="10" fill="#b45309" filter="url(#goldGlow)"/>')
            svg.append(f'    <text x="{cx}" y="{cy - 14}" font-family="{SVG_FONT_FAMILY}" font-size="10.5" font-weight="900" fill="#ffffff" text-anchor="middle">★ {u["arrow"]} • {u["sign"]}</text>')

            svg.append(f'    <text x="{cx}" y="{cy + 2}" font-family="{SVG_FONT_FAMILY}" font-size="10" font-weight="800" fill="#78350f" text-anchor="middle">{u["name"]}</text>')
            svg.append(f'    <text x="{cx}" y="{cy + 15}" font-family="{SVG_FONT_FAMILY}" font-size="8.8" font-weight="700" fill="#b45309" text-anchor="middle">कारक: {u["karaka"]}</text>')
            svg.append(f'    <text x="{cx}" y="{cy + 27}" font-family="{SVG_FONT_FAMILY}" font-size="8.5" font-weight="800" fill="#dc2626" text-anchor="middle">सक्रियता: {u["age"]}</text>')
        else:
            # Passive house subtle label
            svg.append(f'    <text x="{cx}" y="{cy}" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle">भाव {h}</text>')

    svg.append('  </g>')

    # Footer Upachaya Predictive Philosophy Card
    svg.extend([
        f'  <g transform="translate(24, 608)">',
        f'    <rect x="0" y="0" width="{width-48}" height="74" rx="6" fill="#fffbeb" stroke="#b45309" stroke-width="1.2"/>',
        f'    <text x="18" y="20" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="800" fill="#78350f">महर्षि पराशर सूत्र: "उपचयेषु क्रूराः शुभाः" — पापी ग्रह उपचय में क्यों सर्वश्रेष्ठ होते हैं?</text>',
        f'    <text x="18" y="37" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#451a03">1. भाव 3 (साहस): क्रूर ग्रह जातक को निर्भीक बनाते हैं, जिससे वह जोखिम लेकर नए साम्राज्य खड़े करता है।</text>',
        f'    <text x="18" y="51" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#451a03">2. भाव 6 (प्रतियोगिता): मंगल व शनि शत्रुओं, रोगों और कर्जों का निर्मूलन करते हैं। जातक कोर्ट-कचहरी जीतता है।</text>',
        f'    <text x="18" y="65" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#451a03">3. भाव 10 व 11 (कर्म व लाभ): 36 से 40 वर्ष की आयु में जातक को जीवन के सर्वोच्च वित्तीय व सामाजिक शिखर पर पहुंचाते हैं।</text>',
        f'  </g>',

        '</svg>'
    ])

    return "\n".join(svg)


# ==============================================================================
# 3. KENDRA & TRIKONA DIVINE GEOMETRY (लक्ष्मी-नारायण राजयोग चक्र)
# ==============================================================================
def generate_kendra_trikona_diamond_chart(width: int = 560, height: int = 700) -> str:
    """
    Renders an authoritative North Indian Diamond Kundali illustrating
    Vishnu Sthanas (Kendras: 1, 4, 7, 10) and Lakshmi Sthanas (Trikonas: 1, 5, 9).
    """
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" class="astro-chart-svg astro-kendra-trikona-chart">',
        '  <defs>',
        '    <linearGradient id="ktBg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fffefc"/>',
        '      <stop offset="100%" stop-color="#faf5ea"/>',
        '    </linearGradient>',
        '    <linearGradient id="gradVishnu" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#eff6ff" stop-opacity="0.95"/>',
        '      <stop offset="100%" stop-color="#dbeafe" stop-opacity="0.95"/>',
        '    </linearGradient>',
        '    <linearGradient id="gradLakshmi" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fdf2f8" stop-opacity="0.95"/>',
        '      <stop offset="100%" stop-color="#fce7f3" stop-opacity="0.95"/>',
        '    </linearGradient>',
        '    <linearGradient id="gradLagnaSupreme" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.98"/>',
        '      <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.98"/>',
        '    </linearGradient>',
        '  </defs>',

        f'  <rect x="6" y="6" width="{width-12}" height="{height-12}" rx="12" fill="url(#ktBg)" stroke="#d97706" stroke-width="2"/>',
        f'  <rect x="12" y="12" width="{width-24}" height="{height-24}" rx="8" fill="none" stroke="#f59e0b" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>',

        '  <!-- Header Banner -->',
        f'  <rect x="24" y="20" width="{width-48}" height="66" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>',
        f'  <text x="{width//2}" y="42" font-family="{SVG_SERIF_FAMILY}" font-size="16" font-weight="800" fill="#78350f" text-anchor="middle">लक्ष्मी-नारायण योग एवं केन्द्र-त्रिकोण चक्र</text>',
        f'  <text x="{width//2}" y="60" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="600" fill="#b45309" text-anchor="middle">विष्णु स्थान (केन्द्र: 1, 4, 7, 10) एवं लक्ष्मी स्थान (त्रिकोण: 1, 5, 9) का संगम</text>',
        f'  <text x="{width//2}" y="74" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#78716c" text-anchor="middle">वैदिक राजयोग का सर्वोच्च ज्यामितीय व आध्यात्मिक सिद्धांत</text>',

        '  <!-- Diamond Kundali (X: 30 to 530, Y: 96 to 596) -->',
        '  <g transform="translate(10, 0)">'
    ]

    # Draw house polygons
    for h in range(1, 13):
        poly = HOUSE_POLYGONS[h]
        if h == 1:
            # Lagna is BOTH Kendra & Trikona (Supreme Auspiciousness)
            svg.append(f'    <polygon points="{poly}" fill="url(#gradLagnaSupreme)" stroke="#b45309" stroke-width="3"/>')
        elif h in [4, 7, 10]:
            # Vishnu Sthana (Kendra)
            svg.append(f'    <polygon points="{poly}" fill="url(#gradVishnu)" stroke="#2563eb" stroke-width="2.2"/>')
        elif h in [5, 9]:
            # Lakshmi Sthana (Trikona)
            svg.append(f'    <polygon points="{poly}" fill="url(#gradLakshmi)" stroke="#db2777" stroke-width="2.2"/>')
        else:
            # Neutral / Dusthana
            svg.append(f'    <polygon points="{poly}" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.0" opacity="0.65"/>')

    # Accent Lines
    svg.extend([
        '    <polygon points="270,100 520,350 270,600 20,350" fill="none" stroke="#78350f" stroke-width="1.2" opacity="0.65"/>',
        '    <line x1="20" y1="100" x2="520" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <line x1="520" y1="100" x2="20" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <circle cx="270" cy="350" r="4.5" fill="#f59e0b" stroke="#78350f" stroke-width="1.5"/>'
    ])

    # Connecting Raja Yoga Rays (Lagna to 5, 9, 4, 7, 10)
    svg.extend([
        '    <!-- Sacred Raja Yoga Energy Vectors -->',
        '    <line x1="270" y1="225" x2="62" y2="475" stroke="#db2777" stroke-width="1.8" stroke-dasharray="4,3" opacity="0.75"/>',
        '    <line x1="270" y1="225" x2="478" y2="475" stroke="#db2777" stroke-width="1.8" stroke-dasharray="4,3" opacity="0.75"/>',
        '    <line x1="270" y1="225" x2="145" y2="350" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="4,3" opacity="0.75"/>',
        '    <line x1="270" y1="225" x2="395" y2="350" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="4,3" opacity="0.75"/>',
        '    <line x1="270" y1="225" x2="270" y2="475" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="4,3" opacity="0.75"/>'
    ])

    # House Labels
    kendra_names = {
        1:  ("प्रथम भाव (Lagna)", "केन्द्र + त्रिकोण (उभय)", "देह, आत्मा, यश", "#92400e"),
        4:  ("चतुर्थ भाव (Sukha)", "केन्द्र (विष्णु स्थान)", "गृह, भूमि, सुख", "#1e40af"),
        7:  ("सप्तम भाव (Jaya)", "केन्द्र (विष्णु स्थान)", "पत्नी, साझेदारी", "#1e40af"),
        10: ("दशम भाव (Karma)", "परम केन्द्र (विष्णु स्थान)", "कर्म, सत्ता, कीर्ति", "#1e40af"),
        5:  ("पंचम भाव (Putra)", "त्रिकोण (लक्ष्मी स्थान)", "मेधा, पूर्वपुण्य", "#9d174d"),
        9:  ("नवम भाव (Dharma)", "परम त्रिकोण (लक्ष्मी स्थान)", "भाग्य, धर्म, गुरु", "#9d174d")
    }

    for h in range(1, 13):
        cx, cy = HOUSE_CENTROIDS[h]
        if h in kendra_names:
            title, cat, sig, col = kendra_names[h]
            y_shift = -16 if h in [1, 4, 7, 10] else -12
            svg.append(f'    <text x="{cx}" y="{cy + y_shift}" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="900" fill="{col}" text-anchor="middle">{title}</text>')
            svg.append(f'    <text x="{cx}" y="{cy + y_shift + 13}" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="700" fill="{col}" text-anchor="middle">{cat}</text>')
            svg.append(f'    <text x="{cx}" y="{cy + y_shift + 25}" font-family="{SVG_FONT_FAMILY}" font-size="8.5" fill="#334155" text-anchor="middle">{sig}</text>')
        else:
            svg.append(f'    <text x="{cx}" y="{cy - 5}" font-family="{SVG_FONT_FAMILY}" font-size="10" font-weight="600" fill="#94a3b8" text-anchor="middle">भाव {h}</text>')
            dusthana_map = {6: "त्रिक (रोग/ऋण)", 8: "त्रिक (आयु/संकट)", 12: "त्रिक (मोक्ष/व्यय)", 2: "धन / मारक", 3: "सहज / उपचय", 11: "लाभ / उपचय"}
            if h in dusthana_map:
                svg.append(f'    <text x="{cx}" y="{cy + 8}" font-family="{SVG_FONT_FAMILY}" font-size="7.5" fill="#94a3b8" text-anchor="middle">{dusthana_map[h]}</text>')

    svg.append('  </g>')

    # Footer Card explaining Raja Yoga formulation
    svg.extend([
        f'  <g transform="translate(24, 608)">',
        f'    <rect x="0" y="0" width="{width-48}" height="74" rx="6" fill="#fdf4ff" stroke="#db2777" stroke-width="1.2"/>',
        f'    <text x="18" y="20" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="800" fill="#831843">सर्वोच्च राजयोग नियम: केन्द्रेश (विष्णु) + त्रिकोणेश (लक्ष्मी) युति / संबंध</text>',
        f'    <text x="18" y="37" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#701a75">1. केन्द्र भाव कर्म एवं पुरुषार्थ की शक्ति हैं, जबकि त्रिकोण भाव ईश्वरीय कृपा व संचित पुण्यों का कोष हैं।</text>',
        f'    <text x="18" y="51" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#701a75">2. जब 9वें (लक्ष्मी) का स्वामी 10वें (विष्णु) के स्वामी से मिलता है, तो "धर्म-कर्माधिपति राजयोग" बनता है।</text>',
        f'    <text x="18" y="65" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#701a75">3. लग्न भाव दोनों का प्रतिनिधित्व करने के कारण कुण्डली का सर्वाधिक तेजस्वी प्राण-बिंदु है।</text>',
        f'  </g>',

        '</svg>'
    ])

    return "\n".join(svg)


# ==============================================================================
# 4. 360° CIRCULAR NAKSHATRA & PADA MANDALA WHEEL (सप्तविंशति नक्षत्र महामण्डल)
# ==============================================================================
def generate_nakshatra_mandala_wheel(width: int = 650, height: int = 650) -> str:
    """
    Renders an authentic, highly detailed 360° vector circular mandala:
    - Ring 1: 12 Rashis (30° = 8.33% each) color-coded by the 4 elements.
    - Ring 2: 27 Nakshatras (13°20' = 3.704% each) color-coded by ruling planet.
    - Ring 3: 108 Padas (3°20' = 0.926% each) with quarter numbers.
    - Central Yantra & degree compass.
    """
    cx = width / 2
    cy = height / 2

    r_outer = (width / 2) - 30    # Outer border of padas
    r_padas = r_outer - 22        # Dividing line between padas and nakshatras
    r_nakshatras = r_padas - 52   # Dividing line between nakshatras and rashis
    r_rashis = r_nakshatras - 45  # Dividing line between rashis and inner core
    r_center = r_rashis - 35      # Sacred central emblem

    # 27 Nakshatras Data: (Name_Hi, Name_En, Lord, Lord_Color, Degrees_Start)
    nakshatra_lords = ["Ke", "Ve", "Su", "Mo", "Ma", "Ra", "Ju", "Sa", "Me"]
    nakshatra_names = [
        ("अश्विनी", "Ashwini", "Ke"),
        ("भरणी", "Bharani", "Ve"),
        ("कृत्तिका", "Krittika", "Su"),
        ("रोहिणी", "Rohini", "Mo"),
        ("मृगशिरा", "Mrigashira", "Ma"),
        ("आर्द्रा", "Ardra", "Ra"),
        ("पुनर्वसु", "Punarvasu", "Ju"),
        ("पुष्य", "Pushya", "Sa"),
        ("आश्लेषा", "Ashlesha", "Me"),

        ("मघा", "Magha", "Ke"),
        ("पूर्वाफाल्गुनी", "P. Phalguni", "Ve"),
        ("उत्तराफाल्गुनी", "U. Phalguni", "Su"),
        ("हस्त", "Hasta", "Mo"),
        ("चित्रा", "Chitra", "Ma"),
        ("स्वाति", "Swati", "Ra"),
        ("विशाखा", "Vishakha", "Ju"),
        ("अनुराधा", "Anuradha", "Sa"),
        ("ज्येष्ठा", "Jyeshtha", "Me"),

        ("मूल", "Mula", "Ke"),
        ("पूर्वाषाढ़ा", "P. Ashadha", "Ve"),
        ("उत्तराषाढ़ा", "U. Ashadha", "Su"),
        ("श्रवण", "Shravana", "Mo"),
        ("धनिष्ठा", "Dhanishta", "Ma"),
        ("शतभिषा", "Shatabhisha", "Ra"),
        ("पूर्वाभाद्रपद", "P. Bhadra", "Ju"),
        ("उत्तराभाद्रपद", "U. Bhadra", "Sa"),
        ("रेवती", "Revati", "Me")
    ]

    rashi_elements = [
        ("मेष", "Aries", "agni", "#ea580c", "#fff7ed"),
        ("वृषभ", "Taurus", "earth", "#d97706", "#fefce8"),
        ("मिथुन", "Gemini", "air", "#0284c7", "#f0f9ff"),
        ("कर्क", "Cancer", "water", "#0d9488", "#f0fdfa"),
        ("सिंह", "Leo", "agni", "#ea580c", "#fff7ed"),
        ("कन्या", "Virgo", "earth", "#d97706", "#fefce8"),
        ("तुला", "Libra", "air", "#0284c7", "#f0f9ff"),
        ("वृश्चिक", "Scorpio", "water", "#0d9488", "#f0fdfa"),
        ("धनु", "Sagittarius", "agni", "#ea580c", "#fff7ed"),
        ("मकर", "Capricorn", "earth", "#d97706", "#fefce8"),
        ("कुंभ", "Aquarius", "air", "#0284c7", "#f0f9ff"),
        ("मीन", "Pisces", "water", "#0d9488", "#f0fdfa")
    ]

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" class="astro-chart-svg astro-nakshatra-mandala">',
        '  <defs>',
        '    <linearGradient id="mandalaBg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fffefb"/>',
        '      <stop offset="100%" stop-color="#faf5e8"/>',
        '    </linearGradient>',
        '    <filter id="mandalaShadow" x="-5%" y="-5%" width="110%" height="110%">',
        '      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>',
        '    </filter>',
        '  </defs>',

        f'  <rect x="6" y="6" width="{width-12}" height="{height-12}" rx="16" fill="url(#mandalaBg)" stroke="#c89d3d" stroke-width="2" filter="url(#mandalaShadow)"/>',
        f'  <rect x="12" y="12" width="{width-24}" height="{height-24}" rx="12" fill="none" stroke="#eab308" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>',

        '  <!-- Center Background Rings -->',
        f'  <circle cx="{cx}" cy="{cy}" r="{r_outer}" fill="#ffffff" stroke="#c89d3d" stroke-width="1.8"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="{r_padas}" fill="#fdfbf5" stroke="#eab308" stroke-width="1.2"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="{r_nakshatras}" fill="#ffffff" stroke="#c89d3d" stroke-width="1.5"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="{r_rashis}" fill="#fffdfa" stroke="#854d0e" stroke-width="1.8"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="{r_center}" fill="#fff7ed" stroke="#c89d3d" stroke-width="1.5"/>'
    ]

    # 1. RENDER 12 RASHIS (30 degrees each, Ring from r_center to r_rashis)
    for i in range(12):
        start_deg = i * 30.0 - 90.0
        end_deg = (i + 1) * 30.0 - 90.0
        mid_deg = start_deg + 15.0

        rad_start = math.radians(start_deg)
        x1_in = cx + r_rashis * math.cos(rad_start)
        y1_in = cy + r_rashis * math.sin(rad_start)
        x1_out = cx + r_nakshatras * math.cos(rad_start)
        y1_out = cy + r_nakshatras * math.sin(rad_start)

        name_hi, name_en, elem, border_col, bg_col = rashi_elements[i]
        svg.append(f'  <!-- Dividing Line for Rashi {i+1} -->')
        svg.append(f'  <line x1="{x1_in:.2f}" y1="{y1_in:.2f}" x2="{x1_out:.2f}" y2="{y1_out:.2f}" stroke="{border_col}" stroke-width="1.4"/>')

        # Text label in middle of rashi sector
        rad_mid = math.radians(mid_deg)
        r_mid = (r_rashis + r_nakshatras) / 2.0
        lx = cx + r_mid * math.cos(rad_mid)
        ly = cy + r_mid * math.sin(rad_mid)

        svg.append(f'  <text x="{lx:.2f}" y="{ly - 4:.2f}" font-family="{SVG_FONT_FAMILY}" font-size="10.5" font-weight="900" fill="{border_col}" text-anchor="middle" dominant-baseline="central">{i+1}. {name_hi}</text>')
        svg.append(f'  <text x="{lx:.2f}" y="{ly + 8:.2f}" font-family="{SVG_FONT_FAMILY}" font-size="8" font-weight="600" fill="#64748b" text-anchor="middle" dominant-baseline="central">{name_en} • 30°</text>')

    # 2. RENDER 27 NAKSHATRAS (13°20' = 13.3333° each, Ring from r_nakshatras to r_padas)
    nakshatra_deg_span = 360.0 / 27.0 # 13.33333... degrees
    for i in range(27):
        start_deg = i * nakshatra_deg_span - 90.0
        mid_deg = start_deg + (nakshatra_deg_span / 2.0)

        rad_start = math.radians(start_deg)
        x_in = cx + r_nakshatras * math.cos(rad_start)
        y_in = cy + r_nakshatras * math.sin(rad_start)
        x_out = cx + r_padas * math.cos(rad_start)
        y_out = cy + r_padas * math.sin(rad_start)

        hi_name, en_name, lord_key = nakshatra_names[i]
        lord_info = PLANETS_INFO[lord_key]

        svg.append(f'  <line x1="{x_in:.2f}" y1="{y_in:.2f}" x2="{x_out:.2f}" y2="{y_out:.2f}" stroke="#d97706" stroke-width="1.1"/>')

        # Text label along arc
        rad_mid = math.radians(mid_deg)
        r_mid = (r_nakshatras + r_padas) / 2.0
        lx = cx + r_mid * math.cos(rad_mid)
        ly = cy + r_mid * math.sin(rad_mid)

        # Rotate text radially so it reads cleanly along the arc
        rot_angle = mid_deg + 90.0
        if 90.0 < mid_deg + 90.0 < 270.0:
            rot_angle += 180.0

        svg.append(f'  <g transform="translate({lx:.2f}, {ly:.2f}) rotate({rot_angle:.1f})">')
        svg.append(f'    <text x="0" y="-5" font-family="{SVG_FONT_FAMILY}" font-size="8.8" font-weight="800" fill="{lord_info["color"]}" text-anchor="middle" dominant-baseline="central">{hi_name}</text>')
        svg.append(f'    <text x="0" y="5" font-family="{SVG_FONT_FAMILY}" font-size="7" font-weight="700" fill="{lord_info["color"]}" text-anchor="middle" dominant-baseline="central">स्वामी: {lord_key} • 3.7%</text>')
        svg.append(f'  </g>')

    # 3. RENDER 108 PADAS (3°20' = 3.3333° each, Ring from r_padas to r_outer)
    pada_deg_span = 360.0 / 108.0 # 3.33333... degrees
    for i in range(108):
        start_deg = i * pada_deg_span - 90.0
        rad_start = math.radians(start_deg)
        x_in = cx + r_padas * math.cos(rad_start)
        y_in = cy + r_padas * math.sin(rad_start)
        x_out = cx + r_outer * math.cos(rad_start)
        y_out = cy + r_outer * math.sin(rad_start)

        # Stronger line for nakshatra boundary (every 4th pada)
        is_nak_boundary = (i % 4 == 0)
        str_w = "1.5" if is_nak_boundary else "0.5"
        stroke_c = "#b45309" if is_nak_boundary else "#cbd5e1"

        svg.append(f'  <line x1="{x_in:.2f}" y1="{y_in:.2f}" x2="{x_out:.2f}" y2="{y_out:.2f}" stroke="{stroke_c}" stroke-width="{str_w}"/>')

        # Pada number (1, 2, 3, 4)
        pada_num = (i % 4) + 1
        mid_deg = start_deg + (pada_deg_span / 2.0)
        rad_mid = math.radians(mid_deg)
        r_mid = (r_padas + r_outer) / 2.0
        lx = cx + r_mid * math.cos(rad_mid)
        ly = cy + r_mid * math.sin(rad_mid)

        svg.append(f'  <text x="{lx:.2f}" y="{ly:.2f}" font-family="{SVG_FONT_FAMILY}" font-size="6.8" font-weight="700" fill="#475569" text-anchor="middle" dominant-baseline="central">{pada_num}</text>')

    # 4. Sacred Center Emblem (Yantra / Ganesha / Degree Compass)
    svg.extend([
        '  <!-- Sacred Center Circle (Yantra Halo) -->',
        f'  <circle cx="{cx}" cy="{cy}" r="{r_center * 0.85}" fill="#ffffff" stroke="#c89d3d" stroke-width="1.2"/>',
        f'  <polygon points="{cx},{cy - 28} {cx + 24},{cy + 18} {cx - 24},{cy + 18}" fill="none" stroke="#ea580c" stroke-width="1.2"/>',
        f'  <polygon points="{cx},{cy + 28} {cx + 24},{cy - 18} {cx - 24},{cy - 18}" fill="none" stroke="#2563eb" stroke-width="1.2"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="6" fill="#f59e0b" stroke="#78350f" stroke-width="1"/>',
        f'  <text x="{cx}" y="{cy + 38}" font-family="{SVG_SERIF_FAMILY}" font-size="10" font-weight="900" fill="#78350f" text-anchor="middle">सप्तविंशति नक्षत्र चक्र</text>',
        f'  <text x="{cx}" y="{cy + 50}" font-family="{SVG_FONT_FAMILY}" font-size="7.5" fill="#92400e" text-anchor="middle">360° = 27 नक्षत्र • 108 पद</text>',
        f'  <text x="{cx}" y="{cy + 61}" font-family="{SVG_FONT_FAMILY}" font-size="7" fill="#64748b" text-anchor="middle">1 पद = 3°20\' (0.926%)</text>',

        '</svg>'
    ])

    return "\n".join(svg)


# ==============================================================================
# 5. BHAVA KARAKATVA & PLANETARY DOMINANCE (द्वादश भाव कारकत्व चक्र)
# ==============================================================================
def generate_bhava_karaka_diamond_chart(width: int = 560, height: int = 700) -> str:
    """
    Renders an authoritative North Indian Diamond Kundali detailing the
    Classical Sthira Karakas (Fixed Significators) for all 12 Houses.
    """
    karakas = {
        1:  {"graha": "Su", "name": "तनु भाव (Body &amp; Soul)", "karaka_title": "सूर्य (Sun)", "sig": "आत्मबल, तेज, देह, आरोग्यता"},
        2:  {"graha": "Ju", "name": "धन भाव (Wealth &amp; Speech)", "karaka_title": "गुरु (Jupiter)", "sig": "संचित कोष, वाणी, कुटुंब संस्कार"},
        3:  {"graha": "Ma", "name": "सहज भाव (Courage &amp; Siblings)", "karaka_title": "मंगल (Mars)", "sig": "शौर्य, पराक्रम, अनुज भ्राता, उद्यम"},
        4:  {"graha": "Mo", "name": "सुख भाव (Mother &amp; Vehicles)", "karaka_title": "चन्द्र व शुक्र", "sig": "मातृ सुख, गृह, वाहन, मानसिक शांति"},
        5:  {"graha": "Ju", "name": "पुत्र भाव (Wisdom &amp; Children)", "karaka_title": "गुरु (Jupiter)", "sig": "संतति, पूर्वपुण्य, मेधा, मंत्र साधना"},
        6:  {"graha": "Sa", "name": "रिपु भाव (Debts &amp; Disease)", "karaka_title": "शनि व मंगल", "sig": "शत्रु विजय, रोग निदान, ऋण मुक्ति"},
        7:  {"graha": "Ve", "name": "जाया भाव (Spouse &amp; Trade)", "karaka_title": "शुक्र (Venus)", "sig": "जीवनसाथी, काम सुख, व्यापार साझेदारी"},
        8:  {"graha": "Sa", "name": "आयु भाव (Longevity &amp; Occult)", "karaka_title": "शनि (Saturn)", "sig": "दीर्घायु, गूढ़ विद्या, आकस्मिक धन"},
        9:  {"graha": "Ju", "name": "भाग्य भाव (Dharma &amp; Guru)", "karaka_title": "गुरु व सूर्य", "sig": "धर्म, पिता, ईश्वरीय कृपा, तीर्थाटन"},
        10: {"graha": "Su", "name": "कर्म भाव (Career &amp; Authority)", "karaka_title": "सूर्य/बुध/शनि", "sig": "राज्य पद, प्रतिष्ठा, आजीविका शिखर"},
        11: {"graha": "Ju", "name": "लाभ भाव (Income &amp; Gains)", "karaka_title": "गुरु (Jupiter)", "sig": "सर्व कामना सिद्धि, प्रचुर धनोपार्जन"},
        12: {"graha": "Sa", "name": "व्यय भाव (Moksha &amp; Foreign)", "karaka_title": "शनि व केतु", "sig": "मोक्ष, विसर्जन, विदेश वास, एकांत"}
    }

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" class="astro-chart-svg astro-karaka-chart">',
        '  <defs>',
        '    <linearGradient id="karakaBg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fffefd"/>',
        '      <stop offset="100%" stop-color="#faf5e6"/>',
        '    </linearGradient>',
        '  </defs>',

        f'  <rect x="6" y="6" width="{width-12}" height="{height-12}" rx="12" fill="url(#karakaBg)" stroke="#c89d3d" stroke-width="2"/>',
        f'  <rect x="12" y="12" width="{width-24}" height="{height-24}" rx="8" fill="none" stroke="#eab308" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>',

        '  <!-- Header Banner -->',
        f'  <rect x="24" y="20" width="{width-48}" height="66" rx="6" fill="#ffffff" stroke="#c89d3d" stroke-width="1.2"/>',
        f'  <text x="{width//2}" y="42" font-family="{SVG_SERIF_FAMILY}" font-size="16" font-weight="800" fill="#78350f" text-anchor="middle">द्वादश भाव कारकत्व व स्थिर ग्रह चक्र</text>',
        f'  <text x="{width//2}" y="60" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="600" fill="#b45309" text-anchor="middle">महर्षि पराशर प्रतिपादित 12 भावों के नैसर्गिक स्थिर कारक (Sthira Karakas)</text>',
        f'  <text x="{width//2}" y="74" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#78716c" text-anchor="middle">भाव बली होने पर भी कारक के पीड़ित होने से उस जीवन-क्षेत्र में न्यूनता आती है</text>',

        '  <!-- Diamond Kundali (X: 30 to 530, Y: 96 to 596) -->',
        '  <g transform="translate(10, 0)">'
    ]

    # Draw house polygons with authentic planet background tint
    for h in range(1, 13):
        poly = HOUSE_POLYGONS[h]
        k = karakas[h]
        p_info = PLANETS_INFO[k["graha"]]

        svg.append(f'    <polygon points="{poly}" fill="{p_info["bg"]}" stroke="{p_info["border"]}" stroke-width="1.8"/>')

    # Accent Lines
    svg.extend([
        '    <polygon points="270,100 520,350 270,600 20,350" fill="none" stroke="#78350f" stroke-width="1.2" opacity="0.65"/>',
        '    <line x1="20" y1="100" x2="520" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <line x1="520" y1="100" x2="20" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <circle cx="270" cy="350" r="4.5" fill="#f59e0b" stroke="#78350f" stroke-width="1.5"/>'
    ])

    # House Labels
    for h in range(1, 13):
        cx, cy = HOUSE_CENTROIDS[h]
        k = karakas[h]
        p_info = PLANETS_INFO[k["graha"]]
        y_shift = -18 if h in [1, 4, 7, 10] else -14

        svg.append(f'    <!-- House {h} -->')
        svg.append(f'    <text x="{cx}" y="{cy + y_shift}" font-family="{SVG_FONT_FAMILY}" font-size="11.5" font-weight="900" fill="{p_info["color"]}" text-anchor="middle">भाव {h} • {k["karaka_title"]}</text>')
        svg.append(f'    <text x="{cx}" y="{cy + y_shift + 14}" font-family="{SVG_FONT_FAMILY}" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">{k["name"]}</text>')
        svg.append(f'    <text x="{cx}" y="{cy + y_shift + 26}" font-family="{SVG_FONT_FAMILY}" font-size="8.5" fill="#475569" text-anchor="middle">{k["sig"]}</text>')

    svg.append('  </g>')

    # Footer Card explaining Karaka Principle
    svg.extend([
        f'  <g transform="translate(24, 608)">',
        f'    <rect x="0" y="0" width="{width-48}" height="74" rx="6" fill="#fefce8" stroke="#ca8a04" stroke-width="1.2"/>',
        f'    <text x="18" y="20" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="800" fill="#713f12">भाव-भावेश-कारक त्रिसूत्री सिद्धांत (The Triple Pillars of Prediction)</text>',
        f'    <text x="18" y="37" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#713f12">1. भाव (House): घटना का मंच है। भाव पर शुभ ग्रहों का प्रभाव उसे पुष्ट करता है।</text>',
        f'    <text x="18" y="51" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#713f12">2. भावेश (Lord): घटना का नियंत्रक है। भावेश केन्द्र या त्रिकोण में होने पर पूर्ण सामर्थ्य प्रदान करता है।</text>',
        f'    <text x="18" y="65" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#713f12">3. कारक (Significator): घटना की प्राणवायु है। यदि भावेश बली हो किंतु कारक अस्त या नीच हो, तो सुख अधूरा रहता है।</text>',
        f'  </g>',

        '</svg>'
    ])

    return "\n".join(svg)



# ==============================================================================
# 6. KALPURUSH BHAVA CLASSIFICATION MASTER DIAMOND CHART (कालपुरुष भाव वर्गीकरण महाचक्र)
# ==============================================================================

def generate_kalpurush_bhavas_diamond_chart(width: int = 560, height: int = 770) -> str:
    """
    Renders an authoritative Kalpurusha Kundali (Mesha / Aries Lagna) illustrating all
    12 Bhavas categorized into Kendra, Trikona, Upachaya, Trik (Dusthana), and
    Maraka houses with complete significations, planetary rulers, and exaltations
    directly inside each diamond and triangle.
    """
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" class="astro-chart-svg astro-kalpurush-bhavas-chart">',
        '  <defs>',
        '    <style>',
        '      @import url("https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700;800;900&amp;family=Noto+Serif+Devanagari:wght@700;800&amp;display=swap");',
        '    </style>',
        '    <linearGradient id="kpPlateBg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fffefc"/>',
        '      <stop offset="100%" stop-color="#faf5ea"/>',
        '    </linearGradient>',
        '    <!-- Distinct Category Gradients -->',
        '    <linearGradient id="kpGradKendraTrikona" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="kpGradKendra" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#eff6ff" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#dbeafe" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="kpGradTrikona" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ecfdf5" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#d1fae5" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="kpGradUpachaya" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#e0f2fe" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#bae6fd" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="kpGradMaraka" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ffe4e6" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#fecdd3" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="kpGradTrik" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fdf2f8" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#fce7f3" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="kpGradTrikDeep" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#faf5ff" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#f3e8ff" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <filter id="kpShadow" x="-5%" y="-5%" width="110%" height="110%">',
        '      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.08"/>',
        '    </filter>',
        '  </defs>',

        '  <!-- Outer Plate Frame -->',
        f'  <rect x="6" y="6" width="{width-12}" height="{height-12}" rx="12" fill="url(#kpPlateBg)" stroke="#b45309" stroke-width="2" filter="url(#kpShadow)"/>',
        f'  <rect x="12" y="12" width="{width-24}" height="{height-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>',

        '  <!-- Top Header Banner -->',
        f'  <rect x="24" y="20" width="{width-48}" height="66" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.2"/>',
        f'  <text x="{width//2}" y="42" font-family="{SVG_SERIF_FAMILY}" font-size="16" font-weight="800" fill="#78350f" text-anchor="middle">कालपुरुष कुण्डली भाव वर्गीकरण महाचक्र</text>',
        f'  <text x="{width//2}" y="60" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="600" fill="#b45309" text-anchor="middle">केन्द्र (1, 4, 7, 10) • त्रिकोण (1, 5, 9) • उपचय (3, 6, 10, 11) • त्रिक (6, 8, 12) • मारक (2, 7)</text>',
        f'  <text x="{width//2}" y="74" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#78716c" text-anchor="middle">मेष लग्न विन्यास • महर्षि पाराशर प्रतिपादित भाव व्यवस्था, प्राकृतिक कारकत्व व फलित मर्म</text>',

        '  <!-- Diamond Kundali Outer Frame (X: 30 to 530, Y: 96 to 596) -->',
        '  <g transform="translate(10, 0)">'
    ]

    # Map house polygons with styles
    house_styles = {
        1:  ("url(#kpGradKendraTrikona)", "#b45309", 2.6), # Kendra + Trikona
        2:  ("url(#kpGradMaraka)",        "#e11d48", 1.8), # Maraka 2
        3:  ("url(#kpGradUpachaya)",      "#0284c7", 1.8), # Upachaya 3
        4:  ("url(#kpGradKendra)",        "#1d4ed8", 2.2), # Kendra 4 (Vishnu)
        5:  ("url(#kpGradTrikona)",       "#059669", 2.2), # Trikona 5 (Lakshmi)
        6:  ("url(#kpGradTrik)",          "#9f1239", 1.8), # Trik 6 + Upachaya
        7:  ("url(#kpGradMaraka)",        "#dc2626", 2.2), # Kendra 7 + Primary Maraka
        8:  ("url(#kpGradTrikDeep)",      "#7e22ce", 1.8), # Major Trik 8
        9:  ("url(#kpGradTrikona)",       "#047857", 2.4), # Supreme Trikona 9
        10: ("url(#kpGradKendraTrikona)", "#d97706", 2.4), # Supreme Kendra 10 + Upachaya
        11: ("url(#kpGradUpachaya)",      "#4338ca", 2.0), # Supreme Upachaya 11
        12: ("url(#kpGradTrik)",          "#9f1239", 1.8)  # Trik 12 (Moksha)
    }

    for h in range(1, 13):
        poly = HOUSE_POLYGONS[h]
        fill, stroke, sw = house_styles[h]
        svg.append(f'    <polygon points="{poly}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    # Accent Crossing Lines & Center Dot
    svg.extend([
        '    <polygon points="270,100 520,350 270,600 20,350" fill="none" stroke="#78350f" stroke-width="1.2" opacity="0.65"/>',
        '    <line x1="20" y1="100" x2="520" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <line x1="520" y1="100" x2="20" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <circle cx="270" cy="350" r="4.5" fill="#f59e0b" stroke="#78350f" stroke-width="1.5"/>'
    ])

    # Rashi Numbers on Crossing Points
    rashi_coords = {
        1: (270, 318), 2: (200, 128), 3: (55, 275), 4: (230, 350),
        5: (55, 420), 6: (200, 570), 7: (270, 380), 8: (340, 570),
        9: (485, 420), 10: (310, 350), 11: (485, 275), 12: (340, 128)
    }
    for h, (rx, ry) in rashi_coords.items():
        svg.append(f'    <!-- Rashi {h} Badge -->')
        svg.append(f'    <circle cx="{rx}" cy="{ry}" r="10" fill="#ffffff" stroke="#78350f" stroke-width="1.2"/>')
        svg.append(f'    <text x="{rx}" y="{ry + 3.5}" font-family="{SVG_FONT_FAMILY}" font-size="10.5" font-weight="900" fill="#78350f" text-anchor="middle">{h}</text>')

    # Detailed House Annotations inside Centroids
    house_annotations = {
        1: {
            "title": "भाव 1 • तनु (Lagna)",
            "title_fill": "#9a3412",
            "tag": "केन्द्र व त्रिकोण (सर्वोच्च)",
            "tag_bg": "#fef3c7",
            "tag_fill": "#b45309",
            "sig": "देह • आत्मबल • वर्ण • स्वास्थ्य",
            "ruler": "मंगल (स्वराशि) • सूर्य (उच्च 10°)",
            "y_offsets": (-26, -11, 7, 23)
        },
        2: {
            "title": "भाव 2 • धन भाव",
            "title_fill": "#9f1239",
            "tag": "द्वितीय मारक भाव",
            "tag_bg": "#ffe4e6",
            "tag_fill": "#be123c",
            "sig": "संचित धन • कुटुंब • वाणी",
            "ruler": "शुक्र (स्व) • चन्द्र (उच्च 3°)",
            "y_offsets": (-18, -4, 10, 24)
        },
        3: {
            "title": "भाव 3 • सहज",
            "title_fill": "#075985",
            "tag": "प्रथम उपचय भाव",
            "tag_bg": "#e0f2fe",
            "tag_fill": "#0284c7",
            "sig": "पराक्रम • साहस • अनुज",
            "ruler": "बुध (स्व) • पुरुषार्थ साधन",
            "y_offsets": (-18, -4, 10, 24)
        },
        4: {
            "title": "भाव 4 • सुख (विष्णु)",
            "title_fill": "#1e3a8a",
            "tag": "केन्द्र भाव (चतुर्थ केन्द्र)",
            "tag_bg": "#eff6ff",
            "tag_fill": "#1d4ed8",
            "sig": "माता • गृह • भूमि • वाहन • मन",
            "ruler": "चन्द्र (स्व) • गुरु (उच्च 5°)",
            "y_offsets": (-26, -11, 7, 23)
        },
        5: {
            "title": "भाव 5 • पुत्र/धी",
            "title_fill": "#064e3b",
            "tag": "त्रिकोण भाव (लक्ष्मी)",
            "tag_bg": "#ecfdf5",
            "tag_fill": "#047857",
            "sig": "संतान • पूर्वपुण्य • मेधा",
            "ruler": "सूर्य (स्व) • मंत्र साधना",
            "y_offsets": (-18, -4, 10, 24)
        },
        6: {
            "title": "भाव 6 • शत्रु/रोग",
            "title_fill": "#881337",
            "tag": "त्रिक (दुःस्थान) + उपचय",
            "tag_bg": "#fdf2f8",
            "tag_fill": "#9f1239",
            "sig": "रोग • ऋण • शत्रु • सेवा",
            "ruler": "बुध (उच्च 15°) • षडरिपु जय",
            "y_offsets": (-18, -4, 10, 24)
        },
        7: {
            "title": "भाव 7 • जाया (कलत्र)",
            "title_fill": "#7f1d1d",
            "tag": "केन्द्र व प्रबल मारक भाव",
            "tag_bg": "#fee2e2",
            "tag_fill": "#dc2626",
            "sig": "दांपत्य • साझेदारी • व्यापार",
            "ruler": "शुक्र (स्व) • शनि (उच्च 20°)",
            "y_offsets": (-26, -11, 7, 23)
        },
        8: {
            "title": "भाव 8 • रन्ध्र भाव",
            "title_fill": "#4c1d95",
            "tag": "प्रबल त्रिक (घोर दुःस्थान)",
            "tag_bg": "#faf5ff",
            "tag_fill": "#7e22ce",
            "sig": "आयु • मृत्यु • गुप्त ज्ञान",
            "ruler": "मंगल (स्व) • गूढ़ परिवर्तन",
            "y_offsets": (-18, -4, 10, 24)
        },
        9: {
            "title": "भाव 9 • भाग्य/धर्म",
            "title_fill": "#064e3b",
            "tag": "सर्वोच्च त्रिकोण (लक्ष्मी)",
            "tag_bg": "#d1fae5",
            "tag_fill": "#059669",
            "sig": "धर्म • गुरु • पिता • तीर्थ",
            "ruler": "गुरु (स्व) • ईश्वरीय अनुग्रह",
            "y_offsets": (-18, -4, 10, 24)
        },
        10: {
            "title": "भाव 10 • कर्म (विष्णु)",
            "title_fill": "#78350f",
            "tag": "सर्वोच्च केन्द्र व उपचय",
            "tag_bg": "#fef3c7",
            "tag_fill": "#b45309",
            "sig": "राज्य पद • आजीविका • सत्ता",
            "ruler": "शनि (स्व) • मंगल (उच्च 28°)",
            "y_offsets": (-26, -11, 7, 23)
        },
        11: {
            "title": "भाव 11 • लाभ भाव",
            "title_fill": "#312e81",
            "tag": "सर्वोत्तम उपचय भाव",
            "tag_bg": "#e0e7ff",
            "tag_fill": "#4338ca",
            "sig": "आय • सर्वाभीष्ट सिद्धि",
            "ruler": "शनि (स्व) • पूर्ण मनोरथ",
            "y_offsets": (-18, -4, 10, 24)
        },
        12: {
            "title": "भाव 12 • व्यय/मोक्ष",
            "title_fill": "#701a75",
            "tag": "त्रिक भाव (मोक्ष स्थान)",
            "tag_bg": "#fdf2f8",
            "tag_fill": "#9f1239",
            "sig": "व्यय • मोक्ष • विदेश • शयन",
            "ruler": "गुरु (स्व) • शुक्र (उच्च 27°)",
            "y_offsets": (-18, -4, 10, 24)
        }
    }

    for h in range(1, 13):
        cx, cy = HOUSE_CENTROIDS[h]
        ann = house_annotations[h]
        y1, y2, y3, y4 = ann["y_offsets"]
        is_diamond = h in [1, 4, 7, 10]
        font_main = "11.5" if is_diamond else "10.0"
        font_sub = "8.8" if is_diamond else "7.8"
        font_ruler = "8.5" if is_diamond else "7.5"

        svg.append(f'    <!-- House {h} Text Plate -->')
        svg.append(f'    <text x="{cx}" y="{cy + y1}" font-family="{SVG_FONT_FAMILY}" font-size="{font_main}" font-weight="900" fill="{ann["title_fill"]}" text-anchor="middle">{ann["title"]}</text>')
        svg.append(f'    <text x="{cx}" y="{cy + y2}" font-family="{SVG_FONT_FAMILY}" font-size="{font_sub}" font-weight="800" fill="{ann["tag_fill"]}" text-anchor="middle">{ann["tag"]}</text>')
        svg.append(f'    <text x="{cx}" y="{cy + y3}" font-family="{SVG_FONT_FAMILY}" font-size="{font_sub}" font-weight="600" fill="#1e293b" text-anchor="middle">{ann["sig"]}</text>')
        svg.append(f'    <text x="{cx}" y="{cy + y4}" font-family="{SVG_FONT_FAMILY}" font-size="{font_ruler}" font-weight="700" fill="#854d0e" text-anchor="middle">{ann["ruler"]}</text>')

    svg.append('  </g>')

    # -------------------------------------------------------------
    # 5 Structured Categorization Cards at the Bottom
    # -------------------------------------------------------------
    svg.append('  <!-- 5 Functional Classification Cards -->')
    cards_data = [
        (18,  "केन्द्र (1, 4, 7, 10)", "विष्णु स्थान", "देह, सुख, दांपत्य, कर्म", "#eff6ff", "#2563eb", "#1e3a8a"),
        (124, "त्रिकोण (1, 5, 9)",    "लक्ष्मी स्थान", "धर्म, धी, भाग्य, पुण्य", "#ecfdf5", "#059669", "#064e3b"),
        (230, "उपचय (3, 6, 10, 11)", "सतत पुरुषार्थ", "साहस, विजय, सत्ता, लाभ", "#e0f2fe", "#0284c7", "#075985"),
        (336, "त्रिक (6, 8, 12)",     "दुःस्थान / संकट", "रोग, ऋण, मृत्यु, मोक्ष", "#fdf2f8", "#be185d", "#701a75"),
        (442, "मारक (2, 7)",         "जीवन मर्यादा", "धन, कुटुंब, जाया, आयु अंत", "#ffe4e6", "#e11d48", "#9f1239")
    ]

    for x_pos, c_title, c_role, c_desc, bg_col, border_col, text_col in cards_data:
        svg.append(f'  <g transform="translate({x_pos}, 606)">')
        svg.append(f'    <rect x="0" y="0" width="100" height="66" rx="6" fill="{bg_col}" stroke="{border_col}" stroke-width="1.2"/>')
        svg.append(f'    <text x="50" y="18" font-family="{SVG_FONT_FAMILY}" font-size="9.0" font-weight="900" fill="{text_col}" text-anchor="middle">{c_title}</text>')
        svg.append(f'    <text x="50" y="34" font-family="{SVG_FONT_FAMILY}" font-size="8.5" font-weight="700" fill="{border_col}" text-anchor="middle">{c_role}</text>')
        svg.append(f'    <text x="50" y="50" font-family="{SVG_FONT_FAMILY}" font-size="7.5" font-weight="600" fill="#334155" text-anchor="middle">{c_desc}</text>')
        svg.append('  </g>')

    # Bottom Master Shloka / Principle Banner
    svg.extend([
        f'  <g transform="translate(18, 680)">',
        f'    <rect x="0" y="0" width="{width-36}" height="76" rx="6" fill="#fffbeb" stroke="#b45309" stroke-width="1.2"/>',
        f'    <text x="18" y="20" font-family="{SVG_SERIF_FAMILY}" font-size="11" font-weight="800" fill="#78350f">महर्षि पराशर फलित सार • पाराशरी भाव वर्गीकरण सूत्र</text>',
        f'    <text x="18" y="37" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="600" fill="#78350f">1. केन्द्र (विष्णु) एवं त्रिकोण (लक्ष्मी) का युति/दृष्टि संबंध जन्मकुण्डली में सर्वोच्च राजयोग का निर्माण करता है।</text>',
        f'    <text x="18" y="52" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="600" fill="#78350f">2. उपचय भावों (3, 6, 10, 11) में क्रूर ग्रह (शनि, मंगल, राहु) कालान्तर में प्रचंड पुरुषार्थ एवं सर्व-शत्रु विजय प्रदान करते हैं।</text>',
        f'    <text x="18" y="67" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="600" fill="#78350f">3. त्रिक (6, 8, 12) दुःस्थान हैं; इनके स्वामी परस्पर त्रिक में ही बैठें तो &quot;हर्ष, सरल, विमल&quot; नामक विपरीत राजयोग बनता है।</text>',
        f'  </g>',

        '</svg>'
    ])

    return "\n".join(svg)


# ==============================================================================
# 7. PANCHA MAHAPURUSHA & GAJAKESARI RAJYOGA MASTER CHART
# ==============================================================================

def generate_panch_mahapurush_rajyogas_chart(width: int = 560, height: int = 770) -> str:
    """
    Renders an authoritative North Indian Diamond Kundali (Cancer / Karka Lagna)
    illustrating the 5 Imperial Mahapurusha Yogas (Ruchaka, Bhadra, Hamsa, Malavya, Sasa)
    plus Gajakesari Rajyoga and Budhaditya Yoga right inside the Bhavas with
    exalted / own sign placements, planetary degrees, and comprehensive explanatory cards.
    """
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" class="astro-chart-svg astro-rajayogas-master-chart">',
        '  <defs>',
        '    <style>',
        '      @import url("https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700;800;900&amp;family=Noto+Serif+Devanagari:wght@700;800&amp;display=swap");',
        '    </style>',
        '    <linearGradient id="ryPlateBg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fffefc"/>',
        '      <stop offset="100%" stop-color="#faf5e8"/>',
        '    </linearGradient>',
        '    <linearGradient id="ryGradGold" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="ryGradRuby" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fee2e2" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#fecaca" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="ryGradEmerald" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ecfdf5" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#d1fae5" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="ryGradRose" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fdf2f8" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#fce7f3" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <linearGradient id="ryGradAzure" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#eff6ff" stop-opacity="0.96"/>',
        '      <stop offset="100%" stop-color="#dbeafe" stop-opacity="0.96"/>',
        '    </linearGradient>',
        '    <filter id="ryShadow" x="-5%" y="-5%" width="110%" height="110%">',
        '      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.08"/>',
        '    </filter>',
        '  </defs>',

        '  <!-- Outer Plate Frame -->',
        f'  <rect x="6" y="6" width="{width-12}" height="{height-12}" rx="12" fill="url(#ryPlateBg)" stroke="#b45309" stroke-width="2" filter="url(#ryShadow)"/>',
        f'  <rect x="12" y="12" width="{width-24}" height="{height-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>',

        '  <!-- Top Header Banner -->',
        f'  <rect x="24" y="20" width="{width-48}" height="66" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.2"/>',
        f'  <text x="{width//2}" y="42" font-family="{SVG_SERIF_FAMILY}" font-size="16" font-weight="800" fill="#78350f" text-anchor="middle">पंच महापुरुष एवं गजकेसरी राजयोग चक्र</text>',
        f'  <text x="{width//2}" y="60" font-family="{SVG_FONT_FAMILY}" font-size="11" font-weight="600" fill="#b45309" text-anchor="middle">हंस (गुरु) • मालव्य (शुक्र) • रुचक (मंगल) • भद्र (बुध) • शश (शनि) • गजकेसरी (गुरु+चन्द्र)</text>',
        f'  <text x="{width//2}" y="74" font-family="{SVG_FONT_FAMILY}" font-size="9" fill="#78716c" text-anchor="middle">कर्क लग्न विन्यास • केन्द्र-त्रिकोण में उच्च व स्वराशि ग्रहों का अखंड साम्राज्य योग</text>',

        '  <!-- Diamond Kundali Outer Frame (X: 30 to 530, Y: 96 to 596) -->',
        '  <g transform="translate(10, 0)">'
    ]

    # Cancer Ascendant (कर्क लग्न): House 1 is sign 4, House 2 is sign 5, etc.
    karka_styles = {
        1:  ("url(#ryGradGold)",    "#b45309", 2.6), # Hamsa + Gaja Kesari (Ju Exalted + Mo Own)
        2:  ("#fffdf7",              "#cbd5e1", 1.2), # House 2 (Leo)
        3:  ("#fffdf7",              "#cbd5e1", 1.2), # House 3 (Virgo)
        4:  ("url(#ryGradRose)",    "#db2777", 2.4), # Malavya (Ve Own) + Sasa (Sa Exalted)
        5:  ("#f0fdf4",              "#86efac", 1.4), # House 5 (Scorpio - Trikona)
        6:  ("url(#ryGradEmerald)", "#059669", 1.8), # Bhadra (Me Exalted in Virgo)
        7:  ("url(#ryGradRuby)",    "#dc2626", 2.4), # Ruchaka (Ma Exalted in Capricorn)
        8:  ("#fffdf7",              "#cbd5e1", 1.2), # House 8 (Aquarius)
        9:  ("#f0fdf4",              "#86efac", 1.4), # House 9 (Pisces - Trikona)
        10: ("url(#ryGradAzure)",   "#2563eb", 2.4), # Budhaditya (Su Exalted + Me) in Aries
        11: ("#f8fafc",              "#cbd5e1", 1.2), # House 11 (Taurus)
        12: ("#fffdf7",              "#cbd5e1", 1.2)  # House 12 (Gemini)
    }

    for h in range(1, 13):
        poly = HOUSE_POLYGONS[h]
        fill, stroke, sw = karka_styles[h]
        svg.append(f'    <polygon points="{poly}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    # Accent Crossing Lines & Center Dot
    svg.extend([
        '    <polygon points="270,100 520,350 270,600 20,350" fill="none" stroke="#78350f" stroke-width="1.2" opacity="0.65"/>',
        '    <line x1="20" y1="100" x2="520" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <line x1="520" y1="100" x2="20" y2="600" stroke="#78350f" stroke-width="1.0" opacity="0.5"/>',
        '    <circle cx="270" cy="350" r="4.5" fill="#f59e0b" stroke="#78350f" stroke-width="1.5"/>'
    ])

    # Rashi Numbers for Cancer Ascendant: 1=4, 2=5, 3=6, 4=7, 5=8, 6=9, 7=10, 8=11, 9=12, 10=1, 11=2, 12=3
    rashi_nums = {
        1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 10, 8: 11, 9: 12, 10: 1, 11: 2, 12: 3
    }
    rashi_coords = {
        1: (270, 318), 2: (200, 128), 3: (55, 275), 4: (230, 350),
        5: (55, 420), 6: (200, 570), 7: (270, 380), 8: (340, 570),
        9: (485, 420), 10: (310, 350), 11: (485, 275), 12: (340, 128)
    }
    for h, (rx, ry) in rashi_coords.items():
        svg.append(f'    <circle cx="{rx}" cy="{ry}" r="10" fill="#ffffff" stroke="#78350f" stroke-width="1.2"/>')
        svg.append(f'    <text x="{rx}" y="{ry + 3.5}" font-family="{SVG_FONT_FAMILY}" font-size="10" font-weight="900" fill="#78350f" text-anchor="middle">{rashi_nums[h]}</text>')

    # Major Yogas Placements inside Bhavas
    # House 1 (Lagna): Hamsa + Gaja Kesari
    cx1, cy1 = HOUSE_CENTROIDS[1]
    svg.extend([
        f'    <text x="{cx1}" y="{cy1 - 28}" font-family="{SVG_FONT_FAMILY}" font-size="12" font-weight="900" fill="#78350f" text-anchor="middle">भाव 1 • हंस व गजकेसरी योग</text>',
        f'    <text x="{cx1}" y="{cy1 - 12}" font-family="{SVG_FONT_FAMILY}" font-size="9.5" font-weight="800" fill="#b45309" text-anchor="middle">गुरु (Jupiter) 05°20′ [उच्च]</text>',
        f'    <text x="{cx1}" y="{cy1 + 4}" font-family="{SVG_FONT_FAMILY}" font-size="9.5" font-weight="800" fill="#475569" text-anchor="middle">चन्द्र (Moon) 18°40′ [स्वराशि]</text>',
        f'    <text x="{cx1}" y="{cy1 + 22}" font-family="{SVG_FONT_FAMILY}" font-size="8.5" font-weight="600" fill="#92400e" text-anchor="middle">अखंड साम्राज्य • सात्विक कीर्ति • प्रखर प्रज्ञा</text>'
    ])

    # House 4 (Sukha): Malavya + Sasa
    cx4, cy4 = HOUSE_CENTROIDS[4]
    svg.extend([
        f'    <text x="{cx4}" y="{cy4 - 24}" font-family="{SVG_FONT_FAMILY}" font-size="11.5" font-weight="900" fill="#9d174d" text-anchor="middle">भाव 4 • मालव्य व शश योग</text>',
        f'    <text x="{cx4}" y="{cy4 - 9}" font-family="{SVG_FONT_FAMILY}" font-size="9.5" font-weight="800" fill="#be185d" text-anchor="middle">शुक्र (Venus) 27°15′ [स्वराशि]</text>',
        f'    <text x="{cx4}" y="{cy4 + 7}" font-family="{SVG_FONT_FAMILY}" font-size="9.0" font-weight="800" fill="#1d4ed8" text-anchor="middle">शनि 20°00′ [उच्च क्षेत्र संबंध]</text>',
        f'    <text x="{cx4}" y="{cy4 + 23}" font-family="{SVG_FONT_FAMILY}" font-size="8.5" font-weight="600" fill="#831843" text-anchor="middle">विपुल ऐश्वर्य • कला • राजसी वाहन</text>'
    ])

    # House 7 (Jaya): Ruchaka Yoga (Mars Exalted)
    cx7, cy7 = HOUSE_CENTROIDS[7]
    svg.extend([
        f'    <text x="{cx7}" y="{cy7 - 26}" font-family="{SVG_FONT_FAMILY}" font-size="12" font-weight="900" fill="#991b1b" text-anchor="middle">भाव 7 • रुचक महापुरुष योग</text>',
        f'    <text x="{cx7}" y="{cy7 - 10}" font-family="{SVG_FONT_FAMILY}" font-size="10" font-weight="800" fill="#dc2626" text-anchor="middle">मंगल (Mars) 28°00′ [परम उच्च]</text>',
        f'    <text x="{cx7}" y="{cy7 + 8}" font-family="{SVG_FONT_FAMILY}" font-size="8.8" font-weight="700" fill="#7f1d1d" text-anchor="middle">मकर राशि (10) केन्द्र स्थित</text>',
        f'    <text x="{cx7}" y="{cy7 + 24}" font-family="{SVG_FONT_FAMILY}" font-size="8.5" font-weight="600" fill="#991b1b" text-anchor="middle">अदम्य पराक्रम • सेनापति तुल्य प्रभुत्व • अजेय शौर्य</text>'
    ])

    # House 10 (Karma): Budhaditya & Sun Exalted
    cx10, cy10 = HOUSE_CENTROIDS[10]
    svg.extend([
        f'    <text x="{cx10}" y="{cy10 - 24}" font-family="{SVG_FONT_FAMILY}" font-size="11.5" font-weight="900" fill="#1e3a8a" text-anchor="middle">भाव 10 • बुधादित्य योग</text>',
        f'    <text x="{cx10}" y="{cy10 - 9}" font-family="{SVG_FONT_FAMILY}" font-size="9.5" font-weight="800" fill="#c2410c" text-anchor="middle">सूर्य (Sun) 06°10′ [परम उच्च]</text>',
        f'    <text x="{cx10}" y="{cy10 + 7}" font-family="{SVG_FONT_FAMILY}" font-size="9.5" font-weight="800" fill="#047857" text-anchor="middle">बुध (Mercury) 12°50′ [मित्र]</text>',
        f'    <text x="{cx10}" y="{cy10 + 23}" font-family="{SVG_FONT_FAMILY}" font-size="8.5" font-weight="600" fill="#1e40af" text-anchor="middle">सर्वोच्च प्रशासनिक पद • अमर कीर्ति</text>'
    ])

    # House 6: Bhadra Yoga Principle Note (Mercury Exalted in Virgo)
    cx6, cy6 = HOUSE_CENTROIDS[6]
    svg.extend([
        f'    <text x="{cx6}" y="{cy6 - 12}" font-family="{SVG_FONT_FAMILY}" font-size="9.5" font-weight="900" fill="#047857" text-anchor="middle">भद्र योग सूत्र</text>',
        f'    <text x="{cx6}" y="{cy6 + 2}" font-family="{SVG_FONT_FAMILY}" font-size="8.0" font-weight="700" fill="#065f46" text-anchor="middle">बुध कन्या (6) में स्वराशि</text>',
        f'    <text x="{cx6}" y="{cy6 + 16}" font-family="{SVG_FONT_FAMILY}" font-size="7.5" fill="#334155" text-anchor="middle">कुशाग्र वाणिज्य प्रज्ञा</text>'
    ])

    svg.append('  </g>')

    # -------------------------------------------------------------
    # 6 Structured Imperial Raja Yoga Cards at the Bottom
    # -------------------------------------------------------------
    svg.append('  <!-- 6 Imperial Raja Yoga Cards -->')
    yogas_data = [
        (18,  "रुचक (मंगल)", "मेष/वृश्चिक/मकर केन्द्र", "शौर्य, भूमि, सेनाधिपति", "#fee2e2", "#ef4444", "#991b1b"),
        (104, "भद्र (बुध)",   "मिथुन/कन्या केन्द्र",   "कुशाग्र मेधा, वाक्पटुता", "#ecfdf5", "#10b981", "#064e3b"),
        (190, "हंस (गुरु)",   "कर्क/धनु/मीन केन्द्र",   "सात्विक विवेक, राज्य प्रतिष्ठा", "#fef3c7", "#f59e0b", "#78350f"),
        (276, "मालव्य (शुक्र)", "वृषभ/तुला/मीन केन्द्र", "कला, ऐश्वर्य, वाहन, सौंदर्य", "#fdf2f8", "#f43f5e", "#9d174d"),
        (362, "शश (शनि)",    "तुला/मकर/कुंभ केन्द्र",  "जननायक, कूटनीति, संगठन", "#eff6ff", "#3b82f6", "#1e3a8a"),
        (448, "गजकेसरी (गुरु+चन्द्र)", "चन्द्र से केन्द्र में गुरु", "सिंह समान शौर्य, अमर यश", "#fffbeb", "#d97706", "#78350f")
    ]

    for x_pos, y_name, y_rule, y_result, bg_c, border_c, text_c in yogas_data:
        svg.append(f'  <g transform="translate({x_pos}, 606)">')
        svg.append(f'    <rect x="0" y="0" width="82" height="66" rx="6" fill="{bg_c}" stroke="{border_c}" stroke-width="1.2"/>')
        svg.append(f'    <text x="41" y="16" font-family="{SVG_FONT_FAMILY}" font-size="8.2" font-weight="900" fill="{text_c}" text-anchor="middle">{y_name}</text>')
        svg.append(f'    <text x="41" y="32" font-family="{SVG_FONT_FAMILY}" font-size="7.0" font-weight="700" fill="{border_c}" text-anchor="middle">{y_rule}</text>')
        svg.append(f'    <text x="41" y="48" font-family="{SVG_FONT_FAMILY}" font-size="6.8" font-weight="600" fill="#334155" text-anchor="middle">{y_result}</text>')
        svg.append('  </g>')

    # Bottom Master Shloka / Principle Banner
    svg.extend([
        f'  <g transform="translate(18, 680)">',
        f'    <rect x="0" y="0" width="{width-36}" height="76" rx="6" fill="#fffbeb" stroke="#b45309" stroke-width="1.2"/>',
        f'    <text x="18" y="20" font-family="{SVG_SERIF_FAMILY}" font-size="11" font-weight="800" fill="#78350f">बृहत्पाराशर होरा शास्त्र • पंच महापुरुष एवं गजकेसरी राजयोग विधान</text>',
        f'    <text x="18" y="37" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="600" fill="#78350f">1. भौमादि पंच ग्रह (मंगल, बुध, गुरु, शुक्र, शनि) स्वराशि या उच्च होकर लग्न/चन्द्र से केन्द्र में स्थित हों तभी महापुरुष योग बनता है।</text>',
        f'    <text x="18" y="52" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="600" fill="#78350f">2. गजकेसरी योग: चन्द्रमा से केन्द्र (1, 4, 7, 10) में शुभ बृहस्पति की स्थिति जातक को समाज में अमर कीर्ति व अटूट धन-संपदा प्रदान करती है।</text>',
        f'    <text x="18" y="67" font-family="{SVG_FONT_FAMILY}" font-size="9" font-weight="600" fill="#78350f">3. यह योग अस्त, नीच अथवा षष्ठ/अष्टम/द्वादश भाव के दूषित प्रभाव से मुक्त होने पर ही पूर्ण फलित होता है।</text>',
        f'  </g>',

        '</svg>'
    ])

    return "\n".join(svg)
