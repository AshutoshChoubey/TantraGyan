#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the complete suite of 12 ULTRA-CRISP, HIGH-DEFINITION, SACRED PARCHMENT
SVG Diamond Charts & Diagrams for Bhrigu Nandi Nadi: Karma-Samyojan Sutra.

Invariants:
- 100% Valid XML (all & escaped as &amp;)
- Pure Vector Sharpness: NO filters or feGaussianBlur on text/path groups
- Standard parchment aesthetic matching Vedic Astrology Compendium (lagna_chart, kalpurush_bhavas)
- Tailored 560px width coordinate space for 1:1 crisp rendering in 3D book & mobile web view
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

# ==============================================================================
# 1. Philosophy Hierarchy Chart (5-Tier Decision Model)
# ==============================================================================
def make_philosophy_hierarchy():
    w, h = 560, 750
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("भृगु नंदी नाड़ी का ५-स्तरीय फलित निर्णय पदानुक्रम", "BNN 5-Tier Hierarchical Predictive Architecture", "महर्षि भृगु एवं नंदीश्वर प्रोक्त प्रामाणिक पदानुक्रम • Karaka to Timing Protocol", 66)}

  <!-- Tier 1 -->
  <g transform="translate(24, 96)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#b45309"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर १</text>
    <text x="65" y="64" text-anchor="middle" fill="#fef3c7" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">ग्रह कारकत्व</text>
    
    <text x="145" y="30" fill="#78350f" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">नैसर्गिक ग्रह कारकत्व (Planetary Significations)</text>
    <text x="145" y="52" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700">• गुरु (जीव कारक), शुक्र (स्त्री कारक), शनि (कर्म कारक), सूर्य (आत्मा/पिता)</text>
    <text x="145" y="74" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5">नियम: ग्रह स्वयं व्यक्ति व वस्तु दोनों है; भाव स्वामी की तुलना में कारकत्व प्रधान है।</text>
  </g>

  <!-- Flow Arrow 1 -->
  <path d="M 280 192 L 280 210" stroke="#b45309" stroke-width="2" stroke-dasharray="3,2"/>
  <polygon points="276,208 284,208 280,214" fill="#b45309"/>

  <!-- Tier 2 -->
  <g transform="translate(24, 216)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#0284c7"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर २</text>
    <text x="65" y="64" text-anchor="middle" fill="#e0f2fe" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">१-५-९ त्रिकोण</text>
    
    <text x="145" y="30" fill="#0369a1" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">दिशा-संयोजन त्रिकोण (Directional Harmony)</text>
    <text x="145" y="52" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700">• पूर्व (१,५,९ अग्नि), दक्षिण (२,६,१० पृथ्वी), पश्चिम (३,७,११ वायु), उत्तर (४,८,१२ जल)</text>
    <text x="145" y="74" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5">नियम: समान दिशा के ग्रह एक साथ कार्य करते हैं; नाड़ी में यह मुख्य युति संबंध है।</text>
  </g>

  <!-- Flow Arrow 2 -->
  <path d="M 280 312 L 280 330" stroke="#0284c7" stroke-width="2" stroke-dasharray="3,2"/>
  <polygon points="276,328 284,328 280,334" fill="#0284c7"/>

  <!-- Tier 3 -->
  <g transform="translate(24, 336)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#059669"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर ३</text>
    <text x="65" y="64" text-anchor="middle" fill="#d1fae5" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">२-१२ कर्तरी</text>
    
    <text x="145" y="30" fill="#047857" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">अग्रिम, पृष्ठ एवं कर्तरी वेध (Flank Influences)</text>
    <text x="145" y="52" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700">• अग्र (+१ राशि) भविष्य व गति • पृष्ठ (-१ राशि) अतीत व संचित पृष्ठभूमि</text>
    <text x="145" y="74" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5">नियम: दोनों ओर शुभ = सुरक्षा कवच (सुरक्षा); दोनों ओर पापी = बन्धन योग (रुकावट)।</text>
  </g>

  <!-- Flow Arrow 3 -->
  <path d="M 280 432 L 280 450" stroke="#059669" stroke-width="2" stroke-dasharray="3,2"/>
  <polygon points="276,448 284,448 280,454" fill="#059669"/>

  <!-- Tier 4 -->
  <g transform="translate(24, 456)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#7c3aed"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर ४</text>
    <text x="65" y="64" text-anchor="middle" fill="#ede9fe" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">अंश व विनिमय</text>
    
    <text x="145" y="30" fill="#6d28d9" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">ग्रह अंश-क्रम एवं वक्री विनिमय (Degree Ordering &amp; Retro Swap)</text>
    <text x="145" y="52" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700">• निम्न अंश ग्रह आगे, उच्च अंश पीछे • पीछे वाला ग्रह आगे वाले की ओर गतिमान</text>
    <text x="145" y="74" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5">नियम: वक्री ग्रह का ५०% अस्तित्व पूर्व राशि में होता है; राशि विनिमय से दोहरा फल मिलता है।</text>
  </g>

  <!-- Flow Arrow 4 -->
  <path d="M 280 552 L 280 570" stroke="#7c3aed" stroke-width="2" stroke-dasharray="3,2"/>
  <polygon points="276,568 284,568 280,574" fill="#7c3aed"/>

  <!-- Tier 5 -->
  <g transform="translate(24, 576)">
    <rect width="512" height="96" rx="8" fill="#ffffff" stroke="#dc2626" stroke-width="1.6"/>
    <rect width="130" height="96" rx="8" fill="#dc2626"/>
    <text x="65" y="42" text-anchor="middle" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900">स्तर ५</text>
    <text x="65" y="64" text-anchor="middle" fill="#fee2e2" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">काल निर्धारण</text>
    
    <text x="145" y="30" fill="#b91c1c" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800">प्रगति एवं गोचर काल-निर्धारण (Timing of Events)</text>
    <text x="145" y="52" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700">• गुरु १ वर्ष/राशि प्रगति • शनि ३० वर्ष पर्याय चक्र • भृगु बिंदु (BB) सक्रियण</text>
    <text x="145" y="74" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5">नियम: प्रगतिशील गुरु का जन्मकालिक सूर्य/शुक्र/शनि पर गोचर भाग्योदय कराता है।</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="684" width="512" height="46" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="704" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी सिद्धांत: दशा-अन्तर्दशा की अपेक्षा गोचर-संयोजन से तात्कालिक अचूक फलित होता है ★</text>
  <text x="280" y="720" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">प्रत्येक स्तर क्रमशः विश्लेषित करने पर शत-प्रतिशत सटीक भविष्यवाणी संभव है।</text>
