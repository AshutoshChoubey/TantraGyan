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

# Helper to clean titles
def clean_text(s):
    return re.sub(r'<[^>]+>', '', s).strip()

pages = []

# ==============================================================================
# FRONT MATTER PAGES (1 to 5)
# ==============================================================================

# PAGE 1: Grand Book Cover
page_1 = """
<div class="cover-page-inner">
  <div class="cover-tag">प्रामाणिक वैदिक ज्योतिष महाग्रंथ • Digital Edition 2026</div>
  
  <div class="cover-yantra">
    <img src="assets/yantra.svg" alt="Sacred Sri Yantra Emblem" width="130" height="130" style="filter: drop-shadow(0 4px 15px rgba(200, 157, 61, 0.45));">
  </div>

  <h1 class="cover-title-hindi">तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ</h1>
  <h2 class="cover-title-english">Tantra Gyan: Complete Vedic Astrology Compendium</h2>

  <div class="cover-divider"></div>

  <p class="cover-subtitle">
    <strong>नवग्रह कारकत्व, 17 शास्त्रीय राजयोग, 27 नक्षत्र व 108 पद विश्लेषण, दीप्तादि 9 अवस्थाएं, भाव-राशि फल तथा संपूर्ण मेडिकल एस्ट्रोलॉजी व कैंसर रोग निदान।</strong><br>
    <span style="font-size:0.85rem; color:var(--text-muted); display:inline-block; margin-top:0.4rem;">
      Comprehensive Classical Sutras, Astronomical Motion & Empirical Ayur-Jyotish Diagnostics
    </span>
  </p>

  <div class="cover-author-block">
    <div class="cover-author-label">लेखक एवं ज्योतिषाचार्य (Author & Astrologer)</div>
    <div class="cover-author-name">Ashutosh Kumar Choubey</div>
    <div class="cover-author-role">Founder, Tantra Gyan Knowledge Systems</div>
    <div style="margin-top:0.75rem;">
      <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge">
        <span class="yt-play-icon">▶</span>
        <span>YouTube: <strong>@TantraGyan108</strong></span>
      </a>
    </div>
  </div>
</div>
"""
pages.append({
    "chapter": "मुखपृष्ठ • Cover",
    "title": "तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ",
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
      <div class="author-meta">Vedic Astrologer, Tantra Researcher & Founder of Tantra Gyan</div>
      <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
        समर्पित वैदिक ज्योतिषी एवं शोधकर्ता, जिन्होंने शास्त्रीय ज्योतिष ग्रंथों और आधुनिक विश्लेषणात्मक पद्धतियों के समन्वय से 'तंत्र ज्ञान' (Tantra Gyan) ज्ञानकोश की स्थापना की है।
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
      <div class="rule-title">🔬 मेडिकल एस्ट्रोलॉजी में विशेष योगदान (Pioneering Ayur-Jyotish Research)</div>
    </div>
    <div class="rule-body">
      <p>
        आशुतोष जी ने चिकित्सा ज्योतिष (Medical Astrology) के क्षेत्र में विशेष रूप से <strong>कैंसर (Arbuda Roga), ल्यूकीमिया (रक्त कैंसर), स्तन एवं त्वचा विकारों</strong> के ज्योतिषीय कारकों (राहु, शनि, मंगल, षष्ठ/अष्टम भाव) के सूक्ष्म संयोजनों पर अत्यंत प्रामाणिक अनुसंधान प्रस्तुत किया है।
      </p>
      <p style="font-size:0.84rem; color:var(--text-muted); margin-top:0.4rem;">
        इनका दृढ़ विश्वास है कि ज्योतिष भविष्य के प्रति असहाय समर्पण नहीं, बल्कि कर्म सुधार और आत्म-बोध का प्रकाश स्तंभ है।
      </p>
    </div>
  </div>

  <div style="margin-top:1.25rem; padding:1.1rem; border:1px dashed var(--accent-gold); border-radius:10px; background:rgba(179,127,25,0.06); text-align:center;">
    <strong style="color:var(--text-heading); font-size:0.92rem;">आधिकारिक शोध एवं संपर्क मंच (Official Channels & Contact):</strong><br>
    <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem; margin-top:0.75rem;">
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
    "title": "Astrologer Ashutosh Kumar Choubey",
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
    वैदिक ज्योतिष का ज्ञान अनंत सागर की भांति विस्तृत है। साधारण जिज्ञासु और गंभीर अभ्यासकर्ता प्रायः बिखरे हुए सूत्रों, परस्पर विरोधी मतों और जटिल संस्कृत टीकाओं में उलझ जाते हैं। <strong>तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ</strong> को एक <em>"हाई-डेंसिटी प्रेक्टिशनर नोटबुक" (Concise Practitioner Notebook)</em> के रूप में तैयार किया गया है।
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
    "title": "ग्रंथ का उद्देश्य एवं दर्शन (Scope of Compendium)",
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
    "title": "वैधानिक सूचना एवं अस्वीकरण",
    "content": page_4
})

