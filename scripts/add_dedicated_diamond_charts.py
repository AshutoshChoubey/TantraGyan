#!/usr/bin/env python3
"""
Add dedicated full-page North Indian diamond charts across Tantra Gyan book.
Creates 100 canonical pages with 12 prominent full-page visual plates.
"""

import re
import html
import os

INDEX_FILE = "/Users/apple/Movies/ap/TantraGyan/index.html"

with open(INDEX_FILE, "r", encoding="utf-8") as f:
    orig_html = f.read()

# Helper to build a dedicated full-page visual chart plate article
def make_chart_page(chapter, title, subtitle, svg_path, alt_text, caption, card_title, badge_label, card_body):
    content = f"""
<div class="page-inner-content">
  <div class="chapter-header" style="margin-bottom:0.75rem;">
    <div class="chapter-number">{html.escape(chapter)}</div>
    <h3 class="chapter-heading" style="font-size:1.22rem; color:var(--accent-gold);">{html.escape(title)}</h3>
    <div style="font-size:0.86rem; color:var(--text-secondary); margin-top:0.25rem; font-style:italic;">{html.escape(subtitle)}</div>
  </div>
  
  <div class="visual-chart-plate full-page-chart" style="margin: 0.6rem auto 1.1rem auto; text-align: center;">
    <img src="{svg_path}" alt="{html.escape(alt_text)}" style="width:100%; max-width:540px; height:auto; display:block; margin:0 auto; border-radius:12px; box-shadow:0 6px 24px rgba(0,0,0,0.09);" loading="lazy">
    <div class="chart-caption" style="margin-top:0.45rem; font-size:0.84rem; font-style:italic; color:var(--text-muted); text-align:center;">
      {html.escape(caption)}
    </div>
  </div>

  <div class="rule-card" style="margin-top:0.75rem; background:rgba(255,255,255,0.72); border:1px solid rgba(180,83,9,0.25); border-radius:8px; padding:0.8rem 1rem;">
    <div class="rule-header" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
      <div class="rule-title" style="font-weight:800; color:var(--text-heading); font-size:0.92rem;">{card_title}</div>
      <span class="badge-chip badge-gold" style="font-size:0.75rem; padding:2px 8px; border-radius:4px; background:rgba(200,157,61,0.15); color:var(--accent-gold); font-weight:700;">{badge_label}</span>
    </div>
    <div class="rule-body" style="font-size:0.84rem; line-height:1.6; color:var(--text-main);">
      {card_body}
    </div>
  </div>
</div>
"""
    return {
        "chapter": chapter,
        "title": title,
        "content": content
    }

# 1. Extract all existing 88 articles
article_pattern = re.compile(r'<article class="book-page-data" id="page-data-(\d+)" data-page="\d+" data-chapter="([^"]+)" data-title="([^"]+)"[^>]*>(.*?)</article>', re.DOTALL)
existing_articles = []

for m in article_pattern.finditer(orig_html):
    orig_num = int(m.group(1))
    chapter = m.group(2)
    title = m.group(3)
    body = m.group(4)
    
    # Strip any embedded chart plates from host table pages to avoid crowding
    body_clean = re.sub(r'\s*<!-- Dedicated Full-Page Vector[^\n]*-->\s*<div class="visual-chart-plate full-page-chart".*?</div>\s*</div>', '', body, flags=re.DOTALL)
    
    # Strip any other visual-chart-plate if present
    body_clean = re.sub(r'<div class="visual-chart-plate full-page-chart".*?</div>\s*</div>', '', body_clean, flags=re.DOTALL)
    
    existing_articles.append({
        "orig_num": orig_num,
        "chapter": chapter,
        "title": title,
        "body": body_clean
    })

print(f"Extracted {len(existing_articles)} existing articles.")

# Separate into groups based on orig_num
# Pages 1 to 5: Front Matter
front_matter = existing_articles[0:5] # 1 to 5

# Page 6: Index (will be replaced with updated page ranges)
page_6_idx = existing_articles[5]

# Chapter 2 pages (original 7 to 21 -> 15 pages)
ch2_articles = existing_articles[6:21]

# Chapter 3 pages (original 22 to 38 -> 17 pages)
ch3_articles = existing_articles[21:38]

# Chapter 4 pages (original 39 to 49 -> 11 pages)
ch4_articles = existing_articles[38:49]

# Chapter 5 pages (original 50 to 76 -> 27 pages)
ch5_articles = existing_articles[49:76]

# Chapter 6 pages (original 77 to 87 -> 11 pages)
ch6_articles = existing_articles[76:87]

# Back Cover (original 88 -> 1 page)
back_cover = existing_articles[87]

