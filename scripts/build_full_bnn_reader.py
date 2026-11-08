#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembles bnn-reader.html cleanly using exact slice boundaries.
"""

import os

READER_SRC = "/Users/apple/Movies/ap/TantraGyan/reader.html"
BNN_READER = "/Users/apple/Movies/ap/TantraGyan/bnn-reader.html"

with open(READER_SRC, "r", encoding="utf-8") as f:
    lines = f.readlines()

first_art_idx = next(i for i, l in enumerate(lines) if '<article class="book-page-data"' in l)
last_art_idx = next(i for i in range(len(lines)-1, -1, -1) if '</article>' in lines[i])

top_part = "".join(lines[:first_art_idx])
bot_part = "".join(lines[last_art_idx+1:])

# Modify metadata and title
top_part = top_part.replace(
    "<title>वैदिक ज्योतिष महाग्रंथ सरलीकृत | Complete Vedic Astrology Compendium Simplified</title>",
    "<title>भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र (3D फ्लिप बुक) • Bhrigu Nandi Nadi 3D Flip Book</title>"
)
top_part = top_part.replace(
    'title="वैदिक ज्योतिष महाग्रंथ मुखपृष्ठ"',
    'title="भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र"'
)
top_part = top_part.replace(
    'तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ',
    'भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र (BNN)'
)
top_part = top_part.replace('p > 88', 'p > 40')
top_part = top_part.replace("localStorage.getItem('tantra_book_page')", "localStorage.getItem('tantra_bnn_flip_page')")
top_part = top_part.replace("localStorage.setItem('tantra_book_page'", "localStorage.setItem('tantra_bnn_flip_page'")
top_part = top_part.replace('max="100"', 'max="40"')
top_part = top_part.replace('href="astrology-book-engine/dist/web/index.html"', 'href="bhrigu-nandi-nadi.html"')
top_part = top_part.replace('href="tantra-gyan-vedic-jyotish-mahagranth.pdf"', 'href="bhrigu-nandi-nadi-karma-samyojan.pdf"')
top_part = top_part.replace('download="Tantra-Gyan-Vedic-Jyotish-Maha-Granth.pdf"', 'download="Bhrigu-Nandi-Nadi-Karma-Samyojan-Sutra.pdf"')
top_part = top_part.replace("Page 1 of 100", "Page 1 of 40")

def page(num, chapter, title, body):
    return f'''    <article class="book-page-data" id="page-data-{num}" data-page="{num}" data-chapter="{chapter}" data-title="{title}" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page {num}: {title}">
      <meta itemprop="position" content="{num}">
      <meta itemprop="name" content="{title}">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">{chapter}</div>
          <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{title}</h3>
        </div>
        {body}
      </div>
    </article>
'''

pages = []

# Page 1: Cover
p1_content = '''<div class="cover-page-wrapper" style="text-align:center; padding:2rem 1rem;">
  <div style="font-size:1.1rem; color:#fde047; font-weight:700; margin-bottom:1rem;">॥ ॐ गं गणपतये नमः ॥</div>
  <div style="margin:1.5rem auto;"><img src="assets/yantra.svg" alt="Yantra" width="110" height="110"></div>
  <h2 style="font-size:1.9rem; color:#fde047; font-family:'Noto Serif Devanagari',serif; font-weight:900; margin:1rem 0 0.5rem 0;">भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र</h2>
  <div style="font-size:1.1rem; color:#a5b4fc; font-weight:600; margin-bottom:1.5rem;">Bhrigu Nandi Nadi: Karma-Samyojan Sutra</div>
  <p style="font-size:0.9rem; color:#e2e8f0; max-width:480px; margin:0 auto 1.5rem auto; line-height:1.6;">ग्रह-संयोग (Conjunctions), दिशा-आधारित दृष्टि, जीव-कर्म कारक संबंध, प्रगति-गोचर सूत्र एवं अचूक फलित भविष्यवाणियां।</p>
  <div style="border-top:1px solid #d97706; border-bottom:1px solid #d97706; padding:0.8rem 0; max-width:440px; margin:0 auto; color:#fef3c7; font-size:0.9rem;">
    <strong>प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</strong><br>
    <span style="font-size:0.8rem; color:#cbd5e1;">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) • 2026</span>
  </div>
</div>'''
pages.append(page(1, "मुखपृष्ठ • Cover", "भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र", p1_content))

# Page 2: Invocation
p2_content = '''<div style="text-align:center; padding:1.5rem;">
  <div style="font-size:1.8rem; margin-bottom:0.8rem;">☸ 🔱 📜</div>
  <div class="shloka-box" style="background:rgba(200,157,61,0.08); border:1px solid #d97706; border-radius:8px; padding:1.2rem; margin:1rem auto; max-width:540px;">
    <div style="font-family:'Noto Serif Devanagari',serif; font-size:1.05rem; font-weight:700; color:#b45309; line-height:1.8;">
      ॥ नमस्तस्मै मुनीन्द्राय भृगवे ज्ञानरूपिणे ।<br>
      येन नाडी-प्रदीपेन दृश्यते भुवनत्रयम् ॥<br>
      ॥ नन्दीश्वरं महाप्राज्ञं कर्म-संयोजन-प्रभुम् ।<br>
      नमामि ज्ञान-दातारं काल-चक्र-प्रवर्तकम् ॥
    </div>
  </div>
  <p style="font-size:0.92rem; color:var(--text-main); line-height:1.7; max-width:520px; margin:1rem auto;">
    यह ग्रंथ पंडित आर. जी. राव (Pandit R.G. Rao) द्वारा 1950 के दशक में संहिताबद्ध भृगु नंदी नाड़ी (BNN) पद्धति के समस्त मूल सूत्रों, 12 डायमंड चार्ट्स, 16 बृहत् सारणियों और अचूक फलित भविष्यवाणियों का एक संपूर्ण प्रामाणिक संदर्भ-ग्रंथ है।
  </p>
</div>'''
pages.append(page(2, "मंगलाचरण • Invocation", "महर्षि भृगु एवं नंदीश्वर पाद नमन", p2_content))

# Page 3: About Author
p3_content = '''<div class="rule-card">
  <div class="rule-title"><span>✍️</span> प्रणेता परिचय (About Astrologer Ashutosh Kumar Choubey)</div>
  <div class="rule-body" style="font-size:0.9rem; line-height:1.7;">
    <strong>ज्योतिषाचार्य आशुतोष कुमार चौबे</strong> तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) के संस्थापक एवं मुख्य अन्वेषक हैं। वे प्राचीन वैदिक फलित ज्योतिष, भृगु नंदी नाड़ी (BNN), तांत्रिक दर्शन एवं आयुर्वेद के गूढ़ सूत्रों को आधुनिक तार्किक एवं वैज्ञानिक दृष्टिकोण के साथ प्रस्तुत करने के लिए समर्पित हैं।
    <br><br>
    <strong>आधिकारिक मंच:</strong>
    <br>• वेबसाइट: <a href="https://t.worldgyan.com" target="_blank">t.worldgyan.com</a>
    <br>• यूट्यूब: <a href="https://www.youtube.com/@TantraGyan108" target="_blank">@TantraGyan108</a>
    <br>• ईमेल: tantraresearchcenter@gmail.com
  </div>
</div>'''
pages.append(page(3, "लेखक परिचय • About Author", "ज्योतिषाचार्य आशुतोष कुमार चौबे", p3_content))

# Page 4: Preface
p4_content = '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> ग्रंथ का उद्देश्य एवं अध्ययन विधि</div>
  <div class="rule-body" style="font-size:0.9rem; line-height:1.7;">
    पारंपरिक पाराशरी ज्योतिष में विंशोत्तरी दशा, लग्न एवं भावपतियों की जटिलता के कारण अनेक बार जन्म समय के कुछ मिनटों के अंतर से फलित में भ्रम उत्पन्न होता है।
    <br><br>
    भृगु नंदी नाड़ी (BNN) में:
    <br>१. <strong>लग्न गौण है</strong> — पुरुष हेतु गुरु और स्त्री हेतु शुक्र जीव लग्न है।
    <br>२. <strong>विंशोत्तरी दशा की आवश्यकता नहीं</strong> — शनि के ३०-वर्षीय पर्याय और गुरु की वार्षिक प्रगति से अचूक काल-निर्धारण होता है।
    <br>३. <strong>ग्रह-संयोग एवं दिशा त्रिकोण (१-५-९)</strong> से बिना किसी सॉफ्टवेयर के तत्काल अचूक फलित संभव है।
  </div>
</div>'''
pages.append(page(4, "ग्रंथ परिचय • Preface", "बी.एन.एन. का वैज्ञानिक आधार", p4_content))

# Page 5: TOC
p5_content = '''<div style="font-size:0.88rem; line-height:1.8;">
  <div style="font-weight:800; color:var(--accent-gold); margin-bottom:0.5rem;">अनुक्रमणिका (Table of Contents):</div>
  • <strong>अध्याय १:</strong> मूल सिद्धांत एवं व्याकरण (पृष्ठ 6–9)<br>
  • <strong>अध्याय २:</strong> दिशा-आधारित दृष्टि एवं संबंध (पृष्ठ 10–14)<br>
  • <strong>अध्याय ३:</strong> नवग्रह व १२ राशि कारकत्व (पृष्ठ 15–20)<br>
  • <strong>अध्याय ४:</strong> जीव लग्न (गुरु) द्वादश भाव फलित (पृष्ठ 21–24)<br>
  • <strong>अध्याय ५:</strong> ३६ द्वैत ग्रह-संयोग सूत्र (पृष्ठ 25–30)<br>
  • <strong>अध्याय ६:</strong> त्रि-ग्रही व बहु-ग्रहीय महायोग (पृष्ठ 31–33)<br>
  • <strong>अध्याय ७:</strong> प्रगति, गोचर व भृगु बिंदु (पृष्ठ 34–37)<br>
  • <strong>अध्याय ८:</strong> ७-चरणीय कुंडली विश्लेषण (पृष्ठ 38–40)
</div>'''
pages.append(page(5, "अनुक्रमणिका • Contents", "ग्रंथ संरचना व अध्याय अनुक्रमणिका", p5_content))

# Page 6: Chapter 1 Principles
p6_content = '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> भृगु नंदी नाड़ी के ६ मूलभूत नियम</div>
  <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
    <strong>१. लग्न की गौणता:</strong> पुरुष हेतु गुरु और स्त्री हेतु शुक्र जीव लग्न है।<br>
    <strong>२. दशा-मुक्त फलित:</strong> गुरु व शनि की प्रगति से समय निर्धारण।<br>
    <strong>३. ग्रह-संभाषण:</strong> १-५-९ त्रिकोण, १-७ समसप्तक, २-१२ संबंध।<br>
    <strong>४. अंश-क्रम नियम:</strong> निम्न अंश वाला ग्रह आगे, उच्च अंश वाला पीछे।<br>
    <strong>५. वक्री ग्रह का द्वैत नियम:</strong> वक्री ग्रह का पिछली राशि में ५०% अस्तित्व।<br>
    <strong>६. राशि परिवर्तन:</strong> स्वराशि में लौटकर दोनों भावों का फल देना।
  </div>
</div>'''
pages.append(page(6, "अध्याय १ • Chapter 1", "भृगु नंदी नाड़ी के मूल सिद्धांत", p6_content))

# Page 7: Diagram 1.1
p7_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_philosophy_hierarchy_chart.svg" alt="आरेख 1.1" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख १.१: भृगु नंदी नाड़ी का ५-स्तरीय फलित निर्णय पदानुक्रम</div>
</div>'''
pages.append(page(7, "अध्याय १ • आरेख १.१", "५-स्तरीय फलित निर्णय पदानुक्रम", p7_content))

# Page 8: Table 1.1
p8_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका १.१: बी.एन.एन. बनाम पराशरी तुलना</div>
  <table class="bnn-table">
    <tr><th>आधार</th><th>भृगु नंदी नाड़ी (BNN)</th><th>पाराशरी ज्योतिष</th></tr>
    <tr><td><strong>लग्न</strong></td><td>गुरु (पुरुष) / शुक्र (स्त्री)</td><td>जन्म लग्न मुख्य</td></tr>
    <tr><td><strong>दशा</strong></td><td>गुरु/शनि प्रगति व गोचर</td><td>१२०-वर्षीय विंशोत्तरी</td></tr>
    <tr><td><strong>दृष्टि</strong></td><td>दिशा त्रिकोण १-५-९ (७५%)</td><td>विशेष दृष्टियां (३,७,१०)</td></tr>
    <tr><td><strong>समय संवेदनशीलता</strong></td><td>कम (घंटों के अंतर पर भी स्थिर)</td><td>अत्यधिक संवेदनशील</td></tr>
  </table>
</div>'''
pages.append(page(8, "अध्याय १ • तालिका १.१", "पद्धतियों का तुलनात्मक विश्लेषण", p8_content))

# Page 9: Table 1.2
p9_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका १.२: बी.एन.एन. फलित के ५-स्तरीय पदानुक्रम</div>
  <table class="bnn-table">
    <tr><th>स्तर</th><th>तत्व</th><th>महत्व</th></tr>
    <tr><td><strong>१</strong></td><td>कारक चयन (गुरु/शुक्र/शनि)</td><td>आधार स्तंभ</td></tr>
    <tr><td><strong>२</strong></td><td>१-५-९ दिशा त्रिकोण युति</td><td>७५%–१००% प्रभाव</td></tr>
    <tr><td><strong>३</strong></td><td>१-७ सम्मुख व २/१२ पार्श्व</td><td>५०% व १५% प्रभाव</td></tr>
    <tr><td><strong>४</strong></td><td>ग्रह अंश-क्रम व वक्री विनिमय</td><td>ऊर्जा प्रवाह की दिशा</td></tr>
    <tr><td><strong>५</strong></td><td>गोचर, पर्याय व भृगु बिंदु</td><td>अचूक घटना सक्रियण</td></tr>
  </table>
</div>'''
pages.append(page(9, "अध्याय १ • तालिका १.२", "फलित निर्णय पदानुक्रम सारणी", p9_content))

# Page 10: Chapter 2 Directional Rules
p10_content = '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> चारों दिशाएं एवं १-५-९ त्रिकोण संबंध</div>
  <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
    बी.एन.एन. में समान दिशा में स्थित ग्रह एक ही कक्ष में बैठे माने जाते हैं:
    <br>• <strong>पूर्व (अग्नि):</strong> मेष (१), सिंह (५), धनु (९) — १००% युति
    <br>• <strong>दक्षिण (पृथ्वी):</strong> वृषभ (२), कन्या (६), मकर (१०) — १००% युति
    <br>• <strong>पश्चिम (वायु):</strong> मिथुन (३), तुला (७), कुम्भ (११) — १००% युति
    <br>• <strong>उत्तर (जल):</strong> कर्क (४), वृश्चिक (८), मीन (१२) — १००% युति
    <br>• <strong>१-७ सम्मुख दृष्टि:</strong> ५०% प्रत्यक्ष प्रभाव।
    <br>• <strong>+१ अग्रिम व -१ पृष्ठ:</strong> १५% भावी व संचित प्रभाव।
  </div>
</div>'''
pages.append(page(10, "अध्याय २ • Chapter 2", "दिशा-आधारित दृष्टि एवं संबंध", p10_content))

# Page 11: Diagram 2.1
p11_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_jeeva_flow_diamond_chart.svg" alt="आरेख 2.1" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख २.१: उत्तर भारतीय डायमंड चार्ट में जीव-लग्न भाव-प्रवाह</div>
</div>'''
pages.append(page(11, "अध्याय २ • आरेख २.१", "जीव लग्न भाव-प्रवाह चक्र", p11_content))

# Page 12: Diagram 2.2
p12_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_directional_diamond_chart.svg" alt="आरेख 2.2" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख २.२: भृगु नंदी नाड़ी का दिशा-आधारित डायमंड चार्ट</div>
</div>'''
pages.append(page(12, "अध्याय २ • आरेख २.२", "दिशा-आधारित डायमंड चक्र", p12_content))

# Page 13: Diagram 2.3
p13_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_kartari_flank_diamond_chart.svg" alt="आरेख 2.3" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख २.३: अग्रिम, पृष्ठ एवं कर्तरी वेध डायमंड चक्र</div>
</div>'''
pages.append(page(13, "अध्याय २ • आरेख २.३", "कर्तरी वेध एवं पार्श्व प्रभाव", p13_content))

# Page 14: Table 2.1
p14_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका २.१: दिशा एवं त्रिकोण विभाजन</div>
  <table class="bnn-table">
    <tr><th>दिशा</th><th>तत्व</th><th>राशियां</th><th>संबद्ध ग्रह</th></tr>
    <tr><td><strong>पूर्व</strong></td><td>अग्नि</td><td>मेष (1), सिंह (5), धनु (9)</td><td>सूर्य, मंगल, गुरु</td></tr>
    <tr><td><strong>दक्षिण</strong></td><td>पृथ्वी</td><td>वृषभ (2), कन्या (6), मकर (10)</td><td>शुक्र, बुध, शनि</td></tr>
    <tr><td><strong>पश्चिम</strong></td><td>वायु</td><td>मिथुन (3), तुला (7), कुंभ (11)</td><td>बुध, शुक्र, शनि</td></tr>
    <tr><td><strong>उत्तर</strong></td><td>जल</td><td>कर्क (4), वृश्चिक (8), मीन (12)</td><td>चंद्र, मंगल, गुरु</td></tr>
  </table>
</div>'''
pages.append(page(14, "अध्याय २ • तालिका २.१", "दिशा त्रिकोण मास्टर सारणी", p14_content))

# Page 15: Chapter 3 Intro
p15_content = '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> नवग्रहों के नाड़ी कारकत्व का दर्शन</div>
  <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
    बी.एन.एन. में प्रत्येक ग्रह मानव जीवन के विशिष्ट संबंध, देह-अंग एवं भाग्य-पक्ष का स्थिर प्रतिनिधि है:
    <br>• <strong>गुरु:</strong> पुरुष जीव स्वयं • <strong>शुक्र:</strong> स्त्री जीव व धन
    <br>• <strong>शनि:</strong> कर्म व आजीविका • <strong>सूर्य:</strong> पिता व राजसत्ता
    <br>• <strong>चन्द्र:</strong> मन, माता व विदेश प्रवास • <strong>मंगल:</strong> भ्राता, पति व रक्त
    <br>• <strong>बुध:</strong> बुद्धि, व्यापार व मित्र • <strong>राहु:</strong> माया, विस्तार व भ्रम
    <br>• <strong>केतु:</strong> मोक्ष, विरक्ति व अध्यात्म
  </div>
</div>'''
pages.append(page(15, "अध्याय ३ • Chapter 3", "नवग्रह नाड़ी कारकत्व परिचय", p15_content))

# Page 16: Diagram 3.1
p16_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_karaka_relationship_wheel.svg" alt="आरेख 3.1" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख ३.१: नवग्रह नाड़ी कारकत्व एवं त्रि-स्तरीय मैत्री महाचक्र</div>
</div>'''
pages.append(page(16, "अध्याय ३ • आरेख ३.१", "नवग्रह कारकत्व व मैत्री चक्र", p16_content))

# Page 17: Table 3.1
p17_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ३.१: नवग्रह नाड़ी कारकत्व</div>
  <table class="bnn-table">
    <tr><th>ग्रह</th><th>जीव संबंध</th><th>कार्यक्षेत्र / फलित भूमिका</th></tr>
    <tr><td><strong>सूर्य</strong></td><td>पिता, आत्मा</td><td>शासक, औषधि, नेत्र, यश</td></tr>
    <tr><td><strong>चन्द्र</strong></td><td>माता, मन</td><td>द्रव्य, गति, विदेश, कला</td></tr>
    <tr><td><strong>मंगल</strong></td><td>भ्राता, पति</td><td>रक्त, साहस, भूमि, तकनीकी</td></tr>
    <tr><td><strong>बुध</strong></td><td>बुद्धि, मातुल</td><td>वाणिज्य, वाणी, लेखन, मित्र</td></tr>
    <tr><td><strong>गुरु</strong></td><td>पुरुष जीव स्वयं</td><td>ज्ञान, संतति, देवकृपा, विस्तार</td></tr>
  </table>
</div>'''
pages.append(page(17, "अध्याय ३ • तालिका ३.१", "नवग्रह नाड़ी कारकत्व सारणी (भाग 1)", p17_content))

# Page 18: Table 3.2
p18_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ३.२: बी.एन.एन. ग्रह मैत्री चक्र</div>
  <table class="bnn-table">
    <tr><th>ग्रह</th><th>मित्र ग्रह</th><th>सम ग्रह</th><th>शत्रु ग्रह</th></tr>
    <tr><td><strong>गुरु</strong></td><td>सूर्य, चन्द्र, मंगल</td><td>शनि, केतु</td><td>बुध, शुक्र, राहु</td></tr>
    <tr><td><strong>शनि</strong></td><td>बुध, शुक्र, राहु</td><td>गुरु</td><td>सूर्य, चन्द्र, मंगल, केतु</td></tr>
    <tr><td><strong>शुक्र</strong></td><td>बुध, शनि, राहु, केतु</td><td>मंगल</td><td>सूर्य, चन्द्र, गुरु</td></tr>
    <tr><td><strong>बुध</strong></td><td>सूर्य, शुक्र, राहु</td><td>मंगल, गुरु, शनि</td><td>चन्द्र</td></tr>
  </table>
</div>'''
pages.append(page(18, "अध्याय ३ • तालिका ३.२", "ग्रह मैत्री व संबंध सारणी", p18_content))

# Page 19: Diagram 3.2
p19_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_elemental_directional_diamond_chart.svg" alt="आरेख 3.2" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख ३.२: चतुर्विध महाभूत एवं दिशा-संयोजन डायमंड चक्र</div>
</div>'''
pages.append(page(19, "अध्याय ३ • आरेख ३.२", "चतुर्विध महाभूत दिशा चक्र", p19_content))

# Page 20: Table 3.3
p20_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ३.३: द्वादश राशियों का सूक्ष्म नाड़ी स्वरूप</div>
  <table class="bnn-table">
    <tr><th>राशि</th><th>तत्व</th><th>दिशा</th><th>नाड़ी कारकत्व</th></tr>
    <tr><td><strong>मेष (1)</strong></td><td>अग्नि</td><td>पूर्व</td><td>आरंभ, साहस, मस्तक</td></tr>
    <tr><td><strong>वृषभ (2)</strong></td><td>पृथ्वी</td><td>दक्षिण</td><td>धन, कुटुंब, वाहन, रूप</td></tr>
    <tr><td><strong>मिथुन (3)</strong></td><td>वायु</td><td>पश्चिम</td><td>संवाद, व्यापार, यात्रा</td></tr>
    <tr><td><strong>कर्क (4)</strong></td><td>जल</td><td>उत्तर</td><td>मन, गृह, जल, भावना</td></tr>
    <tr><td><strong>सिंह (5)</strong></td><td>अग्नि</td><td>पूर्व</td><td>राजसत्ता, पिता, मान</td></tr>
  </table>
</div>'''
pages.append(page(20, "अध्याय ३ • तालिका ३.३", "द्वादश राशि नाड़ी स्वरूप", p20_content))

# Page 21: Chapter 4 Intro
p21_content = '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> जीव लग्न (गुरु) से द्वादश भाव गणना</div>
  <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
    बी.एन.एन. में जन्म-कालीन गुरु को लग्न मानकर १२ भावों का विचार किया जाता है:
    <br>• १म भाव: जीव स्वयं, देह, चेतना
    <br>• २रा भाव: धन, कुटुंब, प्रारंभिक संसाधन (+१ कदम)
    <br>• १०वां भाव: कर्म, पदवी, आजीविका
    <br>• १२वां भाव: मोक्ष, विदेश वास, संचित ऋण (-१ कदम)
    <br>यह व्यवस्था किसी भी लग्न-कुंडली के अभाव में भी अचूक परिणाम देती है।
  </div>
</div>'''
pages.append(page(21, "अध्याय ४ • Chapter 4", "जीव लग्न द्वादश भाव व्यवस्था", p21_content))

# Page 22: Diagram 4.1
p22_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_jeeva_12bhavas_diamond_chart.svg" alt="आरेख 4.1" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख ४.१: जीव लग्न (गुरु) द्वादश भाव सम्पूर्ण फलित चक्र</div>
</div>'''
pages.append(page(22, "अध्याय ४ • आरेख ४.१", "जीव लग्न द्वादश भाव चक्र", p22_content))

# Page 23: Table 4.1 (1 to 6)
p23_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ४.१ (भाग 1): गुरु से १ से ६ भाव फल</div>
  <table class="bnn-table">
    <tr><th>भाव</th><th>नाम</th><th>नाड़ी फलित</th></tr>
    <tr><td><strong>१</strong></td><td>जीव स्वयं</td><td>आरोग्य, आत्म-चेतना, जीवन की दिशा</td></tr>
    <tr><td><strong>२</strong></td><td>धन/वाणी</td><td>वित्तीय संचय, कुटुंब, आगामी कर्म कदम</td></tr>
    <tr><td><strong>३</strong></td><td>पराक्रम</td><td>छोटे भाई, संचार, विपणन, लघु यात्राएं</td></tr>
    <tr><td><strong>४</strong></td><td>सुख/माता</td><td>गृह, वाहन, प्राथमिक विद्या, शांति</td></tr>
    <tr><td><strong>५</strong></td><td>पूर्वपुण्य</td><td>संतान, बुद्धि, मंत्र दीक्षा, शोध</td></tr>
    <tr><td><strong>६</strong></td><td>रोग/ऋण</td><td>दैनिक सेवा, संघर्ष, कोर्ट-कचहरी, प्रतियोगिता</td></tr>
  </table>
</div>'''
pages.append(page(23, "अध्याय ४ • तालिका ४.१ (क)", "गुरु से १ से ६ भाव फलित", p23_content))

# Page 24: Table 4.1 (7 to 12)
p24_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ४.१ (भाग 2): गुरु से ७ से १२ भाव फल</div>
  <table class="bnn-table">
    <tr><th>भाव</th><th>नाम</th><th>नाड़ी फलित</th></tr>
    <tr><td><strong>७</strong></td><td>जाया</td><td>जीवनसाथी, साझेदारी, प्रत्यक्ष सम्मुख कर्म</td></tr>
    <tr><td><strong>८</strong></td><td>आयु/गूढ़</td><td>आकस्मिक परिवर्तन, संकट, तंत्र विद्या, शोध</td></tr>
    <tr><td><strong>९</strong></td><td>भाग्य/धर्म</td><td>पिता, उच्च ज्ञान, तीर्थ, भाग्य विस्तार</td></tr>
    <tr><td><strong>१०</strong></td><td>कर्म/पदवी</td><td>आजीविका, पदोन्नति, सामाजिक प्रतिष्ठा</td></tr>
    <tr><td><strong>११</strong></td><td>लाभ/सिद्धि</td><td>इच्छापूर्ति, बड़े भाई, वित्तीय लाभ</td></tr>
    <tr><td><strong>१२</strong></td><td>मोक्ष/व्यय</td><td>विदेश वास, आध्यात्मिक मुक्ति, विगत ऋण</td></tr>
  </table>
</div>'''
pages.append(page(24, "अध्याय ४ • तालिका ४.१ (ख)", "गुरु से ७ से १२ भाव फलित", p24_content))

# Page 25: Chapter 5 Dual Conjunctions
p25_content = '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> ३६ द्वैत ग्रह-संयोग सूत्र</div>
  <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
    जब दो ग्रह एक ही राशि या १-५-९ त्रिकोण में मिलते हैं, तो वे एक संयुक्त रासायनिक यौगिक की भांति नया फल उत्पन्न करते हैं:
    <br>• <strong>गुरु + शनि:</strong> धर्म-कर्माधिपति / ब्रह्म योग
    <br>• <strong>बुध + शुक्र:</strong> कला / महालक्ष्मी योग
    <br>• <strong>शनि + शुक्र:</strong> विवाह उपरांत भाग्योदय
    <br>• <strong>गुरु + केतु:</strong> गणेश योग (आध्यात्मिक मुक्ति)
    <br>• <strong>शनि + राहु:</strong> श्रापित / विदेशी तकनीकी उद्योग
  </div>
</div>'''
pages.append(page(25, "अध्याय ५ • Chapter 5", "द्वैत ग्रह-संयोग का आधार", p25_content))

# Page 26: Diagram 5.1
p26_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_major_conjunctions_diamond_chart.svg" alt="आरेख 5.1" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख ५.१: बी.एन.एन. प्रमुख द्वि-ग्रहीय राजयोग एवं कर्म-संयोग चक्र</div>
</div>'''
pages.append(page(26, "अध्याय ५ • आरेख ५.१", "प्रमुख द्वैत राजयोग चक्र", p26_content))

# Page 27: Table 5.1 (Sun Conjunctions)
p27_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ५.१: सूर्य के प्रमुख संयोग</div>
  <table class="bnn-table">
    <tr><th>संयोग</th><th>नाड़ी नाम</th><th>फलित प्रभाव</th></tr>
    <tr><td><strong>सूर्य + गुरु</strong></td><td>राज-ब्रह्म योग</td><td>सर्वोच्च राजकीय सम्मान, पिता से लाभ, सात्विक तेज</td></tr>
    <tr><td><strong>सूर्य + बुध</strong></td><td>बुधादित्य</td><td>तीव्र बुद्धि, वाणिज्य, सरकारी सेवा, वाकपटुता</td></tr>
    <tr><td><strong>सूर्य + शनि</strong></td><td>पिता-पुत्र मतभेद</td><td>संघर्ष उपरांत सफलता, स्वावलंबी, अनुशासन</td></tr>
    <tr><td><strong>सूर्य + राहु</strong></td><td>ग्रहण योग</td><td>पिता कष्ट, भ्रम, किन्तु विदेशी संस्था में उच्च पद</td></tr>
    <tr><td><strong>सूर्य + केतु</strong></td><td>आत्म-मुक्ति</td><td>आध्यात्मिक नेतृत्व, चिकित्सा, पैतृक विरक्ति</td></tr>
  </table>
</div>'''
pages.append(page(27, "अध्याय ५ • तालिका ५.१", "सूर्य ग्रह-संयोग सूत्र", p27_content))

# Page 28: Table 5.2 (Moon Conjunctions)
p28_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ५.२: चन्द्रमा के प्रमुख संयोग</div>
  <table class="bnn-table">
    <tr><th>संयोग</th><th>नाड़ी नाम</th><th>फलित प्रभाव</th></tr>
    <tr><td><strong>चन्द्र + गुरु</strong></td><td>गजकेसरी नाड़ी</td><td>अखंड कीर्ति, परोपकार, जनसमर्थन, यात्रा लाभ</td></tr>
    <tr><td><strong>चन्द्र + शनि</strong></td><td>प्रवास योग</td><td>माता कष्ट, गृह-त्याग, सतत स्थान परिवर्तन, वैराग्य</td></tr>
    <tr><td><strong>चन्द्र + शुक्र</strong></td><td>सौन्दर्य-व्यय</td><td>कला, विलासिता, तरल पदार्थों का व्यापार, आकर्षण</td></tr>
    <tr><td><strong>चन्द्र + केतु</strong></td><td>मातृ-ऋण योग</td><td>तीव्र अंतर्ज्ञान, वैराग्य, मानसिक उतार-चढ़ाव</td></tr>
  </table>
</div>'''
pages.append(page(28, "अध्याय ५ • तालिका ५.२", "चन्द्र ग्रह-संयोग सूत्र", p28_content))

# Page 29: Table 5.3 (Mars & Mercury)
p29_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ५.३: मंगल एवं बुध के प्रमुख संयोग</div>
  <table class="bnn-table">
    <tr><th>संयोग</th><th>नाड़ी नाम</th><th>फलित प्रभाव</th></tr>
    <tr><td><strong>मंगल + गुरु</strong></td><td>तेजस्वी योग</td><td>इंजीनियरिंग, भूमि लाभ, सैन्य/पुलिस नेतृत्व</td></tr>
    <tr><td><strong>मंगल + बुध</strong></td><td>भूमि विवाद</td><td>तीव्र तार्किक बुद्धि, किंतु भ्रातृ मतभेद से सावधानी</td></tr>
    <tr><td><strong>बुध + शुक्र</strong></td><td>कला योग</td><td>अपार व्यापारिक लाभ, विपणन, सौन्दर्य प्रसाधन</td></tr>
    <tr><td><strong>बुध + राहु</strong></td><td>सॉफ्टवेयर योग</td><td>कोडिंग, कृत्रिम बुद्धिमत्ता (AI), विदेशी वाणिज्य</td></tr>
  </table>
</div>'''
pages.append(page(29, "अध्याय ५ • तालिका ५.३", "मंगल व बुध संयोग सूत्र", p29_content))

# Page 30: Table 5.4 (Jupiter, Venus, Saturn)
p30_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ५.४: गुरु, शुक्र एवं शनि संयोग</div>
  <table class="bnn-table">
    <tr><th>संयोग</th><th>नाड़ी नाम</th><th>फलित प्रभाव</th></tr>
    <tr><td><strong>गुरु + शनि</strong></td><td>धर्म-कर्माधिपति</td><td>सर्वोच्च संस्था प्रमुख, न्यायाधीश, आध्यात्मिक कर्म</td></tr>
    <tr><td><strong>शनि + शुक्र</strong></td><td>भाग्यलक्ष्मी</td><td>विवाह उपरांत प्रचंड भाग्योदय, अचल संपत्ति</td></tr>
    <tr><td><strong>गुरु + केतु</strong></td><td>गणेश योग</td><td>त्रिकालज्ञ, ज्योतिष-प्रवीण, मोक्ष मार्ग</td></tr>
    <tr><td><strong>शनि + राहु</strong></td><td>श्रापित/तकनीकी</td><td>वैश्विक प्रौद्योगिकी उद्योग, मशीनरी, विदेशी आय</td></tr>
  </table>
</div>'''
pages.append(page(30, "अध्याय ५ • तालिका ५.४", "गुरु, शुक्र व शनि संयोग सूत्र", p30_content))

# Page 31: Chapter 6 Triplets Intro
p31_content = '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> त्रि-ग्रही एवं बहु-ग्रहीय महायोग</div>
  <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
    जब तीन या अधिक ग्रह एक ही त्रिकोण या परस्पर दृष्टि अक्ष में जुड़ते हैं, तो वे जातक को साधारण से असाधारण स्तर तक पहुंचाते हैं:
    <br>• <strong>सरस्वती राजयोग:</strong> गुरु + बुध + शुक्र (सर्वोच्च विद्वत्ता)
    <br>• <strong>कुबेर महायोग:</strong> शनि + बुध + शुक्र (व्यापारिक साम्राज्य)
    <br>• <strong>ऋषि महायोग:</strong> सूर्य + गुरु + केतु (ब्रह्मज्ञानी)
    <br>• <strong>चक्रवर्ती कर्मयोग:</strong> गुरु + शनि + मंगल (प्रशासनिक प्रमुख)
  </div>
</div>'''
pages.append(page(31, "अध्याय ६ • Chapter 6", "त्रि-ग्रहीय महायोग का विधान", p31_content))

# Page 32: Diagram 6.1
p32_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_triplet_rajyogas_diamond_chart.svg" alt="आरेख 6.1" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख ६.१: बी.एन.एन. त्रि-ग्रहीय एवं बहु-ग्रहीय महायोग डायमंड चक्र</div>
</div>'''
pages.append(page(32, "अध्याय ६ • आरेख ६.१", "त्रि-ग्रहीय महायोग चक्र", p32_content))

# Page 33: Table 6.1
p33_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ६.१: २० शीर्ष त्रि-ग्रहीय महायोग</div>
  <table class="bnn-table">
    <tr><th>संयोग</th><th>योग नाम</th><th>मुख्य फलित</th></tr>
    <tr><td>गुरु + बुध + शुक्र</td><td>सरस्वती राजयोग</td><td>ग्रंथकार, अंतरराष्ट्रीय ख्याति, वाक्सिद्धि</td></tr>
    <tr><td>शनि + बुध + शुक्र</td><td>कुबेर महायोग</td><td>उद्योगपति, विशाल व्यापार साम्राज्य, स्थायी संपदा</td></tr>
    <tr><td>सूर्य + गुरु + केतु</td><td>ऋषि महायोग</td><td>तपोबल, आध्यात्मिक संस्था प्रमुख, ब्रह्मज्ञान</td></tr>
    <tr><td>गुरु + शनि + मंगल</td><td>चक्रवर्ती कर्मयोग</td><td>चीफ सेक्रेटरी, सैन्य प्रमुख, सर्वोच्च निर्माणकर्ता</td></tr>
  </table>
</div>'''
pages.append(page(33, "अध्याय ६ • तालिका ६.१", "२० त्रि-ग्रहीय महायोग सारणी", p33_content))

# Page 34: Chapter 7 Progression Intro
p34_content = '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> प्रगति (Progression) एवं गोचर के अचूक सूत्र</div>
  <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
    घटना किस वर्ष घटेगी, इसका निर्धारण बी.एन.एन. की प्रगति प्रणाली से होता है:
    <br>• <strong>शनि ३०-वर्षीय पर्याय:</strong> १ राशि = २.५ वर्ष (३० माह)। चार पर्याय: ०-३० (नींव), ३०-६० (कर्म उत्थान), ६०-९० (ज्ञान), ९०+ (मोक्ष)।
    <br>• <strong>गुरु वार्षिक प्रगति:</strong> जन्म गुरु से प्रति वर्ष १ राशि आगे बढ़ें (१२ वर्ष चक्र)।
    <br>• <strong>भृगु बिंदु (BB):</strong> राहु व चन्द्र का गणितीय मध्य बिंदु।
  </div>
</div>'''
pages.append(page(34, "अध्याय ७ • Chapter 7", "प्रगति एवं गोचर काल-गणना", p34_content))

# Page 35: Diagram 7.1
p35_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_progression_paryaya_chart.svg" alt="आरेख 7.1" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख ७.१: शनि ३०-वर्षीय पर्याय एवं गुरु प्रगति काल-चक्र</div>
</div>'''
pages.append(page(35, "अध्याय ७ • आरेख ७.१", "शनि पर्याय व गुरु प्रगति चक्र", p35_content))

# Page 36: Diagram 7.2
p36_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_bhrigu_bindu_diagram.svg" alt="आरेख 7.2" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख ७.२: भृगु बिंदु (BB) प्रारब्ध संवाहक बिंदु ज्यामितीय चक्र</div>
</div>'''
pages.append(page(36, "अध्याय ७ • आरेख ७.२", "भृगु बिंदु (BB) ज्यामितीय चक्र", p36_content))

# Page 37: Table 7.1 & 7.2
p37_content = '''<div style="font-size:0.82rem;">
  <div style="font-weight:700; color:var(--accent-gold); margin-bottom:0.4rem;">तालिका ७.१: गणितीय प्रगति सूत्र</div>
  <table class="bnn-table">
    <tr><th>सूत्र</th><th>समीकरण</th><th>उपयोग</th></tr>
    <tr><td><strong>गुरु वृहद प्रगति</strong></td><td>वर्ष = अंश × 0.4</td><td>जन्म पूर्व बीते वर्ष</td></tr>
    <tr><td><strong>शनि पर्याय</strong></td><td>माह = अंश × 1</td><td>पर्याय में बीते माह</td></tr>
    <tr><td><strong>भृगु बिंदु (BB)</strong></td><td>(राहु + चन्द्र) / 2</td><td>घटना का ट्रिगर बिंदु</td></tr>
  </table>
  <div style="margin-top:0.6rem; color:var(--text-muted); font-size:0.8rem;">
    गोचर का गुरु/शनि जब BB को छूता है, तब विवाह, पदोन्नति अथवा संतान प्राप्ति की घटना घटित होती है।
  </div>
</div>'''
pages.append(page(37, "अध्याय ७ • तालिका ७.१", "गणितीय समीकरण सारणी", p37_content))

# Page 38: Chapter 8 Protocol Intro
p38_content = '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> कुण्डली विश्लेषण की ७-चरणीय व्यावहारिक विधि</div>
  <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
    किसी भी जातक की कुण्डली देखते समय निम्न ७ चरणों का क्रमबद्ध पालन करें:
    <br>१. जीव (गुरु/शुक्र) एवं कर्म कारक (शनि) को चिन्हित करें।
    <br>२. १-५-९ समान दिशा त्रिकोण युतियों का मिलान करें।
    <br>३. १-७ सम्मुख दृष्टि संबंध का प्रभाव देखें।
    <br>४. +१ अग्रिम एवं -१ पृष्ठ भाव प्रभावों की जांच करें।
    <br>५. अंश-क्रम एवं वक्री ग्रह का द्वैत नियम लागू करें।
    <br>६. शुभ/पाप कर्तरी वेध का निर्धारण करें।
    <br>७. गोचर पर्याय एवं भृगु बिंदु द्वारा घटना का वर्ष व माह निश्चित करें।
  </div>
</div>'''
pages.append(page(38, "अध्याय ८ • Chapter 8", "७-चरणीय विश्लेषण प्रोटोकॉल", p38_content))

# Page 39: Diagram 8.1
p39_content = '''<div style="text-align:center;">
  <img src="assets/icons/bnn_protocol_flowchart.svg" alt="आरेख 8.1" style="width:100%; max-width:540px; border-radius:8px;" loading="lazy">
  <div style="font-size:0.85rem; font-weight:700; color:var(--accent-gold); margin-top:0.4rem;">आरेख ८.१: बी.एन.एन. ७-चरणीय फलित निर्णय प्रवाह आरेख</div>
</div>'''
pages.append(page(39, "अध्याय ८ • आरेख ८.१", "७-चरणीय निर्णय प्रवाह आरेख", p39_content))

# Page 40: Colophon & Closing
p40_content = '''<div style="text-align:center; padding:2rem 1rem;">
  <div style="font-size:1.8rem; margin-bottom:0.8rem;">☸ ॥ ॐ शान्तिः शान्तिः शान्तिः ॥ ☸</div>
  <h3 style="font-size:1.4rem; color:var(--accent-gold); font-family:'Noto Serif Devanagari',serif; font-weight:800; margin-bottom:1rem;">ग्रंथ समापन एवं मंगल आशीर्वाद</h3>
  <p style="font-size:0.92rem; color:var(--text-main); line-height:1.7; max-width:500px; margin:0 auto 1.5rem auto;">
    यह ग्रंथ समस्त सुधी शोधार्थियों, ज्योतिष प्रेमियों एवं साधकों हेतु पूर्णतः निःशुल्क, खुला एवं सत्यापनीय ज्ञानकोश के रूप में तंत्र ज्ञान शोध संस्थान द्वारा समर्पित है।
  </p>
  <div style="border-top:1px solid #d97706; padding-top:1rem; max-width:440px; margin:0 auto; font-size:0.85rem; color:var(--text-muted);">
    <strong>प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</strong><br>
    तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)<br>
    वेबसाइट: <a href="https://t.worldgyan.com" target="_blank">t.worldgyan.com</a> • २०२६ सर्वाधिकार सुरक्षित
  </div>
</div>'''
pages.append(page(40, "उपसंहार • Colophon", "ग्रंथ समापन व शांति पाठ", p40_content))

# Assemble full HTML
full_html = top_part + "\n".join(pages) + "\n  </main>\n" + bot_part

with open(BNN_READER, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated clean bnn-reader.html ({len(full_html)} bytes, {len(pages)} pages)!")
