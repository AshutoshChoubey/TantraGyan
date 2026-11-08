#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the complete suite of 12 ULTRA-CRISP, VIBRANTLY COLORFUL, SACRED PARCHMENT
SVG Diamond Charts & Diagrams for Bhrigu Nandi Nadi: Karma-Samyojan Sutra.

Key Features:
- Authentic Planet Colors & Astronomical Symbols (☉, ☽, ♂, ☿, ♃, ♀, ♄, ☊, ☋)
- Distinct colored pill badges for every planet in conjunctions and triplets
- 100% Valid XML (all & escaped as &amp;)
- Pure Vector Sharpness: NO filters or feGaussianBlur on text/path groups
- Standard parchment aesthetic matching Vedic Astrology Compendium (lagna_chart, kalpurush_bhavas)
- Tailored 560px width coordinate space for 1:1 crisp rendering in 3D book & mobile web view
- Standard English numerals (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
"""

import os
import xml.etree.ElementTree as ET

ICONS_DIR = "/Users/apple/Movies/ap/TantraGyan/assets/icons"
os.makedirs(ICONS_DIR, exist_ok=True)

def write_and_verify(filename, svg_content):
    filepath = os.path.join(ICONS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    # Validate XML
    ET.parse(filepath)
    print(f"✅ Generated & Validated: {filename} ({os.path.getsize(filepath):,} bytes)")

# Planetary color and symbol constants
P_STYLE = {
    "sun": {"sym": "☉", "hi": "सूर्य", "en": "Sun", "bg": "#ffedd5", "border": "#ea580c", "text": "#c2410c", "grad": "sunGrad"},
    "moon": {"sym": "☽", "hi": "चन्द्र", "en": "Moon", "bg": "#f0f9ff", "border": "#0284c7", "text": "#0369a1", "grad": "moonGrad"},
    "mars": {"sym": "♂", "hi": "मंगल", "en": "Mars", "bg": "#fee2e2", "border": "#ef4444", "text": "#dc2626", "grad": "marsGrad"},
    "mercury": {"sym": "☿", "hi": "बुध", "en": "Mercury", "bg": "#d1fae5", "border": "#10b981", "text": "#047857", "grad": "mercGrad"},
    "jupiter": {"sym": "♃", "hi": "गुरु", "en": "Jupiter", "bg": "#fef3c7", "border": "#f59e0b", "text": "#b45309", "grad": "jupGrad"},
    "venus": {"sym": "♀", "hi": "शुक्र", "en": "Venus", "bg": "#fce7f3", "border": "#ec4899", "text": "#be185d", "grad": "venGrad"},
    "saturn": {"sym": "♄", "hi": "शनि", "en": "Saturn", "bg": "#eff6ff", "border": "#3b82f6", "text": "#1d4ed8", "grad": "satGrad"},
    "rahu": {"sym": "☊", "hi": "राहु", "en": "Rahu", "bg": "#ede9fe", "border": "#8b5cf6", "text": "#4338ca", "grad": "rahuGrad"},
    "ketu": {"sym": "☋", "hi": "केतु", "en": "Ketu", "bg": "#fef3c7", "border": "#b45309", "text": "#78350f", "grad": "ketuGrad"},
}

def planet_badge_svg(p_key, x, y, width=62, height=24):
    p = P_STYLE[p_key]
    rx = height / 2
    return f"""
    <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{rx}" fill="{p['bg']}" stroke="{p['border']}" stroke-width="1.3"/>
    <text x="{x + width/2}" y="{y + height*0.68}" text-anchor="middle" font-family="'Noto Serif Devanagari', 'Kohinoor Devanagari', serif" font-size="11" font-weight="900" fill="{p['text']}">{p['sym']} {p['hi']}</text>"""

COMMON_DEFS = """
  <defs>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700;800;900&amp;family=Noto+Serif+Devanagari:wght@700;800;900&amp;display=swap");
    </style>
    <linearGradient id="plateBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fffefc"/>
      <stop offset="50%" stop-color="#fdfbf5"/>
      <stop offset="100%" stop-color="#faf5ea"/>
    </linearGradient>
    <linearGradient id="goldBannerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fef3c7"/>
      <stop offset="50%" stop-color="#fde68a"/>
      <stop offset="100%" stop-color="#fed7aa"/>
    </linearGradient>
    <linearGradient id="kendraGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="trikonaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ecfdf5" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#d1fae5" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="upachayaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#eff6ff" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#dbeafe" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="waterGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#faf5ff" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#f3e8ff" stop-opacity="0.96"/>
    </linearGradient>
    <linearGradient id="marakaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffe4e6" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#fecdd3" stop-opacity="0.96"/>
    </linearGradient>
    <!-- Planetary Radiant Gradients -->
    <linearGradient id="sunGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ffedd5"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
    <linearGradient id="jupGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef3c7"/><stop offset="100%" stop-color="#fde68a"/></linearGradient>
    <linearGradient id="venGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fce7f3"/><stop offset="100%" stop-color="#fbcfe8"/></linearGradient>
    <linearGradient id="satGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#eff6ff"/><stop offset="100%" stop-color="#bfdbfe"/></linearGradient>
    <linearGradient id="marsGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fee2e2"/><stop offset="100%" stop-color="#fecaca"/></linearGradient>
    <linearGradient id="mercGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#d1fae5"/><stop offset="100%" stop-color="#a7f3d0"/></linearGradient>
    <linearGradient id="moonGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#f0f9ff"/><stop offset="100%" stop-color="#e0f2fe"/></linearGradient>
    <linearGradient id="rahuGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ede9fe"/><stop offset="100%" stop-color="#ddd6fe"/></linearGradient>
    <linearGradient id="ketuGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef3c7"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
    <filter id="cardPlateShadow" x="-3%" y="-3%" width="106%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#78350f" flood-opacity="0.08"/>
    </filter>
  </defs>
"""

def header_banner(title, sub, meta, height=66):
    return f"""
  <!-- Top Header Banner -->
  <rect x="20" y="16" width="520" height="{height}" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.2"/>
  <text x="280" y="38" font-family="'Noto Serif Devanagari', 'Kohinoor Devanagari', Georgia, serif" font-size="15" font-weight="900" fill="#78350f" text-anchor="middle">{title}</text>
  <text x="280" y="55" font-family="'Kohinoor Devanagari', 'Noto Sans Devanagari', 'Poppins', sans-serif" font-size="10.5" font-weight="700" fill="#b45309" text-anchor="middle">{sub}</text>
  <text x="280" y="70" font-family="'Kohinoor Devanagari', 'Noto Sans Devanagari', 'Poppins', sans-serif" font-size="9" font-weight="600" fill="#78716c" text-anchor="middle">{meta}</text>
"""

def draw_north_indian_kundli_polygons(fills, strokes):
    coords = [
        ("270,100 395,225 270,350 145,225", 1),
        ("20,100 270,100 145,225", 2),
        ("20,100 145,225 20,350", 3),
        ("20,350 145,225 270,350 145,475", 4),
        ("20,350 145,475 20,600", 5),
        ("20,600 145,475 270,600", 6),
        ("270,350 395,475 270,600 145,475", 7),
        ("270,600 395,475 520,600", 8),
        ("520,600 395,475 520,350", 9),
        ("270,350 395,225 520,350 395,475", 10),
        ("520,350 395,225 520,100", 11),
        ("520,100 395,225 270,100", 12),
    ]
    svg_parts = []
    for (pts, h_num) in coords:
        f = fills.get(h_num, "#ffffff")
        s = strokes.get(h_num, "#09090b")
        svg_parts.append(f'<polygon points="{pts}" fill="{f}" stroke="{s}" stroke-width="1.8" stroke-linejoin="round"/>')
    svg_parts.append('<rect x="20" y="100" width="500" height="500" fill="none" stroke="#78350f" stroke-width="2.4"/>')
    svg_parts.append('<polygon points="270,100 520,350 270,600 20,350" fill="none" stroke="#b45309" stroke-width="1.8"/>')
    return "\n    ".join(svg_parts)

# ==============================================================================
# 1. Philosophy Hierarchy Chart (5-Tier Decision Model)
# ==============================================================================
def make_philosophy_hierarchy():
    w, h = 560, 750
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("भृगु नंदी नाड़ी का 5-स्तरीय फलित निर्णय पदानुक्रम", "BNN 5-Tier Hierarchical Predictive Architecture", "महर्षि भृगु एवं नंदीश्वर प्रोक्त प्रामाणिक पदानुक्रम • Karaka to Timing Protocol", 66)}

  <!-- Tier 1 -->
  <g transform="translate(24, 96)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#b45309"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर 1</text>
    <text x="65" y="64" text-anchor="middle" fill="#fef3c7" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">ग्रह कारकत्व</text>
    
    <text x="145" y="28" fill="#78350f" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">नैसर्गिक ग्रह कारकत्व (Planetary Significations)</text>
    
    <!-- Colorful Planet Pills in Tier 1 -->
    {planet_badge_svg("jupiter", 145, 36, 58, 20)}
    {planet_badge_svg("venus", 210, 36, 58, 20)}
    {planet_badge_svg("saturn", 275, 36, 58, 20)}
    {planet_badge_svg("sun", 340, 36, 58, 20)}
    {planet_badge_svg("mars", 405, 36, 58, 20)}

    <text x="145" y="74" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700">• गुरु (जीव), शुक्र (स्त्री/धन), शनि (कर्म), सूर्य (आत्मा/पिता), मंगल (पराक्रम)</text>
    <text x="145" y="88" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5">नियम: ग्रह स्वयं व्यक्ति व परिस्थिति दोनों है; भाव स्वामी की अपेक्षा कारकत्व सर्वोपरि है।</text>
  </g>

  <!-- Flow Arrow 1 -->
  <path d="M 280 192 L 280 210" stroke="#b45309" stroke-width="2" stroke-dasharray="3,2"/>
  <polygon points="276,208 284,208 280,214" fill="#b45309"/>

  <!-- Tier 2 -->
  <g transform="translate(24, 216)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#0284c7"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर 2</text>
    <text x="65" y="64" text-anchor="middle" fill="#e0f2fe" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">1-5-9 त्रिकोण</text>
    
    <text x="145" y="30" fill="#0369a1" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">दिशा-संयोजन त्रिकोण (Directional Harmony)</text>
    <text x="145" y="52" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700">• पूर्व (1, 5, 9 अग्नि), दक्षिण (2, 6, 10 पृथ्वी), पश्चिम (3, 7, 11 वायु), उत्तर (4, 8, 12 जल)</text>
    <text x="145" y="74" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5">नियम: समान दिशा के ग्रह एक ही कक्ष में बैठकर 100% संयुक्त फल देते हैं।</text>
  </g>

  <!-- Flow Arrow 2 -->
  <path d="M 280 312 L 280 330" stroke="#0284c7" stroke-width="2" stroke-dasharray="3,2"/>
  <polygon points="276,328 284,328 280,334" fill="#0284c7"/>

  <!-- Tier 3 -->
  <g transform="translate(24, 336)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#059669"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर 3</text>
    <text x="65" y="64" text-anchor="middle" fill="#d1fae5" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">2-12 कर्तरी</text>
    
    <text x="145" y="30" fill="#047857" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">अग्रिम, पृष्ठ एवं कर्तरी वेध (Flank Influences)</text>
    <text x="145" y="52" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700">• अग्र (+1 राशि) भविष्य व गति • पृष्ठ (-1 राशि) अतीत व संचित पृष्ठभूमि</text>
    <text x="145" y="74" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5">नियम: दोनों ओर शुभ ग्रह = सुरक्षा कवच; दोनों ओर पापी ग्रह = बन्धन योग।</text>
  </g>

  <!-- Flow Arrow 3 -->
  <path d="M 280 432 L 280 450" stroke="#059669" stroke-width="2" stroke-dasharray="3,2"/>
  <polygon points="276,448 284,448 280,454" fill="#059669"/>

  <!-- Tier 4 -->
  <g transform="translate(24, 456)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#7c3aed"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर 4</text>
    <text x="65" y="64" text-anchor="middle" fill="#ede9fe" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">अंश व विनिमय</text>
    
    <text x="145" y="30" fill="#6d28d9" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">ग्रह अंश-क्रम एवं वक्री विनिमय (Degree Ordering &amp; Retro Swap)</text>
    <text x="145" y="52" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700">• निम्न अंश ग्रह आगे, उच्च अंश पीछे (पीछे वाला ग्रह आगे वाले की ओर गतिमान)</text>
    <text x="145" y="74" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5">नियम: वक्री ग्रह का 50% अस्तित्व पूर्व राशि में होता है; राशि विनिमय से दोहरा फल मिलता है।</text>
  </g>

  <!-- Flow Arrow 4 -->
  <path d="M 280 552 L 280 570" stroke="#7c3aed" stroke-width="2" stroke-dasharray="3,2"/>
  <polygon points="276,568 284,568 280,574" fill="#7c3aed"/>

  <!-- Tier 5 -->
  <g transform="translate(24, 576)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#dc2626" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#dc2626"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर 5</text>
    <text x="65" y="64" text-anchor="middle" fill="#fee2e2" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">काल निर्धारण</text>
    
    <text x="145" y="30" fill="#b91c1c" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">प्रगति एवं गोचर काल-निर्धारण (Timing of Events)</text>
    <text x="145" y="52" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700">• गुरु 1 वर्ष/राशि प्रगति • शनि 30 वर्ष पर्याय चक्र • भृगु बिंदु (BB) सक्रियण</text>
    <text x="145" y="74" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5">नियम: प्रगतिशील गुरु का जन्मकालिक सूर्य/शुक्र/शनि पर गोचर भाग्योदय कराता है।</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="684" width="512" height="46" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="704" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी सिद्धांत: दशा-अन्तर्दशा की अपेक्षा गोचर-संयोजन से तात्कालिक अचूक फलित होता है ★</text>
  <text x="280" y="720" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">प्रत्येक स्तर क्रमशः विश्लेषित करने पर शत-प्रतिशत सटीक भविष्यवाणी संभव है।</text>
</svg>"""

# ==============================================================================
# 2. Jeeva Flow Diamond Chart
# ==============================================================================
def make_jeeva_flow_chart():
    w, h = 560, 770
    fills = {
        1: "url(#kendraGrad)", 2: "url(#upachayaGrad)", 12: "url(#waterGrad)",
        5: "url(#trikonaGrad)", 9: "url(#trikonaGrad)", 7: "url(#marakaGrad)",
    }
    strokes = {1: "#b45309", 2: "#0284c7", 12: "#7c3aed", 5: "#059669", 9: "#059669", 7: "#dc2626"}
    kundli_svg = draw_north_indian_kundli_polygons(fills, strokes)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("उत्तर भारतीय डायमंड चार्ट में जीव-लग्न भाव-प्रवाह", "BNN Jeeva Lagna Counter-Clockwise Momentum &amp; Step-by-Step Flow", "गुरु (जीव) की केंद्रीय स्थिति, 1-5-9 त्रिकोण, 2-12 पार्श्व एवं 7वीं प्रत्यक्ष दृष्टि", 66)}

  <g>
    {kundli_svg}
  </g>

  <!-- H1: Jeeva Badge -->
  {planet_badge_svg("jupiter", 225, 175, 90, 26)}
  <text x="270" y="218" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">1म भाव • जीव लग्न (स्वयं)</text>
  <text x="270" y="235" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" fill="#451a03" text-anchor="middle">शारीरिक अस्तित्व, बुद्धि व संकल्प</text>

  <!-- H2: Agre -->
  <text x="145" y="140" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">अग्र (+1 भाव)</text>
  <text x="145" y="160" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">2रा: धन, वाणी, भविष्य</text>

  <!-- H12: Prishta -->
  <text x="395" y="140" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#6d28d9" text-anchor="middle">पृष्ठ (-1 भाव)</text>
  <text x="395" y="160" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">12वां: संचित अतीत, व्यय</text>

  <!-- H5: Trikona 1 -->
  <text x="70" y="465" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">त्रिकोण (5म)</text>
  <text x="70" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">पूर्वपुण्य • सन्तान</text>

  <!-- H9: Trikona 2 -->
  <text x="470" y="465" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">त्रिकोण (9म)</text>
  <text x="470" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">भाग्य • धर्म • पिता</text>

  <!-- H7: Samukha -->
  <text x="270" y="460" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#b91c1c" text-anchor="middle">प्रत्यक्ष दृष्टि (7म भाव)</text>
  <text x="270" y="480" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700" fill="#1e293b" text-anchor="middle">180° समसप्तक • जीवनसाथी, व्यापार</text>

  <!-- Flow Arrows connecting 1-5-9 and 7 -->
  <path d="M 230 240 Q 140 320 80 430" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="5,3"/>
  <polygon points="76,432 86,436 82,425" fill="#059669"/>

  <path d="M 310 240 Q 400 320 460 430" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="5,3"/>
  <polygon points="458,425 454,436 464,432" fill="#059669"/>

  <path d="M 270 245 L 270 435" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="4,3"/>
  <polygon points="266,435 274,435 270,443" fill="#dc2626"/>

  <!-- Other Bhavas -->
  <text x="70" y="230" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">3रा: पराक्रम</text>
  <text x="145" y="355" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">4था: सुख/माता</text>
  <text x="145" y="550" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">6ठा: रोग/ऋण</text>
  <text x="395" y="550" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">8वां: संकट/गूढ़</text>
  <text x="395" y="355" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">10वां: कर्म/पद</text>
  <text x="470" y="230" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">11वां: लाभ/इच्छा</text>

  <!-- Bottom Legend Card -->
  <g transform="translate(20, 615)">
    <rect width="520" height="135" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <text x="260" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ भृगु नंदी नाड़ी अग्र-पृष्ठ एवं दृष्टि सूत्र ★</text>
    <text x="260" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">• अग्र नियम (+1 राशि): ग्रह का भविष्य व अगला कदम • पृष्ठ नियम (-1 राशि): संचित अतीत व पृष्ठभूमि बल</text>
    <text x="260" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">• 1-5-9 त्रिकोण संबंध: समान दिशा के ग्रह 100% सम्मिश्रित होकर संयुक्त परिणाम देते हैं</text>
    <text x="260" y="96" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b91c1c" text-anchor="middle">• 7वां भाव (180°): प्रत्यक्ष दृष्टि — जीवनसाथी, साझेदारी व लोक-व्यवहार में प्रत्यक्ष प्रभाव</text>
    <text x="260" y="118" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">• 12वें व 2रे में पापी ग्रह = बन्धन योग • 12वें व 2रे में शुभ ग्रह = सुरक्षा कवच (सहज सफलता)</text>
  </g>
