#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate comprehensive suite of 8 high-definition SVG charts and diagrams
for Bhrigu Nandi Nadi: Karma-Samyojan Sutra.
"""

import os

ICONS_DIR = "/Users/apple/Movies/ap/TantraGyan/assets/icons"
os.makedirs(ICONS_DIR, exist_ok=True)

def write_svg(filename, content):
    filepath = os.path.join(ICONS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filepath} ({len(content)} bytes)")

# -------------------------------------------------------------
# Chart 1: 5-Tier BNN Hierarchical Decision Model
# -------------------------------------------------------------
def make_philosophy_hierarchy_chart():
    width, height = 1000, 840
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" />
      <stop offset="50%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="tier1Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#b45309" /><stop offset="100%" stop-color="#d97706" />
    </linearGradient>
    <linearGradient id="tier2Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0369a1" /><stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
    <linearGradient id="tier3Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#047857" /><stop offset="100%" stop-color="#059669" />
    </linearGradient>
    <linearGradient id="tier4Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6d28d9" /><stop offset="100%" stop-color="#7c3aed" />
    </linearGradient>
    <linearGradient id="tier5Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#be123c" /><stop offset="100%" stop-color="#e11d48" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- Frame -->
  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />
  <rect x="22" y="22" width="{width-44}" height="{height-44}" fill="none" stroke="rgba(217, 119, 6, 0.25)" stroke-width="1" rx="6" />

  <!-- Title Header -->
  <text x="{width/2}" y="55" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800" letter-spacing="1">भृगु नंदी नाड़ी: ५-स्तरीय फलित निर्णय पदानुक्रम</text>
  <text x="{width/2}" y="82" text-anchor="middle" fill="#94a3b8" font-size="14">BNN 5-Tier Hierarchical Predictive Architecture • प्रामाणिक निर्णय संरचना</text>

  <!-- 5 Horizontal Tiers -->
  <!-- Tier 1 -->
  <g transform="translate(60, 110)" filter="url(#shadow)">
    <rect width="880" height="98" rx="10" fill="url(#cardGrad)" stroke="#d97706" stroke-width="1.5" />
    <rect width="180" height="98" rx="10" fill="url(#tier1Grad)" />
    <text x="90" y="42" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">स्तर १ (Level 1)</text>
    <text x="90" y="66" text-anchor="middle" fill="#fef3c7" font-size="13" font-weight="700">कारक चयन</text>
    
    <text x="205" y="38" fill="#fde047" font-size="16" font-weight="800">जीव एवं कर्म कारक का निर्धारण (Primary Karaka Selection)</text>
    <text x="205" y="62" fill="#e2e8f0" font-size="13.5">• पुरुष जातक = गुरु (Jeeva), स्त्री जातक = शुक्र (Female Jeeva) • आजीविका/प्रारब्ध = शनि (Karma Karaka)</text>
    <text x="205" y="84" fill="#94a3b8" font-size="12.5">नियम: बिना लग्न पराधीनता के जातक के अस्तित्व एवं कर्म का प्राथमिक केन्द्र चिन्हित करना।</text>
  </g>

  <!-- Down Connector 1 -->
  <path d="M 500 208 L 500 230" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,4" marker-end="url(#arrow)" />
  <circle cx="500" cy="220" r="4" fill="#f59e0b" />

  <!-- Tier 2 -->
  <g transform="translate(60, 230)" filter="url(#shadow)">
    <rect width="880" height="98" rx="10" fill="url(#cardGrad)" stroke="#0284c7" stroke-width="1.5" />
    <rect width="180" height="98" rx="10" fill="url(#tier2Grad)" />
    <text x="90" y="42" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">स्तर २ (Level 2)</text>
    <text x="90" y="66" text-anchor="middle" fill="#e0f2fe" font-size="13" font-weight="700">दिशा एवं त्रिकोण</text>
    
    <text x="205" y="38" fill="#38bdf8" font-size="16" font-weight="800">१-५-९ दिशा त्रिकोण संबंध (Directional Trine Conjunction • 75%–100%)</text>
    <text x="205" y="62" fill="#e2e8f0" font-size="13.5">• पूर्व (अग्नि: १, ५, ९) • दक्षिण (पृथ्वी: २, ६, १०) • पश्चिम (वायु: ३, ७, ११) • उत्तर (जल: ४, ८, १२)</text>
    <text x="205" y="84" fill="#94a3b8" font-size="12.5">नियम: समान दिशा के ग्रह एक ही कक्ष में बैठे माने जाते हैं — भाव दूरी निरर्थक है।</text>
  </g>

  <!-- Down Connector 2 -->
  <path d="M 500 328 L 500 350" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,4" />
  <circle cx="500" cy="340" r="4" fill="#38bdf8" />

  <!-- Tier 3 -->
  <g transform="translate(60, 350)" filter="url(#shadow)">
    <rect width="880" height="98" rx="10" fill="url(#cardGrad)" stroke="#059669" stroke-width="1.5" />
    <rect width="180" height="98" rx="10" fill="url(#tier3Grad)" />
    <text x="90" y="42" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">स्तर ३ (Level 3)</text>
    <text x="90" y="66" text-anchor="middle" fill="#d1fae5" font-size="13" font-weight="700">सम्मुख व पार्श्व</text>
    
    <text x="205" y="38" fill="#34d399" font-size="16" font-weight="800">१-७ सम्मुख दृष्टि (50%) एवं २/१२ अग्रिम-पृष्ठ संबंध (15%)</text>
    <text x="205" y="62" fill="#e2e8f0" font-size="13.5">• सम्मुख १-७: प्रत्यक्ष कर्म-साक्षात्कार (विपरीत दिशा) • +१ अग्रिम: भावी कदम • -१ पृष्ठ: पूर्व संचित ऋण</text>
    <text x="205" y="84" fill="#94a3b8" font-size="12.5">नियम: शुभ/पाप कर्तरी वेध से जातक के कर्म का संरक्षण या घेराबंदी निर्धारित होती है।</text>
  </g>

  <!-- Down Connector 3 -->
  <path d="M 500 448 L 500 470" stroke="#34d399" stroke-width="2.5" stroke-dasharray="4,4" />
  <circle cx="500" cy="460" r="4" fill="#34d399" />

  <!-- Tier 4 -->
  <g transform="translate(60, 470)" filter="url(#shadow)">
    <rect width="880" height="98" rx="10" fill="url(#cardGrad)" stroke="#7c3aed" stroke-width="1.5" />
    <rect width="180" height="98" rx="10" fill="url(#tier4Grad)" />
    <text x="90" y="42" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">स्तर ४ (Level 4)</text>
    <text x="90" y="66" text-anchor="middle" fill="#ede9fe" font-size="13" font-weight="700">अंश-क्रम व विनिमय</text>
    
    <text x="205" y="38" fill="#c084fc" font-size="16" font-weight="800">ग्रह अंश-क्रम, वक्री विनिमय एवं राशि-परिवर्तन (Degree Ordering & Retro Swap)</text>
    <text x="205" y="62" fill="#e2e8f0" font-size="13.5">• निम्न अंश ग्रह आगे, उच्च अंश ग्रह पीछे (पीछे वाला ग्रह आगे वाले की ओर गतिमान)</text>
    <text x="205" y="84" fill="#94a3b8" font-size="12.5">नियम: वक्री ग्रह का ५०% अस्तित्व पूर्व राशि में होता है; राशि विनिमय से ग्रह दोनों स्थानों पर फल देते हैं।</text>
  </g>

  <!-- Down Connector 4 -->
  <path d="M 500 568 L 500 590" stroke="#c084fc" stroke-width="2.5" stroke-dasharray="4,4" />
  <circle cx="500" cy="580" r="4" fill="#c084fc" />

  <!-- Tier 5 -->
  <g transform="translate(60, 590)" filter="url(#shadow)">
    <rect width="880" height="98" rx="10" fill="url(#cardGrad)" stroke="#e11d48" stroke-width="1.5" />
    <rect width="180" height="98" rx="10" fill="url(#tier5Grad)" />
    <text x="90" y="42" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">स्तर ५ (Level 5)</text>
    <text x="90" y="66" text-anchor="middle" fill="#ffe4e6" font-size="13" font-weight="700">गोचर व भृगु बिंदु</text>
    
    <text x="205" y="38" fill="#fb7185" font-size="16" font-weight="800">पर्याय काल, वार्षिक प्रगति एवं भृगु बिंदु सक्रियण (Paryaya, Progressions & BB)</text>
    <text x="205" y="62" fill="#e2e8f0" font-size="13.5">• शनि ३०-वर्षीय पर्याय (४ चरण) • गुरु १ वर्ष प्रति राशि प्रगति • राहु-चन्द्र मध्य बिंदु = भृगु बिंदु (BB)</text>
    <text x="205" y="84" fill="#94a3b8" font-size="12.5">नियम: जब गोचर का गुरु, शनि या राहु भृगु बिंदु अथवा नेटल त्रिकोण को छूता है, घटना अवश्य घटित होती है।</text>
  </g>

  <!-- Bottom Summary Card -->
  <g transform="translate(60, 715)">
    <rect width="880" height="85" rx="8" fill="#131c2e" stroke="#334155" stroke-width="1" />
    <text x="25" y="32" fill="#fde047" font-size="14.5" font-weight="750">💡 मुख्य फलित सिद्धांत:</text>
    <text x="180" y="32" fill="#cbd5e1" font-size="13.5">बी.एन.एन. में विंशोत्तरी दशा की जगह ग्रहों के परस्पर संयोग, दृष्टि अक्ष एवं गोचर पर्याय से फलित होता है।</text>
    <text x="25" y="60" fill="#94a3b8" font-size="12.5">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</text>
  </g>
</svg>'''
    write_svg("bnn_philosophy_hierarchy_chart.svg", svg)

# -------------------------------------------------------------
# Chart 2: Next/Rear Flank & Kartari Enclosure Diamond Chart
# -------------------------------------------------------------
def make_kartari_flank_diamond_chart():
    width, height = 1000, 920
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <linearGradient id="greenGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399" /><stop offset="100%" stop-color="#059669" />
    </linearGradient>
    <linearGradient id="redGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f87171" /><stop offset="100%" stop-color="#dc2626" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">अग्रिम, पृष्ठ एवं कर्तरी वेध डायमंड चक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">BNN Flank Influences (+1 Next / -1 Rear) &amp; Shubha/Papa Kartari Siege</text>

  <!-- Diamond Kundli Geometry -->
  <!-- Center: cx=500, cy=460, size=520 -->
  <g transform="translate(240, 120)" filter="url(#shadow)">
    <!-- Outer Square -->
    <rect x="0" y="0" width="520" height="520" fill="#0f172a" stroke="#d97706" stroke-width="2.5" />
    
    <!-- Cross Diagonals -->
    <line x1="0" y1="0" x2="520" y2="520" stroke="#d97706" stroke-width="2" />
    <line x1="520" y1="0" x2="0" y2="520" stroke="#d97706" stroke-width="2" />
    
    <!-- Inner Diamond -->
    <polygon points="260,0 520,260 260,520 0,260" fill="#131c2e" stroke="#f59e0b" stroke-width="2" />

    <!-- Center House 1 (Jeeva Lagna) -->
    <polygon points="260,0 390,130 260,260 130,130" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
    <text x="260" y="90" text-anchor="middle" fill="#38bdf8" font-size="22" font-weight="800">गुरु / जीव (H1)</text>
    <text x="260" y="115" text-anchor="middle" fill="#fde047" font-size="14" font-weight="700">केन्द्रीय ग्रह (Jeeva Core)</text>
    <text x="260" y="140" text-anchor="middle" fill="#94a3b8" font-size="12">वर्तमान स्थिति • आत्म चेतना</text>

    <!-- House 2 (Top-Left Triangle: +1 Next House) -->
    <polygon points="0,0 260,0 130,130" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="2.2" />
    <text x="130" y="45" text-anchor="middle" fill="#34d399" font-size="18" font-weight="800">+१ अग्रिम भाव (H2)</text>
    <text x="130" y="68" text-anchor="middle" fill="#fef3c7" font-size="13" font-weight="700">भावी कदम (Next Step)</text>
    <text x="130" y="88" text-anchor="middle" fill="#a7f3d0" font-size="11.5">प्रभाव भार: १५%</text>
    <text x="130" y="106" text-anchor="middle" fill="#94a3b8" font-size="11">शुक्र/बुध = तत्काल सहयोग</text>

    <!-- House 12 (Top-Right Triangle: -1 Rear House) -->
    <polygon points="260,0 520,0 390,130" fill="rgba(244, 63, 94, 0.15)" stroke="#f43f5e" stroke-width="2.2" />
    <text x="390" y="45" text-anchor="middle" fill="#fb7185" font-size="18" font-weight="800">-१ पृष्ठ भाव (H12)</text>
    <text x="390" y="68" text-anchor="middle" fill="#fef3c7" font-size="13" font-weight="700">संचित प्रारब्ध (Rear Foot)</text>
    <text x="390" y="88" text-anchor="middle" fill="#fecdd3" font-size="11.5">प्रभाव भार: १५%</text>
    <text x="390" y="106" text-anchor="middle" fill="#94a3b8" font-size="11">राहु/शनि = पूर्व जन्म ऋण</text>

    <!-- House 7 (Bottom Center Diamond) -->
    <polygon points="260,260 390,390 260,520 130,390" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
    <text x="260" y="375" text-anchor="middle" fill="#fde047" font-size="18" font-weight="800">१-७ सम्मुख भाव (H7)</text>
    <text x="260" y="398" text-anchor="middle" fill="#e2e8f0" font-size="13">विपरीत दिशा • ५०% दृष्टि</text>
    <text x="260" y="418" text-anchor="middle" fill="#94a3b8" font-size="11.5">प्रत्यक्ष आमने-सामने कर्म-साक्षात्कार</text>

    <!-- House 5 (Left Diamond) -->
    <polygon points="0,260 130,130 260,260 130,390" fill="#131c2e" stroke="#38bdf8" stroke-width="1.5" />
    <text x="130" y="245" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="800">५म त्रिकोण (H5)</text>
    <text x="130" y="268" text-anchor="middle" fill="#cbd5e1" font-size="12">पूर्वपुण्य • ७५% युति</text>

    <!-- House 9 (Right Diamond) -->
    <polygon points="520,260 390,130 260,260 390,390" fill="#131c2e" stroke="#38bdf8" stroke-width="1.5" />
    <text x="390" y="245" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="800">९म त्रिकोण (H9)</text>
    <text x="390" y="268" text-anchor="middle" fill="#cbd5e1" font-size="12">भाग्य-गुरु • ७५% युति</text>

    <!-- Visual Kartari Arcs -->
    <!-- Green Flank Arrow from H2 -->
    <path d="M 170 120 Q 210 150 220 140" fill="none" stroke="#10b981" stroke-width="3" marker-end="url(#arrow)" />
    <!-- Red Flank Arrow from H12 -->
    <path d="M 350 120 Q 310 150 300 140" fill="none" stroke="#f43f5e" stroke-width="3" />
  </g>

  <!-- Left Callout Box: Shubha Kartari -->
  <g transform="translate(45, 680)" filter="url(#shadow)">
    <rect width="435" height="195" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.8" />
    <rect width="435" height="38" rx="10" fill="url(#greenGlow)" />
    <text x="217" y="26" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="800">✨ शुभ-कर्तरी वेध (Shubha-Kartari Protection)</text>
    
    <text x="20" y="65" fill="#fde047" font-size="13.5" font-weight="700">• संरचना: ग्रह के २रे भाव में शुक्र एवं १२वें में बुध/गुरु</text>
    <text x="20" y="90" fill="#e2e8f0" font-size="13">• परिणाम: जीव को दोनों ओर से सुरक्षा, धन एवं सम्बल</text>
    <text x="20" y="115" fill="#cbd5e1" font-size="12.5">• आगामी मार्ग सुगम होता है, विगत कर्म से रक्षा मिलती है</text>
    <text x="20" y="140" fill="#34d399" font-size="12.5">• व्यापार एवं जीवन में बाधाएं स्वतः समाप्त हो जाती हैं</text>
    <text x="20" y="170" fill="#94a3b8" font-size="11.5">सूत्र: "द्वितीये द्वादशे सौम्यैः संरक्षितो जीवः सुखं लभते"</text>
  </g>

  <!-- Right Callout Box: Papa Kartari -->
  <g transform="translate(520, 680)" filter="url(#shadow)">
    <rect width="435" height="195" rx="10" fill="#0f172a" stroke="#f43f5e" stroke-width="1.8" />
    <rect width="435" height="38" rx="10" fill="url(#redGlow)" />
    <text x="217" y="26" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="800">⚔️ पाप-कर्तरी वेध (Papa-Kartari Karmic Siege)</text>
    
    <text x="20" y="65" fill="#fca5a5" font-size="13.5" font-weight="700">• संरचना: ग्रह के २रे भाव में राहु/मंगल एवं १२वें में केतु/शनि</text>
    <text x="20" y="90" fill="#e2e8f0" font-size="13">• परिणाम: जीव दोनों ओर से क्रूर ग्रहों से घिर जाता है (घेराबंदी)</text>
    <text x="20" y="115" fill="#cbd5e1" font-size="12.5">• आगे बढ़ने पर रुकावट (+१), पीछे लौटने पर अपराध-बोध (-१)</text>
    <text x="20" y="140" fill="#f87171" font-size="12.5">• समाधान: जब गोचर का गुरु २रे या १२वें पापी को पार करता है</text>
    <text x="20" y="170" fill="#94a3b8" font-size="11.5">सूत्र: "पापैः पाशितो जीवः संकटे भ्रमति यावद् गुरुगोचरः"</text>
  </g>
</svg>'''
    write_svg("bnn_kartari_flank_diamond_chart.svg", svg)

# -------------------------------------------------------------
# Chart 3: Navagraha Nadi Karaka & Relationship Matrix
# -------------------------------------------------------------
def make_karaka_relationship_wheel():
    width, height = 1000, 960
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">नवग्रह नाड़ी कारकत्व एवं त्रि-स्तरीय मैत्री महाचक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">Navagraha Nadi Karakatwas &amp; Planetary Synergy Matrix</text>

  <!-- 3x3 Grid of 9 Planets Cards -->
  <!-- Row 1 -->
  <!-- 1. Surya -->
  <g transform="translate(50, 110)" filter="url(#shadow)">
    <rect width="280" height="235" rx="10" fill="#1e1b4b" stroke="#f59e0b" stroke-width="1.8" />
    <rect width="280" height="38" rx="10" fill="#b45309" />
    <text x="140" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">☀️ सूर्य (Surya) • पिता/आत्मा</text>
    <text x="20" y="65" fill="#fde047" font-size="13.5" font-weight="700">तत्व: अग्नि • दिशा: पूर्व</text>
    <text x="20" y="88" fill="#e2e8f0" font-size="13">नाड़ी कारक: पिता, आत्मा, राजसत्ता, यश, औषधि, नेत्र, जीवन-ऊर्जा</text>
    <text x="20" y="132" fill="#34d399" font-size="12.5">✅ मित्र: गुरु, मंगल, चन्द्र</text>
    <text x="20" y="154" fill="#fbbf24" font-size="12.5">⚖️ सम: बुध</text>
    <text x="20" y="176" fill="#f87171" font-size="12.5">❌ शत्रु: शनि, शुक्र, राहु, केतु</text>
    <text x="20" y="210" fill="#94a3b8" font-size="11.5">नाड़ी सूत्र: सूर्य+गुरु = राजयोग, सूर्य+शनि = पिता मतभेद</text>
  </g>

  <!-- 2. Chandra -->
  <g transform="translate(360, 110)" filter="url(#shadow)">
    <rect width="280" height="235" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8" />
    <rect width="280" height="38" rx="10" fill="#0284c7" />
    <text x="140" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">🌙 चन्द्र (Chandra) • मन/माता</text>
    <text x="20" y="65" fill="#38bdf8" font-size="13.5" font-weight="700">तत्व: जल • दिशा: उत्तर</text>
    <text x="20" y="88" fill="#e2e8f0" font-size="13">नाड़ी कारक: माता, मन, द्रव्य, परिवर्तन, गति, विदेश प्रवास, कला, दूध</text>
    <text x="20" y="132" fill="#34d399" font-size="12.5">✅ मित्र: सूर्य, बुध</text>
    <text x="20" y="154" fill="#fbbf24" font-size="12.5">⚖️ सम: मंगल, गुरु, शुक्र, शनि</text>
    <text x="20" y="176" fill="#f87171" font-size="12.5">❌ शत्रु: राहु, केतु</text>
    <text x="20" y="210" fill="#94a3b8" font-size="11.5">नाड़ी सूत्र: चन्द्र+शनि = प्रवास, चन्द्र+शुक्र = व्यय/सौन्दर्य</text>
  </g>

  <!-- 3. Mangala -->
  <g transform="translate(670, 110)" filter="url(#shadow)">
    <rect width="280" height="235" rx="10" fill="#1c1917" stroke="#ef4444" stroke-width="1.8" />
    <rect width="280" height="38" rx="10" fill="#b91c1c" />
    <text x="140" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">♂️ मंगल (Mangala) • भ्राता/पति</text>
    <text x="20" y="65" fill="#fca5a5" font-size="13.5" font-weight="700">तत्व: अग्नि • दिशा: पूर्व</text>
    <text x="20" y="88" fill="#e2e8f0" font-size="13">नाड़ी कारक: भ्राता, पति (स्त्री कुण्डली), रक्त, पराक्रम, भूमि, शस्त्र, तकनीकी</text>
    <text x="20" y="132" fill="#34d399" font-size="12.5">✅ मित्र: सूर्य, चन्द्र, गुरु</text>
    <text x="20" y="154" fill="#fbbf24" font-size="12.5">⚖️ सम: शुक्र, शनि</text>
    <text x="20" y="176" fill="#f87171" font-size="12.5">❌ शत्रु: बुध, राहु, केतु</text>
    <text x="20" y="210" fill="#94a3b8" font-size="11.5">नाड़ी सूत्र: मंगल+गुरु = तेजस्वी, मंगल+बुध = भूमि विवाद</text>
  </g>

  <!-- Row 2 -->
  <!-- 4. Budha -->
  <g transform="translate(50, 375)" filter="url(#shadow)">
    <rect width="280" height="235" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.8" />
    <rect width="280" height="38" rx="10" fill="#047857" />
    <text x="140" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">☿ बुध (Budha) • बुद्धि/व्यापार</text>
    <text x="20" y="65" fill="#6ee7b7" font-size="13.5" font-weight="700">तत्व: पृथ्वी • दिशा: दक्षिण</text>
    <text x="20" y="88" fill="#e2e8f0" font-size="13">नाड़ी कारक: बुद्धि, वाणी, व्यापार, मातुल, मित्र, विद्या, लेखन, हास्य, वाणिज्य</text>
    <text x="20" y="132" fill="#34d399" font-size="12.5">✅ मित्र: सूर्य, शुक्र, राहु</text>
    <text x="20" y="154" fill="#fbbf24" font-size="12.5">⚖️ सम: मंगल, गुरु, शनि</text>
    <text x="20" y="176" fill="#f87171" font-size="12.5">❌ शत्रु: चन्द्र</text>
    <text x="20" y="210" fill="#94a3b8" font-size="11.5">नाड़ी सूत्र: बुध+शुक्र = व्यापार सिद्धि, बुध+राहु = सॉफ्टवेयर</text>
  </g>

  <!-- 5. Guru (Center Spotlight) -->
  <g transform="translate(360, 375)" filter="url(#shadow)">
    <rect width="280" height="235" rx="10" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2.5" />
    <rect width="280" height="38" rx="10" fill="url(#goldGrad)" />
    <text x="140" y="26" text-anchor="middle" fill="#0f172a" font-size="16" font-weight="900">♃ गुरु (Guru) • पुरुष जीव कारक</text>
    <text x="20" y="65" fill="#fde047" font-size="13.5" font-weight="800">तत्व: आकाश/ईथर • केन्द्र बिंदु</text>
    <text x="20" y="88" fill="#ffffff" font-size="13">नाड़ी कारक: पुरुष जीव स्वयं, ज्ञान, संतति, धर्म, देवकृपा, विस्तार, सम्मान</text>
    <text x="20" y="132" fill="#34d399" font-size="12.5">✅ मित्र: सूर्य, चन्द्र, मंगल</text>
    <text x="20" y="154" fill="#fbbf24" font-size="12.5">⚖️ सम: शनि, केतु</text>
    <text x="20" y="176" fill="#f87171" font-size="12.5">❌ शत्रु: बुध, शुक्र, राहु</text>
    <text x="20" y="210" fill="#fef08a" font-size="11.5">नाड़ी सूत्र: गुरु+शनि = धर्म-कर्माधिपति, गुरु+केतु = मोक्ष</text>
  </g>

  <!-- 6. Shukra -->
  <g transform="translate(670, 375)" filter="url(#shadow)">
    <rect width="280" height="235" rx="10" fill="#131c2e" stroke="#ec4899" stroke-width="1.8" />
    <rect width="280" height="38" rx="10" fill="#be185d" />
    <text x="140" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">♀ शुक्र (Shukra) • स्त्री जीव/धन</text>
    <text x="20" y="65" fill="#f472b6" font-size="13.5" font-weight="700">तत्व: जल • दिशा: उत्तर</text>
    <text x="20" y="88" fill="#e2e8f0" font-size="13">नाड़ी कारक: जाया, स्त्री जीव, धन, विलास, वाहन, कला, सौन्दर्य, सुगन्ध</text>
    <text x="20" y="132" fill="#34d399" font-size="12.5">✅ मित्र: बुध, शनि, राहु, केतु</text>
    <text x="20" y="154" fill="#fbbf24" font-size="12.5">⚖️ सम: मंगल</text>
    <text x="20" y="176" fill="#f87171" font-size="12.5">❌ शत्रु: सूर्य, चन्द्र, गुरु</text>
    <text x="20" y="210" fill="#94a3b8" font-size="11.5">नाड़ी सूत्र: शुक्र+शनि = भाग्यलक्ष्मी, शुक्र+मंगल = आकर्षण</text>
  </g>

  <!-- Row 3 -->
  <!-- 7. Shani -->
  <g transform="translate(50, 640)" filter="url(#shadow)">
    <rect width="280" height="235" rx="10" fill="#0f172a" stroke="#64748b" stroke-width="1.8" />
    <rect width="280" height="38" rx="10" fill="#334155" />
    <text x="140" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">♄ शनि (Shani) • कर्म/प्रारब्ध</text>
    <text x="20" y="65" fill="#cbd5e1" font-size="13.5" font-weight="700">तत्व: वायु • दिशा: पश्चिम</text>
    <text x="20" y="88" fill="#e2e8f0" font-size="13">नाड़ी कारक: कर्म, आजीविका, प्रारब्ध संपादन, श्रम, विलम्ब, सेवा, अनुशासन</text>
    <text x="20" y="132" fill="#34d399" font-size="12.5">✅ मित्र: बुध, शुक्र, राहु</text>
    <text x="20" y="154" fill="#fbbf24" font-size="12.5">⚖️ सम: गुरु</text>
    <text x="20" y="176" fill="#f87171" font-size="12.5">❌ शत्रु: सूर्य, चन्द्र, मंगल, केतु</text>
    <text x="20" y="210" fill="#94a3b8" font-size="11.5">नाड़ी सूत्र: शनि+बुध = वाणिज्य, शनि+राहु = तकनीकी उद्योग</text>
  </g>

  <!-- 8. Rahu -->
  <g transform="translate(360, 640)" filter="url(#shadow)">
    <rect width="280" height="235" rx="10" fill="#090d16" stroke="#8b5cf6" stroke-width="1.8" />
    <rect width="280" height="38" rx="10" fill="#6d28d9" />
    <text x="140" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">☊ राहु (Rahu) • माया/विस्तार</text>
    <text x="20" y="65" fill="#c4b5fd" font-size="13.5" font-weight="700">छाया ग्रह • तमोगुण • दक्षिण/पश्चिम</text>
    <text x="20" y="88" fill="#e2e8f0" font-size="13">नाड़ी कारक: पितामह, माया, विदेशी संस्कृति, कृत्रिमता, बड़ा आकार, भ्रम, शोध</text>
    <text x="20" y="132" fill="#34d399" font-size="12.5">✅ मित्र: बुध, शुक्र, शनि</text>
    <text x="20" y="154" fill="#fbbf24" font-size="12.5">⚖️ सम: —</text>
    <text x="20" y="176" fill="#f87171" font-size="12.5">❌ शत्रु: सूर्य, चन्द्र, मंगल, गुरु</text>
    <text x="20" y="210" fill="#94a3b8" font-size="11.5">नाड़ी सूत्र: राहु+गुरु = गुरु-चांडाल, राहु+बुध = गुप्त विद्या/AI</text>
  </g>

  <!-- 9. Ketu -->
  <g transform="translate(670, 640)" filter="url(#shadow)">
    <rect width="280" height="235" rx="10" fill="#18181b" stroke="#e11d48" stroke-width="1.8" />
    <rect width="280" height="38" rx="10" fill="#9f1239" />
    <text x="140" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">☋ केतु (Ketu) • मोक्ष/ध्वज</text>
    <text x="20" y="65" fill="#fda4af" font-size="13.5" font-weight="700">छाया ग्रह • मोक्ष तत्व • उत्तर</text>
    <text x="20" y="88" fill="#e2e8f0" font-size="13">नाड़ी कारक: मातामह, मोक्ष, विरक्ति, संन्यास, ज्योतिष, सूक्ष्म ज्ञान, कानूनी बाधा</text>
    <text x="20" y="132" fill="#34d399" font-size="12.5">✅ मित्र: शुक्र, गुरु (अध्यात्म)</text>
    <text x="20" y="154" fill="#fbbf24" font-size="12.5">⚖️ सम: बुध</text>
    <text x="20" y="176" fill="#f87171" font-size="12.5">❌ शत्रु: सूर्य, चन्द्र, मंगल, शनि</text>
    <text x="20" y="210" fill="#94a3b8" font-size="11.5">नाड़ी सूत्र: केतु+गुरु = गणेश योग, केतु+शनि = कर्म संन्यास</text>
  </g>

  <!-- Bottom Strip -->
  <text x="{width/2}" y="915" text-anchor="middle" fill="#94a3b8" font-size="13">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान</text>
</svg>'''
    write_svg("bnn_karaka_relationship_wheel.svg", svg)

# -------------------------------------------------------------
# Chart 4: 4 Elements & Directional Conjunctions Diamond Chart
# -------------------------------------------------------------
def make_elemental_directional_diamond_chart():
    width, height = 1000, 920
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">चतुर्विध महाभूत एवं दिशा-संयोजन डायमंड चक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">BNN 4 Elemental Trines &amp; Directional Harmony (1-5-9 Samyoga Matrix)</text>

  <!-- Diamond Kundli Layout: Center (500, 430), Size 500 -->
  <g transform="translate(250, 110)" filter="url(#shadow)">
    <!-- Outer Square -->
    <rect x="0" y="0" width="500" height="500" fill="#0f172a" stroke="#d97706" stroke-width="2.5" />
    
    <!-- Diagonals -->
    <line x1="0" y1="0" x2="500" y2="500" stroke="#d97706" stroke-width="2" />
    <line x1="500" y1="0" x2="0" y2="500" stroke="#d97706" stroke-width="2" />
    
    <!-- Inner Diamond -->
    <polygon points="250,0 500,250 250,500 0,250" fill="#131c2e" stroke="#f59e0b" stroke-width="2" />

    <!-- 1. Lagna (Top Center Diamond) -> Aries (1) FIRE / EAST -->
    <polygon points="250,0 375,125 250,250 125,125" fill="rgba(239, 68, 68, 0.22)" stroke="#ef4444" stroke-width="2" />
    <text x="250" y="85" text-anchor="middle" fill="#fca5a5" font-size="18" font-weight="800">१. मेष (Aries)</text>
    <text x="250" y="110" text-anchor="middle" fill="#fde047" font-size="14" font-weight="700">अग्नि तत्व • पूर्व</text>
    <text x="250" y="132" text-anchor="middle" fill="#cbd5e1" font-size="12">त्रिकोण युति: ५, ९</text>

    <!-- 2. House 2 (Top Left Triangle) -> Taurus (2) EARTH / SOUTH -->
    <polygon points="0,0 250,0 125,125" fill="rgba(245, 158, 11, 0.18)" stroke="#f59e0b" stroke-width="1.8" />
    <text x="125" y="45" text-anchor="middle" fill="#fde68a" font-size="15" font-weight="800">२. वृषभ (Taurus)</text>
    <text x="125" y="68" text-anchor="middle" fill="#fbbf24" font-size="12">पृथ्वी • दक्षिण</text>

    <!-- 12. House 12 (Top Right Triangle) -> Pisces (12) WATER / NORTH -->
    <polygon points="250,0 500,0 375,125" fill="rgba(6, 182, 212, 0.18)" stroke="#06b6d4" stroke-width="1.8" />
    <text x="375" y="45" text-anchor="middle" fill="#a5f3fc" font-size="15" font-weight="800">१२. मीन (Pisces)</text>
    <text x="375" y="68" text-anchor="middle" fill="#22d3ee" font-size="12">जल • उत्तर</text>

    <!-- 3. House 3 (Left-Top Triangle) -> Gemini (3) AIR / WEST -->
    <polygon points="0,0 125,125 0,250" fill="rgba(56, 189, 248, 0.18)" stroke="#38bdf8" stroke-width="1.8" />
    <text x="50" y="115" text-anchor="middle" fill="#bae6fd" font-size="14" font-weight="800">३. मिथुन</text>
    <text x="50" y="135" text-anchor="middle" fill="#38bdf8" font-size="11.5">वायु • पश्चिम</text>

    <!-- 4. House 4 (Left Diamond) -> Cancer (4) WATER / NORTH -->
    <polygon points="0,250 125,125 250,250 125,375" fill="rgba(6, 182, 212, 0.22)" stroke="#06b6d4" stroke-width="2" />
    <text x="125" y="240" text-anchor="middle" fill="#67e8f9" font-size="17" font-weight="800">४. कर्क (Cancer)</text>
    <text x="125" y="265" text-anchor="middle" fill="#22d3ee" font-size="13">जल तत्व • उत्तर</text>
    <text x="125" y="285" text-anchor="middle" fill="#cbd5e1" font-size="11.5">त्रिकोण युति: ८, १२</text>

    <!-- 5. House 5 (Left-Bottom Triangle) -> Leo (5) FIRE / EAST -->
    <polygon points="0,250 125,375 0,500" fill="rgba(239, 68, 68, 0.18)" stroke="#ef4444" stroke-width="1.8" />
    <text x="50" y="365" text-anchor="middle" fill="#fca5a5" font-size="14" font-weight="800">५. सिंह</text>
    <text x="50" y="385" text-anchor="middle" fill="#ef4444" font-size="11.5">अग्नि • पूर्व</text>

    <!-- 6. House 6 (Bottom Left Triangle) -> Virgo (6) EARTH / SOUTH -->
    <polygon points="0,500 250,500 125,375" fill="rgba(245, 158, 11, 0.18)" stroke="#f59e0b" stroke-width="1.8" />
    <text x="125" y="445" text-anchor="middle" fill="#fde68a" font-size="15" font-weight="800">६. कन्या (Virgo)</text>
    <text x="125" y="468" text-anchor="middle" fill="#fbbf24" font-size="12">पृथ्वी • दक्षिण</text>

    <!-- 7. House 7 (Bottom Center Diamond) -> Libra (7) AIR / WEST -->
    <polygon points="250,250 375,375 250,500 125,375" fill="rgba(56, 189, 248, 0.22)" stroke="#38bdf8" stroke-width="2" />
    <text x="250" y="365" text-anchor="middle" fill="#7dd3fc" font-size="17" font-weight="800">७. तुला (Libra)</text>
    <text x="250" y="390" text-anchor="middle" fill="#38bdf8" font-size="13">वायु तत्व • पश्चिम</text>
    <text x="250" y="410" text-anchor="middle" fill="#cbd5e1" font-size="11.5">त्रिकोण युति: ३, ११</text>

    <!-- 8. House 8 (Bottom Right Triangle) -> Scorpio (8) WATER / NORTH -->
    <polygon points="250,500 500,500 375,375" fill="rgba(6, 182, 212, 0.18)" stroke="#06b6d4" stroke-width="1.8" />
    <text x="375" y="445" text-anchor="middle" fill="#a5f3fc" font-size="15" font-weight="800">८. वृश्चिक (Scorpio)</text>
    <text x="375" y="468" text-anchor="middle" fill="#22d3ee" font-size="12">जल • उत्तर</text>

    <!-- 9. House 9 (Right-Bottom Triangle) -> Sagittarius (9) FIRE / EAST -->
    <polygon points="500,250 375,375 500,500" fill="rgba(239, 68, 68, 0.18)" stroke="#ef4444" stroke-width="1.8" />
    <text x="450" y="365" text-anchor="middle" fill="#fca5a5" font-size="14" font-weight="800">९. धनु</text>
    <text x="450" y="385" text-anchor="middle" fill="#ef4444" font-size="11.5">अग्नि • पूर्व</text>

    <!-- 10. House 10 (Right Center Diamond) -> Capricorn (10) EARTH / SOUTH -->
    <polygon points="500,250 375,125 250,250 375,375" fill="rgba(245, 158, 11, 0.22)" stroke="#f59e0b" stroke-width="2" />
    <text x="375" y="240" text-anchor="middle" fill="#fde68a" font-size="17" font-weight="800">१०. मकर (Capricorn)</text>
    <text x="375" y="265" text-anchor="middle" fill="#f59e0b" font-size="13">पृथ्वी तत्व • दक्षिण</text>
    <text x="375" y="285" text-anchor="middle" fill="#cbd5e1" font-size="11.5">त्रिकोण युति: २, ६</text>

    <!-- 11. House 11 (Right-Top Triangle) -> Aquarius (11) AIR / WEST -->
    <polygon points="500,0 375,125 500,250" fill="rgba(56, 189, 248, 0.18)" stroke="#38bdf8" stroke-width="1.8" />
    <text x="450" y="115" text-anchor="middle" fill="#bae6fd" font-size="14" font-weight="800">११. कुम्भ</text>
    <text x="450" y="135" text-anchor="middle" fill="#38bdf8" font-size="11.5">वायु • पश्चिम</text>
  </g>

  <!-- 4 Elemental Legend Cards at Bottom -->
  <g transform="translate(50, 650)">
    <!-- Fire -->
    <g transform="translate(0, 0)" filter="url(#shadow)">
      <rect width="205" height="190" rx="8" fill="#1c1917" stroke="#ef4444" stroke-width="1.5" />
      <rect width="205" height="32" rx="8" fill="#991b1b" />
      <text x="102" y="22" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">🔥 पूर्व दिशा (अग्नि तत्व)</text>
      <text x="15" y="58" fill="#fde047" font-size="13" font-weight="700">राशियाँ: १ मेष, ५ सिंह, ९ धनु</text>
      <text x="15" y="82" fill="#cbd5e1" font-size="12">• युति शक्ति: १००%</text>
      <text x="15" y="104" fill="#cbd5e1" font-size="12">• कारकत्व: ऊर्जा, पराक्रम</text>
      <text x="15" y="126" fill="#cbd5e1" font-size="12">• नेतृत्व, आत्म-चेतना</text>
      <text x="15" y="155" fill="#fca5a5" font-size="11">समान दिशा = एक ही कमरा</text>
    </g>

    <!-- Earth -->
    <g transform="translate(230, 0)" filter="url(#shadow)">
      <rect width="205" height="190" rx="8" fill="#1c1917" stroke="#f59e0b" stroke-width="1.5" />
      <rect width="205" height="32" rx="8" fill="#b45309" />
      <text x="102" y="22" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">🌍 दक्षिण दिशा (पृथ्वी तत्व)</text>
      <text x="15" y="58" fill="#fde047" font-size="13" font-weight="700">राशियाँ: २ वृषभ, ६ कन्या, १० मकर</text>
      <text x="15" y="82" fill="#cbd5e1" font-size="12">• युति शक्ति: १००%</text>
      <text x="15" y="104" fill="#cbd5e1" font-size="12">• कारकत्व: धन, संपत्ति</text>
      <text x="15" y="126" fill="#cbd5e1" font-size="12">• भौतिक स्थिरता, आजीविका</text>
      <text x="15" y="155" fill="#fde68a" font-size="11">स्थिर कर्म व संचित संसाधन</text>
    </g>

    <!-- Air -->
    <g transform="translate(460, 0)" filter="url(#shadow)">
      <rect width="205" height="190" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" />
      <rect width="205" height="32" rx="8" fill="#0284c7" />
      <text x="102" y="22" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">💨 पश्चिम दिशा (वायु तत्व)</text>
      <text x="15" y="58" fill="#fde047" font-size="13" font-weight="700">राशियाँ: ३ मिथुन, ७ तुला, ११ कुम्भ</text>
      <text x="15" y="82" fill="#cbd5e1" font-size="12">• युति शक्ति: १००%</text>
      <text x="15" y="104" fill="#cbd5e1" font-size="12">• कारकत्व: बुद्धि, संचार</text>
      <text x="15" y="126" fill="#cbd5e1" font-size="12">• व्यापार, जनसंपर्क, लाभ</text>
      <text x="15" y="155" fill="#bae6fd" font-size="11">बौद्धिक गति एवं साझेदारी</text>
    </g>

    <!-- Water -->
    <g transform="translate(690, 0)" filter="url(#shadow)">
      <rect width="205" height="190" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5" />
      <rect width="205" height="32" rx="8" fill="#0e7490" />
      <text x="102" y="22" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">🌊 उत्तर दिशा (जल तत्व)</text>
      <text x="15" y="58" fill="#fde047" font-size="13" font-weight="700">राशियाँ: ४ कर्क, ८ वृश्चिक, १२ मीन</text>
      <text x="15" y="82" fill="#cbd5e1" font-size="12">• युति शक्ति: १००%</text>
      <text x="15" y="104" fill="#cbd5e1" font-size="12">• कारकत्व: भावना, मोक्ष</text>
      <text x="15" y="126" fill="#cbd5e1" font-size="12">• गूढ़ साधना, विदेश गमन</text>
      <text x="15" y="155" fill="#a5f3fc" font-size="11">अंतःप्रेरणा एवं आध्यात्मिक मुक्ति</text>
    </g>
  </g>

  <!-- Footer Tag -->
  <text x="{width/2}" y="885" text-anchor="middle" fill="#94a3b8" font-size="13">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान</text>
</svg>'''
    write_svg("bnn_elemental_directional_diamond_chart.svg", svg)

# -------------------------------------------------------------
# Chart 5: 12 Houses from Jeeva Lagna Diamond Chart
# -------------------------------------------------------------
def make_jeeva_12bhavas_diamond_chart():
    width, height = 1000, 920
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">जीव लग्न (गुरु) द्वादश भाव सम्पूर्ण फलित चक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">BNN 12 Houses from Jeeva Lagna (Jupiter as Anchor • Zero Ascendant Dependency)</text>

  <!-- Diamond Chart Layout: Center (500, 440), Size 560 -->
  <g transform="translate(220, 110)" filter="url(#shadow)">
    <!-- Outer Square -->
    <rect x="0" y="0" width="560" height="560" fill="#0f172a" stroke="#d97706" stroke-width="2.5" />
    
    <!-- Cross Lines -->
    <line x1="0" y1="0" x2="560" y2="560" stroke="#d97706" stroke-width="2" />
    <line x1="560" y1="0" x2="0" y2="560" stroke="#d97706" stroke-width="2" />
    
    <!-- Inner Diamond -->
    <polygon points="280,0 560,280 280,560 0,280" fill="#131c2e" stroke="#f59e0b" stroke-width="2" />

    <!-- House 1: Lagna (Center Diamond) -->
    <polygon points="280,0 420,140 280,280 140,140" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2.2" />
    <text x="280" y="85" text-anchor="middle" fill="#fde047" font-size="22" font-weight="900">१. जीव लग्न (गुरु)</text>
    <text x="280" y="112" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="700">जातक स्वयं • स्वास्थ्य • चेतना</text>
    <text x="280" y="135" text-anchor="middle" fill="#cbd5e1" font-size="12">जीवन यात्रा का केन्द्र बिंदु</text>

    <!-- House 2: Top-Left Triangle -->
    <polygon points="0,0 280,0 140,140" fill="rgba(245, 158, 11, 0.15)" stroke="#d97706" stroke-width="1.8" />
    <text x="140" y="45" text-anchor="middle" fill="#fde68a" font-size="16" font-weight="800">२. धन व कुटुंब</text>
    <text x="140" y="70" text-anchor="middle" fill="#e2e8f0" font-size="12.5">वाणी, प्रारंभिक संसाधन, संचित कोष</text>
    <text x="140" y="92" text-anchor="middle" fill="#94a3b8" font-size="11.5">+१ अग्रिम भाव (Next Step 15%)</text>

    <!-- House 12: Top-Right Triangle -->
    <polygon points="280,0 560,0 420,140" fill="rgba(168, 85, 247, 0.15)" stroke="#a855f7" stroke-width="1.8" />
    <text x="420" y="45" text-anchor="middle" fill="#e9d5ff" font-size="16" font-weight="800">१२. मोक्ष व व्यय</text>
    <text x="420" y="70" text-anchor="middle" fill="#e2e8f0" font-size="12.5">विदेश वास, आध्यात्मिक मुक्ति, विरक्ति</text>
    <text x="420" y="92" text-anchor="middle" fill="#94a3b8" font-size="11.5">-१ पृष्ठ भाव (Past Karma 15%)</text>

    <!-- House 3: Left-Top Triangle -->
    <polygon points="0,0 140,140 0,280" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1.8" />
    <text x="55" y="130" text-anchor="middle" fill="#bae6fd" font-size="15" font-weight="800">३. पराक्रम</text>
    <text x="55" y="152" text-anchor="middle" fill="#e2e8f0" font-size="12">अनुज, संचार, यात्रा</text>

    <!-- House 4: Left Center Diamond -->
    <polygon points="0,280 140,140 280,280 140,420" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4" stroke-width="1.8" />
    <text x="140" y="270" text-anchor="middle" fill="#67e8f9" font-size="17" font-weight="800">४. गृह व माता</text>
    <text x="140" y="295" text-anchor="middle" fill="#e2e8f0" font-size="13">वाहन, भौतिक सुख, विद्या</text>
    <text x="140" y="318" text-anchor="middle" fill="#94a3b8" font-size="11.5">चन्द्र/शुक्र का नैसर्गिक आश्रय</text>

    <!-- House 5: Left-Bottom Triangle -->
    <polygon points="0,280 140,420 0,560" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1.8" />
    <text x="55" y="415" text-anchor="middle" fill="#fca5a5" font-size="15" font-weight="800">५. पूर्वपुण्य</text>
    <text x="55" y="438" text-anchor="middle" fill="#e2e8f0" font-size="12">मेधा, संतति, ज्ञान</text>

    <!-- House 6: Bottom-Left Triangle -->
    <polygon points="0,560 280,560 140,420" fill="rgba(245, 158, 11, 0.15)" stroke="#d97706" stroke-width="1.8" />
    <text x="140" y="505" text-anchor="middle" fill="#fde68a" font-size="16" font-weight="800">६. रोग, ऋण, शत्रु</text>
    <text x="140" y="528" text-anchor="middle" fill="#e2e8f0" font-size="12.5">दैनिक सेवा, संघर्ष, प्रतियोगिता</text>

    <!-- House 7: Bottom Center Diamond -->
    <polygon points="280,280 420,420 280,560 140,420" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
    <text x="280" y="405" text-anchor="middle" fill="#38bdf8" font-size="18" font-weight="800">७. जाया व साझेदारी</text>
    <text x="280" y="430" text-anchor="middle" fill="#ffffff" font-size="13.5">जीवनसाथी • सम्मुख दृष्टि (50%)</text>
    <text x="280" y="452" text-anchor="middle" fill="#94a3b8" font-size="12">लोक-व्यवहार एवं जनसंपर्क</text>

    <!-- House 8: Bottom-Right Triangle -->
    <polygon points="280,560 560,560 420,420" fill="rgba(225, 29, 72, 0.15)" stroke="#e11d48" stroke-width="1.8" />
    <text x="420" y="505" text-anchor="middle" fill="#fda4af" font-size="16" font-weight="800">८. आयु व गूढ़ विद्या</text>
    <text x="420" y="528" text-anchor="middle" fill="#e2e8f0" font-size="12.5">आकस्मिक परिवर्तन, संकट, शोध</text>

    <!-- House 9: Right-Bottom Triangle -->
    <polygon points="560,280 420,420 560,560" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1.8" />
    <text x="505" y="415" text-anchor="middle" fill="#fca5a5" font-size="15" font-weight="800">९. भाग्य व धर्म</text>
    <text x="505" y="438" text-anchor="middle" fill="#e2e8f0" font-size="12">गुरु, पिता, तीर्थ</text>

    <!-- House 10: Right Center Diamond -->
    <polygon points="560,280 420,140 280,280 420,420" fill="rgba(245, 158, 11, 0.18)" stroke="#f59e0b" stroke-width="2" />
    <text x="420" y="270" text-anchor="middle" fill="#fde047" font-size="18" font-weight="800">१०. कर्म व पदवी</text>
    <text x="420" y="295" text-anchor="middle" fill="#ffffff" font-size="13.5">शनि का कारक क्षेत्र • आजीविका</text>
    <text x="420" y="318" text-anchor="middle" fill="#94a3b8" font-size="12">राजसत्ता, प्रतिष्ठा, सामाजिक प्रभाव</text>

    <!-- House 11: Right-Top Triangle -->
    <polygon points="560,0 420,140 560,280" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1.8" />
    <text x="505" y="130" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="800">११. लाभ व सिद्धि</text>
    <text x="505" y="152" text-anchor="middle" fill="#e2e8f0" font-size="12">इच्छापूर्ति, बड़े भाई</text>
  </g>

  <!-- Side Annotation -->
  <g transform="translate(60, 710)" filter="url(#shadow)">
    <rect width="880" height="150" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.5" />
    <text x="30" y="35" fill="#fde047" font-size="15" font-weight="800">📌 बी.एन.एन. जीव-लग्न द्वादश भाव विवेचन सूत्र:</text>
    <text x="30" y="65" fill="#e2e8f0" font-size="13.5">१. यह चक्र लग्न-कुंडली के अभाव में भी जन्म-कालीन गुरु को लग्न मानकर सटीक फलित प्रस्तुत करता है।</text>
    <text x="30" y="92" fill="#e2e8f0" font-size="13.5">२. गुरु से १०वें भाव में जो भी ग्रह होगा, वह जातक के कार्यक्षेत्र (Profession) का निर्धारण करेगा।</text>
    <text x="30" y="120" fill="#94a3b8" font-size="12.5">३. गुरु से २रे और १२वें भावों में स्थित ग्रह जातक की जीवन-नौका की दिशा एवं गति (Speed &amp; Stability) तय करते हैं।</text>
  </g>

  <text x="{width/2}" y="895" text-anchor="middle" fill="#94a3b8" font-size="12.5">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान</text>
</svg>'''
    write_svg("bnn_jeeva_12bhavas_diamond_chart.svg", svg)

# -------------------------------------------------------------
# Chart 6: BNN Master Dual Conjunctions Diamond Chart
# -------------------------------------------------------------
def make_major_conjunctions_diamond_chart():
    width, height = 1000, 920
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">बी.एन.एन. प्रमुख द्वि-ग्रहीय राजयोग एवं कर्म-संयोग चक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">Master Dual Conjunctions in BNN Diamond Architecture • ३६ प्रमुख योगों का प्रामाणिक प्रतिपादन</text>

  <!-- Diamond Layout: Center (500, 420), Size 520 -->
  <g transform="translate(240, 110)" filter="url(#shadow)">
    <rect x="0" y="0" width="520" height="520" fill="#0f172a" stroke="#d97706" stroke-width="2.5" />
    <line x1="0" y1="0" x2="520" y2="520" stroke="#d97706" stroke-width="2" />
    <line x1="520" y1="0" x2="0" y2="520" stroke="#d97706" stroke-width="2" />
    <polygon points="260,0 520,260 260,520 0,260" fill="#131c2e" stroke="#f59e0b" stroke-width="2" />

    <!-- Center H1: Guru + Shani (Dharma-Karmadhipati Yoga / Brahma Yoga) -->
    <polygon points="260,0 390,130 260,260 130,130" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2.2" />
    <text x="260" y="75" text-anchor="middle" fill="#fde047" font-size="19" font-weight="900">गुरु + शनि (Guru+Shani)</text>
    <text x="260" y="100" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="800">धर्म-कर्माधिपति / ब्रह्म योग</text>
    <text x="260" y="122" text-anchor="middle" fill="#ffffff" font-size="12.5">आध्यात्मिक कर्म • उच्च संस्था प्रमुख</text>
    <text x="260" y="142" text-anchor="middle" fill="#cbd5e1" font-size="11">न्यायाधीश, कुलपति, निष्काम कर्मयोगी</text>

    <!-- H4 (Left Diamond): Budha + Shukra (Kala Yoga / Mahalakshmi) -->
    <polygon points="0,260 130,130 260,260 130,390" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2" />
    <text x="130" y="240" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="800">बुध + शुक्र</text>
    <text x="130" y="262" text-anchor="middle" fill="#fde047" font-size="13.5" font-weight="700">कला / महालक्ष्मी योग</text>
    <text x="130" y="284" text-anchor="middle" fill="#ffffff" font-size="11.5">अपार व्यापारिक संपदा</text>
    <text x="130" y="304" text-anchor="middle" fill="#cbd5e1" font-size="11">वाक्पटुता, विपणन, सौन्दर्य</text>

    <!-- H5 (Left-Bottom Triangle): Guru + Mangala (Tejasvi Yoga) -->
    <polygon points="0,260 130,390 0,520" fill="rgba(239, 68, 68, 0.2)" stroke="#ef4444" stroke-width="1.8" />
    <text x="50" y="375" text-anchor="middle" fill="#fca5a5" font-size="14" font-weight="800">गुरु+मंगल</text>
    <text x="50" y="398" text-anchor="middle" fill="#fde047" font-size="12">तेजस्वी योग</text>
    <text x="50" y="418" text-anchor="middle" fill="#cbd5e1" font-size="10.5">इंजीनियरिंग, भूमि</text>

    <!-- H7 (Bottom Diamond): Shani + Shukra (Bhagya-Lakshmi) -->
    <polygon points="260,260 390,390 260,520 130,390" fill="rgba(244, 114, 182, 0.2)" stroke="#ec4899" stroke-width="2" />
    <text x="260" y="380" text-anchor="middle" fill="#f472b6" font-size="17" font-weight="800">शनि + शुक्र (Shani+Shukra)</text>
    <text x="260" y="405" text-anchor="middle" fill="#fde047" font-size="13.5" font-weight="700">भाग्यलक्ष्मी योग (Bhagyalakshmi)</text>
    <text x="260" y="426" text-anchor="middle" fill="#ffffff" font-size="12">विवाह उपरांत तीव्र भाग्योदय • वाहन-भवन</text>
    <text x="260" y="446" text-anchor="middle" fill="#cbd5e1" font-size="11">वस्त्र, विलासिता, उद्योग में अचल संपत्ति</text>

    <!-- H9 (Right-Bottom Triangle): Guru + Ketu (Ganesha Yoga / Mukti) -->
    <polygon points="520,260 390,390 520,520" fill="rgba(168, 85, 247, 0.2)" stroke="#a855f7" stroke-width="1.8" />
    <text x="465" y="375" text-anchor="middle" fill="#e9d5ff" font-size="14" font-weight="800">गुरु+केतु</text>
    <text x="465" y="398" text-anchor="middle" fill="#fde047" font-size="12">गणेश/मुक्ति योग</text>
    <text x="465" y="418" text-anchor="middle" fill="#cbd5e1" font-size="10.5">त्रिकालज्ञ, ज्योतिष</text>

    <!-- H10 (Right Diamond): Shani + Rahu (Foreign Tech / Karma) -->
    <polygon points="520,260 390,130 260,260 390,390" fill="rgba(99, 102, 241, 0.2)" stroke="#6366f1" stroke-width="2" />
    <text x="390" y="240" text-anchor="middle" fill="#a5b4fc" font-size="16" font-weight="800">शनि + राहु</text>
    <text x="390" y="262" text-anchor="middle" fill="#fde047" font-size="13.5" font-weight="700">श्रापित / विदेशी कर्म योग</text>
    <text x="390" y="284" text-anchor="middle" fill="#ffffff" font-size="11.5">वैश्विक तकनीकी उद्योग</text>
    <text x="390" y="304" text-anchor="middle" fill="#cbd5e1" font-size="11">सॉफ्टवेयर, विमानन, विदेशी आय</text>
  </g>

  <!-- Bottom Guidelines -->
  <g transform="translate(60, 670)" filter="url(#shadow)">
    <rect width="880" height="195" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.5" />
    <text x="30" y="32" fill="#fde047" font-size="15" font-weight="800">⚡ बी.एन.एन. द्वि-ग्रहीय संयोग के ३ स्वर्णिम नियम (Golden Conjunction Rules):</text>
    
    <text x="30" y="62" fill="#38bdf8" font-size="13.5" font-weight="700">१. अंश-दूरी नियम (Degree Proximity):</text>
    <text x="280" y="62" fill="#e2e8f0" font-size="13">दो ग्रहों के मध्य अंश अंतर जितना कम (०°–१५°) होगा, फल उतना ही प्रचंड व अकाट्य होगा।</text>

    <text x="30" y="92" fill="#34d399" font-size="13.5" font-weight="700">२. अग्रगामी ग्रह नियम (Leading Planet):</text>
    <text x="280" y="92" fill="#e2e8f0" font-size="13">निम्न अंश वाला ग्रह आगे होता है; उच्च अंश वाला ग्रह पीछे से उसका अनुसरण करता है।</text>

    <text x="30" y="122" fill="#f472b6" font-size="13.5" font-weight="700">३. त्रिकोण युति नियम (Trine Conjunction):</text>
    <text x="280" y="122" fill="#e2e8f0" font-size="13">यदि गुरु मेष में और शनि सिंह में हो, तो भी यह पूर्ण गुरु-शनि योग माना जाएगा (समान अग्नि दिशा)।</text>

    <text x="30" y="155" fill="#94a3b8" font-size="12">उदाहरण: गुरु (८°) + शनि (१४°) = गुरु आजीविका की ओर बढ़ रहा है; जातक स्वयं के ज्ञान से कर्म का निर्माण करेगा।</text>
    <text x="30" y="178" fill="#cbd5e1" font-size="12">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान</text>
  </g>
</svg>'''
    write_svg("bnn_major_conjunctions_diamond_chart.svg", svg)

# -------------------------------------------------------------
# Chart 7: BNN Triplet & Multi-Planet Mahayogas Diamond Chart
# -------------------------------------------------------------
def make_triplet_rajyogas_diamond_chart():
    width, height = 1000, 920
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">बी.एन.एन. त्रि-ग्रहीय एवं बहु-ग्रहीय महायोग डायमंड चक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">Master Triplet Combinations in Bhrigu Nandi Nadi • २० शीर्ष शास्त्रीय राजयोग</text>

  <!-- 4 Big Strategic Triplet Cards in 2x2 Grid -->
  <!-- Card 1: Saraswati Yoga (Guru + Budha + Shukra) -->
  <g transform="translate(50, 110)" filter="url(#shadow)">
    <rect width="425" height="255" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
    <rect width="425" height="42" rx="10" fill="#0369a1" />
    <text x="212" y="28" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">📚 १. सरस्वती महायोग (Guru + Budha + Shukra)</text>
    
    <text x="20" y="72" fill="#fde047" font-size="14" font-weight="800">संयोजन: गुरु (ज्ञान) + बुध (बुद्धि) + शुक्र (कला/अभिव्यक्ति)</text>
    <text x="20" y="98" fill="#e2e8f0" font-size="13">• फल: अप्रतिम विद्वत्ता, अंतरराष्ट्रीय ख्याति, ग्रंथकार, सम्पादक</text>
    <text x="20" y="122" fill="#e2e8f0" font-size="13">• जातक जो भी लिखता या बोलता है, समाज उसे शास्त्रवत् स्वीकारता है</text>
    <text x="20" y="146" fill="#cbd5e1" font-size="12.5">• वाक्-सिद्धि एवं विद्या द्वारा अपार धन व प्रतिष्ठा का अर्जन</text>
    <text x="20" y="174" fill="#67e8f9" font-size="13" font-weight="700">अंश-क्रम वरीयता: बुध (१०°) → शुक्र (१६°) → गुरु (२२°)</text>
    <text x="20" y="200" fill="#94a3b8" font-size="12">व्यवसाय: प्रोफेसर, सर्वोच्च शोधकर्ता, दार्शनिक, अंतरराष्ट्रीय वक्ता</text>
    <text x="20" y="232" fill="#fde68a" font-size="12">शास्त्रीय संदर्भ: "बुध-शुक्र-गुरु-संयोगे जातः सर्वज्ञ-सम्मतः"</text>
  </g>

  <!-- Card 2: Kuber Yoga (Shani + Budha + Shukra) -->
  <g transform="translate(525, 110)" filter="url(#shadow)">
    <rect width="425" height="255" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2" />
    <rect width="425" height="42" rx="10" fill="#047857" />
    <text x="212" y="28" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">💰 २. कुबेर महायोग (Shani + Budha + Shukra)</text>
    
    <text x="20" y="72" fill="#fde047" font-size="14" font-weight="800">संयोजन: शनि (कर्म) + बुध (व्यापार) + शुक्र (स्थायी संपत्ति)</text>
    <text x="20" y="98" fill="#e2e8f0" font-size="13">• फल: औद्योगिक साम्राज्य, विशाल व्यावसायिक नेटवर्क, स्थायी संपदा</text>
    <text x="20" y="122" fill="#e2e8f0" font-size="13">• जातक शून्य से शुरुआत करके बहुराष्ट्रीय कंपनी की स्थापना करता है</text>
    <text x="20" y="146" fill="#cbd5e1" font-size="12.5">• वित्तीय प्रबंधन (Finance/Banking) में अद्वितीय चतुराई</text>
    <text x="20" y="174" fill="#a7f3d0" font-size="13" font-weight="700">अंश-क्रम वरीयता: शनि (८°) → बुध (१४°) → शुक्र (२०°)</text>
    <text x="20" y="200" fill="#94a3b8" font-size="12">व्यवसाय: उद्योगपति, रियल एस्टेट टाइकून, वेंचर कैपिटलिस्ट</text>
    <text x="20" y="232" fill="#fde68a" font-size="12">शास्त्रीय संदर्भ: "शनि-बुध-सित-योगेन कुबेर-सम-वैभवम्"</text>
  </g>

  <!-- Card 3: Rishi Yoga (Surya + Guru + Ketu) -->
  <g transform="translate(50, 395)" filter="url(#shadow)">
    <rect width="425" height="255" rx="10" fill="#1c1917" stroke="#f59e0b" stroke-width="2" />
    <rect width="425" height="42" rx="10" fill="#b45309" />
    <text x="212" y="28" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">🔱 ३. ऋषि महायोग (Surya + Guru + Ketu)</text>
    
    <text x="20" y="72" fill="#fde047" font-size="14" font-weight="800">संयोजन: सूर्य (आत्मा) + गुरु (दिव्य ज्ञान) + केतु (मुक्ति/ध्वज)</text>
    <text x="20" y="98" fill="#e2e8f0" font-size="13">• फल: ब्रह्मज्ञान, आध्यात्मिक संस्था प्रमुख, मंत्र-सिद्धि, तपोबल</text>
    <text x="20" y="122" fill="#e2e8f0" font-size="13">• जातक का जीवन समाज के पथ-प्रदर्शन हेतु समर्पित होता है</text>
    <text x="20" y="146" fill="#cbd5e1" font-size="12.5">• पूर्व जन्म के संचित पुण्यों से जन्मजात आत्म-साक्षात्कार की योग्यता</text>
    <text x="20" y="174" fill="#fde68a" font-size="13" font-weight="700">अंश-क्रम वरीयता: सूर्य (५°) → गुरु (१५°) → केतु (२५°)</text>
    <text x="20" y="200" fill="#94a3b8" font-size="12">व्यवसाय: जगद्गुरु, आध्यात्मिक मार्गदर्शक, प्रामाणिक ज्योतिषी</text>
    <text x="20" y="232" fill="#fde68a" font-size="12">शास्त्रीय संदर्भ: "रवि-गुरु-शिखि-योगे तु ब्रह्मर्षि-तुल्य-मानसः"</text>
  </g>

  <!-- Card 4: Chakravarti Karmayoga (Guru + Shani + Mangala) -->
  <g transform="translate(525, 395)" filter="url(#shadow)">
    <rect width="425" height="255" rx="10" fill="#1e1b4b" stroke="#7c3aed" stroke-width="2" />
    <rect width="425" height="42" rx="10" fill="#6d28d9" />
    <text x="212" y="28" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">👑 ४. चक्रवर्ती कर्मयोग (Guru + Shani + Mangala)</text>
    
    <text x="20" y="72" fill="#fde047" font-size="14" font-weight="800">संयोजन: गुरु (जीव/धर्म) + शनि (कर्म) + मंगल (शौर्य/तकनीकी)</text>
    <text x="20" y="98" fill="#e2e8f0" font-size="13">• फल: सर्वोच्च प्रशासनिक पद, सेनाध्यक्ष, मुख्य अभियंता, निर्माणकर्ता</text>
    <text x="20" y="122" fill="#e2e8f0" font-size="13">• जातक के पास कठोर निर्णय लेने की अद्भुत क्षमता व अधिकार होता है</text>
    <text x="20" y="146" fill="#cbd5e1" font-size="12.5">• कठिन से कठिन परिस्थिति में भी अनुशासन एवं विजय की प्राप्ति</text>
    <text x="20" y="174" fill="#ddd6fe" font-size="13" font-weight="700">अंश-क्रम वरीयता: गुरु (४°) → शनि (११°) → मंगल (१९°)</text>
    <text x="20" y="200" fill="#94a3b8" font-size="12">व्यवसाय: कैबिनेट सचिव, चीफ इंजीनियर, सैन्य जनरल, उद्योगपति</text>
    <text x="20" y="232" fill="#fde68a" font-size="12">शास्त्रीय संदर्भ: "गुरु-मन्द-कुज-संयोगे चक्रवर्ती समो भवेत्"</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(50, 680)" filter="url(#shadow)">
    <rect width="900" height="185" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.5" />
    <text x="30" y="32" fill="#fde047" font-size="15" font-weight="800">🎯 बी.एन.एन. त्रि-ग्रहीय योग विश्लेषण विधि (3-Step Practical Evaluation):</text>
    <text x="30" y="62" fill="#cbd5e1" font-size="13.5">१. तीनों ग्रहों की दिशा (तत्व) का मिलान करें (समान दिशा अथवा १-७ सम्मुख अक्ष)।</text>
    <text x="30" y="90" fill="#cbd5e1" font-size="13.5">२. मध्यस्थ ग्रह (Middle Planet) का अध्ययन करें — वह दोनों सिरों के ग्रहों को ऊर्जा स्थानांतरित करता है।</text>
    <text x="30" y="118" fill="#cbd5e1" font-size="13.5">३. यदि कोई पापी ग्रह (राहु/केतु) मध्य में बैठ जाए, तो योग 'खंडित' अथवा 'अवरुद्ध' हो जाता है जब तक कि गोचर का गुरु उसे मुक्त न करे।</text>
    <text x="30" y="152" fill="#94a3b8" font-size="12.5">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</text>
  </g>
</svg>'''
    write_svg("bnn_triplet_rajyogas_diamond_chart.svg", svg)

# -------------------------------------------------------------
# Chart 8: Saturn 30-Year Paryaya & Jupiter Progression Timeline
# -------------------------------------------------------------
def make_progression_paryaya_chart():
    width, height = 1000, 880
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">शनि ३०-वर्षीय पर्याय एवं गुरु प्रगति काल-चक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">BNN Saturn 30-Year Paryaya Cycles &amp; Jupiter 1-Year Progression Engine</text>

  <!-- Section 1: Saturn 4 Paryayas (0 to 120 Years) -->
  <g transform="translate(50, 110)" filter="url(#shadow)">
    <rect width="900" height="340" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.8" />
    <rect width="900" height="38" rx="10" fill="#b45309" />
    <text x="450" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">♄ शनि ३०-वर्षीय पर्याय चक्र (४ महा-चरण • Karmic Evolution Waves)</text>

    <!-- Timeline Bar -->
    <rect x="40" y="65" width="820" height="14" rx="7" fill="#1e293b" />
    <!-- 4 Phases on Bar -->
    <rect x="40" y="65" width="205" height="14" rx="7" fill="#3b82f6" />
    <rect x="245" y="65" width="205" height="14" rx="0" fill="#10b981" />
    <rect x="450" y="65" width="205" height="14" rx="0" fill="#f59e0b" />
    <rect x="655" y="65" width="205" height="14" rx="7" fill="#a855f7" />

    <!-- 4 Columns -->
    <!-- Paryaya 1 -->
    <g transform="translate(40, 95)">
      <text x="100" y="22" text-anchor="middle" fill="#60a5fa" font-size="15" font-weight="800">प्रथम पर्याय (1st Round)</text>
      <text x="100" y="42" text-anchor="middle" fill="#fde047" font-size="13" font-weight="700">० से ३० वर्ष (Years 0-30)</text>
      <text x="0" y="70" fill="#e2e8f0" font-size="12">• बाल्यावस्था, शिक्षा, प्रारंभिक संघर्ष</text>
      <text x="0" y="92" fill="#e2e8f0" font-size="12">• माता-पिता पर निर्भरता एवं संस्कार</text>
      <text x="0" y="114" fill="#cbd5e1" font-size="11.5">• प्रथम आजीविका नींव की स्थापना</text>
      <text x="0" y="136" fill="#94a3b8" font-size="11.5">• नेटल शनि पर प्रथम गोचर (28-30y)</text>
    </g>

    <!-- Paryaya 2 -->
    <g transform="translate(245, 95)">
      <text x="100" y="22" text-anchor="middle" fill="#34d399" font-size="15" font-weight="800">द्वितीय पर्याय (2nd Round)</text>
      <text x="100" y="42" text-anchor="middle" fill="#fde047" font-size="13" font-weight="700">३० से ६० वर्ष (Years 30-60)</text>
      <text x="0" y="70" fill="#e2e8f0" font-size="12">• वास्तविक कर्म उत्थान व आजीविका</text>
      <text x="0" y="92" fill="#e2e8f0" font-size="12">• विवाह, संतान, गृह, धन संचय</text>
      <text x="0" y="114" fill="#cbd5e1" font-size="11.5">• समाज में मान-सम्मान व पदवी</text>
      <text x="0" y="136" fill="#94a3b8" font-size="11.5">• जातक अपने प्रारब्ध का भोग करता है</text>
    </g>

    <!-- Paryaya 3 -->
    <g transform="translate(450, 95)">
      <text x="100" y="22" text-anchor="middle" fill="#fbbf24" font-size="15" font-weight="800">तृतीय पर्याय (3rd Round)</text>
      <text x="100" y="42" text-anchor="middle" fill="#fde047" font-size="13" font-weight="700">६० से ९० वर्ष (Years 60-90)</text>
      <text x="0" y="70" fill="#e2e8f0" font-size="12">• संन्यास भाव, कर्म से विरक्ति</text>
      <text x="0" y="92" fill="#e2e8f0" font-size="12">• सामाजिक मार्गदर्शन, ज्ञान वितरण</text>
      <text x="0" y="114" fill="#cbd5e1" font-size="11.5">• ऋण-मुक्ति एवं तीर्थ यात्राएं</text>
      <text x="0" y="136" fill="#94a3b8" font-size="11.5">• आध्यात्मिक चेतना की परिपक्वता</text>
    </g>

    <!-- Paryaya 4 -->
    <g transform="translate(655, 95)">
      <text x="100" y="22" text-anchor="middle" fill="#c084fc" font-size="15" font-weight="800">चतुर्थ पर्याय (4th Round)</text>
      <text x="100" y="42" text-anchor="middle" fill="#fde047" font-size="13" font-weight="700">९०+ वर्ष (Years 90+)</text>
      <text x="0" y="70" fill="#e2e8f0" font-size="12">• मोक्ष साधना, पूर्ण अनासक्ति</text>
      <text x="0" y="92" fill="#e2e8f0" font-size="12">• भौतिक जगत से पूर्ण विच्छेद</text>
      <text x="0" y="114" fill="#cbd5e1" font-size="11.5">• जीव का परम सत्ता में विलीन होना</text>
      <text x="0" y="136" fill="#94a3b8" font-size="11.5">• महाप्रयाण एवं शाश्वत शांति</text>
    </g>

    <text x="450" y="315" text-anchor="middle" fill="#fde047" font-size="13" font-weight="700">💡 बी.एन.एन. सूत्र: जब गोचर का शनि दूसरे पर्याय में नेटल शुक्र/गुरु को पार करता है, तभी सबसे बड़ा भाग्योदय घटित होता है।</text>
  </g>

  <!-- Section 2: Jupiter 1-Year Progression Engine -->
  <g transform="translate(50, 480)" filter="url(#shadow)">
    <rect width="900" height="340" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="1.8" />
    <rect width="900" height="38" rx="10" fill="#0369a1" />
    <text x="450" y="26" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">♃ गुरु वार्षिक प्रगति चक्र (Jupiter 1-Year Progression • Event Trigger Engine)</text>

    <!-- Visual 12-Step Circular/Horizontal Track -->
    <g transform="translate(30, 60)">
      <text x="20" y="25" fill="#fde047" font-size="14.5" font-weight="800">प्रगति नियम: जन्म-कालीन गुरु से प्रति वर्ष १ राशि आगे बढ़ें (1 Sign Per Year)</text>
      
      <!-- Table of 12 Years -->
      <g transform="translate(0, 45)">
        <rect width="840" height="135" rx="8" fill="#131c2e" stroke="#334155" stroke-width="1" />
        
        <!-- Headers -->
        <text x="70" y="28" text-anchor="middle" fill="#38bdf8" font-weight="700">वर्ष १ (Age 1)</text>
        <text x="210" y="28" text-anchor="middle" fill="#38bdf8" font-weight="700">वर्ष ५ (Age 5)</text>
        <text x="350" y="28" text-anchor="middle" fill="#38bdf8" font-weight="700">वर्ष ७ (Age 7)</text>
        <text x="490" y="28" text-anchor="middle" fill="#38bdf8" font-weight="700">वर्ष ९ (Age 9)</text>
        <text x="630" y="28" text-anchor="middle" fill="#38bdf8" font-weight="700">वर्ष १० (Age 10)</text>
        <text x="770" y="28" text-anchor="middle" fill="#38bdf8" font-weight="700">वर्ष १२ (Age 12)</text>

        <!-- Values -->
        <text x="70" y="55" text-anchor="middle" fill="#ffffff">१म भाव (H1)</text>
        <text x="210" y="55" text-anchor="middle" fill="#ffffff">५म भाव (H5)</text>
        <text x="350" y="55" text-anchor="middle" fill="#ffffff">७म भाव (H7)</text>
        <text x="490" y="55" text-anchor="middle" fill="#ffffff">९म भाव (H9)</text>
        <text x="630" y="55" text-anchor="middle" fill="#ffffff">१०म भाव (H10)</text>
        <text x="770" y="55" text-anchor="middle" fill="#ffffff">१२म भाव (H12)</text>

        <text x="70" y="85" text-anchor="middle" fill="#94a3b8" font-size="11.5">जन्म स्थिति</text>
        <text x="210" y="85" text-anchor="middle" fill="#34d399" font-size="11.5">त्रिकोण सक्रिय</text>
        <text x="350" y="85" text-anchor="middle" fill="#f472b6" font-size="11.5">सम्मुख दृष्टि</text>
        <text x="490" y="85" text-anchor="middle" fill="#34d399" font-size="11.5">भाग्य त्रिकोण</text>
        <text x="630" y="85" text-anchor="middle" fill="#fbbf24" font-size="11.5">कर्म सक्रिय</text>
        <text x="770" y="85" text-anchor="middle" fill="#c084fc" font-size="11.5">पर्याय पूर्ण</text>

        <text x="70" y="112" text-anchor="middle" fill="#cbd5e1" font-size="11">आरम्भिक बीज</text>
        <text x="210" y="112" text-anchor="middle" fill="#cbd5e1" font-size="11">विद्या/संतान</text>
        <text x="350" y="112" text-anchor="middle" fill="#cbd5e1" font-size="11">साझेदारी/विवाह</text>
        <text x="490" y="112" text-anchor="middle" fill="#cbd5e1" font-size="11">भाग्योदय/तीर्थ</text>
        <text x="630" y="112" text-anchor="middle" fill="#cbd5e1" font-size="11">पदोन्नति</text>
        <text x="770" y="112" text-anchor="middle" fill="#cbd5e1" font-size="11">नया चक्र (Cycle 2)</text>
      </g>
    </g>

    <text x="450" y="275" text-anchor="middle" fill="#e2e8f0" font-size="13">नोट: १२ वर्ष पश्चात चक्र पुनः प्रथम भाव से घूमता है (२४वें वर्ष में पुनः H12, २५वें में H1, ३६वें में H12)।</text>
    <text x="450" y="305" text-anchor="middle" fill="#38bdf8" font-size="12.5">जब प्रगतिशील गुरु जन्म-कालीन शुक्र को छूता है, तब विवाह; जब शनि को छूता है, तब करियर में स्थायी मोड़ आता है।</text>
  </g>
</svg>'''
    write_svg("bnn_progression_paryaya_chart.svg", svg)

# -------------------------------------------------------------
# Chart 9: Bhrigu Bindu (BB) Destiny Trigger Geometric Chart
# -------------------------------------------------------------
def make_bhrigu_bindu_diagram():
    width, height = 1000, 880
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <linearGradient id="bbGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899" /><stop offset="100%" stop-color="#8b5cf6" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">भृगु बिंदु (BB) प्रारब्ध संवाहक बिंदु ज्यामितीय चक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">Bhrigu Bindu (BB) Destiny Trigger Geometric Model • Rahu-Moon Midpoint Physics</text>

  <!-- Left: 360° Circular Geometric Dial -->
  <g transform="translate(60, 110)" filter="url(#shadow)">
    <rect width="440" height="520" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.8" />
    <text x="220" y="35" text-anchor="middle" fill="#fde047" font-size="16" font-weight="800">भृगु बिंदु ज्यामितीय रेखांकन</text>

    <!-- Circle (cx=220, cy=280, r=160) -->
    <circle cx="220" cy="280" r="160" fill="#131c2e" stroke="#334155" stroke-width="2" />
    
    <!-- 4 Cardinal Spokes -->
    <line x1="220" y1="120" x2="220" y2="440" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4" />
    <line x1="60" y1="280" x2="380" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4" />

    <!-- Rahu Point (At 45°: x=220+113=333, y=280-113=167) -->
    <circle cx="333" cy="167" r="10" fill="#8b5cf6" />
    <text x="350" y="160" fill="#c4b5fd" font-size="14" font-weight="800">राहु (Rahu)</text>
    <text x="350" y="178" fill="#94a3b8" font-size="11">६०° (मिथुन)</text>

    <!-- Moon Point (At 210°: x=220-138=82, y=280+80=360) -->
    <circle cx="82" cy="360" r="10" fill="#38bdf8" />
    <text x="25" y="390" fill="#7dd3fc" font-size="14" font-weight="800">चन्द्र (Moon)</text>
    <text x="25" y="408" fill="#94a3b8" font-size="11">२४०° (धनु)</text>

    <!-- Arc Path Connecting Rahu to Moon -->
    <path d="M 333 167 A 160 160 0 0 1 82 360" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6,6" />

    <!-- Midpoint Bhrigu Bindu (At 127.5° approx: x=220-30=190, y=280+157=437) -->
    <circle cx="190" cy="437" r="14" fill="url(#bbGlow)" filter="url(#shadow)" />
    <circle cx="190" cy="437" r="6" fill="#ffffff" />
    <text x="190" y="475" text-anchor="middle" fill="#f43f5e" font-size="16" font-weight="900">भृगु बिंदु (BB)</text>
    <text x="190" y="495" text-anchor="middle" fill="#fde047" font-size="12" font-weight="700">१५०° (कन्या राशि • Virgo)</text>
  </g>

  <!-- Right: Mathematical Formulation & Trigger Rules -->
  <g transform="translate(530, 110)" filter="url(#shadow)">
    <rect width="420" height="520" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.8" />
    <text x="210" y="35" text-anchor="middle" fill="#fde047" font-size="16" font-weight="800">गणितीय सूत्र एवं सक्रियण विधान</text>

    <!-- Formula Box -->
    <g transform="translate(20, 60)">
      <rect width="380" height="95" rx="8" fill="#131c2e" stroke="#f59e0b" stroke-width="1.5" />
      <text x="190" y="30" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="800">📐 भृगु बिंदु (BB) गणितीय सूत्र:</text>
      <text x="190" y="58" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">BB = (राहु स्पष्ट अंश + चन्द्र स्पष्ट अंश) / २</text>
      <text x="190" y="80" text-anchor="middle" fill="#94a3b8" font-size="12">यदि अंतर १८०° से अधिक हो, तो १८०° जोड़कर मध्य निकालें</text>
    </g>

    <!-- 3 Trigger Milestones -->
    <g transform="translate(20, 175)">
      <text x="0" y="20" fill="#34d399" font-size="14.5" font-weight="800">⚡ गोचर सक्रियण के ३ अचूक फलित नियम:</text>

      <g transform="translate(0, 35)">
        <rect width="380" height="75" rx="6" fill="#1e293b" />
        <text x="15" y="25" fill="#fde047" font-size="13" font-weight="700">१. गोचर का गुरु जब BB को स्पर्श करे:</text>
        <text x="15" y="48" fill="#e2e8f0" font-size="12">विवाह, प्रथम संतति, उच्च पद प्राप्ति, तीर्थ यात्रा, अथवा</text>
        <text x="15" y="65" fill="#a7f3d0" font-size="11.5">जीवन की सबसे बड़ी शुभ घटना घटित होती है।</text>
      </g>

      <g transform="translate(0, 120)">
        <rect width="380" height="75" rx="6" fill="#1e293b" />
        <text x="15" y="25" fill="#60a5fa" font-size="13" font-weight="700">२. गोचर का शनि जब BB को स्पर्श करे:</text>
        <text x="15" y="48" fill="#e2e8f0" font-size="12">प्रारब्ध का सबसे बड़ा कर्म-हिसाब, आजीविका परिवर्तन,</text>
        <text x="15" y="65" fill="#93c5fd" font-size="11.5">कठोर अनुशासन एवं स्थायी दायित्व की शुरुआत।</text>
      </g>

      <g transform="translate(0, 205)">
        <rect width="380" height="75" rx="6" fill="#1e293b" />
        <text x="15" y="25" fill="#f87171" font-size="13" font-weight="700">३. गोचर का राहु/केतु जब BB को स्पर्श करे:</text>
        <text x="15" y="48" fill="#e2e8f0" font-size="12">जीवन में १८०° का अप्रत्याशित मोड़, विदेश गमन,</text>
        <text x="15" y="65" fill="#fca5a5" font-size="11.5">आकस्मिक आध्यात्मिक क्रांति अथवा भ्रम का निवारण।</text>
      </g>
    </g>
  </g>

  <!-- Bottom Synthesis Box -->
  <g transform="translate(60, 660)" filter="url(#shadow)">
    <rect width="890" height="170" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.5" />
    <text x="30" y="32" fill="#fde047" font-size="15" font-weight="800">🌟 भृगु बिंदु (BB) का आध्यात्मिक महत्व:</text>
    <text x="30" y="60" fill="#e2e8f0" font-size="13.5">राहु जातक की इस जन्म की 'अतृप्त इच्छा' (Future Desire) का प्रतीक है, और चन्द्रमा 'मन एवं पूर्व संचित संस्कार' का।</text>
    <text x="30" y="85" fill="#e2e8f0" font-size="13.5">इन दोनों का गणितीय मध्य बिंदु वह धुरी है जहां प्रारब्ध और पुरुषार्थ का मिलन होता है। जब भी कोई धीमा ग्रह इस बिंदु को छूता है,</text>
    <text x="30" y="110" fill="#38bdf8" font-size="13">जातक के जीवन में काल-चक्र की सुई घूम जाती है और वह घटना टल नहीं सकती।</text>
    <text x="30" y="145" fill="#94a3b8" font-size="12">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</text>
  </g>
</svg>'''
    write_svg("bnn_bhrigu_bindu_diagram.svg", svg)

# -------------------------------------------------------------
# Chart 10: BNN 7-Step Predictive Algorithm Flowchart
# -------------------------------------------------------------
def make_protocol_flowchart():
    width, height = 1000, 940
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">बी.एन.एन. ७-चरणीय फलित निर्णय प्रवाह आरेख</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">BNN 7-Step Predictive Algorithm Protocol • तार्किक एवं अचूक कुण्डली विश्लेषण विधि</text>

  <!-- 7 Stepped Pipeline Cards -->
  <!-- Step 1 -->
  <g transform="translate(60, 105)" filter="url(#shadow)">
    <rect width="880" height="85" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1.5" />
    <rect width="110" height="85" rx="8" fill="#b45309" />
    <text x="55" y="38" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">चरण १</text>
    <text x="55" y="60" text-anchor="middle" fill="#fde047" font-size="12">Step 1</text>
    
    <text x="135" y="34" fill="#fde047" font-size="15.5" font-weight="800">जीव एवं कर्म कारक की पहचान (Identify Jeeva &amp; Karma Karakas)</text>
    <text x="135" y="58" fill="#e2e8f0" font-size="13">• पुरुष जातक = गुरु (Jupiter), स्त्री जातक = शुक्र (Venus), आजीविका/प्रारब्ध = शनि (Saturn)</text>
    <text x="750" y="48" text-anchor="middle" fill="#34d399" font-size="13" font-weight="700">प्राथमिक धुरी</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(60, 205)" filter="url(#shadow)">
    <rect width="880" height="85" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
    <rect width="110" height="85" rx="8" fill="#0369a1" />
    <text x="55" y="38" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">चरण २</text>
    <text x="55" y="60" text-anchor="middle" fill="#e0f2fe" font-size="12">Step 2</text>
    
    <text x="135" y="34" fill="#38bdf8" font-size="15.5" font-weight="800">१-५-९ दिशा त्रिकोण युति संकलन (Collate 1-5-9 Directional Trines)</text>
    <text x="135" y="58" fill="#e2e8f0" font-size="13">• समान दिशा (अग्नि, पृथ्वी, वायु, जल) में बैठे सभी ग्रहों को एक साथ युत मानें (प्रभाव भार: ७५%–१००%)</text>
    <text x="750" y="48" text-anchor="middle" fill="#fde047" font-size="13" font-weight="700">७५%-१००% युति</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(60, 305)" filter="url(#shadow)">
    <rect width="880" height="85" rx="8" fill="#0f172a" stroke="#059669" stroke-width="1.5" />
    <rect width="110" height="85" rx="8" fill="#047857" />
    <text x="55" y="38" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">चरण ३</text>
    <text x="55" y="60" text-anchor="middle" fill="#d1fae5" font-size="12">Step 3</text>
    
    <text x="135" y="34" fill="#34d399" font-size="15.5" font-weight="800">१-७ सम्मुख दृष्टि प्रभाव (Inspect 1-7 Opposite Direction Aspects)</text>
    <text x="135" y="58" fill="#e2e8f0" font-size="13">• ७वें भाव में स्थित ग्रह का ५०% प्रत्यक्ष प्रभाव; पूर्व ↔ पश्चिम एवं उत्तर ↔ दक्षिण कर्म-साक्षात्कार</text>
    <text x="750" y="48" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="700">५०% प्रभाव</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(60, 405)" filter="url(#shadow)">
    <rect width="880" height="85" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5" />
    <rect width="110" height="85" rx="8" fill="#6d28d9" />
    <text x="55" y="38" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">चरण ४</text>
    <text x="55" y="60" text-anchor="middle" fill="#ede9fe" font-size="12">Step 4</text>
    
    <text x="135" y="34" fill="#c084fc" font-size="15.5" font-weight="800">+१ अग्रिम एवं -१ पृष्ठ भाव संबंध (Evaluate +1 Next / -1 Rear Influences)</text>
    <text x="135" y="58" fill="#e2e8f0" font-size="13">• +१ अगला भाव = भावी कर्म व दिशा (१५%); -१ पिछला भाव = संचित प्रारब्ध व पूर्व ऋण (१५%)</text>
    <text x="750" y="48" text-anchor="middle" fill="#f472b6" font-size="13" font-weight="700">१५% अग्र/पृष्ठ</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(60, 505)" filter="url(#shadow)">
    <rect width="880" height="85" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5" />
    <rect width="110" height="85" rx="8" fill="#be185d" />
    <text x="55" y="38" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">चरण ५</text>
    <text x="55" y="60" text-anchor="middle" fill="#fce7f3" font-size="12">Step 5</text>
    
    <text x="135" y="34" fill="#f472b6" font-size="15.5" font-weight="800">ग्रहों का अंश-क्रम एवं वक्री विनिमय (Order by Degree &amp; Retrograde Adjustments)</text>
    <text x="135" y="58" fill="#e2e8f0" font-size="13">• निम्न अंश ग्रह आगे, उच्च अंश ग्रह पीछे; वक्री ग्रह का पूर्व भाव में ५०% अस्तित्व, राशि परिवर्तन विनिमय</text>
    <text x="750" y="48" text-anchor="middle" fill="#fde047" font-size="13" font-weight="700">अंश वक्री नियम</text>
  </g>

  <!-- Step 6 -->
  <g transform="translate(60, 605)" filter="url(#shadow)">
    <rect width="880" height="85" rx="8" fill="#0f172a" stroke="#e11d48" stroke-width="1.5" />
    <rect width="110" height="85" rx="8" fill="#be123c" />
    <text x="55" y="38" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900">चरण ६</text>
    <text x="55" y="60" text-anchor="middle" fill="#ffe4e6" font-size="12">Step 6</text>
    
    <text x="135" y="34" fill="#fb7185" font-size="15.5" font-weight="800">शुभ/पाप-कर्तरी वेध का निर्धारण (Determine Kartari Enclosure Status)</text>
    <text x="135" y="58" fill="#e2e8f0" font-size="13">• २/१२ भावों में शुभ ग्रह = संरक्षण व निर्बाध सफलता; क्रूर ग्रह (राहु/शनि) = घेराबंदी व कार्मिक अवरोध</text>
    <text x="750" y="48" text-anchor="middle" fill="#cbd5e1" font-size="13" font-weight="700">वेध सुरक्षा</text>
  </g>

  <!-- Step 7 -->
  <g transform="translate(60, 705)" filter="url(#shadow)">
    <rect width="880" height="85" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2" />
    <rect width="110" height="85" rx="8" fill="url(#goldGrad)" />
    <text x="55" y="38" text-anchor="middle" fill="#0f172a" font-size="16" font-weight="900">चरण ७</text>
    <text x="55" y="60" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">Step 7</text>
    
    <text x="135" y="34" fill="#fde047" font-size="15.5" font-weight="800">गोचर, पर्याय एवं भृगु बिंदु द्वारा सक्रियण (Timing via Transits &amp; Bhrigu Bindu)</text>
    <text x="135" y="58" fill="#e2e8f0" font-size="13">• शनि ३०-वर्षीय पर्याय, गुरु १ वर्ष/राशि प्रगति एवं भृगु बिंदु (BB) स्पर्श पर अचूक काल-निर्धारण</text>
    <text x="750" y="48" text-anchor="middle" fill="#34d399" font-size="13" font-weight="900">अचूक फलित</text>
  </g>

  <!-- Footer -->
  <g transform="translate(60, 810)">
    <rect width="880" height="85" rx="8" fill="#131c2e" stroke="#334155" stroke-width="1" />
    <text x="25" y="32" fill="#fde047" font-size="14.5" font-weight="750">⚡ फलित निष्पत्ति:</text>
    <text x="145" y="32" fill="#cbd5e1" font-size="13.5">इन ७ चरणों का क्रमबद्ध पालन करने पर बिना किसी सॉफ्टवेयर अथवा जटिल गणित के अचूक फलित प्राप्त होता है।</text>
    <text x="25" y="60" fill="#94a3b8" font-size="12.5">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</text>
  </g>
</svg>'''
    write_svg("bnn_protocol_flowchart.svg", svg)

if __name__ == "__main__":
    print("Generating all 8 BNN charts...")
    make_philosophy_hierarchy_chart()
    make_kartari_flank_diamond_chart()
    make_karaka_relationship_wheel()
    make_elemental_directional_diamond_chart()
    make_jeeva_12bhavas_diamond_chart()
    make_major_conjunctions_diamond_chart()
    make_triplet_rajyogas_diamond_chart()
    make_progression_paryaya_chart()
    make_bhrigu_bindu_diagram()
    make_protocol_flowchart()
    print("All charts successfully generated!")
