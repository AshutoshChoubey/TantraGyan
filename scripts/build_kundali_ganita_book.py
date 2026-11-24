#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the complete Flagship Vol 4 suite for Tantra Gyan:
1. kundali-ganita-reader.html (3D Digital Interactive Flipbook Reader)
2. kundali-ganita.html (Complete Responsive Web Presentation Edition)
3. kundali-ganita-print.html (Print & PDF Generation Source)

Title: वैदिक कुण्डली विचार एवं गणित महाग्रंथ: खगोलीय सूत्र, 16 वर्ग चक्र एवं फलित संयोजन
English: The Cosmic Algorithm: Vedic Horoscope Mathematics & Destiny Decoded
Author: ज्योतिषाचार्य आशुतोष कुमार चौबे
Tantra Gyan Research Center • https://t.worldgyan.com
"""

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/apple/Movies/ap/TantraGyan")
READER_TEMPLATE_SRC = PROJECT_ROOT / "reader.html"
OUTPUT_READER = PROJECT_ROOT / "kundali-ganita-reader.html"
OUTPUT_WEB = PROJECT_ROOT / "kundali-ganita.html"
OUTPUT_PRINT = PROJECT_ROOT / "kundali-ganita-print.html"
OUTPUT_PDF = PROJECT_ROOT / "kundali-ganita-vichar-mahagranth.pdf"

print("=" * 80)
print("🕉️ Building Flagship Vol 4: वैदिक कुण्डली विचार एवं गणित महाग्रंथ")
print("=" * 80)

# SVG Diagrams Generator
def get_diamond_chart_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="600" class="vedic-diamond-chart" style="max-width:540px; margin:1rem auto; display:block; background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
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

  <rect x="160" y="32" width="280" height="32" rx="6" fill="rgba(5, 150, 105, 0.35)" stroke="#10b981" stroke-width="1" />
  <text x="300" y="53" fill="#f8fafc" font-size="14.5" font-weight="700" text-anchor="middle">जन्म कुण्डली (Janm Kundli D1) • कन्या लग्न</text>

  <!-- House 1 (Lagna - Top Diamond) -->
  <text x="300" y="115" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">१म भाव (Lagna 09°21')</text>
  <text x="300" y="140" fill="#34d399" font-size="12" text-anchor="middle">कन्या (Virgo) • बुध (Bhadra Yoga)</text>
  <text x="300" y="168" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">बुध (Budha 24°46')</text>

  <!-- House 2 (Top Left Triangle) -->
  <text x="160" y="85" fill="#94a3b8" font-size="11" text-anchor="middle">२ भाव (तुला)</text>
  <text x="160" y="115" fill="#f8fafc" font-size="13" text-anchor="middle">सूर्य (10°28') नीचभंग</text>
  <text x="160" y="135" fill="#f8fafc" font-size="13" text-anchor="middle">गुरु (22°08')</text>

  <!-- House 3 (Left Top Triangle) -->
  <text x="80" y="165" fill="#94a3b8" font-size="11" text-anchor="middle">३ भाव (वृश्चिक)</text>
  <text x="80" y="195" fill="#f8fafc" font-size="13" text-anchor="middle">राहु (20°35')</text>

  <!-- House 4 (Left Diamond) -->
  <text x="160" y="295" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">४ भाव (धनु - सुख)</text>
  <text x="160" y="325" fill="#f8fafc" font-size="14" font-weight="600" text-anchor="middle">शुक्र (05°34')</text>

  <!-- House 5 (Left Bottom Triangle) -->
  <text x="80" y="440" fill="#94a3b8" font-size="11" text-anchor="middle">५ भाव (मकर)</text>
  <text x="80" y="470" fill="#cbd5e1" font-size="12" text-anchor="middle">—</text>

  <!-- House 6 (Bottom Left Triangle) -->
  <text x="160" y="520" fill="#94a3b8" font-size="11" text-anchor="middle">६ भाव (कुम्भ)</text>
  <text x="160" y="545" fill="#f8fafc" font-size="13" text-anchor="middle">शनि वक्री (12°01')</text>

  <!-- House 7 (Bottom Diamond) -->
  <text x="300" y="445" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">७म भाव (मीन - जाया)</text>
  <text x="300" y="475" fill="#cbd5e1" font-size="13" text-anchor="middle">—</text>

  <!-- House 8 (Bottom Right Triangle) -->
  <text x="440" y="520" fill="#94a3b8" font-size="11" text-anchor="middle">८ भाव (मेष)</text>
  <text x="440" y="545" fill="#cbd5e1" font-size="12" text-anchor="middle">—</text>

  <!-- House 9 (Right Bottom Triangle) -->
  <text x="520" y="440" fill="#94a3b8" font-size="11" text-anchor="middle">९ भाव (वृषभ)</text>
  <text x="520" y="470" fill="#f8fafc" font-size="13" text-anchor="middle">केतु (20°35')</text>

  <!-- House 10 (Right Diamond) -->
  <text x="440" y="295" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">१० भाव (मिथुन - कर्म)</text>
  <text x="440" y="325" fill="#cbd5e1" font-size="13" text-anchor="middle">—</text>

  <!-- House 11 (Right Top Triangle) -->
  <text x="520" y="165" fill="#38bdf8" font-size="11" text-anchor="middle">११ भाव (कर्क - लाभ)</text>
  <text x="520" y="195" fill="#f8fafc" font-size="14" font-weight="700" text-anchor="middle">चंद्र (13°10' पुष्य)</text>
  <text x="520" y="215" fill="#f8fafc" font-size="13" text-anchor="middle">मंगल (01°22')</text>

  <!-- House 12 (Top Right Triangle) -->
  <text x="440" y="85" fill="#94a3b8" font-size="11" text-anchor="middle">१२ भाव (सिंह)</text>
  <text x="440" y="115" fill="#cbd5e1" font-size="12" text-anchor="middle">—</text>
</svg>'''

def get_panchanga_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 320" width="100%" height="320" style="max-width:540px; margin:1rem auto; display:block; background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
  <rect width="680" height="320" fill="#090d16" rx="12" />
  <text x="340" y="35" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">पंचांग के पांच दिव्य अंग (The 5 Cosmic Limbs of Time)</text>
  
  <rect x="25" y="65" width="115" height="230" rx="8" fill="#0f172a" stroke="#059669" stroke-width="1.5" />
  <circle cx="82" cy="100" r="18" fill="rgba(5, 150, 105, 0.25)" />
  <text x="82" y="106" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">१</text>
  <text x="82" y="140" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">तिथि</text>
  <text x="82" y="165" fill="#38bdf8" font-size="11" text-anchor="middle">चंद्र-सूर्य दूरी (12°)</text>
  <text x="82" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">कृष्ण अष्टमी</text>
  <text x="82" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">(72.46% भुक्त)</text>
  <text x="82" y="265" fill="#6ee7b7" font-size="11" font-weight="600" text-anchor="middle">जल तत्व</text>

  <rect x="155" y="65" width="115" height="230" rx="8" fill="#0f172a" stroke="#c89d3d" stroke-width="1.5" />
  <circle cx="212" cy="100" r="18" fill="rgba(200, 157, 61, 0.25)" />
  <text x="212" y="106" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">२</text>
  <text x="212" y="140" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">वार</text>
  <text x="212" y="165" fill="#fbbf24" font-size="11" text-anchor="middle">सूर्योदय स्वामी</text>
  <text x="212" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">शुक्रवार</text>
  <text x="212" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">(शुक्रेन्द्र)</text>
  <text x="212" y="265" fill="#fcd34d" font-size="11" font-weight="600" text-anchor="middle">अग्नि तत्व</text>

  <rect x="285" y="65" width="115" height="230" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
  <circle cx="342" cy="100" r="18" fill="rgba(2, 132, 199, 0.25)" />
  <text x="342" y="106" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">३</text>
  <text x="342" y="140" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">नक्षत्र</text>
  <text x="342" y="165" fill="#38bdf8" font-size="11" text-anchor="middle">चंद्रमा का घर</text>
  <text x="342" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">पुष्य (चरण ३)</text>
  <text x="342" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">स्वामी: शनि</text>
  <text x="342" y="265" fill="#7dd3fc" font-size="11" font-weight="600" text-anchor="middle">वायु तत्व</text>

  <rect x="415" y="65" width="115" height="230" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5" />
  <circle cx="472" cy="100" r="18" fill="rgba(124, 58, 237, 0.25)" />
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
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 320" width="100%" height="320" style="max-width:540px; margin:1rem auto; display:block; background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
  <rect width="680" height="320" fill="#090d16" rx="12" />
  <text x="340" y="35" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">120-वर्षीय विंशोत्तरी दशा: 4-स्तरीय सूक्ष्म विभाजन वृक्ष</text>
  
  <!-- Level 1: Mahadasha -->
  <rect x="40" y="65" width="600" height="48" rx="8" fill="rgba(5, 150, 105, 0.3)" stroke="#10b981" stroke-width="1.5" />
  <text x="60" y="95" fill="#6ee7b7" font-size="14" font-weight="700">१. महादशा (MD):</text>
  <text x="200" y="95" fill="#f8fafc" font-size="14">कुल 120 वर्ष (सूर्य 6, चंद्र 10, मंगल 7, राहु 18, गुरु 16, शनि 19, बुध 17, केतु 7, शुक्र 20)</text>

  <!-- Level 2: Antardasha -->
  <rect x="80" y="125" width="560" height="48" rx="8" fill="rgba(2, 132, 199, 0.25)" stroke="#0284c7" stroke-width="1.5" />
  <text x="100" y="155" fill="#7dd3fc" font-size="14" font-weight="700">२. अंतर्दशा (AD):</text>
  <text x="230" y="155" fill="#f8fafc" font-size="14">सूत्र: (वर्ष A × वर्ष B) ÷ 120 = अवधि (वर्ष एवं माह)</text>

  <!-- Level 3: Pratyantardasha -->
  <rect x="120" y="185" width="520" height="48" rx="8" fill="rgba(124, 58, 237, 0.25)" stroke="#7c3aed" stroke-width="1.5" />
  <text x="140" y="215" fill="#d8b4fe" font-size="14" font-weight="700">३. प्रत्यंतर्दशा (PD):</text>
  <text x="270" y="215" fill="#f8fafc" font-size="14">सूत्र: (AD वर्ष × वर्ष C) ÷ 120 = सटीक दिन एवं सप्ताह</text>

  <!-- Level 4: Sookshma Dasha -->
  <rect x="160" y="245" width="480" height="48" rx="8" fill="rgba(200, 157, 61, 0.25)" stroke="#c89d3d" stroke-width="1.5" />
  <text x="180" y="275" fill="#fde047" font-size="14" font-weight="700">४. सूक्ष्म दशा (SD):</text>
  <text x="300" y="275" fill="#f8fafc" font-size="14">सूत्र: (PD वर्ष × वर्ष D) ÷ 120 = सटीक घंटे एवं मिनट</text>
</svg>'''

def get_ashtakavarga_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" width="100%" height="300" style="max-width:540px; margin:1rem auto; display:block; background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
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

# Generate all 40 Pages for the Interactive Flipbook Reader
def build_pages():
    pages = []

    def make_page(num, chapter, title, body_html):
        return f'''    <article class="book-page-data" id="page-data-{num}" data-page="{num}" data-chapter="{chapter}" data-title="{title}" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page {num}: {title}">
      <meta itemprop="position" content="{num}">
      <meta itemprop="name" content="{title}">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem; border-bottom:1px solid rgba(16, 185, 129, 0.25); padding-bottom:0.4rem;">
          <div class="chapter-number" style="font-size:0.8rem; color:#10b981; font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">{chapter}</div>
          <h3 class="chapter-heading" style="font-size:1.15rem; color:#059669; font-family:'Noto Serif Devanagari', serif; font-weight:800; margin:0.2rem 0;">{title}</h3>
        </div>
        {body_html}
      </div>
    </article>
'''

    # Page 1: Cover Page
    p1 = '''<div class="cover-page-wrapper" style="text-align:center; padding:1.8rem 1rem;">
  <div style="font-size:1.1rem; color:#10b981; font-weight:700; margin-bottom:0.8rem;">॥ श्री गणेशाय नमः • ॐ नमः शिवाय ॥</div>
  <div style="margin:1.2rem auto;"><img src="assets/yantra.svg" alt="Sacred Yantra" width="115" height="115" style="filter: drop-shadow(0 0 16px rgba(16, 185, 129, 0.4));"></div>
  <div style="display:inline-block; padding:0.25rem 0.9rem; background:rgba(5, 150, 105, 0.15); border:1px solid #10b981; border-radius:20px; color:#10b981; font-size:0.8rem; font-weight:700; margin-bottom:0.6rem;">👑 FLAGSHIP VOL 4 • THE MASTER COMPENDIUM</div>
  <h1 style="font-size:1.75rem; color:#059669; font-family:'Noto Serif Devanagari', serif; font-weight:900; margin:0.5rem 0 0.3rem 0; line-height:1.35;">वैदिक कुण्डली विचार एवं गणित महाग्रंथ</h1>
  <div style="font-size:1.05rem; color:#0284c7; font-weight:700; margin-bottom:1rem;">खगोलीय सूत्र, 16 वर्ग चक्र एवं फलित संयोजन</div>
  <div style="font-size:0.9rem; color:#475569; font-weight:600; margin-bottom:1.4rem;">The Cosmic Algorithm: Vedic Horoscope Mathematics & Destiny Decoded</div>
  <p style="font-size:0.88rem; color:#334155; max-width:480px; margin:0 auto 1.4rem auto; line-height:1.65;">
    स्विस एफेमेरिस के जूलियन डे से लेकर 16 वर्ग कुण्डलियाँ, 337 बिंदु अष्टकवर्ग, 120-वर्षीय विंशोत्तरी दशा, 85 विवाह नियम एवं 23 जीवन क्षेत्रों के सभी गणना सूत्रों का सरल, प्रामाणिक एवं रोचक मानव व्याख्यान।
  </p>
  <div style="border-top:1px solid rgba(16, 185, 129, 0.3); border-bottom:1px solid rgba(16, 185, 129, 0.3); padding:0.75rem 0; max-width:440px; margin:0 auto; color:#1e293b; font-size:0.88rem;">
    <strong>प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</strong><br>
    <span style="font-size:0.78rem; color:#64748b;">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) • https://t.worldgyan.com</span>
  </div>
</div>'''
    pages.append(make_page(1, "मुखपृष्ठ • Cover", "वैदिक कुण्डली विचार एवं गणित महाग्रंथ", p1))

    # Page 2: Invocation & Parable
    p2 = '''<div style="text-align:center; padding:1.2rem;">
  <div style="font-size:1.6rem; margin-bottom:0.6rem;">🪐 📐 📜</div>
  <div class="shloka-box" style="background:rgba(5, 150, 105, 0.06); border:1px solid #10b981; border-radius:8px; padding:1.2rem; margin:0.8rem auto; max-width:540px;">
    <div style="font-family:'Noto Serif Devanagari',serif; font-size:1.02rem; font-weight:700; color:#065f46; line-height:1.8;">
      ॥ सिद्धांत-संहिता-होरा-रूपं स्कंध-त्रयात्मकम् ।<br>
      वेदस्य निर्मलं चक्षुर्ज्योतिःशास्त्रमनुत्तमम् ॥<br>
      ॥ गणितं च खगोलीयम् ग्रहाणां गति-निर्णयम् ।<br>
      मानवस्य च भाग्यस्य दर्पणं परमं शुभम् ॥
    </div>
  </div>
  <h4 style="color:#0f766e; margin-top:1rem; font-size:1.05rem;">प्रस्तावना: ब्रह्मांड का दिव्य कंप्यूटर</h4>
  <p style="text-align:justify; font-size:0.88rem; line-height:1.7; color:#334155;">
    वैदिक ज्योतिष कोई काल्पनिक मान्यता या अंधविश्वास नहीं है—यह ब्रह्मांड का एक अत्यंत परिष्कृत, अचूक एवं गणितीय विज्ञान है। जिस प्रकार एक आधुनिक सुपरकंप्यूटर शून्य (0) और एक (1) के बाइनरी कोड पर चलता है, ठीक उसी प्रकार यह संपूर्ण सृष्टि नवग्रहों की रश्मियों, 12 राशियों के कोणीय क्षेत्रों और 27 नक्षत्रों के सूक्ष्म स्पंदनों से संचालित होती है।
  </p>
  <p style="text-align:justify; font-size:0.88rem; line-height:1.7; color:#334155;">
    जब कोई बालक धरती पर अपना पहला श्वास लेता है, तो उस क्षण का संपूर्ण खगोलीय मानचित्र उसकी जन्म-कुण्डली के रूप में अंकित हो जाता है। इस ग्रंथ का उद्देश्य इसी दिव्य गणित को इतनी सरल भाषा में समझाना है कि बिना किसी पूर्व गणितीय ज्ञान के भी कोई भी मनुष्य अपनी कुण्डली की एक-एक गणना स्वयं कर सके।
  </p>
</div>'''
    pages.append(make_page(2, "मंगलाचरण • Invocation", "प्रस्तावना एवं दिव्य काल-विज्ञान", p2))

    # Page 3: Chapter 1 - Ephemeris & Julian Day
    p3 = f'''<div>
  <div class="story-box" style="background:rgba(2, 132, 199, 0.08); border-left:4px solid #0284c7; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#0369a1;">📖 रोचक कथा: ब्रह्मांड की कभी न रुकने वाली घड़ी</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      मानव कैलेंडरों में लीप वर्ष आते हैं, कभी महीना 28 का तो कभी 31 का होता है। परंतु खगोलविदों ने 4713 ईसा पूर्व से एक निरंतर गिनती शुरू की जिसे 'जूलियन डे' (Julian Day) कहा जाता है। आपके जन्म के समय इस महा-घड़ी पर ठीक 24,49,653 दिन बीत चुके थे!
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१.१ यूनिवर्सल टाइम (UT) एवं जूलियन डे समीकरण</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    भारतीय मानक समय (IST) ग्रीनविच से 5 घंटे 30 मिनट आगे है। अतः खगोलीय गणना के लिए जन्म समय में से 5.5 घंटे घटाकर अंतर्राष्ट्रीय समय (UT) निकाला जाता है:
  </p>
  <div style="background:#090d16; color:#38bdf8; padding:0.6rem; border-radius:6px; font-family:monospace; font-size:0.85rem; margin-bottom:0.6rem;">
    UT = 03:45 AM (28 Oct 1994) - 5.5 Hours = 22:15 UT (27 Oct 1994)<br>
    दशमलव घंटे = 22 + (15 ÷ 60) = 22.25 Hours UT<br>
    Julian Day (JD) = 2449653.427083
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१.२ अयनांश (Lahiri Ayanamsha) का महत्व</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6;">
    पृथ्वी के अक्ष का अपनी धुरी पर लट्टू की तरह धीरे-धीरे घूमना (Precession) अयनांश कहलाता है। यह प्रति 72 वर्ष में लगभग 1° खिसक जाता है। 28 अक्टूबर 1994 को लाहिरी अयनांश <strong>23° 47' 11.8''</strong> था। पश्चिमी सायन राशि में से इसे घटाने पर ही सच्ची वैदिक निरयण स्थिति प्राप्त होती है।
  </p>
</div>'''
    pages.append(make_page(3, "अध्याय १ • खगोल गणित", "जूलियन डे एवं अयनांश समीकरण", p3))

    # Page 4: Ascendant Math & 12 Houses
    p4 = f'''<div>
  <div class="story-box" style="background:rgba(5, 150, 105, 0.08); border-left:4px solid #059669; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#065f46;">📖 रोचक कथा: पूर्व क्षितिज की दिव्य खिड़की (लग्न)</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      जैसे एक चलती हुई रेलगाड़ी की खिड़की से बाहर देखने पर दृश्य लगातार बदलते रहते हैं, वैसे ही घूमती हुई पृथ्वी के पूर्व क्षितिज पर 24 घंटे में सभी 12 राशियां बारी-बारी से उदय होती हैं। जिस क्षण आपने जन्म लिया, उस खिड़की से कौन सी राशि झांक रही थी—वही आपका लग्न है!
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१.३ लग्न (Ascendant) का सटीक गणित</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    स्थान के अक्षांश (24.05° N) और देशांतर (83.65° E) पर स्थानीय नाक्षत्र समय (LST) की गणना की जाती है:
  </p>
  <div style="background:#090d16; color:#34d399; padding:0.6rem; border-radius:6px; font-family:monospace; font-size:0.84rem; margin-bottom:0.6rem;">
    LST = GMST + (देशांतर ÷ 15) = 04h 37m 42s<br>
    RAMC = 69° 25' 30''<br>
    लग्न स्पष्ट = कन्या (Virgo) 09° 21' 10'' • उत्तराफाल्गुनी चतुर्थ चरण
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१.४ 12 भावों का सम्पूर्ण-राशि (Whole-Sign) विभाजन</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6;">
    वैदिक ज्योतिष में महर्षि पराशर के अनुसार लग्न जिस राशि में पड़ता है, वह संपूर्ण 30° की राशि प्रथम भाव (तनु भाव) बन जाती है। अगली राशि द्वितीय भाव (धन) और इसी क्रम से 12 भाव निर्धारित होते हैं।
  </p>
  {get_diamond_chart_svg()}
</div>'''
    pages.append(make_page(4, "अध्याय १ • लग्न गणित", "लग्न उदय एवं 12 भाव विभाजन", p4))

    # Page 5: Speeds, Retrogression & Combustion
    p5 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१.५ वक्री गति (Retrogression) का यथार्थ विज्ञान</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    वास्तव में कोई ग्रह कभी उल्टा नहीं चलता। जब पृथ्वी किसी बाहरी ग्रह (मंगल, गुरु, शनि) के पास से तीव्र गति से आगे निकलती है, तो वह ग्रह पीछे जाता हुआ प्रतीत होता है। इसे 'वक्री' (Retrograde) कहते हैं। वक्री ग्रह में चेष्टा बल अत्यधिक होता है—वह 3 गुना अधिक तीव्रता से परिणाम देता है!
  </p>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-top:0.8rem; margin-bottom:0.3rem;">१.६ ग्रहों का अस्त होना (Combustion Orbs)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    जब कोई ग्रह सूर्य के अत्यंत निकट आ जाता है, तो सूर्य के प्रचंड तेज से वह आकाश में अदृश्य हो जाता है। इसे 'अस्त' (Combust) कहते हैं:
  </p>
  <div class="table-responsive" style="margin-bottom:0.8rem;">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>ग्रह</th>
          <th>सामान्य अस्त परिधि</th>
          <th>वक्री होने पर परिधि</th>
          <th>फल प्रभाव</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>चंद्रमा</strong></td><td>12°</td><td>—</td><td>अमावस्या दोष, मानसिक दुर्बलता</td></tr>
        <tr><td><strong>मंगल</strong></td><td>17°</td><td>17°</td><td>पराक्रम में रुकावट, क्रोध की अधिकता</td></tr>
        <tr><td><strong>बुध</strong></td><td>14°</td><td>12°</td><td>बुधादित्य योग में अस्त होने पर भी विद्या लाभ</td></tr>
        <tr><td><strong>बृहस्पति</strong></td><td>11°</td><td>11°</td><td>धर्म व संतान सुख में विलंब</td></tr>
        <tr><td><strong>शुक्र</strong></td><td>10°</td><td>08°</td><td>विवाह व भौतिक सुखों में परीक्षण</td></tr>
        <tr><td><strong>शनि</strong></td><td>15°</td><td>15°</td><td>कर्म क्षेत्र में अत्यधिक विलंब व श्रम</td></tr>
      </tbody>
    </table>
  </div>
  <p style="font-size:0.84rem; color:#64748b; line-height:1.5;">
    <strong>सूक्ष्म रहस्य:</strong> बुध सूर्य के निकट रहने के कारण अस्त होने पर भी अपना विशेष शुभ प्रभाव नहीं खोता, जबकि गुरु या शुक्र का अस्त होना शुभ कार्यों (विवाह आदि) में निषेध माना जाता है।
  </p>
</div>'''
    pages.append(make_page(5, "अध्याय १ • ग्रह गतिकी", "वक्री गति एवं अस्त परिधि गणित", p5))

    # Page 6: Panchadha Maitri & Avasthas
    p6 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१.७ पंचधा मैत्री: 5-स्तरीय संबंध समीकरण</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    दो ग्रहों का अंतिम संबंध उनके जन्मजात (नैसर्गिक) स्वभाव और उस समय की तात्कालिक स्थिति (दूरी) को जोड़कर तय होता है:
  </p>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.83rem; margin-bottom:0.6rem; color:#1e293b;">
    <strong>तात्कालिक मित्रता नियम:</strong> जो ग्रह किसी ग्रह से 2, 3, 4, 10, 11, 12वें भाव में बैठे हों, वे तात्कालिक मित्र होते हैं। शेष भावों (1, 5, 6, 7, 8, 9) वाले तात्कालिक शत्रु होते हैं।<br>
    • मित्र + मित्र = <strong>अधिमित्र (परम मित्र, +2)</strong><br>
    • मित्र + सम = <strong>मित्र (+1)</strong><br>
    • शत्रु + शत्रु = <strong>अधिशत्रु (परम शत्रु, -2)</strong>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१.८ ग्रहों की अवस्थाएं (Avasthas)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    राशि में अंशों के आधार पर ग्रह की आयु एवं फल देने की क्षमता निर्धारित होती है:
  </p>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>अवस्था</th>
          <th>विषम राशि में अंश</th>
          <th>सम राशि में अंश</th>
          <th>फल सामर्थ्य</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>बाल्यावस्था</strong></td><td>0° से 6°</td><td>24° से 30°</td><td>25% फल (शिशुवत)</td></tr>
        <tr><td><strong>कुमारावस्था</strong></td><td>6° से 12°</td><td>18° से 24°</td><td>50% फल (किशोरवत)</td></tr>
        <tr><td><strong>युवावस्था</strong></td><td>12° से 18°</td><td>12° से 18°</td><td>100% पूर्ण फल (युवा)</td></tr>
        <tr><td><strong>वृद्धावस्था</strong></td><td>18° से 24°</td><td>6° से 12°</td><td>अति न्यून फल</td></tr>
        <tr><td><strong>मृतावस्था</strong></td><td>24° से 30°</td><td>0° से 6°</td><td>0% नगण्य फल</td></tr>
      </tbody>
    </table>
  </div>
</div>'''
    pages.append(make_page(6, "अध्याय १ • ग्रह अवस्थाएं", "पंचधा मैत्री एवं बाल्यादि अवस्था", p6))

    # Page 7: Chapter 2 - Panchanga
    p7 = f'''<div>
  <div class="story-box" style="background:rgba(234, 88, 12, 0.08); border-left:4px solid #ea580c; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#c2410c;">📖 रोचक कथा: काल-पुरुष के पांच पावन हाथ</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      वैदिक काल-गणना केवल कैलेंडर देखने का नाम नहीं है। पंचांग के पांच अंग जल, अग्नि, वायु, आकाश और पृथ्वी के 5 तत्वों का प्रतिनिधित्व करते हैं। जब ये पांचों अंग अनुकूल होते हैं, तो साधारण प्रयास भी महान सफलता बन जाता है!
    </p>
  </div>
  {get_panchanga_svg()}
  <h4 style="color:#0f766e; font-size:0.95rem; margin-top:0.6rem; margin-bottom:0.3rem;">२.१ पंचांग के पांचों अंगों का गणितीय सूत्र</h4>
  <ul style="font-size:0.85rem; color:#334155; line-height:1.65; padding-left:1.2rem;">
    <li><strong>तिथि = (चंद्रमा - सूर्य) ÷ 12°:</strong> प्रति 12° के अंतर पर 1 तिथि बनती है। 1 से 15 शुक्ल पक्ष, 16 से 30 कृष्ण पक्ष।</li>
    <li><strong>वार = सूर्योदय कालीन दिवस:</strong> रविवार से शनिवार तक 7 ग्रहों के चक्र से स्वास्थ्य व जीवनी शक्ति का निर्णय।</li>
    <li><strong>नक्षत्र = चंद्रमा का भोगांश ÷ 13°20':</strong> संपूर्ण आकाश 27 नक्षत्रों में बंटा है। चित्त की मूल प्रवृत्ति यहीं से निर्धारित होती है।</li>
    <li><strong>योग = (सूर्य + चंद्रमा) ÷ 13°20':</strong> दोनों का योग करके 27 योग बनते हैं (विष्कंभ से वैधृति तक)।</li>
    <li><strong>करण = आधी तिथि (6° का भोग):</strong> एक तिथि में 2 करण होते हैं (कुल 60 करण, 7 चर + 4 स्थिर)।</li>
  </ul>
</div>'''
    pages.append(make_page(7, "अध्याय २ • पंचांग रहस्य", "काल के पांच अंग एवं उनका गणित", p7))

    # Page 8: Rahu Kalam & Upagrahas
    p8 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">२.२ राहुकाल एवं यमगण्ड गणितीय विभाजन</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    सूर्योदय से सूर्यास्त तक के संपूर्ण दिनमान को 8 बराबर भागों में बांटा जाता है। प्रत्येक भाग लगभग 1.5 घंटे का होता है:
  </p>
  <div class="table-responsive" style="margin-bottom:0.8rem;">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>दिन</th>
          <th>राहुकाल भाग (8 में से)</th>
          <th>यमगण्ड भाग</th>
          <th>विशेष सावधानी</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>सोमवार</strong></td><td>दूसरा भाग (07:30 - 09:00)</td><td>चौथा भाग (10:30 - 12:00)</td><td>यात्रा व धन आरंभ वर्जित</td></tr>
        <tr><td><strong>मंगलवार</strong></td><td>सातवां भाग (15:00 - 16:30)</td><td>दूसरा भाग (09:00 - 10:30)</td><td>ऋण मुक्ति हेतु श्रेष्ठ</td></tr>
        <tr><td><strong>बुधवार</strong></td><td>पांचवां भाग (12:00 - 13:30)</td><td>पहला भाग (07:30 - 09:00)</td><td>नया अनुबंध न करें</td></tr>
        <tr><td><strong>गुरुवार</strong></td><td>छठा भाग (13:30 - 15:00)</td><td>तीसरा भाग (06:00 - 07:30)</td><td>विद्या व बैंक कार्य टालें</td></tr>
        <tr><td><strong>शुक्रवार</strong></td><td>चौथा भाग (10:30 - 12:00)</td><td>छठा भाग (15:00 - 16:30)</td><td>आभूषण क्रय न करें</td></tr>
        <tr><td><strong>शनिवार</strong></td><td>तीसरा भाग (09:00 - 10:30)</td><td>पांचवां भाग (13:30 - 15:00)</td><td>भूमि व वाहन सौदा वर्जित</td></tr>
        <tr><td><strong>रविवार</strong></td><td>आठवां भाग (16:30 - 18:00)</td><td>सातवां भाग (12:00 - 13:30)</td><td>सरकारी कार्य आरंभ न करें</td></tr>
      </tbody>
    </table>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">२.३ गुलिक एवं मांदी (शनि के उपग्रह)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6;">
    शनि के भाग के आरंभ को 'गुलिक' और मध्य को 'मांदी' कहते हैं। कुण्डली में गुलिक जिस भाव में बैठता है, वहां अचानक बाधा या रोग उत्पन्न करता है। परंतु यदि गुलिक 3, 6, 11 भाव में हो तो जातक को अदम्य पराक्रम और शत्रुओं पर विजय दिलाता है!
  </p>
</div>'''
    pages.append(make_page(8, "अध्याय २ • काल मुहूर्त", "राहुकाल, यमगण्ड एवं 11 उपग्रह", p8))

    # Page 9: Chapter 3 - Vimshottari Dasha
    p9 = f'''<div>
  <div class="story-box" style="background:rgba(124, 58, 237, 0.08); border-left:4px solid #7c3aed; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#6d28d9;">📖 रोचक कथा: 9 ग्रहों की 120-वर्षीय रिले दौड़</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      मनुष्य की पूर्ण आयु 120 वर्ष मानी गई है। जन्म के समय चंद्रमा जिस नक्षत्र में था, वही ग्रह आपके जीवन की पहली महादशा का स्वामी बनता है। यह केवल एक कैलेंडर नहीं, बल्कि आपके कर्मों के पकने का अचूक समय-चक्र है!
    </p>
  </div>
  {get_dasha_tree_svg()}
  <h4 style="color:#0f766e; font-size:0.95rem; margin-top:0.6rem; margin-bottom:0.3rem;">३.१ विंशोत्तरी दशा आवंटन तालिका</h4>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>ग्रह</th>
          <th>आवंटित वर्ष</th>
          <th>शासित नक्षत्र (त्रिकोण)</th>
          <th>जीवन प्रभाव</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>केतु</strong></td><td>7 वर्ष</td><td>अश्विनी (0), मघा (9), मूल (18)</td><td>वैराग्य, शोध, आध्यात्मिक जागरण</td></tr>
        <tr><td><strong>शुक्र</strong></td><td>20 वर्ष</td><td>भरणी (1), पू.फा. (10), पूर्वाषाढ़ा (19)</td><td>विवाह, कला, वैभव, ऐश्वर्य</td></tr>
        <tr><td><strong>सूर्य</strong></td><td>6 वर्ष</td><td>कृत्तिका (2), उ.फा. (11), उत्तराषाढ़ा (20)</td><td>प्रतिष्ठा, पदोन्नति, सत्ता लाभ</td></tr>
        <tr><td><strong>चंद्र</strong></td><td>10 वर्ष</td><td>रोहिणी (3), हस्त (12), श्रवण (21)</td><td>मानसिक शांति, जनसंपर्क, माता</td></tr>
        <tr><td><strong>मंगल</strong></td><td>7 वर्ष</td><td>मृगशिरा (4), चित्रा (13), धनिष्ठा (22)</td><td>भूमि, पराक्रम, तकनीकी सफलता</td></tr>
        <tr><td><strong>राहु</strong></td><td>18 वर्ष</td><td>आर्द्रा (5), स्वाति (14), शतभिषा (23)</td><td>विदेशी यात्रा, अचानक उत्थान/पतन</td></tr>
        <tr><td><strong>गुरु</strong></td><td>16 वर्ष</td><td>पुनर्वसु (6), विशाखा (15), पू.भा. (24)</td><td>ज्ञान, संतान, धन, धर्म वृद्धि</td></tr>
        <tr><td><strong>शनि</strong></td><td>19 वर्ष</td><td>पुष्य (7), अनुराधा (16), उ.भा. (25)</td><td>कठोर अनुशासन, स्थायी साम्राज्य</td></tr>
        <tr><td><strong>बुध</strong></td><td>17 वर्ष</td><td>आश्लेषा (8), ज्येष्ठा (17), रेवती (26)</td><td>व्यापार, लेखन, गणित, वाकपटुता</td></tr>
      </tbody>
    </table>
  </div>
</div>'''
    pages.append(make_page(9, "अध्याय ३ • विंशोत्तरी दशा", "120-वर्षीय जीवन चक्र एवं आवंटन", p9))

    # Page 10: Dasha Balance Calculation
    p10 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">३.२ जन्म समय दशा भोग्य शेष गणित (Balance of Dasha)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    जन्म समय नक्षत्र का जितना भाग अभी चलना बाकी है, उसी अनुपात में पहली महादशा का समय मिलता है:
  </p>
  <div style="background:#090d16; color:#fde047; padding:0.7rem; border-radius:6px; font-family:monospace; font-size:0.83rem; margin-bottom:0.7rem; line-height:1.6;">
    उदाहरण: आशुतोष (28 Oct 1994, 03:45 AM)<br>
    चंद्रमा = कर्क राशि 13° 10' 17'' (पुष्य नक्षत्र, स्वामी शनि = 19 वर्ष)<br>
    पुष्य नक्षत्र विस्तार = 93° 20' से 106° 40' (कुल 13° 20' = 800')<br>
    बीता हुआ भाग = 103° 10' 17'' - 93° 20' = 09° 50' 17'' (590.28')<br>
    शेष बचा भाग = 800' - 590.28' = 209.72' (26.215%)<br>
    <strong>शनि महादशा भोग्य शेष = 19 × 0.26215 = 4.9808 वर्ष</strong><br>
    अर्थात: 4 वर्ष, 11 माह, 23 दिन शनि महादशा जन्म के बाद रही।
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">३.३ अंतर्दशा एवं प्रत्यंतर्दशा निकालने का नियम</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    किसी भी महादशा में किसी ग्रह की अंतर्दशा निकालने के लिए दोनों के वर्षों का गुणा करके 120 से भाग दें:
  </p>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.84rem; color:#1e293b;">
    <strong>सूत्र:</strong> अंतर्दशा (वर्ष) = (महादशा वर्ष × अंतर्दशा वर्ष) ÷ 120<br>
    <em>उदाहरण:</em> शनि में बुध की अंतर्दशा = (19 × 17) ÷ 120 = 323 ÷ 120 = <strong>2.69 वर्ष (2 वर्ष, 8 माह, 9 दिन)</strong>
  </div>
</div>'''
    pages.append(make_page(10, "अध्याय ३ • दशा गणित", "जन्म समय दशा भोग्य शेष एवं अंतर्दशा", p10))

    # Page 11: Chapter 4 - Parashari Yogas
    p11 = '''<div>
  <div class="story-box" style="background:rgba(5, 150, 105, 0.08); border-left:4px solid #059669; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#065f46;">📖 रोचक कथा: महल के 4 स्तंभ और 3 खजाने</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      कुण्डली के केंद्र भाव (1, 4, 7, 10) भगवान विष्णु के स्तंभ हैं जो जीवन को स्थिरता देते हैं। त्रिकोण भाव (1, 5, 9) माता लक्ष्मी के खजाने हैं जो भाग्य और पुण्य लाते हैं। जब केंद्र का स्वामी त्रिकोण के स्वामी से हाथ मिलाता है, तो राजयोग का जन्म होता है!
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">४.१ पंच महापुरुष योग (The 5 Royal Yoga Formulations)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    जब 5 तारा ग्रह (मंगल, बुध, गुरु, शुक्र, शनि) केंद्र (1, 4, 7, 10) में स्वराशि या उच्च राशि में हों:
  </p>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>योग नाम</th>
          <th>कारक ग्रह</th>
          <th>राशियां (स्व/उच्च)</th>
          <th>व्यक्तित्व एवं फल</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>रुचक योग</strong></td><td>मंगल</td><td>मेष, वृश्चिक, मकर</td><td>सेनापति, भूमिपति, पराक्रमी, निडर</td></tr>
        <tr><td><strong>भद्र योग</strong></td><td>बुध</td><td>मिथुन, कन्या</td><td>गणितज्ञ, कुशाग्र बुद्धि, वक्ता, सफल व्यापारी</td></tr>
        <tr><td><strong>हंस योग</strong></td><td>बृहस्पति</td><td>धनु, मीन, कर्क</td><td>धर्मात्मा, न्यायाधीश, समाज में पूज्य</td></tr>
        <tr><td><strong>मालव्य योग</strong></td><td>शुक्र</td><td>वृषभ, तुला, मीन</td><td>कला, ऐश्वर्य, सुंदर जीवनसाथी, वाहन सुख</td></tr>
        <tr><td><strong>शश योग</strong></td><td>शनि</td><td>मकर, कुम्भ, तुला</td><td>जनता का नेता, दीर्घायु, उद्योगपति, कर्मठ</td></tr>
      </tbody>
    </table>
  </div>
  <p style="font-size:0.84rem; color:#0f766e; margin-top:0.5rem; font-weight:600;">
    जातक कुण्डली में लग्न (प्रथम भाव) में बुध अपनी उच्च राशि कन्या में स्थित होकर <strong>भद्र महापुरुष योग</strong> का निर्माण कर रहा है!
  </p>
</div>'''
    pages.append(make_page(11, "अध्याय ४ • पराशरी योग", "पंच महापुरुष योग एवं केंद्र-त्रिकोण राजयोग", p11))

    # Page 12: Raja Yogas & Dhana Yogas
    p12 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">४.२ केंद्र-त्रिकोण राजयोग संसूचन मैट्रिक्स</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    केंद्र (1, 4, 7, 10) और त्रिकोण (1, 5, 9) के स्वामियों के मध्य 4 प्रकार के संबंध राजयोग बनाते हैं:
  </p>
  <ul style="font-size:0.84rem; color:#334155; line-height:1.6; padding-left:1.2rem; margin-bottom:0.6rem;">
    <li><strong>क्षेत्र परिवर्तन (Parivartana):</strong> केंद्रपति त्रिकोण में और त्रिकोणपति केंद्र में बैठे हों (सर्वश्रेष्ठ)।</li>
    <li><strong>युति संबंध (Conjunction):</strong> दोनों एक ही भाव में साथ बैठे हों।</li>
    <li><strong>दृष्टि संबंध (Mutual Aspect):</strong> दोनों आमने-सामने बैठकर एक-दूसरे को देख रहे हों।</li>
    <li><strong>एकतरफा दृष्टि:</strong> त्रिकोणपति केंद्रपति को या केंद्रपति त्रिकोणपति को देख रहा हो।</li>
  </ul>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">४.३ धन योग (Dhana Yogas - Wealth Multipliers)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    धन का संबंध लग्न (स्वयं), द्वितीय (कोष/बैंक बैलेंस), पंचम (बुद्धि/सट्टा), नवम (भाग्य) और एकादश (लाभ) से होता है:
  </p>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.83rem; line-height:1.6; color:#1e293b;">
    • <strong>लग्नपति + द्वितीयेश / एकादशेश:</strong> जातक अपने स्वयं के बाहुबल से अकूत संपत्ति बनाता है।<br>
    • <strong>पंचमेश + नवमेश (महालक्ष्मी योग):</strong> ईश्वरीय कृपा से अचानक प्रचुर धन लाभ और बौद्धिक संपदा।<br>
    • <strong>द्वितीयेश + एकादशेश (कुबेर योग):</strong> धन संचय और आय का अटूट प्रवाह।
  </div>
</div>'''
    pages.append(make_page(12, "अध्याय ४ • धन योग", "राजयोग संसूचन एवं धन संचय सूत्र", p12))

    # Page 13: Neechabhanga & Vipareeta
    p13 = '''<div>
  <div class="story-box" style="background:rgba(220, 38, 38, 0.08); border-left:4px solid #dc2626; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#991b1b;">📖 रोचक कथा: फटे कपड़ों में छिपा सम्राट (नीचभंग)</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      यदि कोई राजा भेष बदलकर फटे कपड़ों में घूम रहा हो, लेकिन उसका सबसे वफादार सेनापति उसके पास आकर झुक जाए, तो राजा की शक्ति नष्ट नहीं होती—वह दोगुने पराक्रम से प्रकट होती है! यही नीचभंग राजयोग है।
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">४.४ नीचभंग राजयोग के ४ शास्त्रीय नियम</h4>
  <ul style="font-size:0.84rem; color:#334155; line-height:1.6; padding-left:1.2rem; margin-bottom:0.6rem;">
    <li><strong>नियम १:</strong> नीच ग्रह जिस राशि में बैठा है, उसका स्वामी लग्न या चंद्रमा से केंद्र (1, 4, 7, 10) में हो।</li>
    <li><strong>नियम २:</strong> उस नीच राशि में जो ग्रह उच्च होता है, वह लग्न या चंद्रमा से केंद्र में हो।</li>
    <li><strong>नियम ३:</strong> नीच ग्रह को उसकी राशि का स्वामी सीधे पूर्ण दृष्टि से देख रहा हो।</li>
    <li><strong>नियम ४:</strong> नीच ग्रह नवांश कुण्डली (D9) में अपनी उच्च राशि में बैठा हो।</li>
  </ul>
  <div style="background:#090d16; color:#34d399; padding:0.6rem; border-radius:6px; font-family:monospace; font-size:0.83rem; margin-bottom:0.6rem;">
    जातक कुण्डली में सूर्य तुला राशि (नीच) में है।<br>
    तुला का स्वामी शुक्र चंद्रमा से चतुर्थ (केंद्र) में स्थित है।<br>
    तुला में उच्च होने वाला शनि लग्न से षष्ठ और चंद्रमा से अष्टम में वक्री है।<br>
    <strong>अतः सूर्य का पूर्ण नीचभंग राजयोग सिद्ध होता है!</strong>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">४.५ विपरीत राजयोग (हर्ष, सरल, विमल)</h4>
  <p style="font-size:0.85rem; color:#334155; line-height:1.6;">
    जब त्रिक भावों (6, 8, 12) के स्वामी आपस में ही 6, 8, 12 में बैठ जाएं, तो दूसरों के पतन से जातक का उत्थान होता है।
  </p>
</div>'''
    pages.append(make_page(13, "अध्याय ४ • नीचभंग", "नीचभंग राजयोग एवं विपरीत राजयोग", p13))

    # Page 14: Chapter 5 - Ashtakavarga
    p14 = f'''<div>
  <div class="story-box" style="background:rgba(5, 150, 105, 0.08); border-left:4px solid #059669; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#065f46;">📖 रोचक कथा: गांव के 8 बुजुर्गों का गुप्त मतदान</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      महर्षि पराशर ने कलियुग के अल्पायु मनुष्यों के लिए अष्टकवर्ग की रचना की। 8 बुजुर्ग मिलकर 337 वोट (बिंदु) 12 भावों में बांटते हैं। जिस भाव को 28 या अधिक बिंदु मिले, वह जीवन का सबसे मजबूत किला बन जाता है!
    </p>
  </div>
  {get_ashtakavarga_svg()}
  <h4 style="color:#0f766e; font-size:0.95rem; margin-top:0.6rem; margin-bottom:0.3rem;">५.१ सर्वाष्टकवर्ग (SAV) 337 बिंदु तालिका</h4>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>ग्रह</th>
          <th>कुल बिंदु</th>
          <th>प्रति भाव औसत</th>
          <th>जीवन में फल भूमिका</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>सूर्य</strong></td><td>48</td><td>4.0</td><td>आत्मविश्वास, स्वास्थ्य, सरकारी प्रतिष्ठा</td></tr>
        <tr><td><strong>चंद्रमा</strong></td><td>49</td><td>4.08</td><td>मानसिक प्रसन्नता, जनसमर्थन, द्रव्य लाभ</td></tr>
        <tr><td><strong>मंगल</strong></td><td>39</td><td>3.25</td><td>शौर्य, भूमि क्रय-विक्रय, शत्रु दमन</td></tr>
        <tr><td><strong>बुध</strong></td><td>54</td><td>4.5</td><td>व्यापारिक बुद्धि, बौद्धिक यश, गणितीय सफलता</td></tr>
        <tr><td><strong>बृहस्पति</strong></td><td>56</td><td>4.67</td><td>संतान सुख, धन वृद्धि, ज्ञान, परामर्श</td></tr>
        <tr><td><strong>शुक्र</strong></td><td>52</td><td>4.33</td><td>भौतिक विलास, वाहन सुख, दांपत्य शांति</td></tr>
        <tr><td><strong>शनि</strong></td><td>39</td><td>3.25</td><td>आयु, दीर्घकालिक निर्माण, धैर्य, उद्योग</td></tr>
        <tr style="font-weight:700; background:#f0fdf4;"><td><strong>कुल योग</strong></td><td><strong>337</strong></td><td><strong>28.08</strong></td><td><strong>337 बिंदुओं का सनातन वितरण</strong></td></tr>
      </tbody>
    </table>
  </div>
</div>'''
    pages.append(make_page(14, "अध्याय ५ • अष्टकवर्ग", "337 बिंदु रहस्य एवं 28 बिंदु स्वर्ण-नियम", p14))

    # Page 15: Reductions (Shodhana)
    p15 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">५.२ त्रिकोण शोधन (Trikona Shodhana - Triplicity Reduction)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    प्रकृति के चार तत्वों (अग्नि, पृथ्वी, वायु, जल) के त्रिकोणों में बिंदुओं का शोधन किया जाता है:
  </p>
  <ul style="font-size:0.84rem; color:#334155; line-height:1.6; padding-left:1.2rem; margin-bottom:0.6rem;">
    <li><strong>अग्नि त्रिकोण:</strong> मेष (1), सिंह (5), धनु (9)</li>
    <li><strong>पृथ्वी त्रिकोण:</strong> वृषभ (2), कन्या (6), मकर (10)</li>
    <li><strong>वायु त्रिकोण:</strong> मिथुन (3), तुला (7), कुम्भ (11)</li>
    <li><strong>जल त्रिकोण:</strong> कर्क (4), वृश्चिक (8), मीन (12)</li>
  </ul>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.83rem; line-height:1.6; color:#1e293b; margin-bottom:0.6rem;">
    <strong>शोधन नियम:</strong> तीनों राशियों में जो सबसे न्यूनतम बिंदु हो, उसे तीनों में से घटा दिया जाता है।<br>
    <em>उदाहरण:</em> यदि मेष में 4, सिंह में 6, धनु में 2 बिंदु हों, तो न्यूनतम = 2।<br>
    शोधित मान: मेष = 4 - 2 = <strong>2</strong>, सिंह = 6 - 2 = <strong>4</strong>, धनु = 2 - 2 = <strong>0</strong>।
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">५.३ एकाधिपत्य शोधन (Dual Lordship Balancing)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6;">
    एक ही ग्रह के अधीन दो राशियों (जैसे मंगल की मेष-वृश्चिक, शुक्र की वृषभ-तुला) के बिंदुओं का संतुलन किया जाता है, जब उन राशियों में कोई ग्रह न बैठा हो। इससे कुण्डली की शुद्ध ऊर्जा शक्ति (Shodhya Pinda) निकलती है।
  </p>
</div>'''
    pages.append(make_page(15, "अध्याय ५ • शोधन गणित", "त्रिकोण एवं एकाधिपत्य शोधन सूत्र", p15))

    # Page 16: Kakshya System
    p16 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">५.४ कक्षी प्रणाली: 3° 45' का सूक्ष्म गोचर टाइमर</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    प्रत्येक 30° की राशि को 8 बराबर भागों में काटा जाता है, जिसे 'कक्षी' (Kakshya) कहते हैं। प्रत्येक कक्षी <strong>3° 45' (225 कला)</strong> की होती है:
  </p>
  <div class="table-responsive" style="margin-bottom:0.8rem;">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>कक्षी संख्या</th>
          <th>अंश विस्तार</th>
          <th>कक्षी स्वामी</th>
          <th>फल देने की शर्त</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>१म कक्षी</td><td>00° 00' से 03° 45'</td><td>शनि (Saturn)</td><td>यदि शनि का बिंदु उस राशि में हो</td></tr>
        <tr><td>२य कक्षी</td><td>03° 45' से 07° 30'</td><td>गुरु (Jupiter)</td><td>यदि गुरु का बिंदु उस राशि में हो</td></tr>
        <tr><td>३य कक्षी</td><td>07° 30' से 11° 15'</td><td>मंगल (Mars)</td><td>यदि मंगल का बिंदु उस राशि में हो</td></tr>
        <tr><td>४थ कक्षी</td><td>11° 15' से 15° 00'</td><td>सूर्य (Sun)</td><td>यदि सूर्य का बिंदु उस राशि में हो</td></tr>
        <tr><td>५म कक्षी</td><td>15° 00' से 18° 45'</td><td>शुक्र (Venus)</td><td>यदि शुक्र का बिंदु उस राशि में हो</td></tr>
        <tr><td>६ठ कक्षी</td><td>18° 45' से 22° 30'</td><td>बुध (Mercury)</td><td>यदि बुध का बिंदु उस राशि में हो</td></tr>
        <tr><td>७म कक्षी</td><td>22° 30' से 26° 15'</td><td>चंद्र (Moon)</td><td>यदि चंद्रमा का बिंदु उस राशि में हो</td></tr>
        <tr><td>८म कक्षी</td><td>26° 15' से 30° 00'</td><td>लग्न (Lagna)</td><td>यदि लग्न का बिंदु उस राशि में हो</td></tr>
      </tbody>
    </table>
  </div>
  <p style="font-size:0.85rem; color:#334155; line-height:1.6;">
    <strong>अचूक भविष्यवाणी रहस्य:</strong> कोई भी ग्रह गोचर में शुभ फल तभी देता है जब वह उस विशेष कक्षी में चल रहा हो जहाँ उसने अपना शुभ बिंदु दिया था! जब ग्रह बिंदु-रहित कक्षी में जाता है, तो शुभ गोचर में भी काम अटक जाते हैं।
  </p>
</div>'''
    pages.append(make_page(16, "अध्याय ५ • कक्षी गोचर", "कक्षी प्रणाली एवं सटीक घटना समय", p16))

    # Page 17: Chapter 6 - Varga Suite (D1 to D60)
    p17 = '''<div>
  <div class="story-box" style="background:rgba(2, 132, 199, 0.08); border-left:4px solid #0284c7; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#0369a1;">📖 रोचक कथा: ब्रह्मांडीय सूक्ष्मदर्शी (The Cosmic Microscope)</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      जन्म कुण्डली (D1) पूरे वृक्ष की तस्वीर है। लेकिन यदि आपको देखना हो कि फल मीठा होगा या खट्टा, तो आपको D7 का सूक्ष्मदर्शी लगाना होगा। यदि लकड़ी की मजबूती देखनी हो तो D4, और वृक्ष के मूल बीज का डीएनए देखना हो तो D60!
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">६.१ षोडशवर्ग (16 Divisional Charts) का पूर्ण मानचित्र</h4>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>वर्ग चार्ट</th>
          <th>विभाजन</th>
          <th>एक भाग का अंश</th>
          <th>जांचने का मुख्य विषय</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>D1 राशि</strong></td><td>1</td><td>30° 00'</td><td>स्थूल शरीर, सामान्य जीवन ढांचा</td></tr>
        <tr><td><strong>D2 होरा</strong></td><td>2</td><td>15° 00'</td><td>धन, चल संपत्ति, वित्तीय स्थिरता</td></tr>
        <tr><td><strong>D3 द्रेष्काण</strong></td><td>3</td><td>10° 00'</td><td>भाई-बहन, साहस, पराक्रम, ऊर्जा</td></tr>
        <tr><td><strong>D4 चतुर्थांश</strong></td><td>4</td><td>07° 30'</td><td>अचल संपत्ति, गृह, भूमि, भाग्य</td></tr>
        <tr><td><strong>D7 सप्तमांश</strong></td><td>7</td><td>04° 17' 08''</td><td>संतान सुख, वंश परंपरा, पौत्र-पौत्री</td></tr>
        <tr><td><strong>D9 नवांश</strong></td><td>9</td><td>03° 20'</td><td>दांपत्य जीवन, धर्म, आत्मा का बल</td></tr>
        <tr><td><strong>D10 दशमांश</strong></td><td>10</td><td>03° 00'</td><td>करियर, पद, प्रतिष्ठा, आजीविका</td></tr>
        <tr><td><strong>D12 द्वादशांश</strong></td><td>12</td><td>02° 30'</td><td>माता-पिता, पूर्वज, पैतृक संस्कार</td></tr>
        <tr><td><strong>D16 षोडशांश</strong></td><td>16</td><td>01° 52' 30''</td><td>वाहन सुख, मानसिक सुख-शांति</td></tr>
        <tr><td><strong>D20 विंशांश</strong></td><td>20</td><td>01° 30'</td><td>आध्यात्मिक उपासना, मंत्र सिद्धि, भक्ति</td></tr>
        <tr><td><strong>D24 चतुर्विंशांश</strong></td><td>24</td><td>01° 15'</td><td>उच्च विद्या, अनुसंधान, बौद्धिक सिद्धि</td></tr>
        <tr><td><strong>D27 भाम्श</strong></td><td>27</td><td>01° 06' 40''</td><td>शारीरिक सामर्थ्य, गुप्त दुर्बलताएं</td></tr>
        <tr><td><strong>D30 त्रिंशांश</strong></td><td>30</td><td>असम अंश</td><td>अरिष्ट, दुर्घटनाएं, रोग, पाप कर्म</td></tr>
        <tr><td><strong>D40 खवेदांश</strong></td><td>40</td><td>00° 45'</td><td>मातृकुल के पूर्वज, शुभ-अशुभ संस्कार</td></tr>
        <tr><td><strong>D45 अक्षवेदांश</strong></td><td>45</td><td>00° 40'</td><td>पितृकुल के पूर्वज, चारित्रिक शुद्धि</td></tr>
        <tr><td><strong>D60 षष्ट्यंश</strong></td><td>60</td><td>00° 30'</td><td>पूर्वजन्म के संचित कर्म (परम आधार)</td></tr>
      </tbody>
    </table>
  </div>
</div>'''
    pages.append(make_page(17, "अध्याय ६ • वर्ग कुण्डलियाँ", "16 वर्ग कुण्डलियाँ (D1 से D60) का परिचय", p17))

    # Page 18: D9 Navamsha & D10 Dashamsha
    p18 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">६.२ नवांश कुण्डली (D9) का गणितीय निर्माण</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    नवांश कुण्डली को वैदिक ज्योतिष का हृदय कहा जाता है। प्रत्येक 30° राशि 9 भागों (प्रत्येक 3° 20' = 1 चरण) में विभाजित होती है:
  </p>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.83rem; line-height:1.6; color:#1e293b; margin-bottom:0.6rem;">
    • <strong>चर राशियां (मेष, कर्क, तुला, मकर):</strong> नवांश की गणना उसी राशि से शुरू होती है।<br>
    • <strong>स्थिर राशियां (वृषभ, सिंह, वृश्चिक, कुम्भ):</strong> नवांश की गणना उस राशि से 9वें भाव से शुरू होती है।<br>
    • <strong>द्विस्वभाव राशियां (मिथुन, कन्या, धनु, मीन):</strong> नवांश की गणना उस राशि से 5वें भाव से शुरू होती है।
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">६.३ दशमांश कुण्डली (D10): आजीविका का चक्र</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    दशमांश में प्रत्येक राशि को 3° के 10 भागों में काटा जाता है:
  </p>
  <div style="background:#090d16; color:#38bdf8; padding:0.6rem; border-radius:6px; font-family:monospace; font-size:0.83rem; margin-bottom:0.6rem;">
    विषम राशियों में: उसी राशि से गिनती शुरू होती है।<br>
    सम राशियों में: उस राशि से 9वीं राशि से गिनती शुरू होती है।<br>
    D10 लग्न एवं दशम भाव का स्वामी ही जातक के वास्तविक उद्योग व आजीविका का निर्धारण करता है।
  </div>
</div>'''
    pages.append(make_page(18, "अध्याय ६ • नवांश व दशमांश", "D9 नवांश एवं D10 दशमांश का निर्माण", p18))

    # Page 19: D60 & Special Lagnas
    p19 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">६.४ षष्ट्यंश (D60): पूर्वजन्म के संचित कर्मों का एक्सरे</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    महर्षि पराशर ने विंशोपक बल में षष्ट्यंश को सर्वाधिक 4 अंक दिए हैं (D1 को केवल 3.5 अंक दिए हैं!)। प्रत्येक राशि 30 कला (0.5°) के 60 भागों में बंटती है। प्रत्येक भाग का एक अधिष्ठाता देवता होता है (घोर, राक्षस, अमृत, देव आदि)। D60 ही यह बताता है कि कोई जन्मजात राजा के घर क्यों पैदा हुआ और कोई भिखारी के घर।
  </p>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-top:0.8rem; margin-bottom:0.3rem;">६.५ विशेष लग्न गणित (इन्दु, होरा, घटी लग्न)</h4>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.83rem; line-height:1.6; color:#1e293b;">
    <strong>१. इन्दु लग्न (Indu Lagna - धन चुंबक):</strong><br>
    चंद्रमा की कला संख्या (16) और नवमेश की कला संख्या जोड़कर 12 से भाग दिया जाता है। शेष राशि को चंद्रमा से गिनने पर इन्दु लग्न बनता है। इसमें बैठा शुभ ग्रह जातक को अरबपति बनाता है!<br><br>
    <strong>२. होरा लग्न (Hora Lagna):</strong> प्रति 2.5 घटी (1 घंटे) में 1 राशि बढ़ने वाला लग्न, जिससे चल संपत्ति व नकद धन देखा जाता है।<br><br>
    <strong>३. घटी लग्न (Ghati Lagna):</strong> प्रति 1 घटी (24 मिनट) में 1 राशि बढ़ने वाला लग्न, जिससे जातक का राजसत्ता, पद और यश देखा जाता है।
  </div>
</div>'''
    pages.append(make_page(19, "अध्याय ६ • षष्ट्यंश व विशेष लग्न", "D60 षष्ट्यंश एवं इन्दु लग्न गणित", p19))

    # Page 20: Chapter 7 - Jaimini Karakas
    p20 = '''<div>
  <div class="story-box" style="background:rgba(200, 157, 61, 0.08); border-left:4px solid #c89d3d; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#b45309;">📖 रोचक कथा: रंगमंच के 7 पात्र (जैमिनी चर कारक)</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      पराशर पद्धति में ग्रह पक्के विभागों के स्वामी हैं, लेकिन जैमिनी पद्धति में जो ग्रह सबसे अधिक अंश चल चुका होता है, वह राजा (आत्मकारक) बन जाता है! दूसरा मंत्री बन जाता है। इस प्रकार अंशों की होड़ से 7 चर कारक बनते हैं।
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">७.१ सात चर कारकों की अवरोही क्रम सारणी</h4>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>कारक नाम</th>
          <th>अंश क्रम</th>
          <th>प्रतिनिधित्व</th>
          <th>जातक कुण्डली स्थिति</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>आत्मकारक (AK)</strong></td><td>सर्वोच्च अंश</td><td>आत्मा, राजा, जीवन का मूल उद्देश्य</td><td>बुध (24° 46')</td></tr>
        <tr><td><strong>अमात्यकारक (AmK)</strong></td><td>२य सर्वोच्च</td><td>करियर, पद, आजीविका, मुख्य सलाहकार</td><td>गुरु (22° 08')</td></tr>
        <tr><td><strong>भ्रातृकारक (BK)</strong></td><td>३य सर्वोच्च</td><td>गुरु, मार्गदर्शक, भ्राता</td><td>राहु/केतु (20° 35')</td></tr>
        <tr><td><strong>मातृकारक (MK)</strong></td><td>४थ सर्वोच्च</td><td>माता, भूमि, वाहन, मानसिक शांति</td><td>चंद्रमा (13° 10')</td></tr>
        <tr><td><strong>पुत्रकारक (PK)</strong></td><td>५म सर्वोच्च</td><td>संतान, बुद्धि, उच्च विद्या, मंत्र</td><td>शनि (12° 01')</td></tr>
        <tr><td><strong>ज्ञातिकारक (GK)</strong></td><td>६ठ सर्वोच्च</td><td>शत्रु, रोग, बाधाएं, मुकदमेबाजी</td><td>सूर्य (10° 28')</td></tr>
        <tr><td><strong>दाराकारक (DK)</strong></td><td>न्यूनतम अंश</td><td>जीवनसाथी, व्यापारिक साझीदार</td><td>शुक्र (05° 34') / मंगल (01° 22')</td></tr>
      </tbody>
    </table>
  </div>
</div>'''
    pages.append(make_page(20, "अध्याय ७ • जैमिनी सूत्र", "7 चर कारक एवं उनका अवरोही क्रम", p20))

    # Page 21: Arudha Padas
    p21 = '''<div>
  <div class="story-box" style="background:rgba(5, 150, 105, 0.08); border-left:4px solid #059669; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#065f46;">📖 रोचक कथा: भवन और उसकी परछाईं (आरूढ़)</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      सड़क पर खड़ा व्यक्ति आपके घर की असली तिजोरी को नहीं देख सकता—वह केवल सड़क पर पड़ रही घर की परछाईं को देखता है। आरूढ़ वही परछाईं (माया) है जिसे देखकर दुनिया आपके धन, पद और व्यक्तित्व का आकलन करती है!
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">७.२ १२ आरूढ़ पदों का प्रक्षेपण गणित</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    किसी भी भाव का आरूढ़ निकालने के लिए, उसका स्वामी उस भाव से जितने घर आगे बैठा हो, उस स्वामी से उतने ही घर आगे बढ़ जाएं:
  </p>
  <div style="background:#090d16; color:#f8fafc; padding:0.6rem; border-radius:6px; font-family:monospace; font-size:0.83rem; margin-bottom:0.6rem;">
    सूत्र: आरूढ़ पद = भाव स्वामी + n भाव आगे<br>
    <strong>महत्वपूर्ण अपवाद:</strong> यदि आरूढ़ उसी भाव में आ जाए या उससे 7वें में आ जाए, तो वहां से 10 भाव आगे बढ़ जाते हैं! (क्योंकि छाया कभी मूल वस्तु के ऊपर या ठीक उल्टी नहीं होती)।
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">७.३ उपपद लग्न (UL - Upapada Lagna)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6;">
    व्यय भाव (12वें भाव) का आरूढ़ 'उपपद लग्न' कहलाता है। यह दांपत्य जीवन के स्थायित्व, जीवनसाथी के कुल और परिवार की संपन्नता को प्रकट करता है। यदि उपपद लग्न से द्वितीय भाव में शुभ ग्रह हों तो विवाह अटूट और मंगलमय रहता है।
  </p>
</div>'''
    pages.append(make_page(21, "अध्याय ७ • आरूढ़ पद", "आरूढ़ पद प्रक्षेपण एवं उपपद लग्न", p21))

    # Page 22: Bhrigu Nandi Nadi Trines
    p22 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">७.४ भृगु नंदी नाड़ी (BNN): ४ दिशा त्रिकोण</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    भृगु नंदी नाड़ी में भावों से अधिक दिशाओं का महत्व है। एक ही दिशा में स्थित ग्रह एक साथ हाथ मिलाकर युतिवत कार्य करते हैं:
  </p>
  <div class="table-responsive" style="margin-bottom:0.8rem;">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>दिशा</th>
          <th>राशियां (त्रिकोण)</th>
          <th>जीवन स्तंभ</th>
          <th>कल्याणकारी ग्रह</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>पूर्व दिशा</strong></td><td>मेष (1), सिंह (5), धनु (9)</td><td>धर्म त्रिकोण (कर्तव्य, आत्मा, पूर्वपुण्य)</td><td>सूर्य, मंगल, गुरु</td></tr>
        <tr><td><strong>दक्षिण दिशा</strong></td><td>वृषभ (2), कन्या (6), मकर (10)</td><td>अर्थ त्रिकोण (धन, व्यवसाय, सेवा)</td><td>बुध, शनि, शुक्र</td></tr>
        <tr><td><strong>पश्चिम दिशा</strong></td><td>मिथुन (3), तुला (7), कुम्भ (11)</td><td>काम त्रिकोण (इच्छाएं, समाज, मित्र)</td><td>शुक्र, शनि, राहु</td></tr>
        <tr><td><strong>उत्तर दिशा</strong></td><td>कर्क (4), वृश्चिक (8), मीन (12)</td><td>मोक्ष त्रिकोण (मुक्ति, शोध, परलोक)</td><td>चंद्रमा, मंगल, केतु</td></tr>
      </tbody>
    </table>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">७.५ गुरु का १२-वर्षीय प्रगति-गोचर चक्र</h4>
  <p style="font-size:0.85rem; color:#334155; line-height:1.6;">
    बृहस्पति (जीव कारक) प्रति वर्ष एक राशि चलता हुआ 12 वर्ष में जन्म चक्र पूरा करता है। जब गुरु जन्म कालीन ग्रहों के ऊपर से या उनके त्रिकोण से गुजरता है, तो उस वर्ष जातक का विवाह, संतान जन्म, पदोन्नति या भवन निर्माण सुनिश्चित होता है।
  </p>
</div>'''
    pages.append(make_page(22, "अध्याय ७ • नाड़ी त्रिकोण", "भृगु नंदी नाड़ी के 4 दिशा त्रिकोण", p22))

    # Page 23: Chapter 8 - Transit Observatory & Double Transit
    p23 = '''<div>
  <div class="story-box" style="background:rgba(2, 132, 199, 0.08); border-left:4px solid #0284c7; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#0369a1;">📖 रोचक कथा: दो चाबियों वाला दिव्य ताला</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      बैंक के बड़े लॉकर को खोलने के लिए दो चाबियां चाहिए होती हैं—एक मैनेजर की और एक ग्राहक की। उसी प्रकार भाग्य के किसी भी बड़े फल को खोलने के लिए शनि (कर्म का न्याय) और गुरु (ईश्वर का आशीर्वाद) दोनों की चाबी एक साथ लगनी चाहिए!
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">८.१ दोहरा गोचर नियम (Double Transit Mandate)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    जीवन की कोई भी बड़ी घटना (विवाह, पुत्र जन्म, गृह प्रवेश, उच्च पद) तब तक घटित नहीं हो सकती जब तक:
  </p>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.83rem; line-height:1.6; color:#1e293b; margin-bottom:0.6rem;">
    १. <strong>शनि देव</strong> अपनी स्थिति या दृष्टि (3, 7, 10) से उस संबंधित भाव या भावेश को सक्रिय न करें।<br>
    २. <strong>बृहस्पति देव</strong> अपनी स्थिति या दृष्टि (5, 7, 9) से उसी भाव या भावेश पर अपनी अमृत दृष्टि न डालें।<br>
    ३. जब ये दोनों ग्रह एक ही भाव को आशीर्वाद देते हैं, तो वह घटना अवश्यंभावी हो जाती है।
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">८.२ चंद्रमा से शुभ गोचर के भाव</h4>
  <p style="font-size:0.85rem; color:#334155; line-height:1.6;">
    सूर्य: 3, 6, 10, 11 • चंद्र: 1, 3, 6, 7, 10, 11 • मंगल/शनि/राहु/केतु: 3, 6, 11 • गुरु: 2, 5, 7, 9, 11 • शुक्र: 1, 2, 3, 4, 5, 8, 9, 11, 12 • बुध: 2, 4, 6, 8, 10, 11।
  </p>
</div>'''
    pages.append(make_page(23, "अध्याय ८ • गोचर वेधशाला", "दोहरा गोचर नियम एवं ग्रह दृष्टि", p23))

    # Page 24: Sade Sati Physics
    p24 = '''<div>
  <div class="story-box" style="background:rgba(124, 58, 237, 0.08); border-left:4px solid #7c3aed; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#6d28d9;">📖 रोचक कथा: सोने को तपाने वाली भट्टी (साढ़े साती)</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      शनि की साढ़े साती कोई श्राप नहीं है—यह सोने को कुंदन बनाने वाली भट्टी है। 7.5 वर्षों में शनि आपके जीवन से सभी झूठे मित्रों, घमंड और अज्ञानता को जलाकर राख कर देता है और केवल सच्चा, शुद्ध चरित्र शेष छोड़ता है।
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">८.३ साढ़े साती के ३ चरण एवं काल-विभाजन</h4>
  <div class="table-responsive" style="margin-bottom:0.8rem;">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>चरण</th>
          <th>शनि की स्थिति</th>
          <th>अवधि</th>
          <th>मानसिक एवं व्यावहारिक अनुभव</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>प्रथम चरण (उदय)</strong></td><td>चंद्रमा से १२वें भाव में</td><td>2.5 वर्ष</td><td>वित्तीय दबाव, अनिद्रा, एकाकीपन, स्थानांतरण</td></tr>
        <tr><td><strong>द्वितीय चरण (शिखर)</strong></td><td>जन्म चंद्रमा के ऊपर</td><td>2.5 वर्ष</td><td>आत्म-रूपांतरण, गहन संघर्ष, अत्यधिक जिम्मेदारी</td></tr>
        <tr><td><strong>तृतीय चरण (अस्त)</strong></td><td>चंद्रमा से २रे भाव में</td><td>2.5 वर्ष</td><td>परिवार का पुनर्गठन, धन स्थिरता, परिपक्व दृष्टि</td></tr>
      </tbody>
    </table>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">८.४ कंटक शनि एवं अष्टम शनि</h4>
  <p style="font-size:0.85rem; color:#334155; line-height:1.6;">
    जब शनि जन्म राशि से चतुर्थ या दशम में चले, तो उसे 'कंटक शनि' (कांटे की तरह चुभने वाला) कहते हैं। जब अष्टम में चले, तो उसे 'अष्टम शनि' कहते हैं। इसमें अष्टकवर्ग में यदि 28 से अधिक बिंदु हों, तो शनि कोई हानि नहीं करता।
  </p>
</div>'''
    pages.append(make_page(24, "अध्याय ८ • साढ़े साती", "शनि साढ़े साती के ३ चरण एवं भौतिकी", p24))

    # Page 25: Chapter 9 - Marriage Engine
    p25 = '''<div>
  <div class="story-box" style="background:rgba(220, 38, 38, 0.08); border-left:4px solid #dc2626; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#991b1b;">📖 रोचक कथा: दो पवित्र अग्नियों का पावन संगम</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      विवाह कोई सांसारिक समझौता नहीं है, बल्कि दो भिन्न आत्माओं के कर्मों का ऐसा गठबंधन है जहाँ दोनों मिलकर एक-दूसरे के ऋणों को चुकाते हैं और धर्म का पालन करते हैं। सप्तम भाव इस गठबंधन का पवित्र दर्पण है।
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">९.१ वैवाहिक विचार के ४ मुख्य स्तंभ</h4>
  <ul style="font-size:0.84rem; color:#334155; line-height:1.6; padding-left:1.2rem; margin-bottom:0.6rem;">
    <li><strong>प्रथम स्तंभ:</strong> D1 (लग्न कुण्डली) का ७वां भाव, ७वें भाव का स्वामी और उस पर पड़ने वाली दृष्टियां।</li>
    <li><strong>द्वितीय स्तंभ:</strong> D9 (नवांश कुण्डली) का ७वां भाव एवं नवांश पति की स्थिति।</li>
    <li><strong>तृतीय स्तंभ:</strong> नैसर्गिक कारक—पुरुषों के लिए <strong>शुक्र (प्रेम व दांपत्य)</strong> और स्त्रियों के लिए <strong>गुरु (पति व सम्मान)</strong>।</li>
    <li><strong>चतुर्थ स्तंभ:</strong> जैमिनी दाराकारक (DK) एवं उपपद लग्न (UL) की शुभता।</li>
  </ul>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">९.२ विवाह समय निर्धारण सूत्र</h4>
  <p style="font-size:0.85rem; color:#334155; line-height:1.6;">
    विवाह तभी होता है जब ७वें भाव के स्वामी, शुक्र या गुरु की महादशा-अंतर्दशा चल रही हो और गोचर में गुरु व शनि दोनों ७वें भाव या ७वें भाव के स्वामी को देख रहे हों।
  </p>
</div>'''
    pages.append(make_page(25, "अध्याय ९ • विवाह विचार", "सप्तम भाव एवं वैवाहिक फलित के 4 स्तंभ", p25))

    # Page 26: Manglik Dosha & 16 Cancellations
    p26 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">९.३ मांगलिक दोष (कुज दोष) का यथार्थ स्वरूप</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    जब मंगल लग्न, चंद्रमा या शुक्र से <strong>१, २, ४, ७, ८, १२वें भाव</strong> में बैठता है, तो उसे मांगलिक दोष कहा जाता है। यह केवल अत्यधिक ऊर्जा और तेजस्विता का प्रतीक है, कोई भयावह अभिशाप नहीं!
  </p>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-top:0.8rem; margin-bottom:0.3rem;">९.४ मांगलिक दोष परिहार के १६ शास्त्रीय नियम</h4>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.82rem; line-height:1.6; color:#1e293b;">
    १. मंगल अपनी स्वराशि (मेष, वृश्चिक) या उच्च राशि (मकर) में हो तो दोष शून्य होता है।<br>
    २. द्वितीय भाव में मंगल मिथुन या कन्या में हो तो कोई दोष नहीं।<br>
    ३. चतुर्थ भाव में मंगल मेष या वृश्चिक में हो तो परिहार हो जाता है।<br>
    ४. सप्तम भाव में मंगल कर्क (नीच) या मकर (उच्च) में हो तो दोष भंग हो जाता है।<br>
    ५. अष्टम भाव में मंगल धनु या मीन में हो तो दोष समाप्त।<br>
    ६. द्वादश भाव में मंगल वृषभ या तुला में हो तो दोष शून्य।<br>
    ७. मंगल पर गुरु की पूर्ण दृष्टि पड़ रही हो या मंगल चंद्रमा के साथ बैठा हो।<br>
    ८. जीवनसाथी की कुण्डली में उसी भाव में शनि, राहु या मंगल बैठा हो।<br>
    <strong>सत्य निष्कर्ष:</strong> 80% से अधिक कुण्डलियों में मांगलिक दोष इन परिहार नियमों के कारण पूर्णतः निष्प्रभावी हो जाता है!
  </div>
</div>'''
    pages.append(make_page(26, "अध्याय ९ • मांगलिक विचार", "मांगलिक दोष एवं 16 शास्त्रीय परिहार नियम", p26))

    # Page 27: Chapter 10 - Kundli Milan (36 Gunas)
    p27 = '''<div>
  <div class="story-box" style="background:rgba(5, 150, 105, 0.08); border-left:4px solid #059669; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#065f46;">📖 रोचक कथा: वीणा के ८ तार (अष्टकूट मिलान)</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      अष्टकूट मिलान 8 तारों वाली वीणा की तरह है। 1 अंक के तार (वर्ण) से लेकर 8 अंक के सबसे मोटे तार (नाड़ी) तक, सभी का समवेत स्वर ही दांपत्य संगीत रचता है। यदि 18 से अधिक तार सुर में हों, तो जीवन मधुर हो जाता है!
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१०.१ अष्टकूट ३६ गुणों का सम्पूर्ण अंक विभाजन</h4>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>कूट</th>
          <th>गुण अंक</th>
          <th>जांचने का विषय</th>
          <th>कल्याणकारी प्रभाव</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>१. वर्ण</strong></td><td>१ अंक</td><td>अहंकार व आध्यात्मिक साम्यता</td><td>पारस्परिक सम्मान</td></tr>
        <tr><td><strong>२. वश्य</strong></td><td>२ अंक</td><td>पारस्परिक आकर्षण व समर्पण</td><td>एकनिष्ठता</td></tr>
        <tr><td><strong>३. तारा</strong></td><td>३ अंक</td><td>भाग्य एवं स्वास्थ्य अनुकूलता</td><td>दीर्घायु व सौभाग्य</td></tr>
        <tr><td><strong>४. योनि</strong></td><td>४ अंक</td><td>शारीरिक व जैविक अनुकूलता</td><td>पारस्परिक संतुष्टि</td></tr>
        <tr><td><strong>५. ग्रहमैत्री</strong></td><td>५ अंक</td><td>मानसिक व वैचारिक मित्रता</td><td>संवाद एवं सामंजस्य</td></tr>
        <tr><td><strong>६. गण</strong></td><td>६ अंक</td><td>स्वभाव (देव, मनुष्य, राक्षस)</td><td>दैनिक तालमेल</td></tr>
        <tr><td><strong>७. भकूट</strong></td><td>७ अंक</td><td>भाव दूरी (प्रेम व धन प्रवाह)</td><td>समृद्धि व संतति</td></tr>
        <tr><td><strong>८. नाड़ी</strong></td><td>८ अंक</td><td>आनुवंशिक (Genetic) स्वास्थ्य</td><td>स्वस्थ संतान व वंश रक्षा</td></tr>
        <tr style="font-weight:700; background:#f0fdf4;"><td><strong>कुल अंक</strong></td><td><strong>३६ अंक</strong></td><td colspan="2"><strong>१८ अंक से ऊपर विवाह ग्राह्य माना जाता है</strong></td></tr>
      </tbody>
    </table>
  </div>
</div>'''
    pages.append(make_page(27, "अध्याय १० • अष्टकूट मिलान", "36 गुणों का सम्पूर्ण अंक विभाजन", p27))

    # Page 28: Nadi & Bhakoot Exceptions
    p28 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१०.२ नाड़ी दोष एवं उसके शास्त्रीय परिहार (Nadi Parihara)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    नाड़ी 3 प्रकार की होती है—आद्य (वात), मध्य (पित्त), अंत्य (कफ)। समान नाड़ी होने पर नाड़ी दोष लगता है। परंतु शास्त्रों में इसके अचूक परिहार नियम हैं:
  </p>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.83rem; line-height:1.6; color:#1e293b; margin-bottom:0.6rem;">
    • दोनों का एक ही नक्षत्र हो लेकिन चरण अलग-अलग हों, तो <strong>नाड़ी दोष स्वतः समाप्त</strong> हो जाता है!<br>
    • दोनों की राशि एक हो लेकिन नक्षत्र अलग हों, तो दोष नहीं लगता।<br>
    • दोनों के नक्षत्र स्वामी एक हों या आपस में परम मित्र हों, तो नाड़ी दोष निष्प्रभावी हो जाता है।
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१०.३ भकूट दोष (६/८, ९/५, २/१२) एवं परिहार</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    जब दोनों की राशियों में 6/8, 9/5 या 2/12 का अंतर हो, तो भकूट दोष माना जाता है। परंतु यदि दोनों राशियों के स्वामी एक ही हों (जैसे मेष-वृश्चिक के मंगल, वृषभ-तुला के शुक्र) अथवा दोनों के स्वामी परम मित्र हों (जैसे कर्क-मीन के चंद्र-गुरु), तो <strong>भकूट दोष शून्य</strong> हो जाता है!
  </p>
</div>'''
    pages.append(make_page(28, "अध्याय १० • दोष परिहार", "नाड़ी दोष एवं भकूट दोष के परिहार", p28))

    # Page 29: Chapter 11 - 23 Domains (Career)
    p29 = '''<div>
  <div class="story-box" style="background:rgba(2, 132, 199, 0.08); border-left:4px solid #0284c7; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#0369a1;">📖 रोचक कथा: कर्म क्षेत्र का दिव्य सिंहासन</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      कोई व्यक्ति नौकरी करेगा या व्यापार? वह डॉक्टर बनेगा, इंजीनियर, लेखक या राजनेता? इसका उत्तर दशम भाव और दशमांश (D10) के उस ग्रह में छिपा है जो सबसे अधिक बलवान होकर आजीविका का निर्देश देता है।
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">११.१ आजीविका निर्धारण का ३-स्तरीय एल्गोरिथ्म</h4>
  <ul style="font-size:0.84rem; color:#334155; line-height:1.6; padding-left:1.2rem; margin-bottom:0.6rem;">
    <li><strong>स्तर १:</strong> लग्न कुण्डली के दशम भाव में बैठे ग्रह एवं दशमेश की स्थिति।</li>
    <li><strong>स्तर २:</strong> जैमिनी अमात्यकारक (AmK) ग्रह किस राशि और भाव में स्थित है।</li>
    <li><strong>स्तर ३:</strong> दशमांश (D10) के लग्न एवं दशम भाव का स्वामी।</li>
  </ul>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">११.२ ग्रहों के आधार पर ३५+ उद्योग क्षेत्र</h4>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.82rem; line-height:1.6; color:#1e293b;">
    • <strong>सूर्य:</strong> प्रशासनिक सेवा, आईएएस/आईपीएस, राजनीति, औषधि, स्वर्ण, सत्ता।<br>
    • <strong>चंद्रमा:</strong> जनसंपर्क, नौसेना, दुग्ध उद्योग, होटल, तरल पदार्थ, मनोविज्ञान।<br>
    • <strong>मंगल:</strong> सॉफ्टवेयर कोडिंग, रक्षा, रियल एस्टेट, शल्य चिकित्सा (Surgeon), पुलिस।<br>
    • <strong>बुध:</strong> आईटी, आर्टिफिशियल इंटेलिजेंस, वाणिज्य, बैंकिंग, प्रकाशन, चार्टर्ड अकाउंटेंसी।<br>
    • <strong>बृहस्पति:</strong> न्यायपालिका, शिक्षा, दर्शन, वित्तीय सलाहकार, आध्यात्मिक मार्गदर्शक।<br>
    • <strong>शुक्र:</strong> मीडिया, फिल्म, फैशन, विलासिता, वास्तुकला, वाहन उद्योग।<br>
    • <strong>शनि:</strong> भारी उद्योग, खनन, तेल, श्रम संगठन, न्याय, प्राचीन इतिहास, शोध।<br>
    • <strong>राहु:</strong> एआई अनुसंधान, विदेशी व्यापार, विमानन, साइबर सुरक्षा, गुप्तचर विभाग।<br>
    • <strong>केतु:</strong> अध्यात्म, सूक्ष्म जीव विज्ञान, गुप्त साधना, कोडिंग, योग।
  </div>
</div>'''
    pages.append(make_page(29, "अध्याय ११ • आजीविका गणित", "दशम भाव, D10 एवं 35+ उद्योग क्षेत्र", p29))

    # Page 30: Wealth, Property, Children
    p30 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">११.३ धन एवं संपत्ति का इन्दु लग्न गणित</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    इन्दु लग्न में यदि उच्च का या स्वराशि का शुभ ग्रह बैठा हो, तो जातक अपने जीवन में करोड़ों की संपत्ति का स्वामी बनता है। द्वितीय भाव से संचित धन और एकादश भाव से दैनिक आय की गति देखी जाती है।
  </p>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-top:0.7rem; margin-bottom:0.3rem;">११.४ भूमि, भवन एवं वाहन (D4 व D16)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    चतुर्थ भाव और मंगल भूमि के स्थायी स्वामी हैं। चतुर्थांश (D4) में यदि चतुर्थेश बली हो, तो जातक अनेक भवनों का स्वामी बनता है। षोडशांश (D16) में शुक्र बली होने पर उत्तम वाहनों का निरंतर सुख मिलता है।
  </p>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-top:0.7rem; margin-bottom:0.3rem;">११.५ संतान सुख एवं सप्तमांश (D7) चक्र</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6;">
    पंचम भाव बुद्धि और संतान का स्थान है। गुरु इसका नैसर्गिक कारक है। सप्तमांश (D7) में विषम राशि से प्रथम संतान और उससे तीसरे (७वें) से द्वितीय संतान की गणना की जाती है। बीज स्फुट (पुरुष) और क्षेत्र स्फुट (स्त्री) की शुभता से गर्भाधान की क्षमता का निर्णय होता है।
  </p>
</div>'''
    pages.append(make_page(30, "अध्याय ११ • धन व संपत्ति", "इन्दु लग्न, भूमि D4 एवं संतान D7", p30))

    # Page 31: Health, Travel, Litigation
    p31 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">११.६ आयुर्-ज्योतिष एवं त्रिदोष संतुलन (Health Engine)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    शरीर की आरोग्यता लग्न से और रोग षष्ठ भाव से देखे जाते हैं। ग्रहों के तत्वों से त्रिदोष निर्धारित होते हैं:
  </p>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.83rem; line-height:1.6; color:#1e293b; margin-bottom:0.6rem;">
    • <strong>वात प्रकृति (Air):</strong> शनि एवं बुध — संधिवात, तंत्रिका विकार, गैस, अनिद्रा।<br>
    • <strong>पित्त प्रकृति (Fire):</strong> सूर्य एवं मंगल — एसिडिटी, रक्त विकार, ज्वर, त्वचा रोग।<br>
    • <strong>कफ प्रकृति (Water):</strong> चंद्रमा एवं शुक्र — श्वास रोग, मोटापा, कफ, जल विकार।
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">११.७ विदेश यात्रा एवं विदेश में बसना</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    नवम भाव (लंबी धार्मिक यात्रा), द्वादश भाव (विदेश भूमि) और राहु का चर राशियों (मेष, कर्क, तुला, मकर) या जल राशियों से संबंध होने पर जातक का स्थायी विदेश वास होता है।
  </p>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">११.८ शत्रु, विवाद एवं मुकदमेबाजी (६ठा भाव)</h4>
  <p style="font-size:0.85rem; color:#334155; line-height:1.6;">
    षष्ठ भाव में मंगल या शनि का बैठना शत्रुओं का नाश करता है। जब षष्ठेश एकादशेश से संबंध बनाए, तो जातक अदालती मुकदमों में भारी विजय प्राप्त करता है।
  </p>
</div>'''
    pages.append(make_page(31, "अध्याय ११ • स्वास्थ्य व यात्रा", "त्रिदोष संतुलन, विदेश वास एवं षष्ठ भाव", p31))

    # Page 32: Chapter 12 - Misfortune & Arishta Bhanga
    p32 = '''<div>
  <div class="story-box" style="background:rgba(5, 150, 105, 0.08); border-left:4px solid #059669; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#065f46;">📖 रोचक कथा: किले की अभेद्य ढाल (अरिष्ट भंग)</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      यदि बाहर तेज आंधी-तूफान चल रहा हो, लेकिन आपके पास कंक्रीट की मजबूत छत और गर्म अलाव हो, तो आंधी आपका बाल भी बांका नहीं कर सकती! कुण्डली में अरिष्ट भंग वही अभेद्य ढाल है जो लाखों दोषों को एक पल में भस्म कर देती है।
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१२.१ १००-अंक अरिष्ट भंग सुरक्षा स्कोर कार्ड</h4>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>सुरक्षा ढाल</th>
          <th>कवच अंक</th>
          <th>शास्त्रीय प्रमाण</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>उच्च का गुरु केंद्र (1, 4, 7, 10) में</strong></td><td>+२५ अंक</td><td>"किं कुर्वन्ति ग्रहाः सर्वे यस्य केंद्रे बृहस्पतिः" (लाखों दोष नष्ट)</td></tr>
        <tr><td><strong>बली लग्नेश केंद्र या त्रिकोण में</strong></td><td>+२० अंक</td><td>शरीर और आत्मबल की पूर्ण विजय</td></tr>
        <tr><td><strong>पूर्ण चंद्रमा पर गुरु/शुक्र की दृष्टि</strong></td><td>+१५ अंक</td><td>मानसिक व शारीरिक संजीवनी कवच</td></tr>
        <tr><td><strong>चंद्रमा से 6, 7, 8 में शुभ ग्रह (अधि योग)</strong></td><td>+१५ अंक</td><td>अकाल मृत्यु व रोगों से संपूर्ण मुक्ति</td></tr>
        <tr><td><strong>लग्न में 30 से अधिक SAV बिंदु</strong></td><td>+१० अंक</td><td>प्रकृति का स्वाभाविक रोग-प्रतिरोधक तंत्र</td></tr>
        <tr><td><strong>दशम या एकादश भाव में बली सूर्य</strong></td><td>+१५ अंक</td><td>राजकीय व सामाजिक जीवन रक्षा</td></tr>
        <tr style="font-weight:700; background:#f0fdf4;"><td><strong>कुल कवच अंक</strong></td><td><strong>१०० अंक</strong></td><td><strong>५० अंक से ऊपर सम्पूर्ण अरिष्ट भंग सिद्ध होता है!</strong></td></tr>
      </tbody>
    </table>
  </div>
</div>'''
    pages.append(make_page(32, "अध्याय १२ • अरिष्ट भंग", "100-अंक अरिष्ट भंग सुरक्षा कवच", p32))

    # Page 33: Kaal Sarp & Pitru Dosha
    p33 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१२.२ कालसर्प योग का वैज्ञानिक यथार्थ</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    जब सभी सातों ग्रह राहु और केतु की धुरी के एक तरफ आ जाते हैं, तो उसे कालसर्प योग कहा जाता है। यह कोई अभिशाप नहीं, बल्कि जीवन की ऊर्जा का एक तरफ एकाग्र (Intense Focus) होना है। संसार के शीर्ष वैज्ञानिकों, दार्शनिकों और नेताओं की कुण्डलियों में कालसर्प योग पाया गया है!
  </p>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-top:0.7rem; margin-bottom:0.3rem;">१२.३ पितृ दोष एवं ग्रहण दोष</h4>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.6rem; border-radius:6px; font-size:0.82rem; line-height:1.6; color:#1e293b; margin-bottom:0.6rem;">
    • <strong>पितृ दोष:</strong> नवम भाव, नवमेश या सूर्य पर राहु/केतु का प्रभाव। इसका उपाय किसी भय से नहीं, बल्कि पूर्वजों के प्रति तर्पण, पीपल वृक्षारोपण और निर्धनों को अन्नदान से होता है।<br>
    • <strong>ग्रहण दोष:</strong> सूर्य या चंद्रमा के साथ राहु/केतु की युति। इसमें शिव उपासना और महामृत्युंजय जप से जीवन अमृतमय हो जाता है।<br>
    • <strong>गुरु चांडाल योग:</strong> गुरु + राहु की युति। परंपराओं से हटकर नए युग के लीक से अलग आविष्कार करने की क्षमता!
  </div>
  <p style="font-size:0.84rem; color:#0f766e; font-weight:600;">
    शास्त्र का नियम: कोई भी दोष व्यक्ति को तभी छू सकता है जब उसका लग्नेश कमजोर हो। लग्नेश के बलवान होते ही सभी दोष अनुकूलता में बदल जाते हैं।
  </p>
</div>'''
    pages.append(make_page(33, "अध्याय १२ • दोष विवेक", "कालसर्प, पितृ दोष एवं वैज्ञानिक परिहार", p33))

    # Page 34: Muhurat & Katapayadi Naming
    p34 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१२.४ शुभ विवाह मुहूर्त के अनिवार्य खगोलीय नियम</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    विवाह मुहूर्त में सूर्य, चंद्रमा, गुरु और शुक्र की स्थिति का सर्वोच्च ध्यान रखा जाता है:
  </p>
  <ul style="font-size:0.84rem; color:#334155; line-height:1.6; padding-left:1.2rem; margin-bottom:0.6rem;">
    <li><strong>गुरु एवं शुक्र का अस्त न होना:</strong> देवगुरु बृहस्पति या भार्गव शुक्र के अस्त काल में विवाह निषेध है।</li>
    <li><strong>त्रिबल शुद्धि:</strong> वर के लिए सूर्य का बल, कन्या के लिए गुरु का बल, और दोनों के लिए चंद्रमा का बल अनुकूल होना चाहिए।</li>
    <li><strong>मलमास (अधिमास) निषेध:</strong> जिस चंद्र मास में सूर्य संक्रांति न हो, उसमें मांगलिक कार्य वर्जित हैं।</li>
  </ul>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१२.५ कटपयादि वर्ण-ध्वनि एवं व्यापार नामकरण</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6;">
    प्राचीन भारत का 'कटपयादि' सूत्र प्रत्येक अक्षर को अंक और तत्व प्रदान करता है। जातक के जन्म नक्षत्र के मित्र अक्षर से जब व्यवसाय, कंपनी या ब्रांड का नाम रखा जाता है, तो उस ब्रांड की ख्याति देश-विदेश में बिना अतिरिक्त विज्ञापन के फैलती है!
  </p>
</div>'''
    pages.append(make_page(34, "अध्याय १२ • मुहूर्त संहिता", "शुभ विवाह मुहूर्त एवं कटपयादि नामकरण", p34))

    # Page 35: Sarvatobhadra Chakra
    p35 = '''<div>
  <div class="story-box" style="background:rgba(2, 132, 199, 0.08); border-left:4px solid #0284c7; padding:0.8rem; border-radius:4px; margin-bottom:0.8rem;">
    <strong style="color:#0369a1;">📖 रोचक कथा: 81 कोष्ठकों का सर्वतोभद्र चक्र</strong>
    <p style="font-size:0.86rem; margin:0.3rem 0; color:#334155; line-height:1.6;">
      प्राचीन राजाओं के युद्ध और आज के शेयर बाजार के उतार-चढ़ाव की भविष्यवाणी करने का सबसे गुप्त और शक्तिशाली यंत्र 9×9 = 81 खानों का 'सर्वतोभद्र चक्र' है। यह अक्षरों, नक्षत्रों और राशियों के सीधे वेध को दर्शाता है।
    </p>
  </div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">१२.६ सर्वतोभद्र चक्र वेध के ३ प्रमुख नियम</h4>
  <ul style="font-size:0.84rem; color:#334155; line-height:1.6; padding-left:1.2rem; margin-bottom:0.6rem;">
    <li><strong>सम्मुख वेध (Direct Front Aspect):</strong> ग्रह अपने ठीक सामने वाले नक्षत्र और अक्षर को सीधे प्रभावित करता है।</li>
    <li><strong>वाम वेध (Left Diagonal):</strong> वक्री ग्रह का वेध बाईं ओर मुड़कर तीव्र उतार-चढ़ाव लाता है।</li>
    <li><strong>दक्षिण वेध (Right Diagonal):</strong> मार्गी और शीघ्रगामी ग्रह दाईं ओर वेध करके त्वरित लाभ देते हैं।</li>
  </ul>
  <p style="font-size:0.85rem; color:#334155; line-height:1.6;">
    जब गुरु या शुक्र जन्म नक्षत्र या नामाक्षर पर अमृत वेध करते हैं, तो व्यक्ति का यश, व्यापारिक अनुबंध और वित्तीय लाभ शिखर पर पहुंच जाता है।
  </p>
</div>'''
    pages.append(make_page(35, "अध्याय १२ • सर्वतोभद्र", "81 कोष्ठक सर्वतोभद्र चक्र एवं वेध विज्ञान", p35))

    # Page 36: Chapter 13 - Master Calculation Pipeline
    p36 = f'''<div>
  <h4 style="color:#0f766e; font-size:1rem; margin-bottom:0.4rem; text-align:center;">१३.१ संपूर्ण कुण्डली विवेचन महा-पाइपलाइन (The 15-Step Algorithm)</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.5rem; text-align:center;">
    जब भी कोई जन्म विवरण प्राप्त हो, एक दक्ष ज्योतिषी एवं शोधकर्ता को इसी क्रम में गणना करनी चाहिए:
  </p>
  <div style="background:#090d16; color:#f8fafc; padding:0.8rem; border-radius:8px; font-size:0.82rem; line-height:1.7;">
    <strong style="color:#10b981;">चरण १:</strong> जन्म समय से UT एवं जूलियन डे (JD) की शुद्ध खगोलीय गणना।<br>
    <strong style="color:#10b981;">चरण २:</strong> लाहिरी अयनांश घटाकर ९ ग्रहों एवं लग्न का स्पष्ट निरयण भोगांश।<br>
    <strong style="color:#10b981;">चरण ३:</strong> पंचांग के ५ अंगों (तिथि, वार, नक्षत्र, योग, करण) का निर्धारण।<br>
    <strong style="color:#10b981;">चरण ४:</strong> ग्रहों की दीप्तादि एवं बाल्यादि अवस्थाएं तथा पंचधा मैत्री सारणी।<br>
    <strong style="color:#10b981;">चरण ५:</strong> चंद्रमा के पुष्य नक्षत्र से 120-वर्षीय विंशोत्तरी दशा भोग्य शेष।<br>
    <strong style="color:#10b981;">चरण ६:</strong> पंच महापुरुष, केंद्र-त्रिकोण राजयोग एवं नीचभंग की जांच।<br>
    <strong style="color:#10b981;">चरण ७:</strong> सर्वाष्टकवर्ग में 337 बिंदुओं का वितरण एवं 28 बिंदु कसौटी।<br>
    <strong style="color:#10b981;">चरण ८:</strong> D9 नवांश, D10 दशमांश एवं D60 षष्ट्यंश सूक्ष्म कुण्डली निर्माण।<br>
    <strong style="color:#10b981;">चरण ९:</strong> जैमिनी 7 चर कारक अवरोही क्रम एवं 12 आरूढ़ पदों का प्रक्षेपण।<br>
    <strong style="color:#10b981;">चरण १०:</strong> भृगु नंदी नाड़ी के 4 दिशा त्रिकोण (1-5-9, 2-6-10) ग्रह संगम।<br>
    <strong style="color:#10b981;">चरण ११:</strong> शनि-गुरु का दोहरा गोचर (Double Transit) एवं साढ़े साती चरण।<br>
    <strong style="color:#10b981;">चरण १२:</strong> वैवाहिक सप्तम भाव, उपपद एवं 16 मांगलिक परिहार जांच।<br>
    <strong style="color:#10b981;">चरण १३:</strong> 23 जीवन क्षेत्रों का स्वतंत्र विश्लेषण (करियर, वित्त, स्वास्थ्य)।<br>
    <strong style="color:#10b981;">चरण १४:</strong> 17 अरिष्ट संकलन एवं 100-अंक सुरक्षा कवच स्कोरिंग।<br>
    <strong style="color:#10b981;">चरण १५:</strong> अंतिम प्रामाणिक भविष्यवाणी एवं जीवन मार्गदर्शन का प्रतिपादन!
  </div>
</div>'''
    pages.append(make_page(36, "अध्याय १३ • महा-पाइपलाइन", "सम्पूर्ण कुण्डली विवेचन का 15-चरणीय क्रम", p36))

    # Page 37: Appendix A - Formula Cheat Sheet
    p37 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">परिशिष्ट क: शास्त्रीय गणितीय स्थिरांक एवं त्वरित सूत्र</h4>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.82rem; text-align:left;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>खगोलीय घटक</th>
          <th>शास्त्रीय मान</th>
          <th>त्वरित गणना सूत्र</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>राशि चक्र</strong></td><td>360° (12 राशियां)</td><td>प्रति राशि = 30° (1800')</td></tr>
        <tr><td><strong>नक्षत्र विस्तार</strong></td><td>13° 20' (800')</td><td>360° ÷ 27 नक्षत्र</td></tr>
        <tr><td><strong>नक्षत्र चरण</strong></td><td>03° 20' (200')</td><td>13° 20' ÷ 4 चरण (नवांश मान)</td></tr>
        <tr><td><strong>तिथि विस्तार</strong></td><td>12° 00' (720')</td><td>(चंद्रमा - सूर्य) ÷ 12°</td></tr>
        <tr><td><strong>करण विस्तार</strong></td><td>06° 00' (360')</td><td>तिथि का आधा भाग</td></tr>
        <tr><td><strong>कक्षी विस्तार</strong></td><td>03° 45' (225')</td><td>30° राशि ÷ 8 कक्षी</td></tr>
        <tr><td><strong>घटी-पल मान</strong></td><td>1 घटी = 24 मिनट</td><td>60 घटी = 24 घंटे (1 अहोरात्र)</td></tr>
        <tr><td><strong>इन्दु लग्न</strong></td><td>कला योग ÷ 12</td><td>शेष राशि चंद्रमा से अग्रिम</td></tr>
        <tr><td><strong>विंशोत्तरी दशा</strong></td><td>120 वर्ष</td><td>चंद्र नक्षत्र भोग्य अनुपात</td></tr>
      </tbody>
    </table>
  </div>
</div>'''
    pages.append(make_page(37, "परिशिष्ट क • सूत्र संक्षेप", "गणितीय स्थिरांक एवं त्वरित सूत्र तालिका", p37))

    # Page 38: Appendix B - Nakshatra & Navamsha Table
    p38 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">परिशिष्ट ख: २७ नक्षत्र, स्वामी एवं नवांश राशि सारणी</h4>
  <div class="table-responsive">
    <table class="data-table" style="width:100%; font-size:0.80rem; text-align:center;">
      <thead>
        <tr style="background:#0f766e; color:#fff;">
          <th>सं.</th>
          <th>नक्षत्र नाम</th>
          <th>स्वामी</th>
          <th>विस्तार अंश</th>
          <th>नवांश चरण (१, २, ३, ४)</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>1</td><td>अश्विनी</td><td>केतु</td><td>00°00' - 13°20' मेष</td><td>मेष, वृषभ, मिथुन, कर्क</td></tr>
        <tr><td>2</td><td>भरणी</td><td>शुक्र</td><td>13°20' - 26°40' मेष</td><td>सिंह, कन्या, तुला, वृश्चिक</td></tr>
        <tr><td>3</td><td>कृत्तिका</td><td>सूर्य</td><td>26°40' मेष - 10°00' वृषभ</td><td>धनु, मकर, कुम्भ, मीन</td></tr>
        <tr><td>4</td><td>रोहिणी</td><td>चंद्र</td><td>10°00' - 23°20' वृषभ</td><td>मेष, वृषभ, मिथुन, कर्क</td></tr>
        <tr><td>5</td><td>मृगशिरा</td><td>मंगल</td><td>23°20' वृषभ - 06°40' मिथुन</td><td>सिंह, कन्या, तुला, वृश्चिक</td></tr>
        <tr><td>6</td><td>आर्द्रा</td><td>राहु</td><td>06°40' - 20°00' मिथुन</td><td>धनु, मकर, कुम्भ, मीन</td></tr>
        <tr><td>7</td><td>पुनर्वसु</td><td>गुरु</td><td>20°00' मिथुन - 03°20' कर्क</td><td>मेष, वृषभ, मिथुन, कर्क</td></tr>
        <tr><td>8</td><td>पुष्य</td><td>शनि</td><td>03°20' - 16°40' कर्क</td><td>सिंह, कन्या, तुला, वृश्चिक</td></tr>
        <tr><td>9</td><td>आश्लेषा</td><td>बुध</td><td>16°40' - 30°00' कर्क</td><td>धनु, मकर, कुम्भ, मीन</td></tr>
      </tbody>
    </table>
  </div>
  <p style="font-size:0.82rem; color:#64748b; margin-top:0.4rem; line-height:1.5;">
    शेष 18 नक्षत्र (मघा से रेवती तक) इसी 108 चरणों के चक्र की आवृत्ति करते हैं। 108 चरण ही 108 नवांश और रुद्राक्ष माला के 108 मणियों का गूढ़ रहस्य हैं।
  </p>
</div>'''
    pages.append(make_page(38, "परिशिष्ट ख • नक्षत्र चक्र", "27 नक्षत्र, स्वामी एवं 108 चरण चक्र", p38))

    # Page 39: Bibliography & Classical Authorities
    p39 = '''<div>
  <h4 style="color:#0f766e; font-size:0.95rem; margin-bottom:0.3rem;">परिशिष्ट ग: संदर्भ ग्रंथ सूची एवं शास्त्रीय आधार</h4>
  <p style="font-size:0.86rem; color:#334155; line-height:1.6; margin-bottom:0.4rem;">
    इस महाग्रंथ में प्रतिपादित समस्त सूत्र सनातन ऋषियों द्वारा विरचित मूल ग्रंथों एवं आधुनिक खगोलीय वेधशालाओं के मानकों पर पूर्णतः आधारित हैं:
  </p>
  <ul style="font-size:0.83rem; color:#334155; line-height:1.65; padding-left:1.2rem;">
    <li><strong>बृहत् पराशर होरा शास्त्र (BPHS):</strong> महर्षि पराशर प्रणीत संपूर्ण होरा, षोडशवर्ग, राजयोग एवं अष्टकवर्ग का मूल आधार ग्रंथ।</li>
    <li><strong>जैमिनी उपदेश सूत्रम्:</strong> महर्षि जैमिनी कृत चर कारक, आरूढ़ पद एवं कारकांश विवेचन।</li>
    <li><strong>भृगु नंदी नाड़ी (BNN):</strong> महर्षि भृगु एवं नंदीश्वर प्रणीत ग्रह संयोजन, दिशा-आधारित दृष्टि एवं जीव-कर्म कारक संबंध।</li>
    <li><strong>मुहूर्त चिंतामणि:</strong> आचार्य राम दैवज्ञ कृत पंचांग, लग्न शुद्धि, विवाह एवं यात्रा मुहूर्त विधान।</li>
    <li><strong>फलदीपिका:</strong> मंत्रेश्वर महाराज कृत दशा फल, भाव फल एवं ग्रह अवस्थाएं।</li>
    <li><strong>सूर्य सिद्धांत:</strong> प्राचीनतम वैदिक खगोलीय गति-विज्ञान एवं अयनांश विवेचना।</li>
    <li><strong>स्विस एफेमेरिस (Swiss Ephemeris):</strong> आधुनिक नासा एवं आईएयू समर्थित माइक्रोन-सटीक ग्रहीय गणना इंजन।</li>
  </ul>
</div>'''
    pages.append(make_page(39, "परिशिष्ट ग • संदर्भ ग्रंथ", "शास्त्रीय प्रमाण एवं ग्रंथ सूची", p39))

    # Page 40: Colophon & Closing
    p40 = '''<div class="colophon-wrapper" style="text-align:center; padding:1.5rem 1rem;">
  <div style="font-size:1.6rem; color:#10b981; margin-bottom:0.8rem;">॥ शुभं भवतु • ॐ तत्सत् ॥</div>
  <div style="margin:1rem auto;"><img src="assets/yantra.svg" alt="Yantra" width="90" height="90" style="filter: drop-shadow(0 0 12px rgba(16, 185, 129, 0.3));"></div>
  <h3 style="font-size:1.35rem; color:#059669; font-family:'Noto Serif Devanagari', serif; font-weight:800; margin-bottom:0.4rem;">वैदिक कुण्डली विचार एवं गणित महाग्रंथ</h3>
  <div style="font-size:0.95rem; color:#0284c7; font-weight:600; margin-bottom:1rem;">The Cosmic Algorithm: Vedic Horoscope Mathematics & Destiny Decoded</div>
  <p style="font-size:0.86rem; color:#334155; max-width:460px; margin:0 auto 1.2rem auto; line-height:1.65;">
    यह पावन ग्रंथ तंत्र ज्ञान शोध संस्थान की आधिकारिक डिजिटल ग्रंथमाला का चतुर्थ स्तम्भ है। इसका उद्देश्य प्राचीन ऋषियों के गुप्त गणितीय विज्ञान को जन-जन तक पहुंचाना है ताकि प्रत्येक मनुष्य अपने जीवन के पथ को स्पष्ट देख सके।
  </p>
  <div style="background:rgba(5, 150, 105, 0.08); border:1px solid #10b981; border-radius:8px; padding:0.8rem; max-width:440px; margin:0 auto; font-size:0.85rem; color:#1e293b;">
    <strong>ग्रंथकार: ज्योतिषाचार्य आशुतोष कुमार चौबे</strong><br>
    <span style="font-size:0.8rem; color:#64748b;">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</span><br>
    <span style="font-size:0.8rem; color:#0284c7;">आधिकारिक पोर्टल: https://t.worldgyan.com</span>
  </div>
</div>'''
    pages.append(make_page(40, "अंतिम पृष्ठ • Colophon", "प्रशस्ति एवं ग्रंथ समाप्ति", p40))

    return pages

def main():
    pages_list = build_pages()
    print(f"Generated {len(pages_list)} rich pages for Kundali Ganita Vichar Mahagranth.")

    # 1. Assemble kundali-ganita-reader.html using exact structure from reader.html
    with open(READER_TEMPLATE_SRC, "r", encoding="utf-8") as f:
        template_lines = f.readlines()

    first_art_idx = next(i for i, l in enumerate(template_lines) if '<article class="book-page-data"' in l)
    last_art_idx = next(i for i in range(len(template_lines)-1, -1, -1) if '</article>' in template_lines[i])

    reader_top = "".join(template_lines[:first_art_idx])
    reader_bot = "".join(template_lines[last_art_idx+1:])

    # Customize reader top metadata
    reader_top = reader_top.replace(
        "<title>वैदिक ज्योतिष महाग्रंथ सरलीकृत | Complete Vedic Astrology Compendium Simplified</title>",
        "<title>वैदिक कुण्डली विचार एवं गणित महाग्रंथ (3D फ्लिप बुक) • The Cosmic Algorithm 3D Reader</title>"
    )
    reader_top = reader_top.replace(
        'title="वैदिक ज्योतिष महाग्रंथ मुखपृष्ठ"',
        'title="वैदिक कुण्डली विचार एवं गणित महाग्रंथ"'
    )
    reader_top = reader_top.replace(
        'तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ',
        'वैदिक कुण्डली विचार एवं गणित महाग्रंथ (The Cosmic Algorithm)'
    )
    reader_top = reader_top.replace('p > 88', 'p > 40')
    reader_top = reader_top.replace("localStorage.getItem('tantra_book_page')", "localStorage.getItem('tantra_ganita_flip_page')")
    reader_top = reader_top.replace("localStorage.setItem('tantra_book_page'", "localStorage.setItem('tantra_ganita_flip_page'")
    reader_top = reader_top.replace('max="100"', 'max="40"')
    reader_top = reader_top.replace('href="astrology-book-engine/dist/web/index.html"', 'href="kundali-ganita.html"')
    reader_top = reader_top.replace('href="tantra-gyan-vedic-jyotish-mahagranth.pdf"', 'href="kundali-ganita-vichar-mahagranth.pdf"')
    reader_top = reader_top.replace('download="Tantra-Gyan-Vedic-Jyotish-Maha-Granth.pdf"', 'download="Kundali-Ganita-Vichar-Mahagranth.pdf"')
    reader_top = reader_top.replace("Page 1 of 100", "Page 1 of 40")

    # Inject prominent navigation buttons into the 3D Reader header
    custom_nav = '''
          <div style="display:flex; align-items:center; gap:0.5rem; margin-left:auto;">
            <a href="kundali-ganita.html" class="reader-nav-btn" title="सम्पूर्ण वेब संस्करण पढ़ें" style="background:#059669; color:#fff; padding:0.35rem 0.85rem; border-radius:6px; font-size:0.78rem; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.3rem;">🌐 वेब संस्करण</a>
            <a href="kundali-ganita-vichar-mahagranth.pdf" class="reader-nav-btn" download title="मास्टर PDF डाउनलोड करें" style="background:#0284c7; color:#fff; padding:0.35rem 0.85rem; border-radius:6px; font-size:0.78rem; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.3rem;">📥 मास्टर PDF</a>
            <a href="media/concept_animations/3d_ephemeris_simulation.html" target="_blank" class="reader-nav-btn" title="3D खगोलीय सिमुलेशन" style="background:rgba(255,255,255,0.12); color:#e2e8f0; border:1px solid #10b981; padding:0.35rem 0.85rem; border-radius:6px; font-size:0.78rem; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.3rem;">🌌 3D सिमुलेशन</a>
          </div>
    '''
    if '<button id="btn-toggle-sound"' in reader_top:
        reader_top = reader_top.replace('<button id="btn-toggle-sound"', custom_nav + '\n      <button id="btn-toggle-sound"')

    # Write out kundali-ganita-reader.html
    with open(OUTPUT_READER, "w", encoding="utf-8") as f:
        f.write(reader_top)
        for p in pages_list:
            f.write(p)
        f.write(reader_bot)

    print(f"✓ Created 3D Interactive Flipbook Reader: {OUTPUT_READER}")

    # 2. Build Massive Web Presentation Edition, Print Media Layout & Vector PDF
    sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
    from build_exhaustive_kundali_ganita_content import build_master_publications

    build_master_publications(
        output_web=OUTPUT_WEB,
        output_print=OUTPUT_PRINT,
        output_pdf=OUTPUT_PDF,
        output_reader=OUTPUT_READER,
        reader_src=READER_TEMPLATE_SRC,
        pages_list=pages_list
    )

    print("=" * 80)
    print("🎉 Flagship Vol 4 Exhaustive Generation Successfully Completed!")
    print("=" * 80)

if __name__ == "__main__":
    main()