</svg>"""

# ==============================================================================
# 3. Directional Diamond Chart (4 Directions & 1-5-9)
# ==============================================================================
def make_directional_diamond_chart():
    w, h = 560, 770
    fills = {
        1: "url(#kendraGrad)", 5: "url(#kendraGrad)", 9: "url(#kendraGrad)",
        2: "url(#trikonaGrad)", 6: "url(#trikonaGrad)", 10: "url(#trikonaGrad)",
        3: "url(#upachayaGrad)", 7: "url(#upachayaGrad)", 11: "url(#upachayaGrad)",
        4: "url(#waterGrad)", 8: "url(#waterGrad)", 12: "url(#waterGrad)",
    }
    strokes = {
        1: "#b45309", 5: "#b45309", 9: "#b45309",
        2: "#059669", 6: "#059669", 10: "#059669",
        3: "#0284c7", 7: "#0284c7", 11: "#0284c7",
        4: "#7c3aed", 8: "#7c3aed", 12: "#7c3aed",
    }
    kundli_svg = draw_north_indian_kundli_polygons(fills, strokes)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("भृगु नंदी नाड़ी दिशा-आधारित डायमंड चक्र", "BNN 4 Directional Trines &amp; 1-5-9 Conjunction Matrix", "पूर्व (1, 5, 9 अग्नि) • दक्षिण (2, 6, 10 पृथ्वी) • पश्चिम (3, 7, 11 वायु) • उत्तर (4, 8, 12 जल)", 66)}

  <g>
    {kundli_svg}
  </g>

  <!-- Direction Badges in Kundli -->
  <!-- H1: East / Mesha -->
  <text x="270" y="195" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="900" fill="#78350f" text-anchor="middle">1. पूर्व (अग्नि)</text>
  <text x="270" y="215" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700" fill="#b45309" text-anchor="middle">मेष • धर्म त्रिकोण</text>

  <!-- H5: East / Simha -->
  <text x="70" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">5. पूर्व (अग्नि)</text>
  <text x="70" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">सिंह राशि</text>

  <!-- H9: East / Dhanu -->
  <text x="470" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">9. पूर्व (अग्नि)</text>
  <text x="470" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">धनु राशि</text>

  <!-- South: 2, 6, 10 -->
  <text x="145" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">2. दक्षिण (पृथ्वी)</text>
  <text x="145" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">वृषभ राशि</text>

  <text x="145" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">6. दक्षिण (पृथ्वी)</text>
  <text x="145" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">कन्या राशि</text>

  <text x="395" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">10. दक्षिण (पृथ्वी)</text>
  <text x="395" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">मकर राशि</text>

  <!-- West: 3, 7, 11 -->
  <text x="70" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">3. पश्चिम (वायु)</text>
  <text x="70" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#0284c7" text-anchor="middle">मिथुन राशि</text>

  <text x="270" y="465" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#0369a1" text-anchor="middle">7. पश्चिम (वायु)</text>
  <text x="270" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700" fill="#0284c7" text-anchor="middle">तुला • काम त्रिकोण</text>

  <text x="470" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">11. पश्चिम (वायु)</text>
  <text x="470" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#0284c7" text-anchor="middle">कुम्भ राशि</text>

  <!-- North: 4, 8, 12 -->
  <text x="145" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">4. उत्तर (जल)</text>
  <text x="145" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#7c3aed" text-anchor="middle">कर्क राशि</text>

  <text x="395" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">8. उत्तर (जल)</text>
  <text x="395" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#7c3aed" text-anchor="middle">वृश्चिक राशि</text>

  <text x="395" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">12. उत्तर (जल)</text>
  <text x="395" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#7c3aed" text-anchor="middle">मीन राशि</text>

  <!-- Bottom Legend Card -->
  <g transform="translate(20, 615)">
    <rect width="520" height="135" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <text x="260" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ नाड़ी दिशा-त्रिकोण संयोजन सूत्र (Directional Conjunction Law) ★</text>
    <text x="260" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">• पूर्व (1, 5, 9): मेष, सिंह, धनु = अग्नि तत्व • आत्मा, धर्म, जीवन ऊर्जा, नेतृत्व</text>
    <text x="260" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669" text-anchor="middle">• दक्षिण (2, 6, 10): वृषभ, कन्या, मकर = पृथ्वी तत्व • धन, आजीविका, भौतिक स्थिरता</text>
    <text x="260" y="96" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#0284c7" text-anchor="middle">• पश्चिम (3, 7, 11): मिथुन, तुला, कुम्भ = वायु तत्व • बुद्धि, व्यापार, सामाजिक संबंध</text>
    <text x="260" y="118" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#7c3aed" text-anchor="middle">• उत्तर (4, 8, 12): कर्क, वृश्चिक, मीन = जल तत्व • भावना, अंतर्ज्ञान, वैराग्य, मोक्ष</text>
  </g>
</svg>"""

