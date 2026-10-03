#!/usr/bin/env python3
"""
Tantra Gyan Vedic Astrology Book Compiler
Transforms authentic source content from TantraGyan_Vedic_Astrology_Book.html
into a high-performance, SEO-optimized, bilingual interactive 3D digital book.
"""

import re
import html
import os

source_file = "/Users/apple/Downloads/TantraGyan_Vedic_Astrology_Book.html"
target_file = "/Users/apple/Movies/ap/TantraGyan/index.html"

with open(source_file, "r", encoding="utf-8") as f:
    raw_content = f.read()

# Constants and helpers for clean, glyph-safe book rendering
SCROLL_HINT_HTML = '<div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)</div>'

def clean_text(s):
    s = re.sub(r'<[^>]+>', '', s).strip()
    s = re.sub(r'^\d+\s*\|\s*', '', s)
    # Remove symbols and emojis that might cause box tofu on mobile
    s = re.sub(r'[☿♃♄☊☋♀♂♈♉♊♋♌♍♎♏♐♑♒♓⇄⛶\ufe0f]', '', s)
    s = re.sub(r'[\U00010000-\U0010ffff]', '', s)
    return s.strip()

def clean_table_glyphs(tb_html):
    if not tb_html:
        return ""
    # Replace astrological symbols with clean text
    replacements = [
        ('☿', 'बुध (Mercury)'),
        ('♃', 'गुरु (Jupiter)'),
        ('♄', 'शनि (Saturn)'),
        ('☊', 'राहु (Rahu)'),
        ('☋', 'केतु (Ketu)'),
        ('♀', 'शुक्र (Venus)'),
        ('♂', 'मंगल (Mars)'),
        ('☉', 'सूर्य (Sun)'),
        ('☽', 'चन्द्र (Moon)'),
        ('♈', 'मेष (Aries)'),
        ('♉', 'वृषभ (Taurus)'),
        ('♊', 'मिथुन (Gemini)'),
        ('♋', 'कर्क (Cancer)'),
        ('♌', 'सिंह (Leo)'),
        ('♍', 'कन्या (Virgo)'),
        ('♎', 'तुला (Libra)'),
        ('♏', 'वृश्चिक (Scorpio)'),
        ('♐', 'धनु (Sagittarius)'),
        ('♑', 'मकर (Capricorn)'),
        ('♒', 'कुंभ (Aquarius)'),
        ('♓', 'मीन (Pisces)'),
        ('⇄', ''),
        ('⛶', ''),
        ('\ufe0f', '')
    ]
    for orig, rep in replacements:
        tb_html = tb_html.replace(orig, rep)
    # Strip SMP emojis that cause box tofu on mobile
    tb_html = re.sub(r'[\U00010000-\U0010ffff]', '', tb_html)
    return tb_html

def sanitize_content_block(cb_raw):
    if not cb_raw:
        return ""
    # Strip slide indicators like <div class="slide-indicator">Section 29 |</div>
    s = re.sub(r'<div[^>]*class=[\"\']slide-indicator[\"\'][^>]*>.*?</div>', '', cb_raw, flags=re.DOTALL)
    # Strip Section XX | text
    s = re.sub(r'Section\s*\d+\s*\|\s*', '', s)
    # Strip all scraped headings to eliminate stacked duplicate titles
    s = re.sub(r'<h[1-6][^>]*>.*?</h[1-6]>', '', s, flags=re.DOTALL)
    # Strip empty divs and paragraphs
    s = re.sub(r'<div[^>]*>\s*</div>', '', s)
    s = re.sub(r'<p>\s*</p>', '', s)
    # Strip formula pills that merely repeat section titles
    s = re.sub(r'<span class="rule-badge">.*?</span>', '', s)
    s = re.sub(r'<span class="formula-pill">.*?</span>', '', s)
    # Check if there is actual non-heading content left
    text_content = re.sub(r'<[^>]+>', '', s).strip()
    if not text_content or len(text_content) < 30:
        return ""
    return s.strip()

pages = []

# ==============================================================================
# FRONT MATTER PAGES (1 to 5)
# ==============================================================================

# PAGE 1: Grand Book Cover
page_1 = """
<div class="cover-page-inner">
  <div class="cover-tag">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) • Digital Edition 2026</div>
  
  <div class="cover-yantra">
    <img src="assets/yantra.svg" alt="Sacred Sri Yantra Emblem" width="130" height="130" style="filter: drop-shadow(0 4px 15px rgba(200, 157, 61, 0.45));">
  </div>

  <h1 class="cover-title-hindi">वैदिक ज्योतिष महाग्रंथ सरलीकृत</h1>
  <h2 class="cover-title-english">Complete Vedic Astrology Compendium Simplified</h2>

  <div class="cover-divider"></div>

  <p class="cover-subtitle">
    <strong>नवग्रह कारकत्व, 17 शास्त्रीय राजयोग, 27 नक्षत्र व 108 पद विश्लेषण, दीप्तादि 9 अवस्थाएं एवं 12 भाव-राशि फल।</strong><br>
    <span style="font-size:0.85rem; color:var(--text-muted); display:inline-block; margin-top:0.4rem;">
      Comprehensive Classical Sutras, Astronomical Motion & Predictive Principles
    </span>
  </p>

  <div class="cover-author-block">
    <div class="cover-author-label">लेखक एवं ज्योतिषाचार्य (Author & Astrologer)</div>
    <div class="cover-author-name">Ashutosh Kumar Choubey</div>
    <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem; margin-top:0.75rem;">
      <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="contact-channel-badge" style="border-color:var(--accent-gold); color:var(--accent-gold) !important; font-weight:700;">
        <span class="contact-icon">🌐</span>
        <span><strong>t.worldgyan.com</strong></span>
      </a>
      <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge" style="margin-top:0;">
        <span class="yt-play-icon">▶</span>
        <span>YouTube: <strong>@TantraGyan108</strong></span>
      </a>
    </div>
  </div>
</div>
"""
pages.append({
    "chapter": "मुखपृष्ठ • Cover",
    "title": "वैदिक ज्योतिष महाग्रंथ सरलीकृत",
    "content": page_1
})