</svg>"""
    return svg

# ==============================================================================
# Helper to draw North Indian Diamond Grid
# ==============================================================================
def draw_north_indian_kundli_polygons(fills, strokes):
    """
    Returns the standard 12 polygons for North Indian Kundli:
    Bounds: x: 20-520, y: 100-600. Center: (270, 350)
    """
    coords = [
        # H1
        ("270,100 395,225 270,350 145,225", 1),
        # H2
        ("20,100 270,100 145,225", 2),
        # H3
        ("20,100 145,225 20,350", 3),
        # H4
        ("20,350 145,225 270,350 145,475", 4),
        # H5
        ("20,350 145,475 20,600", 5),
        # H6
        ("20,600 145,475 270,600", 6),
        # H7
        ("270,350 395,475 270,600 145,475", 7),
        # H8
        ("270,600 395,475 520,600", 8),
        # H9
        ("520,600 395,475 520,350", 9),
        # H10
        ("270,350 395,225 520,350 395,475", 10),
        # H11
        ("520,350 395,225 520,100", 11),
        # H12
        ("520,100 395,225 270,100", 12),
    ]
    svg_parts = []
    for (pts, h_num) in coords:
        f = fills.get(h_num, "#ffffff")
        s = strokes.get(h_num, "#09090b")
        svg_parts.append(f'<polygon points="{pts}" fill="{f}" stroke="{s}" stroke-width="1.8" stroke-linejoin="round"/>')
    # Outer frame square
    svg_parts.append('<rect x="20" y="100" width="500" height="500" fill="none" stroke="#78350f" stroke-width="2.4"/>')
    # Inner diamond frame
    svg_parts.append('<polygon points="270,100 520,350 270,600 20,350" fill="none" stroke="#b45309" stroke-width="1.8"/>')
    return "\n    ".join(svg_parts)

# Rashi centers for text placement
HOUSE_CENTERS = {
    1: (270, 225),
    2: (145, 150),
    3: (70, 225),
    4: (145, 350),
    5: (70, 475),
    6: (145, 545),
    7: (270, 475),
    8: (395, 545),
    9: (470, 475),
    10: (395, 350),
    11: (470, 225),
    12: (395, 150)
}

RASHI_LABEL_POS = {
    1: (270, 125),
    2: (250, 115),
    3: (35, 130),
    4: (160, 250),
    5: (35, 370),
    6: (160, 580),
    7: (270, 375),
    8: (380, 580),
    9: (505, 370),
    10: (380, 250),
    11: (505, 130),
    12: (290, 115)
}

# ==============================================================================
# 2. Jeeva Flow Diamond Chart
# ==============================================================================
def make_jeeva_flow_chart():
    w, h = 560, 770
    fills = {
        1: "url(#kendraGrad)", # Jeeva Lagna (Guru)
        2: "url(#upachayaGrad)", # Agre (+1)
        12: "url(#waterGrad)", # Prishta (-1)
        5: "url(#trikonaGrad)", # Trikona 1
        9: "url(#trikonaGrad)", # Trikona 2
        7: "url(#marakaGrad)", # Samukha 180
    }
    strokes = {
        1: "#b45309",
        2: "#0284c7",
        12: "#7c3aed",
        5: "#059669",
        9: "#059669",
        7: "#dc2626"
    }
    kundli_svg = draw_north_indian_kundli_polygons(fills, strokes)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("उत्तर भारतीय डायमंड चार्ट में जीव-लग्न भाव-प्रवाह", "BNN Jeeva Lagna Counter-Clockwise Momentum &amp; Step-by-Step Flow", "गुरु (जीव) की केंद्रीय स्थिति, १-५-९ त्रिकोण, २-१२ पार्श्व एवं ७वीं प्रत्यक्ष दृष्टि", 66)}

  <!-- Kundli Polygons -->
  <g>
    {kundli_svg}
  </g>

  <!-- Labels for Houses -->
  <!-- H1: Jeeva -->
  <text x="270" y="185" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900" fill="#78350f" text-anchor="middle">★ जीव (गुरु) ★</text>
  <text x="270" y="208" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">१म भाव • स्वयं जातक</text>
  <text x="270" y="230" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" fill="#451a03" text-anchor="middle">शारीरिक अस्तित्व, बुद्धि व आत्मा</text>

  <!-- H2: Agre -->
  <text x="145" y="140" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">अग्र (+१ भाव)</text>
  <text x="145" y="160" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">२रा: धन, वाणी, भविष्य</text>

  <!-- H12: Prishta -->
  <text x="395" y="140" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#6d28d9" text-anchor="middle">पृष्ठ (-१ भाव)</text>
  <text x="395" y="160" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">१२वां: संचित अतीत, व्यय</text>

  <!-- H5: Trikona 1 -->
  <text x="70" y="465" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">त्रिकोण (५म)</text>
  <text x="70" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">पूर्वपुण्य • सन्तान</text>

  <!-- H9: Trikona 2 -->
  <text x="470" y="465" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">त्रिकोण (९म)</text>
  <text x="470" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">भाग्य • धर्म • पिता</text>

  <!-- H7: Samukha -->
  <text x="270" y="460" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#b91c1c" text-anchor="middle">प्रत्यक्ष दृष्टि (७म भाव)</text>
  <text x="270" y="480" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700" fill="#1e293b" text-anchor="middle">१८०° समसप्तक • जीवनसाथी, व्यापार</text>

  <!-- Flow Arrows connecting 1-5-9 and 7 -->
  <path d="M 230 240 Q 140 320 80 430" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="5,3"/>
  <polygon points="76,432 86,436 82,425" fill="#059669"/>

  <path d="M 310 240 Q 400 320 460 430" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="5,3"/>
  <polygon points="458,425 454,436 464,432" fill="#059669"/>

  <path d="M 270 245 L 270 435" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="4,3"/>
  <polygon points="266,435 274,435 270,443" fill="#dc2626"/>

  <!-- Other Bhavas -->
  <text x="70" y="230" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">३रा: पराक्रम</text>
  <text x="145" y="355" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">४था: सुख/माता</text>
  <text x="145" y="550" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">६ठा: रोग/ऋण</text>
  <text x="395" y="550" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">८वां: संकट/गूढ़</text>
  <text x="395" y="355" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">१०वां: कर्म/पद</text>
  <text x="470" y="230" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">११वां: लाभ/इच्छा</text>

  <!-- Bottom Legend Card -->
  <g transform="translate(20, 615)">
    <rect width="520" height="135" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <text x="260" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ भृगु नंदी नाड़ी अग्र-पृष्ठ एवं दृष्टि सूत्र ★</text>
    <text x="260" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">• अग्र नियम (+१ राशि): ग्रह का भविष्य व अगला कदम • पृष्ठ नियम (-१ राशि): संचित अतीत व पृष्ठभूमि बल</text>
    <text x="260" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">• १-५-९ त्रिकोण संबंध: समान दिशा के ग्रह १००% सम्मिश्रित होकर संयुक्त परिणाम देते हैं</text>
    <text x="260" y="96" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b91c1c" text-anchor="middle">• ७वां भाव (१८०°): प्रत्यक्ष दृष्टि — जीवनसाथी, साझेदारी व लोक-व्यवहार में प्रत्यक्ष प्रभाव</text>
    <text x="260" y="118" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">• १२वें व २रे में पापी ग्रह = बन्धन योग • १२वें व २रे में शुभ ग्रह = सुरक्षा कवच (सहज सफलता)</text>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 3. Directional Diamond Chart (4 Directions & 1-5-9)
# ==============================================================================
def make_directional_diamond_chart():
    w, h = 560, 770
    fills = {
        # East (Fire: 1, 5, 9)
        1: "url(#kendraGrad)",
        5: "url(#kendraGrad)",
        9: "url(#kendraGrad)",
        # South (Earth: 2, 6, 10)
        2: "url(#trikonaGrad)",
        6: "url(#trikonaGrad)",
        10: "url(#trikonaGrad)",
        # West (Air: 3, 7, 11)
        3: "url(#upachayaGrad)",
        7: "url(#upachayaGrad)",
        11: "url(#upachayaGrad)",
        # North (Water: 4, 8, 12)
        4: "url(#waterGrad)",
        8: "url(#waterGrad)",
        12: "url(#waterGrad)",
    }
    strokes = {
        1: "#b45309", 5: "#b45309", 9: "#b45309",
        2: "#059669", 6: "#059669", 10: "#059669",
        3: "#0284c7", 7: "#0284c7", 11: "#0284c7",
        4: "#7c3aed", 8: "#7c3aed", 12: "#7c3aed",
    }
    kundli_svg = draw_north_indian_kundli_polygons(fills, strokes)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("भृगु नंदी नाड़ी दिशा-आधारित डायमंड चक्र", "BNN 4 Directional Trines &amp; 1-5-9 Conjunction Matrix", "पूर्व (१,५,९ अग्नि) • दक्षिण (२,६,१० पृथ्वी) • पश्चिम (३,७,११ वायु) • उत्तर (४,८,१२ जल)", 66)}

  <!-- Kundli Polygons -->
  <g>
    {kundli_svg}
  </g>

  <!-- Direction Badges in Kundli -->
  <!-- H1: East / Mesha -->
  <text x="270" y="195" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="900" fill="#78350f" text-anchor="middle">१. पूर्व (अग्नि)</text>
  <text x="270" y="215" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700" fill="#b45309" text-anchor="middle">मेष • धर्म त्रिकोण</text>

  <!-- H5: East / Simha -->
  <text x="70" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">५. पूर्व (अग्नि)</text>
  <text x="70" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">सिंह राशि</text>

  <!-- H9: East / Dhanu -->
  <text x="470" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">९. पूर्व (अग्नि)</text>
  <text x="470" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">धनु राशि</text>

  <!-- South: 2, 6, 10 -->
  <text x="145" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">२. दक्षिण (पृथ्वी)</text>
  <text x="145" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">वृषभ राशि</text>

  <text x="145" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">६. दक्षिण (पृथ्वी)</text>
  <text x="145" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">कन्या राशि</text>

  <text x="395" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">१०. दक्षिण (पृथ्वी)</text>
  <text x="395" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">मकर राशि</text>

  <!-- West: 3, 7, 11 -->
  <text x="70" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">३. पश्चिम (वायु)</text>
  <text x="70" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#0284c7" text-anchor="middle">मिथुन राशि</text>

  <text x="270" y="465" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#0369a1" text-anchor="middle">७. पश्चिम (वायु)</text>
  <text x="270" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="700" fill="#0284c7" text-anchor="middle">तुला • काम त्रिकोण</text>

  <text x="470" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">११. पश्चिम (वायु)</text>
  <text x="470" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#0284c7" text-anchor="middle">कुम्भ राशि</text>

  <!-- North: 4, 8, 12 -->
  <text x="145" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">४. उत्तर (जल)</text>
  <text x="145" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#7c3aed" text-anchor="middle">कर्क राशि</text>

  <text x="395" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">८. उत्तर (जल)</text>
  <text x="395" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#7c3aed" text-anchor="middle">वृश्चिक राशि</text>

  <text x="395" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">१२. उत्तर (जल)</text>
  <text x="395" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#7c3aed" text-anchor="middle">मीन राशि</text>

  <!-- Bottom Legend Card -->
  <g transform="translate(20, 615)">
    <rect width="520" height="135" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <text x="260" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ नाड़ी दिशा-त्रिकोण संयोजन सूत्र (Directional Conjunction Law) ★</text>
    <text x="260" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">• पूर्व (१, ५, ९): मेष, सिंह, धनु = अग्नि तत्व • आत्मा, धर्म, जीवन ऊर्जा, नेतृत्व</text>
    <text x="260" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669" text-anchor="middle">• दक्षिण (२, ६, १०): वृषभ, कन्या, मकर = पृथ्वी तत्व • धन, आजीविका, भौतिक स्थिरता</text>
    <text x="260" y="96" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#0284c7" text-anchor="middle">• पश्चिम (३, ७, ११): मिथुन, तुला, कुम्भ = वायु तत्व • बुद्धि, व्यापार, सामाजिक संबंध</text>
    <text x="260" y="118" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#7c3aed" text-anchor="middle">• उत्तर (४, ८, १२): कर्क, वृश्चिक, मीन = जल तत्व • भावना, अंतर्ज्ञान, वैराग्य, मोक्ष</text>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 4. Kartari & Flank Diamond Chart
# ==============================================================================
def make_kartari_flank_chart():
    w, h = 560, 770
    fills = {
        1: "url(#kendraGrad)", # Center Target Planet
        2: "url(#upachayaGrad)", # Agre (+1)
        12: "url(#waterGrad)", # Prishta (-1)
    }
    strokes = {
        1: "#b45309",
        2: "#0284c7",
        12: "#7c3aed",
    }
    kundli_svg = draw_north_indian_kundli_polygons(fills, strokes)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("अग्रिम, पृष्ठ एवं शुभ/पाप-कर्तरी वेध डायमंड चक्र", "Next (+1) &amp; Rear (-1) Flank Influences &amp; Planetary Siege Mechanics", "किसी भी ग्रह के आगे व पीछे स्थित ग्रहों का जीवन पर नियंत्रणकारी प्रभाव", 66)}

  <!-- Kundli Polygons -->
  <g>
    {kundli_svg}
  </g>

  <!-- H1: Middle Planet -->
  <text x="270" y="195" font-family="'Noto Serif Devanagari', serif" font-size="15" font-weight="900" fill="#78350f" text-anchor="middle">★ मध्य ग्रह (Target) ★</text>
  <text x="270" y="218" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">१म भाव • फलित का केंद्र</text>
  <text x="270" y="238" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" fill="#451a03" text-anchor="middle">(उदा. गुरु = जीव, शनि = कर्म)</text>

  <!-- H2: Front Flank -->
  <text x="145" y="140" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#0369a1" text-anchor="middle">अग्रिम ग्रह (+१ राशि)</text>
  <text x="145" y="160" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">भविष्य, दिशा, अगला कदम</text>

  <!-- H12: Rear Flank -->
  <text x="395" y="140" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#6d28d9" text-anchor="middle">पृष्ठ ग्रह (-१ राशि)</text>
  <text x="395" y="160" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">अतीत, संचित बल, पृष्ठभूमि</text>

  <!-- Flank Pressure Arrows -->
  <path d="M 180 170 L 230 200" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="3,2"/>
  <polygon points="228,194 234,202 224,204" fill="#0284c7"/>

  <path d="M 360 170 L 310 200" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="3,2"/>
  <polygon points="316,204 306,202 312,194" fill="#7c3aed"/>

  <!-- Neutral text in other houses -->
  <text x="70" y="230" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">३रा भाव</text>
  <text x="145" y="355" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">४था भाव</text>
  <text x="70" y="475" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">५वां भाव</text>
  <text x="145" y="550" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">६ठा भाव</text>
  <text x="270" y="475" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">७वां भाव</text>
  <text x="395" y="550" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">८वां भाव</text>
  <text x="470" y="475" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">९वां भाव</text>
  <text x="395" y="355" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">१०वां भाव</text>
  <text x="470" y="230" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#64748b" text-anchor="middle">११वां भाव</text>

  <!-- Bottom Comparison Cards -->
  <g transform="translate(20, 615)">
    <!-- Shubha Kartari -->
    <rect x="0" y="0" width="255" height="135" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.4"/>
    <text x="127" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#047857" text-anchor="middle">🛡️ शुभ कर्तरी योग (Suraksha Kavach)</text>
    <text x="127" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">१२वें में शुक्र/बुध + २रे में गुरु/चन्द्र</text>
    <text x="127" y="70" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#334155" text-anchor="middle">• जातक को हर संकट में दैवीय सुरक्षा मिलती है</text>
    <text x="127" y="90" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#334155" text-anchor="middle">• बिना बड़े श्रम के भी कार्य सहज सिद्ध होते हैं</text>
    <text x="127" y="112" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">परिणाम: सुख, समृद्धि, राजकृपा व सम्मान</text>

    <!-- Papa Kartari -->
    <rect x="265" y="0" width="255" height="135" rx="8" fill="#ffffff" stroke="#dc2626" stroke-width="1.4"/>
    <text x="392" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#b91c1c" text-anchor="middle">⛓️ पाप कर्तरी योग (Bandhana Yoga)</text>
    <text x="392" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">१२वें में शनि/राहु + २रे में मंगल/केतु</text>
    <text x="392" y="70" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#334155" text-anchor="middle">• मध्य ग्रह पिस जाता है; जातक बंधन महसूस करता है</text>
    <text x="392" y="90" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#334155" text-anchor="middle">• आगे बढ़ने पर रुकावट, पीछे मुड़ने पर पछतावा</text>
    <text x="392" y="112" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#b91c1c" text-anchor="middle">परिणाम: विलंब, मानसिक तनाव, संघर्ष</text>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 5. Karaka Relationship Wheel
# ==============================================================================
def make_karaka_relationship_wheel():
    w, h = 560, 770
    planets = [
        ("सूर्य (Sun)", "आत्मा • पिता • शासन • अहंकार", "गुरु, मंगल", "बुध", "शुक्र, शनि, राहु", "#b45309", "#fef3c7"),
        ("चन्द्र (Moon)", "मन • माता • जल • यात्रा • कला", "सूर्य, गुरु", "मंगल, बुध, शुक्र, शनि", "राहु, केतु", "#0284c7", "#e0f2fe"),
        ("मंगल (Mars)", "पराक्रम • भ्राता • रक्त • भूमि • साहस", "सूर्य, चन्द्र, गुरु", "शुक्र, शनि", "बुध, राहु", "#dc2626", "#fee2e2"),
        ("बुध (Mercury)", "बुद्धि • व्यापार • वाणी • शिक्षा • मित्र", "सूर्य, शुक्र, शनि", "मंगल, गुरु", "चन्द्र, राहु", "#059669", "#d1fae5"),
        ("गुरु (Jupiter)", "जीव (पुरुष) • ज्ञान • सन्तान • धर्म", "सूर्य, चन्द्र, मंगल", "शनि, राहु", "शुक्र, बुध", "#d97706", "#fef3c7"),
        ("शुक्र (Venus)", "जीव (स्त्री) • धन • पत्नी • वाहन • विलास", "बुध, शनि, राहु", "मंगल, चन्द्र", "सूर्य, गुरु, केतु", "#db2777", "#fce7f3"),
        ("शनि (Saturn)", "कर्म • आजीविका • विलंब • श्रम • आयु", "बुध, शुक्र, राहु", "गुरु", "सूर्य, चन्द्र, मंगल", "#475569", "#f1f5f9"),
        ("राहु (Rahu)", "भ्रम • विदेश • विस्तार • माया • तकनीक", "बुध, शुक्र, शनि", "गुरु", "सूर्य, चन्द्र, मंगल, केतु", "#4338ca", "#ede9fe"),
        ("केतु (Ketu)", "मोक्ष • संन्यास • त्याग • सूक्ष्म ज्ञान • जड़", "गुरु, मंगल, सूर्य", "शुक्र, शनि", "बुध, राहु, चन्द्र", "#78350f", "#fef3c7"),
    ]

    cards_svg = []
    card_w = 512
    card_h = 58
    start_y = 96
    gap = 9

    for i, (name, karaka, friends, neutral, enemies, stroke_col, bg_col) in enumerate(planets):
        cy = start_y + i * (card_h + gap)
        cards_svg.append(f"""
  <g transform="translate(24, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="6" fill="#ffffff" stroke="{stroke_col}" stroke-width="1.3"/>
    <rect width="115" height="{card_h}" rx="6" fill="{bg_col}" stroke="{stroke_col}" stroke-width="0.8"/>
    <text x="57" y="26" text-anchor="middle" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="{stroke_col}">{name}</text>
    <text x="57" y="44" text-anchor="middle" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="700" fill="#334155">प्रमुख नाड़ी कारक</text>

    <!-- Details -->
    <text x="125" y="22" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="800" fill="#0f172a">कारकत्व: <tspan font-weight="600" fill="#334155">{karaka}</tspan></text>
    <text x="125" y="44" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700">
      <tspan fill="#059669">मित्र: {friends}</tspan> • <tspan fill="#64748b">सम: {neutral}</tspan> • <tspan fill="#dc2626">शत्रु: {enemies}</tspan>
    </text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("नवग्रह नाड़ी कारकत्व एवं त्रि-स्तरीय मैत्री महाचक्र", "Navagraha Nadi Karakatwas &amp; Natural Harmony Matrix", "जीव, कर्म, धन, बुद्धि व मोक्ष के प्राकृतिक नियंत्रक ग्रह", 66)}

  {cards_str}

  <!-- Bottom Summary Footer -->
  <rect x="24" y="700" width="512" height="48" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.2"/>
  <text x="280" y="720" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#78350f" text-anchor="middle">★ नाड़ी सूत्र: मित्र ग्रहों की युति भाग्योदय कराती है, शत्रु ग्रहों का योग संघर्ष पैदा करता है ★</text>
  <text x="280" y="736" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">गुरु-शुक्र दोनों जीव हैं, शनि कर्म है, सूर्य यश है, बुध व्यापार है, राहु भ्रम व केतु मोक्ष है।</text>
