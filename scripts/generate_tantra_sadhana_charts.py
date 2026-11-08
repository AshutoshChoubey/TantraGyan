#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the complete suite of 6 SACRED TANTRA SADHANA SVG Diagrams & Mandalas
for Tantra Sadhana Siddhi Mahagranth (41-Day Empirical Protocols).
Curated & Created by Jyotishacharya Ashutosh Kumar Choubey, Tantra Gyan.

Diagrams:
1. sadhana_altar_mandala.svg - Sacred Altar, Diya Dual Physics, Asana & Puja Sequence
2. sadhana_timeline_clock.svg - 8:30 PM to 10:40 PM Minute-by-Minute Sadhana Timeline Clock
3. sadhana_health_emergency_matrix.svg - 3-Tier Health Management, Emergency Recital & Vitamins
4. sadhana_samput_architecture.svg - Siddha Kunjika Samput & Vivaha Marriage Invocation Engine
5. sadhana_panchakshari_125k_wheel.svg - 41-Day 1,25,000 Japa Siddhi Mathematics & Pradosha Cycle
6. sadhana_lifestyle_disciplines_chart.svg - 6 Pillars of Tantric Austerity, Swara & Dream Journaling
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
    <linearGradient id="parchmentBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fffefb"/>
      <stop offset="50%" stop-color="#fdfbf5"/>
      <stop offset="100%" stop-color="#faf5ea"/>
    </linearGradient>
    <linearGradient id="goldHeadGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fef3c7"/>
      <stop offset="50%" stop-color="#fde68a"/>
      <stop offset="100%" stop-color="#fed7aa"/>
    </linearGradient>
    <linearGradient id="shivaBlueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#eff6ff"/>
      <stop offset="100%" stop-color="#dbeafe"/>
    </linearGradient>
    <linearGradient id="durgaRedGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef2f2"/>
      <stop offset="100%" stop-color="#fee2e2"/>
    </linearGradient>
    <linearGradient id="bhairavDarkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="tantraShadow" x="-3%" y="-3%" width="106%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#78350f" flood-opacity="0.08"/>
    </filter>
  </defs>
"""

def header_banner(title, sub, meta, height=66):
    return f"""
  <!-- Top Header Banner -->
  <rect x="20" y="16" width="520" height="{height}" rx="6" fill="#ffffff" stroke="#b45309" stroke-width="1.3"/>
  <text x="280" y="38" font-family="'Noto Serif Devanagari', 'Kohinoor Devanagari', Georgia, serif" font-size="14.5" font-weight="900" fill="#78350f" text-anchor="middle">{title}</text>
  <text x="280" y="55" font-family="'Kohinoor Devanagari', 'Noto Sans Devanagari', sans-serif" font-size="10.5" font-weight="700" fill="#b45309" text-anchor="middle">{sub}</text>
  <text x="280" y="70" font-family="'Kohinoor Devanagari', 'Noto Sans Devanagari', sans-serif" font-size="9" font-weight="600" fill="#78716c" text-anchor="middle">{meta}</text>