# ==============================================================================
# 4. Kartari & Flank Diamond Chart
# ==============================================================================
def make_kartari_flank_chart():
    w, h = 560, 770
    fills = {1: "url(#kendraGrad)", 2: "url(#upachayaGrad)", 12: "url(#waterGrad)"}
    strokes = {1: "#b45309", 2: "#0284c7", 12: "#7c3aed"}
    kundli_svg = draw_north_indian_kundli_polygons(fills, strokes)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("अग्रिम, पृष्ठ एवं शुभ/पाप-कर्तरी वेध डायमंड चक्र", "Next (+1) &amp; Rear (-1) Flank Influences &amp; Planetary Siege Mechanics", "किसी भी ग्रह के आगे व पीछे स्थित ग्रहों का जीवन पर नियंत्रणकारी प्रभाव", 66)}

  <g>
    {kundli_svg}
  </g>

  <!-- H1: Middle Planet Badge -->
  {planet_badge_svg("jupiter", 215, 175, 110, 26)}
  <text x="270" y="218" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">1म भाव • फलित का केंद्र</text>
  <text x="270" y="238" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" fill="#451a03" text-anchor="middle">(उदा. गुरु = जीव, शनि = कर्म)</text>

  <!-- H2: Front Flank -->
  <text x="145" y="140" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#0369a1" text-anchor="middle">अग्रिम ग्रह (+1 राशि)</text>
  <text x="145" y="160" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">भविष्य, दिशा, अगला कदम</text>

  <!-- H12: Rear Flank -->
  <text x="395" y="140" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#6d28d9" text-anchor="middle">पृष्ठ ग्रह (-1 राशि)</text>
  <text x="395" y="160" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">अतीत, संचित बल, पृष्ठभूमि</text>

  <path d="M 180 170 L 230 200" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="3,2"/>
  <polygon points="228,194 234,202 224,204" fill="#0284c7"/>

  <path d="M 360 170 L 310 200" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="3,2"/>
  <polygon points="316,204 306,202 312,194" fill="#7c3aed"/>

  <text x="70" y="230" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">3रा भाव</text>
  <text x="145" y="355" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">4था भाव</text>
  <text x="70" y="475" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">5वां भाव</text>
  <text x="145" y="550" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">6ठा भाव</text>
  <text x="270" y="475" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">7वां भाव</text>
  <text x="395" y="550" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">8वां भाव</text>
  <text x="470" y="475" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">9वां भाव</text>
  <text x="395" y="355" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">10वां भाव</text>
  <text x="470" y="230" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">11वां भाव</text>

  <!-- Bottom Comparison Cards with colorful planet icons -->
  <g transform="translate(20, 615)">
    <!-- Shubha Kartari -->
    <rect x="0" y="0" width="255" height="135" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.4"/>
    <text x="127" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#047857" text-anchor="middle">🛡️ शुभ कर्तरी योग (Suraksha Kavach)</text>
    
    <!-- Planets in Shubha Kartari -->
    <g transform="translate(10, 36)">
      {planet_badge_svg("venus", 5, 0, 52, 20)}
      {planet_badge_svg("mercury", 62, 0, 52, 20)}
      {planet_badge_svg("jupiter", 119, 0, 52, 20)}
      {planet_badge_svg("moon", 176, 0, 52, 20)}
    </g>

    <text x="127" y="74" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#334155" text-anchor="middle">• 12वें में शुक्र/बुध + 2रे में गुरु/चन्द्र</text>
    <text x="127" y="92" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#334155" text-anchor="middle">• जातक को हर संकट में दैवीय सुरक्षा मिलती है</text>
    <text x="127" y="114" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">परिणाम: सुख, समृद्धि, राजकृपा व सम्मान</text>

    <!-- Papa Kartari -->
    <rect x="265" y="0" width="255" height="135" rx="8" fill="#ffffff" stroke="#dc2626" stroke-width="1.4"/>
    <text x="392" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#b91c1c" text-anchor="middle">⛓️ पाप कर्तरी योग (Bandhana Yoga)</text>
    
    <!-- Planets in Papa Kartari -->
    <g transform="translate(275, 36)">
      {planet_badge_svg("saturn", 5, 0, 52, 20)}
      {planet_badge_svg("rahu", 62, 0, 52, 20)}
      {planet_badge_svg("mars", 119, 0, 52, 20)}
      {planet_badge_svg("ketu", 176, 0, 52, 20)}
    </g>

    <text x="392" y="74" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#334155" text-anchor="middle">• 12वें में शनि/राहु + 2रे में मंगल/केतु</text>
    <text x="392" y="92" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#334155" text-anchor="middle">• मध्य ग्रह पिस जाता है; रुकावट व विलंब</text>
    <text x="392" y="114" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#b91c1c" text-anchor="middle">परिणाम: विलंब, मानसिक तनाव, कठोर संघर्ष</text>
  </g>
</svg>"""

# ==============================================================================
# 5. Karaka Relationship Wheel
# ==============================================================================
def make_karaka_relationship_wheel():
    w, h = 560, 770
    planets_order = ["sun", "moon", "mars", "mercury", "jupiter", "venus", "saturn", "rahu", "ketu"]
    karaka_data = {
        "sun": ("आत्मा • पिता • शासन • अहंकार", "गुरु, मंगल", "बुध", "शुक्र, शनि, राहु"),
        "moon": ("मन • माता • जल • यात्रा • कला", "सूर्य, गुरु", "मंगल, बुध, शुक्र, शनि", "राहु, केतु"),
        "mars": ("पराक्रम • भ्राता • रक्त • भूमि • साहस", "सूर्य, चन्द्र, गुरु", "शुक्र, शनि", "बुध, राहु"),
        "mercury": ("बुद्धि • व्यापार • वाणी • शिक्षा • मित्र", "सूर्य, शुक्र, शनि", "मंगल, गुरु", "चन्द्र, राहु"),
        "jupiter": ("जीव (पुरुष) • ज्ञान • सन्तान • धर्म", "सूर्य, चन्द्र, मंगल", "शनि, राहु", "शुक्र, बुध"),
        "venus": ("जीव (स्त्री) • धन • पत्नी • वाहन • विलास", "बुध, शनि, राहु", "मंगल, चन्द्र", "सूर्य, गुरु, केतु"),
        "saturn": ("कर्म • आजीविका • विलंब • श्रम • आयु", "बुध, शुक्र, राहु", "गुरु", "सूर्य, चन्द्र, मंगल"),
        "rahu": ("भ्रम • विदेश • विस्तार • माया • तकनीक", "बुध, शुक्र, शनि", "गुरु", "सूर्य, चन्द्र, मंगल, केतु"),
        "ketu": ("मोक्ष • संन्यास • त्याग • सूक्ष्म ज्ञान • जड़", "गुरु, मंगल, सूर्य", "शुक्र, शनि", "बुध, राहु, चन्द्र"),
    }

    cards_svg = []
    card_w = 512
    card_h = 58
    start_y = 96
    gap = 9

    for i, p_key in enumerate(planets_order):
        p = P_STYLE[p_key]
        karaka, friends, neutral, enemies = karaka_data[p_key]
        cy = start_y + i * (card_h + gap)
        cards_svg.append(f"""
  <g transform="translate(24, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="6" fill="#ffffff" stroke="{p['border']}" stroke-width="1.3"/>
    <rect width="125" height="{card_h}" rx="6" fill="{p['bg']}" stroke="{p['border']}" stroke-width="0.8"/>
    
    <!-- Planet Symbol & Name with authentic color -->
    <text x="62" y="27" text-anchor="middle" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="900" fill="{p['text']}">{p['sym']} {p['hi']}</text>
    <text x="62" y="45" text-anchor="middle" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#475569">{p['en']}</text>

    <!-- Details -->
    <text x="135" y="23" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="800" fill="#0f172a">कारकत्व: <tspan font-weight="600" fill="#334155">{karaka}</tspan></text>
    <text x="135" y="44" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700">
      <tspan fill="#059669">मित्र: {friends}</tspan> • <tspan fill="#64748b">सम: {neutral}</tspan> • <tspan fill="#dc2626">शत्रु: {enemies}</tspan>
    </text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("नवग्रह नाड़ी कारकत्व एवं त्रि-स्तरीय मैत्री महाचक्र", "Navagraha Nadi Karakatwas &amp; Natural Harmony Matrix", "जीव, कर्म, धन, बुद्धि व मोक्ष के प्राकृतिक नियंत्रक ग्रह", 66)}

  {cards_str}

  <!-- Bottom Summary Footer -->
  <rect x="24" y="700" width="512" height="48" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.2"/>
  <text x="280" y="720" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#78350f" text-anchor="middle">★ नाड़ी सूत्र: मित्र ग्रहों की युति भाग्योदय कराती है, शत्रु ग्रहों का योग संघर्ष पैदा करता है ★</text>
  <text x="280" y="736" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">गुरु-शुक्र दोनों जीव हैं, शनि कर्म है, सूर्य यश है, बुध व्यापार है, राहु भ्रम व केतु मोक्ष है।</text>
</svg>"""

# ==============================================================================
# 6. Elemental Directional Diamond Chart
# ==============================================================================
def make_elemental_directional_chart():
    w, h = 560, 770
    fills = {
        1: "url(#kendraGrad)", 5: "url(#kendraGrad)", 9: "url(#kendraGrad)",
        2: "url(#trikonaGrad)", 6: "url(#trikonaGrad)", 10: "url(#trikonaGrad)",
        3: "url(#upachayaGrad)", 7: "url(#upachayaGrad)", 11: "url(#upachayaGrad)",
        4: "url(#waterGrad)", 8: "url(#waterGrad)", 12: "url(#waterGrad)",
    }
    strokes = {
        1: "#b45309", 5: "#b45309", 9: "#b45309",
        2: "#059669", 6: "#059669", 10: "#059669",
        3: "#0284c7", 7: "#0284c7", 11: "#0284c7",
        4: "#7c3aed", 8: "#7c3aed", 12: "#7c3aed",
    }
    kundli_svg = draw_north_indian_kundli_polygons(fills, strokes)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("चतुर्विध महाभूत एवं दिशा-संयोजन डायमंड चक्र", "BNN 4 Elemental Trines &amp; Directional Harmony (1-5-9 Samyoga Matrix)", "अग्नि (1, 5, 9), पृथ्वी (2, 6, 10), वायु (3, 7, 11), जल (4, 8, 12) का सम्मिश्रण", 66)}

  <g>
    {kundli_svg}
  </g>

  <!-- Labels & colorful planet lords in Bhavas -->
  <!-- Fire (1, 5, 9) -->
  <text x="270" y="185" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#78350f" text-anchor="middle">अग्नि तत्व (1)</text>
  <text x="270" y="202" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">मेष • धर्म त्रिकोण</text>
  {planet_badge_svg("mars", 240, 210, 60, 20)}

  <text x="70" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">अग्नि (5)</text>
  <text x="70" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#b45309" text-anchor="middle">सिंह (☉ सूर्य)</text>

  <text x="470" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">अग्नि (9)</text>
  <text x="470" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#b45309" text-anchor="middle">धनु (♃ गुरु)</text>

  <!-- Earth (2, 6, 10) -->
  <text x="145" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">पृथ्वी (2)</text>
  <text x="145" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">वृषभ (♀ शुक्र)</text>

  <text x="145" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">पृथ्वी (6)</text>
  <text x="145" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">कन्या (☿ बुध)</text>

  <text x="395" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">पृथ्वी (10)</text>
  <text x="395" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">मकर (♄ शनि)</text>

  <!-- Air (3, 7, 11) -->
  <text x="70" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">वायु (3)</text>
  <text x="70" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#0284c7" text-anchor="middle">मिथुन (☿ बुध)</text>

  <text x="270" y="465" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#0369a1" text-anchor="middle">वायु तत्व (7)</text>
  <text x="270" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#0284c7" text-anchor="middle">तुला • काम (♀ शुक्र)</text>

  <text x="470" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">वायु (11)</text>
  <text x="470" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#0284c7" text-anchor="middle">कुम्भ (♄ शनि)</text>

  <!-- Water (4, 8, 12) -->
  <text x="145" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">जल (4)</text>
  <text x="145" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">कर्क (☽ चन्द्र)</text>

  <text x="395" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">जल (8)</text>
  <text x="395" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">वृश्चिक (♂ मंगल)</text>

  <text x="395" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">जल (12)</text>
  <text x="395" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">मीन (♃ गुरु)</text>

  <!-- Bottom Legend Card -->
  <g transform="translate(20, 615)">
    <rect width="520" height="135" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <text x="260" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ महाभूत सम्मिश्रण एवं फलित नियम ★</text>
    <text x="260" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">• अग्नि + वायु = मित्र सम्मिश्रण (अग्नि को वायु प्रज्वलित करती है: विचार + कर्म = सफलता)</text>
    <text x="260" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669" text-anchor="middle">• पृथ्वी + जल = मित्र सम्मिश्रण (मिट्टी को जल उर्वर बनाता है: धन + स्थिरता + सिद्धि)</text>
    <text x="260" y="96" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#dc2626" text-anchor="middle">• अग्नि + जल = विरोधी सम्मिश्रण (भाप व संघर्ष: क्रोध, मानसिक उथल-पुथल, रुकावट)</text>
    <text x="260" y="118" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">• वायु + पृथ्वी = मध्यम सम्मिश्रण (धूल/उदासीनता: कठोर परिश्रम के बाद ही फल)</text>
  </g>
</svg>"""

