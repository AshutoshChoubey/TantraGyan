#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembles sadhana-reader.html cleanly from bnn-reader.html slice boundaries.
Interactive 3D Hardcover Flipbook for Tantra Sadhana Siddhi Mahagranth.
Curated & Created by Jyotishacharya Ashutosh Kumar Choubey, Tantra Gyan.
Strictly uses standard English numerals (0-9) throughout all text and tables.
"""

import os
import re

SRC_READER = "/Users/apple/Movies/ap/TantraGyan/bnn-reader.html"
DST_READER = "/Users/apple/Movies/ap/TantraGyan/sadhana-reader.html"

with open(SRC_READER, "r", encoding="utf-8") as f:
    html_data = f.read()

# Isolate top part before first <article class="book-page-data"
art_match = re.search(r'<article class="book-page-data"', html_data)
first_art_pos = art_match.start()
last_art_pos = html_data.rfind('</article>') + len('</article>')

top_part = html_data[:first_art_pos]
bot_part = html_data[last_art_pos:]

# Replace metadata in top_part
top_part = top_part.replace(
    "<title>भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र (3D फ्लिप बुक) • Bhrigu Nandi Nadi 3D Flip Book</title>",
    "<title>तंत्र साधना सिद्धि महाग्रंथ (3D फ्लिप बुक) • Tantra Sadhana Siddhi 3D Flip Book</title>"
)
top_part = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="तंत्र साधना सिद्धि महाग्रंथ: 41-दिवसीय प्रत्यक्ष प्रयोग एवं गुप्त विधि-विधान by ज्योतिषाचार्य Ashutosh Kumar Choubey. सवा लाख पंचाक्षरी जप, 21 सिद्ध कुंजिका पाठ, वेदी निर्माण एवं संपुट रहस्य।">',
    top_part
)
top_part = re.sub(
    r'<meta name="keywords" content="[^"]*">',
    '<meta name="keywords" content="Tantra Sadhana Siddhi, Siddha Kunjika Stotra, Panchakshari Sadhana, Om Namah Shivaya 125000, Samput Vidhan, Vivaha Sadhana, Batuk Bhairav, Durga Kavach, Ashutosh Kumar Choubey, Tantra Gyan">',
    top_part
)
top_part = top_part.replace('content="BNN 3D Flip Book"', 'content="Tantra Sadhana Siddhi 3D Flip Book"')
top_part = top_part.replace('href="https://t.worldgyan.com/bnn-reader.html"', 'href="https://t.worldgyan.com/sadhana-reader.html"')
top_part = top_part.replace('href="https://t.worldgyan.com/bhrigu-nandi-nadi.html"', 'href="https://t.worldgyan.com/tantra-sadhana-siddhi.html"')
top_part = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="तंत्र साधना सिद्धि महाग्रंथ | Tantra Sadhana Siddhi 3D Flip Book">', top_part)
top_part = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="41-दिवसीय प्रत्यक्ष प्रयोग, सवा लाख पंचाक्षरी जप, श्री सिद्ध कुंजिका स्तोत्र 21 पाठ, वेदी द्वैत दीप विज्ञान एवं संपुट विधान। लेखक: ज्योतिषाचार्य Ashutosh Kumar Choubey।">', top_part)

top_part = top_part.replace('tantra_bnn_flip_page', 'tantra_sadhana_flip_page')
top_part = top_part.replace('p > 40', 'p > 38')
top_part = top_part.replace('p > 46', 'p > 38')
top_part = top_part.replace('max="46"', 'max="38"')
top_part = top_part.replace('Cover • 1 / 46', 'Cover • 1 / 38')
top_part = top_part.replace('goToPage(46, true)', 'goToPage(38, true)')
top_part = top_part.replace('href="bhrigu-nandi-nadi-karma-samyojan.pdf"', 'href="tantra-sadhana-siddhi-protocol.pdf"')
top_part = top_part.replace('download="Bhrigu-Nandi-Nadi-Karma-Samyojan-Sutra.pdf"', 'download="Tantra-Sadhana-Siddhi-Protocol.pdf"')
top_part = top_part.replace('href="bhrigu-nandi-nadi.html"', 'href="tantra-sadhana-siddhi.html"')
top_part = top_part.replace('वैदिक ज्योतिष महाग्रंथ सरलीकृत', 'तंत्र साधना सिद्धि महाग्रंथ')
top_part = top_part.replace('Complete Vedic Astrology Compendium Simplified', '41-Day Empirical Sadhana Protocol & Secret Rituals')
top_part = top_part.replace('सम्पूर्ण प्रामाणिक शास्त्रीय फलित ज्ञानकोश', 'श्री सिद्ध कुंजिका स्तोत्र एवं पंचाक्षरी महासाधना प्रत्यक्ष कल्प')

# Inject custom styling for hawan gallery, rule cards, and shloka boxes
custom_sadhana_styles = """
  <style>
    .hawan-flip-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin: 6px 0;
    }
    .rule-card {
      background: rgba(200, 157, 61, 0.08);
      border-left: 3px solid #b45309;
      border-radius: 4px;
      padding: 6px 10px;
      margin: 6px 0;
    }
    .rule-card.success {
      border-left-color: #059669;
      background: rgba(5, 150, 105, 0.08);
    }
    .rule-card.warning {
      border-left-color: #dc2626;
      background: rgba(220, 38, 38, 0.08);
    }
    .rule-card.info {
      border-left-color: #0284c7;
      background: rgba(2, 132, 199, 0.08);
    }
    .shloka-box, .mantra-box {
      background: rgba(200, 157, 61, 0.06);
      border: 1px solid #d97706;
      border-radius: 6px;
      padding: 6px 10px;
      margin: 6px 0;
    }
  </style>