"""

# ==============================================================================
# 1. Altar Setup, Dual Diya Physics & Asana Mandala
# ==============================================================================
def make_altar_mandala():
    w, h = 560, 770
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#parchmentBg)" stroke="#b45309" stroke-width="2" filter="url(#tantraShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("तांत्रिक वेदी निर्माण, द्वैत दीप विज्ञान एवं 7-पद सामग्री क्रम", "Sacred Altar Architecture, Dual Diya Physics &amp; 7-Item Material Sequence", "दिशा: उत्तर या पूर्व मुखी • दक्षिण हस्त: घृत दीप • वाम हस्त: तैल दीप", 66)}

  <!-- Direction Compass Bar -->
  <g transform="translate(24, 94)">
    <rect width="512" height="32" rx="4" fill="#0f172a"/>
    <text x="256" y="21" fill="#fde047" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="800" text-anchor="middle">🧭 साधना मुख: उत्तर (North) अथवा पूर्व (East) दिशा</text>
  </g>

  <!-- Visual Altar Table -->
  <g transform="translate(24, 134)">
    <rect width="512" height="255" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.5"/>

    <!-- Altar Chowki Platform -->
    <rect x="25" y="20" width="462" height="130" rx="8" fill="#fdf2f8" stroke="#f43f5e" stroke-width="1.4"/>
    <rect x="25" y="20" width="462" height="24" rx="8" fill="#be185d"/>
    <text x="256" y="37" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" text-anchor="middle">लाल/पीत वस्त्र आच्छादित पवित्र काष्ठ चौकी (Sacred Altar Platform)</text>

    <!-- Center Deity / Yantra -->
    <circle cx="256" cy="90" r="34" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
    <text x="256" y="86" font-family="'Noto Serif Devanagari', serif" font-size="16" font-weight="900" fill="#78350f" text-anchor="middle">ॐ 卐 🔱</text>
    <text x="256" y="104" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="800" fill="#991b1b" text-anchor="middle">माँ दुर्गा / शिव प्रतिमा</text>

    <!-- Right Diya: Ghee (Deity's Right, Sadhak's Left Facing Altar) -->
    <g transform="translate(45, 60)">
      <rect width="110" height="75" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.3"/>
      <circle cx="55" cy="28" r="14" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>
      <text x="55" y="33" font-size="14" text-anchor="middle">🪔</text>
      <text x="55" y="55" font-family="'Noto Serif Devanagari', serif" font-size="10" font-weight="900" fill="#b45309" text-anchor="middle">शुद्ध घृत दीपक</text>
      <text x="55" y="68" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" font-weight="700" fill="#78350f" text-anchor="middle">(दाहिनी ओर - सत्व)</text>
    </g>

    <!-- Left Diya: Mustard Oil (Sarso) -->
    <g transform="translate(357, 60)">
      <rect width="110" height="75" rx="6" fill="#f1f5f9" stroke="#475569" stroke-width="1.3"/>
      <circle cx="55" cy="28" r="14" fill="#cbd5e1" stroke="#334155" stroke-width="1.5"/>
      <text x="55" y="33" font-size="14" text-anchor="middle">🪔</text>
      <text x="55" y="55" font-family="'Noto Serif Devanagari', serif" font-size="10" font-weight="900" fill="#0f172a" text-anchor="middle">सरसों तैल दीपक</text>
      <text x="55" y="68" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" font-weight="700" fill="#334155" text-anchor="middle">(बाईं ओर - भैरव रक्षा)</text>
    </g>

    <!-- Sadhak Asana Space -->
    <rect x="145" y="165" width="222" height="75" rx="8" fill="#fef3c7" stroke="#b45309" stroke-width="1.5" stroke-dasharray="4,2"/>
    <text x="256" y="190" font-family="'Noto Serif Devanagari', serif" font-size="12" font-weight="900" fill="#78350f" text-anchor="middle">साधक का कुशासन / ऊनी कम्बल आसन</text>
    <text x="256" y="208" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">रीढ़ सीधी • स्थिर सुखासन / सिद्धासन • मौन व्रत</text>
    <text x="256" y="224" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">आसन के नीचे आचमन जल विसर्जन मंत्र: ॐ शक्राय नमः। ॐ इन्द्राय नमः॥</text>
  </g>

  <!-- 7-Step Material Sequence Flow -->
  <g transform="translate(24, 398)">
    <rect width="512" height="110" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.4"/>
    <rect width="512" height="26" rx="8" fill="#065f46"/>
    <text x="256" y="18" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" text-anchor="middle">★ शास्त्रीय पूजा सामग्री अर्पण क्रम (7-Step Sacred Order) ★</text>

    <!-- 7 Step Pills -->
    <g transform="translate(14, 40)">
      <!-- 1 -->
      <rect x="0" y="0" width="62" height="50" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
      <text x="31" y="20" font-size="12" text-anchor="middle">💧</text>
      <text x="31" y="34" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="800" fill="#1d4ed8" text-anchor="middle">1. जल</text>
      <text x="31" y="44" font-size="7" fill="#64748b" text-anchor="middle">आचमन</text>

      <text x="66" y="28" font-weight="900" fill="#059669">➔</text>

      <!-- 2 -->
      <rect x="76" y="0" width="62" height="50" rx="6" fill="#fefce8" stroke="#eab308" stroke-width="1"/>
      <text x="107" y="20" font-size="12" text-anchor="middle">🌾</text>
      <text x="107" y="34" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="800" fill="#a16207" text-anchor="middle">2. अक्षत</text>
      <text x="107" y="44" font-size="7" fill="#64748b" text-anchor="middle">अखंडित</text>

      <text x="142" y="28" font-weight="900" fill="#059669">➔</text>

      <!-- 3 -->
      <rect x="152" y="0" width="62" height="50" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="1"/>
      <text x="183" y="20" font-size="12" text-anchor="middle">🪵</text>
      <text x="183" y="34" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="800" fill="#b91c1c" text-anchor="middle">3. चंदन</text>
      <text x="183" y="44" font-size="7" fill="#64748b" text-anchor="middle">रक्त/श्वेत</text>

      <text x="218" y="28" font-weight="900" fill="#059669">➔</text>

      <!-- 4 -->
      <rect x="228" y="0" width="62" height="50" rx="6" fill="#fdf2f8" stroke="#ec4899" stroke-width="1"/>
      <text x="259" y="20" font-size="12" text-anchor="middle">🌸</text>
      <text x="259" y="34" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="800" fill="#be185d" text-anchor="middle">4. इत्र</text>
      <text x="259" y="44" font-size="7" fill="#64748b" text-anchor="middle">सुगंध</text>

      <text x="294" y="28" font-weight="900" fill="#059669">➔</text>

      <!-- 5 -->
      <rect x="304" y="0" width="56" height="50" rx="6" fill="#f1f5f9" stroke="#64748b" stroke-width="1"/>
      <text x="332" y="20" font-size="12" text-anchor="middle">💨</text>
      <text x="332" y="34" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="800" fill="#334155" text-anchor="middle">5. धूप</text>
      <text x="332" y="44" font-size="7" fill="#64748b" text-anchor="middle">गुग्गुल</text>

      <text x="364" y="28" font-weight="900" fill="#059669">➔</text>

      <!-- 6 -->
      <rect x="374" y="0" width="56" height="50" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="1"/>
      <text x="402" y="20" font-size="12" text-anchor="middle">🔥</text>
      <text x="402" y="34" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="800" fill="#b45309" text-anchor="middle">6. दीप</text>
      <text x="402" y="44" font-size="7" fill="#64748b" text-anchor="middle">आरती</text>

      <text x="434" y="28" font-weight="900" fill="#059669">➔</text>

      <!-- 7 -->
      <rect x="444" y="0" width="46" height="50" rx="6" fill="#ecfdf5" stroke="#10b981" stroke-width="1"/>
      <text x="467" y="20" font-size="12" text-anchor="middle">🍯</text>
      <text x="467" y="34" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="800" fill="#047857" text-anchor="middle">7. प्रसाद</text>
      <text x="467" y="44" font-size="7" fill="#64748b" text-anchor="middle">नैवेद्य</text>
    </g>
  </g>

  <!-- Achamana Box -->
  <g transform="translate(24, 516)">
    <rect width="512" height="110" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.3"/>
    <text x="256" y="24" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="900" fill="#78350f" text-anchor="middle">✨ आचमन / याच्यापान विधि (3 बार जल ग्रहण) ✨</text>
    
    <text x="30" y="50" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309">1. ॐ केशवाय नमः</text>
    <text x="175" y="50" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" fill="#334155">➔ दाहिनी हथेली से प्रथम बार जल पान करें (काया शुद्धि)</text>

    <text x="30" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309">2. ॐ नारायणाय नमः</text>
    <text x="175" y="72" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" fill="#334155">➔ द्वितीय बार जल पान करें (प्राण शुद्धि)</text>

    <text x="30" y="94" font-family="'Kohinoor Devanagari', sans-serif" font-size="10" font-weight="700" fill="#b45309">3. ॐ माधवाय नमः</text>
    <text x="175" y="94" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" fill="#334155">➔ तृतीय बार जल पान करें (मन-बुद्धि शुद्धि) व हस्त प्रक्षालन करें</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="635" width="512" height="112" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="658" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ वेदी प्रतिष्ठा का तांत्रिक नियम ★</text>
  <text x="280" y="680" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• घृत दीपक सात्विक चेतना को आकर्षित करता है, सरसों तैल दीपक समस्त नकारात्मक शक्तियों से सुरक्षा करता है</text>
  <text x="280" y="700" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• 41 दिनों तक वेदी और आसन का स्थान कभी न बदलें; एक ही बिंदु पर ऊर्जा का संचय होता है</text>
  <text x="280" y="720" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: तंत्र साधना सिद्धि महाग्रंथ • प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""

# ==============================================================================
# 2. Sadhana Timeline Clock (8:30 PM - 10:40 PM Minute-by-Minute)
# ==============================================================================
def make_timeline_clock():
    w, h = 560, 770
    steps = [
        ("8:30 PM", "5 min", "वेदी तैयारी व दीप प्रज्वलन", "Diya placement &amp; materials ready", "#1e293b"),
        ("8:35 PM", "10 min", "संकल्प एवं पूर्वांग आह्वान", "Sacred vow, Achamana &amp; Invocations", "#b45309"),
        ("8:45 PM", "1 min", "ॐ नमः शिवाय (11 बार)", "11 recitations + 1 min Deep Breathing", "#0284c7"),
        ("8:47 PM", "1 min", "ॐ गं गणपतये नमः (11 बार)", "Ganesha protection + 1 min Deep Breathing", "#dc2626"),
        ("8:49 PM", "3 min", "बटुक भैरव रक्षा मंत्र (11 बार)", "आपदुद्धारणाय बटुकाय + 1 min Deep Breathing", "#4338ca"),
        ("8:53 PM", "3 min", "हरे कृष्ण महामंत्र (11 बार)", "Bhakti alignment + 1 min Deep Breathing", "#059669"),
        ("8:57 PM", "5 min", "श्री हनुमान चालीसा (1 पाठ)", "Complete recital + 1 min Deep Breathing", "#ea580c"),
        ("9:03 PM", "20 min", "श्री दुर्गा कवच (सम्पूर्ण पाठ)", "Complete Kavach + 1 min Deep Breathing", "#be185d"),
        ("9:24 PM", "3 min", "महामृत्युंजय मंत्र (11 बार)", "Mrityunjaya + 1 min Deep Breathing", "#047857"),
        ("9:28 PM", "65 min", "★ सिद्ध कुंजिका स्तोत्र (21 पाठ)", "CORE: Shiv Uvacha in 1st &amp; 21st only", "#b91c1c"),
        ("10:33 PM", "2 min", "क्षमा प्रार्थना (Forgiveness)", "अज्ञानाद्विस्मृतेर्भ्रान्त्या यन्न्यूनमधिकं कृतम्", "#475569"),
        ("10:35 PM", "5 min", "आरती एवं आसन उत्थापन", "Aarti, Asana water release &amp; Immediate Sleep", "#78350f"),
    ]

    cards_svg = []
    card_h = 42
    for idx, (t_start, dur, title, sub, col) in enumerate(steps):
        cy = 96 + idx * (card_h + 3)
        cards_svg.append(f"""
  <!-- Step {idx+1} -->
  <g transform="translate(24, {cy})">
    <rect width="512" height="{card_h}" rx="6" fill="#ffffff" stroke="{col}" stroke-width="1.2"/>
    <rect width="78" height="{card_h}" rx="6" fill="{col}"/>
    <text x="39" y="18" font-family="'Kohinoor Devanagari', sans-serif" font-size="10.5" font-weight="900" fill="#ffffff" text-anchor="middle">{t_start}</text>
    <text x="39" y="32" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="700" fill="#fde047" text-anchor="middle">({dur})</text>

    <text x="92" y="19" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="900" fill="{col}">{title}</text>
    <text x="92" y="33" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.8" font-weight="600" fill="#64748b">{sub}</text>

    <!-- Rest Pill -->
    <rect x="445" y="10" width="55" height="22" rx="4" fill="#f1f5f9"/>
    <text x="472" y="24" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" font-weight="700" fill="#334155" text-anchor="middle">विश्राम 1m</text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#parchmentBg)" stroke="#b45309" stroke-width="2" filter="url(#tantraShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("दैनिक साधना काल-तालिका (8:30 PM – 10:40 PM)", "Master Daily Sadhana Timeline Protocol • Minute-by-Minute Sequence", "प्रत्येक मंत्र के पश्चात 1 मिनट गहरा श्वास (Deep Breathing Rest) अनिवार्य", 66)}

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="642" width="512" height="105" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="664" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ साधना समाप्ति के उपरांत का अनिवार्य नियम ★</text>
  <text x="280" y="685" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• 10:40 PM पर आरती व क्षमा प्रार्थना के तुरंत बाद बिना किसी वार्तालाप या फोन के सीधे शयन करें</text>
  <text x="280" y="705" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• साधना में अर्जित ब्रह्मांडीय ऊर्जा निद्रा काल में सूक्ष्म शरीर (Astral Body) में संचित होती है</text>
  <text x="280" y="725" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: तंत्र साधना सिद्धि महाग्रंथ • प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""

