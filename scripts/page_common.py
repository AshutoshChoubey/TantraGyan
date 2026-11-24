#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Common page components and SVG visual generators for the 108-page Vedic Kundali Ganita Vichar Mahagranth.
Tantra Gyan Research Center • https://t.worldgyan.com
"""

def make_page(page_num: int, chapter: str, title: str, content: str) -> str:
    """Wraps page content in standard reader.html article format."""
    return f'''    <article class="book-page-data" id="page-data-{page_num}" data-page="{page_num}" data-chapter="{chapter}" data-title="{title}">
      <div class="page-inner" style="padding: 1.6rem 1.4rem; font-family: 'Noto Sans Devanagari', -apple-system, sans-serif; line-height: 1.65; color: #1e293b;">
        <div class="page-header" style="display:flex; justify-content:space-between; align-items:center; border-bottom:1.5px solid #d4af37; padding-bottom:0.4rem; margin-bottom:0.9rem;">
          <span style="font-size:0.75rem; font-weight:800; color:#059669; letter-spacing:0.04em; text-transform:uppercase;">{chapter}</span>
          <span style="font-size:0.75rem; font-weight:700; color:#b45309; background:rgba(212,175,55,0.15); padding:0.15rem 0.55rem; border-radius:4px;">पृष्ठ {page_num} / १०८</span>
        </div>
        <h2 style="font-size:1.15rem; font-weight:800; color:#0f172a; margin-top:0; margin-bottom:0.8rem; border-left:4px solid #10b981; padding-left:0.6rem; line-height:1.35;">{title}</h2>
        <div class="page-body-flow" style="font-size:0.875rem; color:#334155;">
{content}
        </div>
        <div class="page-footer" style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:0.4rem; margin-top:1rem; font-size:0.7rem; color:#64748b;">
          <span>वैदिक कुण्डली विचार एवं गणित महाग्रंथ • तंत्र ज्ञान शोध संस्थान</span>
          <span>t.worldgyan.com</span>
        </div>
      </div>
    </article>
'''

def get_diamond_chart_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 480" width="100%" height="220" style="max-width:320px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px;">
  <defs>
    <linearGradient id="gGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c89d3d" />
      <stop offset="100%" stop-color="#10b981" />
    </linearGradient>
  </defs>
  <rect width="600" height="480" fill="#090d16" rx="8" />
  <rect x="50" y="40" width="500" height="400" fill="none" stroke="#2a334a" stroke-width="2" />
  <line x1="50" y1="40" x2="550" y2="440" stroke="#2a334a" stroke-width="2" />
  <line x1="550" y1="40" x2="50" y2="440" stroke="#2a334a" stroke-width="2" />
  <polygon points="300,40 550,240 300,440 50,240" fill="none" stroke="url(#gGold)" stroke-width="2.5" />
  <text x="300" y="140" fill="#38bdf8" font-size="20" font-weight="bold" text-anchor="middle">१ (लग्न)</text>
  <text x="180" y="85" fill="#cbd5e1" font-size="16" text-anchor="middle">२</text>
  <text x="100" y="140" fill="#cbd5e1" font-size="16" text-anchor="middle">३</text>
  <text x="170" y="240" fill="#cbd5e1" font-size="18" font-weight="bold" text-anchor="middle">४ (सुख)</text>
  <text x="100" y="340" fill="#cbd5e1" font-size="16" text-anchor="middle">५</text>
  <text x="180" y="400" fill="#cbd5e1" font-size="16" text-anchor="middle">६</text>
  <text x="300" y="350" fill="#cbd5e1" font-size="18" font-weight="bold" text-anchor="middle">७ (जाया)</text>
  <text x="420" y="400" fill="#cbd5e1" font-size="16" text-anchor="middle">८</text>
  <text x="500" y="340" fill="#cbd5e1" font-size="16" text-anchor="middle">९</text>
  <text x="430" y="240" fill="#cbd5e1" font-size="18" font-weight="bold" text-anchor="middle">१० (कर्म)</text>
  <text x="500" y="140" fill="#cbd5e1" font-size="16" text-anchor="middle">११</text>
  <text x="420" y="85" fill="#cbd5e1" font-size="16" text-anchor="middle">१२</text>
</svg>'''

def get_circular_zodiac_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="100%" height="210" style="max-width:320px; margin:0.5rem auto; display:block; background:#0b101b; border-radius:8px;">
  <circle cx="250" cy="200" r="180" fill="none" stroke="#1e293b" stroke-width="2" />
  <circle cx="250" cy="200" r="140" fill="none" stroke="#d4af37" stroke-width="2" stroke-dasharray="4,4" />
  <circle cx="250" cy="200" r="90" fill="#0f172a" stroke="#10b981" stroke-width="2" />
  <text x="250" y="195" fill="#f8fafc" font-size="15" font-weight="bold" text-anchor="middle">कालचक्र</text>
  <text x="250" y="215" fill="#38bdf8" font-size="11" text-anchor="middle">३६०° भचक्र (१२ राशियाँ)</text>
  <text x="250" y="35" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">मेष ०°</text>
  <text x="420" y="205" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">कर्क ९०°</text>
  <text x="250" y="375" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">तुला १८०°</text>
  <text x="80" y="205" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">मकर २७०°</text>
</svg>'''

def get_ayanamsha_shift_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="28" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">सायन (Tropical) बनाम निरयण (Sidereal) अयनांश विस्थापन</text>
  <!-- Sayana track -->
  <line x1="60" y1="80" x2="540" y2="80" stroke="#64748b" stroke-width="4" stroke-linecap="round" />
  <circle cx="120" cy="80" r="7" fill="#ef4444" />
  <text x="120" y="65" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">सायन वसंत विषुव (०°)</text>
  <!-- Nirayana track -->
  <line x1="60" y1="160" x2="540" y2="160" stroke="#10b981" stroke-width="4" stroke-linecap="round" />
  <circle cx="210" cy="160" r="7" fill="#10b981" />
  <text x="210" y="195" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">निरयण मेषारंभ (रेवती तारा)</text>
  <!-- Ayanamsha gap -->
  <line x1="120" y1="80" x2="120" y2="160" stroke="#d4af37" stroke-width="1.5" stroke-dasharray="3,3" />
  <line x1="210" y1="80" x2="210" y2="160" stroke="#d4af37" stroke-width="1.5" stroke-dasharray="3,3" />
  <rect x="125" y="105" width="80" height="30" fill="rgba(212,175,55,0.2)" rx="4" stroke="#d4af37" />
  <text x="165" y="125" fill="#facc15" font-size="12" font-weight="bold" text-anchor="middle">अयनांश २३° ५१'</text>
  <text x="300" y="225" fill="#94a3b8" font-size="10.5" text-anchor="middle">निरयण ग्रह = सायन ग्रह - २४° (लाहिड़ी अयनांश अंतर)</text>
</svg>'''

def get_lagna_horizon_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="28" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">लग्न साधन: पूर्वी क्षितिज एवं क्रांतिवृत्त का संगम बिंदु</text>
  <!-- Earth Horizon -->
  <line x1="50" y1="140" x2="550" y2="140" stroke="#059669" stroke-width="3" />
  <text x="90" y="130" fill="#34d399" font-size="11" font-weight="bold">पूर्वी क्षितिज (Eastern Horizon)</text>
  <text x="500" y="130" fill="#94a3b8" font-size="11">पश्चिम क्षितिज</text>
  <!-- Ecliptic arc -->
  <path d="M 60,190 Q 300,40 540,190" fill="none" stroke="#f59e0b" stroke-width="3" />
  <text x="470" y="80" fill="#f59e0b" font-size="11" font-weight="bold">क्रांतिवृत्त (Ecliptic)</text>
  <!-- Intersection: Lagna -->
  <circle cx="165" cy="140" r="8" fill="#ef4444" stroke="#fff" stroke-width="2" />
  <text x="165" y="170" fill="#f87171" font-size="13" font-weight="bold" text-anchor="middle">★ लग्न (Ascendant)</text>
  <rect x="230" y="175" width="310" height="45" fill="rgba(255,255,255,0.06)" rx="6" />
  <text x="385" y="194" fill="#cbd5e1" font-size="10.5" text-anchor="middle">जन्म समय पूर्व दिशा में जो राशि उदित हो रही थी,</text>
  <text x="385" y="210" fill="#38bdf8" font-size="10.5" font-weight="bold" text-anchor="middle">वही प्रथम भाव (लग्न) बनती है (जातक 'क': कन्या लग्न)</text>
</svg>'''

def get_panchanga_star_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 250" width="100%" height="190" style="max-width:440px; margin:0.5rem auto; display:block; background:#0b1329; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">पंचांग के ५ दिव्य अंग एवं ५ महाभूत तत्व</text>
  <!-- 5 Nodes in a row -->
  <!-- Tithi -->
  <rect x="30" y="60" width="95" height="110" fill="#0284c7" rx="8" />
  <text x="77" y="85" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">१. तिथि</text>
  <text x="77" y="110" fill="#e0f2fe" font-size="11" text-anchor="middle">जल तत्व</text>
  <text x="77" y="130" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">शुक्र</text>
  <text x="77" y="155" fill="#e0f2fe" font-size="9.5" text-anchor="middle">मानसिक तृप्ति</text>

  <!-- Vaara -->
  <rect x="140" y="60" width="95" height="110" fill="#dc2626" rx="8" />
  <text x="187" y="85" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">२. वार</text>
  <text x="187" y="110" fill="#fee2e2" font-size="11" text-anchor="middle">अग्नि तत्व</text>
  <text x="187" y="130" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">मंगल</text>
  <text x="187" y="155" fill="#fee2e2" font-size="9.5" text-anchor="middle">शारीरिक तेज</text>

  <!-- Nakshatra -->
  <rect x="250" y="60" width="100" height="110" fill="#059669" rx="8" />
  <text x="300" y="85" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">३. नक्षत्र</text>
  <text x="300" y="110" fill="#d1fae5" font-size="11" text-anchor="middle">वायु तत्व</text>
  <text x="300" y="130" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">शनि</text>
  <text x="300" y="155" fill="#d1fae5" font-size="9.5" text-anchor="middle">प्रारब्ध संस्कार</text>

  <!-- Yoga -->
  <rect x="365" y="60" width="95" height="110" fill="#7c3aed" rx="8" />
  <text x="412" y="85" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">४. योग</text>
  <text x="412" y="110" fill="#ede9fe" font-size="11" text-anchor="middle">आकाश तत्व</text>
  <text x="412" y="130" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">गुरु</text>
  <text x="412" y="155" fill="#ede9fe" font-size="9.5" text-anchor="middle">आरोग्य व सामंजस्य</text>

  <!-- Karana -->
  <rect x="475" y="60" width="95" height="110" fill="#d97706" rx="8" />
  <text x="522" y="85" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">५. करण</text>
  <text x="522" y="110" fill="#fef3c7" font-size="11" text-anchor="middle">पृथ्वी तत्व</text>
  <text x="522" y="130" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">बुध</text>
  <text x="522" y="155" fill="#fef3c7" font-size="9.5" text-anchor="middle">कर्म सिद्धि</text>

  <text x="300" y="210" fill="#cbd5e1" font-size="10.5" text-anchor="middle">पंचांग के इन पांच अंगों के संतुलन से जातक के संपूर्ण जीवन का आधार निर्मित होता है।</text>
</svg>'''

def get_vimshottari_tree_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 260" width="100%" height="200" style="max-width:460px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">विंशोत्तरी दशा: १२०-वर्षीय काल चक्र एवं ९ ग्रहों के वर्ष</text>
  <!-- Bar sequence of 9 planets -->
  <g transform="translate(30, 60)">
    <!-- Ketu 7y -->
    <rect x="0" y="0" width="31" height="80" fill="#64748b" rx="4" />
    <text x="15" y="45" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">केतु</text>
    <text x="15" y="65" fill="#fef08a" font-size="9" text-anchor="middle">७ वर्ष</text>

    <!-- Venus 20y -->
    <rect x="35" y="0" width="90" height="80" fill="#ec4899" rx="4" />
    <text x="80" y="45" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">शुक्र</text>
    <text x="80" y="65" fill="#fef08a" font-size="10" text-anchor="middle">२० वर्ष</text>

    <!-- Sun 6y -->
    <rect x="129" y="0" width="27" height="80" fill="#f59e0b" rx="4" />
    <text x="142" y="45" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">सूर्य</text>
    <text x="142" y="65" fill="#fef08a" font-size="8.5" text-anchor="middle">६व</text>

    <!-- Moon 10y -->
    <rect x="160" y="0" width="45" height="80" fill="#0284c7" rx="4" />
    <text x="182" y="45" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">चंद्र</text>
    <text x="182" y="65" fill="#fef08a" font-size="9" text-anchor="middle">१० वर्ष</text>

    <!-- Mars 7y -->
    <rect x="209" y="0" width="31" height="80" fill="#ef4444" rx="4" />
    <text x="224" y="45" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">भौम</text>
    <text x="224" y="65" fill="#fef08a" font-size="9" text-anchor="middle">७ वर्ष</text>

    <!-- Rahu 18y -->
    <rect x="244" y="0" width="81" height="80" fill="#475569" rx="4" />
    <text x="284" y="45" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">राहु</text>
    <text x="284" y="65" fill="#fef08a" font-size="10" text-anchor="middle">१८ वर्ष</text>

    <!-- Jupiter 16y -->
    <rect x="329" y="0" width="72" height="80" fill="#eab308" rx="4" />
    <text x="365" y="45" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">गुरु</text>
    <text x="365" y="65" fill="#451a03" font-size="10" text-anchor="middle">१६ वर्ष</text>

    <!-- Saturn 19y -->
    <rect x="405" y="0" width="85" height="80" fill="#1e3a8a" rx="4" />
    <text x="447" y="45" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">शनि</text>
    <text x="447" y="65" fill="#fef08a" font-size="10" text-anchor="middle">१९ वर्ष</text>

    <!-- Mercury 17y -->
    <rect x="494" y="0" width="46" height="80" fill="#10b981" rx="4" />
    <text x="517" y="45" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">बुध</text>
    <text x="517" y="65" fill="#fef08a" font-size="9.5" text-anchor="middle">१७ वर्ष</text>
  </g>
  <rect x="30" y="165" width="540" height="60" fill="rgba(255,255,255,0.06)" rx="6" />
  <text x="300" y="190" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle">कुल योग: ७ + २० + ६ + १० + ७ + १८ + १६ + १९ + १७ = १२० वर्ष</text>
  <text x="300" y="210" fill="#cbd5e1" font-size="10.5" text-anchor="middle">जन्म समय चंद्रमा पुष्य (शनि) में था ➔ शनि में ५ वर्ष ९ माह भोग्य दशा के बाद बुध दशा आई।</text>
</svg>'''

def get_ashtakavarga_wheel_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">अष्टकवर्ग ३३७ बिंदु चक्र: १२ भावों में शक्ति वितरण</text>
  <g transform="translate(40, 50)">
    <!-- Houses 1 to 12 as colored cards -->
    <rect x="0" y="0" width="38" height="50" fill="#0284c7" rx="4" /><text x="19" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">१</text><text x="19" y="42" fill="#fef08a" font-size="10" text-anchor="middle">२८</text>
    <rect x="44" y="0" width="38" height="50" fill="#059669" rx="4" /><text x="63" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">२</text><text x="63" y="42" fill="#fef08a" font-size="10" text-anchor="middle">३२</text>
    <rect x="88" y="0" width="38" height="50" fill="#059669" rx="4" /><text x="107" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">३</text><text x="107" y="42" fill="#fef08a" font-size="10" text-anchor="middle">३४</text>
    <rect x="132" y="0" width="38" height="50" fill="#0284c7" rx="4" /><text x="151" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">४</text><text x="151" y="42" fill="#fef08a" font-size="10" text-anchor="middle">२६</text>
    <rect x="176" y="0" width="38" height="50" fill="#059669" rx="4" /><text x="195" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">५</text><text x="195" y="42" fill="#fef08a" font-size="10" text-anchor="middle">३०</text>
    <rect x="220" y="0" width="38" height="50" fill="#ef4444" rx="4" /><text x="239" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">६</text><text x="239" y="42" fill="#fef08a" font-size="10" text-anchor="middle">२४</text>
    <rect x="264" y="0" width="38" height="50" fill="#0284c7" rx="4" /><text x="283" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">७</text><text x="283" y="42" fill="#fef08a" font-size="10" text-anchor="middle">२७</text>
    <rect x="308" y="0" width="38" height="50" fill="#ef4444" rx="4" /><text x="327" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">८</text><text x="327" y="42" fill="#fef08a" font-size="10" text-anchor="middle">२१</text>
    <rect x="352" y="0" width="38" height="50" fill="#059669" rx="4" /><text x="371" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">९</text><text x="371" y="42" fill="#fef08a" font-size="10" text-anchor="middle">३३</text>
    <rect x="396" y="0" width="38" height="50" fill="#059669" rx="4" /><text x="415" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">१०</text><text x="415" y="42" fill="#fef08a" font-size="10" text-anchor="middle">३६</text>
    <rect x="440" y="0" width="38" height="50" fill="#059669" rx="4" /><text x="459" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">११</text><text x="459" y="42" fill="#fef08a" font-size="10" text-anchor="middle">३५</text>
    <rect x="484" y="0" width="38" height="50" fill="#ef4444" rx="4" /><text x="503" y="25" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">१२</text><text x="503" y="42" fill="#fef08a" font-size="10" text-anchor="middle">२०</text>
  </g>
  <rect x="40" y="125" width="520" height="75" fill="rgba(255,255,255,0.06)" rx="6" />
  <text x="300" y="150" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle">★ कुल सर्वाष्टकवर्ग बिंदु योग = ३३७ (औसत प्रति भाव = २८ बिंदु)</text>
  <text x="300" y="170" fill="#cbd5e1" font-size="10.5" text-anchor="middle">२८+ बिंदु (हरा): अति शुभ व शक्तिशाली भाव • २८ से कम बिंदु (लाल): संघर्ष एवं साधना भाव</text>
  <text x="300" y="188" fill="#facc15" font-size="10" text-anchor="middle">जातक 'क': १०वें भाव में ३६ बिंदु एवं ११वें भाव में ३५ बिंदु असाधारण आजीविका सफलता देते हैं।</text>
</svg>'''

def get_shadbala_pillars_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">षड्बल के ६ शक्ति स्तंभ (रूपा मापन)</text>
  <g transform="translate(45, 55)">
    <!-- 6 pillars -->
    <rect x="0" y="20" width="75" height="100" fill="#0284c7" rx="4" />
    <text x="37" y="45" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">१. स्थान</text>
    <text x="37" y="70" fill="#e0f2fe" font-size="9.5" text-anchor="middle">उच्च/स्वक्षेत्र</text>
    <text x="37" y="105" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">स्थान बल</text>

    <rect x="85" y="35" width="75" height="85" fill="#10b981" rx="4" />
    <text x="122" y="60" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">२. दिग्</text>
    <text x="122" y="85" fill="#e0f2fe" font-size="9.5" text-anchor="middle">दिशा शक्ति</text>
    <text x="122" y="105" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">दिग् बल</text>

    <rect x="170" y="15" width="75" height="105" fill="#f59e0b" rx="4" />
    <text x="207" y="40" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">३. काल</text>
    <text x="207" y="65" fill="#e0f2fe" font-size="9.5" text-anchor="middle">दिन/रात्रि</text>
    <text x="207" y="105" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">काल बल</text>

    <rect x="255" y="40" width="75" height="80" fill="#8b5cf6" rx="4" />
    <text x="292" y="65" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">४. चेष्टा</text>
    <text x="292" y="85" fill="#e0f2fe" font-size="9.5" text-anchor="middle">वक्री गति</text>
    <text x="292" y="105" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">चेष्टा बल</text>

    <rect x="340" y="10" width="75" height="110" fill="#ec4899" rx="4" />
    <text x="377" y="35" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">५. नैसर्गिक</text>
    <text x="377" y="60" fill="#e0f2fe" font-size="9.5" text-anchor="middle">जन्मजात तेज</text>
    <text x="377" y="105" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">नैसर्गिक बल</text>

    <rect x="425" y="30" width="75" height="90" fill="#06b6d4" rx="4" />
    <text x="462" y="55" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">६. दृग्</text>
    <text x="462" y="80" fill="#e0f2fe" font-size="9.5" text-anchor="middle">शुभ दृष्टि</text>
    <text x="462" y="105" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">दृग् बल</text>
  </g>
  <text x="300" y="210" fill="#cbd5e1" font-size="10.5" text-anchor="middle">इन ६ बलों का योग 'षड्बल' कहलाता है। ५ रूपा से अधिक बल होने पर ग्रह श्रेष्ठ फल देता है।</text>
</svg>'''

def get_shodashavarga_tree_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">१६ वर्ग कुण्डलियाँ (षोडशवर्ग) विभाजन सोपान</text>
  <!-- 4 category boxes -->
  <rect x="30" y="55" width="125" height="90" fill="#0284c7" rx="6" />
  <text x="92" y="80" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">षड्वर्ग (६ वर्ग)</text>
  <text x="92" y="102" fill="#e0f2fe" font-size="9.5" text-anchor="middle">D1 राशि • D2 होरा</text>
  <text x="92" y="118" fill="#e0f2fe" font-size="9.5" text-anchor="middle">D3 द्रेष्काण • D9 नवांश</text>
  <text x="92" y="134" fill="#e0f2fe" font-size="9.5" text-anchor="middle">D12 द्वादशांश • D30</text>

  <rect x="165" y="55" width="130" height="90" fill="#059669" rx="6" />
  <text x="230" y="80" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">सप्तवर्ग (+D7)</text>
  <text x="230" y="102" fill="#d1fae5" font-size="9.5" text-anchor="middle">D7 सप्तांश</text>
  <text x="230" y="120" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">संतान एवं वंश वृद्धि</text>
  <text x="230" y="136" fill="#d1fae5" font-size="9.5" text-anchor="middle">का सूक्ष्म परीक्षण</text>

  <rect x="305" y="55" width="130" height="90" fill="#d97706" rx="6" />
  <text x="370" y="80" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">दशवर्ग (+D10)</text>
  <text x="370" y="102" fill="#fef3c7" font-size="9.5" text-anchor="middle">D10 दशमांश</text>
  <text x="370" y="120" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">व्यापार एवं आजीविका</text>
  <text x="370" y="136" fill="#fef3c7" font-size="9.5" text-anchor="middle">D16, D60 आदि</text>

  <rect x="445" y="55" width="125" height="90" fill="#7c3aed" rx="6" />
  <text x="507" y="80" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">षोडशवर्ग (१६)</text>
  <text x="507" y="102" fill="#ede9fe" font-size="9.5" text-anchor="middle">D20, D24, D27</text>
  <text x="507" y="118" fill="#ede9fe" font-size="9.5" text-anchor="middle">D40, D45, D60</text>
  <text x="507" y="134" fill="#fef08a" font-size="9.5" font-weight="bold" text-anchor="middle">D60 षष्ट्यंश (सर्वोच्च)</text>

  <text x="300" y="185" fill="#cbd5e1" font-size="10.5" text-anchor="middle">ऋषि पराशर के अनुसार: जो ग्रह अधिकांश वर्गों में शुभ हो (वैशेषिकांश), वह चक्रवर्ती फल देता है।</text>
</svg>'''

def get_jaimini_ladder_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">जैमिनी ७ चर कारक सोपान (अंशों का अवरोही क्रम)</text>
  <!-- Descending steps -->
  <g transform="translate(30, 45)">
    <rect x="0" y="0" width="70" height="40" fill="#f59e0b" rx="4" /><text x="35" y="24" fill="#000" font-size="10.5" font-weight="bold" text-anchor="middle">१. AK आत्म</text>
    <rect x="74" y="20" width="70" height="40" fill="#0284c7" rx="4" /><text x="109" y="44" fill="#fff" font-size="10.5" font-weight="bold" text-anchor="middle">२. AmK अमात्य</text>
    <rect x="148" y="40" width="70" height="40" fill="#059669" rx="4" /><text x="183" y="64" fill="#fff" font-size="10.5" font-weight="bold" text-anchor="middle">३. BK भ्रातृ</text>
    <rect x="222" y="60" width="70" height="40" fill="#d97706" rx="4" /><text x="257" y="84" fill="#fff" font-size="10.5" font-weight="bold" text-anchor="middle">४. MK मातृ</text>
    <rect x="296" y="80" width="70" height="40" fill="#8b5cf6" rx="4" /><text x="331" y="104" fill="#fff" font-size="10.5" font-weight="bold" text-anchor="middle">५. PK पुत्र</text>
    <rect x="370" y="100" width="70" height="40" fill="#64748b" rx="4" /><text x="405" y="124" fill="#fff" font-size="10.5" font-weight="bold" text-anchor="middle">६. GK ज्ञाति</text>
    <rect x="444" y="120" width="70" height="40" fill="#ec4899" rx="4" /><text x="479" y="144" fill="#fff" font-size="10.5" font-weight="bold" text-anchor="middle">७. DK दारा</text>
  </g>
  <text x="300" y="210" fill="#cbd5e1" font-size="10.5" text-anchor="middle">सर्वोच्च अंश = आत्मकारक (आत्मा का ध्येय) • न्यूनतम अंश = दाराकारक (जीवनसाथी व साझेदारी)</text>
</svg>'''

def get_bnn_trines_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">भृगु नंदी नाड़ी (BNN) ४ दिशा त्रिकोण चक्र</text>
  <!-- 4 Directional Cards -->
  <rect x="30" y="50" width="125" height="120" fill="#dc2626" rx="6" />
  <text x="92" y="75" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">पूर्व • धर्म त्रिकोण</text>
  <text x="92" y="100" fill="#fee2e2" font-size="10" text-anchor="middle">१, ५, ९ राशि</text>
  <text x="92" y="120" fill="#fef08a" font-size="10.5" font-weight="bold" text-anchor="middle">मेष • सिंह • धनु</text>
  <text x="92" y="145" fill="#fee2e2" font-size="9" text-anchor="middle">अग्नि तत्व • आत्मा</text>

  <rect x="165" y="50" width="125" height="120" fill="#059669" rx="6" />
  <text x="227" y="75" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">दक्षिण • अर्थ त्रिकोण</text>
  <text x="227" y="100" fill="#d1fae5" font-size="10" text-anchor="middle">२, ६, १० राशि</text>
  <text x="227" y="120" fill="#fef08a" font-size="10.5" font-weight="bold" text-anchor="middle">वृषभ • कन्या • मकर</text>
  <text x="227" y="145" fill="#d1fae5" font-size="9" text-anchor="middle">पृथ्वी तत्व • संपदा</text>

  <rect x="300" y="50" width="125" height="120" fill="#0284c7" rx="6" />
  <text x="362" y="75" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">पश्चिम • काम त्रिकोण</text>
  <text x="362" y="100" fill="#e0f2fe" font-size="10" text-anchor="middle">३, ७, ११ राशि</text>
  <text x="362" y="120" fill="#fef08a" font-size="10.5" font-weight="bold" text-anchor="middle">मिथुन • तुला • कुंभ</text>
  <text x="362" y="145" fill="#e0f2fe" font-size="9" text-anchor="middle">वायु तत्व • व्यापार</text>

  <rect x="435" y="50" width="135" height="120" fill="#7c3aed" rx="6" />
  <text x="502" y="75" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">उत्तर • मोक्ष त्रिकोण</text>
  <text x="502" y="100" fill="#ede9fe" font-size="10" text-anchor="middle">४, ८, १२ राशि</text>
  <text x="502" y="120" fill="#fef08a" font-size="10.5" font-weight="bold" text-anchor="middle">कर्क • वृश्चिक • मीन</text>
  <text x="502" y="145" fill="#ede9fe" font-size="9" text-anchor="middle">जल तत्व • अध्यात्म</text>

  <text x="300" y="205" fill="#cbd5e1" font-size="10.5" text-anchor="middle">नाड़ी नियम: एक ही दिशा के तीनों भावों में बैठे ग्रह १००% परस्पर युति जैसा फल देते हैं।</text>
</svg>'''

def get_sade_sati_wave_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">शनि साढ़े साती: ३ चरण (४५° कक्षा) एवं कर्म शुद्धि तरंग</text>
  <!-- 3 Phase Curve -->
  <path d="M 60,160 Q 200,60 300,60 T 540,160" fill="none" stroke="#38bdf8" stroke-width="3" />
  <!-- Phase 1 -->
  <circle cx="170" cy="95" r="7" fill="#f59e0b" />
  <text x="170" y="125" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">१. उदय चरण</text>
  <text x="170" y="142" fill="#cbd5e1" font-size="9.5" text-anchor="middle">चंद्र से १२वां भाव</text>
  <text x="170" y="157" fill="#94a3b8" font-size="9" text-anchor="middle">(ढाई वर्ष)</text>

  <!-- Phase 2 -->
  <circle cx="300" cy="60" r="8" fill="#ef4444" />
  <text x="300" y="90" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">२. शिखर चरण</text>
  <text x="300" y="108" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">जन्म चंद्र पर शनि</text>
  <text x="300" y="123" fill="#cbd5e1" font-size="9" text-anchor="middle">(ढाई वर्ष - महामंथन)</text>

  <!-- Phase 3 -->
  <circle cx="430" cy="95" r="7" fill="#10b981" />
  <text x="430" y="125" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">३. अस्त चरण</text>
  <text x="430" y="142" fill="#cbd5e1" font-size="9.5" text-anchor="middle">चंद्र से दूसरा भाव</text>
  <text x="430" y="157" fill="#94a3b8" font-size="9" text-anchor="middle">(ढाई वर्ष - पुनर्निर्माण)</text>

  <rect x="60" y="180" width="480" height="35" fill="rgba(255,255,255,0.06)" rx="4" />
  <text x="300" y="202" fill="#cbd5e1" font-size="10.5" text-anchor="middle">कुल अवधि = २.५ + २.५ + २.५ = ७.५ वर्ष (साढ़े साती) • शनि केवल प्रारब्ध कर्मों का फल देता है।</text>
</svg>'''

def get_ashtakoot_gauge_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">अष्टकूट ३६ गुण मिलान स्पीडोमीटर एवं मानक क्षेत्र</text>
  <!-- Meter Bar -->
  <g transform="translate(60, 60)">
    <!-- Red Zone: <18 -->
    <rect x="0" y="0" width="240" height="36" fill="#dc2626" rx="4" />
    <text x="120" y="23" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">० से १७ गुण (अस्वीकार्य)</text>

    <!-- Yellow Zone: 18-24 -->
    <rect x="245" y="0" width="100" height="36" fill="#f59e0b" rx="4" />
    <text x="295" y="23" fill="#000" font-size="11" font-weight="bold" text-anchor="middle">१८-२४ (मध्यम)</text>

    <!-- Green Zone: 25-36 -->
    <rect x="350" y="0" width="130" height="36" fill="#059669" rx="4" />
    <text x="415" y="23" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">२५-३६ (उत्तम)</text>
  </g>
  <!-- Details Box -->
  <rect x="60" y="125" width="480" height="85" fill="rgba(255,255,255,0.06)" rx="6" />
  <text x="300" y="150" fill="#facc15" font-size="12" font-weight="bold" text-anchor="middle">८ कूट: वर्ण (१), वश्य (२), तारा (३), योनि (४), ग्रहमैत्री (५), गण (६), भकूट (७), नाड़ी (८)</text>
  <text x="300" y="172" fill="#cbd5e1" font-size="10.5" text-anchor="middle">१८ गुण से अधिक होने पर ही विवाह शुभ माना जाता है। नाड़ी दोष (८ अंक) परिहार अत्यंत अनिवार्य है।</text>
  <text x="300" y="194" fill="#34d399" font-size="10" text-anchor="middle">२८ से ३२ गुण = असाधारण दांपत्य सामंजस्य • ३३ से ३६ गुण = दिव्य आत्मिक मेल</text>
</svg>'''

def get_pipeline_flow_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 250" width="100%" height="190" style="max-width:460px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">१५-चरणीय संपूर्ण कुण्डली विवेचन महा-पाइपलाइन</text>
  <!-- Flow steps -->
  <g transform="translate(20, 50)">
    <!-- Row 1 -->
    <rect x="10" y="0" width="95" height="36" fill="#0284c7" rx="4" /><text x="57" y="22" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">१. खगोल गणना</text>
    <text x="115" y="22" fill="#64748b" font-size="12">➔</text>
    <rect x="130" y="0" width="95" height="36" fill="#0284c7" rx="4" /><text x="177" y="22" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">२. अयनांश संस्कार</text>
    <text x="235" y="22" fill="#64748b" font-size="12">➔</text>
    <rect x="250" y="0" width="95" height="36" fill="#059669" rx="4" /><text x="297" y="22" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">३. लग्न साधन</text>
    <text x="355" y="22" fill="#64748b" font-size="12">➔</text>
    <rect x="370" y="0" width="95" height="36" fill="#059669" rx="4" /><text x="417" y="22" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">४. नवग्रह स्पष्ट</text>
    <text x="475" y="22" fill="#64748b" font-size="12">➔</text>
    <rect x="490" y="0" width="85" height="36" fill="#d97706" rx="4" /><text x="532" y="22" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">५. भाव कस्प</text>

    <!-- Row 2 -->
    <rect x="10" y="55" width="95" height="36" fill="#d97706" rx="4" /><text x="57" y="77" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">६. षोडशवर्ग D9</text>
    <text x="115" y="77" fill="#64748b" font-size="12">➔</text>
    <rect x="130" y="55" width="95" height="36" fill="#7c3aed" rx="4" /><text x="177" y="77" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">७. षड्बल मापन</text>
    <text x="235" y="77" fill="#64748b" font-size="12">➔</text>
    <rect x="250" y="55" width="95" height="36" fill="#7c3aed" rx="4" /><text x="297" y="77" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">८. अष्टकवर्ग SAV</text>
    <text x="355" y="77" fill="#64748b" font-size="12">➔</text>
    <rect x="370" y="55" width="95" height="36" fill="#ef4444" rx="4" /><text x="417" y="77" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">९. पराशरी योग</text>
    <text x="475" y="77" fill="#64748b" font-size="12">➔</text>
    <rect x="490" y="55" width="85" height="36" fill="#ef4444" rx="4" /><text x="532" y="77" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">१०. चर कारक</text>

    <!-- Row 3 -->
    <rect x="10" y="110" width="95" height="36" fill="#0891b2" rx="4" /><text x="57" y="132" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">११. BNN नाड़ी</text>
    <text x="115" y="132" fill="#64748b" font-size="12">➔</text>
    <rect x="130" y="110" width="95" height="36" fill="#0891b2" rx="4" /><text x="177" y="132" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">१२. विंशोत्तरी दशा</text>
    <text x="235" y="132" fill="#64748b" font-size="12">➔</text>
    <rect x="250" y="110" width="95" height="36" fill="#4f46e5" rx="4" /><text x="297" y="132" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">१३. गोचर वेध</text>
    <text x="355" y="132" fill="#64748b" font-size="12">➔</text>
    <rect x="370" y="110" width="95" height="36" fill="#4f46e5" rx="4" /><text x="417" y="132" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">१४. अरिष्ट भंग</text>
    <text x="475" y="132" fill="#64748b" font-size="12">➔</text>
    <rect x="490" y="110" width="85" height="36" fill="#10b981" rx="4" /><text x="532" y="132" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">१५. समाधान</text>
  </g>
  <text x="300" y="225" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">१५ चरणों के इस वैज्ञानिक अनुक्रम से कुण्डली फलादेश १००% अचूक और प्रामाणिक बनता है।</text>
</svg>'''

def get_navamsha_grid_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="100%" height="180" style="max-width:440px; margin:0.5rem auto; display:block; background:#090d16; border-radius:8px; border:1px solid #1e293b;">
  <text x="300" y="26" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">नवांश चक्र (D9) विभाजन सूत्र: ३° २०' प्रति नवांश</text>
  <g transform="translate(35, 50)">
    <!-- 9 Navamsha segments -->
    <rect x="0" y="0" width="55" height="50" fill="#0284c7" rx="4" /><text x="27" y="23" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">१ नवांश</text><text x="27" y="40" fill="#fef08a" font-size="9" text-anchor="middle">०°-३°२०'</text>
    <rect x="60" y="0" width="55" height="50" fill="#0284c7" rx="4" /><text x="87" y="23" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">२ नवांश</text><text x="87" y="40" fill="#fef08a" font-size="9" text-anchor="middle">३°२०'-६°४०'</text>
    <rect x="120" y="0" width="55" height="50" fill="#0284c7" rx="4" /><text x="147" y="23" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">३ नवांश</text><text x="147" y="40" fill="#fef08a" font-size="9" text-anchor="middle">६°४०'-१०°</text>
    <rect x="180" y="0" width="55" height="50" fill="#059669" rx="4" /><text x="207" y="23" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">४ नवांश</text><text x="207" y="40" fill="#fef08a" font-size="9" text-anchor="middle">१०°-१३°२०'</text>
    <rect x="240" y="0" width="55" height="50" fill="#059669" rx="4" /><text x="267" y="23" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">५ नवांश</text><text x="267" y="40" fill="#fef08a" font-size="9" text-anchor="middle">१३°२०'-१६°४०'</text>
    <rect x="300" y="0" width="55" height="50" fill="#059669" rx="4" /><text x="327" y="23" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">६ नवांश</text><text x="327" y="40" fill="#fef08a" font-size="9" text-anchor="middle">१६°४०'-२०°</text>
    <rect x="360" y="0" width="55" height="50" fill="#d97706" rx="4" /><text x="387" y="23" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">७ नवांश</text><text x="387" y="40" fill="#fef08a" font-size="9" text-anchor="middle">२०°-२३°२०'</text>
    <rect x="420" y="0" width="55" height="50" fill="#d97706" rx="4" /><text x="447" y="23" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">८ नवांश</text><text x="447" y="40" fill="#fef08a" font-size="9" text-anchor="middle">२३°२०'-२६°४०'</text>
    <rect x="480" y="0" width="55" height="50" fill="#d97706" rx="4" /><text x="507" y="23" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">९ नवांश</text><text x="507" y="40" fill="#fef08a" font-size="9" text-anchor="middle">२६°४०'-३०°</text>
  </g>
  <rect x="35" y="125" width="535" height="75" fill="rgba(255,255,255,0.06)" rx="6" />
  <text x="302" y="150" fill="#facc15" font-size="11.5" font-weight="bold" text-anchor="middle">अग्नि राशि (मेष, सिंह, धनु): मेष से गणना • पृथ्वी राशि (वृषभ, कन्या, मकर): मकर से गणना</text>
  <text x="302" y="170" fill="#cbd5e1" font-size="10.5" text-anchor="middle">वायु राशि (मिथुन, तुला, कुंभ): तुला से गणना • जल राशि (कर्क, वृश्चिक, मीन): कर्क से गणना</text>
  <text x="302" y="188" fill="#34d399" font-size="10" text-anchor="middle">जातक 'क': कन्या लग्न (१४° ३५') ➔ ५वां नवांश = वृषभ नवांश (भाग्य एवं धर्म वर्धक)</text>
</svg>'''