</svg>"""
    return svg

# ==============================================================================
# 6. Elemental Directional Diamond Chart
# ==============================================================================
def make_elemental_directional_chart():
    # Similar to directional diamond, but focusing on elemental interactions
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

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("चतुर्विध महाभूत एवं दिशा-संयोजन डायमंड चक्र", "BNN 4 Elemental Trines &amp; Directional Harmony (1-5-9 Samyoga Matrix)", "अग्नि (१,५,९), पृथ्वी (२,६,१०), वायु (३,७,११), जल (४,८,१२) का सम्मिश्रण", 66)}

  <g>
    {kundli_svg}
  </g>

  <!-- Labels -->
  <text x="270" y="195" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="900" fill="#78350f" text-anchor="middle">अग्नि तत्व (१)</text>
  <text x="270" y="215" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">मेष • ऊर्जा व धर्म</text>

  <text x="70" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">अग्नि (५)</text>
  <text x="70" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#b45309" text-anchor="middle">सिंह राशि</text>

  <text x="470" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">अग्नि (९)</text>
  <text x="470" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#b45309" text-anchor="middle">धनु राशि</text>

  <text x="145" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">पृथ्वी (२)</text>
  <text x="145" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">वृषभ • अर्थ</text>

  <text x="145" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">पृथ्वी (६)</text>
  <text x="145" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">कन्या राशि</text>

  <text x="395" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">पृथ्वी (१०)</text>
  <text x="395" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">मकर राशि</text>

  <text x="70" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">वायु (३)</text>
  <text x="70" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#0284c7" text-anchor="middle">मिथुन • काम</text>

  <text x="270" y="465" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#0369a1" text-anchor="middle">वायु तत्व (७)</text>
  <text x="270" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#0284c7" text-anchor="middle">तुला राशि</text>

  <text x="470" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">वायु (११)</text>
  <text x="470" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#0284c7" text-anchor="middle">कुम्भ राशि</text>

  <text x="145" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">जल (४)</text>
  <text x="145" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">कर्क • मोक्ष</text>

  <text x="395" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">जल (८)</text>
  <text x="395" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">वृश्चिक राशि</text>

  <text x="395" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">जल (१२)</text>
  <text x="395" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">मीन राशि</text>

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
    return svg

# ==============================================================================
# 7. Jeeva 12 Bhavas Diamond Chart
# ==============================================================================
def make_jeeva_12bhavas_chart():
    w, h = 560, 770
    fills = {
        1: "url(#kendraGrad)",
        2: "url(#trikonaGrad)",
        3: "url(#upachayaGrad)",
        4: "url(#waterGrad)",
        5: "url(#kendraGrad)",
        6: "url(#trikonaGrad)",
        7: "url(#marakaGrad)",
        8: "url(#waterGrad)",
        9: "url(#kendraGrad)",
        10: "url(#trikonaGrad)",
        11: "url(#upachayaGrad)",
        12: "url(#waterGrad)",
    }
    strokes = {i: "#78350f" for i in range(1, 13)}
    kundli_svg = draw_north_indian_kundli_polygons(fills, strokes)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("जीव लग्न (गुरु) द्वादश भाव सम्पूर्ण फलित चक्र", "Jeeva (Guru) 12 Bhavas Manifestation Architecture", "गुरु जहां बैठता है, वह जातक का 'जीव' है; उस भाव से सम्पूर्ण जीवन संचालित होता है", 66)}

  <g>
    {kundli_svg}
  </g>

  <!-- 12 Bhavas Meaning relative to Guru -->
  <text x="270" y="195" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="900" fill="#78350f" text-anchor="middle">१म: जीव स्वयं</text>
  <text x="270" y="215" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">आत्मज्ञानी, सात्विक, दीर्घायु</text>

  <text x="145" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">२रा: धन/वाणी</text>
  <text x="145" y="165" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">मधुर वक्ता, उत्तम कुल</text>

  <text x="70" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">३रा: पराक्रम</text>
  <text x="70" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#0284c7" text-anchor="middle">लेखक, सहोदर सुख</text>

  <text x="145" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">४था: सुख/गृह</text>
  <text x="145" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">मातृभक्त, वाहन, विद्या</text>

  <text x="70" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">५वां: मन्त्र/सन्तान</text>
  <text x="70" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#b45309" text-anchor="middle">पूर्वपुण्य, उच्च बुद्धि</text>

  <text x="145" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">६ठा: सेवा/आरोग्य</text>
  <text x="145" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">शत्रुहन्ता, ऋणमुक्ति</text>

  <text x="270" y="465" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="800" fill="#b91c1c" text-anchor="middle">७वां: जीवनसाथी</text>
  <text x="270" y="485" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" fill="#dc2626" text-anchor="middle">गुणी पत्नी/पति, व्यापार</text>

  <text x="395" y="545" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">८वां: गूढ़ ज्ञान</text>
  <text x="395" y="565" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#7c3aed" text-anchor="middle">दीर्घायु, वसीयत, साधना</text>

  <text x="470" y="470" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#78350f" text-anchor="middle">९वां: धर्म/भाग्य</text>
  <text x="470" y="490" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#b45309" text-anchor="middle">तीर्थयात्री, पिता-भक्त</text>

  <text x="395" y="345" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">१०वां: आजीविका</text>
  <text x="395" y="365" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#059669" text-anchor="middle">प्रतिष्ठित कर्म, शासन</text>

  <text x="470" y="225" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">११वां: सर्व लाभ</text>
  <text x="470" y="245" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#0284c7" text-anchor="middle">इच्छापूर्ति, आय, सिद्धि</text>

  <text x="395" y="145" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">१२वां: मोक्ष/त्याग</text>
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
    return svg

# ==============================================================================
# 8. Major Conjunctions Diamond Chart
# ==============================================================================
def make_major_conjunctions_chart():
    w, h = 560, 770
    conjunctions = [
        ("गुरु + शनि", "धर्म-कर्माधिपति योग", "न्यायिक पद, सामाजिक प्रतिष्ठा, उच्च कर्मयोग, कर्तव्यपरायणता", "#b45309", "#fef3c7"),
        ("सूर्य + गुरु", "राजकृपा / प्रतिष्ठा योग", "सरकारी सम्मान, उच्च पद, पिता का पूर्ण सहयोग, सात्विक सत्ता", "#d97706", "#fffbeb"),
        ("शुक्र + शनि", "लक्ष्मी-कर्म योग", "स्थिर अचल संपत्ति, विलासिता, व्यापारिक सफलता, ऐश्वर्य", "#059669", "#ecfdf5"),
        ("बुध + शुक्र", "सरस्वती-लक्ष्मी योग", "चतुर व्यापारी, वाक्पटु, कला-संगीत प्रेमी, उच्च एकाउंटिंग/सीए", "#0284c7", "#eff6ff"),
        ("मंगल + शनि", "यांत्रिकी / इंजीनियरिंग योग", "तकनीकी विशेषज्ञ, उद्योगपति, कठिन परिश्रम से शिखर की प्राप्ति", "#dc2626", "#fef2f2"),
        ("शुक्र + केतु", "मुक्ति-लक्ष्मी / संन्यास योग", "आध्यात्मिक समृद्धि, वस्त्र/रसायन व्यापार, वैराग्य में सुख", "#7c3aed", "#faf5ff"),
    ]

    cards_svg = []
    card_w = 512
    card_h = 76
    start_y = 96
    gap = 10

    for i, (planets, yoga, fruit, stroke_col, bg_col) in enumerate(conjunctions):
        cy = start_y + i * (card_h + gap)
        cards_svg.append(f"""
  <g transform="translate(24, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="6" fill="#ffffff" stroke="{stroke_col}" stroke-width="1.4"/>
    <rect width="130" height="{card_h}" rx="6" fill="{bg_col}" stroke="{stroke_col}" stroke-width="0.8"/>
    <text x="65" y="32" text-anchor="middle" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900" fill="{stroke_col}">{planets}</text>
    <text x="65" y="54" text-anchor="middle" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#334155">{yoga}</text>

    <!-- Content -->
    <text x="145" y="28" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="{stroke_col}">{yoga} (Conjunction Fruit)</text>
    <text x="145" y="52" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• {fruit}</text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("बी.एन.एन. प्रमुख द्वि-ग्रहीय राजयोग एवं कर्म-संयोग चक्र", "Master 2-Planet Combinations in Bhrigu Nandi Nadi", "३६ प्रमुख ग्रहीय संयोगों में से शीर्ष ६ शास्त्रीय राजयोग", 66)}

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="625" width="512" height="120" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.3"/>
  <text x="280" y="648" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" fill="#78350f" text-anchor="middle">★ नाड़ी ग्रहीय संयोग गणितीय नियम ★</text>
  <text x="280" y="670" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• एक ही राशि में युति (०°) अथवा १-५-९ त्रिकोण में स्थिति = समान शक्तिशाली फल</text>
  <text x="280" y="692" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">• निम्न अंश वाला ग्रह पूर्ववर्ती एवं उच्च अंश वाला ग्रह परवर्ती प्रभाव डालता है</text>
  <text x="280" y="714" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#6d28d9" text-anchor="middle">• यदि दोनों में से कोई वक्री हो तो पूर्व राशि से भी संयोग प्रभाव की गणना करें</text>
  <text x="280" y="734" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • तंत्र ज्ञान शोध संस्थान</text>