# ==============================================================================
# 7. Jeeva 12 Bhavas Diamond Chart
# ==============================================================================
def make_jeeva_12bhavas_chart():
    w, h = 560, 770
    fills = {
        1: "url(#kendraGrad)", 2: "url(#trikonaGrad)", 3: "url(#upachayaGrad)",
        4: "url(#waterGrad)", 5: "url(#kendraGrad)", 6: "url(#trikonaGrad)",
        7: "url(#marakaGrad)", 8: "url(#waterGrad)", 9: "url(#kendraGrad)",
        10: "url(#trikonaGrad)", 11: "url(#upachayaGrad)", 12: "url(#waterGrad)",
    }
    strokes = {i: "#78350f" for i in range(1, 13)}
    kundli_svg = draw_north_indian_kundli_polygons(fills, strokes)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("जीव लग्न (गुरु) द्वादश भाव सम्पूर्ण फलित चक्र", "Jeeva (Guru) 12 Bhavas Manifestation Architecture", "गुरु जहां बैठता है, वह जातक का 'जीव' है; उस भाव से सम्पूर्ण जीवन संचालित होता है", 66)}

  <g>
    {kundli_svg}
  </g>

  <!-- 12 Bhavas Meaning relative to Guru with Planet badges -->
  <text x="270" y="185" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#78350f" text-anchor="middle">1म: जीव स्वयं</text>
  {planet_badge_svg("jupiter", 240, 192, 60, 20)}
  <text x="270" y="226" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">आत्मज्ञानी, सात्विक, दीर्घायु</text>

  <text x="145" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">2रा: धन/वाणी</text>
  <text x="145" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">मधुर वक्ता, उत्तम कुल</text>

  <text x="70" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">3रा: पराक्रम</text>
  <text x="70" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#0284c7" text-anchor="middle">लेखक, सहोदर सुख</text>

  <text x="145" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">4था: सुख/गृह</text>
  <text x="145" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">मातृभक्त, वाहन, विद्या</text>

  <text x="70" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">5वां: मन्त्र/सन्तान</text>
  <text x="70" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#b45309" text-anchor="middle">पूर्वपुण्य, उच्च बुद्धि</text>

  <text x="145" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">6ठा: सेवा/आरोग्य</text>
  <text x="145" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">शत्रुहन्ता, ऋणमुक्ति</text>

  <text x="270" y="465" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#b91c1c" text-anchor="middle">7वां: जीवनसाथी</text>
  <text x="270" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#dc2626" text-anchor="middle">गुणी पत्नी/पति, व्यापार</text>

  <text x="395" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">8वां: गूढ़ ज्ञान</text>
  <text x="395" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">दीर्घायु, वसीयत, साधना</text>

  <text x="470" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">9वां: धर्म/भाग्य</text>
  <text x="470" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#b45309" text-anchor="middle">तीर्थयात्री, पिता-भक्त</text>

  <text x="395" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">10वां: आजीविका</text>
  <text x="395" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">प्रतिष्ठित कर्म, शासन</text>

  <text x="470" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">11वां: सर्व लाभ</text>
  <text x="470" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#0284c7" text-anchor="middle">इच्छापूर्ति, आय, सिद्धि</text>

  <text x="395" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">12वां: मोक्ष/त्याग</text>
  <text x="395" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">विदेश गमन, वैराग्य</text>

  <!-- Bottom Legend Card -->
  <g transform="translate(20, 615)">
    <rect width="520" height="135" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <text x="260" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ नाड़ी जीव-कारकत्व फलित सूत्र ★</text>
    <text x="260" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">• गुरु जिस भाव में बैठता है, वहां जातक की चेतना और प्राण ऊर्जा केंद्रित होती है</text>
    <text x="260" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">• गुरु के साथ सूर्य = राजयोग; गुरु के साथ मंगल = पराक्रम; गुरु के साथ बुध = उच्च विद्या</text>
    <text x="260" y="96" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#0284c7" text-anchor="middle">• गुरु के साथ शुक्र = अपार धन व विलास; गुरु के साथ शनि = धर्म-कर्म सामंजस्य</text>
    <text x="260" y="118" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#7c3aed" text-anchor="middle">• गुरु के साथ राहु = गुरु-चांडाल (विदेश/भ्रम); गुरु के साथ केतु = परम मोक्ष योग</text>
  </g>
</svg>"""

# ==============================================================================
# 8. Major Conjunctions Diamond Chart (VIBRANT PLANET BADGES)
# ==============================================================================
def make_major_conjunctions_chart():
    w, h = 560, 770
    conjunctions = [
        ("jupiter", "saturn", "धर्म-कर्माधिपति योग", "न्यायिक पद, सामाजिक प्रतिष्ठा, उच्च कर्मयोग, कर्तव्यपरायणता", "#b45309"),
        ("sun", "jupiter", "राजकृपा / प्रतिष्ठा योग", "सरकारी सम्मान, उच्च पद, पिता का पूर्ण सहयोग, सात्विक सत्ता", "#d97706"),
        ("venus", "saturn", "लक्ष्मी-कर्म योग", "स्थिर अचल संपत्ति, विलासिता, व्यापारिक सफलता, ऐश्वर्य", "#059669"),
        ("mercury", "venus", "सरस्वती-लक्ष्मी योग", "चतुर व्यापारी, वाक्पटु, कला-संगीत प्रेमी, उच्च एकाउंटिंग/CA", "#0284c7"),
        ("mars", "saturn", "यांत्रिकी / इंजीनियरिंग योग", "तकनीकी विशेषज्ञ, उद्योगपति, कठिन परिश्रम से शिखर की प्राप्ति", "#dc2626"),
        ("venus", "ketu", "मुक्ति-लक्ष्मी / संन्यास योग", "आध्यात्मिक समृद्धि, वस्त्र/रसायन व्यापार, वैराग्य में सुख", "#7c3aed"),
    ]

    cards_svg = []
    card_w = 512
    card_h = 76
    start_y = 96
    gap = 10

    for i, (p1_key, p2_key, yoga, fruit, stroke_col) in enumerate(conjunctions):
        cy = start_y + i * (card_h + gap)
        cards_svg.append(f"""
  <g transform="translate(24, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="6" fill="#ffffff" stroke="{stroke_col}" stroke-width="1.4"/>
    
    <!-- Left Planet Badges Container -->
    <rect width="150" height="{card_h}" rx="6" fill="#f8fafc" stroke="{stroke_col}" stroke-width="0.8"/>
    
    <!-- Colorful Dual Planet Badges -->
    {planet_badge_svg(p1_key, 10, 16, 58, 24)}
    <text x="75" y="33" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="900" fill="#475569">+</text>
    {planet_badge_svg(p2_key, 83, 16, 58, 24)}
    <text x="75" y="58" text-anchor="middle" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#334155">{yoga}</text>

    <!-- Content on the right -->
    <text x="165" y="28" font-family="'Noto Serif Devanagari', serif" font-size="12.5" font-weight="800" fill="{stroke_col}">{yoga} (Conjunction Fruit)</text>
    <text x="165" y="52" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• {fruit}</text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("बी.एन.एन. प्रमुख द्वि-ग्रहीय राजयोग एवं कर्म-संयोग चक्र", "Master 2-Planet Combinations in Bhrigu Nandi Nadi", "36 प्रमुख ग्रहीय संयोगों में से शीर्ष 6 शास्त्रीय राजयोग", 66)}

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="625" width="512" height="120" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.3"/>
  <text x="280" y="648" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" fill="#78350f" text-anchor="middle">★ नाड़ी ग्रहीय संयोग गणितीय नियम ★</text>
  <text x="280" y="670" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• एक ही राशि में युति (0°) अथवा 1-5-9 त्रिकोण में स्थिति = समान शक्तिशाली फल</text>
  <text x="280" y="692" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">• निम्न अंश वाला ग्रह पूर्ववर्ती एवं उच्च अंश वाला ग्रह परवर्ती प्रभाव डालता है</text>
  <text x="280" y="714" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#6d28d9" text-anchor="middle">• यदि दोनों में से कोई वक्री हो तो पूर्व राशि से भी संयोग प्रभाव की गणना करें</text>
  <text x="280" y="734" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • तंत्र ज्ञान शोध संस्थान</text>
</svg>"""

# ==============================================================================
# 9. Triplet Rajyogas Diamond Chart (VIBRANT PLANET BADGES)
# ==============================================================================
def make_triplet_rajyogas_chart():
    w, h = 560, 770
    triplets = [
        ("jupiter", "saturn", "sun", "सर्वोच्च प्रशासनिक योग (IAS / Cabinet)", "गुरु (जीव) + शनि (कर्म) + सूर्य (शासन) = देश/संस्थान का सर्वोच्च नेतृत्व, स्थायी मान-सम्मान व राजसत्ता।", "#b45309"),
        ("jupiter", "venus", "ketu", "ब्रह्मर्षि / आध्यात्मिक शिखर योग", "गुरु (ज्ञान) + शुक्र (तप) + केतु (मोक्ष) = संन्यास, अलौकिक अंतर्ज्ञान, जगद्गुरु पद, निःस्वार्थ लोकमंगल।", "#7c3aed"),
        ("saturn", "mercury", "venus", "महा-व्यापारी योग (कुबेर साम्राज्य)", "शनि (कर्म) + बुध (व्यापार) + शुक्र (धन/लक्ष्मी) = बहुराष्ट्रीय व्यापार, विशाल धन सम्पदा, वैश्विक ब्रांड।", "#059669"),
        ("mars", "saturn", "rahu", "अंतर्राष्ट्रीय तकनीकी / AI योग", "मंगल (यंत्र) + शनि (श्रम/उद्योग) + राहु (विदेशी/सॉफ्टवेयर) = रक्षा तकनीक, एयरोस्पेस, विदेश में बड़ा उद्योग।", "#dc2626"),
        ("moon", "ketu", "jupiter", "सिद्ध योगी / प्रज्ञा-चक्षु योग", "चन्द्र (मन) + केतु (सूक्ष्म दृष्टि) + गुरु (ईश्वरीय कृपा) = सटीक भविष्यवाणी, त्रिकालज्ञ, निस्पृह तपस्वी।", "#0284c7"),
    ]

    cards_svg = []
    card_w = 512
    card_h = 92
    start_y = 96
    gap = 12

    for i, (p1, p2, p3, title, desc, stroke_col) in enumerate(triplets):
        cy = start_y + i * (card_h + gap)
        cards_svg.append(f"""
  <g transform="translate(24, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="6" fill="#ffffff" stroke="{stroke_col}" stroke-width="1.5"/>
    <rect width="180" height="{card_h}" rx="6" fill="#f8fafc" stroke="{stroke_col}" stroke-width="0.8"/>
    
    <!-- 3 Colorful Planet Badges inline -->
    {planet_badge_svg(p1, 6, 20, 50, 24)}
    <text x="60" y="36" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="900" fill="#475569">+</text>
    {planet_badge_svg(p2, 65, 20, 50, 24)}
    <text x="119" y="36" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="900" fill="#475569">+</text>
    {planet_badge_svg(p3, 124, 20, 50, 24)}
    
    <text x="90" y="66" text-anchor="middle" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#475569">त्रि-ग्रहीय महायोग</text>

    <!-- Description on the right -->
    <text x="195" y="28" font-family="'Noto Serif Devanagari', serif" font-size="12.5" font-weight="800" fill="{stroke_col}">{title}</text>
    <text x="195" y="52" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• {desc}</text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("बी.एन.एन. त्रि-ग्रहीय एवं बहु-ग्रहीय महायोग डायमंड चक्र", "Master Triplet Combinations in Bhrigu Nandi Nadi", "Root (बीज), Carrier (माध्यम) एवं Fruit (फल) की शास्त्रीय श्रृंखला", 66)}

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="625" width="512" height="120" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.3"/>
  <text x="280" y="648" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" fill="#78350f" text-anchor="middle">★ त्रि-ग्रहीय संयोजन के 3 मूलभूत घटक ★</text>
  <text x="280" y="670" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">1. मूल कारण (Root): प्रथम ग्रह घटना का बीज व संकल्प निर्धारित करता है</text>
  <text x="280" y="692" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#0284c7" text-anchor="middle">2. माध्यम (Carrier): द्वितीय ग्रह साधन, वातावरण एवं कार्य-प्रणाली प्रदान करता है</text>
  <text x="280" y="714" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">3. अंतिम फल (Fruit): तृतीय ग्रह परिणाम का अंतिम स्वरूप व प्रभाव तय करता है</text>
  <text x="280" y="734" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">सूत्र: तीन ग्रहों का त्रिकोण सम्मिश्रण जातक के जीवन की सबसे बड़ी दिशा तय करता है।</text>