# PAGE 2: About the Author (Astrologer Ashutosh Kumar Choubey)
page_2 = """
<div class="page-inner-content">
  <div class="chapter-header" style="margin-bottom:1.25rem;">
    <div class="chapter-number">Author Profile</div>
    <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-crimson);">लेखक परिचय — ज्योतिषाचार्य Ashutosh Kumar Choubey</h2>
  </div>

  <div class="author-profile-box">
    <div class="author-avatar-badge">🕉️</div>
    <div class="author-bio-text">
      <h3>Ashutosh Kumar Choubey</h3>
      <div class="author-meta">Vedic Astrologer & Tantra Researcher</div>
      <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
        समर्पित वैदिक ज्योतिषी एवं शोधकर्ता, जिन्होंने शास्त्रीय ज्योतिष ग्रंथों और आधुनिक विश्लेषणात्मक पद्धतियों के समन्वय से 'तंत्र ज्ञान' (Tantra Gyan) ज्ञानकोश की रचना की है।
      </p>
    </div>
  </div>

  <div class="rule-card">
    <div class="rule-header">
      <div class="rule-title">📜 शोध दृष्टि एवं शास्त्रीय परंपरा (Research Lineage & Vision)</div>
      <span class="badge-chip badge-gold">प्रामाणिक दृष्टिकोण</span>
    </div>
    <div class="rule-body">
      <p>
        <strong>ज्योतिषाचार्य आशुतोष कुमार चौबे</strong> का मुख्य ध्येय प्राचीन वैदिक ज्ञान को अंधविश्वास, भय एवं रूढ़िवादिता से मुक्त करके एक तार्किक, वैज्ञानिक तथा व्यावहारिक सूत्रबद्ध पद्धति के रूप में प्रस्तुत करना है।
      </p>
      <p>
        इन्होंने <em>बृहत्पाराशर होरा शास्त्र, सारावली (कल्याण वर्मा), फलदीपिका (मन्त्रेश्वर), जातक पारिजात, नंदी नाड़ी</em> तथा <em>लाल किताब</em> जैसे मूर्धन्य ग्रंथों का गहन अध्ययन करके उनके रहस्यों को वर्तमान संदर्भ में सत्यापनीय नियमों (Reproducible Principles) के रूप में रूपांतरित किया है।
      </p>
    </div>
  </div>

  <div class="rule-card success">
    <div class="rule-header">
      <div class="rule-title">🎯 फलित ज्योतिष दर्शन एवं कर्म सिद्धांत (Predictive Philosophy & Karmic Principles)</div>
      <span class="badge-chip badge-gold">मार्गदर्शक दृष्टि</span>
    </div>
    <div class="rule-body">
      <p>
        आशुतोष जी का मानना है कि जन्मकुण्डली केवल भविष्य की घटनाओं का पूर्वानुमान नहीं, बल्कि मनुष्य के संचित कर्मों (Sanchita Karma) और प्रारब्ध (Prarabdha) का एक सूक्ष्म खगोलीय मानचित्र है।
      </p>
      <p>
        ग्रह दशाओं, गोचर और भाव-कारकत्व के वैज्ञानिक विश्लेषण से व्यक्ति अपनी स्वाभाविक शक्तियों, चुनौतियों और जीवन के उचित समय को पहचान सकता है। इनका ध्येय प्रत्येक जिज्ञासु को अंधविश्वास से परे आत्म-निरीक्षण, सही कर्म-निर्णय और चेतना के उत्थान के लिए सक्षम बनाना है।
      </p>
      <p style="font-size:0.84rem; color:var(--text-muted); margin-top:0.4rem;">
        <em>"ज्योतिष भाग्य के प्रति असहाय समर्पण नहीं, बल्कि आत्म-बोध और कर्म सुधार का प्रकाश स्तंभ है।"</em>
      </p>
    </div>
  </div>

  <div style="margin-top:1.25rem; padding:1.1rem; border:1px dashed var(--accent-gold); border-radius:10px; background:rgba(179,127,25,0.06); text-align:center;">
    <strong style="color:var(--text-heading); font-size:0.92rem;">आधिकारिक शोध, वेबसाइट एवं संपर्क मंच (Official Channels):</strong><br>
    <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem; margin-top:0.75rem;">
      <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="contact-channel-badge" style="border-color:var(--accent-gold); color:var(--accent-gold) !important; font-weight:700;">
        <span class="contact-icon">🌐</span>
        <span>वेबसाइट: <strong>t.worldgyan.com</strong></span>
      </a>
      <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge" style="margin-top:0;">
        <span class="yt-play-icon">▶</span>
        <span>YouTube: <strong>@TantraGyan108</strong></span>
      </a>
      <a href="mailto:tantraresearchcenter@gmail.com" class="contact-channel-badge">
        <span class="contact-icon">✉️</span>
        <span>tantraresearchcenter@gmail.com</span>
      </a>
      <a href="tel:+919658476170" class="contact-channel-badge">
        <span class="contact-icon">📞</span>
        <span>+91 9658476170</span>
      </a>
    </div>
  </div>
</div>
"""
pages.append({
    "chapter": "लेखक परिचय • About the Author",
    "title": "लेखक परिचय — ज्योतिषाचार्य आशुतोष कुमार चौबे",
    "content": page_2
})

# PAGE 3: Why This Book? (Purpose & Scope of Compendium)
page_3 = """
<div class="page-inner-content">
  <div class="chapter-header" style="margin-bottom:1.25rem;">
    <div class="chapter-number">Preface & Philosophy</div>
    <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-gold);">ग्रंथ का उद्देश्य एवं दर्शन — Why This Book?</h2>
  </div>

  <p style="font-size:0.9rem; line-height:1.6; margin-bottom:1rem;">
    वैदिक ज्योतिष का ज्ञान अनंत सागर की भांति विस्तृत है। साधारण जिज्ञासु और गंभीर अभ्यासकर्ता प्रायः बिखरे हुए सूत्रों, परस्पर विरोधी मतों और जटिल संस्कृत टीकाओं में उलझ जाते हैं। <strong>वैदिक ज्योतिष महाग्रंथ सरलीकृत</strong> को एक <em>"हाई-डेंसिटी प्रेक्टिशनर नोटबुक" (Concise Practitioner Notebook)</em> के रूप में तैयार किया गया है।
  </p>

  <div class="pillar-grid">
    <div class="pillar-card">
      <div class="pillar-number">Pillar 1</div>
      <div class="pillar-title">नवग्रह कारकत्व सार (Planetary Karakatvas)</div>
      <div class="pillar-desc">प्रत्येक ग्रह के संपूर्ण शारीरिक, मानसिक, आध्यात्मिक व संबंधपरक संकेतक शास्त्रीय संदर्भों सहित।</div>
    </div>
    <div class="pillar-card">
      <div class="pillar-number">Pillar 2</div>
      <div class="pillar-title">17 शास्त्रीय राजयोग (Classical Raja Yogas)</div>
      <div class="pillar-desc">पंच महापुरुष, गजकेसरी, बुधादित्य एवं विपरीत राजयोगों की सटीक निर्माण शर्तें व फल।</div>
    </div>
    <div class="pillar-card">
      <div class="pillar-number">Pillar 3</div>
      <div class="pillar-title">ग्रह गति व महादशा (Astronomical Motion)</div>
      <div class="pillar-desc">ग्रहों की कक्षा गति, गोचर अवधि, दृष्टियां तथा विंशोत्तरी दशा चक्र का गणितीय सामंजस्य।</div>
    </div>
    <div class="pillar-card">
      <div class="pillar-number">Pillar 4</div>
      <div class="pillar-title">मेडिकल एस्ट्रोलॉजी (Medical Diagnostics)</div>
      <div class="pillar-desc">12 भावों, 12 राशियों और 9 ग्रहों का अंग-रोग संबंध तथा कैंसर व्याधि के अचूक ज्योतिषीय सूत्र।</div>
    </div>
  </div>

  <div class="rule-card info" style="margin-top:1rem;">
    <div class="rule-header">
      <div class="rule-title">📖 इस ग्रंथ के अध्ययन की विधि (How to Use this Notebook)</div>
    </div>
    <div class="rule-body">
      <ul style="padding-left:1.25rem; font-size:0.85rem; line-height:1.6;">
        <li>प्रत्येक पृष्ठ स्वतंत्र विषय पर केंद्रित संक्षिप्त, सूत्रबद्ध तालिका (Tabular Notes) प्रस्तुत करता है।</li>
        <li>ऊपरी टूलबार से <strong>हिंदी, English अथवा Bilingual (द्विभाषी)</strong> मोड अपनी सुविधानुसार चुनें।</li>
        <li>शीर्षक और तालिका संदर्भों को सीधे अपने व्यावहारिक कुण्डली विश्लेषण में मार्गदर्शक के रूप में प्रयोग करें।</li>
      </ul>
    </div>
  </div>
</div>
"""
pages.append({
    "chapter": "प्रस्तावना • Preface",
    "title": "ग्रंथ का उद्देश्य एवं आधारभूत संरचना",
    "content": page_3
})