</svg>"""
    return svg

# ==============================================================================
# 9. Triplet Rajyogas Diamond Chart
# ==============================================================================
def make_triplet_rajyogas_chart():
    w, h = 560, 770
    triplets = [
        ("गुरु + शनि + सूर्य", "सर्वोच्च प्रशासनिक योग (IAS / Cabinet)", "गुरु (जीव) + शनि (कर्म) + सूर्य (शासन) = देश/संस्थान का सर्वोच्च नेतृत्व, स्थायी मान-सम्मान व राजसत्ता।", "#b45309", "#fef3c7"),
        ("गुरु + शुक्र + केतु", "ब्रह्मर्षि / आध्यात्मिक शिखर योग", "गुरु (ज्ञान) + शुक्र (तप) + केतु (मोक्ष) = संन्यास, अलौकिक अंतर्ज्ञान, जगद्गुरु पद, निःस्वार्थ लोकमंगल।", "#7c3aed", "#faf5ff"),
        ("शनि + बुध + शुक्र", "महा-व्यापारी योग (कुबेर साम्राज्य)", "शनि (कर्म) + बुध (व्यापार) + शुक्र (धन/लक्ष्मी) = बहुराष्ट्रीय व्यापार, विशाल धन सम्पदा, वैश्विक ब्रांड।", "#059669", "#ecfdf5"),
        ("मंगल + शनि + राहु", "अंतर्राष्ट्रीय तकनीकी / AI योग", "मंगल (यंत्र) + शनि (श्रम/उद्योग) + राहु (विदेशी/सॉफ्टवेयर) = रक्षा तकनीक, एयरोस्पेस, विदेश में बड़ा उद्योग।", "#dc2626", "#fef2f2"),
        ("चन्द्र + केतु + गुरु", "सिद्ध योगी / प्रज्ञा-चक्षु योग", "चन्द्र (मन) + केतु (सूक्ष्म दृष्टि) + गुरु (ईश्वरीय कृपा) = सटीक भविष्यवाणी, त्रिकालज्ञ, निस्पृह तपस्वी।", "#0284c7", "#eff6ff"),
    ]

    cards_svg = []
    card_w = 512
    card_h = 92
    start_y = 96
    gap = 12

    for i, (planets, title, desc, stroke_col, bg_col) in enumerate(triplets):
        cy = start_y + i * (card_h + gap)
        cards_svg.append(f"""
  <g transform="translate(24, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="6" fill="#ffffff" stroke="{stroke_col}" stroke-width="1.5"/>
    <rect width="140" height="{card_h}" rx="6" fill="{bg_col}" stroke="{stroke_col}" stroke-width="0.8"/>
    <text x="70" y="38" text-anchor="middle" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="900" fill="{stroke_col}">{planets}</text>
    <text x="70" y="62" text-anchor="middle" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="700" fill="#475569">त्रि-ग्रहीय संयोग</text>

    <!-- Description -->
    <text x="155" y="30" font-family="'Noto Serif Devanagari', serif" font-size="12.5" font-weight="800" fill="{stroke_col}">{title}</text>
    <text x="155" y="52" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• {desc}</text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("बी.एन.एन. त्रि-ग्रहीय एवं बहु-ग्रहीय महायोग डायमंड चक्र", "Master Triplet Combinations in Bhrigu Nandi Nadi", "Root (बीज), Carrier (माध्यम) एवं Fruit (फल) की शास्त्रीय श्रृंखला", 66)}

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="625" width="512" height="120" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.3"/>
  <text x="280" y="648" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" fill="#78350f" text-anchor="middle">★ त्रि-ग्रहीय संयोजन के ३ मूलभूत घटक ★</text>
  <text x="280" y="670" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">१. मूल कारण (Root): प्रथम ग्रह घटना का बीज व संकल्प निर्धारित करता है</text>
  <text x="280" y="692" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#0284c7" text-anchor="middle">२. माध्यम (Carrier): द्वितीय ग्रह साधन, वातावरण एवं कार्य-प्रणाली प्रदान करता है</text>
  <text x="280" y="714" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">३. अंतिम फल (Fruit): तृतीय ग्रह परिणाम का अंतिम स्वरूप व प्रभाव तय करता है</text>
  <text x="280" y="734" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">सूत्र: तीन ग्रहों का त्रिकोण सम्मिश्रण जातक के जीवन की सबसे बड़ी दिशा तय करता है।</text>