# 2. Build Chapter 1 dedicated full-page diamond charts
ch1_pages = [
    make_chart_page(
        chapter="Ch 1: कालपुरुष कुण्डली व भाव व्यवस्था",
        title="कालपुरुष कुण्डली चक्र — 12 भाव एवं उच्च ग्रह विन्यास",
        subtitle="मेष लग्न आधार • 12 भाव, राशियां, उच्च-नीच ग्रह एवं शारीरिक कार्यक्षेत्र",
        svg_path="assets/icons/lagna_chart.svg",
        alt_text="कालपुरुष कुण्डली चक्र (Kaalpurusha Kundli Diamond Chart)",
        caption="चित्र 1.1: कालपुरुष कुण्डली (Kaalpurusha Kundli) — मेष लग्न आधार, 12 भाव एवं उच्च ग्रहीय विन्यास (सूर्य 10°, चन्द्र 3°, गुरु 5°, बुध 15°, शनि 20°, मंगल 28°, शुक्र 27°)",
        card_title="☸ कालपुरुष कुण्डली का शास्त्रीय रहस्य (Kaalpurusha Cosmic Anatomy)",
        badge_label="वेदांग ज्योतिष",
        card_body="""<p style="margin-bottom:0.4rem;"><strong>12 भाव एवं जीवन आयाम:</strong> प्रथम भाव (तनु/Lagna) से लेकर द्वादश भाव (व्यय/मोक्ष) तक जीवन के समस्त 12 आयामों (शारीरिक, आर्थिक, पराक्रम, पारिवारिक, आध्यात्मिक) का कालपुरुष चक्र द्वारा संचालन होता है।</p>
<p style="margin:0;"><strong>7 प्रमुख उच्च ग्रहीय बिंदु:</strong> सूर्य (मेष 10°), चन्द्रमा (वृषभ 3°), गुरु (कर्क 5°), बुध (कन्या 15°), शनि (तुला 20°), मंगल (मकर 28°), शुक्र (मीन 27°)। जब ग्रह अपने परमोच्च अंशों पर होते हैं, तो वे कुण्डली में अद्वितीय आत्मबल व अखंड राजयोग प्रदान करते हैं।</p>"""
    ),
    make_chart_page(
        chapter="Ch 1: कालपुरुष कुण्डली व भाव व्यवस्था",
        title="कालपुरुष कुण्डली भाव वर्गीकरण महाचक्र — केन्द्र, त्रिकोण, उपचय, त्रिक व मारक भाव",
        subtitle="महर्षि पाराशर प्रतिपादित पांच प्रमुख आध्यात्मिक एवं भौतिक भाव श्रेणियां",
        svg_path="assets/icons/kalpurush_bhavas_diamond_chart.svg",
        alt_text="कालपुरुष कुण्डली भाव वर्गीकरण महाचक्र (Bhava Classification Diamond Chart)",
        caption="चित्र 1.2: कालपुरुष कुण्डली भाव वर्गीकरण महाचक्र — केन्द्र (विष्णु), त्रिकोण (लक्ष्मी), उपचय (वृद्धि), त्रिक (दुःस्थान) एवं मारक भाव व्यवस्था",
        card_title="📜 भाव वर्गीकरण एवं आध्यात्मिक सिद्धांत (Functional House Classification)",
        badge_label="पाराशर होरा",
        card_body="""<p style="margin-bottom:0.4rem;"><strong>केन्द्र (1, 4, 7, 10):</strong> विष्णु स्थान — संसार का आधार स्तम्भ, भौतिक शक्ति, सामाजिक संप्रभुता एवं प्रतिष्ठा।</p>
<p style="margin-bottom:0.4rem;"><strong>त्रिकोण (1, 5, 9):</strong> लक्ष्मी स्थान — दैवीय अनुग्रह, धर्म, पूर्वपुण्य, मंत्र सिद्धि, विद्या एवं सात्विक विवेक।</p>
<p style="margin:0;"><strong>उपचय (3, 6, 10, 11), त्रिक (6, 8, 12) व मारक (2, 7):</strong> उपचय भाव समय के साथ सतत वृद्धि देते हैं; त्रिक भाव व्याधि, मृत्यु व मोक्ष का नियमन करते हैं; मारक भाव देह की आयु मर्यादा निर्धारित करते हैं।</p>"""
    ),
    make_chart_page(
        chapter="Ch 1: कालपुरुष कुण्डली व भाव व्यवस्था",
        title="उपचय भाव साधन चक्र — 3, 6, 10, 11 भावों की सतत विजय एवं वृद्धि",
        subtitle="समय के साथ निरंतर विस्तार, पुरुषार्थ, प्रतिस्पर्धात्मक विजय व सामाजिक उत्थान",
        svg_path="assets/icons/upachaya_diamond_chart.svg",
        alt_text="उपचय भाव साधन चक्र (Upachaya Growth Mandala)",
        caption="चित्र 1.3: उपचय भाव साधन चक्र (Upachaya Growth Mandala) — तृतीय (साहस), षष्ठ (प्रतिस्पर्धा), दशम (साम्राज्य) व एकादश (सर्व लाभ) भाव",
        card_title="⚔️ उपचय भावों में पापी ग्रहों का राजयोग (Upachaya Growth Mandala)",
        badge_label="सतत विजय सूत्र",
        card_body="""<p style="margin-bottom:0.4rem;"><strong>क्रूर ग्रहों की विजय शक्ति:</strong> उपचय भावों (3, 6, 10, 11) में नैसर्गिक क्रूर/पापी ग्रह (सूर्य, मंगल, शनि, राहु) स्थित होकर जातक को असीम इच्छाशक्ति, शत्रुहंता योग और कठिन परिस्थितियों में अभूतपूर्व विजय दिलाते हैं।</p>
<p style="margin:0;"><strong>काल-प्रवाह में फल वृद्धि:</strong> जैसे-जैसे जातक की आयु और अनुभव बढ़ता है, उपचय भावों की ऊर्जा संचित होकर जीवन के उत्तरार्ध में उच्च प्रतिष्ठा, विपुल संपत्ति और दीर्घकालिक प्रभाव प्रदान करती है।</p>"""
    ),
    make_chart_page(
        chapter="Ch 1: कालपुरुष कुण्डली व भाव व्यवस्था",
        title="ग्रहीय दृष्टि महाचक्र — 7वीं सार्वभौमिक दृष्टि व विशेष दृष्टि सूत्र",
        subtitle="समस्त ग्रहों की 7वीं पूर्ण दृष्टि तथा मंगल, गुरु, शनि, राहु-केतु की विशेष दृष्टियां",
        svg_path="assets/icons/aspect_wheel.svg",
        alt_text="ग्रहीय दृष्टि महाचक्र (Planetary Aspect Wheel)",
        caption="चित्र 1.4: ग्रहीय दृष्टि महाचक्र (Planetary Aspect Mandala) — 360° भचक्र में परस्पर ग्रहीय दृष्टि संबंध एवं प्रभाव क्षेत्र",
        card_title="👁️ ग्रहीय दृष्टि प्रभाव एवं शास्त्रीय नियम (Planetary Aspects & Drishti Matrix)",
        badge_label="दृष्टि फलित",
        card_body="""<p style="margin-bottom:0.4rem;"><strong>सार्वभौमिक सप्तम दृष्टि:</strong> सूर्य, चन्द्र, बुध, शुक्र सहित समस्त ग्रह अपने स्थित भाव से 7वें सम्मुख भाव को पूर्ण (100%) दृष्टि से देखते हैं।</p>
<p style="margin:0;"><strong>विशेष दृष्टियां:</strong> मंगल 4थे व 8वें भाव को; गुरु, राहु व केतु 5वें व 9वें भाव को (त्रिकोण अमृत दृष्टि); तथा शनि 3रे व 10वें भाव को पूर्ण दृष्टि से देखते हैं। शुभ ग्रहों की दृष्टि रक्षा व वृद्धि करती है, जबकि पापी ग्रहों की दृष्टि अनुशासन, अलगाव या संघर्ष लाती है।</p>"""
    ),
    make_chart_page(
        chapter="Ch 1: कालपुरुष कुण्डली व भाव व्यवस्था",
        title="द्वादश भाव स्थिर कारकत्व कुण्डली चक्र — महर्षि पाराशर प्रतिपादित स्थिर कारक ग्रह",
        subtitle="कुण्डली के प्रत्येक भाव के सनातन अधिष्ठाता व नियंत्रक स्थिर ग्रह",
        svg_path="assets/icons/bhava_karaka_diamond_chart.svg",
        alt_text="द्वादश भाव स्थिर कारकत्व कुण्डली चक्र (12 Bhavas Sthira Karakatva Diamond Chart)",
        caption="चित्र 1.5: द्वादश भाव स्थिर कारकत्व कुण्डली चक्र — 12 भावों के स्थिर कारक ग्रह (सूर्य, चन्द्र, मंगल, बुध, गुरु, शुक्र, शनि)",
        card_title="☸ स्थिर कारक ग्रह एवं भाव फल सिद्धांत (Permanent Signifiers Matrix)",
        badge_label="पाराशर सिद्धांत",
        card_body="""<p style="margin-bottom:0.4rem;"><strong>भावों के स्थायी स्वामी:</strong> 1-सूर्य (आत्मा), 2-गुरु (धन/कुटुंब), 3-मंगल (साहस/अनुज), 4-चन्द्र (माता/सुख), 5-गुरु (पुत्र/विवेक), 6-मंगल/शनि (ऋण/रोग), 7-शुक्र (कलत्र), 8-शनि (आयु), 9-गुरु/सूर्य (धर्म/भाग्य), 10-सूर्य/बुध/गुरु/शनि (कर्म), 11-गुरु (लाभ), 12-शनि (मोक्ष)।</p>
<p style="margin:0;"><strong>कारको भाव नाशाय:</strong> जब कोई स्थिर कारक ग्रह अपने ही कारक भाव में अकेला स्थित हो, तो उस भाव के प्राकृतिक फल में संकुचन या परीक्षा उत्पन्न होती है (यथा गुरु पंचम में)।</p>"""
    )
]