# PAGE 5: Table of Contents (Index)
page_5 = """
<div class="page-inner-content">
  <div class="chapter-header" style="margin-bottom:1rem;">
    <div class="chapter-number">Index & Navigation</div>
    <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-gold);">विषय-सूची — Table of Contents</h2>
  </div>

  <div style="display:flex; flex-direction:column; gap:0.65rem;">
    <div style="background:var(--page-bg-alt); border:1px solid var(--page-border); border-radius:6px; padding:0.65rem 0.85rem; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Ch 1</span>
        <strong style="font-size:0.88rem;">प्रस्तावना, लेखक परिचय एवं वैधानिक सूचना</strong>
      </div>
      <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 1 - 5</span>
    </div>

    <div style="background:var(--page-bg-alt); border:1px solid var(--page-border); border-radius:6px; padding:0.65rem 0.85rem; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Ch 2</span>
        <strong style="font-size:0.88rem;">नवग्रह कारकत्व एवं 17 शास्त्रीय राजयोग</strong>
      </div>
      <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 6 - 20</span>
    </div>

    <div style="background:var(--page-bg-alt); border:1px solid var(--page-border); border-radius:6px; padding:0.65rem 0.85rem; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Ch 3</span>
        <strong style="font-size:0.88rem;">राशि, नक्षत्र, ग्रह गति एवं विंशोत्तरी महादशा</strong>
      </div>
      <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 21 - 37</span>
    </div>

    <div style="background:var(--page-bg-alt); border:1px solid var(--page-border); border-radius:6px; padding:0.65rem 0.85rem; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Ch 4</span>
        <strong style="font-size:0.88rem;">भाव एवं राशियों में ग्रहों का प्रभाव (दीप्तादि 9 अवस्थाएं व सूर्य फल)</strong>
      </div>
      <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 38 - 47</span>
    </div>

    <div style="background:var(--page-bg-alt); border:1px solid var(--page-border); border-radius:6px; padding:0.65rem 0.85rem; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Ch 5</span>
        <strong style="font-size:0.88rem;">मेडिकल एस्ट्रोलॉजी एवं कैंसर रोग विश्लेषण (27 संपूर्ण तालिकाएं)</strong>
      </div>
      <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 48 - 74</span>
    </div>

    <div style="background:var(--page-bg-alt); border:1px solid var(--page-border); border-radius:6px; padding:0.65rem 0.85rem; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Ch 6</span>
        <strong style="font-size:0.88rem;">नक्षत्रों का गहन पद एवं ग्रह विश्लेषण (अश्विनी, आश्लेषा, पुष्य)</strong>
      </div>
      <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 75 - 85</span>
    </div>

    <div style="background:var(--page-bg-alt); border:1px solid var(--page-border); border-radius:6px; padding:0.65rem 0.85rem; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Colophon</span>
        <strong style="font-size:0.88rem;">समापन पृष्ठ, मंगल श्लोक व संपर्क</strong>
      </div>
      <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Page 86</span>
    </div>
  </div>

  <div style="margin-top:1.25rem; font-size:0.82rem; color:var(--text-muted); text-align:center;">
    💡 <em>संकेत: किसी भी पृष्ठ पर सीधे जाने हेतु ऊपरी टूलबार के <strong>📖 विषय-सूची</strong> बटन का उपयोग करें या नीचे स्लाइडर को खिसकाएं।</em>
  </div>
</div>
"""
pages.append({
    "chapter": "अनुक्रमणिका • Index",
    "title": "विषय-सूची (Table of Contents)",
    "content": page_5
})