# PAGE 4: Legal & Spiritual Disclaimer
page_4 = """
<div class="page-inner-content">
  <div class="chapter-header" style="margin-bottom:1.25rem;">
    <div class="chapter-number">Notice & Ethics</div>
    <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-crimson);">वैधानिक सूचना एवं अस्वीकरण (Legal & Spiritual Disclaimer)</h2>
  </div>

  <div class="disclaimer-box warning" style="border:1px solid rgba(220,38,38,0.3); background:rgba(220,38,38,0.04); border-left:4px solid var(--accent-crimson); border-radius:8px; padding:1.25rem; margin-bottom:1.5rem;">
    <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;">
      <span style="font-size:1.4rem;">⚠️</span>
      <h3 style="color:var(--accent-crimson); font-family:var(--font-heading); font-size:1.05rem;">महत्वपूर्ण वैधानिक चेतावनी एवं अस्वीकरण</h3>
    </div>
    
    <div style="font-size:0.88rem; line-height:1.65; color:var(--text-main);">
      <p style="margin-bottom:0.75rem;">
        <strong>1. केवल शैक्षणिक एवं शोध उद्देश्य (Educational Purposes Only):</strong><br>
        The content shared by Tantra Gyan and Astrologer Ashutosh Kumar Choubey is strictly for educational, historical, and astrological research purposes. Astrology offers symbolic guidance and probabilistic tendencies, not guaranteed outcomes. Real-life decisions should be based on your personal judgment, professional counsel, and conscious actions—not solely on astrology, spiritual beliefs, or rituals.
      </p>

      <p style="margin-bottom:0.75rem;">
        <strong>2. तांत्रिक साधना एवं अनुशासन (Tantra Discipline & Guru Guidance):</strong><br>
        Tantra is a deep, profound, and potentially perilous esoteric discipline. Never attempt any tantric ritual, mantra experiment, or occult practice without the direct initiation and personal supervision of an authentic, qualified Guru and strict adherence to moral discipline (Yama & Niyama).
      </p>

      <p style="margin-bottom:0.75rem;">
        <strong>3. अंधविश्वास एवं रूढ़िवादिता का पूर्ण खंडन (Rejection of Blind Faith & Superstition):</strong><br>
        We strictly condemn and do not promote blind faith, fear-mongering, fatalistic superstition, or exploitative practices. Astrology is a diagnostic tool, not an excuse for passivity.
      </p>

      <div style="margin-top:1.25rem; padding-top:0.75rem; border-top:1px solid var(--page-border); font-size:0.82rem; color:var(--text-muted);">
        <strong>कॉपीराइट सूचना (Copyright Notice):</strong><br>
        © 2026 Ashutosh Kumar Choubey. All rights reserved. No part of this compendium may be reproduced, distributed, or transmitted in any form without express prior written permission.
      </div>
    </div>
  </div>
</div>
"""
pages.append({
    "chapter": "अस्वीकरण • Legal Disclaimer",
    "title": "तांत्रिक अनुशासन, आचार संहिता एवं वैधानिक परामर्श",
    "content": page_4
})

# PAGE 5: Table of Contents (Index)
page_5 = """
<div class="page-inner-content">
  <div class="chapter-header" style="margin-bottom:1.2rem;">
    <div class="chapter-number">Index & Navigation</div>
    <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-gold);">विषय-सूची — Table of Contents</h2>
  </div>

  <div class="index-grid-container">
    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(1, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 1</span>
        <div class="index-card-info">
          <strong class="index-card-title">प्रस्तावना, लेखक परिचय एवं वैधानिक सूचना</strong>
          <span class="index-card-desc">Front Matter, Author Profile & Guidelines</span>
        </div>
      </div>
      <span class="index-page-range">Pages 1 - 5</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(6, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 2</span>
        <div class="index-card-info">
          <strong class="index-card-title">नवग्रह कारकत्व एवं 17 शास्त्रीय राजयोग</strong>
          <span class="index-card-desc">Navagraha Karakatva & Classical Raja Yogas</span>
        </div>
      </div>
      <span class="index-page-range">Pages 6 - 20</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(21, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 3</span>
        <div class="index-card-info">
          <strong class="index-card-title">राशि, नक्षत्र, ग्रह गति एवं विंशोत्तरी महादशा</strong>
          <span class="index-card-desc">Zodiac Signs, 27 Nakshatras & Vimshottari Dasha</span>
        </div>
      </div>
      <span class="index-page-range">Pages 21 - 37</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(38, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 4</span>
        <div class="index-card-info">
          <strong class="index-card-title">भाव एवं राशियों में ग्रहों का प्रभाव (दीप्तादि 9 अवस्थाएं)</strong>
          <span class="index-card-desc">12 Houses, Planetary States & Operational Rules</span>
        </div>
      </div>
      <span class="index-page-range">Pages 38 - 47</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(48, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 5</span>
        <div class="index-card-info">
          <strong class="index-card-title">मेडिकल एस्ट्रोलॉजी एवं कैंसर रोग विश्लेषण (27 संपूर्ण तालिकाएं)</strong>
          <span class="index-card-desc">Medical Astrology & Organ Pathology Reference</span>
        </div>
      </div>
      <span class="index-page-range">Pages 48 - 74</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(75, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 6</span>
        <div class="index-card-info">
          <strong class="index-card-title">नक्षत्रों का गहन पद एवं ग्रह विश्लेषण (अश्विनी, आश्लेषा, पुष्य)</strong>
          <span class="index-card-desc">Deep Pada Matrices & Degrees Reference</span>
        </div>
      </div>
      <span class="index-page-range">Pages 75 - 85</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(86, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Colophon</span>
        <div class="index-card-info">
          <strong class="index-card-title">समापन पृष्ठ, मंगल श्लोक व आधिकारिक संपर्क</strong>
          <span class="index-card-desc">Benediction, Upanishad Shloka & Contacts</span>
        </div>
      </div>
      <span class="index-page-range">Page 86</span>
    </div>
  </div>

  <div style="margin-top:1.15rem; font-size:0.84rem; color:var(--text-muted); text-align:center;">
    💡 <em>संकेत: किसी भी अध्याय कार्ड पर क्लिक करके सीधे उस पृष्ठ पर जा सकते हैं, या शीर्ष टूलबार के <strong>📖 विषय-सूची</strong> बटन से संपूर्ण सूची देखें।</em>
  </div>
</div>
"""
pages.append({
    "chapter": "अनुक्रमणिका • Index",
    "title": "विषय-सूची (सम्पूर्ण ग्रंथ अनुक्रमणिका)",
    "content": page_5
})

# ==============================================================================
# CHAPTER 2: Navagraha Karakatva & Classical Raja Yogas (15 Tables)
# ==============================================================================
ch2_titles = [
    "सूर्य देव के संपूर्ण शास्त्रीय कारकत्व",
    "चन्द्रमा के संपूर्ण शास्त्रीय कारकत्व",
    "चन्द्रमा: शास्त्रीय ग्रंथ संदर्भ व फलित सूत्र",
    "चन्द्रमा: आधुनिक व्यावहारिक फलित व मानसिक विश्लेषण",
    "मंगल देव के संपूर्ण शास्त्रीय कारकत्व",
    "मंगल देव: शास्त्रीय ग्रंथ संदर्भ व पराक्रम सूत्र",
    "बृहस्पति (गुरु) के संपूर्ण शास्त्रीय कारकत्व",
    "शुक्र देव के संपूर्ण शास्त्रीय कारकत्व",
    "शनि देव के संपूर्ण कारकत्व व कर्म सिद्धांत",
    "शनि देव: प्रमुख शास्त्रीय एवं आधुनिक दृष्टिकोण",
    "बुध देव के संपूर्ण कारकत्व व बुद्धि-विवेक",
    "राहु देव के संपूर्ण कारकत्व व मायावी प्रभाव",
    "केतु देव के संपूर्ण कारकत्व व मोक्ष मार्ग",
    "१७ शास्त्रीय राजयोग एवं पंच महापुरुष योग (भाग १)",
    "१७ शास्त्रीय राजयोग एवं विपरीत राजयोग (भाग २)"
]