# 3. Build Chapter 2 dedicated full-page diamond charts
ch2_chart_pancha = make_chart_page(
    chapter="Ch 2: नवग्रह कारकत्व व राजयोग",
    title="पंच महापुरुष एवं गजकेसरी राजयोग चक्र — हंस, मालव्य, रुचक, भद्र, शश व गजकेसरी",
    subtitle="केन्द्र भावों (1, 4, 7, 10) में उच्च व स्वराशि ग्रहों से निर्मित अखंड साम्राज्य योग",
    svg_path="assets/icons/raja_yogas_chart.svg",
    alt_text="पंच महापुरुष एवं गजकेसरी राजयोग चक्र (Pancha Mahapurusha & Gajakesari Diamond Chart)",
    caption="चित्र 2.1: पंच महापुरुष एवं गजकेसरी राजयोग चक्र — हंस (गुरु), मालव्य (शुक्र), रुचक (मंगल), भद्र (बुध), शश (शनि) एवं गजकेसरी (गुरु+चन्द्र)",
    card_title="👑 पंच महापुरुष एवं गजकेसरी राजयोग का शास्त्रीय रहस्य (Imperial Yogas)",
    badge_label="परम राजयोग",
    card_body="""<p style="margin-bottom:0.4rem;"><strong>पंच महापुरुष योग:</strong> रुचक (मंगल - मेष/वृश्चिक/मकर), भद्र (बुध - मिथुन/कन्या), हंस (गुरु - धनु/मीन/कर्क), मालव्य (शुक्र - वृषभ/तुला/मीन), शश (शनि - मकर/कुंभ/तुला) जब लग्न या चन्द्र से केन्द्र (1, 4, 7, 10) में हों।</p>
<p style="margin:0;"><strong>गजकेसरी योग:</strong> चन्द्रमा से केन्द्र में बृहस्पति स्थित होकर जातक को विद्वान, तेजस्वी, उच्चाधिकारी एवं सर्वत्र पूजित बनाता है।</p>"""
)