# ==============================================================================
# CHAPTER 2: Navagraha Karakatva & Classical Raja Yogas (15 Tables)
# ==============================================================================
ch2_m = re.search(r'<section\b[^>]*id=[\"\']chapter-2[\"\'][^>]*>(.*?)</section>', raw_content, re.DOTALL)
if ch2_m:
    ch2_text = ch2_m.group(1)
    ch2_pairs = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch2_text, re.DOTALL)
    
    for idx, (cb, tb, tid) in enumerate(ch2_pairs):
        cap_m = re.search(r'<div class=\"table-caption\">(.*?)</div>', tb, re.DOTALL)
        caption = clean_text(cap_m.group(1)) if cap_m else f"Planetary Karakatva Table {idx+1}"
        
        # Clean up cb and tb to fit book layout
        cb_clean = cb if cb else ""
        # Remove redunant h2 Page 2 marker
        cb_clean = re.sub(r'<h2[^>]*id=\"Page-2[^\"]*\"[^>]*>.*?</h2>', '', cb_clean)
        
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 2 • Section {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{caption}</h3>
          </div>
          {cb_clean}
          <div class="astro-table-container">
            {tb}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 2: नवग्रह कारकत्व व राजयोग",
            "title": caption[:45],
            "content": content
        })

# ==============================================================================
# CHAPTER 3: Rashis, Nakshatras & Astronomical Motion (17 Tables)
# ==============================================================================
ch3_m = re.search(r'<section\b[^>]*id=[\"\']chapter-3[\"\'][^>]*>(.*?)</section>', raw_content, re.DOTALL)
if ch3_m:
    ch3_text = ch3_m.group(1)
    ch3_pairs = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch3_text, re.DOTALL)
    
    for idx, (cb, tb, tid) in enumerate(ch3_pairs):
        cap_m = re.search(r'<div class=\"table-caption\">(.*?)</div>', tb, re.DOTALL)
        caption = clean_text(cap_m.group(1)) if cap_m else f"Astronomical Motion Table {idx+1}"
        
        cb_clean = cb if cb else ""
        cb_clean = re.sub(r'<h2[^>]*id=\"Page-3[^\"]*\"[^>]*>.*?</h2>', '', cb_clean)
        
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 3 • Section {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{caption}</h3>
          </div>
          {cb_clean}
          <div class="astro-table-container">
            {tb}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 3: राशि, नक्षत्र एवं ग्रह गति",
            "title": caption[:45],
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
            <h3 class="chapter-heading" style="font-size:1.2rem; color:var(--accent-gold);">Deeptadi Avastha Explained 🔯 | ग्रहों की स्थिति और 9 अवस्थाएं</h3>
          </div>
          <div class="rule-card">
            <div class="rule-header">
              <div class="rule-title">दीप्तादि 9 अवस्थाएं (Nine Planetary States)</div>
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
            "title": "दीप्तादि 9 अवस्थाएं (Deeptadi Avasthas)",
            "content": page_4_1
        })
    
    # 4.2 Tables 1 to 6 in Ch4
    ch4_tables = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch4_text, re.DOTALL)
    for idx, (cb, tb, tid) in enumerate(ch4_tables):
        cap_m = re.search(r'<div class=\"table-caption\">(.*?)</div>', tb, re.DOTALL)
        caption = clean_text(cap_m.group(1)) if cap_m else f"House & Rashi Table {idx+1}"
        cb_clean = cb if cb else ""
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 4 • Table {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{caption}</h3>
          </div>
          {cb_clean}
          <div class="astro-table-container">
            {tb}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 4: भाव एवं राशियों में ग्रह",
            "title": caption[:45],
            "content": content
        })
    
    # 4.3 Sun in 12 Houses (Split into Houses 1-6 and 7-12)
    pos_sun_houses = ch4_text.find('Sun in 12 Houses')
    pos_sun_signs = ch4_text.find('Effect of Sun in 12 Zodiac Signs')
    if pos_sun_houses != -1 and pos_sun_signs != -1:
        sun_houses_raw = ch4_text[pos_sun_houses:pos_sun_signs]
        
        pos_7th = sun_houses_raw.find('7. 7th House')
        if pos_7th != -1:
            houses_1_6 = re.sub(r'</?div[^>]*>', '', sun_houses_raw[:pos_7th]).strip()
            houses_7_12 = re.sub(r'</?div[^>]*>', '', sun_houses_raw[pos_7th:]).strip()
            
            p_sun_1_6 = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 4 • Sun in Houses</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">🌞 Surya in 12 Houses (Part 1: भाव 1 से 6)</h3>
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
                "title": "सूर्य: भाव 1 से 6 फल",
                "content": p_sun_1_6
            })
            
            p_sun_7_12 = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 4 • Sun in Houses</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">🌞 Surya in 12 Houses (Part 2: भाव 7 से 12)</h3>
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
                "title": "सूर्य: भाव 7 से 12 फल",
                "content": p_sun_7_12
            })
            
    # 4.4 Sun in 12 Signs (Split into Signs 1-6 and 7-12)
    if pos_sun_signs != -1:
        sun_signs_raw = ch4_text[pos_sun_signs:]
        pos_libra = sun_signs_raw.find('7. Libra')
        if pos_libra != -1:
            signs_1_6 = re.sub(r'</?div[^>]*>', '', sun_signs_raw[:pos_libra]).strip()
            signs_7_12 = re.sub(r'</?div[^>]*>', '', sun_signs_raw[pos_libra:]).strip()
            
            p_signs_1_6 = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 4 • Sun in Signs</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">☀️ Surya in 12 Signs (Part 1: मेष से कन्या)</h3>
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
                "title": "सूर्य: मेष से कन्या राशि फल",
                "content": p_signs_1_6
            })
            
            p_signs_7_12 = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 4 • Sun in Signs</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">☀️ Surya in 12 Signs (Part 2: तुला से मीन)</h3>
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
                "title": "सूर्य: तुला से मीन राशि फल",
                "content": p_signs_7_12
            })