# ==============================================================================
# 3. Health Emergency Matrix & Vitamin Support
# ==============================================================================
def make_health_emergency_matrix():
    w, h = 560, 770
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#parchmentBg)" stroke="#b45309" stroke-width="2" filter="url(#tantraShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("साधना काल में स्वास्थ्य प्रबंधन एवं आपातकालीन प्रोटोकॉल", "Sadhana Health Issue Management, Emergency Minimum &amp; Recovery Rules", "शरीरं खलु धर्मसाधनम् • स्वास्थ्य सुरक्षा के साथ साधना की अखंडता", 66)}

  <!-- 3-Tier Illness Protocol Table -->
  <g transform="translate(24, 96)">
    <rect width="512" height="235" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <rect width="512" height="28" rx="8" fill="#0f172a"/>
    <text x="256" y="19" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">१. त्रि-स्तरीय बीमारी प्रबंधन प्रोटोकॉल (3-Tier Health Matrix)</text>

    <!-- Tier 1: Minor -->
    <g transform="translate(14, 38)">
      <rect width="484" height="58" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.2"/>
      <text x="12" y="22" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#15803d">हल्की बीमारी (सर्दी, खांसी, हल्का बुखार)</text>
      <text x="12" y="40" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">➔ तुरंत घरेलू/चिकित्सीय उपचार लें; साधना को 100% जारी रखें।</text>
      <text x="12" y="52" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#047857">नियम: समय एवं स्थान में कोई समझौता न करें।</text>
    </g>

    <!-- Tier 2: Moderate -->
    <g transform="translate(14, 102)">
      <rect width="484" height="58" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="12" y="22" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#b45309">मध्यम समस्या (तीव्र दर्द, चक्कर, अधिक कमजोरी)</text>
      <text x="12" y="40" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">➔ चिकित्सक से परामर्श लें; दिन में कम से कम 1 पाठ उसी स्थान व समय पर करें।</text>
      <text x="12" y="52" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#78350f">आकस्मिक न्यूनतम: 10:00–10:15 PM पर 1 से 3 पाठ + क्षमा प्रार्थना।</text>
    </g>

    <!-- Tier 3: Emergency -->
    <g transform="translate(14, 166)">
      <rect width="484" height="58" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="1.2"/>
      <text x="12" y="22" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#b91c1c">गंभीर आपात स्थिति (अस्पताल भर्ती / जीवन रक्षा)</text>
      <text x="12" y="40" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">➔ साधना तुरंत रोकें; माँ भगवती से मानसिक क्षमा प्रार्थना करें।</text>
      <text x="12" y="52" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#991b1b">पुनर्प्राप्ति: स्वस्थ होते ही स्नान, नवीन संकल्प लेकर साधना पुनः प्रारंभ करें।</text>
    </g>
  </g>

  <!-- Vitamin & Health Nutrition Section -->
  <g transform="translate(24, 345)">
    <rect width="512" height="150" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.4"/>
    <rect width="512" height="28" rx="8" fill="#0369a1"/>
    <text x="256" y="19" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">२. तांत्रिक पोषण एवं विटामिन दिशानिर्देश (Nervous System Strength)</text>

    <g transform="translate(14, 38)">
      <rect width="150" height="98" rx="6" fill="#eff6ff" stroke="#93c5fd" stroke-width="1"/>
      <text x="75" y="24" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#1d4ed8" text-anchor="middle">B-Complex (B12)</text>
      <text x="75" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#1e293b" text-anchor="middle">मानसिक ऊर्जा एवं</text>
      <text x="75" y="62" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#1e293b" text-anchor="middle">तंत्रिका तंत्र (Nerves) को</text>
      <text x="75" y="76" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#1e293b" text-anchor="middle">सुदृढ़ बनाए रखता है।</text>
    </g>

    <g transform="translate(180, 38)">
      <rect width="150" height="98" rx="6" fill="#fffbeb" stroke="#fde047" stroke-width="1"/>
      <text x="75" y="24" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#b45309" text-anchor="middle">Vitamin D3</text>
      <text x="75" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#1e293b" text-anchor="middle">मूड स्टेबिलिटी, शांति एवं</text>
      <text x="75" y="62" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#1e293b" text-anchor="middle">गहरी सात्विक निद्रा</text>
      <text x="75" y="76" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#1e293b" text-anchor="middle">की गुणवत्ता सुनिश्चित करता है।</text>
    </g>

    <g transform="translate(346, 38)">
      <rect width="150" height="98" rx="6" fill="#fdf4ff" stroke="#f0abfc" stroke-width="1"/>
      <text x="75" y="24" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#a21caf" text-anchor="middle">Magnesium</text>
      <text x="75" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#1e293b" text-anchor="middle">मांसपेशियों का तनाव कम</text>
      <text x="75" y="62" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#1e293b" text-anchor="middle">करता है और 8 घंटे</text>
      <text x="75" y="76" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#1e293b" text-anchor="middle">भूमि शयन को सुगम बनाता है।</text>
    </g>
  </g>

  <!-- Women's Sadhana Guidelines Section -->
  <g transform="translate(24, 508)">
    <rect width="512" height="120" rx="8" fill="#ffffff" stroke="#be185d" stroke-width="1.4"/>
    <rect width="512" height="26" rx="8" fill="#9d174d"/>
    <text x="256" y="18" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" text-anchor="middle">३. महिला साधक विशेष नियम (Women’s Menstrual Protocol)</text>

    <text x="20" y="46" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#9d174d">• मासिक धर्म के दिन:</text>
    <text x="140" y="46" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">शारीरिक वेदी स्पर्श न करें; मानसिक रूप से केवल 1 पाठ करें व क्षमा प्रार्थना करें।</text>

    <text x="20" y="68" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#9d174d">• अन्य मंत्रों का निषेध:</text>
    <text x="140" y="68" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">मासिक धर्म के दिनों में केवल कुंजिका पाठ करें, अन्य उग्र मंत्रों का जाप न करें।</text>

    <text x="20" y="90" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#9d174d">• छूटे पाठों की भरपाई:</text>
    <text x="140" y="90" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">शुद्धि के उपरांत 5 दिनों के छूटे हुए पाठ 41 दिनों के बाद अतिरिक्त दिन जोड़कर पूर्ण करें।</text>

    <text x="256" y="110" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">माँ भगवती परम दयालु हैं; भाव-शुद्धि और निष्ठा ही तांत्रिक सिद्धि का वास्तविक आधार है।</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="640" width="512" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="662" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ तांत्रिक स्वास्थ्य दर्शन ★</text>
  <text x="280" y="682" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• बीमारी कभी-कभी संचित प्रारब्ध की कर्म-शुद्धि का साधन होती है</text>
  <text x="280" y="702" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• महामृत्युंजय मंत्र रोगमुक्ति देता है तथा बटुक भैरव साधना समस्त भय व विपत्तियों से रक्षा करती है</text>
  <text x="280" y="722" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: तंत्र साधना सिद्धि महाग्रंथ • प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""