ch2_chart_kendra_trikona = make_chart_page(
    chapter="Ch 2: नवग्रह कारकत्व व राजयोग",
    title="लक्ष्मी-नारायण योग एवं केन्द्र-त्रिकोण चक्र — विष्णु-लक्ष्मी संगम राजयोग",
    subtitle="विष्णु स्थान (केन्द्र: 1, 4, 7, 10) एवं लक्ष्मी स्थान (त्रिकोण: 1, 5, 9) का पावन संगम",
    svg_path="assets/icons/kendra_trikona_diamond_chart.svg",
    alt_text="लक्ष्मी-नारायण योग एवं केन्द्र-त्रिकोण चक्र (Lakshmi-Narayana Yoga Diamond Chart)",
    caption="चित्र 2.2: लक्ष्मी-नारायण योग व केन्द्र-त्रिकोण चक्र — धर्म एवं कर्म अधिपतियों का युति, दृष्टि व राशि-परिवर्तन संबंध",
    card_title="⚜ केन्द्र-त्रिकोण स्वामियों का संबंध सिद्धांत (Lakshmi-Narayana Yoga)",
    badge_label="सर्वोत्तम राजयोग",
    card_body="""<p style="margin-bottom:0.4rem;"><strong>4 प्रकार के फलदायी संबंध:</strong> 1. युति (एक ही भाव में बैठना), 2. परस्पर दृष्टि (एक-दूसरे को देखना), 3. क्षेत्र परिवर्तन (एक-दूसरे की राशि में बैठना), 4. एकतरफा पूर्ण दृष्टि।</p>
<p style="margin:0;"><strong>जीवन में फल:</strong> केन्द्र कर्म व सत्ता है, त्रिकोण भाग्य व कृपा है। इन दोनों के मिलन से जातक को अनायास ही धन, प्रतिष्ठा, राज्य सम्मान और आध्यात्मिक तेज प्राप्त होता है।</p>"""
)