</svg>"""

# ==============================================================================
# 10. Progression & Paryaya Chart
# ==============================================================================
def make_progression_paryaya_chart():
    w, h = 560, 770
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("शनि 30-वर्षीय पर्याय एवं गुरु प्रगति काल-चक्र", "BNN Saturn 30-Year Paryaya Cycles &amp; Jupiter 1-Year Progression Engine", "दशा-महादशा के बिना अचूक घटना समय-निर्धारण (Timing of Events)", 66)}

  <g transform="translate(24, 96)">
    <rect width="512" height="32" rx="4" fill="#0f172a"/>
    <text x="256" y="21" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" text-anchor="middle">शनि के 3 प्रमुख 30-वर्षीय पर्याय चक्र (Saturn 30-Year Cycles)</text>
  </g>

  <!-- Paryaya 1 -->
  <g transform="translate(24, 136)">
    <rect width="512" height="88" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.4"/>
    <rect width="130" height="88" rx="8" fill="#e0f2fe"/>
    <text x="65" y="38" text-anchor="middle" fill="#0369a1" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900">प्रथम पर्याय</text>
    <text x="65" y="58" text-anchor="middle" fill="#0284c7" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">आयु 0 से 30 वर्ष</text>

    <text x="145" y="28" fill="#0369a1" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800">बाल्यावस्था, शिक्षा, संघर्ष एवं आधार निर्माण</text>
    <text x="145" y="50" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600">• शिक्षा, शारीरिक वृद्धि, पारिवारिक निर्भरता एवं प्रथम कर्म का चयन</text>
    <text x="145" y="70" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9">28वें-30वें वर्ष में शनि की पहली वापसी (Saturn Return) जीवन को नई दिशा देती है।</text>
  </g>

  <!-- Paryaya 2 -->
  <g transform="translate(24, 232)">
    <rect width="512" height="88" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <rect width="130" height="88" rx="8" fill="#fef3c7"/>
    <text x="65" y="38" text-anchor="middle" fill="#78350f" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900">द्वितीय पर्याय</text>
    <text x="65" y="58" text-anchor="middle" fill="#b45309" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">आयु 30 से 60 वर्ष</text>

    <text x="145" y="28" fill="#78350f" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800">कर्म विस्तार, पद-प्रतिष्ठा, विवाह, सन्तान एवं गृह</text>
    <text x="145" y="50" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600">• जीवन का सबसे फलदायी काल; आजीविका में स्थायित्व व सामाजिक प्रतिष्ठा</text>
    <text x="145" y="70" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9">58वें-60वें वर्ष में शनि की दूसरी वापसी से कर्म चक्र की पूर्णता होती है।</text>
  </g>

  <!-- Paryaya 3 -->
  <g transform="translate(24, 328)">
    <rect width="512" height="88" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="1.4"/>
    <rect width="130" height="88" rx="8" fill="#ede9fe"/>
    <text x="65" y="38" text-anchor="middle" fill="#6d28d9" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900">तृतीय पर्याय</text>
    <text x="65" y="58" text-anchor="middle" fill="#7c3aed" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">आयु 60 से 90 वर्ष</text>

    <text x="145" y="28" fill="#6d28d9" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800">सेवानिवृत्ति, नाती-पोते, अध्यात्म एवं मोक्ष चिंतन</text>
    <text x="145" y="50" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600">• भौतिक उत्तरदायित्वों से मुक्ति, आध्यात्मिक साधना व अंतर्मुखी शांति</text>
    <text x="145" y="70" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9">संचित कर्मों का अंतिम परिशोधन एवं आत्म-साक्षात्कार।</text>
  </g>

  <!-- Jupiter Progression Header -->
  <g transform="translate(24, 428)">
    <rect width="512" height="32" rx="4" fill="#0f172a"/>
    <text x="256" y="21" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" text-anchor="middle">गुरु 1-वर्षीय प्रगति नियम (Jupiter 1-Year Progression)</text>
  </g>

  <!-- Jupiter Rules Card -->
  <g transform="translate(24, 468)">
    <rect width="512" height="155" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.4"/>
    <text x="256" y="26" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ गुरु प्रगति से विवाह, सन्तान एवं भाग्योदय का वर्ष निर्धारण ★</text>
    
    <text x="20" y="54" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669">1. गति:</text>
    <text x="65" y="54" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="600" fill="#1e293b">गुरु प्रति वर्ष ठीक 1 राशि (30°) आगे बढ़ता है (12 वर्ष में 1 परिक्रमा)।</text>

    <text x="20" y="78" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669">2. विवाह वर्ष:</text>
    <text x="100" y="78" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="600" fill="#1e293b">प्रगतिशील गुरु जब जन्मकालिक शुक्र (पुरुष हेतु) या मंगल (स्त्री हेतु) पर आए।</text>

    <text x="20" y="102" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669">3. पदोन्नति:</text>
    <text x="95" y="102" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="600" fill="#1e293b">प्रगतिशील गुरु जब जन्मकालिक शनि अथवा सूर्य के ऊपर या त्रिकोण में गोचर करे।</text>

    <text x="20" y="126" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669">4. सन्तान जन्म:</text>
    <text x="105" y="126" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="600" fill="#1e293b">प्रगतिशील गुरु का 5वें भाव या जन्मकालिक गुरु के त्रिकोण में गोचर काल।</text>

    <text x="256" y="146" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">सूत्र: 12, 24, 36, 48वें वर्ष में गुरु की वापसी अत्यंत महत्वपूर्ण घटनाक्रम लाती है।</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="635" width="512" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="658" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी काल-निर्धारण सिद्धांत (BNN Event Timing Architecture) ★</text>
  <text x="280" y="680" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• शनि तय करता है घटना की पृष्ठभूमि (स्थूल काल)</text>
  <text x="280" y="700" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• गुरु निर्धारित करता है भाग्योदय का सटीक वर्ष (मध्यम काल)</text>
  <text x="280" y="720" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">• सूर्य व चन्द्र का गोचर निश्चित करता है घटना का सटीक माह एवं दिन (सूक्ष्म काल)</text>
  <text x="280" y="736" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""

# ==============================================================================
# 11. Bhrigu Bindu Diagram
# ==============================================================================
def make_bhrigu_bindu_diagram():
    w, h = 560, 770
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("भृगु बिंदु (BB) प्रारब्ध संवाहक बिंदु ज्यामितीय चक्र", "Bhrigu Bindu (BB) Destiny Trigger &amp; Rahu-Moon Midpoint Physics", "गणितीय सूत्र: (राहु स्पष्ट अंश + चन्द्र स्पष्ट अंश) ÷ 2 = भृगु बिंदु", 66)}

  <g transform="translate(24, 96)">
    <rect width="512" height="66" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.6"/>
    <text x="256" y="28" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="900" fill="#78350f" text-anchor="middle">भृगु बिंदु (Bhrigu Bindu - BB) की गणितीय गणना</text>
    <text x="256" y="50" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700" fill="#dc2626" text-anchor="middle">BB = (राहु के निरयण अंश + चन्द्र के निरयण अंश) / 2</text>
  </g>

  <!-- Geometric Illustration Area -->
  <g transform="translate(24, 172)">
    <rect width="512" height="340" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>

    <circle cx="256" cy="170" r="120" fill="none" stroke="#e2e8f0" stroke-width="2"/>
    <circle cx="256" cy="170" r="120" fill="none" stroke="#b45309" stroke-width="2.8" stroke-dasharray="8,4"/>

    <circle cx="256" cy="170" r="4" fill="#78350f"/>
    <text x="256" y="195" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">केन्द्र (360° भचक्र)</text>

    <!-- Point 1: Rahu (Smoky Violet) -->
    <line x1="256" y1="170" x2="160" y2="85" stroke="#4338ca" stroke-width="2"/>
    <circle cx="160" cy="85" r="16" fill="#ede9fe" stroke="#8b5cf6" stroke-width="2"/>
    <text x="160" y="90" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#4338ca" text-anchor="middle">☊ राहु</text>
    <text x="160" y="60" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="800" fill="#4338ca" text-anchor="middle">राहु स्पष्ट अंश</text>
    <text x="160" y="115" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" fill="#64748b" text-anchor="middle">(प्रारब्ध / कर्म बीज)</text>

    <!-- Point 2: Moon (Pearl Blue) -->
    <line x1="256" y1="170" x2="352" y2="85" stroke="#0284c7" stroke-width="2"/>
    <circle cx="352" cy="85" r="16" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
    <text x="352" y="90" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#0369a1" text-anchor="middle">☽ चन्द्र</text>
    <text x="352" y="60" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="800" fill="#0284c7" text-anchor="middle">चन्द्र स्पष्ट अंश</text>
    <text x="352" y="115" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" fill="#64748b" text-anchor="middle">(मन / अनुभूति)</text>

    <!-- Point 3: Bhrigu Bindu (Radiant Golden Crimson Midpoint) -->
    <line x1="256" y1="170" x2="256" y2="50" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="4,2"/>
    <circle cx="256" cy="50" r="20" fill="#fef3c7" stroke="#dc2626" stroke-width="2.5"/>
    <text x="256" y="55" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#dc2626" text-anchor="middle">★ BB</text>
    <text x="256" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle">★ भृगु बिंदु (BB) ★</text>
    <text x="256" y="82" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#78350f" text-anchor="middle">प्रारब्ध प्रकटीकरण बिंदु</text>

    <!-- Arc between Rahu and Moon -->
    <path d="M 160 85 A 120 120 0 0 1 352 85" fill="none" stroke="#dc2626" stroke-width="2"/>
    
    <rect x="20" y="240" width="472" height="85" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text x="256" y="260" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">उदाहरण गणना (Practical Calculation Example):</text>
    <text x="256" y="280" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" fill="#334155" text-anchor="middle">यदि राहु मेष 15° (15°) एवं चन्द्र वृषभ 15° (45°) हो, तो BB = (15 + 45)/2 = 30° (वृषभ 0°)</text>
    <text x="256" y="302" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#dc2626" text-anchor="middle">वृषभ 0° वह संवेदनशील बिंदु है जहां गोचर करते ही घटना का विस्फोट होगा।</text>
  </g>

  <!-- Transit Activation Rules Card -->
  <g transform="translate(24, 522)">
    <rect width="512" height="225" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <text x="256" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ भृगु बिंदु पर गोचर सक्रियण के 3 अचूक नियम ★</text>

    <text x="20" y="52" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#059669">1. ♃ गुरु का BB पर गोचर (Jupiter Transit over BB):</text>
    <text x="20" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• जीवन का सबसे बड़ा भाग्योदय; अप्रत्याशित धन लाभ, विवाह, सन्तान प्राप्ति अथवा प्रतिष्ठा की प्राप्ति।</text>
    <text x="20" y="90" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#64748b">जातक को लगता है कि ईश्वर ने अचानक सारे द्वार खोल दिए हैं।</text>

    <text x="20" y="116" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#dc2626">2. ♄ शनि का BB पर गोचर (Saturn Transit over BB):</text>
    <text x="20" y="136" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• प्रारब्ध कर्म का कठोर शोधन; स्वास्थ्य संकट, कार्यक्षेत्र में भारी परिवर्तन या अत्यधिक दायित्व का भार।</text>
    <text x="20" y="154" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#64748b">धैर्य और धर्म के पालन से यही काल स्थायी नींव का निर्माण करता है।</text>

    <text x="20" y="180" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#7c3aed">3. ☊☋ राहु या केतु का BB पर गोचर (Nodes Transit over BB):</text>
    <text x="20" y="200" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• आकस्मिक दिशा परिवर्तन, विदेश गमन, पुराने भ्रमों का टूटना अथवा असाधारण आध्यात्मिक अनुभव।</text>
  </g>
</svg>"""

# ==============================================================================
# 12. Protocol Flowchart (7-Step Predictive Algorithm)
# ==============================================================================
def make_protocol_flowchart():
    w, h = 560, 770
    steps = [
        ("चरण 1", "जीव कारक (गुरु/शुक्र) की स्थिति व अंश ज्ञात करें", "पुरुष जातक हेतु ♃ गुरु (जीव) एवं स्त्री हेतु ♀ शुक्र की राशि व स्पष्ट अंश देखें।", "#b45309", "#fef3c7"),
        ("चरण 2", "1-5-9 त्रिकोण में स्थित ग्रहों का संयोजन बनाएं", "गुरु जिस दिशा (अग्नि, पृथ्वी, वायु, जल) में है, उस दिशा के शेष दो भावों के ग्रह जोड़ें।", "#0284c7", "#e0f2fe"),
        ("चरण 3", "2-12 भावों के अग्रिम व पृष्ठ प्रभाव (कर्तरी) का परीक्षण", "अग्र (+1 भाव) से भविष्य व पृष्ठ (-1 भाव) से संचित पृष्ठभूमि का आंकलन करें।", "#059669", "#d1fae5"),
        ("चरण 4", "7वें भाव (180° प्रत्यक्ष दृष्टि) के ग्रह का फल जोड़ें", "सामने बैठा ग्रह प्रत्यक्ष रूप से जीवनसाथी, साझेदारी व लोक-व्यवहार को प्रभावित करता है।", "#dc2626", "#fee2e2"),
        ("चरण 5", "अंश-क्रम (Degree Ordering) से ग्रहों का क्रम तय करें", "कम अंश वाला ग्रह आगे एवं अधिक अंश वाला ग्रह पीछे होता है (पीछे वाला आगे की ओर गतिमान)।", "#7c3aed", "#ede9fe"),
        ("चरण 6", "वक्री व राशि-परिवर्तन (Exchange) के प्रभाव को समाहित करें", "वक्री ग्रह पूर्व राशि से भी फल देता है; राशि विनिमय होने पर ग्रह दोनों भावों में फलित होता है।", "#4338ca", "#ede9fe"),
        ("चरण 7", "गुरु प्रगति व शनि-राहु गोचर से अचूक समय (Timing) निकालें", "प्रगतिशील गुरु व गोचरीय शनि जब संबंधित ग्रहों अथवा भृगु बिंदु (BB) पर आएं, तब घटना घटित होती है।", "#047857", "#d1fae5"),
    ]

    cards_svg = []
    card_w = 512
    card_h = 66
    start_y = 96
    gap = 20

    for i, (step_num, title, desc, stroke_col, bg_col) in enumerate(steps):
        cy = start_y + i * (card_h + gap)
        cards_svg.append(f"""
  <g transform="translate(24, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="6" fill="#ffffff" stroke="{stroke_col}" stroke-width="1.5"/>
    <rect width="90" height="{card_h}" rx="6" fill="{bg_col}" stroke="{stroke_col}" stroke-width="0.8"/>
    <text x="45" y="38" text-anchor="middle" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="900" fill="{stroke_col}">{step_num}</text>

    <!-- Details -->
    <text x="105" y="26" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="{stroke_col}">{title}</text>
    <text x="105" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• {desc}</text>
  </g>""")
        if i < len(steps) - 1:
            arrow_y = cy + card_h
            cards_svg.append(f"""
  <line x1="280" y1="{arrow_y}" x2="280" y2="{arrow_y + gap}" stroke="{stroke_col}" stroke-width="2" stroke-dasharray="3,2"/>
  <polygon points="276,{arrow_y + gap - 2} 284,{arrow_y + gap - 2} 280,{arrow_y + gap + 3}" fill="{stroke_col}"/>""")

    cards_str = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("बी.एन.एन. 7-चरणीय फलित निर्णय प्रवाह आरेख", "BNN 7-Step Predictive Algorithm Protocol", "कुण्डली देखते ही 30 सेकंड में सटीक फलादेश करने की शास्त्रीय प्रणाली", 66)}

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="700" width="512" height="48" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="720" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी निष्कर्ष: इन 7 चरणों का क्रमशः पालन करने पर कभी भविष्यवाणी विफल नहीं होती ★</text>
  <text x="280" y="736" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • तंत्र ज्ञान शोध संस्थान (2026)</text>