# ==============================================================================
# 4. Siddha Kunjika Samput & Vivaha Marriage Invocation Engine
# ==============================================================================
def make_samput_architecture():
    w, h = 560, 770
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#parchmentBg)" stroke="#b45309" stroke-width="2" filter="url(#tantraShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("सिद्ध कुंजिका स्तोत्र संपुट विधान एवं विवाह सिद्धि चक्र", "Siddha Kunjika Samput Architecture &amp; Vivaha Blessing Engine", "संपुट श्लोक मंत्र के आदि और अंत में जुड़कर अभीष्ट फल को लाख गुना तीव्र करता है", 66)}

  <!-- Step-by-Step Samput Visual Flow -->
  <g transform="translate(24, 96)">
    <rect width="512" height="360" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <rect width="512" height="28" rx="8" fill="#0f172a"/>
    <text x="256" y="19" fill="#f8fafc" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">२१ पाठों में प्रत्येक पाठ का संपूर्ण संपुट चक्र (Full Cycle for Each Recital)</text>

    <!-- Part 1: Initial Samput Verse -->
    <g transform="translate(20, 38)">
      <rect width="472" height="60" rx="6" fill="#fdf2f8" stroke="#f43f5e" stroke-width="1.2"/>
      <text x="236" y="22" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#be185d" text-anchor="middle">१. आदि संपुट श्लोक (Opening Samput Verse)</text>
      <text x="236" y="40" font-family="'Noto Serif Devanagari', serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">“पत्नीं मनोरमां देहि मनोवृत्तानुसारिणीम् ।</text>
      <text x="236" y="54" font-family="'Noto Serif Devanagari', serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">तारिणीं दुर्गसंसारसागरस्य कुलोद्भवाम् ॥”</text>
    </g>

    <!-- Arrow Down -->
    <text x="256" y="112" font-size="14" font-weight="900" fill="#b45309" text-anchor="middle">⬇</text>

    <!-- Part 2: Core Ath Mantra (Navarna & Beeja Sparks) -->
    <g transform="translate(20, 118)">
      <rect width="472" height="75" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="1.4"/>
      <text x="236" y="20" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#b91c1c" text-anchor="middle">२. अथ मन्त्रः (Core Kunjika Navarna Beeja Mantras)</text>
      <text x="236" y="38" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="800" fill="#78350f" text-anchor="middle">ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे।</text>
      <text x="236" y="53" font-family="'Noto Serif Devanagari', serif" font-size="9" font-weight="700" fill="#1e293b" text-anchor="middle">ॐ ग्लौं हुं क्लीं जूं सः ज्वालय ज्वालय ज्वल ज्वल प्रज्वल प्रज्वल</text>
      <text x="236" y="68" font-family="'Noto Serif Devanagari', serif" font-size="9" font-weight="700" fill="#dc2626" text-anchor="middle">ऐं ह्रीं क्लीं चामुण्डायै विच्चे ज्वल हं सं लं क्षं फट् स्वाहा॥</text>
    </g>

    <!-- Arrow Down -->
    <text x="256" y="205" font-size="14" font-weight="900" fill="#b45309" text-anchor="middle">⬇</text>

    <!-- Part 3: Iti Mantra & Stotra Verses -->
    <g transform="translate(20, 212)">
      <rect width="472" height="60" rx="6" fill="#fefce8" stroke="#ca8a04" stroke-width="1.2"/>
      <text x="236" y="20" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#854d0e" text-anchor="middle">३. इति मन्त्रः (स्तवन एवं बीज स्तुति - श्लोक 5 से 11)</text>
      <text x="236" y="38" font-family="'Noto Serif Devanagari', serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">नमस्ते रुद्ररूपिण्यै... ऐङ्कारी सृष्टिरूपायै... धां धीं धूं धूर्जटेः पत्नी...</text>
      <text x="236" y="52" font-family="'Noto Serif Devanagari', serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">पां पीं पूं पार्वती पूर्णा... सां सीं सूं सप्तशती देव्या मंत्रसिद्धिं कुरूष्व मे॥</text>
    </g>

    <!-- Arrow Down -->
    <text x="256" y="284" font-size="14" font-weight="900" fill="#b45309" text-anchor="middle">⬇</text>

    <!-- Part 4: Closing Samput Verse -->
    <g transform="translate(20, 290)">
      <rect width="472" height="60" rx="6" fill="#fdf2f8" stroke="#f43f5e" stroke-width="1.2"/>
      <text x="236" y="22" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="#be185d" text-anchor="middle">४. अंत संपुट श्लोक (Closing Samput Verse)</text>
      <text x="236" y="40" font-family="'Noto Serif Devanagari', serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">“पत्नीं मनोरमां देहि मनोवृत्तानुसारिणीम् ।</text>
      <text x="236" y="54" font-family="'Noto Serif Devanagari', serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">तारिणीं दुर्गसंसारसागरस्य कुलोद्भवाम् ॥”</text>
    </g>
  </g>

  <!-- Marriage Sankalpa Focus Box -->
  <g transform="translate(24, 468)">
    <rect width="512" height="160" rx="8" fill="#ffffff" stroke="#e11d48" stroke-width="1.4"/>
    <rect width="512" height="26" rx="8" fill="#9f1239"/>
    <text x="256" y="18" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" text-anchor="middle">★ शीघ्र विवाह एवं सुयोग्य जीवनसाथी संकल्प सूत्र (Marriage Siddhi Sankalpa) ★</text>

    <text x="20" y="46" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#9f1239">उद्देश्य:</text>
    <text x="65" y="46" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">माँ भगवती की कृपा से शीघ्र, अनुकूल, सुलक्षणा एवं धर्मपरायण जीवनसाथी की प्राप्ति।</text>

    <text x="20" y="68" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#9f1239">अवधि विकल्प:</text>
    <text x="100" y="68" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">२१ पाठ नित्य • ७ दिन का लघु अनुष्ठान अथवा ४१ दिन का पूर्ण महा-अनुष्ठान।</text>

    <text x="20" y="90" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#9f1239">शिव उवाच नियम:</text>
    <text x="115" y="90" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">‘शिव उवाच’ एवं ‘फलश्रुति’ केवल प्रथम (1st) व अंतिम (21st) पाठ में ही पढ़ें।</text>

    <text x="20" y="112" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#9f1239">मध्यवर्ती १९ पाठ:</text>
    <text x="115" y="112" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">पाठ २ से २० तक केवल संपुट + अथ मन्त्र + इति मन्त्र + संपुट का आवर्तन करें।</text>

    <rect x="15" y="125" width="482" height="26" rx="4" fill="#fff1f2"/>
    <text x="256" y="142" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.8" font-weight="700" fill="#be185d" text-anchor="middle">आसन उत्थापन: पाठोपरांत ॐ शक्राय नमः। ॐ इन्द्राय नमः बोलकर जल माथे पर लगाएं।</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="638" width="512" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="660" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ संपुट साधना का गोपनीय तंत्र विज्ञान ★</text>
  <text x="280" y="680" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• जैसे दोनों ओर से ढक्कन बंद करने पर पात्र में रखी वस्तु सुरक्षित रहती है, वैसे ही संपुट से मंत्र-ऊर्जा बंधी रहती है</text>
  <text x="280" y="700" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• यह प्रयोग वैवाहिक बाधा, मांगलिक दोष एवं विवाह में अनावश्यक विलंब का शत-प्रतिशत निवारण करता है</text>
  <text x="280" y="720" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: तंत्र साधना सिद्धि महाग्रंथ • प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""