ch2_chart_viparita = make_chart_page(
    chapter="Ch 2: नवग्रह कारकत्व व राजयोग",
    title="विपरीत राजयोग महाचक्र — हर्ष, सरल व विमल योग (6, 8, 12 भाव)",
    subtitle="त्रिक भावों (6, 8, 12) के स्वामियों का त्रिक भावों में ही स्थित होकर अमंगल को परम सौभाग्य में रूपांतरित करना",
    svg_path="assets/icons/viparita_chart.svg",
    alt_text="विपरीत राजयोग महाचक्र (Viparita Raja Yoga Diamond Chart)",
    caption="चित्र 2.3: विपरीत राजयोग महाचक्र — हर्ष योग (षष्ठेश 6, 8, 12 में), सरल योग (अष्टमेश 6, 8, 12 में), विमल योग (द्वादशेश 6, 8, 12 में)",
    card_title="⚡ विपरीत राजयोग का गूढ़ रसायन (Viparita Raja Yoga Architecture)",
    badge_label="गुप्त राजयोग",
    card_body="""<p style="margin-bottom:0.4rem;"><strong>हर्ष योग:</strong> षष्ठेश 6, 8 या 12वें भाव में हो। शत्रु नाश, अजेय मनोबल, मुकदमों में जीत, रोग मुक्ति।</p>
<p style="margin-bottom:0.4rem;"><strong>सरल योग:</strong> अष्टमेश 6, 8 या 12वें भाव में हो। दीर्घायु, निर्भयता, अचानक अकूत धन व प्रतिष्ठा, संकटों का चमत्कारिक निवारण।</p>
<p style="margin:0;"><strong>विमल योग:</strong> द्वादशेश 6, 8 या 12वें भाव में हो। स्वतंत्र जीवन, मितव्ययिता, परोपकार, मोक्ष प्राप्ति एवं शत्रुओं द्वारा हानि का शून्य होना।</p>"""
)

# 4. Build Chapter 3 dedicated full-page diamond charts
ch3_chart_nakshatra = make_chart_page(
    chapter="Ch 3: राशि, नक्षत्र एवं ग्रह गति",
    title="सप्तविंशति नक्षत्र व 108 पद 360° महामण्डल चक्र",
    subtitle="संपूर्ण 360° भचक्र में 27 नक्षत्र (13°20' प्रत्येक) एवं 108 पद (3°20' प्रत्येक) का सूक्ष्म नवमांश विस्तार",
    svg_path="assets/icons/nakshatra_mandala_wheel.svg",
    alt_text="सप्तविंशति नक्षत्र व 108 पद 360° महामण्डल चक्र (Nakshatra Mandala Wheel)",
    caption="चित्र 3.1: सप्तविंशति नक्षत्र व 108 पद 360° महामण्डल चक्र — 27 नक्षत्र (3.7% प्रत्येक) एवं 108 पद (0.926% प्रत्येक) का संपूर्ण भचक्र",
    card_title="🌌 27 नक्षत्र एवं 108 पद चक्र संरचना (Cosmic 360° Mandala)",
    badge_label="भचक्र गणित",
    card_body="""<p style="margin-bottom:0.4rem;"><strong>नक्षत्र विस्तार:</strong> प्रत्येक नक्षत्र ठीक 13 अंश 20 कला (13°20') का होता है। 12 राशियां × 30° = 360° = 27 नक्षत्र × 13°20'।</p>
<p style="margin:0;"><strong>108 पद व नवमांश:</strong> प्रत्येक नक्षत्र में 4 पद (3°20' प्रत्येक) होते हैं। 27 × 4 = 108 पद। यह 108 संख्या नवमांश कुण्डली (D9) का मूल आधार है।</p>"""
)

ch3_chart_elements = make_chart_page(
    chapter="Ch 3: राशि, नक्षत्र एवं ग्रह गति",
    title="चतुर्विध महाभूत कुण्डली चक्र — अग्नि (1-5-9), पृथ्वी (2-6-10), वायु (3-7-11) व जल (4-8-12)",
    subtitle="12 राशियों एवं 12 भावों का 4 मूलभूत तत्वों में वैज्ञानिक विभाजन",
    svg_path="assets/icons/elements_diamond_chart.svg",
    alt_text="चतुर्विध महाभूत कुण्डली चक्र (The Four Elements Diamond Kundali)",
    caption="चित्र 3.2: चतुर्विध महाभूत कुण्डली चक्र — अग्नि (1, 5, 9), पृथ्वी (2, 6, 10), वायु (3, 7, 11) एवं जल (4, 8, 12) तत्वों का सम्पूर्ण भाव विश्लेषण",
    card_title="🔥 चतुर्विध महाभूत तत्व विश्लेषण (The Four Elemental Trikonas)",
    badge_label="तत्व विज्ञान",
    card_body="""<p style="margin-bottom:0.4rem;"><strong>अग्नि (1, 5, 9):</strong> जीवन शक्ति, आत्मसम्मान, नेतृत्व, पराक्रम व धर्म। मेष, सिंह, धनु राशियां।</p>
<p style="margin-bottom:0.4rem;"><strong>पृथ्वी (2, 6, 10):</strong> स्थिरता, अर्थ संचय, कर्म, सहनशीलता व यथार्थ। वृषभ, कन्या, मकर राशियां।</p>
<p style="margin-bottom:0.4rem;"><strong>वायु (3, 7, 11):</strong> बुद्धि, संवाद, सामाजिक संबंध, यात्राएं व लाभ। मिथुन, तुला, कुंभ राशियां।</p>
<p style="margin:0;"><strong>जल (4, 8, 12):</strong> भावनाएं, अंतःकरण, गुप्त विद्याएं, त्याग व मोक्ष। कर्क, वृश्चिक, मीन राशियां।</p>"""
)