</svg>"""

def make_vakri_parivartana_chart():
    w, h = 560, 770
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("बी.एन.एन. वक्री ग्रह द्वैत स्थिति एवं राशि परिवर्तन चक्र", "BNN Retrograde Dual Ray Physics &amp; Parivartana Yoga Mutual Exchange", "वक्री ग्रह अपनी वर्तमान राशि एवं 12वें भाव दोनों से पूर्ण त्रिकोण दृष्टि प्रसारित करता है", 66)}

  <!-- Section 1: Retrograde Dual Rays Visual -->
  <g transform="translate(24, 96)">
    <rect width="512" height="300" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <rect width="512" height="30" rx="8" fill="#0f172a"/>
    <text x="256" y="20" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" text-anchor="middle">१. वक्री ग्रह का द्वैत स्थिति प्रभाव (Dual Radiant Positions)</text>

    <!-- Visual Box Left: Current Position -->
    <rect x="25" y="48" width="215" height="110" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.4"/>
    <text x="132" y="70" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#1d4ed8" text-anchor="middle">वर्तमान प्रत्यक्ष राशि (Direct)</text>
    {planet_badge_svg("saturn", 92, 80, 80, 24)}
    <text x="132" y="122" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">मकर राशि (Capricorn)</text>
    <text x="132" y="142" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#0284c7" text-anchor="middle">दक्षिण त्रिकोण (2-6-10) दृष्टि (50%)</text>

    <!-- Backward Retrograde Arrow -->
    <path d="M 245,100 Q 256,65 267,100" fill="none" stroke="#d97706" stroke-width="2.5" stroke-dasharray="4,3"/>
    <polygon points="245,100 248,90 255,95" fill="#d97706"/>
    <text x="256" y="60" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="800" fill="#d97706" text-anchor="middle">वक्री गति</text>

    <!-- Visual Box Right: 12th House Shadow Position -->
    <rect x="272" y="48" width="215" height="110" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.4" stroke-dasharray="4,2"/>
    <text x="379" y="70" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#b45309" text-anchor="middle">12वें भाव की छाया स्थिति (12th Shadow)</text>
    {planet_badge_svg("saturn", 339, 80, 80, 24)}
    <text x="379" y="122" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#78350f" text-anchor="middle">धनु राशि (Sagittarius - 12th)</text>
    <text x="379" y="142" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#b45309" text-anchor="middle">पूर्व त्रिकोण (1-5-9) दृष्टि (50%)</text>

    <!-- Explanatory note inside section 1 -->
    <rect x="20" y="172" width="472" height="112" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text x="256" y="194" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ वक्री ग्रह के 3 मूलभूत नाड़ी नियम ★</text>
    <text x="35" y="218" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">1. द्वैत सक्रियता:</text>
    <text x="125" y="218" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#334155">वक्री ग्रह अपनी वर्तमान राशि और 12वें भाव दोनों में एक साथ उपस्थित माना जाता है।</text>
    <text x="35" y="240" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">2. पूर्व प्रारब्ध:</text>
    <text x="125" y="240" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#334155">वक्री ग्रह जातक के पूर्व-जन्म के अधूरे कार्यों एवं संचित कर्मों की पूर्ति कराता है।</text>
    <text x="35" y="262" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">3. 12वें ग्रह से युति:</text>
    <text x="125" y="262" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#334155">यदि 12वें भाव में कोई ग्रह हो, तो वक्री ग्रह सीधे उसके साथ 100% युति बना लेता है।</text>
  </g>

  <!-- Section 2: Parivartana Yoga (Mutual Exchange) -->
  <g transform="translate(24, 410)">
    <rect width="512" height="215" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.4"/>
    <rect width="512" height="30" rx="8" fill="#064e3b"/>
    <text x="256" y="20" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" text-anchor="middle">२. राशि परिवर्तन योग विनिमय चक्र (Parivartana Exchange)</text>

    <!-- Planet A in Planet B sign -->
    <rect x="25" y="46" width="185" height="85" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.3"/>
    <text x="117" y="66" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#78350f" text-anchor="middle">स्थान A: मकर राशि</text>
    {planet_badge_svg("jupiter", 82, 75, 70, 24)}
    <text x="117" y="118" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#b45309" text-anchor="middle">(गुरु शनि के घर में - नीच)</text>

    <!-- Bidirectional Golden Arc Exchange -->
    <path d="M 218,80 L 294,80" stroke="#059669" stroke-width="3"/>
    <polygon points="218,80 228,75 228,85" fill="#059669"/>
    <polygon points="294,80 284,75 284,85" fill="#059669"/>
    <text x="256" y="70" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="900" fill="#059669" text-anchor="middle">परस्पर</text>
    <text x="256" y="100" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="700" fill="#065f46" text-anchor="middle">विनिमय</text>

    <!-- Planet B in Planet A sign -->
    <rect x="302" y="46" width="185" height="85" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.3"/>
    <text x="394" y="66" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#1d4ed8" text-anchor="middle">स्थान B: धनु राशि</text>
    {planet_badge_svg("saturn", 359, 75, 70, 24)}
    <text x="394" y="118" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1d4ed8" text-anchor="middle">(शनि गुरु के घर में)</text>

    <!-- Result Callout -->
    <rect x="20" y="142" width="472" height="60" rx="6" fill="#ecfdf5" stroke="#10b981" stroke-width="1"/>
    <text x="256" y="162" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#065f46" text-anchor="middle">अचूक फलित: नीच-भंग एवं प्रबल महाभाग्य राजयोग</text>
    <text x="256" y="184" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b" text-anchor="middle">विनिमय के उपरांत गुरु और शनि दोनों अपनी स्वराशि में स्थित माने जाते हैं। नीचत्व पूर्णतः समाप्त हो जाता है।</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="638" width="512" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="660" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी अनुसंधान सूत्र: वक्री एवं परिवर्तन योग का समय सक्रियण ★</text>
  <text x="280" y="682" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• जीवन के पूर्वार्ध (0-30 वर्ष) में प्रत्यक्ष ग्रह का फल मिलता है</text>
  <text x="280" y="702" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• जीवन के उत्तरार्ध (30-60 वर्ष) में 12वें भाव व स्वराशि विनिमय का राजयोग फलित होता है</text>
  <text x="280" y="722" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""

# ==============================================================================
# 14. Saturn Karma Karaka Career & Profession Matrix
# ==============================================================================
def make_career_matrix_chart():
    w, h = 560, 770
    professions = [
        ("saturn", "mercury", "सॉफ्टवेयर, वाणिज्य, बैंकिंग व सीए", "कोडिंग, डेटा एनालिसिस, अकाउंटिंग, वित्तीय प्रबंधन, संवाद व वाणिज्य।", "आईटी, डेटा व वित्तीय क्षेत्र"),
        ("saturn", "mars", "इंजीनियरिंग, रक्षा व शल्य-चिकित्सा", "मैकेनिकल, सिविल, रक्षा सेना, पुलिस, रियल एस्टेट व भारी मशीनरी।", "तकनीकी, रक्षा व निर्माण"),
        ("saturn", "sun", "प्रशासनिक सेवा व सरकारी पद", "आईएएस, लोक नीति, सरकारी ठेका, सार्वजनिक उपक्रम व प्रशासनिक नेतृत्व।", "राजकीय व प्रशासनिक सेवा"),
        ("saturn", "venus", "वास्तुकला, विलासिता, वित्त व कला", "आर्किटेक्चर, ऑटोमोबाइल, आभूषण, फिल्म, होटल व सौंदर्य प्रसाधन।", "विलासिता, कला व वित्त"),
        ("saturn", "jupiter", "न्यायाधीश, विधि, शिक्षण व परामर्श", "न्यायालय, प्रोफेसर, नीति-निर्माता, आध्यात्मिक गुरु व उच्च सलाहकार।", "शिक्षा, न्याय व धर्म-कर्म"),
        ("saturn", "moon", "जल-व्यापार, पर्यटन व आयात-निर्यात", "पर्यटन, खाद्य व पेय, नौसेना, विदेशी व्यापार व सतत स्थानांतरण।", "लॉजिस्टिक्स व हॉस्पिटैलिटी"),
        ("saturn", "rahu", "एआई, रोबोटिक्स व विदेशी बहुराष्ट्रीय", "एआई आर्किटेक्चर, इलेक्ट्रॉनिक्स, बहुराष्ट्रीय कंपनी व विदेशी कार्य।", "अत्याधुनिक उच्च-प्रौद्योगिकी"),
        ("saturn", "ketu", "सूक्ष्म शोध, तंत्र-ज्योतिष व ऑडिटिंग", "गूढ़ शोध, फॉरेंसिक ऑडिट, बुनकर, वस्त्र उद्योग व आध्यात्मिक संस्थाएं।", "शोध, ऑडिट व गुप्त विद्याएं"),
    ]

    cards_svg = []
    card_w, card_h = 250, 115
    for i, (p1, p2, title, desc, sector) in enumerate(professions):
        col = i % 2
        row = i // 2
        cx = 24 + col * (card_w + 12)
        cy = 138 + row * (card_h + 8)

        cards_svg.append(f"""
  <!-- Profession Card {i+1} -->
  <g transform="translate({cx}, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.2"/>
    <rect width="{card_w}" height="28" rx="6" fill="#f8fafc"/>
    <line x1="0" y1="28" x2="{card_w}" y2="28" stroke="#e2e8f0" stroke-width="1"/>

    <!-- Planet Badges -->
    <g transform="translate(8, 2)">
      {planet_badge_svg(p1, 0, 0, 56, 22)}
      <text x="64" y="16" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#d97706">+</text>
      {planet_badge_svg(p2, 75, 0, 56, 22)}
    </g>

    <text x="{card_w - 8}" y="19" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="end">{sector}</text>

    <!-- Title -->
    <text x="10" y="47" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#78350f">{title}</text>

    <!-- Description -->
    <text x="10" y="66" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.8" font-weight="600" fill="#334155">{desc[:38]}</text>
    <text x="10" y="81" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.8" font-weight="600" fill="#334155">{desc[38:80]}</text>

    <rect x="8" y="93" width="{card_w - 16}" height="16" rx="3" fill="#fef3c7"/>
    <text x="{card_w/2}" y="105" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" font-weight="700" fill="#b45309" text-anchor="middle">शनि से 1-5-9 त्रिकोण अथवा 2रे भाव में युति प्रभाव</text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("शनि कर्म-कारक आजीविका एवं व्यवसाय निर्धारण महाचक्र", "Saturn (Karma Karaka) Career, Profession &amp; Livelihood Destiny Matrix", "शनि से 1-5-9 त्रिकोण एवं 2रे भाव में स्थित ग्रह जातक का मुख्य पेशा तय करते हैं", 66)}

  <!-- Master Center Callout -->
  <g transform="translate(24, 94)">
    <rect width="512" height="34" rx="6" fill="#0f172a"/>
    <text x="256" y="22" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" text-anchor="middle">★ शनि (Saturn) = संपूर्ण ब्रह्मांड का प्रधान कर्म एवं आजीविका कारक ★</text>
  </g>

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="642" width="512" height="105" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="664" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ बी.एन.एन. आजीविका निर्धारण के 3 अकाट्य नियम ★</text>
  <text x="280" y="685" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">1. शनि की राशि का तत्व: अग्नि = नेतृत्व, पृथ्वी = उद्योग/निर्माण, वायु = आईटी/बुद्धि, जल = सेवा/विदेश</text>
  <text x="280" y="705" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">2. शनि के निकटतम अंश वाला ग्रह जातक की कार्यप्रणाली की मूल प्रकृति निश्चित करता है</text>
  <text x="280" y="725" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">3. शनि से 2रे भाव का ग्रह आजीविका के माध्यम से होने वाले धन आगमन का स्रोत होता है</text>