# ==============================================================================
# CHAPTER 5: Medical Astrology & Cancer Analysis (27 Tables)
# ==============================================================================
ch5_m = re.search(r'<section\b[^>]*id=[\"\']chapter-5[\"\'][^>]*>(.*?)</section>', raw_content, re.DOTALL)
if ch5_m:
    ch5_text = ch5_m.group(1)
    ch5_pairs = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch5_text, re.DOTALL)
    
    for idx, (cb, tb, tid) in enumerate(ch5_pairs):
        cap_m = re.search(r'<div class=\"table-caption\">(.*?)</div>', tb, re.DOTALL)
        caption = clean_text(cap_m.group(1)) if cap_m else f"Medical Astrology Table {idx+1}"
        cb_clean = cb if cb else ""
        cb_clean = re.sub(r'<h2[^>]*id=\"Page-5[^\"]*\"[^>]*>.*?</h2>', '', cb_clean)
        
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 5 • Medical Section {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-crimson);">{caption}</h3>
          </div>
          {cb_clean}
          <div class="astro-table-container">
            {tb}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 5: मेडिकल एस्ट्रोलॉजी व कैंसर",
            "title": caption[:45],
            "content": content
        })

# ==============================================================================
# CHAPTER 6: Nakshatra & Pada Analysis (11 Tables)
# ==============================================================================
ch6_m = re.search(r'<section\b[^>]*id=[\"\']chapter-6[\"\'][^>]*>(.*?)</section>', raw_content, re.DOTALL)
if ch6_m:
    ch6_text = ch6_m.group(1)
    ch6_pairs = re.findall(r'(<div class=\"content-block\">.*?</div>)?\s*(<div class=\"table-container\"[^>]*id=\"([^\"]+)\".*?>.*?</div>\s*</div>)', ch6_text, re.DOTALL)
    
    for idx, (cb, tb, tid) in enumerate(ch6_pairs):
        cap_m = re.search(r'<div class=\"table-caption\">(.*?)</div>', tb, re.DOTALL)
        caption = clean_text(cap_m.group(1)) if cap_m else f"Nakshatra Pada Table {idx+1}"
        cb_clean = cb if cb else ""
        cb_clean = re.sub(r'<h2[^>]*id=\"Page-6[^\"]*\"[^>]*>.*?</h2>', '', cb_clean)
        
        content = f"""
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 6 • Pada Section {idx+1}</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{caption}</h3>
          </div>
          {cb_clean}
          <div class="astro-table-container">
            {tb}
          </div>
        </div>
        """
        pages.append({
            "chapter": "Ch 6: नक्षत्र पद व ग्रह विश्लेषण",
            "title": caption[:45],
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
    <div class="cover-author-label">Tantra Gyan Sacred Publication</div>
    <div class="cover-author-name">ज्योतिषाचार्य Ashutosh Kumar Choubey</div>
    <div class="cover-author-role">Copyright © 2026. All rights reserved.</div>
    <div style="margin-top:0.85rem; display:flex; flex-direction:column; align-items:center; gap:0.6rem;">
      <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge" style="margin-top:0;">
        <span class="yt-play-icon">▶</span>
        <span>YouTube: <strong>@TantraGyan108</strong></span>
      </a>
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
    "title": "समापन व मंगल कामना",
    "content": colophon_page
})