ch3_chart_purushartha = make_chart_page(
    chapter="Ch 3: राशि, नक्षत्र एवं ग्रह गति",
    title="चतुर्विध पुरुषार्थ कुण्डली चक्र — धर्म (1-5-9), अर्थ (2-6-10), काम (3-7-11) व मोक्ष (4-8-12)",
    subtitle="मानव जीवन के चार परम लक्ष्य — धर्म, अर्थ, काम एवं मोक्ष त्रिकोण का संपूर्ण फलित दर्पण",
    svg_path="assets/icons/purushartha_diamond_chart.svg",
    alt_text="चतुर्विध पुरुषार्थ कुण्डली चक्र (Purushartha Trikona Diamond Kundali)",
    caption="चित्र 3.3: चतुर्विध पुरुषार्थ कुण्डली चक्र — धर्म (1, 5, 9), अर्थ (2, 6, 10), काम (3, 7, 11) एवं मोक्ष (4, 8, 12) त्रिकोण व्यवस्था",
    card_title="☸ मानव जीवन के चार परम पुरुषार्थ (The Four Pillars of Human Destiny)",
    badge_label="पुरुषार्थ त्रिकोण",
    card_body="""<p style="margin-bottom:0.4rem;"><strong>धर्म त्रिकोण (1, 5, 9):</strong> आत्मा, पूर्वपुण्य, सात्विक ज्ञान, सत्य आचरण एवं ईश्वरीय कृपा।</p>
<p style="margin-bottom:0.4rem;"><strong>अर्थ त्रिकोण (2, 6, 10):</strong> संचित धन, नियमित कर्म, सेवा, ऋणमुक्ति एवं सांसारिक साम्राज्य।</p>
<p style="margin-bottom:0.4rem;"><strong>काम त्रिकोण (3, 7, 11):</strong> पराक्रम, वैवाहिक संबंध, साझेदारी, समस्त अभिलाषा पूर्ति व प्रभाव।</p>
<p style="margin:0;"><strong>मोक्ष त्रिकोण (4, 8, 12):</strong> अंतर्मुखी शांति, कुण्डलिनी साधना, संकट निवारण, त्याग व कैवल्य।</p>"""
)

# 5. Build Chapter 5 dedicated full-page diamond chart
ch5_chart_medical = make_chart_page(
    chapter="Ch 5: मेडिकल व स्वास्थ्य ज्योतिष",
    title="कालपुरुष अंग-प्रत्यंग व आयुर्वेद कुण्डली चक्र — 12 भाव, शारीरिक अंग व त्रिदोष निदान",
    subtitle="12 भावों एवं 12 राशियों का मानव देह के अंगों, वात-पित्त-कफ त्रिदोषों एवं रोगों से सूक्ष्म समन्वय",
    svg_path="assets/icons/medical_astrology_chart.svg",
    alt_text="कालपुरुष अंग-प्रत्यंग व आयुर्वेद कुण्डली चक्र (Medical Astrology Diamond Chart)",
    caption="चित्र 5.1: कालपुरुष अंग-प्रत्यंग व आयुर्वेद कुण्डली चक्र — मस्तक (प्रथम भाव) से लेकर चरण (द्वादश भाव) तक का सम्पूर्ण रोग निदान दर्पण",
    card_title="🩺 कालपुरुष अंग-प्रत्यंग एवं त्रिदोष चिकित्सा सिद्धांत (Ayur-Jyotish Anatomy)",
    badge_label="आयुर्वेद ज्योतिष",
    card_body="""<p style="margin-bottom:0.4rem;"><strong>12 भावों में देह रचना:</strong> 1-सिर/मस्तिष्क, 2-मुख/दाहिनी आँख, 3-कण्ठ/हाथ, 4-हृदय/फेफड़े, 5-पेट/यकृत, 6-आंतें/गुर्दे, 7-कमर/गुप्तांग, 8-गुदा/मूत्रमार्ग, 9-जांघें, 10-घुटने, 11-पिंडलियां/बायां कान, 12-पैर के तलवे/बाईं आँख।</p>
<p style="margin:0;"><strong>त्रिदोष संतुलन:</strong> सूर्य/मंगल/केतु (पित्त दोष), चन्द्र/शुक्र (कफ दोष), शनि/राहु (वात दोष), बुध (त्रिदोष सम)। जब भाव और उसके कारक ग्रह पीड़ित होते हैं, तो उस शारीरिक अंग में रोग का प्रादुर्भाव होता है।</p>"""
)

# 6. Assemble the 100 pages in ordered sequence
all_new_pages = []

# Pages 1 to 5: Front matter
for item in front_matter:
    all_new_pages.append({
        "chapter": item["chapter"],
        "title": item["title"],
        "content": item["body"]
    })