</svg>"""

# ==============================================================================
# 15. Marriage, Relationship & Spouse Karaka Chart
# ==============================================================================
def make_marriage_matrix_chart():
    w, h = 560, 770
    male_rules = [
        ("venus", "jupiter", "सुलक्षणा, धर्मपरायण व समृद्ध पत्नी; समय पर सुखद विवाह।"),
        ("venus", "mercury", "वाक्पटु, व्यापार-कुशल, उच्च शिक्षित व युवा दिखने वाली पत्नी।"),
        ("venus", "saturn", "परिपक्व, स्वावलंबी; 28-30 वर्ष पर विवाह उपरांत भाग्योदय।"),
        ("venus", "rahu", "भिन्न संस्कृति/जाति, विदेशी संपर्क, असाधारण रूप-सौंदर्य।"),
        ("venus", "ketu", "आध्यात्मिक रुचि, विरक्ति; अहंकार त्यागने पर सात्विक शांति।"),
    ]
    female_rules = [
        ("mars", "jupiter", "विद्वान, प्रतिष्ठित, धर्मनिष्ठ, रक्षा/न्याय/शिक्षा से जुड़ा पति।"),
        ("mars", "sun", "स्वाभिमानी, उच्च प्रशासनिक अधिकारी, सरकारी सेवा में उच्च पद।"),
        ("mars", "mercury", "तकनीकी इंजीनियर, गणितज्ञ, चतुर व वाक्पटु व्यापारी पति।"),
        ("mars", "saturn", "कठोर परिश्रमी, अनुशासित, आत्मनिर्मित (Self-made); स्थिर स्वभाव।"),
        ("mars", "rahu", "अप्रत्याशित प्रारब्ध; गुरु की दृष्टि होने पर समस्त बाधाएं दूर।"),
    ]

    male_svg = []
    for idx, (p1, p2, text) in enumerate(male_rules):
        male_svg.append(f"""
      <g transform="translate(6, {idx * 68})">
        <rect width="238" height="62" rx="6" fill="#ffffff" stroke="#fbcfe8" stroke-width="1.2"/>
        <g transform="translate(6, 4)">
          {planet_badge_svg(p1, 0, 0, 52, 20)}
          <text x="59" y="15" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#be185d">+</text>
          {planet_badge_svg(p2, 69, 0, 52, 20)}
        </g>
        <text x="6" y="38" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.4" font-weight="600" fill="#1e293b">{text[:32]}</text>
        <text x="6" y="52" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.4" font-weight="600" fill="#1e293b">{text[32:70]}</text>
      </g>""")

    female_svg = []
    for idx, (p1, p2, text) in enumerate(female_rules):
        female_svg.append(f"""
      <g transform="translate(6, {idx * 68})">
        <rect width="238" height="62" rx="6" fill="#ffffff" stroke="#fecaca" stroke-width="1.2"/>
        <g transform="translate(6, 4)">
          {planet_badge_svg(p1, 0, 0, 52, 20)}
          <text x="59" y="15" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#dc2626">+</text>
          {planet_badge_svg(p2, 69, 0, 52, 20)}
        </g>
        <text x="6" y="38" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.4" font-weight="600" fill="#1e293b">{text[:32]}</text>
        <text x="6" y="52" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.4" font-weight="600" fill="#1e293b">{text[32:70]}</text>
      </g>""")

    male_str = "\n".join(male_svg)
    female_str = "\n".join(female_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("विवाह, दांपत्य एवं जीवनसाथी कारक महाचक्र", "BNN Marriage, Relationship &amp; Spouse Timing Architecture", "पुरुष कुंडली: शुक्र (पत्नी कारक) • स्त्री कुंडली: मंगल (पति कारक)", 66)}

  <!-- Left Column: Male Chart -->
  <g transform="translate(24, 96)">
    <rect width="250" height="400" rx="8" fill="#fdf2f8" stroke="#be185d" stroke-width="1.4"/>
    <rect width="250" height="30" rx="8" fill="#9d174d"/>
    <text x="125" y="20" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">पुरुष कुंडली: शुक्र [♀] (पत्नी कारक)</text>
    <g transform="translate(0, 42)">
      {male_str}
    </g>
  </g>

  <!-- Right Column: Female Chart -->
  <g transform="translate(286, 96)">
    <rect width="250" height="400" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.4"/>
    <rect width="250" height="30" rx="8" fill="#991b1b"/>
    <text x="125" y="20" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">स्त्री कुंडली: मंगल [♂] (पति कारक)</text>
    <g transform="translate(0, 42)">
      {female_str}
    </g>
  </g>

  <!-- Timing of Marriage Box -->
  <g transform="translate(24, 508)">
    <rect width="512" height="120" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <text x="256" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#78350f" text-anchor="middle">★ विवाह का सटीक वर्ष निर्धारण (Timing of Marriage) ★</text>
    
    <text x="20" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309">1. गुरु गोचर:</text>
    <text x="85" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">प्रगतिशील गुरु जब जन्मकालिक शुक्र (पुरुष) या मंगल (स्त्री) के ऊपर या 1-5-9 त्रिकोण में आए।</text>

    <text x="20" y="70" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#0284c7">2. शनि स्वीकृति:</text>
    <text x="100" y="70" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">गोचर शनि का त्रिकोण संबंध विवाह को दीर्घकालिक सामाजिक व पारिवारिक स्थायित्व देता है।</text>

    <text x="20" y="92" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#dc2626">3. विलंब सूत्र:</text>
    <text x="90" y="92" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">यदि शुक्र/मंगल पर शनि या केतु की युति/दृष्टि हो तो विवाह 28 वर्ष की आयु के बाद होता है।</text>

    <text x="256" y="112" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">विशेष: गुरु की त्रिकोण दृष्टि समस्त वैवाहिक दोषों का शमन कर अखंड दांपत्य प्रदान करती है।</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="638" width="512" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="660" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी दांपत्य समन्वय सूत्र ★</text>
  <text x="280" y="682" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• वर-वधू की कुंडलियों में गुरु और शुक्र का परस्पर त्रिकोण संबंध सर्वोत्तम माना जाता है</text>
  <text x="280" y="702" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• पति-पत्नी के जन्म ग्रहों का 1-5-9 संरेखण आजीवन मानसिक व आत्मिक एकात्मता देता है</text>
  <text x="280" y="722" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""

# ==============================================================================
# 16. Master Special Yogas Diamond Chart
# ==============================================================================
def make_special_yogas_diamond_chart():
    w, h = 560, 770
    yogas = [
        ("jupiter", "saturn", "ब्रह्म / धर्म-कर्माधिपति योग", "सर्वोच्च सामाजिक प्रतिष्ठा, न्यायाधीश, संस्था प्रमुख, निष्काम कर्म व समाज सुधारक।", "#1d4ed8"),
        ("sun", "mercury", "बुधादित्य एवं मेधा योग", "तीक्ष्ण तार्किक बुद्धि, वित्तीय प्रबंधन, सरकारी सलाहकार, वाणी में प्रखर ओज व यश।", "#c2410c"),
        ("mercury", "venus", "महालक्ष्मी एवं कला योग", "अपार व्यापारिक लाभ, मीडिया, सौन्दर्य, वाक-चातुर्य, संगीत व अखंड धन-वैभव।", "#047857"),
        ("moon", "jupiter", "गजकेसरी नाड़ी योग", "अखंड जनसमर्थन, कीर्ति, परोपकार, धार्मिक यात्राएं, उच्च ज्ञान व उत्तम स्वास्थ्य।", "#0369a1"),
        ("jupiter", "ketu", "गणेश एवं मोक्ष योग", "त्रिकालज्ञ, ज्योतिष-प्रवीण, दिव्य अंतर्ज्ञान, वैराग्य, आध्यात्मिक मुक्ति व तपस्या।", "#78350f"),
        ("saturn", "venus", "भाग्यलक्ष्मी योग", "विवाह उपरांत प्रचंड भाग्योदय, अचल संपत्ति, वाहन सुख, लग्जरी जीवन व स्थिरता।", "#be185d"),
    ]

    cards_svg = []
    card_w, card_h = 250, 160
    for i, (p1, p2, title, desc, accent) in enumerate(yogas):
        col = i % 2
        row = i // 2
        cx = 24 + col * (card_w + 12)
        cy = 96 + row * (card_h + 10)

        cards_svg.append(f"""
  <!-- Special Yoga Card {i+1} -->
  <g transform="translate({cx}, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="8" fill="#ffffff" stroke="{accent}" stroke-width="1.4"/>
    <rect width="{card_w}" height="32" rx="8" fill="#f8fafc"/>
    <line x1="0" y1="32" x2="{card_w}" y2="32" stroke="#e2e8f0" stroke-width="1"/>

    <!-- Planet Badges -->
    <g transform="translate(10, 4)">
      {planet_badge_svg(p1, 0, 0, 60, 24)}
      <text x="69" y="17" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="{accent}">+</text>
      {planet_badge_svg(p2, 80, 0, 60, 24)}
    </g>

    <!-- Yoga Name -->
    <text x="12" y="54" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="900" fill="{accent}">{title}</text>

    <!-- Description -->
    <text x="12" y="76" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.2" font-weight="600" fill="#1e293b">{desc[:36]}</text>
    <text x="12" y="93" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.2" font-weight="600" fill="#1e293b">{desc[36:74]}</text>
    <text x="12" y="110" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.2" font-weight="600" fill="#1e293b">{desc[74:110]}</text>

    <!-- Bottom Pill -->
    <rect x="8" y="128" width="{card_w - 16}" height="22" rx="4" fill="#fef3c7"/>
    <text x="{card_w/2}" y="143" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="800" fill="#b45309" text-anchor="middle">1-5-9 त्रिकोण अथवा एक ही राशि में युति</text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("अष्टादश विशिष्ट नाड़ी राजयोग एवं कर्म-संयोग चक्र", "Master Auspicious Yogas &amp; Divine Planetary Conjunctions in BNN", "ग्रहाणां संवादेन जीवस्य प्रारब्धं प्रकाशते • 6 सर्वोच्च फलदायी नाड़ी राजयोग", 66)}

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="620" width="512" height="128" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="642" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी योगों के सक्रियण एवं भंग होने के शास्त्रीय नियम ★</text>
  <text x="280" y="664" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">1. योग सक्रियण: जब संबंधित ग्रहों के 1-5-9 त्रिकोण में गुरु या शनि का गोचर होता है</text>
  <text x="280" y="684" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#dc2626" text-anchor="middle">2. योग भंग: यदि दो मित्र ग्रहों के बीच राहु या शत्रु ग्रह कम अंशों पर स्थित हो जाए</text>
  <text x="280" y="704" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">3. दोष भंग: किसी भी नकारात्मक योग पर यदि गुरु की 1-5-9 त्रिकोण दृष्टि पड़ जाए तो दोष शांत हो जाता है</text>
  <text x="280" y="724" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.8" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • तंत्र ज्ञान शोध संस्थान (2026)</text>