ch2_m = re.search(r'<section\b[^>]*id=[\"\']chapter-2[\"\'][^>]*>(.*?)</section>', raw_content, re.DOTALL)
if ch2_m:
    ch2_text = ch2_m.group(1)
    ch2_pairs = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch2_text, re.DOTALL)
    
    for idx, (cb, tb, tid) in enumerate(ch2_pairs):
        caption = ch2_titles[idx] if idx < len(ch2_titles) else f"नवग्रह कारकत्व तालिका {idx+1}"
        
        # Clean up cb and tb to fit book layout
        cb_clean = sanitize_content_block(cb) if cb else ""
        cb_clean = re.sub(r'<h2[^>]*id=\"Page-2[^\"]*\"[^>]*>.*?</h2>', '', cb_clean)
        
        # Eliminate stacked duplicate title bar
        tb_clean = re.sub(r'<div class=\"table-caption\">.*?</div>', '', tb)
        tb_clean = clean_table_glyphs(tb_clean)
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 2 • Section {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{caption}</h3>
          </div>
          {cb_clean}
          {SCROLL_HINT_HTML}
          <div class="astro-table-container">
            {tb_clean}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 2: नवग्रह कारकत्व व राजयोग",
            "title": caption,
            "content": content
        })

# ==============================================================================
ch3_titles = [
    "ग्रह गति, गोचर अवधि एवं विंशोत्तरी महादशा चक्र",
    "ग्रह दृष्टि तालिका एवं शास्त्रीय दृष्टि नियम",
    "२७ नक्षत्र, विस्तार व राशि सीमा तालिका",
    "२७ नक्षत्र, अधिष्ठाता देवता व पद नामाक्षर",
    "नक्षत्र, अधिष्ठाता देवता और स्वामी तालिका",
    "नक्षत्र स्वामी व दशा अधिपति सूत्र",
    "२७ नक्षत्र एवं स्वामी शास्त्रीय तालिका",
    "१२ राशियां, स्वामी व पंचमहाभूत तत्व",
    "राशियों के गुण, तत्व एवं स्वभाव वर्गीकरण",
    "राशियों का लिंग वर्गीकरण (पुरुष व स्त्री राशियां)",
    "राशियों की ध्रुवता (धनात्मक एवं ऋणात्मक स्वभाव)",
    "अग्नि तत्व राशियां: मेष, सिंह, धनु",
    "पृथ्वी तत्व राशियां: वृषभ, कन्या, मकर",
    "वायु तत्व राशियां: मिथुन, तुला, कुंभ",
    "जल तत्व राशियां: कर्क, वृश्चिक, मीन",
    "तत्व एवं गतिशीलता का संयुक्त वर्गीकरण",
    "चर, स्थिर, द्विस्वभाव व तत्व फलित नियम"
]

ch3_m = re.search(r'<section\b[^>]*id=[\"\']chapter-3[\"\'][^>]*>(.*?)</section>', raw_content, re.DOTALL)
if ch3_m:
    ch3_text = ch3_m.group(1)
    ch3_pairs = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch3_text, re.DOTALL)
    
    for idx, (cb, tb, tid) in enumerate(ch3_pairs):
        caption = ch3_titles[idx] if idx < len(ch3_titles) else f"खगोलीय गति तालिका {idx+1}"
        
        cb_clean = sanitize_content_block(cb) if cb else ""
        cb_clean = re.sub(r'<h2[^>]*id=\"Page-3[^\"]*\"[^>]*>.*?</h2>', '', cb_clean)
        
        # Section 2: Planetary Drishti Notes cleanly organized
        if idx == 1:
            cb_clean = """
            <div class="rule-card success">
              <div class="rule-header">
                <div class="rule-title">📜 शास्त्रीय दृष्टि नियम (Classical Aspect Principles)</div>
              </div>
              <div class="rule-body">
                <ul style="margin:0; padding-left:1.2rem; line-height:1.6; font-size:0.88rem;">
                  <li><strong>सामान्य दृष्टि (7वां भाव):</strong> सभी ग्रह अपने अधिष्ठित भाव से सप्तम भाव पर पूर्ण दृष्टि डालते हैं।</li>
                  <li><strong>विशेष पूर्ण दृष्टियां:</strong>
                    <ul>
                      <li><strong>मंगल (Mars):</strong> 4था, 7वां और 8वां भाव।</li>
                      <li><strong>गुरु (Jupiter):</strong> 5वां, 7वां और 9वां भाव।</li>
                      <li><strong>शनि (Saturn):</strong> 3रा, 7वां और 10वां भाव।</li>
                    </ul>
                  </li>
                  <li><strong>राहु एवं केतु:</strong> शास्त्रीय ग्रंथों में दृष्टि नहीं, परंतु आधुनिक फलित ज्योतिष में 5वीं, 7वीं व 9वीं दृष्टि मान्य है।</li>
                </ul>
              </div>
            </div>
            """
        # Section 3: 27 Nakshatras Degree Spans cleanly organized
        elif idx == 2:
            cb_clean = """
            <div class="rule-card">
              <div class="rule-body" style="font-size:0.88rem; line-height:1.6;">
                वैदिक ज्योतिष में संपूर्ण 360° भचक्र को 27 समान नक्षत्रों में विभाजित किया गया है। प्रत्येक नक्षत्र का विस्तार <strong>13°20’ (13 अंश और 20 कला)</strong> होता है। नीचे प्रत्येक नक्षत्र के प्रारंभ एवं समापन अंश व्यवस्थित रूप से दिए गए हैं।
              </div>
            </div>
            """
        
        # Eliminate stacked duplicate title bar
        tb_clean = re.sub(r'<div class=\"table-caption\">.*?</div>', '', tb)
        tb_clean = clean_table_glyphs(tb_clean)
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 3 • Section {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{caption}</h3>
          </div>
          {cb_clean}
          {SCROLL_HINT_HTML}
          <div class="astro-table-container">
            {tb_clean}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 3: राशि, नक्षत्र एवं ग्रह गति",
            "title": caption,
            "content": content
        })