# Page 6: Index placeholder (will generate dynamic content)
all_new_pages.append({
    "chapter": page_6_idx["chapter"],
    "title": page_6_idx["title"],
    "content": "" # Generated below
})

# Chapter 1: 5 dedicated full-page diamond charts
for p in ch1_pages:
    all_new_pages.append(p)

# Chapter 2: 13 Navagraha Karakatva section pages
for item in ch2_articles[0:13]: # Surya through Ketu
    all_new_pages.append({
        "chapter": item["chapter"],
        "title": item["title"],
        "content": item["body"]
    })

# Insert Pancha Mahapurusha dedicated chart
all_new_pages.append(ch2_chart_pancha)

# Section 14 table (Pancha Mahapurusha table)
all_new_pages.append({
    "chapter": ch2_articles[13]["chapter"],
    "title": ch2_articles[13]["title"],
    "content": ch2_articles[13]["body"]
})

# Insert Kendra-Trikona dedicated chart & Viparita dedicated chart
all_new_pages.append(ch2_chart_kendra_trikona)
all_new_pages.append(ch2_chart_viparita)

# Section 15 table (Viparita Raja Yoga table)
all_new_pages.append({
    "chapter": ch2_articles[14]["chapter"],
    "title": ch2_articles[14]["title"],
    "content": ch2_articles[14]["body"]
})

# Chapter 3: Section 1 & 2
all_new_pages.append({
    "chapter": ch3_articles[0]["chapter"],
    "title": ch3_articles[0]["title"],
    "content": ch3_articles[0]["body"]
})
all_new_pages.append({
    "chapter": ch3_articles[1]["chapter"],
    "title": ch3_articles[1]["title"],
    "content": ch3_articles[1]["body"]
})

# Insert Nakshatra Mandala Wheel dedicated chart
all_new_pages.append(ch3_chart_nakshatra)

# Sections 3 to 7 (Nakshatra tables)
for item in ch3_articles[2:7]:
    all_new_pages.append({
        "chapter": item["chapter"],
        "title": item["title"],
        "content": item["body"]
    })

# Insert 4 Elements dedicated chart & 4 Purusharthas dedicated chart
all_new_pages.append(ch3_chart_elements)
all_new_pages.append(ch3_chart_purushartha)

# Remaining Chapter 3 sections (Sections 8 to 17)
for item in ch3_articles[7:]:
    all_new_pages.append({
        "chapter": item["chapter"],
        "title": item["title"],
        "content": item["body"]
    })

# Chapter 4: all 11 sections
for item in ch4_articles:
    all_new_pages.append({
        "chapter": item["chapter"],
        "title": item["title"],
        "content": item["body"]
    })

# Chapter 5: Insert Medical Astrology Diamond Chart first, then all 27 sections
all_new_pages.append(ch5_chart_medical)
for item in ch5_articles:
    all_new_pages.append({
        "chapter": item["chapter"],
        "title": item["title"],
        "content": item["body"]
    })

# Chapter 6: all 11 sections
for item in ch6_articles:
    all_new_pages.append({
        "chapter": item["chapter"],
        "title": item["title"],
        "content": item["body"]
    })

# Back Cover
all_new_pages.append({
    "chapter": back_cover["chapter"],
    "title": back_cover["title"],
    "content": back_cover["body"]
})

TOTAL_PAGES = len(all_new_pages)
print(f"Total new assembled pages: {TOTAL_PAGES}")