</svg>"""

# ==============================================================================
# 17. Rahu-Ketu Nodal Axis & Bandhana-Moksha Chart
# ==============================================================================
def make_rahu_ketu_nodal_axis_chart():
    w, h = 560, 770
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("राहु-केतु अक्ष, कालसर्प एवं कर्म-बंधन महाचक्र", "Rahu-Ketu 180° Karmic Nodal Axis &amp; Bandhana-Moksha Dynamics", "राहु भविष्य की संचित तृष्णा (Desire) • केतु पूर्व-जन्म की मुक्ति (Dissolution)", 66)}

  <!-- Central Axis Circle Visual -->
  <g transform="translate(24, 96)">
    <rect width="512" height="300" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <rect width="512" height="28" rx="8" fill="#0f172a"/>
    <text x="256" y="19" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">180° संपात अक्ष: भविष्य भोगेच्छा बनाम पूर्व-कर्म मुक्ति</text>

    <!-- Center 180 Axis Line -->
    <line x1="80" y1="160" x2="432" y2="160" stroke="#78350f" stroke-width="2.5" stroke-dasharray="6,4"/>
    <circle cx="256" cy="160" r="85" fill="none" stroke="#cbd5e1" stroke-width="1.5"/>

    <!-- Rahu Node (Top North) -->
    <g transform="translate(60, 80)">
      <rect width="180" height="65" rx="8" fill="#ede9fe" stroke="#8b5cf6" stroke-width="1.4"/>
      <text x="90" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#4338ca" text-anchor="middle">☊ राहु (Rahu Node)</text>
      <text x="90" y="42" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#1e293b" text-anchor="middle">भविष्य तृष्णा • माया • तकनीकी विस्तार</text>
      <text x="90" y="56" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" font-weight="600" fill="#6d28d9" text-anchor="middle">जातक को खींचने वाला चुंबकीय केंद्र</text>
    </g>

    <!-- Ketu Node (Bottom South) -->
    <g transform="translate(272, 175)">
      <rect width="180" height="65" rx="8" fill="#fef3c7" stroke="#b45309" stroke-width="1.4"/>
      <text x="90" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#78350f" text-anchor="middle">☋ केतु (Ketu Node)</text>
      <text x="90" y="42" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#1e293b" text-anchor="middle">अतीत मुक्ति • वैराग्य • सूक्ष्म ज्ञान</text>
      <text x="90" y="56" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" font-weight="600" fill="#b45309" text-anchor="middle">कर्म ऋण विसर्जन व मोक्ष का द्वार</text>
    </g>

    <!-- Dynamic Curved Arrows connecting them -->
    <path d="M 230,120 Q 256,100 280,120" fill="none" stroke="#dc2626" stroke-width="2"/>
    <text x="256" y="98" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" font-weight="700" fill="#dc2626" text-anchor="middle">प्रारब्ध प्रवाह</text>

    <!-- Bottom summary box inside graphic -->
    <rect x="20" y="250" width="472" height="40" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
    <text x="256" y="268" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#334155" text-anchor="middle">राहु जातक को भौतिक संसार में उलझाता है • केतु जातक को आत्म-साक्षात्कार की ओर धकेलता है</text>
    <text x="256" y="282" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" font-weight="600" fill="#64748b" text-anchor="middle">दोनों का अक्ष 180° पर स्थिर रहकर प्रत्येक कुण्डली का 'कर्म-संतुलन' (Karmic Balance) बनाता है।</text>
  </g>

  <!-- Section 2: Comparative Cards -->
  <g transform="translate(24, 408)">
    <!-- Left Card: Bandhana Yoga -->
    <g transform="translate(0, 0)">
      <rect width="250" height="215" rx="8" fill="#ffffff" stroke="#dc2626" stroke-width="1.4"/>
      <rect width="250" height="28" rx="8" fill="#991b1b"/>
      <text x="125" y="19" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">कालसर्प / कर्म-बंधन योग (Karmic Trap)</text>

      <text x="12" y="52" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#991b1b">१. स्वरूप एवं स्थिति:</text>
      <text x="12" y="70" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">जब समस्त 7 ग्रह राहु और केतु की 180° परिधि</text>
      <text x="12" y="86" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">के एक ही ओर कैद हो जाएं।</text>

      <text x="12" y="112" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#991b1b">२. जीवन पर प्रभाव:</text>
      <text x="12" y="130" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">• आयु 0 से 32 वर्ष: कठोर संघर्ष, मानसिक दबाव।</text>
      <text x="12" y="148" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">• आयु 33 के बाद: असाधारण उत्थान व सफलता।</text>

      <rect x="8" y="172" width="234" height="34" rx="4" fill="#fee2e2"/>
      <text x="125" y="186" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="700" fill="#991b1b" text-anchor="middle">नाड़ी समाधान: सात्विक साधना एवं</text>
      <text x="125" y="200" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="700" fill="#991b1b" text-anchor="middle">कुलदेवता/महादेव की नित्य आराधना।</text>
    </g>

    <!-- Right Card: Moksha Yoga -->
    <g transform="translate(262, 0)">
      <rect width="250" height="215" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.4"/>
      <rect width="250" height="28" rx="8" fill="#065f46"/>
      <text x="125" y="19" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">अमृता / मोक्ष मुक्ति योग (Liberation)</text>

      <text x="12" y="52" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#065f46">१. स्वरूप एवं स्थिति:</text>
      <text x="12" y="70" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">जब गुरु (Jupiter) या शुक्र (Venus) केतु के</text>
      <text x="12" y="86" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">साथ अथवा 1-5-9 त्रिकोण में स्थित हों।</text>

      <text x="12" y="112" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#065f46">२. जीवन पर प्रभाव:</text>
      <text x="12" y="130" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">• पूर्व-पुण्य जागृति: सिद्धियों की स्वतः प्राप्ति।</text>
      <text x="12" y="148" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">• वासना क्षय: आत्मिक शांति एवं परमानंद।</text>

      <rect x="8" y="172" width="234" height="34" rx="4" fill="#d1fae5"/>
      <text x="125" y="186" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="700" fill="#065f46" text-anchor="middle">नाड़ी वरदान: ऐसा जातक समाज के</text>
      <text x="125" y="200" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="700" fill="#065f46" text-anchor="middle">कल्याण हेतु अवतरित मार्गदर्शक होता है।</text>
    </g>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="635" width="512" height="112" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="658" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ राहु-केतु को साधने का स्वर्णिम नाड़ी सूत्र ★</text>
  <text x="280" y="680" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• राहु जिस ग्रह के साथ हो, उस कारकत्व के प्रति असीम भूख उत्पन्न करता है</text>
  <text x="280" y="700" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• केतु जिस ग्रह के साथ हो, उस कारकत्व से भौतिक अलगाव देकर आध्यात्मिक पूर्णता देता है</text>
  <text x="280" y="720" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">• गुरु की दृष्टि राहु के विष को अमृत में और केतु के वैराग्य को आत्मज्ञान में बदल देती है</text>
  <text x="280" y="736" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • तंत्र ज्ञान शोध संस्थान (2026)</text>
</svg>"""

# ==============================================================================
# 18. Planetary Transit Clocks & Event Activation
# ==============================================================================
def make_transits_activation_chart():
    w, h = 560, 770
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("गोचर गति एवं जीवन घटना सक्रियण काल-चक्र", "Planetary Transit Clocks &amp; Event Activation Dynamics in BNN", "धीमी गति वाले ग्रह आधार बनाते हैं • तीव्र गति वाले ग्रह घटना को ट्रिगर करते हैं", 66)}

  <!-- Section 1: Master Clocks (Slow Moving) -->
  <g transform="translate(24, 96)">
    <rect width="512" height="152" rx="8" fill="#ffffff" stroke="#1d4ed8" stroke-width="1.4"/>
    <rect width="512" height="28" rx="8" fill="#0f172a"/>
    <text x="256" y="19" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">१. स्थूल काल प्रवर्तक (Master Clocks - मंद गति ग्रह)</text>

    <!-- Saturn Row -->
    <g transform="translate(16, 36)">
      {planet_badge_svg("saturn", 0, 0, 56, 22)}
      <text x="70" y="15" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#1d4ed8">2.5 वर्ष प्रति राशि (30 वर्ष चक्र)</text>
      <text x="255" y="15" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">कर्म, आजीविका व सामाजिक प्रतिष्ठा का स्थूल आधार</text>
    </g>

    <!-- Rahu/Ketu Row -->
    <g transform="translate(16, 72)">
      {planet_badge_svg("rahu", 0, 0, 56, 22)}
      <text x="70" y="15" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#4338ca">1.5 वर्ष प्रति राशि (18 वर्ष चक्र)</text>
      <text x="255" y="15" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">प्रारब्ध का आकस्मिक मोड़ व कर्म ऋण चुकाने का काल</text>
    </g>

    <!-- Jupiter Row -->
    <g transform="translate(16, 108)">
      {planet_badge_svg("jupiter", 0, 0, 56, 22)}
      <text x="70" y="15" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#b45309">1.0 वर्ष प्रति राशि (12 वर्ष चक्र)</text>
      <text x="255" y="15" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">विवाह, सन्तान, पदोन्नति व भाग्योदय का सटीक वर्ष</text>
    </g>
  </g>

  <!-- Section 2: Trigger Switches (Fast Moving) -->
  <g transform="translate(24, 258)">
    <rect width="512" height="195" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.4"/>
    <rect width="512" height="28" rx="8" fill="#064e3b"/>
    <text x="256" y="19" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">२. सूक्ष्म घटना ट्रिगर (Trigger Switches - तीव्र गति ग्रह)</text>

    <!-- Sun Row -->
    <g transform="translate(16, 36)">
      {planet_badge_svg("sun", 0, 0, 56, 22)}
      <text x="70" y="15" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#c2410c">1 माह प्रति राशि (30 दिन)</text>
      <text x="240" y="15" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">घटना का सटीक माह एवं सरकारी/अधिकारिक स्वीकृति</text>
    </g>

    <!-- Mars Row -->
    <g transform="translate(16, 72)">
      {planet_badge_svg("mars", 0, 0, 56, 22)}
      <text x="70" y="15" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#dc2626">45 दिन प्रति राशि</text>
      <text x="240" y="15" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">ऊर्जा, क्रियान्वयन, भूमि क्रय, अनुबंध व सक्रियता</text>
    </g>

    <!-- Mercury/Venus Row -->
    <g transform="translate(16, 108)">
      {planet_badge_svg("mercury", 0, 0, 56, 22)}
      <text x="70" y="15" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#047857">25-30 दिन प्रति राशि</text>
      <text x="240" y="15" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">वित्तीय लेन-देन, व्यावसायिक पत्र व्यवहार व यात्रा</text>
    </g>

    <!-- Moon Row -->
    <g transform="translate(16, 144)">
      {planet_badge_svg("moon", 0, 0, 56, 22)}
      <text x="70" y="15" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#0369a1">2.25 दिन प्रति राशि (54 घंटे)</text>
      <text x="240" y="15" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">घटना का सटीक दिन एवं जातक का मानसिक संकल्प</text>
    </g>
  </g>

  <!-- Section 3: Predictive Trigger Formula -->
  <g transform="translate(24, 464)">
    <rect width="512" height="155" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.6"/>
    <text x="256" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#78350f" text-anchor="middle">★ अचूक फलित ट्रिगर समीकरण (Master Timing Formula) ★</text>

    <!-- Equation Row -->
    <rect x="15" y="38" width="482" height="42" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
    <text x="256" y="64" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="800" fill="#b45309" text-anchor="middle">
      [शनि की सहमति] + [गुरु का गोचर] + [सूर्य का संक्रमण] + [चन्द्र का गोचर] = निश्चित घटना
    </text>

    <text x="20" y="102" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">• चरण 1 (वर्ष):</text>
    <text x="95" y="102" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#334155">शनि और गुरु मिलकर घटना का वर्ष तय करते हैं।</text>

    <text x="20" y="122" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">• चरण 2 (माह):</text>
    <text x="95" y="122" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#334155">सूर्य जब संबंधित भाव या ग्रह के 1-5-9 त्रिकोण में आए, तो वह माह निश्चित होता है।</text>

    <text x="20" y="142" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">• चरण 3 (दिन):</text>
    <text x="95" y="142" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#334155">चन्द्रमा जब उस राशि से गुजरे, ठीक उसी दिन वह घटना घटित होती है।</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="630" width="512" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="652" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी काल-चक्र निर्णय निष्कर्ष ★</text>
  <text x="280" y="674" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• मंद ग्रह जीवन के स्थायी अध्याय लिखते हैं</text>
  <text x="280" y="694" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• मध्यम ग्रह शुभ अवसरों के द्वार खोलते हैं</text>
  <text x="280" y="714" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">• शीघ्रगामी ग्रह उस द्वार से जातक को अंदर प्रवेश कराते हैं</text>
  <text x="280" y="732" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • तंत्र ज्ञान शोध संस्थान (2026)</text>
</svg>"""

def main():
    print("🚀 Generating all 18 Ultra-Crisp HD Sacred Parchment Diamond Charts for BNN...")
    write_and_verify("bnn_philosophy_hierarchy_chart.svg", make_philosophy_hierarchy())
    write_and_verify("bnn_jeeva_flow_diamond_chart.svg", make_jeeva_flow_chart())
    write_and_verify("bnn_directional_diamond_chart.svg", make_directional_diamond_chart())
    write_and_verify("bnn_kartari_flank_diamond_chart.svg", make_kartari_flank_chart())
    write_and_verify("bnn_karaka_relationship_wheel.svg", make_karaka_relationship_wheel())
    write_and_verify("bnn_elemental_directional_diamond_chart.svg", make_elemental_directional_chart())
    write_and_verify("bnn_jeeva_12bhavas_diamond_chart.svg", make_jeeva_12bhavas_chart())
    write_and_verify("bnn_major_conjunctions_diamond_chart.svg", make_major_conjunctions_chart())
    write_and_verify("bnn_triplet_rajyogas_diamond_chart.svg", make_triplet_rajyogas_chart())
    write_and_verify("bnn_progression_paryaya_chart.svg", make_progression_paryaya_chart())
    write_and_verify("bnn_bhrigu_bindu_diagram.svg", make_bhrigu_bindu_diagram())
    write_and_verify("bnn_protocol_flowchart.svg", make_protocol_flowchart())
    # 6 New Master Explanatory Charts
    write_and_verify("bnn_vakri_parivartana_chart.svg", make_vakri_parivartana_chart())
    write_and_verify("bnn_career_matrix_chart.svg", make_career_matrix_chart())
    write_and_verify("bnn_marriage_matrix_chart.svg", make_marriage_matrix_chart())
    write_and_verify("bnn_special_yogas_diamond_chart.svg", make_special_yogas_diamond_chart())
    write_and_verify("bnn_rahu_ketu_nodal_axis_chart.svg", make_rahu_ketu_nodal_axis_chart())
    write_and_verify("bnn_transits_activation_chart.svg", make_transits_activation_chart())
    print("🎉 All 18 BNN charts generated, validated 100% XML compliant!")

if __name__ == "__main__":
    main()
