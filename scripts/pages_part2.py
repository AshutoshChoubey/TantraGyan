#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 2: Pages 29 to 54 of the 108-page Vedic Kundali Ganita Vichar Mahagranth.
Covers: Panchanga (5 Tattvas), Vimshottari Dasha Allocation & Hierarchy, Parashari Yogas & Rajyoga Matrix.
Zero raw Python code - pure mathematical formulas, Hindi algorithms, and worked examples for जातक 'क'.
"""

from page_common import (
    make_page, get_diamond_chart_svg, get_circular_zodiac_svg,
    get_ayanamsha_shift_svg, get_lagna_horizon_svg, get_panchanga_star_svg,
    get_vimshottari_tree_svg, get_ashtakavarga_wheel_svg, get_shadbala_pillars_svg,
    get_shodashavarga_tree_svg, get_jaimini_ladder_svg, get_bnn_trines_svg,
    get_sade_sati_wave_svg, get_ashtakoot_gauge_svg, get_pipeline_flow_svg,
    get_navamsha_grid_svg
)

def get_pages_part2():
    pages = []

    # Page 29: पंचांग का तात्विक रहस्य
    p29 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ पञ्चाङ्ग तत्त्व रहस्यम् ॥</strong><br>
  <em>"तिथेश्च श्रियमाप्नोति वारादायुष्यवर्धनम् । नक्षत्राद्धरते पापं योगाद्रोगनिवारणम् ॥<br>
  करणात्कार्यसिद्धिः स्यात् पञ्चाङ्गस्य फलं विदुः ॥"</em>
</div>

<p>पंचांग काल के ५ दिव्य अंगों का समुच्चय है, जो ब्रह्मांड के ५ मूल महाभूतों (पञ्चमहाभूत) का प्रतिनिधित्व करते हैं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">पंचांग अंग</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">महाभूत</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">खगोलीय कारक</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">मानव जीवन पर प्रभाव</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>१. तिथि</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">जल (Water)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">सूर्य-चंद्र अंतर (१२°)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">धन, समृद्धि, मानसिक तृप्ति।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>२. वार</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">अग्नि (Fire)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">सौर दिवस / वारेश</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">आयु, जीवन शक्ति, तेजस्विता।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>३. नक्षत्र</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">वायु (Air)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">चंद्र स्पष्ट (१३° २०')</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कर्म फल, पाप-नाश, प्रारब्ध।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>४. योग</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">आकाश (Ether)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">सूर्य + चंद्र योग (१३° २०')</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">आरोग्य, संबंध, चित्त शुद्धि।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>५. करण</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">पृथ्वी (Earth)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">अर्ध-तिथि (६°)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कर्म सिद्धि, भौतिक सफलता।</td></tr>
  </tbody>
</table>
'''
    p29 += get_panchanga_star_svg()

    pages.append(make_page(29, "पंचांग रहस्य • Panchanga", "पंचांग का तात्विक रहस्य एवं काल-पुरुष का शरीर", p29))

    # Page 30: तिथि साधन सूत्र
    p30 = '''
<p>सूर्य और चंद्रमा के कोणीय देशांतर के अंतर को १२° से विभाजित करने पर <strong>तिथि (Tithi)</strong> प्राप्त होती है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0; line-height:1.65;">
  <strong style="color:#38bdf8;">📐 तिथि साधन की सरल विधि:</strong><br>
  • <strong>कोणीय अंतर:</strong> चंद्र भोगांश में से सूर्य भोगांश घटाएं (ऋणात्मक होने पर ३६०° जोड़ें)।<br>
  • <strong>तिथि क्रमांक:</strong> कोणीय अंतर को १२° से भाग देकर १ जोड़ें।<br>
  • १ से १५: <strong>शुक्ल पक्ष</strong> (१ प्रतिपदा से १५ पूर्णिमा)<br>
  • १६ से ३०: <strong>कृष्ण पक्ष</strong> (१६ प्रतिपदा से ३० अमावस्या)
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.7rem; font-size:0.82rem; line-height:1.65;">
  <strong style="color:#166534;">जातक 'क' पर प्रत्यक्ष तिथि गणना:</strong><br>
  • चंद्र स्पष्ट = १०३° १०' (कर्क राशि), सूर्य स्पष्ट = १९०° २९' (तुला राशि)<br>
  • कोणीय अंतर = (१०३.१७° - १९०.४८°) + ३६०° = २७२.६९°<br>
  • तिथि भाग = २७२.६९° ÷ १२° = २२.७२ ➔ २२ पूर्ण + १ = <strong>२३वीं तिथि</strong><br>
  • <strong>परिणाम:</strong> कृष्ण पक्ष अष्टमी (२३वीं तिथि, काल भैरव एवं शिव उपासना के लिए श्रेष्ठ)।
</div>
'''
    pages.append(make_page(30, "पंचांग रहस्य • Panchanga", "तिथि साधन सूत्र: सूर्य-चंद्र अंतर एवं क्षय/वृद्धि", p30))

    # Page 31: वार साधन एवं होरा चक्र
    p31 = '''
<p>सप्ताह के सातों दिनों के अधिपति सूर्य सिद्धांत के अनुसार गति-क्रम से निर्धारित होते हैं:</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>अहर्गण (Ahargana) द्वारा वार साधन:</strong><br>
  कैलेंडर के कुल बीते दिनों (Ahargana) को ७ से भाग देने पर शेषफल वार बताता है:<br>
  वार संख्या = (जूलियन डे + १.५) को ७ से भाग देने पर प्राप्त शेषफल<br>
  (० = रविवार, १ = सोमवार, २ = मंगलवार, ३ = बुधवार, ४ = गुरुवार, <strong>५ = शुक्रवार</strong>, ६ = शनिवार)
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.82rem;">
  <strong>होरा चक्र (Hourly Planetary Lord):</strong><br>
  प्रत्येक दिन सूर्योदय से आरंभ होकर प्रत्येक घंटे का स्वामी मंदतम से तीव्रतम गति क्रम में होता है:<br>
  <strong>शनि ➔ गुरु ➔ मंगल ➔ सूर्य ➔ शुक्र ➔ बुध ➔ चंद्र</strong> (पुनरावृत्ति २४ घंटे)<br>
  जातक 'क' का जन्म शुक्रवार की रात्रि में (सूर्योदय से २१.८ घंटे बाद) हुआ। उस समय <strong>बुध की होरा</strong> चल रही थी (बौद्धिक एवं तार्किक बल)।
</div>
'''
    pages.append(make_page(31, "पंचांग रहस्य • Panchanga", "वार साधन एवं होरा चक्र कलन विधि", p31))

    # Page 32: नक्षत्र साधन
    p32 = '''
<p>चंद्रमा क्रांतिवृत्त में जिस तारा-पुंज के क्षेत्र में स्थित होता है, वह जातक का <strong>जन्म नक्षत्र (Janma Nakshatra)</strong> कहलाता है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 नक्षत्र एवं चरण साधन सूत्र:</strong><br>
  • संपूर्ण भचक्र = ३६०° = २१६०० कला<br>
  • १ नक्षत्र का मान = ३६०° / २७ = १३° २०' = ८०० कला<br>
  • १ चरण का मान = ८०० / ४ = २०० कला = ३° २०'<br>
  • नक्षत्र क्रमांक = चंद्र देशांतर (कला) ÷ ८०० + १<br>
  • चरण क्रमांक = (८०० से भाग देने पर शेष कला) ÷ २०० + १
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.82rem;">
  <strong style="color:#166534;">जातक 'क' पर प्रत्यक्ष नक्षत्र गणना:</strong><br>
  • चंद्र स्पष्ट = कर्क १६° ३७' १२'' = (३ × ३० + १६.६२०) × ६० = ६३९७.२ कला<br>
  • नक्षत्र संख्या =  ६३९७.२ / ८००  + १ = ७ + १ = ८ (पुष्य नक्षत्र)<br>
  • शेष कला = ६३९७.२ - ५६०० = ७९७.२ कला<br>
  • चरण संख्या =  ७९७.२ / २००  + १ = ३ + १ = ४था चरण<br>
  • <strong>परिणाम:</strong> पुष्य नक्षत्र (स्वामी: शनि देव), चतुर्थ चरण (नवांश: वृश्चिक, नवांशेश: मंगल)।
</div>
'''
    pages.append(make_page(32, "पंचांग रहस्य • Panchanga", "नक्षत्र साधन: चंद्र स्पष्ट एवं १३°२०' विभाजन", p32))

    # Page 33: २७ नित्य योग
    p33 = '''
<p>सूर्य और चंद्रमा के निरयण देशांतरों के योग को १३° २०' (८०० कला) से विभाजित करने पर <strong>नित्य योग (Nitya Yoga)</strong> प्राप्त होता है:</p>

<div style="background:#f1f5f9; border-left:4px solid #0284c7; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>नित्य योग साधन सूत्र:</strong><br>
  • योग भोगांश = (सूर्य भोगांश + चंद्र भोगांश) को ३६०° चक्र में समायोजित करें<br>
  • योग क्रमांक = योग भोगांश (कला) ÷ ८०० + १
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.82rem;">
  <strong style="color:#854d0e;">जातक 'क' पर प्रत्यक्ष योग गणना:</strong><br>
  • सूर्य स्पष्ट = १९०° २५' ३६'', चंद्र स्पष्ट = १०६° ३७' १२''<br>
  • योग देशांतर = १९०.४२६७° + १०६.६२००° = २९७.०४६७° = १७८२२.८ कला<br>
  • योग संख्या =  १७८२२.८ / ८००  + १ = २२ + १ = २३<br>
  • <strong>परिणाम:</strong> २३वां योग = <strong>शुभ योग (Shubha Yoga)</strong>।<br>
  • <em>फल:</em> जातक धार्मिक, विद्यावान, परोपकारी एवं समाज में सम्मानित होता है।
</div>
'''
    pages.append(make_page(33, "पंचांग रहस्य • Panchanga", "२७ नित्य योग साधन सूत्र: सूर्य + चंद्र देशांतर योग", p33))

    # Page 34: ११ करण साधन
    p34 = '''
<p>एक तिथि के आधे भाग (६° सूर्य-चंद्र अंतर) को <strong>करण (Karana)</strong> कहते हैं। कुल ११ करण होते हैं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">प्रकार</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">करण नाम</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">प्रकृति एवं प्रभाव</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>चर करण (७)</strong><br>(८ बार आवृत्ति)</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">१. बव, २. बालव, ३. कौलव, ४. तैतिल, ५. गर, ६. वणिज, ७. विष्टि (भद्रा)</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">सामान्य शुभ कार्य। विष्टि (भद्रा) क्रूर एवं त्याज्य है।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>स्थिर करण (४)</strong><br>(माह में १ बार)</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">८. शकुनि, ९. चतुष्पाद, १०. नाग, ११. किस्तुघ्न</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">कृष्ण चतुर्दशी उत्तरार्ध से शुक्ल प्रतिपदा पूर्वार्ध तक।</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' पर प्रत्यक्ष करण गणना:</strong><br>
  • चंद्र-सूर्य कोणीय अंतर = २७२.७° ➔ २७२.७° ÷ ६° = ४५.४५ ➔ ४५ + १ = ४६वां भाग (कौलव करण)।<br>
  • ४६वां भाग = कौलव करण (स्वामी: मित्र देव)<br>
  • <em>फल:</em> जातक सौम्य, संवेदनशील, सर्वप्रिय एवं तंत्र साधना में स्थिर चित्त होता है।
</div>
'''
    pages.append(make_page(34, "पंचांग रहस्य • Panchanga", "११ करण साधन: चर एवं स्थिर करणों का गणित", p34))

    # Page 35: अशुभ मुहूर्त गणित
    p35 = '''
<p>दिन के आठवें भाग के अनुसार अशुभ काल-खंडों का निर्धारण सूर्योदय व दिनमान से होता है:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">वार (Day)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">राहुकाल (दिन का भाग)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">यमगण्ड (दिन का भाग)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">गुलिक काल</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">रविवार</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">८वां भाग (१६:३० - १८:००)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५वां भाग (१२:०० - १३:३०)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">७वां भाग</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">सोमवार</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">२रा भाग (०७:३० - ०९:००)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४था भाग (१०:३० - १२:००)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">६ठा भाग</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">मंगलवार</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">७वां भाग (१५:०० - १६:३०)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३रा भाग (०९:०० - १०:३०)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५वां भाग</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">बुधवार</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५वां भाग (१२:०० - १३:३०)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">२रा भाग (०७:३० - ०९:००)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४था भाग</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">गुरुवार</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">६ठा भाग (१३:३० - १५:००)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१ला भाग (०६:०० - ०७:३०)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३रा भाग</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">शुक्रवार</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४था भाग (१०:३० - १२:००)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">७वां भाग (१५:०० - १६:३०)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">२रा भाग</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">शनिवार</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३रा भाग (०९:०० - १०:३०)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">६ठा भाग (१३:३० - १५:००)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१ला भाग</td></tr>
  </tbody>
</table>

<div style="background:#fefce8; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>नोट:</strong> दिए गए समय १२ घंटे के मानक दिनमान पर आधारित हैं। स्थानीय सूर्योदय अनुसार इनमें सूक्ष्म अंतर आता है।
</div>
'''
    pages.append(make_page(35, "पंचांग रहस्य • Panchanga", "राहुकाल, यमगण्ड एवं अशुभ मुहूर्त साधन", p35))

    # Page 36: जातक 'क' संपूर्ण पंचांग तालिका
    p36 = '''
<p>जातक 'क' के जन्मकालीन संपूर्ण पंचांग तत्वों की मास्टर सारणी:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.8rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.4rem; border:1px solid #334155; text-align:left;">पंचांग अंग</th>
      <th style="padding:0.4rem; border:1px solid #334155; text-align:left;">प्राप्त मान</th>
      <th style="padding:0.4rem; border:1px solid #334155; text-align:left;">स्वामी ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #334155; text-align:left;">ज्योतिषीय फलित निष्कर्ष</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>१. तिथि</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कृष्ण पक्ष नवमी</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">सूर्य</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">उग्र-प्रकृति, साहसी, दृढ़ संकल्पी।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>२. वार</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">शुक्रवार (रात्रि)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">शुक्र</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">सौंदर्य, कला, वैभव एवं आकर्षण।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>३. नक्षत्र</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">पुष्य (४था चरण)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">शनि</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">सर्वश्रेष्ठ नक्षत्र; पोषण, धर्म, साधना।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>४. योग</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">शुभ योग</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">सूर्य</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कल्याणकारी, धार्मिक कार्यों में रुचि।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>५. करण</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">गर करण</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">भूमि / पृथ्वी</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कर्मठ, व्यवहारकुशल, स्थिरता।</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.6rem; font-size:0.8rem;">
  <strong>पंचांग संतुलन निष्कर्ष:</strong> जातक के पांचों तत्व अत्यंत संतुलित हैं। पुष्य नक्षत्र एवं शुभ योग का सम्मिलन जातक को उच्च आध्यात्मिक एवं बौद्धिक क्षमता प्रदान करता है।
</div>
'''
    pages.append(make_page(36, "केस स्टडी • Case Study", "जातक 'क' की संपूर्ण पंचांग तालिका एवं फल", p36))

    # Pages 37 to 44: विंशोत्तरी दशा
    p37 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ विंशोत्तरी दशा रहस्यम् बृहत्पाराशरे ॥</strong><br>
  <em>"दशा विंशोत्तरी ज्ञेया कलौ सर्वाधिका शुभा । मानवानां परमायुः शतविंशतिवत्सरम् ॥"</em>
</div>

<p>कलियुग में मनुष्य की पूर्ण आयु <strong>१२० वर्ष</strong> मानी गई है। महर्षि पराशर ने २७ नक्षत्रों को ९ ग्रहों के बीच ३ बार पुनरावृत्त करके १२० वर्षों का काल-चक्र स्थापित किया है।</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>९ ग्रहों के महादशा वर्ष:</strong><br>
  • केतु: ७ वर्ष • शुक्र: २० वर्ष • सूर्य: ६ वर्ष • चंद्रमा: १० वर्ष<br>
  • मंगल: ७ वर्ष • राहु: १८ वर्ष • गुरु: १६ वर्ष • शनि: १९ वर्ष • बुध: १७ वर्ष<br>
  कुल योग = ७ + २० + ६ + १० + ७ + १८ + १६ + १९ + १७ = १२० वर्ष
</div>
'''
    p37 += get_vimshottari_tree_svg()

    pages.append(make_page(37, "दशा तंत्र • Vimshottari Dasha", "विंशोत्तरी दशा का मूल दर्शन एवं १२० वर्षीय चक्र", p37))

    # Page 38: दशा वर्ष आवंटन एवं नक्षत्र त्रिकोण
    p38 = '''
<p>२७ नक्षत्रों को ९ ग्रहों में ३-३ नक्षत्रों के त्रिकोण (Trines) के रूप में बांटा गया है:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">दशा स्वामी</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">वर्ष</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">प्रथम चक्र नक्षत्र</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">द्वितीय चक्र नक्षत्र</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">तृतीय चक्र नक्षत्र</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">१. केतु</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">७</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१. अश्विनी</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१०. मघा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१९. मूल</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">२. शुक्र</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">२०</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२. भरणी</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">११. पूर्वाफाल्गुनी</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२०. पूर्वाषाढ़ा</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">३. सूर्य</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">६</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">३. कृत्तिका</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१२. उत्तराफाल्गुनी</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२१. उत्तराषाढ़ा</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">४. चंद्र</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१०</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">४. रोहिणी</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१३. हस्त</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२२. श्रवण</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">५. मंगल</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">७</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">५. मृगशिरा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१४. चित्रा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२३. धनिष्ठा</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">६. राहु</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१८</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">६. आर्द्रा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१५. स्वाति</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२४. शतभिषा</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">७. गुरु</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१६</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">७. पुनर्वसु</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१६. विशाखा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२५. पूर्वाभाद्रपद</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">८. शनि</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१९</td><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>८. पुष्य</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१७. अनुराधा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२६. उत्तराभाद्रपद</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">९. बुध</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१७</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">९. आश्लेषा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१८. ज्येष्ठा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२७. रेवती</td></tr>
  </tbody>
</table>
'''
    pages.append(make_page(38, "दशा तंत्र • Vimshottari Dasha", "९ ग्रहों का दशा वर्ष आवंटन एवं नक्षत्र त्रिकोण", p38))

    # Page 39: भुक्त-भोग्य साधन
    p39 = '''
<p>जन्म समय चंद्रमा नक्षत्र में जितना चल चुका होता है, उसे <strong>भुक्त (Elapsed)</strong> तथा जितना चलना शेष होता है, उसे <strong>भोग्य (Balance)</strong> कहते हैं:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 भुक्त एवं भोग्य दशा का बीजगणितीय सूत्र:</strong><br>
  १. नक्षत्र का कुल मान = ८०० कला = १३° २०'<br>
  २. भुक्त कला = चंद्र देशांतर को ८०० से भाग देने पर शेष कला<br>
  ३. भोग्य कला = ८०० - भुक्त कला<br>
  ४. दशा भोग्य शेष (वर्ष) = (भोग्य कला ÷ ८०० कला) × दशा स्वामी के कुल वर्ष
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong>तात्विक अर्थ:</strong> जातक अपने पूर्व जन्म के जिस कर्म-भाग को भोगकर आता है, वह भुक्त है; और इस जन्म में जन्म-क्षण से जो कर्म फलना प्रारंभ होता है, वह भोग्य दशा है।
</div>
'''
    pages.append(make_page(39, "दशा तंत्र • Vimshottari Dasha", "जन्मकालीन नक्षत्र भुक्त-भोग्य साधन सूत्र", p39))

    # Page 40: जातक 'क' दशा शेष गणना
    p40 = '''
<p>जातक 'क' की जन्मकालीन शनि महादशा के भोग्य शेष की चरणबद्ध गणितीय प्रक्रिया:</p>

<div style="background:#f1f5f9; border-left:4px solid #b45309; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>चरण १: चंद्र देशांतर एवं पुष्य नक्षत्र का आरंभ:</strong><br>
  • पुष्य नक्षत्र का विस्तार: कर्क ३° २०' (९३° २०') से कर्क १६° ४०' (१०६° ४०')<br>
  • चंद्र स्पष्ट = कर्क १६° ३७' १२'' = १०६° ३७' १२''<br>
  <strong>चरण २: भुक्त एवं भोग्य कला निकालना:</strong><br>
  • पुष्य का आरंभ = ९३° २०' = ५६०० कला<br>
  • चंद्र स्थिति = १०६° ३७' १२'' = ६३९७.२ कला<br>
  • भुक्त कला = ६३९७.२ - ५६०० = ७९७.२ कला<br>
  • भोग्य कला = ८०० - ७९७.२ = २.८ कला<br>
  <strong>चरण ३: शनि दशा भोग्य अनुपात:</strong><br>
  भोग्य वर्ष = (२.८ ÷ ८००) × १९ वर्ष = ०.०६६५ वर्ष = २४ दिन
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong style="color:#854d0e;">जातक 'क' जन्मकालीन दशा परिणाम:</strong><br>
  जन्म समय शनि की महादशा मात्र <strong>२४ दिन</strong> शेष थी। २१ नवंबर १९९४ से जातक पर <strong>बुध की १७-वर्षीय महादशा</strong> प्रारंभ हुई।
</div>
'''
    pages.append(make_page(40, "केस स्टडी • Case Study", "जातक 'क' की जन्म समय दशा भोग्य शेष गणना", p40))

    # Page 41: अंतर्दशा उप-विभाजन
    p41 = '''
<p>किसी महादशा के भीतर ९ ग्रहों की <strong>अंतर्दशा (Antardasha / भुक्ति)</strong> निकालने का आनुपातिक नियम:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 अंतर्दशा साधन का सार्वभौमिक सूत्र:</strong><br>
  अंतर्दशा अवधि (वर्ष) = (महादशा वर्ष × अंतर्दशा नाथ के वर्ष) ÷ १२०<br>
  • <strong>माह निकालने का नियम:</strong> (महादशा वर्ष × अंतर्दशा वर्ष) में १२ का भाग दें, जो भागफल आए वह माह है।<br>
  • <strong>दिन निकालने का नियम:</strong> शेषफल को ३ से गुणा करें, वह दिन होगा।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">उदाहरण: बुध महादशा (१७ वर्ष) में शुक्र अंतर्दशा (२० वर्ष):</strong><br>
  • गुणनफल = १७ × २० = ३४०<br>
  • ३४० में १२ का भाग: भागफल = २८ माह, शेषफल = ४<br>
  • दिन = ४ × ३ = १२ दिन<br>
  • <strong>अवधि:</strong> २८ माह १२ दिन = २ वर्ष  ४ माह  १२ दिन।
</div>
'''
    pages.append(make_page(41, "दशा तंत्र • Vimshottari Dasha", "अंतर्दशा (भुक्ति) उप-विभाजन का आनुपातिक सूत्र", p41))

    # Page 42: प्रत्यंतर्दशा एवं सूक्ष्म दशा
    p42 = '''
<p>घटना के सटीक दिन व समय तक पहुँचने के लिए अंतर्दशा का और सूक्ष्म विभाजन किया जाता है:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">दशा स्तर</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">गणितीय सूत्र</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">काल विस्तार</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">संकेत</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>१. प्रत्यंतर्दशा (PD)</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">(MD × AD × PD) ÷ (१२० × १२०) वर्ष</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">सप्ताह से माह</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">घटना का माह सुनिश्चित करना।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>२. सूक्ष्म दशा (SD)</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">(PD अवधि × SD वर्ष) ÷ १२०</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">दिन से सप्ताह</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">सटीक सप्ताह एवं दिन।</td>
    </tr>
    <tr>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>३. प्राण दशा (PrD)</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">(SD अवधि × PrD वर्ष) ÷ १२०</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">घंटे से दिन</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">घंटे एवं सूक्ष्म मुहूर्त।</td>
    </tr>
  </tbody>
</table>

<div style="background:#fefce8; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>ऋषि नियम:</strong> जब महादशा, अंतर्दशा और प्रत्यंतर्दशा तीनों एक ही भाव या ग्रह से संबंधित हों, तब वह घटना अवश्य घटित होती है।
</div>
'''
    pages.append(make_page(42, "दशा तंत्र • Vimshottari Dasha", "प्रत्यंतर्दशा, सूक्ष्म एवं प्राण दशा कलन विधि", p42))

    # Page 43: दशा फलित के ५ नियम
    p43 = '''
<p>दशा स्वामी के फलित निर्णय के ५ अचूक शास्त्रीय नियम:</p>

<ol style="font-size:0.82rem; line-height:1.6; padding-left:1.2rem;">
  <li><strong>स्वामित्व नियम (Lordship):</strong> ग्रह जिन भावों का स्वामी है, उन भावों के फल अपनी दशा में देगा। केंद्र व त्रिकोण के स्वामियों की दशा शुभ, तथा ६, ८, १२ के स्वामियों की दशा संघर्षमय होती है।</li>
  <li><strong>स्थिति नियम (Placement):</strong> ग्रह जिस भाव में बैठा है, उस भाव के फल को सक्रिय करता है।</li>
  <li><strong>दृष्टि एवं युति नियम (Aspects):</strong> ग्रह पर जिन शुभ या पापी ग्रहों की दृष्टि होती है, वह उनके स्वभाव को आत्मसात कर लेता है।</li>
  <li><strong>नक्षत्र स्वामी नियम (Nakshatra Lord):</strong> ग्रह अपने नक्षत्र स्वामी के भावों का फल पहले देता है।</li>
  <li><strong>गोचर सामंजस्य (Transit Concurrence):</strong> दशा जब किसी घटना का संकेत दे, तब गोचर (Transit) उस घटना का ताला खोलता है।</li>
</ol>
'''
    pages.append(make_page(43, "दशा तंत्र • Vimshottari Dasha", "दशा फलित निर्णय के ५ अचूक शास्त्रीय नियम", p43))

    # Page 44: जातक 'क' संपूर्ण दशा वृक्ष
    p44 = '''
<p>जातक 'क' के जीवन का संपूर्ण महादशा क्रम एवं काल-खंड तालिका:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.35rem; border:1px solid #334155;">महादशा</th>
      <th style="padding:0.35rem; border:1px solid #334155;">अवधि (वर्ष)</th>
      <th style="padding:0.35rem; border:1px solid #334155;">आरंभ तिथि</th>
      <th style="padding:0.35rem; border:1px solid #334155;">समाप्ति तिथि</th>
      <th style="padding:0.35rem; border:1px solid #334155;">प्रमुख जीवन प्रभाव</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">शनि (शेष)</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">०.०७</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२८-१०-१९९४</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१-११-१९९४</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शैशव काल।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>बुध</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">१७.००</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१-११-१९९४</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१-११-२०११</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">लग्नेश दशा; तीव्र बुद्धि, उच्च शिक्षा।</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>केतु</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">७.००</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१-११-२०११</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१-११-२०१८</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">अष्टम केतु; शोध, आंतरिक साधना, वैराग्य।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>शुक्र</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">२०.००</td><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>२१-११-२०१८</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>२१-११-२०३८</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>भाग्येश दशा; महान रचना, वैभव, प्रतिष्ठा।</strong></td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">सूर्य</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">६.००</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१-११-२०३८</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१-११-२०४४</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">द्वादशेश दशा; आध्यात्मिक शिखर, त्याग।</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.5rem; font-size:0.8rem;">
  <strong>वर्तमान स्थिति:</strong> जातक 'क' इस समय <strong>शुक्र की २०-वर्षीय महादशा</strong> में चल रहे हैं (द्वितीय भाव में स्वक्षेत्री भाग्येश शुक्र), जो जीवन का स्वर्णिम काल है।
</div>
'''
    pages.append(make_page(44, "केस स्टडी • Case Study", "जातक 'क' का विंशोत्तरी दशा चक्र: जन्म से वर्तमान", p44))

    # Pages 45 to 54: पराशरी योग
    p45 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ राजयोग लक्षणम् बृहत्पाराशरे ॥</strong><br>
  <em>"केन्द्राधिपाश्च त्रिकोणाधिपाश्च परस्परं सम्बन्धेन राजयोगा भवन्ति..."</em>
</div>

<p><strong>योग का मूल सिद्धांत:</strong> जब दो या दो से अधिक ग्रहों के बीच युति (Conjunction), परस्पर दृष्टि (Mutual Aspect), अथवा राशि परिवर्तन (Mutual Reception) होता है, तो ग्रहों का यह विशिष्ट संयोग <strong>योग (Yoga)</strong> कहलाता है।</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>केंद्र एवं त्रिकोण का रहस्य:</strong><br>
  • <strong>केंद्र भाव (१, ४, ७, १०):</strong> भगवान विष्णु के प्रतीक (कर्म, पुरुषार्थ, शक्ति)।<br>
  • <strong>त्रिकोण भाव (१, ५, ९):</strong> भगवती महालक्ष्मी के प्रतीक (भाग्य, पूर्वपुण्य, कृपा)।<br>
  • जब केंद्र और त्रिकोण के स्वामियों का संबंध बनता है, तो <strong>महालक्ष्मी-नारायण योग (राजयोग)</strong> उत्पन्न होता है।
</div>
'''
    p45 += get_diamond_chart_svg()

    pages.append(make_page(45, "पराशरी योग • Parashari Yogas", "योग की परिभाषा एवं पराशरी केंद्र-त्रिकोण सिद्धांत", p45))

    # Page 46: धर्माधिपति-कर्माधिपति योग
    p46 = '''
<p>वैदिक ज्योतिष का सर्वोच्च राजयोग <strong>धर्माधिपति-कर्माधिपति योग (९वें व १०वें भाव का संबंध)</strong> माना जाता है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 धर्माधिपति-कर्माधिपति योग के ४ संबंध प्रकार:</strong><br>
  १. <strong>राशि परिवर्तन:</strong> नवमेश दशम में तथा दशमेश नवम में स्थित हो।<br>
  २. <strong>युति:</strong> नवमेश और दशमेश दोनों किसी शुभ भाव में एक साथ बैठे हों।<br>
  ३. <strong>दृष्टि संबंध:</strong> नवमेश और दशमेश एक दूसरे को पूर्ण दृष्टि से देख रहे हों।<br>
  ४. <strong>एकतरफा दृष्टि:</strong> एक ग्रह दूसरे के घर में हो और दूसरा उसे देख रहा हो।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' कुण्डली में प्रत्यक्ष परीक्षण:</strong><br>
  • नवमेश (धर्मेश): <strong>शुक्र</strong> • दशमेश (कर्मेश): <strong>बुध</strong><br>
  • जातक की कुण्डली में बुध और शुक्र दोनों द्वितीय भाव (तुला) में एक साथ युति कर रहे हैं।<br>
  • <strong>परिणाम:</strong> द्वितीय भाव में विशुद्ध <strong>धर्माधिपति-कर्माधिपति राजयोग</strong> विद्यमान है।
</div>
'''
    pages.append(make_page(46, "पराशरी योग • Parashari Yogas", "धर्माधिपति-कर्माधिपति (९वें व १०वें) राजयोग", p46))

    # Page 47: पंच महापुरुष योग १
    p47 = '''
<p>जब मंगल, बुध अथवा गुरु स्वक्षेत्री या उच्च होकर केंद्र (१, ४, ७, १०) में स्थित हों, तो पंच महापुरुष योग बनते हैं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">योग नाम</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">कारक ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">शर्तें (केंद्र में स्थिति)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">फलित प्रभाव</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>१. रुचक योग</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">मंगल</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">मेष, वृश्चिक (स्व) या मकर (उच्च)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">सेनापति, अदम्य साहस, भूमि लाभ।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>२. भद्र योग</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">बुध</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">मिथुन (स्व) या कन्या (उच्च)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">प्रकांड विद्वान, तार्किक, लेखक, दीर्घायु।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>३. हंस योग</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">गुरु</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">धनु, मीन (स्व) या कर्क (उच्च)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">न्यायाधीश, संत, आध्यात्मिक गुरु।</td></tr>
  </tbody>
</table>

<div style="background:#fefce8; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>नवांश में हंस योग:</strong> जातक 'क' के नवांश (D9) में गुरु उच्च राशि (कर्क) में होकर केंद्र में स्थित हैं, जिससे सूक्ष्म <strong>हंस महापुरुष योग</strong> सिद्ध होता है।
</div>
'''
    pages.append(make_page(47, "पराशरी योग • Parashari Yogas", "पंच महापुरुष योग १: रुचक, भद्र एवं हंस योग", p47))

    # Page 48: पंच महापुरुष योग २
    p48 = '''
<p>शुक्र एवं शनि द्वारा निर्मित पंच महापुरुष योग:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">योग नाम</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">कारक ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">शर्तें (केंद्र में स्थिति)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">फलित प्रभाव</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>४. मालव्य योग</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">शुक्र</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">वृषभ, तुला (स्व) या मीन (उच्च)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">अतुलनीय सौंदर्य, वाहन सुख, कला में ख्याति।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>५. शश योग</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">शनि</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">मकर, कुंभ (स्व) या तुला (उच्च)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">प्रजापालक, जननायक, कूटनीतिज्ञ, दीर्घायु।</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong>चंद्र लग्न से शश योग (जातक 'क'):</strong><br>
  जातक 'क' की चंद्र राशि <strong>कर्क</strong> है। कर्क से अष्टम में शनि कुंभ राशि (स्वक्षेत्री) में हैं। परंतु लग्न से षष्ठ भाव में शनि होने के कारण यह <strong>हर्ष विपरीत राजयोग</strong> का निर्माण करते हैं।
</div>
'''
    pages.append(make_page(48, "पराशरी योग • Parashari Yogas", "पंच महापुरुष योग २: मालव्य एवं शश योग", p48))

    # Page 49: गजकेसरी योग
    p49 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ गजकेसरी योग लक्षणम् ॥</strong><br>
  <em>"केन्द्रे देवगुरौ लग्नाच्चन्द्राद्वा चन्द्रसद्मनि । नीचारिमौढ्यहीने च गजकेसरी उच्यते ॥"</em>
</div>

<p><strong>शास्त्रीय परिभाषा:</strong> जब चंद्रमा से केंद्र (१, ४, ७, १०) में देवगुरु बृहस्पति स्थित हों, और दोनों पाप ग्रहों से पीड़ित अथवा अस्त न हों, तो <strong>गजकेसरी योग</strong> बनता है।</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.6rem; font-size:0.8rem; margin:0.6rem 0;">
  <strong>गजकेसरी योग के फल:</strong><br>
  जातक हाथी के समान तेजस्वी, सिंह के समान साहसी, राजमान्य, दीर्घायु, स्थिर बुद्धि एवं शत्रुओं पर सदा विजय प्राप्त करने वाला होता है।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' कुण्डली में गजकेसरी परीक्षण:</strong><br>
  • चंद्रमा: कर्क राशि (एकादश भाव) में स्वक्षेत्री हैं।<br>
  • गुरु: वृश्चिक राशि (तृतीय भाव) में चंद्रमा से पंचम (त्रिकोण) में हैं।<br>
  • परंतु <strong>नवांश कुण्डली (D9)</strong> में चंद्रमा कर्क में और गुरु कर्क में (उच्च) <strong>एक साथ युति</strong> कर रहे हैं, जिससे नवांश में साक्षात गजकेसरी योग बनता है।
</div>
'''
    pages.append(make_page(49, "पराशरी योग • Parashari Yogas", "गजकेसरी योग: शास्त्रीय परिभाषा, बल एवं भेद", p49))

    # Page 50: धन योग एवं लक्ष्मी योग
    p50 = '''
<p>वैदिक ज्योतिष में आर्थिक संपन्नता के लिए २ (धन), ५ (बुद्धि/लक्ष्मी), ९ (भाग्य) एवं ११ (लाभ) भावों का संबंध देखा जाता है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 धन योग के प्रमुख सूत्र:</strong><br>
  १. द्वितीयेश और एकादशेश की युति अथवा परस्पर दृष्टि।<br>
  २. पंचमेश और नवमेश का संबंध (लक्ष्मी योग)।<br>
  ३. लग्नेश का द्वितीय, नवम या एकादश भाव में बैठना।<br>
  ४. गुरु का चंद्रमा से संबंध अथवा एकादश भाव पर दृष्टि।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' कुण्डली में धन योग:</strong><br>
  • लग्नेश बुध + भाग्येश शुक्र की युति <strong>द्वितीय (धन) भाव</strong> में।<br>
  • लाभेश चंद्रमा एकादश भाव में स्वक्षेत्री।<br>
  • गुरु की नवम दृष्टि एकादश भाव स्थित चंद्रमा पर (अत्यंत दुर्लभ धन योग)।
</div>
'''
    pages.append(make_page(50, "पराशरी योग • Parashari Yogas", "धन योग एवं लक्ष्मी योग: २, ५, ९, ११ भाव संयोजन", p50))

    # Page 51: विपरीत राजयोग
    p51 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ विपरीत राजयोग लक्षणम् ॥</strong><br>
  <em>"रन्ध्रेशो व्ययगो रिपुगो वा व्ययेशो रिपुगो रन्ध्रगो वा ।<br>
  रिपुनाथो रन्ध्रगतो व्ययगो वा विपरीतराजयोगः ॥"</em>
</div>

<p>त्रिक भावों (६, ८, १२) के स्वामी जब आपस में ही ६, ८, १२ में बैठें और किसी शुभ भाव के स्वामी से युति न करें, तो <strong>विपरीत राजयोग</strong> बनता है:</p>

<ol style="font-size:0.8rem; line-height:1.6; padding-left:1.2rem;">
  <li><strong>हर्ष योग:</strong> षष्ठेश ६, ८ या १२वें भाव में हो ➔ शत्रुओं पर विजय, अजेयता, स्वास्थ्य।</li>
  <li><strong>सरल योग:</strong> अष्टमेश ६, ८ या १२वें भाव में हो ➔ दीर्घायु, गुप्त ज्ञान, संकट में अकूत लाभ।</li>
  <li><strong>विमल योग:</strong> द्वादशेश ६, ८ या १२वें भाव में हो ➔ स्वतंत्र विचार, परोपकारी, मितव्ययी।</li>
</ol>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.5rem; font-size:0.8rem;">
  <strong>जातक 'क' कुण्डली:</strong> षष्ठेश शनि षष्ठ भाव (कुंभ) में स्वक्षेत्री हैं, जिससे <strong>हर्ष विपरीत राजयोग</strong> बनता है। जातक समस्त गुप्त शत्रुओं व रोगों को परास्त करता है।
</div>
'''
    pages.append(make_page(51, "पराशरी योग • Parashari Yogas", "विपरीत राजयोग: हर्ष, सरल एवं विमल योग", p51))

    # Page 52: नीचभंग राजयोग के ५ सूत्र
    p52 = '''
<p>नीच ग्रह का दोष समाप्त होकर जब वह राजा के समान फल देने लगे, उसे <strong>नीचभंग राजयोग</strong> कहते हैं:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 नीचभंग राजयोग के ५ अचूक शास्त्रीय सूत्र:</strong><br>
  १. नीच राशि का स्वामी (Dispositor) लग्न या चंद्रमा से केंद्र (१, ४, ७, १०) में हो।<br>
  २. नीच ग्रह जिस राशि में उच्च होता है, उस राशि का स्वामी केंद्र में हो।<br>
  ३. नीच ग्रह पर उसकी उच्च राशि के स्वामी की दृष्टि हो।<br>
  ४. नीच ग्रह नवांश कुण्डली (D9) में अपनी उच्च राशि अथवा स्वक्षेत्री हो।<br>
  ५. नीच ग्रह के साथ कोई उच्च का ग्रह बैठा हो।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' कुण्डली में सूर्य का नीचभंग:</strong><br>
  • सूर्य तुला राशि (नीच) में स्थित है।<br>
  • तुला राशि का स्वामी <strong>शुक्र</strong> उसी भाव में सूर्य के साथ स्वक्षेत्री बैठा है (सूत्र १ व २)।<br>
  • अतः सूर्य का नीचत्व पूर्णतः भंग होकर <strong>नीचभंग राजयोग</strong> बन गया है।
</div>
'''
    pages.append(make_page(52, "पराशरी योग • Parashari Yogas", "नीचभंग राजयोग के ५ अचूक शास्त्रीय सूत्र", p52))

    # Page 53: दरिद्र एवं केमद्रुम योग परिहार
    p53 = '''
<p>अशुभ योगों के शास्त्रीय परिहार (Cancellations) का गणित:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">दोष योग</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">निर्माण शर्त</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">शास्त्रीय परिहार (Bhanga) नियम</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>१. केमद्रुम योग</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">चंद्रमा के द्वितीय एवं द्वादश दोनों में कोई ग्रह न हो।</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">यदि लग्न से केंद्र में कोई ग्रह हो, अथवा चंद्र पर गुरु की दृष्टि हो, तो केमद्रुम <strong>शत-प्रतिशत भंग</strong> हो जाता है।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>२. कालसर्प योग</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">समस्त ग्रह राहु और केतु के मध्य स्थित हों।</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">यदि कोई एक भी ग्रह (जैसे गुरु या लग्न) परिधि से बाहर हो, अथवा गुरु केंद्र में हो, तो कालसर्प भंग होता है।</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0fdf4; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>जातक 'क' कुण्डली:</strong> चंद्र के दोनों ओर ग्रह हैं (सिंह में मंगल, तुला में शुक्र-बुध), अतः केमद्रुम योग नहीं है। गुरु तृतीय में होकर कालसर्प परिधि को तोड़ते हैं।
</div>
'''
    pages.append(make_page(53, "पराशरी योग • Parashari Yogas", "दरिद्र, केमद्रुम एवं कालसर्प योग के परिहार", p53))

    # Page 54: जातक 'क' समग्र योग संसूचन
    p54 = '''
<p>जातक 'क' की कुण्डली में गणितीय रूप से संसूचित समस्त योगों का मास्टर स्कोरकार्ड:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.35rem; border:1px solid #334155;">योग का नाम</th>
      <th style="padding:0.35rem; border:1px solid #334155;">कारक ग्रह एवं भाव</th>
      <th style="padding:0.35rem; border:1px solid #334155;">श्रेणी</th>
      <th style="padding:0.35rem; border:1px solid #334155;">बल / स्थिति</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>१. धर्माधिपति-कर्माधिपति योग</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">बुध + शुक्र (द्वितीय भाव)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">महा-राजयोग</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पूर्ण बली (१००%)</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>२. नीचभंग राजयोग</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सूर्य + शुक्र (द्वितीय भाव)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">राजयोग</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सिद्ध (शुक्र स्वक्षेत्री)</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>३. हर्ष विपरीत राजयोग</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शनि (षष्ठ भाव में स्वक्षेत्री)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सुरक्षा योग</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">अत्यंत बली (वक्री)</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>४. बुधादित्य योग</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सूर्य + बुध (द्वितीय भाव)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मेधा योग</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सक्रिय (वाक-पटुता)</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>५. मालव्य सदृश योग</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शुक्र स्वक्षेत्री (द्वितीय भाव)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">धन/वैभव</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">अत्यंत शुभ</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.5rem; font-size:0.8rem;">
  <strong>खंड २ संपूर्ण:</strong> पंचांग, दशा एवं योगों का गणित पूर्ण हुआ। अब हम खंड ३ में १६ वर्ग कुण्डलियों एवं अष्टकवर्ग का सूक्ष्म गणित सिद्ध करेंगे।
</div>
'''
    pages.append(make_page(54, "केस स्टडी • Case Study", "जातक 'क' कुण्डली में विद्यमान योगों का मास्टर स्कोरकार्ड", p54))

    return pages

print("Part 2 defined")