# ==============================================================================
# CHAPTER 4: Planets in Houses & Signs (Deeptadi Avasthas, Karakas, Sun in Houses)
# ==============================================================================
ch4_m = re.search(r'<section\b[^>]*id=[\"\']chapter-4[\"\'][^>]*>(.*?)</section>', raw_content, re.DOTALL)
if ch4_m:
    ch4_text = ch4_m.group(1)
    # Extract major components of Ch4
    
    # 4.1 Deeptadi Avasthas 9 States Explanation
    pos_deep = ch4_text.find('Deeptadi Avastha Explained')
    pos_tbl1 = ch4_text.find('<div class="table-container"')
    if pos_deep != -1 and pos_tbl1 != -1:
        deep_intro = ch4_text[pos_deep:pos_tbl1]
        deep_intro = re.sub(r'<h4[^>]*class="topic-title">The classification of signs.*?$', '', deep_intro, flags=re.DOTALL)
        deep_intro = re.sub(r'</?div[^>]*>', '', deep_intro).strip()
        page_4_1 = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 4 • Section 1</div>
            <h3 class="chapter-heading" style="font-size:1.2rem; color:var(--accent-gold);">दीप्तादि ९ अवस्थाएं: ग्रहों की स्थिति व फल</h3>
          </div>
          <div class="rule-card">
            <div class="rule-header">
              <div class="rule-title">दीप्तादि ९ अवस्थाएं (Nine Planetary States)</div>
              <span class="badge-chip badge-gold">पाराशरी सूत्र</span>
            </div>
            <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
              {deep_intro}
            </div>
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 4: भाव एवं राशियों में ग्रह",
            "title": "दीप्तादि ९ अवस्थाएं: ग्रहों की स्थिति व फल",
            "content": page_4_1
        })
    
    # 4.2 Tables 1 to 6 in Ch4
    ch4_table_titles = [
        "ग्रहों की नैसर्गिक व तात्कालिक मैत्री वर्गीकरण",
        "दीप्तादि अवस्थाएं, मूलत्रिकोण व स्वराशि तालिका",
        "ग्रह अवस्थाओं के व्यावहारिक फलित नियम",
        "ग्रहों के पांच प्रकार के संबंध (पंच संबंध)",
        "१२ भावों के स्थिर कारक ग्रह",
        "भाव कारक व भावेश का शास्त्रीय अंतर एवं विश्लेषण"
    ]
    ch4_tables = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch4_text, re.DOTALL)
    for idx, (cb, tb, tid) in enumerate(ch4_tables):
        caption = ch4_table_titles[idx] if idx < len(ch4_table_titles) else f"भाव एवं राशि तालिका {idx+1}"
        cb_clean = sanitize_content_block(cb) if cb else ""
        tb_clean = re.sub(r'<div class=\"table-caption\">.*?</div>', '', tb)
        tb_clean = clean_table_glyphs(tb_clean)
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 4 • Table {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{caption}</h3>
          </div>
          {cb_clean}
          {SCROLL_HINT_HTML}
          <div class="astro-table-container">
            {tb_clean}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 4: भाव एवं राशियों में ग्रह",
            "title": caption,
            "content": content
        })
    
    def clean_sun_block(raw_text):
        s = re.sub(r'<div[^>]*class=[\"\']slide-indicator[\"\'][^>]*>.*?</div>', '', raw_text, flags=re.DOTALL)
        s = re.sub(r'Section\s*\d+\s*\|\s*', '', s)
        s = re.sub(r'<h[1-6][^>]*>\s*\d+\s*\|\s*.*?<\/h[1-6]>', '', s, flags=re.DOTALL)
        s = re.sub(r'<h[1-6][^>]*>.*?(?:Surya in 12|Sun in 12 Houses|Effect of Sun|YouTube Video Title|SEO-Optimized|Sun[\'&#x27;]*s Impact|Zodiac Signs Vedic Astrology).*?<\/h[1-6]>', '', s, flags=re.DOTALL | re.IGNORECASE)
        
        items = re.split(r'(?=<h4[^>]*>\s*\d+\.\s*)', s)
        cleaned_items = []
        for item in items:
            item = item.strip()
            if not item:
                continue
            m_title = re.search(r'<h4[^>]*>\s*(\d+\.\s*[^<]+)</h4>', item)
            if m_title:
                title = m_title.group(1).strip()
                title = re.sub(r'[☀️🌞🔥📽️]', '', title).strip()
                rest = item[m_title.end():]
                rest = re.sub(r'<h[1-6][^>]*>.*?(?:Surya in 12|Sun in 12 Houses|Effect of Sun|YouTube Video Title|SEO-Optimized|Sun[\'&#x27;]*s Impact|Zodiac Signs Vedic Astrology).*?<\/h[1-6]>', '', rest, flags=re.DOTALL | re.IGNORECASE)
                body = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'<p style=\"margin:0.25rem 0;\">\1</p>', rest, flags=re.DOTALL)
                body = re.sub(r'<p[^>]*>.*?(?:Surya in 12|YouTube Video Title|SEO-Optimized|Sun[\'&#x27;]*s Impact).*?</p>', '', body, flags=re.DOTALL | re.IGNORECASE)
                body = re.sub(r'[☀️🌞🔥📽️]', '', body)
                body = re.sub(r'</?div[^>]*>', '', body).strip()
                cleaned_items.append(f'<div class=\"sun-effect-item\" style=\"margin-bottom:0.75rem;\"><div style=\"color:var(--accent-gold); font-weight:700; font-size:0.9rem; border-bottom:1px dashed var(--page-border); padding-bottom:3px;\">{title}</div><div style=\"font-size:0.84rem; line-height:1.55; margin-top:0.25rem;\">{body}</div></div>')
        return '\n'.join(cleaned_items)

    # 4.3 Sun in 12 Houses (Split into Houses 1-6 and 7-12)
    pos_1st_house = ch4_text.find('1. 1st House')
    pos_houses_start = ch4_text.rfind('<h4', 0, pos_1st_house) if pos_1st_house != -1 else -1

    idx_surya_houses = ch4_text.find('Surya in 12 Houses')
    if idx_surya_houses != -1:
        pos_houses_end = ch4_text.rfind('<div class="slide-indicator"', 0, idx_surya_houses)
        if pos_houses_end == -1:
            pos_houses_end = ch4_text.rfind('<h4', 0, idx_surya_houses)
    else:
        pos_houses_end = ch4_text.find('Effect of Sun in 12 Zodiac Signs')
        if pos_houses_end != -1:
            pos_houses_end = ch4_text.rfind('<h4', 0, pos_houses_end)

    if pos_houses_start != -1 and pos_houses_end != -1:
        sun_houses_raw = ch4_text[pos_houses_start:pos_houses_end]
        idx_7th = sun_houses_raw.find('7. 7th House')
        if idx_7th != -1:
            pos_7th = sun_houses_raw.rfind('<h4', 0, idx_7th)
            houses_1_6 = clean_sun_block(sun_houses_raw[:pos_7th])
            houses_7_12 = clean_sun_block(sun_houses_raw[pos_7th:])
            
            p_sun_1_6 = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 4 • Sun in Houses</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">सूर्य देव: भाव १ से ६ फल</h3>
              </div>
              <div class="rule-card">
                <div class="rule-body" style="font-size:0.85rem; line-height:1.6;">
                  {houses_1_6}
                </div>
              </div>
            </div>
            """
            pages.append({
                "chapter": "Ch 4: भाव एवं राशियों में ग्रह",
                "title": "सूर्य देव: भाव १ से ६ फलित विचार",
                "content": p_sun_1_6
            })
            
            p_sun_7_12 = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 4 • Sun in Houses</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">सूर्य देव: भाव ७ से १२ फल</h3>
              </div>
              <div class="rule-card">
                <div class="rule-body" style="font-size:0.85rem; line-height:1.6;">
                  {houses_7_12}
                </div>
              </div>
            </div>
            """
            pages.append({
                "chapter": "Ch 4: भाव एवं राशियों में ग्रह",
                "title": "सूर्य देव: भाव ७ से १२ फलित विचार",
                "content": p_sun_7_12
            })
            
    # 4.4 Sun in 12 Signs (Split into Signs 1-6 and 7-12)
    pos_1st_sign = ch4_text.find('1. Aries')
    pos_signs_start = ch4_text.rfind('<h4', 0, pos_1st_sign) if pos_1st_sign != -1 else -1

    pos_yt = ch4_text.find('YouTube Video Title')
    if pos_yt != -1:
        pos_signs_end = ch4_text.rfind('<h4', 0, pos_yt)
    else:
        pos_signs_end = len(ch4_text)

    if pos_signs_start != -1:
        sun_signs_raw = ch4_text[pos_signs_start:pos_signs_end]
        idx_libra = sun_signs_raw.find('7. Libra')
        if idx_libra != -1:
            pos_libra = sun_signs_raw.rfind('<h4', 0, idx_libra)
            signs_1_6 = clean_sun_block(sun_signs_raw[:pos_libra])
            signs_7_12 = clean_sun_block(sun_signs_raw[pos_libra:])
            
            p_signs_1_6 = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 4 • Sun in Signs</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">सूर्य देव: मेष से कन्या राशि फल</h3>
              </div>
              <div class="rule-card">
                <div class="rule-body" style="font-size:0.85rem; line-height:1.6;">
                  {signs_1_6}
                </div>
              </div>
            </div>
            """
            pages.append({
                "chapter": "Ch 4: भाव एवं राशियों में ग्रह",
                "title": "सूर्य देव: मेष से कन्या राशि फल",
                "content": p_signs_1_6
            })
            
            p_signs_7_12 = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 4 • Sun in Signs</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">सूर्य देव: तुला से मीन राशि फल</h3>
              </div>
              <div class="rule-card">
                <div class="rule-body" style="font-size:0.85rem; line-height:1.6;">
                  {signs_7_12}
                </div>
              </div>
            </div>
            """
            pages.append({
                "chapter": "Ch 4: भाव एवं राशियों में ग्रह",
                "title": "सूर्य देव: तुला से मीन राशि फल",
                "content": p_signs_7_12
            })