"""
if '</head>' in top_part:
    top_part = top_part.replace('</head>', f'{custom_sadhana_styles}\n</head>')


# Page data definition
page_specs = [
    (1, "मुखपृष्ठ • Cover", "तंत्र साधना सिद्धि महाग्रंथ", '''<div class="cover-page-wrapper" style="text-align:center; padding:2rem 1rem;">
  <div style="font-size:1.1rem; color:#fde047; font-weight:700; margin-bottom:1rem;">॥ ॐ नमः शिवाय • ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे ॥</div>
  <div style="margin:1.5rem auto;"><img src="assets/yantra.svg" alt="Yantra" width="115" height="115"></div>
  <h2 style="font-size:1.85rem; color:#fde047; font-family:'Noto Serif Devanagari',serif; font-weight:900; margin:1rem 0 0.4rem 0;">तंत्र साधना सिद्धि महाग्रंथ</h2>
  <div style="font-size:1.05rem; color:#a5b4fc; font-weight:600; margin-bottom:1.3rem;">41-Day Empirical Sadhana Protocols & Secret Rituals</div>
  <p style="font-size:0.88rem; color:#e2e8f0; max-width:480px; margin:0 auto 1.3rem auto; line-height:1.6;">
    सवा लाख (1,25,000) पंचाक्षरी जप, श्री सिद्ध कुंजिका स्तोत्र 21 पाठ, वेदी निर्माण, 8:30 PM–10:40 PM मिनट-दर-मिनट अनुष्ठान, स्वास्थ्य प्रबंधन एवं संपुट रहस्य।
  </p>
  <div style="border-top:1px solid #d97706; border-bottom:1px solid #d97706; padding:0.8rem 0; max-width:440px; margin:0 auto; color:#fef3c7; font-size:0.88rem;">
    <strong>प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</strong><br>
    <span style="font-size:0.8rem; color:#cbd5e1;">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) • 2026</span>
  </div>
</div>'''),
    (2, "मंगलाचरण • Invocation", "शिव-शक्ति व बटुक भैरव स्मरण", '''<div style="text-align:center; padding:1.5rem;">
  <div style="font-size:1.8rem; margin-bottom:0.8rem;">🔱 卐 🪔</div>
  <div class="shloka-box" style="background:rgba(200,157,61,0.08); border:1px solid #d97706; border-radius:8px; padding:1.2rem; margin:1rem auto; max-width:540px;">
    <div style="font-family:'Noto Serif Devanagari',serif; font-size:1.05rem; font-weight:700; color:#b45309; line-height:1.8;">
      ॥ नमो देव्यै महादेव्यै शिवायै सततं नमः ।<br>
      नमः प्रकृत्यै भद्रायै नियताः प्रणताः स्म ताम् ॥<br>
      ॥ ॐ ह्रीं बटुकाय आपदुद्धारणाय कुरु कुरु बटुकाय ह्रीं ॐ ॥
    </div>
  </div>
  <p style="font-size:0.92rem; color:var(--text-main); line-height:1.7; max-width:520px; margin:1rem auto;">
    यह महाग्रंथ तंत्र-शास्त्र के उन प्रत्यक्ष, गोपनीय एवं वैज्ञानिक विधि-विधानों को प्रस्तुत करता है जो साधक को बिना किसी भ्रम अथवा भय के आत्म-शुद्धि, देव-कृपा एवं मंत्र-सिद्धि का मार्ग प्रशस्त करते हैं।
  </p>
</div>'''),
    (3, "लेखक परिचय • About Author", "ज्योतिषाचार्य आशुतोष कुमार चौबे", '''<div class="rule-card">
  <div class="rule-title"><span>✍️</span> प्रणेता परिचय (About Astrologer Ashutosh Kumar Choubey)</div>
  <div class="rule-body" style="font-size:0.9rem; line-height:1.7;">
    <strong>ज्योतिषाचार्य आशुतोष कुमार चौबे</strong> तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) के संस्थापक एवं मुख्य शोध-अन्वेषक हैं। वे वैदिक ज्योतिष, भृगु नंदी नाड़ी, तंत्र साधना एवं आयुर्वेद के दुर्लभ सूत्रों के वैज्ञानिक अनुसंधान हेतु समर्पित हैं।
    <br><br>
    <strong>आधिकारिक मंच:</strong>
    <br>• वेबसाइट: <a href="https://t.worldgyan.com" target="_blank">t.worldgyan.com</a>
    <br>• यूट्यूब: <a href="https://www.youtube.com/@TantraGyan108" target="_blank">@TantraGyan108</a>
    <br>• ईमेल: tantraresearchcenter@gmail.com
  </div>
</div>'''),
    (4, "ग्रंथ परिचय • Preface", "साधना का वैज्ञानिक व आध्यात्मिक आधार", '''<div class="rule-card">
  <div class="rule-title"><span>✦</span> ग्रंथ का उद्देश्य एवं वैज्ञानिक दृष्टिकोण</div>
  <div class="rule-body" style="font-size:0.9rem; line-height:1.7;">
    तांत्रिक साधना कोई जादू-टोना नहीं, बल्कि मानव शरीर के स्नायु-तंत्र (Central Nervous System), श्वास की गति और चेतना (Consciousness) को परा-चेतना से जोड़ने का एक अत्यंत सुव्यवस्थित विज्ञान है।
    <br><br>
    इस ग्रंथ में:
    <br>1. <strong>सवा लाख पंचाक्षरी जप</strong> द्वारा सूक्ष्म शरीर की शुद्धि।
    <br>2. <strong>द्वैत दीप विज्ञान</strong> द्वारा नकारात्मक ऊर्जा का पूर्ण शमन।
    <br>3. <strong>मिनट-दर-मिनट समय अनुशासन</strong> (8:30 PM–10:40 PM) से ऊर्जा का अधिकतम संचय सुनिश्चित किया गया है।
  </div>
</div>'''),
    (5, "अनुक्रमणिका • Contents", "संपूर्ण 8 अध्यायों की रूपरेखा", '''<div style="font-size:0.86rem; line-height:1.75;">
  <div style="font-weight:800; color:var(--accent-gold); margin-bottom:0.4rem;">अनुक्रमणिका (Table of Contents):</div>
  <ul style="list-style:none; padding-left:0;">
    <li><strong>अध्याय 1:</strong> 41-दिवसीय पंचाक्षरी साधना व 1,25,000 जप गणित (पृष्ठ 6–9)</li>
    <li><strong>अध्याय 2:</strong> तांत्रिक वेदी निर्माण, द्वैत दीप व 7-पद सामग्री (पृष्ठ 10–14)</li>
    <li><strong>अध्याय 3:</strong> दैनिक काल-तालिका (8:30 PM–10:40 PM) (पृष्ठ 15–20)</li>
    <li><strong>अध्याय 4:</strong> त्रि-स्तरीय स्वास्थ्य प्रबंधन व महिला साधक नियम (पृष्ठ 21–25)</li>
    <li><strong>अध्याय 5:</strong> षड्विध यम-नियम, प्राणायाम व स्वप्न-स्वर (पृष्ठ 26–30)</li>
    <li><strong>अध्याय 6:</strong> संपुट विधान, विवाह सिद्धि व 21 पाठ चक्र (पृष्ठ 31–33)</li>
    <li><strong>अध्याय 7:</strong> सिद्ध कुंजिका स्तोत्र सम्पूर्ण मूल पाठ (पृष्ठ 34)</li>
    <li><strong>अध्याय 8:</strong> 41वें दिन पूर्णाहुति हवन, षट्द्रव्य सामग्री, 9-चरणीय क्रम व आसन उत्थापन (पृष्ठ 35–37)</li>
    <li><strong>उपसंहार:</strong> ग्रंथ समापन, शांति पाठ एवं प्रणेता परिचय (पृष्ठ 38)</li>
  </ul>
</div>'''),
    (6, "अध्याय 1 • पंचाक्षरी साधना", "1,25,000 जप सिद्धि एवं प्रारम्भ नियम", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p>41 दिनों का काल-खंड तांत्रिक परंपरा में एक <strong>'मंडल काल'</strong> कहलाता है। किसी भी उच्च महाविद्या अथवा देवी साधना के प्रवेश हेतु साधक को भगवान शिव के पंचाक्षरी महामंत्र <strong>'ॐ नमः शिवाय'</strong> का सवा लाख (1,25,000) जप पूर्ण करना अनिवार्य है।</p>
  <div class="rule-card success">
    <strong>शुभारम्भ काल:</strong>
    <br>• सर्वोत्तम: कृष्ण पक्ष त्रयोदशी (प्रदोष काल)।
    <br>• विकल्प: सोमवार अथवा शुक्ल पक्ष प्रदोष तिथि।
    <br>• आरम्भ के दिन प्रातः स्नान, स्वच्छ वस्त्र एवं हल्का सात्विक आहार लें।
  </div>
</div>'''),
    (7, "अध्याय 1 • जप गणित", "दैनिक 3,049 जप एवं माला संख्या", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>सवा लाख जप का दैनिक गणितीय विभाजन:</strong></p>
  <table class="data-table" style="width:100%; font-size:0.84rem; margin:0.6rem 0;">
    <thead>
      <tr><th>मापदंड</th><th>संख्या / विवरण</th></tr>
    </thead>
    <tbody>
      <tr><td>कुल जप लक्ष्य</td><td>1,25,000 मंत्र</td></tr>
      <tr><td>साधना अवधि</td><td>41 दिन (एक मंडल)</td></tr>
      <tr><td>दैनिक जप लक्ष्य</td><td>3,049 मंत्र प्रति दिन</td></tr>
      <tr><td>दैनिक माला संख्या</td><td>28 से 31 माला (रुद्राक्ष माला 108)</td></tr>
      <tr><td>दैनिक समय</td><td>2 से 2.5 घंटे एकनिष्ठ अभ्यास</td></tr>
    </tbody>
  </table>
  <div class="rule-card info" style="margin-top:0.6rem;">
    <strong>सूत्र:</strong> 3,049 जप × 41 दिन = 1,25,009 मंत्र (सवा लाख जप सिद्ध)।
  </div>
</div>'''),
    (8, "अध्याय 1 • आरेख 1.1", "1,25,000 पंचाक्षरी जप महाचक्र", '''<div class="visual-chart-plate full-page-chart" style="text-align:center;">
  <img src="assets/icons/sadhana_panchakshari_125k_wheel.svg" alt="पंचाक्षरी जप सिद्धि चक्र" style="width:100%; max-width:520px; height:auto; display:block; margin:0 auto; border-radius:8px;">
  <div style="font-size:0.82rem; font-style:italic; color:var(--text-muted); margin-top:0.4rem;">
    आरेख 1.1: 41-दिवसीय पंचाक्षरी महासाधना एवं 1,25,000 जप सिद्धि चक्र
  </div>
</div>'''),
    (9, "अध्याय 1 • विल्वपत्र विधान", "पंचोपचार व 41वें दिन का समापन", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>दैनिक पंचोपचार एवं विल्वपत्र अर्पण:</strong></p>
  <ul style="padding-left:1.2rem; margin-bottom:0.8rem;">
    <li><strong>पंचोपचार:</strong> गंध (श्वेत चंदन), पुष्प, धूप, दीप एवं नैवेद्य अर्पित करें।</li>
    <li><strong>विल्वपत्र:</strong> चिकने भाग पर चंदन से ॐ नमः शिवाय लिखकर शिवलिंग/प्रतिमा पर उल्टी दिशा में अर्पित करें।</li>
    <li><strong>माला नियम:</strong> रुद्राक्ष माला को गोमुखी में रखें; अनामिका और अंगुष्ठ से फेरें; सुमेरु न लांघें।</li>
  </ul>
  <div class="rule-card">
    41वें दिन दशांश हवन (108 आहुति), मंदिर में प्रसाद वितरण एवं ताम्र/रजत पात्र में मंत्र स्थापन करें।
  </div>
</div>'''),
    (10, "अध्याय 2 • वेदी निर्माण", "पवित्र काष्ठ चौकी एवं दिशा विन्यास", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>तांत्रिक वेदी निर्माण एवं दिशा विन्यास:</strong></p>
  <p>साधना कक्ष में काष्ठ (लकड़ी) की एक पवित्र चौकी स्थापित करें। चौकी पर शुद्ध लाल अथवा पीला वस्त्र बिछाएं।</p>
  <div class="rule-card success">
    <strong>दिशा नियम:</strong> साधक का मुख सदैव <strong>उत्तर (North)</strong> अथवा <strong>पूर्व (East)</strong> दिशा की ओर होना चाहिए। उत्तर दिशा सदाशिव और कुबेर की दिशा है जो चेतना को उर्ध्वगामी बनाती है।
  </div>
  <p>41 दिनों तक वेदी और आसन का स्थान कभी न बदलें; एक ही स्थान पर ऊर्जा का संचय होता है।</p>
</div>'''),
    (11, "अध्याय 2 • द्वैत दीप विज्ञान", "घृत दीप (सत्व) एवं सरसों तैल दीप (रक्षा)", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>द्वैत दीप विज्ञान (Dual Diya Physics):</strong></p>
  <div class="rule-card" style="border-left-color:#f59e0b; margin-bottom:0.6rem;">
    <strong>1. शुद्ध गो-घृत दीपक (दाहिनी ओर / Right):</strong>
    <br>सत्व गुण का प्रतीक; माँ दुर्गा व भगवान शिव की सात्विक चेतना को आकर्षित करता है।
  </div>
  <div class="rule-card" style="border-left-color:#334155; margin-bottom:0.6rem;">
    <strong>2. सरसों तैल दीपक (बाईं ओर / Left):</strong>
    <br>भैरव रक्षा कवच; समस्त नकारात्मक शक्तियों, भूत-प्रेत एवं तंद्रा से साधक की रक्षा करता है।
  </div>
</div>'''),
    (12, "अध्याय 2 • सामग्री क्रम", "7-पद शास्त्रीय अर्पण अनुक्रम", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>शास्त्रीय 7-पद सामग्री अर्पण क्रम:</strong></p>
  <div class="rule-card info">
    <strong>1. जल (आचमन) ➔ 2. अक्षत (अखंडित) ➔ 3. चंदन (रक्त/श्वेत) ➔ 4. इत्र (गुलाब/चंदन) ➔ 5. धूप (गुग्गुल) ➔ 6. दीप (दर्शन) ➔ 7. प्रसाद (नैवेद्य)</strong>
  </div>
  <p>इस शास्त्रीय क्रम से पंचभूतों का आदर होता है और वेदी का चुंबकीय क्षेत्र संतुलित रहता है।</p>
</div>'''),
    (13, "अध्याय 2 • आरेख 2.1", "वेदी निर्माण एवं द्वैत दीप महाचक्र", '''<div class="visual-chart-plate full-page-chart" style="text-align:center;">
  <img src="assets/icons/sadhana_altar_mandala.svg" alt="तांत्रिक वेदी निर्माण एवं द्वैत दीप चक्र" style="width:100%; max-width:520px; height:auto; display:block; margin:0 auto; border-radius:8px;">
  <div style="font-size:0.82rem; font-style:italic; color:var(--text-muted); margin-top:0.4rem;">
    आरेख 2.1: तांत्रिक वेदी निर्माण, द्वैत दीप विज्ञान एवं 7-पद सामग्री क्रम
  </div>
</div>'''),
    (14, "अध्याय 2 • आचमन विधि", "काया, प्राण व बुद्धि शुद्धि मंत्र", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>आचमन / याच्यापान विधि (3 बार जल ग्रहण):</strong></p>
  <div class="shloka-box" style="padding:0.8rem; margin:0.6rem 0;">
    <div style="font-family:'Noto Serif Devanagari',serif; font-size:0.95rem; font-weight:700; color:#b45309; line-height:1.8;">
      1. ॐ केशवाय नमः स्वाहा। (काया शुद्धि)<br>
      2. ॐ नारायणाय नमः स्वाहा। (प्राण शुद्धि)<br>
      3. ॐ माधवाय नमः स्वाहा। (मन-बुद्धि शुद्धि)
    </div>
  </div>
  <p>दाहिनी हथेली से तीन बार आचमन कर 'ॐ हृषीकेशाय नमः' बोलकर हाथ धोएं।</p>
</div>'''),
    (15, "अध्याय 3 • दैनिक काल-तालिका", "8:30 PM से 10:40 PM साधना चक्र", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>दैनिक साधना काल-तालिका (8:30 PM – 10:40 PM):</strong></p>
  <p>साधना में समय की पाबंदी सर्वोपरि है। 8:00 से 8:30 PM के मध्य स्नान कर शुद्ध वस्त्र धारण करें। ঠিক 8:30 PM पर वेदी पर उपस्थित हों।</p>
  <div class="rule-card warning">
    <strong>नियम:</strong> प्रत्येक मंत्र के पश्चात <strong>1 मिनट का गहरा श्वास (Deep Breathing Rest)</strong> अनिवार्य है।
  </div>
</div>'''),
    (16, "अध्याय 3 • पूर्वांग क्रम", "8:30 PM से 8:56 PM मंत्र क्रम", '''<div style="font-size:0.86rem; line-height:1.65;">
  <table class="data-table" style="width:100%; font-size:0.82rem;">
    <thead><tr><th>समय</th><th>क्रिया</th><th>अवधि</th></tr></thead>
    <tbody>
      <tr><td>8:30 PM</td><td>वेदी तैयारी व दीप प्रज्वलन</td><td>5 min</td></tr>
      <tr><td>8:35 PM</td><td>संकल्प एवं पूर्वांग आचमन</td><td>10 min</td></tr>
      <tr><td>8:45 PM</td><td>ॐ नमः शिवाय (11 बार) + विश्राम</td><td>1+1 min</td></tr>
      <tr><td>8:47 PM</td><td>ॐ गं गणपतये नमः (11 बार) + विश्राम</td><td>1+1 min</td></tr>
      <tr><td>8:49 PM</td><td>बटुक भैरव रक्षा मंत्र (11 बार) + विश्राम</td><td>3+1 min</td></tr>
      <tr><td>8:53 PM</td><td>हरे कृष्ण महामंत्र (11 बार) + विश्राम</td><td>3+1 min</td></tr>
    </tbody>
  </table>
</div>'''),
    (17, "अध्याय 3 • कवच व स्तुति", "8:57 PM से 9:27 PM रक्षा विधान", '''<div style="font-size:0.86rem; line-height:1.65;">
  <table class="data-table" style="width:100%; font-size:0.82rem;">
    <thead><tr><th>समय</th><th>क्रिया</th><th>अवधि</th></tr></thead>
    <tbody>
      <tr><td>8:57 PM</td><td>श्री हनुमान चालीसा (1 सम्पूर्ण पाठ) + विश्राम</td><td>5+1 min</td></tr>
      <tr><td>9:03 PM</td><td>श्री दुर्गा कवच (सम्पूर्ण पाठ) + विश्राम</td><td>20+1 min</td></tr>
      <tr><td>9:24 PM</td><td>महामृत्युंजय मंत्र (11 बार) + विश्राम</td><td>3+1 min</td></tr>
    </tbody>
  </table>
  <div class="rule-card success" style="margin-top:0.6rem;">
    दुर्गा कवच से दशों दिशाओं में सुरक्षा चक्र बनता है और महामृत्युंजय मंत्र संजीवनी शक्ति देता है।
  </div>
</div>'''),
    (18, "अध्याय 3 • मुख्य कुंजिका पाठ", "9:28 PM से 10:40 PM समापन", '''<div style="font-size:0.86rem; line-height:1.65;">
  <table class="data-table" style="width:100%; font-size:0.82rem;">
    <thead><tr><th>समय</th><th>मुख्य साधना</th><th>अवधि</th></tr></thead>
    <tbody>
      <tr><td>9:28 PM</td><td>★ सिद्ध कुंजिका स्तोत्र (21 पाठ)</td><td>65 min</td></tr>
      <tr><td>10:33 PM</td><td>क्षमा प्रार्थना (Forgiveness)</td><td>2 min</td></tr>
      <tr><td>10:35 PM</td><td>आरती एवं आसन उत्थापन</td><td>5 min</td></tr>
      <tr><td>10:40 PM</td><td>सीधे मौन शयन (Immediate Sleep)</td><td>तत्काल</td></tr>
    </tbody>
  </table>
  <div class="rule-card" style="margin-top:0.6rem;">
    शिव उवाच केवल 1st एवं 21st पाठ में ही पढ़ें; मध्यवर्ती 19 पाठों में केवल मूल मंत्र।
  </div>
</div>'''),
    (19, "अध्याय 3 • आरेख 3.1", "दैनिक साधना काल-तालिका महाचक्र", '''<div class="visual-chart-plate full-page-chart" style="text-align:center;">
  <img src="assets/icons/sadhana_timeline_clock.svg" alt="दैनिक साधना काल-तालिका चक्र" style="width:100%; max-width:520px; height:auto; display:block; margin:0 auto; border-radius:8px;">
  <div style="font-size:0.82rem; font-style:italic; color:var(--text-muted); margin-top:0.4rem;">
    आरेख 3.1: दैनिक साधना काल-तालिका (8:30 PM – 10:40 PM) मिनट-दर-मिनट अनुक्रम
  </div>
</div>'''),
    (20, "अध्याय 3 • शयन विज्ञान", "साधना पश्चात ऊर्जा संचय का नियम", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>साधना पश्चात तत्काल शयन विज्ञान:</strong></p>
  <p>10:40 PM पर साधना समाप्त होते ही बिना किसी से बात किए, बिना फोन देखे सीधे शयन करें।</p>
  <div class="rule-card info">
    <strong>तांत्रिक रहस्य:</strong> साधना में अर्जित ब्रह्मांडीय ऊर्जा निद्रा काल में साधक के सूक्ष्म शरीर (Astral Body) में संचित होती है। किसी से भी बोलने या स्क्रीन देखने से ऊर्जा तुरंत नष्ट हो जाती है।
  </div>
</div>'''),
    (21, "अध्याय 4 • स्वास्थ्य प्रबंधन", "त्रि-स्तरीय बीमारी प्रबंधन प्रोटोकॉल", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>त्रि-स्तरीय बीमारी प्रबंधन प्रोटोकॉल:</strong></p>
  <div class="rule-card success" style="margin-bottom:0.5rem;">
    <strong>स्तर 1 (हल्की बीमारी):</strong> सर्दी, खांसी, बुखार। तुरंत उपचार लें; साधना को <strong>100% जारी रखें</strong>।
  </div>
  <div class="rule-card" style="border-left-color:#f59e0b; margin-bottom:0.5rem;">
    <strong>स्तर 2 (मध्यम समस्या):</strong> तेज दर्द, कमजोरी। डॉक्टर से परामर्श लें; दिन में कम से कम 1 पाठ उसी स्थान व समय पर करें।
  </div>
  <div class="rule-card" style="border-left-color:#dc2626;">
    <strong>स्तर 3 (गंभीर आपात स्थिति):</strong> अस्पताल भर्ती। साधना तुरंत रोकें; स्वस्थ होने पर पुनः संकल्प लेकर शुरू करें।
  </div>
</div>'''),
    (22, "अध्याय 4 • आकस्मिक न्यूनतम", "10:00-10:15 PM पर 1 से 3 पाठ", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>आकस्मिक न्यूनतम अभ्यास (Emergency Minimum):</strong></p>
  <p>यदि शारीरिक अस्वस्थता या अपरिहार्य कारण से 21 पाठ संभव न हों:</p>
  <div class="rule-card warning">
    <strong>समय:</strong> 10:00 PM – 10:15 PM<br>
    <strong>अभ्यास:</strong> सिद्ध कुंजिका स्तोत्र के 1 से 3 पाठ करें।<br>
    <strong>स्थान:</strong> नियमित साधना का ही स्थान हो।<br>
    <strong>अंत:</strong> 2 मिनट क्षमा प्रार्थना अवश्य करें।
  </div>
</div>'''),
    (23, "अध्याय 4 • आरेख 4.1", "स्वास्थ्य प्रबंधन एवं आपातकालीन महाचक्र", '''<div class="visual-chart-plate full-page-chart" style="text-align:center;">
  <img src="assets/icons/sadhana_health_emergency_matrix.svg" alt="स्वास्थ्य प्रबंधन एवं आपातकालीन चक्र" style="width:100%; max-width:520px; height:auto; display:block; margin:0 auto; border-radius:8px;">
  <div style="font-size:0.82rem; font-style:italic; color:var(--text-muted); margin-top:0.4rem;">
    आरेख 4.1: साधना काल में स्वास्थ्य प्रबंधन एवं त्रि-स्तरीय आपातकालीन प्रोटोकॉल
  </div>
</div>'''),
    (24, "अध्याय 4 • स्वास्थ्य दर्शन", "रोग-निवृत्ति एवं तांत्रिक स्वास्थ्य सुरक्षा", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>तांत्रिक स्वास्थ्य दर्शन एवं प्रारब्ध शोधन:</strong></p>
  <div class="rule-card" style="border-left-color:#0284c7; margin-bottom:0.6rem;">
    • <strong>प्रारब्ध कर्म शोधन:</strong> 41-दिवसीय तीव्र साधना में शरीर की ऊर्जा में तीव्र परिवर्तन आता है। कभी-कभी शारीरिक अस्वस्थता संचित प्रारब्ध की कर्म-शुद्धि का साधन बनकर उभरती है। साधक विचलित न हों।
  </div>
  <div class="rule-card" style="border-left-color:#b45309; margin-bottom:0.6rem;">
    • <strong>महामृत्युंजय व भैरव रक्षा:</strong> अस्वस्थता की दशा में मानसिक रूप से 11 बार महामृत्युंजय मंत्र अथवा बटुक भैरव आपदुद्धारक मंत्र का स्मरण कर साधना की रक्षा करें।
  </div>
  <div class="rule-card" style="border-left-color:#15803d;">
    • <strong>शरीरं खलु धर्मसाधनम्:</strong> शरीर ही समस्त साधनाओं का प्राथमिक आधार है। चिकित्सा में कभी उपेक्षा न करें।
  </div>
</div>'''),
    (25, "अध्याय 4 • महिला साधक नियम", "मासिक धर्म प्रोटोकॉल व पाठ भरपाई", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>महिला साधक विशेष नियम (Women’s Protocol):</strong></p>
  <div class="rule-card" style="border-left-color:#be185d;">
    • <strong>मासिक धर्म के दिन:</strong> शारीरिक रूप से वेदी स्पर्श न करें। शयन कक्ष में बैठकर मानसिक रूप से प्रतिदिन केवल 1 पाठ करें व क्षमा प्रार्थना करें।<br>
    • <strong>अन्य मंत्रों का निषेध:</strong> इन दिनों में केवल कुंजिका पाठ करें; अन्य उग्र मंत्र न पढ़ें।<br>
    • <strong>छूटे पाठों की भरपाई:</strong> शुद्धि के उपरांत 5 दिनों के छूटे हुए पाठ 41 दिनों के बाद अतिरिक्त दिन जोड़कर पूर्ण करें।
  </div>
</div>'''),
    (26, "अध्याय 5 • यम-नियम (भाग 1)", "ब्रह्मचर्य, सात्विक आहार व मौन व्रत", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>षड्विध तांत्रिक यम-नियम (प्रथम 3 स्तम्भ):</strong></p>
  <div class="rule-card" style="border-left-color:#991b1b; margin-bottom:0.5rem;">
    <strong>1. ब्रह्मचर्य (Complete Celibacy):</strong> कायिक, मानसिक व दृश्य ब्रह्मचर्य। कामुक विचारों एवं उत्तेजक दृश्यों से पूर्ण विरक्ति।
  </div>
  <div class="rule-card" style="border-left-color:#15803d; margin-bottom:0.5rem;">
    <strong>2. सात्विक आहार:</strong> लहसुन, प्याज, मांसाहार, मद्य, तंबाकू पूर्ण वर्जित। 3 घंटे से अधिक पुराना भोजन न लें।
  </div>
  <div class="rule-card" style="border-left-color:#1d4ed8;">
    <strong>3. मौन एवं वाणी संयम:</strong> केवल अनिवार्य संवाद। फोन दूसरे कमरे में रखें; सोशल मीडिया व फिल्में वर्जित।
  </div>
</div>'''),
    (27, "अध्याय 5 • यम-नियम (भाग 2)", "भूमि शयन, स्थिर आसन व मेरुदंड शुद्धि", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>शारीरिक अनुशासन (Physical Austerities):</strong></p>
  <ul style="padding-left:1.2rem;">
    <li><strong>भूमि शयन:</strong> 41 दिनों तक स्वच्छ चटाई व चादर पर फर्श पर शयन करें। गद्देदार पलंग वर्जित।</li>
    <li><strong>स्थिर आसन:</strong> प्रतिदिन एक ही कुशासन अथवा ऊनी कम्बल पर बैठें।</li>
    <li><strong>रीढ़ सीधी:</strong> मेरुदंड पूर्णतः सीधा रहे जिससे सुषुम्ना नाड़ी में प्राण-ऊर्जा का प्रवाह अबाध रहे।</li>
  </ul>
</div>'''),
    (28, "अध्याय 5 • प्रातः प्राणायाम", "7:30-8:00 AM कपालभाति व अनुलोम-विलोम", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>प्रातः दिनचर्या एवं प्राणायाम (7:00 AM – 8:00 AM):</strong></p>
  <div class="rule-card success">
    <strong>7:00 AM:</strong> 8 घंटे की गहरी निद्रा के उपरांत प्राकृतिक जागरण।<br>
    <strong>7:00–7:30 AM:</strong> शौच-स्नान एवं शारीरिक शुद्धि।<br>
    <strong>7:30–7:40 AM:</strong> कपालभाति प्राणायाम (10 मिनट - विषाक्त वायु निष्कासन)।<br>
    <strong>7:40–7:50 AM:</strong> अनुलोम-विलोम प्राणायाम (10 मिनट - इड़ा-पिंगला संतुलन)।<br>
    <strong>7:50–8:00 AM:</strong> विश्राम एवं दैनिक कार्यों में प्रवेश।
  </div>
</div>'''),
    (29, "अध्याय 5 • स्वप्न-स्वर विज्ञान", "अचेतन मन का शोधन व देव संकेत", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>स्वप्न एवं स्वर विज्ञान (Dream & Swara Practice):</strong></p>
  <ul style="padding-left:1.2rem;">
    <li><strong>स्वप्न डायरी:</strong> जागते ही बिना बत्ती जलाए स्वप्न डायरी में लिखें (फोन में नहीं)।</li>
    <li><strong>स्वर परीक्षण:</strong> जागते समय कौन सा नथुना (बायां इड़ा / दायां पिंगला) सक्रिय था, नोट करें।</li>
    <li><strong>तांत्रिक रहस्य:</strong> साधना काल के स्वप्न आंतरिक शुद्धि और देवी संकेतों के प्रत्यक्ष दर्पण होते हैं।</li>
  </ul>
</div>'''),
    (30, "अध्याय 5 • आरेख 5.1", "षड्विध तांत्रिक यम-नियम महाचक्र", '''<div class="visual-chart-plate full-page-chart" style="text-align:center;">
  <img src="assets/icons/sadhana_lifestyle_disciplines_chart.svg" alt="षड्विध तांत्रिक यम-नियम चक्र" style="width:100%; max-width:520px; height:auto; display:block; margin:0 auto; border-radius:8px;">
  <div style="font-size:0.82rem; font-style:italic; color:var(--text-muted); margin-top:0.4rem;">
    आरेख 5.1: षड्विध तांत्रिक यम-नियम, प्राणायाम एवं स्वप्न-स्वर विज्ञान
  </div>
</div>'''),
    (31, "अध्याय 6 • संपुट विधान", "मंत्र ऊर्जा का संपुट एवं विवाह सिद्धि", '''<div style="font-size:0.88rem; line-height:1.7;">
  <p><strong>संपुट विधान का तांत्रिक रहस्य:</strong></p>
  <p>संपुट का अर्थ है — किसी विशेष उद्देश्य की पूर्ति हेतु मूल मंत्र के आगे और पीछे अभीष्ट श्लोक को जोड़कर ऊर्जा को लॉक (Lock) कर देना।</p>
  <div class="rule-card success">
    <strong>शीघ्र विवाह संपुट श्लोक:</strong><br>
    “पत्नीं मनोरमां देहि मनोवृत्तानुसारिणीम् ।<br>
    तारिणीं दुर्गसंसारसागरस्य कुलोद्भवाम् ॥”
  </div>
  <p>यह प्रयोग वैवाहिक बाधा, मांगलिक दोष एवं विवाह में विलंब का अचूक समाधान करता है।</p>
</div>'''),
    (32, "अध्याय 6 • 21 पाठ चक्र", "संपुट सहित प्रत्येक पाठ का संपूर्ण अनुक्रम", '''<div style="font-size:0.86rem; line-height:1.65;">
  <p><strong>21 पाठों में प्रत्येक पाठ का संपुट चक्र:</strong></p>
  <div class="rule-card" style="margin-bottom:0.4rem;">
    <strong>1. आदि संपुट:</strong> “पत्नीं मनोरमां देहि मनोवृत्तानुसारिणीम्... कुलोद्भवाम् ॥”
  </div>
  <div class="rule-card info" style="margin-bottom:0.4rem;">
    <strong>2. अथ मन्त्रः:</strong> ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे... फट् स्वाहा ॥
  </div>
  <div class="rule-card warning" style="margin-bottom:0.4rem;">
    <strong>3. इति मन्त्रः:</strong> नमस्ते रुद्ररूपिण्यै... मंत्रसिद्धिं कुरूष्व मे ॥
  </div>
  <div class="rule-card" style="margin-bottom:0.4rem;">
    <strong>4. अंत संपुट:</strong> “पत्नीं मनोरमां देहि मनोवृत्तानुसारिणीम्... कुलोद्भवाम् ॥”
  </div>
  <p style="font-size:0.8rem; color:#64748b;">(पाठ 1 से 21 तक प्रत्येक बार यह 4-चरणीय चक्र चलेगा।)</p>
</div>'''),
    (33, "अध्याय 6 • आरेख 6.1", "संपुट विधान एवं विवाह सिद्धि महाचक्र", '''<div class="visual-chart-plate full-page-chart" style="text-align:center;">
  <img src="assets/icons/sadhana_samput_architecture.svg" alt="सिद्ध कुंजिका संपुट विधान चक्र" style="width:100%; max-width:520px; height:auto; display:block; margin:0 auto; border-radius:8px;">
  <div style="font-size:0.82rem; font-style:italic; color:var(--text-muted); margin-top:0.4rem;">
    आरेख 6.1: सिद्ध कुंजिका स्तोत्र संपुट विधान एवं विवाह सिद्धि चक्र
  </div>
</div>'''),
    (34, "अध्याय 7 • सिद्ध कुंजिका", "स्तोत्र सम्पूर्ण मूल संस्कृत पाठ", '''<div style="font-size:0.84rem; line-height:1.65;">
  <div class="shloka-box" style="padding:0.75rem; margin-bottom:0.6rem;">
    <div style="font-family:'Noto Serif Devanagari',serif; font-size:0.88rem; font-weight:700; color:#b91c1c; line-height:1.7;">
      ॥ शिव उवाच ॥<br>
      शृणु देवि प्रवक्ष्यामि कुञ्जिकास्तोत्रमुत्तमम् । येन मन्त्रप्रभावेण चण्डीजापः शुभो भवेत् ॥ 1 ॥<br>
      न कवचं नार्गलास्तोत्रं कीलकं न रहस्यकम् । न सूक्तं नापि ध्यानं च न न्यासो न च वाचनम् ॥ 2 ॥<br>
      कुञ्जिकापाठमात्रेण दुर्गापाठफलं लभेत् । अति गुह्यतरं देवि देवानामपि दुर्लभम् ॥ 3 ॥<br>
      ॥ अथ मन्त्रः ॥<br>
      ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे । ॐ ग्लौं हुं क्लीं जूं सः ज्वालय ज्वालय ज्वल ज्वल प्रज्वल प्रज्वल ऐं ह्रीं क्लीं चामुण्डायै विच्चे ज्वल हं सं लं क्षं फट् स्वाहा ॥<br>
      ॥ इति मन्त्रः ॥ नमस्ते रुद्ररूपिण्यै... सां सीं सूं सप्तशती देव्या मन्त्रसिद्धिं कुरुष्व मे ॥
    </div>
  </div>
</div>'''),
    (35, "अध्याय 8 • पूर्णाहुति हवन", "षड्विध सचित्र हवन सामग्री एवं ताम्र कुंड", '''<div style="font-size:0.86rem; line-height:1.65;">
  <p><strong>41वें दिन अनुष्ठान समापन हवन (षड्विध पवित्र सामग्री दर्शन):</strong></p>
  <div class="hawan-flip-grid" style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; margin:0.4rem 0;">
    <div style="background:rgba(200,157,61,0.06); border:1px solid #d97706; border-radius:6px; overflow:hidden; text-align:center;">
      <div style="position:relative; height:80px; background:#180802;">
        <img src="assets/images/hawan/samidha_mango.jpg" alt="आम की समिधा" style="width:100%; height:100%; object-fit:cover; display:block;">
        <span style="position:absolute; top:3px; left:3px; background:rgba(180,83,9,0.92); color:#fff; font-size:0.6rem; font-weight:800; padding:1px 4px; border-radius:3px;">1. समिधा</span>
      </div>
      <div style="padding:4px 5px;">
        <strong style="color:#78350f; font-size:0.75rem; display:block;">आम की समिधा</strong>
        <span style="color:#b45309; font-size:0.62rem; font-weight:700;">Mango Sticks</span>
        <div style="font-size:0.66rem; color:#475569; line-height:1.25; margin-top:2px;">अग्नि प्रज्वलन व मुख्य काष्ठ आधार</div>
      </div>
    </div>
    <div style="background:rgba(200,157,61,0.06); border:1px solid #d97706; border-radius:6px; overflow:hidden; text-align:center;">
      <div style="position:relative; height:80px; background:#180802;">
        <img src="assets/images/hawan/cow_ghee.jpg" alt="शुद्ध गाय का घी" style="width:100%; height:100%; object-fit:cover; display:block;">
        <span style="position:absolute; top:3px; left:3px; background:rgba(180,83,9,0.92); color:#fff; font-size:0.6rem; font-weight:800; padding:1px 4px; border-radius:3px;">2. घृत</span>
      </div>
      <div style="padding:4px 5px;">
        <strong style="color:#78350f; font-size:0.75rem; display:block;">देशी गो-घृत</strong>
        <span style="color:#b45309; font-size:0.62rem; font-weight:700;">Pure Cow Ghee</span>
        <div style="font-size:0.66rem; color:#475569; line-height:1.25; margin-top:2px;">अग्निदेव का प्रत्यक्ष हविष्य भोजन</div>
      </div>
    </div>
    <div style="background:rgba(200,157,61,0.06); border:1px solid #d97706; border-radius:6px; overflow:hidden; text-align:center;">
      <div style="position:relative; height:80px; background:#180802;">
        <img src="assets/images/hawan/black_sesame.jpg" alt="काले तिल" style="width:100%; height:100%; object-fit:cover; display:block;">
        <span style="position:absolute; top:3px; left:3px; background:rgba(180,83,9,0.92); color:#fff; font-size:0.6rem; font-weight:800; padding:1px 4px; border-radius:3px;">3. काले तिल</span>
      </div>
      <div style="padding:4px 5px;">
        <strong style="color:#78350f; font-size:0.75rem; display:block;">काले तिल</strong>
        <span style="color:#b45309; font-size:0.62rem; font-weight:700;">Black Sesame</span>
        <div style="font-size:0.66rem; color:#475569; line-height:1.25; margin-top:2px;">प्रधान हविष्य व कर्मदोष भस्म</div>
      </div>
    </div>
    <div style="background:rgba(200,157,61,0.06); border:1px solid #d97706; border-radius:6px; overflow:hidden; text-align:center;">
      <div style="position:relative; height:80px; background:#180802;">
        <img src="assets/images/hawan/barley_jau.jpg" alt="जौ" style="width:100%; height:100%; object-fit:cover; display:block;">
        <span style="position:absolute; top:3px; left:3px; background:rgba(180,83,9,0.92); color:#fff; font-size:0.6rem; font-weight:800; padding:1px 4px; border-radius:3px;">4. जौ</span>
      </div>
      <div style="padding:4px 5px;">
        <strong style="color:#78350f; font-size:0.75rem; display:block;">जौ (यव)</strong>
        <span style="color:#b45309; font-size:0.62rem; font-weight:700;">Sacred Barley</span>
        <div style="font-size:0.66rem; color:#475569; line-height:1.25; margin-top:2px;">आरोग्य, पुष्टि व समृद्धि सिद्धि</div>
      </div>
    </div>
    <div style="background:rgba(200,157,61,0.06); border:1px solid #d97706; border-radius:6px; overflow:hidden; text-align:center;">
      <div style="position:relative; height:80px; background:#180802;">
        <img src="assets/images/hawan/kamalgatta.jpg" alt="कमलगट्टा" style="width:100%; height:100%; object-fit:cover; display:block;">
        <span style="position:absolute; top:3px; left:3px; background:rgba(180,83,9,0.92); color:#fff; font-size:0.6rem; font-weight:800; padding:1px 4px; border-radius:3px;">5. कमलगट्टा</span>
      </div>
      <div style="padding:4px 5px;">
        <strong style="color:#78350f; font-size:0.75rem; display:block;">कमलगट्टा बीज</strong>
        <span style="color:#b45309; font-size:0.62rem; font-weight:700;">Lotus Seeds</span>
        <div style="font-size:0.66rem; color:#475569; line-height:1.25; margin-top:2px;">देवी महालक्ष्मी व दुर्गा प्रिय आहुति</div>
      </div>
    </div>
    <div style="background:rgba(200,157,61,0.06); border:1px solid #d97706; border-radius:6px; overflow:hidden; text-align:center;">
      <div style="position:relative; height:80px; background:#180802;">
        <img src="assets/images/hawan/hawan_samagri.jpg" alt="हवन सामग्री" style="width:100%; height:100%; object-fit:cover; display:block;">
        <span style="position:absolute; top:3px; left:3px; background:rgba(180,83,9,0.92); color:#fff; font-size:0.6rem; font-weight:800; padding:1px 4px; border-radius:3px;">6. मिश्रण</span>
      </div>
      <div style="padding:4px 5px;">
        <strong style="color:#78350f; font-size:0.75rem; display:block;">हवन सामग्री</strong>
        <span style="color:#b45309; font-size:0.62rem; font-weight:700;">Herbal Mix</span>
        <div style="font-size:0.66rem; color:#475569; line-height:1.25; margin-top:2px;">दिव्य सुगंधित जड़ी-बूटी मिश्रण</div>
      </div>
    </div>
  </div>
  <div class="rule-card" style="padding:6px 10px; margin:4px 0; font-size:0.78rem;">
    <strong>📦 सहायक उपकरण:</strong> ताम्र हवन कुंड, काष्ठ स्रुवा, घृत पात्र, भीमसेनी कर्पूर, पुष्प-अक्षत, सूखा गोला (नारियल) व कलावा।
  </div>
</div>'''),
    (36, "अध्याय 8 • हवन विधि", "मुख्य मंत्र एवं नव-चरणीय शास्त्रीय अनुक्रम", '''<div style="font-size:0.84rem; line-height:1.6;">
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-bottom:6px;">
    <div class="rule-card" style="padding:5px 8px; margin:0;">
      <strong style="color:#78350f; font-size:0.78rem;">A. शिव पंचाक्षरी आहुति मंत्र:</strong>
      <div style="font-family:'Noto Serif Devanagari',serif; font-size:0.9rem; font-weight:700; color:#b45309; margin-top:2px;">
        ॥ ॐ नमः शिवाय स्वाहा ॥
      </div>
    </div>
    <div class="rule-card warning" style="padding:5px 8px; margin:0;">
      <strong style="color:#991b1b; font-size:0.78rem;">B. चामुण्डा सिद्ध कुंजिका मंत्र:</strong>
      <div style="font-family:'Noto Serif Devanagari',serif; font-size:0.76rem; font-weight:700; color:#7f1d1d; margin-top:2px;">
        ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे... फट् स्वाहा॥
      </div>
      <span style="font-size:0.65rem; color:#dc2626;">(अंत में स्वाहा है, पुनः अतिरिक्त स्वाहा न जोड़ें)</span>
    </div>
  </div>
  <div style="font-weight:800; color:var(--accent-gold); font-size:0.82rem; margin:4px 0 2px;">
    9-चरणीय हवन क्रम (9-Step Ritual Sequence):
  </div>
  <ol style="padding-left:1.1rem; margin:0; font-size:0.8rem; line-height:1.55;">
    <li><strong>गणेश पूजन:</strong> ॐ गं गणपतये नमः (11 बार स्मरण व पुष्प समर्पण)</li>
    <li><strong>संकल्प:</strong> "मम उपात्त समस्त दुरितक्षयद्वारा... पूर्णाहुत्यर्थं हवनं करिष्ये"</li>
    <li><strong>अग्नि स्थापना:</strong> 5 घृत आहुतियां (अग्नये, सोमाय, अग्निसोमाभ्यां, प्रजापतये, इन्द्राय स्वाहा)</li>
    <li><strong>शिव पंचाक्षरी आहुति:</strong> ॐ नमः शिवाय स्वाहा (मृगी मुद्रा से)</li>
    <li><strong>चामुण्डा कुंजिका आहुति:</strong> कमलगट्टा, तिल, जौ व घृत से आहुति</li>
    <li><strong>स्विष्टकृत आहुति:</strong> ॐ अग्नये स्विष्टकृते स्वाहा (दोष निवारण)</li>
    <li><strong>पूर्णाहुति:</strong> सूखा गोला (नारियल), सुपारी व घृत से ॐ पूर्णमदः पूर्णमिदं... स्वाहा</li>
    <li><strong>क्षमा प्रार्थना:</strong> अज्ञानाद्विस्मृतेर्भ्रान्त्या यन्न्यूनमधिकं कृतम्... क्षम्यतां देवि</li>
    <li><strong>आरती व प्रसाद:</strong> कर्पूर आरती, प्रसाद वितरण व ऊर्जा कीलन</li>
  </ol>
</div>'''),
    (37, "अध्याय 8 • आहुति निर्णय", "आहुति संख्या (108 बनाम 12,500), कर्तव्य व अग्नि सुरक्षा", '''<div style="font-size:0.84rem; line-height:1.6;">
  <div style="margin-bottom:6px;">
    <strong style="color:var(--accent-gold); font-size:0.82rem;">आहुति संख्या निर्णय (Clarification & 2 Editions):</strong>
    <table class="data-table" style="width:100%; font-size:0.76rem; margin:4px 0;">
      <thead>
        <tr>
          <th>संस्करण</th>
          <th>आहुति संख्या</th>
          <th>प्रयोजन व उपयुक्तता</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>विधि A (संक्षिप्त)</strong></td>
          <td><strong>108 आहुतियां</strong></td>
          <td>गृहस्थ साधकों हेतु ताम्र कुंड में व्यावहारिक समापन हवन।</td>
        </tr>
        <tr>
          <td><strong>विधि B (पूर्ण दशांश)</strong></td>
          <td><strong>12,500 आहुतियां</strong></td>
          <td>1,25,000 जप का वास्तविक 10% दशांश (यज्ञशाला/मंदिर)।</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="rule-card success" style="padding:5px 8px; margin:4px 0; font-size:0.75rem;">
    <strong>★ 861 कुंजिका पाठों का नियम:</strong> 21 × 41 = 861 पाठों की अलग से दशांश आहुति शास्त्र में नहीं है; यह स्वयंसिद्ध जाग्रत स्तोत्र है। इसे 12,500 पंचाक्षरी आहुतियों में न मिलाएं।
  </div>
  <div style="font-size:0.78rem; line-height:1.45; margin:5px 0;">
    <strong>हवनोपरांत 3 पवित्र कर्तव्य:</strong> 1. मंदिर भोग व प्रसाद वितरण • 2. कन्या पूजन (1-9 कन्याएं) • 3. भोजपत्र यंत्र/मंजूषा स्थापन पूजा घर में।
  </div>
  <div class="shloka-box" style="padding:6px 10px; margin:4px 0; border-color:#b45309; background:#fffdf5;">
    <div style="font-family:'Noto Serif Devanagari',serif; font-size:0.95rem; font-weight:700; color:#78350f;">
      ॥ गुप्त आसन-उत्थापन मन्त्र ॥<br>
      ॐ शक्राय नमः । ॐ इन्द्राय नमः ॥
    </div>
    <div style="font-size:0.72rem; color:#475569; margin-top:2px;">
      आसन के नीचे 2 बूंद जल छोड़ें, अनामिका से स्पर्श कर मस्तक, दोनों नेत्रों व कंठ पर लगाएं।
    </div>
  </div>
  <div class="rule-card warning" style="padding:5px 8px; margin:4px 0; font-size:0.72rem;">
    <strong>⚠️ अग्नि सुरक्षा:</strong> पर्याप्त वेंटिलेशन (खुली खिड़कियां), अग्निरोधक आधार (पत्थर/टाइल), पास में जल व गीला कपड़ा रखें।
  </div>
</div>'''),
    (38, "उपसंहार • Colophon", "ग्रंथ समापन व शांति पाठ", '''<div style="text-align:center; padding:1.2rem 1rem;">
  <div style="font-size:1.8rem; margin-bottom:0.6rem;">☸ ॥ ॐ शान्तिः शान्तिः शान्तिः ॥ ☸</div>
  <h3 style="font-size:1.3rem; color:var(--accent-gold); font-family:'Noto Serif Devanagari',serif; font-weight:800; margin-bottom:0.6rem;">
    महाग्रंथ समापन एवं मंगल आशीर्वाद
  </h3>
  <p style="font-size:0.86rem; color:var(--text-main); line-height:1.7; max-width:480px; margin:0 auto 1rem auto;">
    यह महाग्रंथ समस्त निष्ठावान साधकों हेतु पूर्णतः प्रामाणिक ज्ञानकोश के रूप में तंत्र ज्ञान शोध संस्थान द्वारा समर्पित है। 41 दिनों की यह साधना साधक के जीवन में आध्यात्मिक रूपांतरण, विघ्न-निवारण एवं अभीष्ट सिद्धि प्रदान करने में समर्थ है।
  </p>
  <div style="border-top:1px solid #d97706; padding-top:0.8rem; max-width:420px; margin:0 auto; font-size:0.82rem; color:var(--text-muted); line-height:1.6;">
    <strong>प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</strong><br>
    तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)<br>
    आधिकारिक मंच: <a href="https://t.worldgyan.com" target="_blank" style="color:var(--accent-gold); font-weight:700;">t.worldgyan.com</a> • 2026 सर्वाधिकार सुरक्षित
  </div>
</div>''')
]

# Build TOC Modal items
toc_items_html = []
for p_num, ch_title, p_title, _ in page_specs:
    toc_items_html.append(f'''        <div class="toc-chapter-header">
          <span class="toc-chapter-pill">📌 {ch_title}</span>
        </div>
    <a href="#page-{p_num}" class="toc-item" data-goto="{p_num}">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.{p_num}</span>
        <span class="toc-item-title">{p_title}</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>''')

new_toc_body = "\n".join(toc_items_html)

# Replace TOC list in top_part and close toc-overlay properly
top_part = re.sub(
    r'<div class="toc-list">.*?</div>\s*</div>\s*</div>\s*<!-- Bookmark Drawer',
    f'<div class="toc-list">\n{new_toc_body}\n      </div>\n    </div>\n  </div>\n</div>\n\n  <!-- Bookmark Drawer',
    top_part,
    flags=re.DOTALL
)

# Clean up duplicate </main> in bot_part
bot_part = bot_part.replace('</main>\n    \n  </main>', '</main>')

# Build articles
articles_html = []
for num, ch, tit, body in page_specs:
    articles_html.append(f'''    <article class="book-page-data" id="page-data-{num}" data-page="{num}" data-chapter="{ch}" data-title="{tit}" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page {num}: {tit}">
      <meta itemprop="position" content="{num}">
      <meta itemprop="name" content="{tit}">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">{ch}</div>
          <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{tit}</h3>
        </div>
        {body}
      </div>
    </article>
''')

full_html = top_part + "".join(articles_html) + bot_part

with open(DST_READER, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"✅ Generated {DST_READER} with {len(page_specs)} pages ({os.path.getsize(DST_READER):,} bytes)")
