#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

ICONS_DIR = "/Users/apple/Movies/ap/TantraGyan/assets/icons"

# Chart 1: Deeptadi 9 States & Sun in 12 Houses Diamond Chart
def make_deeptadi_chart():
    width, height = 1000, 920
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:system-ui, -apple-system, 'Segoe UI', 'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047" /><stop offset="50%" stop-color="#d97706" /><stop offset="100%" stop-color="#92400e" />
    </linearGradient>
    <linearGradient id="sunGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" /><stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="#090d16" rx="12" />
  <rect x="15" y="15" width="{width-30}" height="{height-30}" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" rx="8" opacity="0.65" />

  <!-- Header -->
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">ग्रहों की दीप्तादि ९ अवस्थाएं एवं द्वादश भावों में सूर्य फल चक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">Deeptadi 9 Planetary Dignities &amp; Sun Across 12 Houses Diamond Chart (Kalyana Varma Saravali)</text>

  <!-- Diamond Kundli Layout: Center (500, 430), Size 520 -->
  <g transform="translate(240, 110)" filter="url(#shadow)">
    <rect x="0" y="0" width="520" height="520" fill="#0f172a" stroke="#d97706" stroke-width="2.5" />
    <line x1="0" y1="0" x2="520" y2="520" stroke="#d97706" stroke-width="2" />
    <line x1="520" y1="0" x2="0" y2="520" stroke="#d97706" stroke-width="2" />
    <polygon points="260,0 520,260 260,520 0,260" fill="#131c2e" stroke="#f59e0b" stroke-width="2" />

    <!-- Center H1: Surya in Lagna (Deepta / Swastha Focus) -->
    <polygon points="260,0 390,130 260,260 130,130" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2.2" />
    <text x="260" y="80" text-anchor="middle" fill="#fde047" font-size="20" font-weight="900">☀️ सूर्य (Surya) H1</text>
    <text x="260" y="105" text-anchor="middle" fill="#ffffff" font-size="13.5" font-weight="800">तनु भाव • आत्म-तेज</text>
    <text x="260" y="125" text-anchor="middle" fill="#38bdf8" font-size="12">दीप्त अवस्था (मेष 10° = 100%)</text>
    <text x="260" y="145" text-anchor="middle" fill="#cbd5e1" font-size="11">आरोग्य, नेतृत्व, स्वाभिमान</text>

    <!-- H2: Top-Left Triangle -->
    <polygon points="0,0 260,0 130,130" fill="rgba(245, 158, 11, 0.15)" stroke="#d97706" stroke-width="1.8" />
    <text x="130" y="45" text-anchor="middle" fill="#fde68a" font-size="15" font-weight="800">२. धन व कुटुंब</text>
    <text x="130" y="68" text-anchor="middle" fill="#e2e8f0" font-size="12">स्पष्ट वाणी, पैतृक लाभ</text>
    <text x="130" y="88" text-anchor="middle" fill="#94a3b8" font-size="11">नेत्र तेज, धन संचय</text>

    <!-- H12: Top-Right Triangle -->
    <polygon points="260,0 520,0 390,130" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1.8" />
    <text x="390" y="45" text-anchor="middle" fill="#fca5a5" font-size="15" font-weight="800">१२. व्यय व मोक्ष</text>
    <text x="390" y="68" text-anchor="middle" fill="#e2e8f0" font-size="12">विदेश प्रवास, एकांत</text>
    <text x="390" y="88" text-anchor="middle" fill="#94a3b8" font-size="11">आध्यात्मिक चेतना</text>

    <!-- H3: Left-Top Triangle -->
    <polygon points="0,0 130,130 0,260" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1.8" />
    <text x="50" y="120" text-anchor="middle" fill="#bae6fd" font-size="14" font-weight="800">३. पराक्रम</text>
    <text x="50" y="140" text-anchor="middle" fill="#e2e8f0" font-size="11.5">शत्रुजयी, शौर्य</text>

    <!-- H4: Left Diamond -->
    <polygon points="0,260 130,130 260,260 130,390" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4" stroke-width="1.8" />
    <text x="130" y="245" text-anchor="middle" fill="#67e8f9" font-size="16" font-weight="800">४. सुख व गृह</text>
    <text x="130" y="268" text-anchor="middle" fill="#e2e8f0" font-size="12">हृदय तेज, वाहन</text>
    <text x="130" y="288" text-anchor="middle" fill="#94a3b8" font-size="11">गृह से दूर भाग्योदय</text>

    <!-- H5: Left-Bottom Triangle -->
    <polygon points="0,260 130,390 0,520" fill="rgba(245, 158, 11, 0.18)" stroke="#f59e0b" stroke-width="1.8" />
    <text x="50" y="375" text-anchor="middle" fill="#fde68a" font-size="14" font-weight="800">५. बुद्धि व मंत्र</text>
    <text x="50" y="395" text-anchor="middle" fill="#e2e8f0" font-size="11.5">प्रज्ञा, मंत्रसिद्धि</text>

    <!-- H6: Bottom-Left Triangle -->
    <polygon points="0,520 260,520 130,390" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1.8" />
    <text x="130" y="475" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="800">६. शत्रुहंता (उपचय)</text>
    <text x="130" y="495" text-anchor="middle" fill="#e2e8f0" font-size="12">रोग व ऋण पर विजय</text>

    <!-- H7: Bottom Diamond -->
    <polygon points="260,260 390,390 260,520 130,390" fill="rgba(244, 63, 94, 0.18)" stroke="#f43f5e" stroke-width="2" />
    <text x="260" y="380" text-anchor="middle" fill="#fda4af" font-size="16" font-weight="800">७. जाया व साझेदारी</text>
    <text x="260" y="405" text-anchor="middle" fill="#ffffff" font-size="13">नीच स्थान (तुला 10° = खल अवस्था)</text>
    <text x="260" y="426" text-anchor="middle" fill="#cbd5e1" font-size="11.5">जीवनसाथी से मतभेद, लोकव्यवहार</text>

    <!-- H8: Bottom-Right Triangle -->
    <polygon points="260,520 520,520 390,390" fill="rgba(225, 29, 72, 0.15)" stroke="#e11d48" stroke-width="1.8" />
    <text x="390" y="475" text-anchor="middle" fill="#fda4af" font-size="15" font-weight="800">८. आयु व शोध</text>
    <text x="390" y="495" text-anchor="middle" fill="#e2e8f0" font-size="12">गूढ़ विद्या, दीर्घायु</text>

    <!-- H9: Right-Bottom Triangle -->
    <polygon points="520,260 390,390 520,520" fill="rgba(245, 158, 11, 0.18)" stroke="#f59e0b" stroke-width="1.8" />
    <text x="470" y="375" text-anchor="middle" fill="#fde68a" font-size="14" font-weight="800">९. भाग्य व धर्म</text>
    <text x="470" y="395" text-anchor="middle" fill="#e2e8f0" font-size="11.5">तीर्थ, पिता कीर्ति</text>

    <!-- H10: Right Diamond -->
    <polygon points="520,260 390,130 260,260 390,390" fill="rgba(245, 158, 11, 0.22)" stroke="#f59e0b" stroke-width="2" />
    <text x="390" y="245" text-anchor="middle" fill="#fde047" font-size="17" font-weight="900">१०. कर्म व पदवी</text>
    <text x="390" y="270" text-anchor="middle" fill="#ffffff" font-size="13">दिग्बल (Directional Strength)</text>
    <text x="390" y="290" text-anchor="middle" fill="#cbd5e1" font-size="11.5">सर्वोच्च राजसत्ता, ख्याति</text>

    <!-- H11: Right-Top Triangle -->
    <polygon points="520,0 390,130 520,260" fill="rgba(16, 185, 129, 0.18)" stroke="#10b981" stroke-width="1.8" />
    <text x="470" y="120" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="800">११. लाभ व सिद्धि</text>
    <text x="470" y="140" text-anchor="middle" fill="#e2e8f0" font-size="11.5">अखंड धन, प्रतिष्ठा</text>
  </g>

  <!-- Bottom Legend: 9 Deeptadi States Summary -->
  <g transform="translate(50, 670)" filter="url(#shadow)">
    <rect width="900" height="195" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.5" />
    <text x="30" y="30" fill="#fde047" font-size="15" font-weight="800">👑 ग्रहों की ९ दीप्तादि अवस्थाएं एवं फल की तीव्रता (Potency Scale):</text>

    <g transform="translate(30, 50)">
      <text x="0" y="20" fill="#34d399" font-size="13" font-weight="700">१. दीप्त (Deepta • उच्च): १००%</text>
      <text x="210" y="20" fill="#38bdf8" font-size="13" font-weight="700">२. स्वस्थ (Swastha • स्वराशि): ८५%</text>
      <text x="430" y="20" fill="#a7f3d0" font-size="13" font-weight="700">३. मुदित (Mudita • अधिमित्र): ७५%</text>
      <text x="650" y="20" fill="#fde68a" font-size="13" font-weight="700">४. शांत (Shanta • मित्र): ६०%</text>

      <text x="0" y="50" fill="#cbd5e1" font-size="13" font-weight="700">५. दीन (Deena • सम): ४०%</text>
      <text x="210" y="50" fill="#fbbf24" font-size="13" font-weight="700">६. दुखित (Dukhita • शत्रु): २५%</text>
      <text x="430" y="50" fill="#fca5a5" font-size="13" font-weight="700">७. विकल (Vikala • अस्त): १०%</text>
      <text x="650" y="50" fill="#f87171" font-size="13" font-weight="700">८. खल (Khala • नीच): ०–१५%</text>

      <text x="0" y="80" fill="#ef4444" font-size="13" font-weight="700">९. कोप (Kopa • युद्ध पराजित): अनिष्ट</text>
      <text x="210" y="80" fill="#cbd5e1" font-size="12">सूत्र: "दीप्तः स्वोच्चे स्वस्थः स्वगृहे मुदितोऽधिमित्रे शान्तः सुहृदि॥"</text>
    </g>

    <text x="30" y="165" fill="#94a3b8" font-size="12">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</text>
  </g>
