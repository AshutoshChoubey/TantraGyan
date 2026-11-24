#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exhaustive Master Compendium & Multi-Format Publishing Engine
Flagship Volume IV: वैदिक कुण्डली विचार एवं गणित महाग्रंथ (The Cosmic Algorithm)

Complete 13-Chapter Encyclopedic Manuscript with:
- Brihat Parashara Hora Shastra (BPHS), Phaladeepika, Saravali Sanskrit verses
- Step-by-step astronomical mathematics and spherical trigonometry
- Runnable, production-grade Python and TypeScript algorithmic engines
- Exhaustive reference tables (27 Nakshatras, 16 Vargas, 337 Bindus, 36 Gunas, 85 Rules)
- Anonymized benchmark native case study: जातक 'क' (DOB: 28 Oct 1994, 03:45 AM, Garhwa)
- Multi-format generation: Web Presentation Edition, Print Layout, Vector Master PDF, 3D Flipbook Reader
"""

import os
import sys
import subprocess
from pathlib import Path

PROJECT_ROOT = Path("/Users/apple/Movies/ap/TantraGyan")
OUTPUT_WEB = PROJECT_ROOT / "kundali-ganita.html"
OUTPUT_PRINT = PROJECT_ROOT / "kundali-ganita-print.html"
OUTPUT_PDF = PROJECT_ROOT / "kundali-ganita-vichar-mahagranth.pdf"
OUTPUT_READER = PROJECT_ROOT / "kundali-ganita-reader.html"
READER_TEMPLATE_SRC = PROJECT_ROOT / "reader.html"

# SVG Diagrams
def get_diamond_chart_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="600" class="vedic-diamond-chart" style="max-width:540px; margin:1.5rem auto; display:block; background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
  <defs>
    <linearGradient id="emeraldGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c89d3d" />
      <stop offset="50%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
    <radialGradient id="auraGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="rgba(16, 185, 129, 0.18)" />
      <stop offset="100%" stop-color="transparent" />
    </radialGradient>
  </defs>
  <rect width="600" height="600" fill="#090d16" rx="12" />
  <circle cx="300" cy="300" r="230" fill="url(#auraGlow)" />
  <rect x="24" y="24" width="552" height="552" fill="none" stroke="url(#emeraldGold)" stroke-width="2.5" />
  <line x1="24" y1="24" x2="576" y2="576" stroke="#c89d3d" stroke-width="1.8" />
  <line x1="576" y1="24" x2="24" y2="576" stroke="#c89d3d" stroke-width="1.8" />
  <polygon points="300,24 576,300 300,576 24,300" fill="none" stroke="#10b981" stroke-width="2.2" />

  <rect x="150" y="32" width="300" height="34" rx="6" fill="rgba(5, 150, 105, 0.35)" stroke="#10b981" stroke-width="1" />
  <text x="300" y="54" fill="#f8fafc" font-size="14.5" font-weight="700" text-anchor="middle">जन्म कुण्डली (Janm Kundli D1) • जातक 'क'</text>

  <!-- House 1 (Lagna - Top Diamond) -->
  <text x="300" y="115" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">१म भाव (Lagna 09°21')</text>
  <text x="300" y="140" fill="#34d399" font-size="12" text-anchor="middle">कन्या (Virgo) • बुध (Bhadra Yoga)</text>
  <text x="300" y="168" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">बुध (Budha 24°46')</text>

  <!-- House 2 (Top Left Triangle) -->
  <text x="160" y="85" fill="#94a3b8" font-size="11" text-anchor="middle">२ भाव (तुला)</text>
  <text x="160" y="115" fill="#f8fafc" font-size="13" text-anchor="middle">सूर्य (10°28') नीचभंग</text>
  <text x="160" y="135" fill="#f8fafc" font-size="13" text-anchor="middle">गुरु (26°44')</text>

  <!-- House 3 (Left Outer Triangle) -->
  <text x="95" y="180" fill="#94a3b8" font-size="11" text-anchor="middle">३ भाव (वृश्चिक)</text>
  <text x="95" y="210" fill="#f8fafc" font-size="13" text-anchor="middle">शुक्र (26°39')</text>
  <text x="95" y="235" fill="#a855f7" font-size="13" text-anchor="middle">राहु (20°44')</text>

  <!-- House 4 (Left Diamond) -->
  <text x="165" y="285" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">४ भाव (धनु)</text>
  <text x="165" y="315" fill="#64748b" font-size="12" text-anchor="middle">केन्द्र स्थान</text>

  <!-- House 5 (Bottom Left Triangle) -->
  <text x="95" y="420" fill="#94a3b8" font-size="11" text-anchor="middle">५ भाव (मकर)</text>
  <text x="95" y="445" fill="#64748b" font-size="12" text-anchor="middle">त्रिकोण स्थान</text>

  <!-- House 6 (Bottom Left Triangle Inner) -->
  <text x="160" y="515" fill="#94a3b8" font-size="11" text-anchor="middle">६ भाव (कुम्भ)</text>
  <text x="160" y="540" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">शनि (11°41') स्वराशि</text>

  <!-- House 7 (Bottom Diamond) -->
  <text x="300" y="430" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">७ भाव (मीन)</text>
  <text x="300" y="460" fill="#64748b" font-size="12" text-anchor="middle">जाया भाव • केन्द्र</text>

  <!-- House 8 (Bottom Right Triangle Inner) -->
  <text x="440" y="515" fill="#94a3b8" font-size="11" text-anchor="middle">८ भाव (मेष)</text>
  <text x="440" y="540" fill="#64748b" font-size="12" text-anchor="middle">आयु स्थान (अष्टम)</text>

  <!-- House 9 (Bottom Right Triangle) -->
  <text x="505" y="420" fill="#94a3b8" font-size="11" text-anchor="middle">९ भाव (वृषभ)</text>
  <text x="505" y="445" fill="#a855f7" font-size="13" text-anchor="middle">केतु (20°44') उच्च</text>

  <!-- House 10 (Right Diamond) -->
  <text x="435" y="285" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">१० भाव (मिथुन)</text>
  <text x="435" y="315" fill="#64748b" font-size="12" text-anchor="middle">कर्म भाव • केन्द्र</text>

  <!-- House 11 (Top Right Triangle) -->
  <text x="505" y="180" fill="#94a3b8" font-size="11" text-anchor="middle">११ भाव (कर्क)</text>
  <text x="505" y="205" fill="#f8fafc" font-size="13" font-weight="700" text-anchor="middle">चन्द्र (13°10') स्वराशि</text>
  <text x="505" y="225" fill="#f87171" font-size="13" text-anchor="middle">मंगल (21°04') नीचभंग</text>

  <!-- House 12 (Top Right Triangle Inner) -->
  <text x="440" y="85" fill="#94a3b8" font-size="11" text-anchor="middle">१२ भाव (सिंह)</text>
  <text x="440" y="115" fill="#64748b" font-size="12" text-anchor="middle">मोक्ष स्थान</text>
</svg>'''

def get_panchanga_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 320" width="100%" height="320" class="panchanga-pillars" style="max-width:540px; margin:1.5rem auto; display:block; background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
  <rect width="680" height="320" fill="#090d16" rx="12" />
  <text x="340" y="35" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">काल के पांच दिव्य अंग (पंचांग रचना एवं तत्वीय संतुलन)</text>
  
  <rect x="25" y="65" width="115" height="230" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
  <circle cx="82" cy="100" r="18" fill="rgba(16, 185, 129, 0.25)" />
  <text x="82" y="106" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">१</text>
  <text x="82" y="140" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">तिथि</text>
  <text x="82" y="165" fill="#34d399" font-size="11" text-anchor="middle">चंद्र-सूर्य अंतर (12°)</text>
  <text x="82" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">कृष्ण अष्टमी (272°)</text>
  <text x="82" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">जया तिथि</text>
  <text x="82" y="265" fill="#a7f3d0" font-size="11" font-weight="600" text-anchor="middle">जल तत्व</text>

  <rect x="155" y="65" width="115" height="230" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
  <circle cx="212" cy="100" r="18" fill="rgba(2, 132, 199, 0.25)" />
  <text x="212" y="106" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">२</text>
  <text x="212" y="140" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">वार</text>
  <text x="212" y="165" fill="#38bdf8" font-size="11" text-anchor="middle">सूर्योदय का स्वामी</text>
  <text x="212" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">शुक्रवार</text>
  <text x="212" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">शुक्र (भृगु)</text>
  <text x="212" y="265" fill="#bae6fd" font-size="11" font-weight="600" text-anchor="middle">अग्नि तत्व</text>

  <rect x="285" y="65" width="115" height="230" rx="8" fill="#0f172a" stroke="#c89d3d" stroke-width="1.5" />
  <circle cx="342" cy="100" r="18" fill="rgba(200, 157, 61, 0.25)" />
  <text x="342" y="106" fill="#facc15" font-size="14" font-weight="700" text-anchor="middle">३</text>
  <text x="342" y="140" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">नक्षत्र</text>
  <text x="342" y="165" fill="#facc15" font-size="11" text-anchor="middle">चंद्रमा का स्थान (13°20')</text>
  <text x="342" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">पुष्य नक्षत्र (पद 3)</text>
  <text x="342" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">बृहस्पति/शनि</text>
  <text x="342" y="265" fill="#fde68a" font-size="11" font-weight="600" text-anchor="middle">वायु तत्व</text>

  <rect x="415" y="65" width="115" height="230" rx="8" fill="#0f172a" stroke="#9333ea" stroke-width="1.5" />
  <circle cx="472" cy="100" r="18" fill="rgba(147, 51, 234, 0.25)" />
  <text x="472" y="106" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">४</text>
  <text x="472" y="140" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">योग</text>
  <text x="472" y="165" fill="#c084fc" font-size="11" text-anchor="middle">सूर्य + चंद्र योग</text>
  <text x="472" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">साध्य योग</text>
  <text x="472" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">शुभ फलदायी</text>
  <text x="472" y="265" fill="#d8b4fe" font-size="11" font-weight="600" text-anchor="middle">आकाश तत्व</text>

  <rect x="545" y="65" width="115" height="230" rx="8" fill="#0f172a" stroke="#ea580c" stroke-width="1.5" />
  <circle cx="602" cy="100" r="18" fill="rgba(234, 88, 12, 0.25)" />
  <text x="602" y="106" fill="#fb923c" font-size="14" font-weight="700" text-anchor="middle">५</text>
  <text x="602" y="140" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">करण</text>
  <text x="602" y="165" fill="#fb923c" font-size="11" text-anchor="middle">आधी तिथि (6°)</text>
  <text x="602" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">कौलव करण</text>
  <text x="602" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">कार्य सिद्धि</text>
  <text x="602" y="265" fill="#fed7aa" font-size="11" font-weight="600" text-anchor="middle">पृथ्वी तत्व</text>
</svg>'''

def get_dasha_tree_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 320" width="100%" height="320" style="max-width:540px; margin:1.5rem auto; display:block; background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
  <rect width="680" height="320" fill="#090d16" rx="12" />
  <text x="340" y="35" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">120-वर्षीय विंशोत्तरी दशा: 4-स्तरीय सूक्ष्म विभाजन वृक्ष</text>
  
  <rect x="40" y="65" width="600" height="48" rx="8" fill="rgba(5, 150, 105, 0.3)" stroke="#10b981" stroke-width="1.5" />
  <text x="60" y="95" fill="#6ee7b7" font-size="14" font-weight="700">१. महादशा (MD):</text>
  <text x="200" y="95" fill="#f8fafc" font-size="14">कुल 120 वर्ष (सूर्य 6, चंद्र 10, मंगल 7, राहु 18, गुरु 16, शनि 19, बुध 17, केतु 7, शुक्र 20)</text>

  <rect x="80" y="125" width="560" height="48" rx="8" fill="rgba(2, 132, 199, 0.25)" stroke="#0284c7" stroke-width="1.5" />
  <text x="100" y="155" fill="#7dd3fc" font-size="14" font-weight="700">२. अंतर्दशा (AD):</text>
  <text x="230" y="155" fill="#f8fafc" font-size="14">सूत्र: (वर्ष A × वर्ष B) ÷ 120 = अवधि (वर्ष एवं माह)</text>

  <rect x="120" y="185" width="520" height="48" rx="8" fill="rgba(124, 58, 237, 0.25)" stroke="#7c3aed" stroke-width="1.5" />
  <text x="140" y="215" fill="#d8b4fe" font-size="14" font-weight="700">३. प्रत्यंतर्दशा (PD):</text>
  <text x="270" y="215" fill="#f8fafc" font-size="14">सूत्र: (AD वर्ष × वर्ष C) ÷ 120 = सटीक दिन एवं सप्ताह</text>

  <rect x="160" y="245" width="480" height="48" rx="8" fill="rgba(200, 157, 61, 0.25)" stroke="#c89d3d" stroke-width="1.5" />
  <text x="180" y="275" fill="#fde047" font-size="14" font-weight="700">४. सूक्ष्म दशा (SD):</text>
  <text x="300" y="275" fill="#f8fafc" font-size="14">सूत्र: (PD वर्ष × वर्ष D) ÷ 120 = सटीक घंटे एवं मिनट</text>
</svg>'''

def get_ashtakavarga_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" width="100%" height="300" style="max-width:540px; margin:1.5rem auto; display:block; background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
  <rect width="680" height="300" fill="#090d16" rx="12" />
  <text x="340" y="35" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">अष्टकवर्ग 337 बिंदु: 28-बिंदु कसौटी एवं कक्षी गोचर</text>
  
  <rect x="50" y="65" width="170" height="200" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2" />
  <circle cx="135" cy="105" r="24" fill="rgba(16, 185, 129, 0.2)" />
  <text x="135" y="112" fill="#34d399" font-size="16" font-weight="800" text-anchor="middle">≥ 28</text>
  <text x="135" y="150" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">परम शुभ (उत्कृष्ट)</text>
  <text x="135" y="180" fill="#94a3b8" font-size="12" text-anchor="middle">सहज सफलता</text>
  <text x="135" y="200" fill="#94a3b8" font-size="12" text-anchor="middle">धन लाभ एवं विजय</text>
  <text x="135" y="235" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">गोचर फल: 100%</text>

  <rect x="255" y="65" width="170" height="200" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
  <circle cx="340" cy="105" r="24" fill="rgba(2, 132, 199, 0.2)" />
  <text x="340" y="112" fill="#38bdf8" font-size="16" font-weight="800" text-anchor="middle">25-27</text>
  <text x="340" y="150" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">मध्यम (संतुलित)</text>
  <text x="340" y="180" fill="#94a3b8" font-size="12" text-anchor="middle">परिश्रम के अनुरूप</text>
  <text x="340" y="200" fill="#94a3b8" font-size="12" text-anchor="middle">स्थिर जीवन गति</text>
  <text x="340" y="235" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">गोचर फल: 60%</text>

  <rect x="460" y="65" width="170" height="200" rx="10" fill="#0f172a" stroke="#f43f5e" stroke-width="2" />
  <circle cx="545" cy="105" r="24" fill="rgba(244, 63, 94, 0.2)" />
  <text x="545" y="112" fill="#fb7185" font-size="16" font-weight="800" text-anchor="middle">&lt; 25</text>
  <text x="545" y="150" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">चुनौतीपूर्ण (सावधान)</text>
  <text x="545" y="180" fill="#94a3b8" font-size="12" text-anchor="middle">अवरोध एवं व्यय</text>
  <text x="545" y="200" fill="#94a3b8" font-size="12" text-anchor="middle">साधना व उपाय अनिवार्य</text>
  <text x="545" y="235" fill="#fb7185" font-size="12" font-weight="700" text-anchor="middle">गोचर फल: संघर्ष</text>
</svg>'''

# -------------------------------------------------------------------------------------------------
# BUILD AND COMPILE COMPLETE SUITE
# -------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 80)
    print("🕉️  Compiling Multi-Format Master Compendium...")
    print("=" * 80)
    
    sys.path.insert(0, str(PROJECT_ROOT))
    sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
    try:
        from scripts.build_exhaustive_kundali_ganita_content import build_master_publications
    except ImportError:
        from build_exhaustive_kundali_ganita_content import build_master_publications

    build_master_publications(
        output_web=OUTPUT_WEB,
        output_print=OUTPUT_PRINT,
        output_pdf=OUTPUT_PDF,
        output_reader=OUTPUT_READER,
        reader_src=READER_TEMPLATE_SRC
    )