# 7. Update Page 6 (Index / Table of Contents) with accurate page ranges
page_6_content = f"""
<div class="page-inner-content">
  <div class="chapter-header" style="margin-bottom:1.2rem;">
    <div class="chapter-number">Index & Navigation</div>
    <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-gold);">विषय-सूची — Table of Contents</h2>
  </div>

  <div class="index-grid-container">
    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(1, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">प्रारम्भ</span>
        <div class="index-card-info">
          <strong class="index-card-title">प्रस्तावना, लेखक परिचय एवं वैधानिक सूचना</strong>
          <span class="index-card-desc">Front Matter, Author Profile & Guidelines</span>
        </div>
      </div>
      <span class="index-page-range">Pages 1 - 5</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(7, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 1</span>
        <div class="index-card-info">
          <strong class="index-card-title">कालपुरुष कुण्डली, भाव व्यवस्था व ग्रहीय दृष्टियां (5 महाचक्र)</strong>
          <span class="index-card-desc">Kaalpurusha Kundli, 12 Bhavas, Upachaya & Aspects</span>
        </div>
      </div>
      <span class="index-page-range">Pages 7 - 11</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(12, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 2</span>
        <div class="index-card-info">
          <strong class="index-card-title">नवग्रह कारकत्व एवं 17 शास्त्रीय राजयोग (पंच महापुरुष व विपरीत)</strong>
          <span class="index-card-desc">Navagraha Karakatva, Pancha Mahapurusha & Viparita Raja Yogas</span>
        </div>
      </div>
      <span class="index-page-range">Pages 12 - 29</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(30, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 3</span>
        <div class="index-card-info">
          <strong class="index-card-title">राशि, नक्षत्र, पंचमहाभूत, पुरुषार्थ एवं विंशोत्तरी महादशा</strong>
          <span class="index-card-desc">Zodiac Signs, 27 Nakshatras, 4 Elements, Purusharthas & Dasha</span>
        </div>
      </div>
      <span class="index-page-range">Pages 30 - 49</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(50, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 4</span>
        <div class="index-card-info">
          <strong class="index-card-title">भाव एवं राशियों में ग्रहों का प्रभाव (दीप्तादि 9 अवस्थाएं)</strong>
          <span class="index-card-desc">12 Houses, Planetary States & Operational Rules</span>
        </div>
      </div>
      <span class="index-page-range">Pages 50 - 60</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(61, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 5</span>
        <div class="index-card-info">
          <strong class="index-card-title">मेडिकल एस्ट्रोलॉजी चक्र एवं कैंसर रोग विश्लेषण (27 संपूर्ण तालिकाएं)</strong>
          <span class="index-card-desc">Medical Astrology Diamond Chart, Anatomy & Organ Pathology</span>
        </div>
      </div>
      <span class="index-page-range">Pages 61 - 88</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(89, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 6</span>
        <div class="index-card-info">
          <strong class="index-card-title">नक्षत्रों का गहन पद एवं ग्रह विश्लेषण (अश्विनी, आश्लेषा, पुष्य)</strong>
          <span class="index-card-desc">Deep Pada Matrices, Degrees & Navamsha Reference</span>
        </div>
      </div>
      <span class="index-page-range">Pages 89 - 99</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage({TOTAL_PAGES}, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Colophon</span>
        <div class="index-card-info">
          <strong class="index-card-title">समापन पृष्ठ, मंगल श्लोक व आधिकारिक संपर्क</strong>
          <span class="index-card-desc">Benediction, Upanishad Shloka & Contacts</span>
        </div>
      </div>
      <span class="index-page-range">Page {TOTAL_PAGES}</span>
    </div>
  </div>

  <div style="margin-top:1.15rem; font-size:0.84rem; color:var(--text-muted); text-align:center;">
    💡 <em>संकेत: किसी भी अध्याय कार्ड पर क्लिक करके सीधे उस पृष्ठ पर जा सकते हैं, या शीर्ष टूलबार के <strong>📖 विषय-सूची</strong> बटन से संपूर्ण सूची देखें।</em>
  </div>
</div>
"""
all_new_pages[5]["content"] = page_6_content

# 8. Build TOC list HTML for the Modal Drawer
toc_items_html = []
current_chapter = None
for p_idx, p in enumerate(all_new_pages):
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
new_toc_html = "\n".join(toc_items_html)

# 9. Build all <article class="book-page-data"> elements
articles_html = []
for p_idx, p in enumerate(all_new_pages):
    page_num = p_idx + 1
    ch_escaped = html.escape(p['chapter'])
    title_escaped = html.escape(p['title'])
    articles_html.append(f"""
    <article class="book-page-data" id="page-data-{page_num}" data-page="{page_num}" data-chapter="{ch_escaped}" data-title="{title_escaped}" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page {page_num}: {title_escaped}">
      <meta itemprop="position" content="{page_num}">
      <meta itemprop="name" content="{title_escaped}">
      {p['content'].strip()}
    </article>
    """)
all_articles_block = "\n".join(articles_html)

# 10. Replace the book corpus store in orig_html
corpus_pattern = re.compile(r'<main id="book-pages-store" class="book-corpus-store"[^>]*>.*?</main>', re.DOTALL)
new_corpus_tag = f'<main id="book-pages-store" class="book-corpus-store" itemscope itemtype="https://schema.org/Book" aria-label="Tantra Gyan Vedic Astrology Compendium">\n{all_articles_block}\n  </main>'

updated_html = corpus_pattern.sub(new_corpus_tag, orig_html)

# 11. Replace TOC list in modal
toc_list_pattern = re.compile(r'<div class="toc-list">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
new_toc_list_block = f'<div class="toc-list">\n{new_toc_html}\n        </div>\n      </div>\n    </div>\n  </div>'
updated_html = toc_list_pattern.sub(new_toc_list_block, updated_html)

# 12. Update slider max and counter badge
updated_html = re.sub(r'id="page-slider"\s+class="page-slider"\s+min="1"\s+max="\d+"', f'id="page-slider" class="page-slider" min="1" max="{TOTAL_PAGES}"', updated_html)
updated_html = re.sub(r'id="page-counter-badge">[^<]+<', f'id="page-counter-badge">Cover • 1 / {TOTAL_PAGES}<', updated_html)

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(updated_html)

print(f"Successfully generated {INDEX_FILE} with {TOTAL_PAGES} pages and updated TOC!")