# ==============================================================================
# CHAPTER 5: Medical Astrology Analysis (27 Tables)
# ==============================================================================
ch5_titles = [
    "सूर्य देव: शारीरिक अंग व रोग संबंध",
    "चन्द्रमा: शारीरिक अंग व रोग संबंध",
    "मंगल देव: शारीरिक अंग व रोग संबंध",
    "बुध देव: शारीरिक अंग व रोग संबंध",
    "बृहस्पति (गुरु): शारीरिक अंग व रोग संबंध",
    "शुक्र देव: शारीरिक अंग व रोग संबंध",
    "शनि देव: शारीरिक अंग व रोग संबंध",
    "राहु देव: शारीरिक अंग व रोग संबंध",
    "केतु देव: शारीरिक अंग व रोग संबंध",
    "प्रथम भाव (लग्न): शारीरिक अंग व रोग निदान",
    "द्वितीय भाव: शारीरिक अंग व रोग निदान",
    "तृतीय भाव: शारीरिक अंग व रोग निदान",
    "चतुर्थ भाव: शारीरिक अंग व रोग निदान",
    "पंचम भाव: शारीरिक अंग व रोग निदान",
    "षष्ठ भाव: शारीरिक अंग व रोग निदान",
    "सप्तम भाव: शारीरिक अंग व रोग निदान",
    "अष्टम भाव: शारीरिक अंग व रोग निदान",
    "नवम भाव: शारीरिक अंग व रोग निदान",
    "दशम भाव: शारीरिक अंग व रोग निदान",
    "एकादश भाव: शारीरिक अंग व रोग निदान",
    "द्वादश भाव: शारीरिक अंग व रोग निदान",
    "१२ भाव, शारीरिक अंग एवं व्याधि समन्वय तालिका",
    "१२ राशियां, शारीरिक अंग और विशिष्ट रोग तालिका",
    "कैंसर (अर्भुद रोग) के ज्योतिषीय कारण व मुख्य बिंदु",
    "सामान्य कैंसर (स्तन व फेफड़े): ग्रह योग व विश्लेषण",
    "रक्त कैंसर (ल्यूकीमिया): ज्योतिषीय योग व विश्लेषण",
    "त्वचा कैंसर (मेलानोमा): ग्रह योग व विश्लेषण"
]

ch5_m = re.search(r'<section\b[^>]*id=[\"\']chapter-5[\"\'][^>]*>(.*?)</section>', raw_content, re.DOTALL)
if ch5_m:
    ch5_text = ch5_m.group(1)
    ch5_pairs = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch5_text, re.DOTALL)
    
    for idx, (cb, tb, tid) in enumerate(ch5_pairs):
        caption = ch5_titles[idx] if idx < len(ch5_titles) else f"चिकित्सा ज्योतिष तालिका {idx+1}"
        cb_clean = sanitize_content_block(cb) if cb else ""
        cb_clean = re.sub(r'<h2[^>]*id=\"Page-5[^\"]*\"[^>]*>.*?</h2>', '', cb_clean)
        
        # Eliminate stacked duplicate title bar
        tb_clean = re.sub(r'<div class=\"table-caption\">.*?</div>', '', tb)
        tb_clean = clean_table_glyphs(tb_clean)
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 5 • Medical Section {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-crimson);">{caption}</h3>
          </div>
          {cb_clean}
          {SCROLL_HINT_HTML}
          <div class="astro-table-container">
            {tb_clean}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 5: मेडिकल व स्वास्थ्य ज्योतिष",
            "title": caption,
            "content": content
        })

# ==============================================================================
# CHAPTER 6: Nakshatra & Pada Analysis (11 Tables)
# ==============================================================================
ch6_titles = [
    "२७ नक्षत्र, विस्तार व राशि सीमा विभाजन",
    "२७ नक्षत्र, देवता व पद नामाक्षर तालिका",
    "नक्षत्र, देवता एवं ग्रह स्वामी तालिका",
    "नक्षत्र स्वामी व दशा अधिपति शास्त्रीय सूत्र",
    "२७ नक्षत्र एवं स्वामी सम्पूर्ण ज्ञानकोश तालिका",
    "आश्लेषा नक्षत्र: ४ पद एवं ग्रह फल विश्लेषण",
    "पुष्य नक्षत्र: ४ पद एवं नवमांश ग्रह प्रभाव",
    "अश्विनी नक्षत्र: ४ पद व नवमांश अधिपति तालिका",
    "अश्विनी नक्षत्र: पद ध्वनि, प्रतीक व मूल स्वभाव",
    "अश्विनी नक्षत्र में ९ ग्रहों का फलित विश्लेषण",
    "अश्विनी नक्षत्र: ४ पद, नवमांश व ग्रह संबंध सारांश"
]

ch6_m = re.search(r'<section\b[^>]*id=[\"\']chapter-6[\"\'][^>]*>(.*?)</section>', raw_content, re.DOTALL)
if ch6_m:
    ch6_text = ch6_m.group(1)
    ch6_pairs = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch6_text, re.DOTALL)
    
    for idx, (cb, tb, tid) in enumerate(ch6_pairs):
        caption = ch6_titles[idx] if idx < len(ch6_titles) else f"नक्षत्र पद तालिका {idx+1}"
        cb_clean = sanitize_content_block(cb) if cb else ""
        cb_clean = re.sub(r'<h2[^>]*id=\"Page-6[^\"]*\"[^>]*>.*?</h2>', '', cb_clean)
        
        # Eliminate stacked duplicate title bar
        tb_clean = re.sub(r'<div class=\"table-caption\">.*?</div>', '', tb)
        tb_clean = clean_table_glyphs(tb_clean)
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 6 • Pada Section {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{caption}</h3>
          </div>
          {cb_clean}
          {SCROLL_HINT_HTML}
          <div class="astro-table-container">
            {tb_clean}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 6: नक्षत्र पद व ग्रह विश्लेषण",
            "title": caption,
            "content": content
        })

# ==============================================================================
# BACK MATTER (Colophon & Sacred Benediction)
# ==============================================================================
colophon_page = """
<div class="cover-page-inner" style="border: 2px solid var(--accent-gold);">
  <div class="cover-tag">समापन पृष्ठ • Sacred Colophon</div>

  <div class="shloka-box" style="margin:1.5rem 0; width:100%;">
    <div class="shloka-sanskrit">
      ॐ असतो मा सद्गमय । तमसो मा ज्योतिर्गमय ।<br>
      मृत्योर्मा अमृतं गमय । ॐ शान्तिः शान्तिः शान्तिः ॥
    </div>
    <div class="shloka-meaning">
      "Lead me from falsehood to truth, from darkness to cosmic light, from mortality to spiritual immortality."
    </div>
    <span class="shloka-source">बृहदारण्यकोपनिषद् (Brihadaranyaka Upanishad)</span>
  </div>

  <div style="max-width:500px; margin:1rem auto; font-size:0.88rem; line-height:1.6; color:var(--text-secondary);">
    <p>
      यह महाग्रंथ वैदिक ज्योतिष, खगोल गणित एवं आयुर्वेद-ज्योतिष का सारगर्भित संकलन है। 
      आशा है कि यह ग्रंथ सभी ज्योतिष प्रेमियों, शोधार्थियों एवं अभ्यासकर्ताओं के लिए एक विश्वसनीय मार्गदर्शक सिद्ध होगा।
    </p>
  </div>

  <div class="cover-author-block" style="margin-top:auto;">
    <div class="cover-author-label">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</div>
    <div class="cover-author-name">ज्योतिषाचार्य Ashutosh Kumar Choubey</div>
    <div class="cover-author-role">Copyright © 2026. All rights reserved.</div>
    <div style="margin-top:0.85rem; display:flex; flex-direction:column; align-items:center; gap:0.6rem;">
      <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem;">
        <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="contact-channel-badge" style="border-color:var(--accent-gold); color:var(--accent-gold) !important; font-weight:700;">
          <span class="contact-icon">🌐</span>
          <span><strong>t.worldgyan.com</strong></span>
        </a>
        <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge" style="margin-top:0;">
          <span class="yt-play-icon">▶</span>
          <span>YouTube: <strong>@TantraGyan108</strong></span>
        </a>
      </div>
      <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.8rem; font-size:0.86rem; margin-top:0.25rem;">
        <a href="mailto:tantraresearchcenter@gmail.com" style="color:var(--text-secondary); text-decoration:none; font-weight:600;">✉️ tantraresearchcenter@gmail.com</a>
        <span style="color:var(--border-color);">•</span>
        <a href="tel:+919658476170" style="color:var(--text-secondary); text-decoration:none; font-weight:600;">📞 +91 9658476170</a>
      </div>
    </div>
  </div>
</div>
"""
pages.append({
    "chapter": "समापन • Colophon",
    "title": "समापन पृष्ठ • उपनिषद् मंगल कामना व आधिकारिक संपर्क",
    "content": colophon_page
})