# ==============================================================================
# 5. 41-Day Panchakshari 1,25,000 Japa Siddhi Wheel
# ==============================================================================
def make_panchakshari_wheel():
    w, h = 560, 770
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#parchmentBg)" stroke="#b45309" stroke-width="2" filter="url(#tantraShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("४१-दिवसीय पंचाक्षरी महासाधना एवं १,२५,००० जप सिद्धि चक्र", "41-Day Panchakshari Sadhana (Om Namah Shivaya) 125,000 Japa Siddhi", "४१ दिनों में सवा लाख जप सिद्ध कर शिव कृपा, आत्म-शुद्धि व तांत्रिक अधिकार की प्राप्ति", 66)}

  <!-- Mathematical Breakdown Grid -->
  <g transform="translate(24, 96)">
    <rect width="512" height="155" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.4"/>
    <rect width="512" height="28" rx="8" fill="#0369a1"/>
    <text x="256" y="19" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">★ सवा लाख (1,25,000) जप का सटीक गणितीय विभाजन ★</text>

    <!-- 4 Stats Cards -->
    <g transform="translate(14, 38)">
      <!-- Card 1 -->
      <rect x="0" y="0" width="112" height="70" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
      <text x="56" y="24" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900" fill="#1d4ed8" text-anchor="middle">1,25,000</text>
      <text x="56" y="44" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#1e293b" text-anchor="middle">कुल जप संख्या</text>
      <text x="56" y="58" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" fill="#64748b" text-anchor="middle">(सवा लाख अनुष्ठान)</text>

      <!-- Card 2 -->
      <rect x="124" y="0" width="112" height="70" rx="6" fill="#fefce8" stroke="#ca8a04" stroke-width="1.2"/>
      <text x="180" y="24" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900" fill="#a16207" text-anchor="middle">41 दिन</text>
      <text x="180" y="44" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#1e293b" text-anchor="middle">कुल समयावधि</text>
      <text x="180" y="58" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" fill="#64748b" text-anchor="middle">(एक मंडल काल)</text>

      <!-- Card 3 -->
      <rect x="248" y="0" width="112" height="70" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/>
      <text x="304" y="24" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900" fill="#15803d" text-anchor="middle">3,049 जप</text>
      <text x="304" y="44" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#1e293b" text-anchor="middle">प्रतिदिन जप संख्या</text>
      <text x="304" y="58" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" fill="#64748b" text-anchor="middle">(Daily Target)</text>

      <!-- Card 4 -->
      <rect x="372" y="0" width="112" height="70" rx="6" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/>
      <text x="428" y="24" font-family="'Noto Serif Devanagari', serif" font-size="14" font-weight="900" fill="#be185d" text-anchor="middle">28–31 माला</text>
      <text x="428" y="44" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="700" fill="#1e293b" text-anchor="middle">प्रतिदिन माला गणना</text>
      <text x="428" y="58" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" fill="#64748b" text-anchor="middle">(रुद्राक्ष माला 108)</text>
    </g>

    <text x="256" y="135" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#0369a1" text-anchor="middle">सूत्र: 3,049 मंत्र प्रति दिन × 41 दिन = 1,25,009 मंत्र (सवा लाख जप पूर्ण)</text>
    <text x="256" y="148" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">समय: प्रातः अथवा संध्या काल में 2 से 2.5 घंटे का एकनिष्ठ अभ्यास।</text>
  </g>

  <!-- Commencement & Protocol Rules -->
  <g transform="translate(24, 260)">
    <rect width="512" height="235" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.4"/>
    <rect width="512" height="28" rx="8" fill="#78350f"/>
    <text x="256" y="19" fill="#fde047" font-family="'Noto Serif Devanagari', serif" font-size="11.5" font-weight="800" text-anchor="middle">साधना के ५ अनिवार्य चरण (5 Sacred Protocol Milestones)</text>

    <!-- Phase 1 -->
    <g transform="translate(14, 38)">
      <rect width="484" height="34" rx="4" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
      <text x="12" y="22" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#b45309">१. शुभारम्भ तिथि:</text>
      <text x="110" y="22" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">अत्यंत शुभ: कृष्ण पक्ष त्रयोदशी (प्रदोष) • विकल्प: सोमवार या शुक्ल प्रदोष।</text>
    </g>

    <!-- Phase 2 -->
    <g transform="translate(14, 76)">
      <rect width="484" height="34" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
      <text x="12" y="22" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#1d4ed8">२. संकल्प विधान:</text>
      <text x="110" y="22" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">हाथ में जल, अक्षत लेकर नाम, गोत्र, स्थान बोलकर 41 दिन का संकल्प लें।</text>
    </g>

    <!-- Phase 3 -->
    <g transform="translate(14, 114)">
      <rect width="484" height="34" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1"/>
      <text x="12" y="22" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#15803d">३. नित्य पंचोपचार:</text>
      <text x="115" y="22" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">धूप, दीप, जल, श्वेत चंदन, नैवेद्य एवं 'ॐ नमः शिवाय' बोलकर विल्वपत्र अर्पण।</text>
    </g>

    <!-- Phase 4 -->
    <g transform="translate(14, 152)">
      <rect width="484" height="34" rx="4" fill="#fdf2f8" stroke="#ec4899" stroke-width="1"/>
      <text x="12" y="22" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#be185d">४. जप व माला नियम:</text>
      <text x="125" y="22" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">रुद्राक्ष माला को गोमुखी में रखकर अनामिका-अंगुष्ठ से फेरें, सुमेरु न लांघें।</text>
    </g>

    <!-- Phase 5 -->
    <g transform="translate(14, 190)">
      <rect width="484" height="34" rx="4" fill="#faf5ff" stroke="#a855f7" stroke-width="1"/>
      <text x="12" y="22" font-family="'Noto Serif Devanagari', serif" font-size="10.5" font-weight="900" fill="#7e22ce">५. ४१वें दिन समापन:</text>
      <text x="125" y="22" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">108 आहुति दशांश हवन, मंदिर में प्रसाद वितरण व ताम्र-पात्र में मंत्र स्थापन।</text>
    </g>
  </g>

  <!-- Benefits & Spiritual Fruit -->
  <g transform="translate(24, 504)">
    <rect width="512" height="124" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.4"/>
    <rect width="512" height="26" rx="8" fill="#065f46"/>
    <text x="256" y="18" fill="#ffffff" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" text-anchor="middle">★ सवा लाख पंचाक्षरी सिद्धि के अलौकिक फल ★</text>

    <text x="25" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#047857">• कुंडलिनी चेतना जागृति:</text>
    <text x="160" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">मूलाधार से सहस्रार तक ऊर्जा का उर्ध्वगमन एवं चित्त की अखंड एकाग्रता।</text>

    <text x="25" y="70" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#047857">• तांत्रिक साधना अधिकार:</text>
    <text x="160" y="70" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">पंचाक्षरी सिद्ध होने पर साधक अन्य उच्च महाविद्या साधनाओं का स्वाभाविक पात्र बनता है।</text>

    <text x="25" y="92" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#047857">• अकाल मृत्यु व रोग निवारण:</text>
    <text x="160" y="92" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">महादेव का अभय कवच साधक को समस्त व्याधियों एवं संकटों से मुक्त करता है।</text>

    <text x="256" y="112" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">॥ नमस्तस्मै मुनीन्द्राय भृगवे ज्ञानरूपिणे । नमामि ज्ञानदातारं शिवसंकल्पसिद्धिदम् ॥</text>
  </g>

  <!-- Bottom Legend Footer -->
  <rect x="24" y="638" width="512" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="660" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ पंचाक्षरी सिद्धि का मूल रहस्य ★</text>
  <text x="280" y="682" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• 'ॐ नमः शिवाय' पंचभूतों (पृथ्वी, जल, अग्नि, वायु, आकाश) को वश में करने वाला महामंत्र है</text>
  <text x="280" y="702" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• जब सवा लाख जप पूर्ण होता है, तो साधक का प्रत्येक श्वास स्वतः जप रूप बन जाता है</text>
  <text x="280" y="722" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: तंत्र साधना सिद्धि महाग्रंथ • प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""