</svg>'''
    with open(os.path.join(ICONS_DIR, "deeptadi_sun_diamond_chart.svg"), "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print("Generated deeptadi_sun_diamond_chart.svg")

# Chart 2: Navamsha D-9 & 108 Pada Diamond Chart
def make_navamsha_chart():
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
  <text x="{width/2}" y="52" text-anchor="middle" fill="url(#goldGrad)" font-size="24" font-weight="800">नवांश कुण्डली (D9) एवं १०८ नक्षत्र पद महाचक्र</text>
  <text x="{width/2}" y="78" text-anchor="middle" fill="#94a3b8" font-size="14">Navamsha Kundli (D-9) 108 Pada Architecture &amp; Vargottama Principles (Brihat Parasara)</text>

  <!-- Diamond Layout: Center (500, 420), Size 520 -->
  <g transform="translate(240, 110)" filter="url(#shadow)">
    <rect x="0" y="0" width="520" height="520" fill="#0f172a" stroke="#d97706" stroke-width="2.5" />
    <line x1="0" y1="0" x2="520" y2="520" stroke="#d97706" stroke-width="2" />
    <line x1="520" y1="0" x2="0" y2="520" stroke="#d97706" stroke-width="2" />
    <polygon points="260,0 520,260 260,520 0,260" fill="#131c2e" stroke="#f59e0b" stroke-width="2" />

    <!-- Center H1: D-9 Lagna (सूक्ष्म आत्मा) -->
    <polygon points="260,0 390,130 260,260 130,130" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2.2" />
    <text x="260" y="80" text-anchor="middle" fill="#fde047" font-size="20" font-weight="900">१. नवांश लग्न (D9 H1)</text>
    <text x="260" y="105" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">सूक्ष्म चेतना • आंतरिक सामर्थ्य</text>
    <text x="260" y="125" text-anchor="middle" fill="#38bdf8" font-size="12">वर्गोत्तम पद (D1 = D9)</text>
    <text x="260" y="145" text-anchor="middle" fill="#cbd5e1" font-size="11">जीवन के उत्तरार्ध का सत्य</text>

    <!-- H4: Left Diamond -->
    <polygon points="0,260 130,130 260,260 130,390" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4" stroke-width="1.8" />
    <text x="130" y="245" text-anchor="middle" fill="#67e8f9" font-size="16" font-weight="800">४. मानसिक शांति</text>
    <text x="130" y="268" text-anchor="middle" fill="#e2e8f0" font-size="12">गृह सुख, अंतःकरण</text>
    <text x="130" y="288" text-anchor="middle" fill="#94a3b8" font-size="11">नवांश चतुर्थेश की शक्ति</text>

    <!-- H7: Bottom Diamond -->
    <polygon points="260,260 390,390 260,520 130,390" fill="rgba(244, 114, 182, 0.18)" stroke="#ec4899" stroke-width="2" />
    <text x="260" y="380" text-anchor="middle" fill="#f472b6" font-size="17" font-weight="800">७. कलत्र एवं दांपत्य (D9 H7)</text>
    <text x="260" y="405" text-anchor="middle" fill="#ffffff" font-size="13">जीवनसाथी का वास्तविक स्वरूप व संस्कार</text>
    <text x="260" y="426" text-anchor="middle" fill="#cbd5e1" font-size="11.5">नवांश सप्तमेश से दांपत्य सुख का अंतिम निर्णय</text>

    <!-- H9: Right-Bottom Triangle -->
    <polygon points="520,260 390,390 520,520" fill="rgba(245, 158, 11, 0.18)" stroke="#f59e0b" stroke-width="1.8" />
    <text x="465" y="375" text-anchor="middle" fill="#fde68a" font-size="14" font-weight="800">९. भाग्य</text>
    <text x="465" y="398" text-anchor="middle" fill="#e2e8f0" font-size="11.5">धर्म व पूर्वपुण्य</text>

    <!-- H10: Right Diamond -->
    <polygon points="520,260 390,130 260,260 390,390" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2" />
    <text x="390" y="245" text-anchor="middle" fill="#fde047" font-size="17" font-weight="800">१०. कर्म की सत्यता</text>
    <text x="390" y="268" text-anchor="middle" fill="#ffffff" font-size="12.5">आजीविका का सूक्ष्म कारकत्व</text>
    <text x="390" y="288" text-anchor="middle" fill="#cbd5e1" font-size="11">D-10 (दशांश) का पूरक</text>
  </g>

  <!-- Bottom Legend: 3 Modality Rules & Vargottama -->
  <g transform="translate(50, 670)" filter="url(#shadow)">
    <rect width="900" height="195" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.5" />
    <text x="30" y="30" fill="#fde047" font-size="15" font-weight="800">📐 नवांश गणना के ३ मूलभूत नियम (The 3 Modality Algorithms):</text>

    <g transform="translate(30, 52)">
      <text x="0" y="20" fill="#38bdf8" font-size="13.5" font-weight="700">१. चर राशियां (Movable - १, ४, ७, १०):</text>
      <text x="270" y="20" fill="#e2e8f0" font-size="13">नवांश की गणना उसी राशि से प्रारंभ होती है (मेष ➔ मेष, कर्क ➔ कर्क)।</text>

      <text x="0" y="48" fill="#f59e0b" font-size="13.5" font-weight="700">२. स्थिर राशियां (Fixed - २, ५, ८, ११):</text>
      <text x="270" y="48" fill="#e2e8f0" font-size="13">नवांश की गणना उस राशि से ९वें स्थान से प्रारंभ होती है (वृषभ ➔ मकर, सिंह ➔ मेष)।</text>

      <text x="0" y="76" fill="#34d399" font-size="13.5" font-weight="700">३. द्विस्वभाव राशियां (Dual - ३, ६, ९, १२):</text>
      <text x="270" y="76" fill="#e2e8f0" font-size="13">नवांश की गणना उस राशि से ५वें स्थान से प्रारंभ होती है (मिथुन ➔ तुला, कन्या ➔ मकर)।</text>

      <text x="0" y="104" fill="#f472b6" font-size="13.5" font-weight="700">★ वर्गोत्तम अमृत नियम (Vargottama):</text>
      <text x="270" y="104" fill="#fde68a" font-size="13">यदि कोई ग्रह D1 व D9 में समान राशि में हो, तो वह उच्च ग्रह के समान राजसी फल देता है।</text>
    </g>

    <text x="30" y="172" fill="#94a3b8" font-size="12">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे • तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</text>
  </g>
</svg>'''
    with open(os.path.join(ICONS_DIR, "navamsha_diamond_chart.svg"), "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print("Generated navamsha_diamond_chart.svg")

if __name__ == "__main__":
    make_deeptadi_chart()
    make_navamsha_chart()