total_pages = len(pages)
print(f"Total compiled pages: {total_pages}")

# Build TOC Items HTML
toc_items_html = []
for p_idx, p in enumerate(pages):
    toc_items_html.append(f"""
    <a href="#page-{p_idx+1}" class="toc-item" data-goto="{p_idx+1}">
      <div class="toc-item-left">
        <span class="toc-chapter-badge">P.{p_idx+1}</span>
        <span class="toc-item-title">{p['title']}</span>
      </div>
      <span class="toc-page-num">{p['chapter'].split('•')[0].strip()}</span>
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

# Final HTML Template
html_template = f"""<!DOCTYPE html>
<html lang="hi" data-theme="parchment" data-lang-mode="bilingual">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ | Tantra Gyan Complete Vedic Astrology Compendium</title>
  
  <!-- SEO Best Practice Meta Tags -->
  <meta name="description" content="तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ by Astrologer Ashutosh Kumar Choubey. Comprehensive authentic compendium covering Navagraha Karakatva, 17 Classical Raja Yogas, 27 Nakshatras & 108 Padas, Deeptadi Avasthas, and Complete Medical Astrology & Cancer Analysis.">
  <meta name="keywords" content="Tantra Gyan, Vedic Astrology, Astrologer Ashutosh Kumar Choubey, Navagraha Karakatva, Raja Yoga, Medical Astrology, Cancer in Astrology, Nakshatra Padas, Jyotish Shastra, Parashara, Phaladeepika">
  <meta name="author" content="Ashutosh Kumar Choubey">
  <meta name="robots" content="index, follow">
  
  <!-- OpenGraph Metadata -->
  <meta property="og:title" content="तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ | Tantra Gyan Complete Vedic Astrology Compendium">
  <meta property="og:description" content="Comprehensive Authentic Vedic Astrology Reference Book by Astrologer Ashutosh Kumar Choubey.">
  <meta property="og:type" content="book">
  <meta property="og:url" content="https://www.youtube.com/@TantraGyan108">
  
  <!-- Google Fonts for Vedic & Modern Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400&family=Noto+Serif+Devanagari:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Standard CSS Files for Maximum Maintainability -->
  <link rel="stylesheet" href="css/book.css">
  <link rel="stylesheet" href="css/tables.css">
  
  <!-- Schema.org JSON-LD Educational Book Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Book",
    "name": "तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ (Tantra Gyan: Complete Vedic Astrology Compendium)",
    "alternateName": "Tantra Gyan Complete Vedic Astrology Compendium",
    "author": {{
      "@type": "Person",
      "name": "Ashutosh Kumar Choubey",
      "jobTitle": "Vedic Astrologer & Researcher",
      "url": "https://www.youtube.com/@TantraGyan108",
      "email": "tantraresearchcenter@gmail.com",
      "telephone": "+919658476170"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "Tantra Gyan",
      "url": "https://www.youtube.com/@TantraGyan108",
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
      <!-- Search Input -->
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="book-search" class="search-input" placeholder="खोजें / Search book..." aria-label="Search Book">
        <span id="search-counter" class="search-count"></span>
      </div>

      <!-- TOC Toggle Button -->
      <button class="tool-btn" id="btn-toc-toggle" title="Open Table of Contents (विषय-सूची)">
        <span>📖</span> <span>विषय-सूची</span>
      </button>

      <!-- YouTube Channel Link -->
      <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="tool-btn yt-header-btn" title="YouTube: @TantraGyan108" style="color:#ef4444; font-weight:700; border-color:rgba(239,68,68,0.4); text-decoration:none;">
        <span style="font-size:0.95rem;">▶</span> <span>@TantraGyan108</span>
      </a>

      <!-- Language Mode Switcher -->
      <div class="lang-switcher" title="Switch Reading Language">
        <button class="lang-btn" data-lang="hindi">🇮🇳 हिंदी</button>
        <button class="lang-btn" data-lang="english">🇬🇧 English</button>
        <button class="lang-btn active" data-lang="bilingual">🌐 द्विभाषी</button>
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

      <!-- Font Zoom -->
      <button class="tool-btn" id="btn-font-dec" title="Decrease Font Size" style="padding:0.45rem 0.6rem;">A-</button>
      <button class="tool-btn" id="btn-font-inc" title="Increase Font Size" style="padding:0.45rem 0.6rem;">A+</button>

      <!-- Fullscreen -->
      <button class="tool-btn" id="btn-fullscreen" title="Toggle Fullscreen" style="padding:0.45rem 0.6rem;">⛶</button>
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
        <section class="page-sheet left-page" id="left-page-container" aria-label="Left Page"></section>
        <section class="page-sheet right-page" id="right-page-container" aria-label="Right Page"></section>
      </div>
    </div>
  </main>

  <!-- Bottom Reading Controller Bar -->
  <nav class="bottom-reading-bar" aria-label="Book Navigation Bar">
    <div style="display:flex; align-items:center; gap:0.5rem;">
      <button class="tool-btn" onclick="if(window.bookEngine) window.bookEngine.goToPage(1, true);" title="First Page (Home)">⇤ प्रारंभ</button>
      <button class="tool-btn" onclick="if(window.bookEngine) window.bookEngine.prevPage();" title="Previous Page">‹ पिछला</button>
    </div>

    <div class="slider-container">
      <input type="range" id="page-slider" class="page-slider" min="1" max="{total_pages}" value="1" aria-label="Page Position">
      <span class="page-counter-badge" id="page-counter-badge">Page 1 of {total_pages}</span>
    </div>

    <div style="display:flex; align-items:center; gap:0.5rem;">
      <button class="tool-btn" onclick="if(window.bookEngine) window.bookEngine.nextPage();" title="Next Page">अगला ›</button>
      <button class="tool-btn" onclick="if(window.bookEngine) window.bookEngine.goToPage({total_pages}, true);" title="Last Page (End)">अंतिम ⇥</button>
    </div>
  </nav>

  <!-- Table of Contents Modal Drawer -->
  <div class="toc-overlay" id="toc-overlay" role="dialog" aria-modal="true" aria-labelledby="toc-modal-title">
    <div class="toc-modal">
      <div class="toc-header">
        <h3 class="toc-title" id="toc-modal-title">
          <span>📖</span> विषय-सूची (Table of Contents)
        </h3>
        <button class="toc-close-btn" id="toc-close-btn" title="Close Index">✕</button>
      </div>
      <div class="toc-body">
        <div class="toc-list">
          {toc_html}
        </div>
      </div>
    </div>
  </div>

  <!-- Raw Page Data Repository (Parsed & Rendered Dynamically) -->
  <div id="book-pages-store" style="display:none;" aria-hidden="true">
    {all_pages_html}
  </div>

  <!-- Scripts -->
  <script src="js/sound.js"></script>
  <script src="js/book-engine.js"></script>
  <script src="js/book-ui.js"></script>
</body>
</html>
"""

with open(target_file, "w", encoding="utf-8") as out:
    out.write(html_template)

print(f"Successfully generated {target_file} with {total_pages} pages!")