# ==============================================================================
# 6. Six Pillars of Tantric Austerity, Swara & Dream Journaling
# ==============================================================================
def make_lifestyle_disciplines_chart():
    w, h = 560, 770
    disciplines = [
        ("१. ब्रह्मचर्य (Complete Celibacy)", "कायिक, मानसिक व दृश्य ब्रह्मचर्य। कामुक विचारों, रोमांस व उत्तेजक दृश्यों से पूर्ण विरक्ति।", "#991b1b", "#fef2f2"),
        ("२. सात्विक आहार (Sattvic Food)", "लहसुन, प्याज, मांसाहार, मद्य, तंबाकू पूर्ण वर्जित। ३ घंटे से अधिक पुराना भोजन न लें।", "#15803d", "#f0fdf4"),
        ("३. मौन एवं वाणी संयम (Mauna)", "केवल अनिवार्य व्यावसायिक संवाद। फोन दूसरे कमरे में रखें; सोशल मीडिया, संगीत, फिल्म वर्जित।", "#1d4ed8", "#eff6ff"),
        ("४. भूमि शयन (Ground Sleeping)", "४१ दिनों तक शुद्ध चटाई व स्वच्छ चादर पर फर्श पर शयन अनिवार्य। रीढ़ सीधी रखें।", "#b45309", "#fffbeb"),
        ("५. प्रातः प्राणायाम (Pranayama)", "प्रातः 7:30–8:00 AM: कपालभाति (10 मिनट) एवं अनुलोम-विलोम (10 मिनट) तंत्रिका शुद्धि हेतु।", "#047857", "#ecfdf5"),
        ("६. स्वप्न-स्वर विज्ञान (Dream &amp; Swara)", "जागते ही स्वप्न डायरी में लिखें। जागते समय कौन सा नथुना (स्वर: इड़ा/पिंगला) सक्रिय था, नोट करें।", "#6d28d9", "#faf5ff"),
    ]

    cards_svg = []
    card_w, card_h = 250, 160
    for i, (title, desc, accent, bg) in enumerate(disciplines):
        col = i % 2
        row = i // 2
        cx = 24 + col * (card_w + 12)
        cy = 96 + row * (card_h + 10)

        cards_svg.append(f"""
  <!-- Discipline Card {i+1} -->
  <g transform="translate({cx}, {cy})">
    <rect width="{card_w}" height="{card_h}" rx="8" fill="#ffffff" stroke="{accent}" stroke-width="1.3"/>
    <rect width="{card_w}" height="28" rx="8" fill="{bg}"/>
    <line x1="0" y1="28" x2="{card_w}" y2="28" stroke="{accent}" stroke-width="0.8"/>

    <text x="12" y="19" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="900" fill="{accent}">{title}</text>

    <text x="12" y="48" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">{desc[:38]}</text>
    <text x="12" y="65" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">{desc[38:76]}</text>
    <text x="12" y="82" font-family="'Kohinoor Devanagari', sans-serif" font-size="9" font-weight="600" fill="#1e293b">{desc[76:115]}</text>

    <!-- Specific Golden Tip -->
    <rect x="8" y="105" width="{card_w - 16}" height="44" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
    <text x="{card_w/2}" y="122" font-family="'Kohinoor Devanagari', sans-serif" font-size="8" font-weight="700" fill="#b45309" text-anchor="middle">★ ४१-दिवसीय यम-नियम साधना स्तम्भ ★</text>
    <text x="{card_w/2}" y="138" font-family="'Kohinoor Devanagari', sans-serif" font-size="7.8" font-weight="600" fill="#64748b" text-anchor="middle">ऊर्जा को क्षय होने से बचाकर सहस्रार में संचित करना</text>
  </g>""")

    cards_str = "\n".join(cards_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
{COMMON_DEFS}
  <rect x="6" y="6" width="548" height="{h-12}" rx="12" fill="url(#parchmentBg)" stroke="#b45309" stroke-width="2" filter="url(#tantraShadow)"/>
  <rect x="12" y="12" width="536" height="{h-24}" rx="8" fill="none" stroke="#d97706" stroke-width="0.8" stroke-dasharray="6,3" opacity="0.6"/>

  {header_banner("षड्विध तांत्रिक यम-नियम, प्राणायाम एवं स्वप्न-स्वर विज्ञान", "Six Pillars of Tantric Austerity, Morning Pranayama &amp; Swara-Dream Science", "मन, वचन, कर्म व आहार की पूर्ण शुद्धि से ही मंत्र चैतन्य और जागृत होता है", 66)}

  {cards_str}

  <!-- Bottom Legend Footer -->
  <rect x="24" y="622" width="512" height="126" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="644" font-family="'Noto Serif Devanagari', serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">★ स्वप्न एवं स्वर विज्ञान का गोपनीय उपयोग ★</text>
  <text x="280" y="665" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#1e293b" text-anchor="middle">• साधना काल में आने वाले स्वप्न साधक की आंतरिक शुद्धि व देव-संकेत का दर्पण होते हैं</text>
  <text x="280" y="685" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">• यदि प्रातः जागते ही बायां स्वर (इड़ा) चले तो दिन में ज्ञान-साधना, दायां (पिंगला) चले तो कर्म-साधना फलीभूत होती है</text>
  <text x="280" y="705" font-family="'Kohinoor Devanagari', sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">• इन ६ नियमों का पालन करने पर ४१वें दिन साधक के आभा-मंडल (Aura) में दिव्य प्रकाश प्रगट होता है</text>
  <text x="280" y="724" font-family="'Kohinoor Devanagari', sans-serif" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">स्रोत: तंत्र साधना सिद्धि महाग्रंथ • प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</text>
</svg>"""

def main():
    print("🚀 Generating 6 Sacred Tantra Sadhana SVG Diagrams & Mandalas...")
    write_and_verify("sadhana_altar_mandala.svg", make_altar_mandala())
    write_and_verify("sadhana_timeline_clock.svg", make_timeline_clock())
    write_and_verify("sadhana_health_emergency_matrix.svg", make_health_emergency_matrix())
    write_and_verify("sadhana_samput_architecture.svg", make_samput_architecture())
    write_and_verify("sadhana_panchakshari_125k_wheel.svg", make_panchakshari_wheel())
    write_and_verify("sadhana_lifestyle_disciplines_chart.svg", make_lifestyle_disciplines_chart())
    print("🎉 All 6 Tantra Sadhana diagrams generated and validated 100% XML compliant!")

if __name__ == "__main__":
    main()