total_pages = len(pages)
print(f"Total compiled pages: {total_pages}")

# Build TOC Items HTML (Grouped cleanly by Chapter)
toc_items_html = []
current_chapter = None
for p_idx, p in enumerate(pages):
    ch_raw = p['chapter'].split('•')[0].strip()
    if ch_raw != current_chapter:
        current_chapter = ch_raw
        toc_items_html.append(f"""
        <div class="toc-chapter-header">
          <span class="toc-chapter-pill">📌 {current_chapter}</span>
        </div>
        """)
    toc_items_html.append(f"""
    <a href="#page-{p_idx+1}" class="toc-item" data-goto="{p_idx+1}">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.{p_idx+1}</span>
        <span class="toc-item-title">{p['title']}</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>
    """)
toc_html = "\n".join(toc_items_html)

# Build Raw Page Data Nodes HTML
pages_data_html = []
for p_idx, p in enumerate(pages):
    pages_data_html.append(f"""
    <div class="book-page-data" id="page-data-{p_idx+1}" data-page="{p_idx+1}" data-chapter="{html.escape(p['chapter'])}" data-title="{html.escape(p['title'])}" style="display:none;">
      {p['content']}
    </div>
    """)
all_pages_html = "\n".join(pages_data_html)

def make_initial_sheet_markup(pageNum, pageData, totalPages):
    ch = pageData["chapter"]
    ti = pageData["title"]
    co = pageData["content"]
    return f"""
        <div class="page-header">
          <div class="page-header-info">
            <span class="page-header-title">
              <span class="chapter-wheel">☸</span> {ch}
            </span>
            <span class="page-header-subtitle">{ti}</span>
          </div>
        </div>
        <div class="page-body">
          {co}
        </div>
        <div class="page-footer">
          <span class="page-footer-title">वैदिक ज्योतिष महाग्रंथ सरलीकृत</span>
          <span class="page-number-display">Page {pageNum} of {totalPages}</span>
        </div>
    """

initial_left_html = make_initial_sheet_markup(1, pages[0], total_pages)
initial_right_html = make_initial_sheet_markup(2, pages[1], total_pages)