</svg>"""
    return svg

# ==============================================================================
# 10. Progression & Paryaya Chart
# ==============================================================================
def make_progression_paryaya_chart():
    w, h = 560, 770
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("शनि ३०-वर्षीय पर्याय एवं गुरु प्रगति काल-चक्र", "BNN Saturn 30-Year Paryaya Cycles &amp; Jupiter 1-Year Progression Engine", "दशा-महादशा के बिना अचूक घटना समय-निर्धारण (Timing of Events)", 66)}

  <!-- Saturn 3 Paryayas Header -->
  <g transform="translate(24, 96)">
    <rect width="512" height="32" rx="4" fill="#0f172a"/>
    <text x="256" y="21" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" text-anchor="middle">शनि के ३ प्रमुख ३०-वर्षीय पर्याय चक्र (Saturn 30-Year Cycles)</text>
  </g>

  <!-- Paryaya 1 -->
  <g transform="translate(24, 136)">
    <rect width="512" height="88" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.4"/>
    <rect width="130" height="88" rx="8" fill="#e0f2fe"/>
    <text x="65" y="38" text-anchor="middle" fill="#0369a1" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900">प्रथम पर्याय</text>
    <text x="65" y="58" text-anchor="middle" fill="#0284c7" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">आयु ० से ३० वर्ष</text>

    <text x="145" y="28" fill="#0369a1" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800">बाल्यावस्था, शिक्षा, संघर्ष एवं आधार निर्माण</text>
    <text x="145" y="50" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600">• शिक्षा, शारीरिक वृद्धि, पारिवारिक निर्भरता एवं प्रथम कर्म का चयन</text>
    <text x="145" y="70" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9">२८वें-३०वें वर्ष में शनि की पहली वापसी (Saturn Return) जीवन को नई दिशा देती है।</text>
  </g>

  <!-- Paryaya 2 -->
  <g transform="translate(24, 232)">
    <rect width="512" height="88" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <rect width="130" height="88" rx="8" fill="#fef3c7"/>
    <text x="65" y="38" text-anchor="middle" fill="#78350f" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900">द्वितीय पर्याय</text>
    <text x="65" y="58" text-anchor="middle" fill="#b45309" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">आयु ३० से ६० वर्ष</text>

    <text x="145" y="28" fill="#78350f" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800">कर्म विस्तार, पद-प्रतिष्ठा, विवाह, सन्तान एवं गृह</text>
    <text x="145" y="50" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600">• जीवन का सबसे फलदायी काल; आजीविका में स्थायित्व व सामाजिक प्रतिष्ठा</text>
    <text x="145" y="70" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9">५८वें-६०वें वर्ष में शनि की दूसरी वापसी से कर्म चक्र की पूर्णता होती है।</text>
  </g>

  <!-- Paryaya 3 -->
  <g transform="translate(24, 328)">
    <rect width="512" height="88" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="1.4"/>
    <rect width="130" height="88" rx="8" fill="#ede9fe"/>
    <text x="65" y="38" text-anchor="middle" fill="#6d28d9" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900">तृतीय पर्याय</text>
    <text x="65" y="58" text-anchor="middle" fill="#7c3aed" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700">आयु ६० से ९० वर्ष</text>

    <text x="145" y="28" fill="#6d28d9" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800">सेवानिवृत्ति, नाती-पोते, अध्यात्म एवं मोक्ष चिंतन</text>
    <text x="145" y="50" fill="#1e293b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600">• भौतिक उत्तरदायित्वों से मुक्ति, आध्यात्मिक साधना व अंतर्मुखी शांति</text>
    <text x="145" y="70" fill="#64748b" font-family="'Kohinoor Devanagari', sans-serif" font-size="9">संचित कर्मों का अंतिम परिशोधन एवं आत्म-साक्षात्कार।</text>
  </g>

  <!-- Jupiter Progression Header -->
  <g transform="translate(24, 428)">
    <rect width="512" height="32" rx="4" fill="#0f172a"/>
    <text x="256" y="21" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" text-anchor="middle">गुरु १-वर्षीय प्रगति नियम (Jupiter 1-Year Progression)</text>
  </g>

  <!-- Jupiter Rules Card -->
  <g transform="translate(24, 468)">
    <rect width="512" height="155" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.4"/>
    <text x="256" y="26" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ गुरु प्रगति से विवाह, सन्तान एवं भाग्योदय का वर्ष निर्धारण ★</text>
    
    <text x="20" y="54" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669">१. गति:</text>
    <text x="65" y="54" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="600" fill="#1e293b">गुरु प्रति वर्ष ठीक १ राशि (३०°) आगे बढ़ता है (१२ वर्ष में १ परिक्रमा)।</text>

    <text x="20" y="78" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669">२. विवाह वर्ष:</text>
    <text x="100" y="78" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="600" fill="#1e293b">प्रगतिशील गुरु जब जन्मकालिक शुक्र (पुरुष हेतु) या मंगल (स्त्री हेतु) पर आए।</text>

    <text x="20" y="102" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669">३. पदोन्नति:</text>
    <text x="95" y="102" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="600" fill="#1e293b">प्रगतिशील गुरु जब जन्मकालिक शनि अथवा सूर्य के ऊपर या त्रिकोण में गोचर करे।</text>

    <text x="20" y="126" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#059669">४. सन्तान जन्म:</text>
    <text x="105" y="126" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="600" fill="#1e293b">प्रगतिशील गुरु का ५वें भाव या जन्मकालिक गुरु के त्रिकोण में गोचर काल।</text>

    <text x="256" y="146" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">सूत्र: १२, २४, ३६, ४८वें वर्ष में गुरु की वापसी अत्यंत महत्वपूर्ण घटनाक्रम लाती है।</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="635" width="512" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="658" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी काल-निर्धारण सिद्धांत (BNN Event Timing Architecture) ★</text>
  <text x="280" y="680" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• शनि तय करता है घटना की पृष्ठभूमि (स्थूल काल)</text>
  <text x="280" y="700" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• गुरु निर्धारित करता है भाग्योदय का सटीक वर्ष (मध्यम काल)</text>
  <text x="280" y="720" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">• सूर्य व चन्द्र का गोचर निश्चित करता है घटना का सटीक माह एवं दिन (सूक्ष्म काल)</text>
  <text x="280" y="736" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""
    return svg

# ==============================================================================
# 11. Bhrigu Bindu Diagram
# ==============================================================================
def make_bhrigu_bindu_diagram():
    w, h = 560, 770
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("भृगु बिंदु (BB) प्रारब्ध संवाहक बिंदु ज्यामितीय चक्र", "Bhrigu Bindu (BB) Destiny Trigger &amp; Rahu-Moon Midpoint Physics", "गणितीय सूत्र: (राहु स्पष्ट अंश + चन्द्र स्पष्ट अंश) ÷ २ = भृगु बिंदु", 66)}

  <!-- Formula Highlight Card -->
  <g transform="translate(24, 96)">
    <rect width="512" height="66" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.6"/>
    <text x="256" y="28" font-family="'Noto Serif Devanagari', serif" font-size="13" font-weight="900" fill="#78350f" text-anchor="middle">भृगु बिंदु (Bhrigu Bindu - BB) की गणितीय गणना</text>
    <text x="256" y="50" font-family="'Kohinoor Devanagari', sans-serif" font-size="11" font-weight="700" fill="#dc2626" text-anchor="middle">BB = (राहु के निरयण अंश + चन्द्र के निरयण अंश) / २</text>
  </g>

  <!-- Geometric Illustration Circle Area -->
  <g transform="translate(24, 172)">
    <rect width="512" height="340" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>

    <!-- Celestial Longitude Line / Arc -->
    <circle cx="256" cy="170" r="120" fill="none" stroke="#e2e8f0" stroke-width="2"/>
    <circle cx="256" cy="170" r="120" fill="none" stroke="#b45309" stroke-width="2.8" stroke-dasharray="8,4"/>

    <!-- Center Pivot -->
    <circle cx="256" cy="170" r="4" fill="#78350f"/>
    <text x="256" y="195" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">केन्द्र (३६०° भचक्र)</text>

    <!-- Point 1: Rahu (Top Left) -->
    <line x1="256" y1="170" x2="160" y2="85" stroke="#4338ca" stroke-width="2"/>
    <circle cx="160" cy="85" r="14" fill="#4338ca"/>
    <text x="160" y="90" font-family="'Noto Serif Devanagari', serif" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">राहु</text>
    <text x="160" y="60" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="800" fill="#4338ca" text-anchor="middle">राहु स्पष्ट अंश</text>
    <text x="160" y="115" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" fill="#64748b" text-anchor="middle">(प्रारब्ध / कर्म बीज)</text>

    <!-- Point 2: Moon (Top Right) -->
    <line x1="256" y1="170" x2="352" y2="85" stroke="#0284c7" stroke-width="2"/>
    <circle cx="352" cy="85" r="14" fill="#0284c7"/>
    <text x="352" y="90" font-family="'Noto Serif Devanagari', serif" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">चन्द्र</text>
    <text x="352" y="60" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="800" fill="#0284c7" text-anchor="middle">चन्द्र स्पष्ट अंश</text>
    <text x="352" y="115" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" fill="#64748b" text-anchor="middle">(मन / अनुभूति)</text>

    <!-- Point 3: Bhrigu Bindu (Center Top Exact Midpoint) -->
    <line x1="256" y1="170" x2="256" y2="50" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="4,2"/>
    <circle cx="256" cy="50" r="18" fill="#fef3c7" stroke="#dc2626" stroke-width="2.5"/>
    <text x="256" y="55" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#dc2626" text-anchor="middle">BB</text>
    <text x="256" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle">★ भृगु बिंदु (BB) ★</text>
    <text x="256" y="80" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#78350f" text-anchor="middle">प्रारब्ध प्रकटीकरण बिंदु</text>

    <!-- Arc between Rahu and Moon -->
    <path d="M 160 85 A 120 120 0 0 1 352 85" fill="none" stroke="#dc2626" stroke-width="2"/>
    
    <!-- Legend inside geometric box -->
    <rect x="20" y="240" width="472" height="85" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text x="256" y="260" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">उदाहरण गणना (Practical Calculation Example):</text>
    <text x="256" y="280" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" fill="#334155" text-anchor="middle">यदि राहु मेष १५° (१५°) एवं चन्द्र वृषभ १५° (४५°) हो, तो BB = (१५ + ४५)/२ = ३०° (वृषभ ०°)</text>
    <text x="256" y="302" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#dc2626" text-anchor="middle">वृषभ ०° वह संवेदनशील बिंदु है जहां गोचर करते ही घटना का विस्फोट होगा।</text>
  </g>

  <!-- Transit Activation Rules Card -->
  <g transform="translate(24, 522)">
    <rect width="512" height="225" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <text x="256" y="24" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" fill="#78350f" text-anchor="middle">★ भृगु बिंदु पर गोचर सक्रियण के ३ अचूक नियम ★</text>

    <!-- Rule 1 -->
    <text x="20" y="52" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#059669">१. गुरु का BB पर गोचर (Jupiter Transit over BB):</text>
    <text x="20" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• जीवन का सबसे बड़ा भाग्योदय; अप्रत्याशित धन लाभ, विवाह, सन्तान प्राप्ति अथवा प्रतिष्ठा की प्राप्ति।</text>
    <text x="20" y="90" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#64748b">जातक को लगता है कि ईश्वर ने अचानक सारे द्वार खोल दिए हैं।</text>

    <!-- Rule 2 -->
    <text x="20" y="116" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#dc2626">२. शनि का BB पर गोचर (Saturn Transit over BB):</text>
    <text x="20" y="136" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• प्रारब्ध कर्म का कठोर शोधन; स्वास्थ्य संकट, कार्यक्षेत्र में भारी परिवर्तन या अत्यधिक दायित्व का भार।</text>
    <text x="20" y="154" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" fill="#64748b">धैर्य और धर्म के पालन से यही काल स्थायी नींव का निर्माण करता है।</text>

    <!-- Rule 3 -->
    <text x="20" y="180" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#7c3aed">३. राहु या केतु का BB पर गोचर (Nodes Transit over BB):</text>
    <text x="20" y="200" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">• आकस्मिक दिशा परिवर्तन, विदेश गमन, पुराने भ्रमों का टूटना अथवा असाधारण आध्यात्मिक अनुभव।</text>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 12. Protocol Flowchart (7-Step Predictive Algorithm)
# ==============================================================================
def make_protocol_flowchart():
    w, h = 560, 770
    steps = [
        ("चरण १", "जीव कारक (गुरु) की स्थिति व अंश ज्ञात करें", "पुरुष जातक हेतु गुरु (जीव) एवं स्त्री हेतु शुक्र की राशि व स्पष्ट अंश देखें।", "#b45309", "#fef3c7"),
        ("चरण २", "१-५-९ त्रिकोण में स्थित ग्रहों का संयोजन बनाएं", "गुरु जिस दिशा (अग्नि, पृथ्वी, वायु, जल) में है, उस दिशा के शेष दो भावों के ग्रह जोड़ें।", "#0284c7", "#e0f2fe"),
        ("चरण ३", "२-१२ भावों के अग्रिम व पृष्ठ प्रभाव (कर्तरी) का परीक्षण", "अग्र (+१ भाव) से भविष्य व पृष्ठ (-१ भाव) से संचित पृष्ठभूमि का आंकलन करें।", "#059669", "#d1fae5"),
        ("चरण ४", "७वें भाव (१८०° प्रत्यक्ष दृष्टि) के ग्रह का फल जोड़ें", "सामने बैठा ग्रह प्रत्यक्ष रूप से जीवनसाथी, साझेदारी व लोक-व्यवहार को प्रभावित करता है।", "#dc2626", "#fee2e2"),
        ("चरण ५", "अंश-क्रम (Degree Ordering) से ग्रहों का क्रम तय करें", "कम अंश वाला ग्रह आगे एवं अधिक अंश वाला ग्रह पीछे होता है (पीछे वाला आगे की ओर गतिमान)।", "#7c3aed", "#ede9fe"),
        ("चरण ६", "वक्री व राशि-परिवर्तन (Exchange) के प्रभाव को समाहित करें", "वक्री ग्रह पूर्व राशि से भी फल देता है; राशि विनिमय होने पर ग्रह दोनों भावों में फलित होता है।", "#4338ca", "#ede9fe"),
        ("चरण ७", "गुरु प्रगति व शनि-राहु गोचर से अचूक समय (Timing) निकालें", "प्रगतिशील गुरु व गोचरीय शनि जब संबंधित ग्रहों अथवा भृगु बिंदु (BB) पर आएं, तब घटना घटित होती है।", "#047857", "#d1fae5"),
    ]

    cards_svg = []
    card_w = 512
    card_h = 66
    start_y = 96
    gap = 20

    for i, (step_num, title, desc, stroke_col, bg_col) in enumerate(steps):
        cy = start_y + i * (card_h + gap)
        cards_svg.append(f"""
  <!-- {step_num} -->
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

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <!-- Outer Plate Frame -->
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#plateBg)" stroke="#b45309" stroke-width="2" filter="url(#cardPlateShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("बी.एन.एन. ७-चरणीय फलित निर्णय प्रवाह आरेख", "BNN 7-Step Predictive Algorithm Protocol", "कुण्डली देखते ही ३० सेकंड में सटीक फलादेश करने की शास्त्रीय प्रणाली", 66)}

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="700" width="512" height="48" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="720" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">★ नाड़ी निष्कर्ष: इन ७ चरणों का क्रमशः पालन करने पर कभी भविष्यवाणी विफल नहीं होती ★</text>
  <text x="280" y="736" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • तंत्र ज्ञान शोध संस्थान (2026)</text>
</svg>"""
    return svg

def main():
    print("🚀 Generating 12 Ultra-Crisp HD Sacred Parchment Diamond Charts for BNN...")
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
    print("🎉 All 12 charts generated and XML validated successfully!")

if __name__ == "__main__":
    main()