# Final HTML Template
html_template = f"""<!DOCTYPE html>
<html lang="hi" data-theme="parchment" data-lang-mode="bilingual">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>वैदिक ज्योतिष महाग्रंथ सरलीकृत | Complete Vedic Astrology Compendium Simplified</title>
  
  <!-- SEO Best Practice Meta Tags -->
  <meta name="description" content="वैदिक ज्योतिष महाग्रंथ सरलीकृत by Astrologer Ashutosh Kumar Choubey, Published by Tantra Gyan Research Center. Comprehensive authentic compendium covering Navagraha Karakatva, 17 Classical Raja Yogas, 27 Nakshatras & 108 Padas, Deeptadi Avasthas, and Planetary Predictions.">
  <meta name="keywords" content="Tantra Gyan, Vedic Astrology, Astrologer Ashutosh Kumar Choubey, Navagraha Karakatva, Raja Yoga, Medical Astrology, Cancer in Astrology, Nakshatra Padas, Jyotish Shastra, Parashara, Phaladeepika">
  <meta name="author" content="Ashutosh Kumar Choubey">
  <meta name="robots" content="index, follow">
  
  <!-- OpenGraph Metadata -->
  <meta property="og:title" content="वैदिक ज्योतिष महाग्रंथ सरलीकृत | Complete Vedic Astrology Compendium Simplified">
  <meta property="og:description" content="Comprehensive Authentic Vedic Astrology Reference Book by Astrologer Ashutosh Kumar Choubey.">
  <meta property="og:type" content="book">
  <meta property="og:url" content="https://t.worldgyan.com">
  <link rel="canonical" href="https://t.worldgyan.com">
  
  <!-- Standard High-Quality Google Fonts for Vedic & Modern Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400&family=Inter:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&family=Noto+Serif+Devanagari:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
  
  <!-- Standard CSS Files for Maximum Maintainability -->
  <link rel="stylesheet" href="css/book.css?v=3.3">
  <link rel="stylesheet" href="css/tables.css?v=3.3">
  
  <!-- Schema.org JSON-LD Educational Book Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Book",
    "name": "वैदिक ज्योतिष महाग्रंथ सरलीकृत (Complete Vedic Astrology Compendium Simplified)",
    "alternateName": "Complete Vedic Astrology Compendium Simplified",
    "url": "https://t.worldgyan.com",
    "author": {{
      "@type": "Person",
      "name": "Ashutosh Kumar Choubey",
      "jobTitle": "Vedic Astrologer & Researcher",
      "url": "https://t.worldgyan.com",
      "sameAs": [
        "https://www.youtube.com/@TantraGyan108",
        "https://t.worldgyan.com"
      ],
      "email": "tantraresearchcenter@gmail.com",
      "telephone": "+919658476170"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)",
      "url": "https://t.worldgyan.com",
      "sameAs": [
        "https://www.youtube.com/@TantraGyan108"
      ],
      "email": "tantraresearchcenter@gmail.com",
      "telephone": "+919658476170"
    }},
    "datePublished": "2026",
    "inLanguage": ["hi", "en"],
    "bookFormat": "EBook",
    "numberOfPages": {total_pages},
    "genre": "Vedic Astrology / Jyotish / Medical Astrology",
    "about": [
      "Vedic Astrology",
      "Navagraha Karakatva",
      "Pancha Mahapurusha Raja Yogas",
      "27 Nakshatras and 108 Padas",
      "Medical Astrology and Cancer Disease"
    ]
  }}
  </script>
</head>
<body>

  <!-- Floating Book App Header -->
  <header class="app-header">
    <a href="#page-1" class="brand-section" onclick="if(window.bookEngine) window.bookEngine.goToPage(1, true);">
      <div class="brand-logo">
        <img src="assets/yantra.svg" alt="Tantra Gyan Mandala" width="34" height="34">
      </div>
      <div class="brand-titles">
        <span class="brand-name">तंत्र ज्ञान <span>Tantra Gyan</span></span>
        <span class="brand-tagline">ज्योतिषाचार्य Ashutosh Kumar Choubey</span>
      </div>
    </a>

    <!-- Toolbar Controls -->
    <div class="toolbar-controls">
      <!-- Search Input Container with Dropdown Results -->
      <div class="search-box" id="search-box-container">
        <span class="search-icon" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        </span>
        <input type="text" id="book-search" class="search-input" placeholder="खोजें / Search (e.g. Moon, सूर्य)..." aria-label="Search Book" autocomplete="off">
        <button type="button" id="search-clear-btn" class="search-clear-btn" title="Clear search" aria-label="Clear search" style="display:none;">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
        <span id="search-counter" class="search-count" title="Click to view all matching pages"></span>
        
        <!-- Live Search Results Dropdown -->
        <div id="search-dropdown" class="search-dropdown" style="display:none;" role="region" aria-label="Search Results">
          <div class="search-dropdown-header">
            <span id="search-dropdown-title" class="search-dropdown-title">परिणाम (Search Results)</span>
            <button type="button" id="search-dropdown-close" class="search-dropdown-close" title="Close" aria-label="Close search">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
          </div>
          <div id="search-results-list" class="search-results-list"></div>
        </div>
      </div>

      <!-- TOC Toggle Button -->
      <button class="tool-btn" id="btn-toc-toggle" title="Open Table of Contents (विषय-सूची)">
        <span>📖</span> <span>विषय-सूची</span>
      </button>

      <!-- Bookmark Button -->
      <button class="tool-btn" id="btn-bookmark-toggle" title="Saved Bookmarks (सहेजे गए बुकमार्क)">
        <span>🔖</span> <span id="bookmark-btn-label">बुकमार्क</span>
        <span id="bookmark-count-badge" class="badge-count" style="display:none;">0</span>
      </button>

      <!-- Official Website Link -->
      <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="tool-btn website-header-btn" title="Website: t.worldgyan.com" style="color:var(--accent-gold); font-weight:700; border-color:rgba(200,157,61,0.4); text-decoration:none;">
        <span style="font-size:0.95rem;">🌐</span> <span>t.worldgyan.com</span>
      </a>

      <!-- YouTube Channel Link -->
      <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="tool-btn yt-header-btn" title="YouTube: @TantraGyan108" style="color:#ef4444; font-weight:700; border-color:rgba(239,68,68,0.4); text-decoration:none;">
        <span style="font-size:0.95rem;">▶</span> <span>@TantraGyan108</span>
      </a>

      <!-- Language Mode Switcher -->
      <div class="lang-switcher" title="Switch Reading Language">
        <button class="lang-btn" data-lang="hindi"><span class="lang-code-tag">HI</span> हिंदी</button>
        <button class="lang-btn" data-lang="english"><span class="lang-code-tag">EN</span> English</button>
        <button class="lang-btn active" data-lang="bilingual"><span class="lang-code-tag">ALL</span> द्विभाषी</button>
      </div>

      <!-- Theme Switcher -->
      <button class="tool-btn" id="btn-theme-toggle" title="Toggle Theme (भोजपत्र / रात्रि / श्वेत)">
        <span>📜</span> <span>भोजपत्र</span>
      </button>

      <!-- Dual / Single Spread Toggle -->
      <button class="tool-btn" id="btn-layout-toggle" title="Toggle Spread Layout (दो पृष्ठ / एकल पृष्ठ)">
        <span>📖</span> <span>दो पृष्ठ</span>
      </button>

      <!-- Sound Mute Toggle -->
      <button class="tool-btn" id="btn-sound-toggle" title="Page Turn Sound Effect" style="padding:0.45rem 0.55rem;">
        <span>🔊</span>
      </button>

      <!-- Font Zoom Segmented Control -->
      <div class="font-zoom-group" title="Adjust Text Size">
        <button class="font-zoom-btn" id="btn-font-dec" title="Decrease Font Size">A−</button>
        <button class="font-zoom-btn" id="btn-font-inc" title="Increase Font Size">A+</button>
      </div>

      <!-- Fullscreen -->
      <button class="tool-btn" id="btn-fullscreen" title="Toggle Fullscreen" style="padding:0.45rem 0.6rem;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg></button>
    </div>
  </header>

  <!-- Reading Progress Bar -->
  <div class="reading-progress-track">
    <div class="reading-progress-fill" id="reading-progress-fill"></div>
  </div>

  <!-- Main Book Reading Stage -->
  <main class="main-stage">
    <div class="book-container dual-page-layout">
      <!-- Decorative Gilded Corners -->
      <div class="corner-ornament corner-tl"></div>
      <div class="corner-ornament corner-tr"></div>
      <div class="corner-ornament corner-bl"></div>
      <div class="corner-ornament corner-br"></div>

      <!-- Silk Ribbon Bookmark -->
      <div class="silk-bookmark" title="Click to bookmark this page"></div>

      <!-- Center Spine Crease & Shadow -->
      <div class="book-spine-crease"></div>

      <!-- Turn Page Arrow Buttons -->
      <button class="nav-arrow-btn nav-prev" id="btn-prev-page" title="Previous Page (Left Arrow)">‹</button>
      <button class="nav-arrow-btn nav-next" id="btn-next-page" title="Next Page (Right Arrow / Spacebar)">›</button>

      <!-- Two-Page Spread Container -->
      <div class="book-pages-wrapper">
        <section class="page-sheet left-page" id="left-page-container" aria-label="Left Page">
{initial_left_html}
        </section>
        <section class="page-sheet right-page" id="right-page-container" aria-label="Right Page">
{initial_right_html}
        </section>
      </div>
    </div>
  </main>

  <!-- Bottom Reading Controller Bar -->
  <nav class="bottom-reading-bar" aria-label="Book Navigation Bar">
    <div style="display:flex; align-items:center; gap:0.35rem;">
      <button class="tool-btn nav-edge-btn" onclick="if(window.bookEngine) window.bookEngine.goToPage(1, true);" title="First Page (Home)">« प्रारंभ</button>
      <button class="tool-btn nav-step-btn" id="btn-prev-bottom" onclick="if(window.bookEngine) window.bookEngine.prevPage();" title="Previous Page">‹ पिछला</button>
    </div>

    <div class="slider-container">
      <input type="range" id="page-slider" class="page-slider" min="1" max="{total_pages}" value="1" aria-label="Page Position">
      <span class="page-counter-badge" id="page-counter-badge">Page 1 of {total_pages}</span>
    </div>

    <div style="display:flex; align-items:center; gap:0.35rem;">
      <button class="tool-btn nav-step-btn" id="btn-next-bottom" onclick="if(window.bookEngine) window.bookEngine.nextPage();" title="Next Page">अगला ›</button>
      <button class="tool-btn nav-edge-btn" onclick="if(window.bookEngine) window.bookEngine.goToPage({total_pages}, true);" title="Last Page (End)">अंतिम »</button>
    </div>
  </nav>

  <!-- Table of Contents Modal Drawer -->
  <div class="toc-overlay" id="toc-overlay" role="dialog" aria-modal="true" aria-labelledby="toc-modal-title">
    <div class="toc-modal">
      <div class="toc-header">
        <h3 class="toc-title" id="toc-modal-title">
          <span>📖</span> विषय-सूची (Table of Contents)
        </h3>
        <button class="toc-close-btn" id="toc-close-btn" title="Close Index" aria-label="Close Table of Contents">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <div class="toc-body">
        <div class="toc-list">
          {toc_html}
        </div>
      </div>
    </div>
  </div>

  <!-- Bookmark Drawer Modal -->
  <div class="bookmark-overlay" id="bookmark-overlay" role="dialog" aria-modal="true" aria-labelledby="bookmark-modal-title">
    <div class="bookmark-modal" id="bookmark-modal">
      <div class="bookmark-header">
        <h3 class="bookmark-title" id="bookmark-modal-title">
          <span>🔖</span> सहेजे गए बुकमार्क (Saved Bookmarks)
        </h3>
        <button class="bookmark-close-btn" id="bookmark-close-btn" title="Close Bookmarks" aria-label="Close Bookmarks">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <div class="bookmark-action-bar">
        <button id="btn-bookmark-current" class="btn-bookmark-action">
          <span id="bookmark-current-icon">➕</span>
          <span id="bookmark-current-text">वर्तमान पृष्ठ बुकमार्क करें</span>
        </button>
      </div>
      <div class="bookmark-body">
        <div id="bookmark-list" class="bookmark-list">
          <!-- Dynamically populated bookmarks -->
        </div>
      </div>
    </div>
  </div>

  <!-- Floating Toast Notification -->
  <div id="book-toast" class="book-toast" role="status" aria-live="polite"></div>

  <!-- Raw Page Data Repository (Parsed & Rendered Dynamically) -->
  <div id="book-pages-store" style="display:none;" aria-hidden="true">
    {all_pages_html}
  </div>

  <!-- Scripts -->
  <script src="js/sound.js?v=3.3"></script>
  <script src="js/book-engine.js?v=3.3"></script>
  <script src="js/book-ui.js?v=3.3"></script>
</body>
</html>
"""

with open(target_file, "w", encoding="utf-8") as out:
    out.write(html_template)

print(f"Successfully generated {target_file} with {total_pages} pages!")
