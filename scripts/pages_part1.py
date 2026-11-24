#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 1: Pages 1 to 28 of the 108-page Vedic Kundali Ganita Vichar Mahagranth.
Covers: Introduction, Celestial Mechanics, Julian Day, Ayanamsha, Lagna, Planetary Dynamics.
Zero raw Python code - pure mathematical formulas, Hindi algorithms, and worked examples for जातक 'क'.
"""

from page_common import make_page, get_diamond_chart_svg, get_circular_zodiac_svg

def get_pages_part1():
    pages = []

    # Page 1: मुखपृष्ठ • Cover
    p1 = '''
<div style="text-align:center; padding:1.5rem 0.5rem;">
  <div style="font-size:0.9rem; font-weight:700; color:#b45309; letter-spacing:0.1em; margin-bottom:0.5rem;">॥ श्री गणेशाय नमः • ॐ नमः शिवाय ॥</div>
  <div style="font-size:1.6rem; font-weight:900; color:#0f172a; line-height:1.3; margin-bottom:0.5rem;">वैदिक कुण्डली विचार एवं गणित महाग्रंथ</div>
  <div style="font-size:1rem; font-weight:700; color:#059669; margin-bottom:1rem;">खगोलीय सूत्र, १६ वर्ग चक्र, दशा रहस्य एवं फलित संयोजन</div>
  <div style="font-size:0.85rem; color:#64748b; font-style:italic; margin-bottom:1.5rem;">The Cosmic Algorithm: Vedic Horoscope Mathematics & Destiny Decoded</div>
  
  <div style="background:linear-gradient(135deg, #090d16, #1e293b); color:#f8fafc; border-radius:10px; padding:1.2rem; margin:1rem 0; border:1px solid #d4af37; text-align:left;">
    <div style="color:#d4af37; font-weight:700; font-size:0.9rem; margin-bottom:0.5rem; text-align:center;">🌟 ग्रंथ की प्रमुख विशेषताएं</div>
    <ul style="margin:0; padding-left:1.2rem; font-size:0.82rem; line-height:1.6;">
      <li><strong>१००% शुद्ध हस्त-गणित सूत्र:</strong> बिना किसी प्रोग्रामिंग भाषा के, केवल प्रत्यक्ष गणितीय समीकरण।</li>
      <li><strong>चरणबद्ध हिंदी कलन विधि:</strong> कक्षा ८ उत्तीर्ण व्यक्ति भी सरलता से कुण्डली बना सके।</li>
      <li><strong>आदर्श शोध केस स्टडी:</strong> जातक 'क' (२८ अक्टूबर १९९४, ०३:४५ AM) के वास्तविक मानों पर पूर्ण प्रत्यक्ष अभ्यास।</li>
      <li><strong>वृहत्पाराशर एवं सूर्य सिद्धांत:</strong> प्राचीन ऋषियों के प्रामाणिक श्लोकों का वैज्ञानिक निरूपण।</li>
    </ul>
  </div>

  <div style="margin-top:1.5rem; font-size:0.8rem; color:#475569;">
    <strong>प्रणेता:</strong> तंत्र ज्ञान शोध संस्थान • <strong>आधिकारिक पोर्टल:</strong> https://t.worldgyan.com
  </div>
</div>
'''
    pages.append(make_page(1, "मुखपृष्ठ • Cover", "वैदिक कुण्डली विचार एवं गणित महाग्रंथ", p1))

    # Page 2: मंगलाचरण • Invocation
    p2 = '''
<div style="background:#fefce8; border:1px solid #fef08a; border-radius:8px; padding:0.9rem; margin-bottom:1rem; text-align:center;">
  <div style="font-family:'Noto Serif Devanagari', serif; font-size:0.95rem; font-weight:700; color:#854d0e; line-height:1.6;">
    ॥ प्रणम्य शिरसा देवं गौरीपुत्रं विनायकम् ।<br>
    भक्तावासं स्मरेन्नित्यमायुःकामार्थसिद्धये ॥<br>
    ॥ नमः सूर्याय चन्द्राय मङ्गलाय बुधाय च ।<br>
    गुरुशुक्रशनिभ्यश्च राहवे केतवे नमः ॥
  </div>
  <div style="font-size:0.8rem; color:#713f12; margin-top:0.4rem;">
    <em>भावार्थ:</em> विघ्नहर्ता भगवान श्री गणेश एवं नवग्रहों को नमन करते हुए हम काल-विज्ञान एवं ब्रह्माण्डीय गणित के इस पावन महाग्रंथ का शुभारंभ करते हैं।
  </div>
</div>

<p><strong>ग्रंथ का संकल्प:</strong> वैदिक ज्योतिष कोई अंधविश्वास या अनुमान का खेल नहीं है, अपितु यह विशुद्ध खगोल-गणित (Spherical Astronomy) और कॉस्मिक ज्यामिति (Cosmic Geometry) पर आधारित पूर्ण विज्ञान है। जब किसी बालक का जन्म इस भूतल पर होता है, उस सूक्ष्म क्षण में पूर्वी क्षितिज पर उदित होने वाली राशि और आकाश में ग्रहों के सटीक कोणीय देशांतर उस आत्मा के संचित प्रारब्ध का खगोलीय मानचित्र अंकित करते हैं।</p>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.7rem 0.9rem; margin-top:0.8rem; font-size:0.82rem;">
  <strong>📌 पाठक के लिए मार्गदर्शिका:</strong> इस महाग्रंथ में प्रत्येक खगोलीय नियम को चार स्तरों पर प्रस्तुत किया गया है: (१) ऋषि पराशर का मूल संस्कृत सूत्र, (२) सरल हिंदी में खगोलीय अवधारणा, (३) शुद्ध गणितीय समीकरण, और (४) <strong>जातक 'क'</strong> पर प्रत्यक्ष चरणबद्ध गणना।
</div>
'''
    pages.append(make_page(2, "मंगलाचरण • Invocation", "प्रस्तावना एवं दिव्य काल-विज्ञान", p2))

    # Page 3: दर्शन एवं खगोलीय निर्देशांक
    p3 = '''
<p>वैदिक ज्योतिष में काल-गणना को समझने के लिए तीन प्रमुख खगोलीय संदर्भ मंडलों को जानना अनिवार्य है:</p>

<table style="width:100%; border-collapse:collapse; margin:0.8rem 0; font-size:0.8rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">संदर्भ वृत्त</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">खगोलीय परिभाषा</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">ज्योतिषीय उपयोग</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>१. क्रांतिवृत्त (Ecliptic)</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">पृथ्वी से देखने पर सूर्य का वार्षिक प्रत्यक्ष मार्ग ($३६०^\circ$ वृत्त)।</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">१२ राशियों एवं २७ नक्षत्रों का आधार।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>२. खगोलीय विषुवत् (Celestial Equator)</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">पृथ्वी की भूमध्य रेखा का अंतरिक्ष में विस्तार।</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">विषुवांश (Right Ascension) एवं विषुव संपात का आधार।</td>
    </tr>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>३. स्थानीय क्षितिज (Local Horizon)</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">किसी स्थान विशेष पर प्रेक्षक की दृष्टि सीमा।</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">लग्न (Ascendant) एवं १२ भावों का विभाजन।</td>
    </tr>
  </tbody>
</table>

<div style="background:#f1f5f9; border-radius:6px; padding:0.7rem; font-size:0.82rem; margin-top:0.6rem;">
  <strong>💡 क्रांतिवृत्त का झुकाव कोण (Obliquity $\varepsilon$):</strong> क्रांतिवृत्त और विषुवत् वृत्त एक दूसरे पर लगभग $२३^\circ २६'$ के कोण पर झुके हुए हैं। इसी झुकाव के कारण ऋतु परिवर्तन और राशियों के उदय मान में अक्षांशीय अंतर आता है।
</div>
'''
    pages.append(make_page(3, "खगोल आधार • Astronomy", "ब्रह्माण्डीय संदर्भ मंडल एवं त्रि-आयामी ज्यामिति", p3))

    # Page 4: गणितीय शब्दावली एवं प्रतीक
    p4 = '''
<p>इस महाग्रंथ में प्रयुक्त प्रमुख गणितीय एवं खगोलीय प्रतीकों की सूची:</p>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:0.6rem; font-size:0.8rem; margin:0.8rem 0;">
  <div style="background:#fff; border:1px solid #e2e8f0; padding:0.6rem; border-radius:6px;">
    <strong style="color:#0284c7;">📐 कोणीय माप:</strong><br>
    • $१$ वृत्त = १२ राशियां = $३६०^\circ$<br>
    • $१$ राशि = $३०^\circ$<br>
    • $१^\circ$ (अंश) = ६०' (कला / मिनट)<br>
    • १' (कला) = ६०'' (विकला / सेकंड)<br>
    • १ नक्षत्र = $१३^\circ २०'$ = ८०० कला<br>
    • १ नक्षत्र चरण = $३^\circ २०'$ = २०० कला
  </div>
  <div style="background:#fff; border:1px solid #e2e8f0; padding:0.6rem; border-radius:6px;">
    <strong style="color:#b45309;">⏱️ वैदिक काल माप:</strong><br>
    • १ दिन-रात = ६० घटी = २४ घंटे<br>
    • १ घटी = २४ मिनट = ६० पल<br>
    • १ पल = २४ सेकंड = ६० विपल<br>
    • १ विपल = ०.४ सेकंड<br>
    • १ सौर वर्ष = ३६५.२४२२ दिन<br>
    • १ नाक्षत्र वर्ष = ३६५.२५६३६ दिन
  </div>
</div>

<div style="background:#fdf2f8; border-left:4px solid #db2777; padding:0.6rem 0.8rem; font-size:0.8rem;">
  <strong>स्वर्ण नियम (अंश से कला रूपांतरण):</strong> किसी भी ग्रह की स्थिति को कला में बदलने का सूत्र:<br>
  $$\text{कुल कला} = (\text{राशि} \times ३० + \text{अंश}) \times ६० + \text{कला}$$
</div>
'''
    pages.append(make_page(4, "खगोल आधार • Astronomy", "वैदिक गणितीय इकाइयां, प्रतीक एवं रूपांतरण सूत्र", p4))

    # Page 5: सौर-सावन-नाक्षत्र दिवस
    p5 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ सूर्यसिद्धांते कालविभागः ॥</strong><br>
  <em>"सावनैर्दिनमासाब्दाः सौराः स्युः रविसंक्रमात् । नाक्षत्रं भपरिक्रान्त्या..."</em>
</div>

<p>काल-गणना में तीन प्रमुख दिवसों का अंतर समझना अत्यंत आवश्यक है:</p>

<ol style="font-size:0.82rem; line-height:1.6; padding-left:1.2rem;">
  <li><strong>सावन दिवस (Civil / Solar Day):</strong> एक सूर्योदय से अगले सूर्योदय तक का समय (औसत २४ घंटा = ६० घटी)।</li>
  <li><strong>नाक्षत्र दिवस (Sidereal Day):</strong> किसी दूरस्थ तारे के परिप्रेक्ष्य में पृथ्वी का अपनी धुरी पर एक पूरा चक्कर ($३६०^\circ$ घूर्णन)। समय: <strong>२३ घंटे ५६ मिनट ४.०९१ सेकंड</strong>।</li>
  <li><strong>सौर दिवस (Solar Day):</strong> सूर्य के प्रत्यक्ष मार्ग में १ अंश गति करने में लगा समय।</li>
</ol>

<div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:6px; padding:0.7rem; font-size:0.82rem; margin-top:0.6rem;">
  <strong>⚡ नाक्षत्र एवं सावन दिन में अंतर का कारण:</strong> पृथ्वी जब अपनी धुरी पर घूमती है, तब साथ-साथ वह सूर्य की परिक्रमा में लगभग $१^\circ$ आगे भी बढ़ जाती है। इसलिए सूर्य को पुनः उसी मध्याह्न रेखा पर आने के लिए पृथ्वी को $३६०^\circ$ के अतिरिक्त लगभग $१^\circ$ और घूमना पड़ता है, जिसमें लगभग ३ मिनट ५६ सेकंड का अतिरिक्त समय लगता है।
</div>
'''
    pages.append(make_page(5, "खगोल आधार • Astronomy", "सौर, सावन एवं नाक्षत्र दिवस का गणितीय भेद", p5))

    # Page 6: जूलियन डे कलन विधि
    p6 = '''
<p>खगोल-विज्ञान में शताब्दियों के पंचांगीय विचलन को दूर करने के लिए ईसा पूर्व ४७१३ से निरंतर बीत चुके दिनों की गणना को <strong>जूलियन डे (Julian Day - JD)</strong> कहते हैं।</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.8rem; border-radius:6px; font-size:0.82rem; margin:0.7rem 0;">
  <strong style="color:#38bdf8;">📐 जूलियन डे गणितीय सूत्र (ग्रेगोरियन कैलेंडर):</strong><br>
  यदि माह ($M$) १ या २ (जनवरी/फरवरी) हो, तो $Y = Y - १$ और $M = M + १२$ लें।<br>
  $$A = \lfloor Y / १०० \rfloor$$<br>
  $$B = २ - A + \lfloor A / ४ \rfloor$$<br>
  $$JD = \lfloor ३६५.२५ \times (Y + ४७१६) \rfloor + \lfloor ३०.६००१ \times (M + १) \rfloor + D + B - १५२४.५$$
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.7rem; font-size:0.82rem;">
  <strong style="color:#166534;">📝 जातक 'क' पर प्रत्यक्ष गणना:</strong><br>
  • जन्म: २८ अक्टूबर १९९४, ०३:४५:०० AM IST (२२:१५:०० UTC, २७ अक्टूबर)<br>
  • $Y = १९९४, M = १०, D = २७ + २२.२५ / २४ = २७.९२७०८३$<br>
  • $A = \lfloor १९९४ / १०० \rfloor = १९$<br>
  • $B = २ - १९ + \lfloor १९ / ४ \rfloor = २ - १९ + ४ = -१३$<br>
  • गणना उपरांत: <strong>JD = २४४९६५३.४२७०८३</strong>
</div>
'''
    pages.append(make_page(6, "खगोल आधार • Astronomy", "जूलियन डे (JD) साधन: गणितीय सूत्र एवं कलन विधि", p6))

    # Page 7: GMST एवं LST साधन
    p7 = '''
<p>लग्न निकालने के लिए हमें जन्म-स्थान पर उस क्षण का <strong>स्थानीय नाक्षत्र समय (Local Sidereal Time - LST)</strong> ज्ञात होना चाहिए।</p>

<div style="background:#f1f5f9; border-left:4px solid #0284c7; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>चरणबद्ध कलन विधि (Hindi Algorithm):</strong><br>
  <strong>चरण १:</strong> जूलियन सदियों ($T$) की गणना करें:<br>
  $$T = (JD - २४५१५४५.०) / ३६५२५$$<br>
  <strong>चरण २:</strong> ग्रीनविच मध्याह्न नाक्षत्र समय ($GMST$) अंशों में निकालें:<br>
  $$GMST = २८०.४६०६१८३७ + ३६०.९८५६४७३६६२९ \times (JD - २४५१५४५.०) + ०.०००३८७९३३ \times T^२$$<br>
  <strong>चरण ३:</strong> स्थानीय देशांतर ($\lambda$) जोड़कर स्थानीय नाक्षत्र समय ($LST$) प्राप्त करें:<br>
  $$LST = GMST + \lambda_{\text{स्थानीय}}$$
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.82rem;">
  <strong style="color:#854d0e;">जातक 'क' पर प्रत्यक्ष गणना:</strong><br>
  • जन्म स्थान देशांतर: $८३.६५^\circ$ पूर्व (गढ़वा, झारखंड)<br>
  • $GMST = ५.३३३३\text{ घंटा}$, स्थानीय देशांतर संशोधन $= +५.५७६७\text{ घंटा}$<br>
  • <strong>LST = ५.९०८० घंटा = ८८.६२००° (RAMC)</strong>
</div>
'''
    pages.append(make_page(7, "खगोल आधार • Astronomy", "ग्रीनविच एवं स्थानीय नाक्षत्र समय (LST) साधन", p7))

    # Page 8: सायन-निरयण भेद एवं अयनांश
    p8 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ अयनांश रहस्यम् ॥</strong><br>
  <em>"संपाताग्रं यदा चक्रं भ्रमतेऽयनसंज्ञितम् । तदंतरं तु यत्प्रोक्तमयनांशः स उच्यते ॥"</em>
</div>

<p><strong>सायन (Tropical) बनाम निरयण (Sidereal):</strong></p>
<ul style="font-size:0.82rem; line-height:1.6; padding-left:1.2rem;">
  <li><strong>सायन प्रणाली:</strong> वसंत संपात (Vernal Equinox, जहाँ सूर्य विषुवत् वृत्त को काटता है) को मेष ०° माना जाता है। संपात बिंदु स्थिर नहीं है; यह प्रतिवर्ष लगभग ५०.२९ विकला पीछे खिसकता है (Precession)।</li>
  <li><strong>निरयण प्रणाली (वैदिक):</strong> स्थिर तारों (जैसे चित्रा तारा / Spica) को आधार बनाकर मेष ०° निर्धारित किया जाता है।</li>
  <li><strong>अयनांश (Ayanamsha):</strong> सायन राशि और निरयण राशि के बीच का कोणीय अंतर अयनांश कहलाता है:</li>
</ul>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.85rem; text-align:center; margin:0.7rem 0;">
  $$\text{निरयण ग्रह स्पष्ट} = \text{सायन ग्रह स्पष्ट} - \text{अयनांश}$$
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.82rem;">
  <strong>शून्य अयनांश वर्ष:</strong> भारत सरकार की कैलेंडर सुधार समिति (लहिरी मत) के अनुसार ईस्वी सन् <strong>२८५</strong> में सायन एवं निरयण मेष बिंदु एक ही स्थान पर संपाती थे।
</div>
'''
    pages.append(make_page(8, "अयनांश गणित • Ayanamsha", "सायन-निरयण भेद एवं अयनांश का खगोलीय आधार", p8))

    # Page 9: लहिरी (चित्रापक्षीय) अयनांश सूत्र
    p9 = '''
<p>वैदिक ज्योतिष में सर्वाधिक प्रामाणिक एवं मान्य अयनांश <strong>चित्रापक्षीय लहिरी अयनांश</strong> है, जिसमें चित्रा तारे (Spica) को तुला राशि में ठीक $६^\circ ००'$ (अर्थात $१८०^\circ$ के विपरीत) पर स्थित माना गया है।</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>लहिरी अयनांश का यथार्थ गणितीय सूत्र:</strong><br>
  $$T = (JD - २४५१५४५.०) / ३६५२५$$<br>
  $$\text{Ayanamsha} = २३.८५८०७२ + १.३९६०४२ \times T + ०.०००३०८ \times T^२$$<br>
  (अथवा वार्षिक गति दर: $५०.२९०९६६''$ प्रति वर्ष)
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem;">
  <strong style="color:#854d0e;">जातक 'क' पर प्रत्यक्ष अयनांश गणना:</strong><br>
  • जन्म दिनांक: २८ अक्टूबर १९९४<br>
  • $JD = २४४९६५३.४२७०८३$<br>
  • $T = (२४४९६५३.४२७०८३ - २४५१५४५.०) / ३६५२५ = -०.०५१८$ शताब्दियां<br>
  • गणना उपरांत: <strong>अयनांश = २३° ४८' १३'' (२३.८०३७°)</strong>
</div>

<div style="background:#f0fdf4; padding:0.6rem; border-radius:6px; font-size:0.8rem; margin-top:0.6rem;">
  <strong>फलित प्रभाव:</strong> जातक 'क' के सायन ग्रहों में से $२३^\circ ४८' १३''$ घटाने पर ही वास्तविक निरयण कुण्डली प्राप्त होगी।
</div>
'''
    pages.append(make_page(9, "अयनांश गणित • Ayanamsha", "चित्रापक्षीय लहिरी अयनांश: प्रामाणिक सूत्र एवं साधन", p9))

    # Page 10: रमन एवं केपी अयनांश तुलना
    p10 = '''
<p>विभिन्न ज्योतिषीय परंपराओं में शून्य अयनांश वर्ष के भिन्न मतों के कारण अयनांश मानों में सूक्ष्म अंतर आता है:</p>

<table style="width:100%; border-collapse:collapse; margin:0.8rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">अयनांश पद्धति</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">शून्य वर्ष</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">१९९४ में मान</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">प्रमुख विशेषता</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>१. लहिरी (चित्रापक्ष)</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">२८५ ई.</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;"><strong>२३° ४८' १३''</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">भारत सरकार एवं पराशर परंपरा द्वारा मान्य।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>२. कृष्णमूर्ति (KP)</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">२९१ ई.</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">२३° ४१' ३०''</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">उप-नक्षत्र (Sub-lord) पद्धति में प्रयुक्त।</td>
    </tr>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>३. बी. वी. रमन</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">३९७ ई.</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">२२° २१' ०५''</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">प्रो. रमन द्वारा प्रतिपादित प्राचीन मत।</td>
    </tr>
  </tbody>
</table>

<div style="background:#fffbeb; border-left:4px solid #f59e0b; padding:0.6rem; font-size:0.8rem;">
  <strong>महत्वपूर्ण निष्कर्ष:</strong> इस महाग्रंथ में सर्वमान्य <strong>लहिरी अयनांश</strong> को ही मानक आधार माना गया है, क्योंकि यह आधुनिक स्विस एफेमेरिस एवं दृश्य वेधशालाओं से शत-प्रतिशत मेल खाता है।
</div>
'''
    pages.append(make_page(10, "अयनांश गणित • Ayanamsha", "लहिरी, रमन एवं कृष्णमूर्ति (KP) अयनांश तुलना", p10))

    # Page 11: सौर क्रांति एवं Obliquity
    p11 = '''
<p>पृथ्वी की अक्षीय झुकाव दर को <strong>क्रांतिवृत्त झुकाव (True Obliquity of Ecliptic - $\varepsilon$)</strong> कहते हैं। लग्न साधन में इसका अत्यंत महत्वपूर्ण स्थान है।</p>

<div style="background:#f1f5f9; border-left:4px solid #0284c7; padding:0.7rem; font-size:0.82rem; margin:0.7rem 0;">
  <strong>झुकाव कोण ($\varepsilon$) का खगोलीय सूत्र:</strong><br>
  $$T = (JD - २४५१५४५.०) / ३६५२५$$<br>
  $$\varepsilon_० = २३^\circ २६' २१.४४८'' - ४६.८१५०'' \times T - ०.०००५९'' \times T^२ + ०.००१८१३'' \times T^३$$
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.82rem;">
  <strong style="color:#166534;">जातक 'क' की जन्म तिथि पर मान:</strong><br>
  • दिनांक: २८ अक्टूबर १९९४<br>
  • $T = -०.०५१८$<br>
  • $\varepsilon = २३^\circ २६' २३.८७''$ = <strong>२३.४३९९६°</strong>
</div>

<div style="background:#fefce8; padding:0.6rem; border-radius:6px; font-size:0.8rem; margin-top:0.6rem;">
  <strong>भौतिक प्रभाव:</strong> इसी $\varepsilon$ कोण के कारण जब सूर्य क्रांतिवृत्त पर चलता है, तो उसकी उत्तर-दक्षिण क्रांति (Declination $\delta$) $-२३.४४^\circ$ (मकर संक्रांति) से $+२३.४४^\circ$ (कर्क संक्रांति) के बीच दोलन करती है।
</div>
'''
    pages.append(make_page(11, "खगोल आधार • Astronomy", "सौर क्रांति एवं क्रांतिवृत्त झुकाव कोण (Obliquity)", p11))

    # Page 12: जातक 'क' खगोल समरी
    p12 = '''
<p>जातक 'क' के जन्मकालीन आधारभूत खगोलीय इनपुट एवं गणना परिणामों की मास्टर तालिका:</p>

<table style="width:100%; border-collapse:collapse; margin:0.8rem 0; font-size:0.8rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.4rem; border:1px solid #334155; text-align:left;">खगोलीय पैरामीटर</th>
      <th style="padding:0.4rem; border:1px solid #334155; text-align:left;">इनपुट / मान</th>
      <th style="padding:0.4rem; border:1px solid #334155; text-align:left;">ज्योतिषीय उपयोगिता</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">जन्म दिनांक एवं समय</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">२८ अक्टूबर १९९४, ०३:४५ AM IST</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">काल गणना का आरंभ बिंदु।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">जन्म स्थान निर्देशांक</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">२४.०५° उत्तर, ८३.६५° पूर्व (गढ़वा)</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">स्थानीय क्षितिज एवं अक्षांश।</td>
    </tr>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">जूलियन डे (JD)</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>२४४९६५३.४२७०८३</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">निरंतर खगोलीय समय।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">स्थानीय नाक्षत्र समय (LST)</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>५.९०८० घंटा (८८.६२° RAMC)</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">लग्न एवं दशम भाव का आधार।</td>
    </tr>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">चित्रापक्ष लहिरी अयनांश</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>२३° ४८' १३'' (२३.८०३७°)</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">सायन से निरयण रूपांतरण।</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.6rem; font-size:0.8rem;">
  <strong>अध्याय १ निष्कर्ष:</strong> इन पांच अचूक खगोलीय आधारों से अब हम अगले अध्यायों में लग्न, भाव एवं ग्रह स्पष्ट का गणित सिद्ध करेंगे।
</div>
'''
    pages.append(make_page(12, "केस स्टडी • Case Study", "जातक 'क' की आधारभूत खगोलीय तालिका", p12))

    # Pages 13 to 28 can be similarly defined with pure formulas and examples!
    # Let's populate pages 13-28 with rich content.
    return pages

print("Part 1 defined")

def append_pages_13_to_28(pages):
    # Page 13: लग्न की खगोलीय परिभाषा
    p13 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ लग्न लक्षणम् बृहत्पाराशरे ॥</strong><br>
  <em>"प्राची क्षितिजे यल्लग्नं तल्लग्नमिति कथ्यते । राशीनामुदयो यस्माल्लग्नादेव प्रकीर्तितः ॥"</em>
</div>

<p><strong>खगोलीय परिभाषा:</strong> जिस क्षण बालक का जन्म होता है, उस समय पूर्वी क्षितिज (Eastern Horizon) और क्रांतिवृत्त (Ecliptic) का जो प्रतिच्छेदन बिंदु (Intersection Point) होता है, उसे <strong>लग्न (Ascendant)</strong> कहते हैं।</p>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>लग्न का ज्योतिषीय महत्व:</strong><br>
  • लग्न जातक का शरीर, रूप, स्वास्थ्य, स्वभाव एवं आत्मिक चेतना है।<br>
  • संपूर्ण १२ भावों की आधारशिला लग्न ही है; यदि लग्न अशुद्ध हो जाए, तो संपूर्ण फलादेश भ्रांत हो जाता है।<br>
  • पृथ्वी के २४ घंटे में $३६०^\circ$ घूमने के कारण प्रत्येक राशि औसतन २ घंटे (५ घटी) पूर्वी क्षितिज पर उदित रहती है।
</div>
'''
    pages.append(make_page(13, "लग्न साधन • Ascendant", "लग्न की खगोलीय परिभाषा एवं क्षितिज वृत्त", p13))

    # Page 14: लंका-उदय मान एवं चर-खंड
    p14 = '''
<p>विषुवत् रेखा (Equator / लंका) पर सभी राशियों के उदय काल सममित होते हैं, जिन्हें <strong>लंका-उदय मान (Equatorial Ascensions)</strong> कहते हैं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">राशि युग्म</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">लंका मान (पल)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">समय (मिनट)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">अंश विस्तार</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">मेष - मीन - कन्या - तुला</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">२७८ पल</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">१११.२ मिनट</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">२७.८°</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">वृषभ - कुंभ - सिंह - वृश्चिक</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">२९९ पल</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">११९.६ मिनट</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">२९.९°</td>
    </tr>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">मिथुन - मकर - कर्क - धनु</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">३२३ पल</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">१२९.२ मिनट</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1; text-align:center;">३२.३°</td>
    </tr>
  </tbody>
</table>

<div style="background:#f1f5f9; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong>चर-खंड (Ascensional Difference):</strong> किसी स्थान के अक्षांश ($\phi$) के कारण लंका-मान में जो वृद्धि या ह्रास होता है, उसे चर-खंड कहते हैं:<br>
  $$\sin(\text{चर}) = \tan(\phi) \times \tan(\delta)$$
</div>
'''
    pages.append(make_page(14, "लग्न साधन • Ascendant", "लंका-उदय मान एवं चर-खंड साधन सूत्र", p14))

    # Page 15: स्वदेशीय उदय मान
    p15 = '''
<p>किसी विशिष्ट नगर या अक्षांश ($\phi$) के लिए राशियों के वास्तविक उदय मान निकालने की शास्त्रीय विधि:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 स्वदेशीय मान साधन सूत्र:</strong><br>
  १. मेष, मीन = लंका मान - चर खंड १<br>
  २. वृषभ, कुंभ = लंका मान - चर खंड २<br>
  ३. मिथुन, मकर = लंका मान - चर खंड ३<br>
  ४. कर्क, धनु = लंका मान + चर खंड ३<br>
  ५. सिंह, वृश्चिक = लंका मान + चर खंड २<br>
  ६. कन्या, तुला = लंका मान + चर खंड १
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong>जातक 'क' के जन्म स्थान (गढ़वा, २४.०५° उ.) के लिए मान:</strong><br>
  • कन्या राशि (६ठी राशि) का उदय मान $= २७८ + ४२ = ३२०\text{ पल} = २\text{ घंटा } ८\text{ मिनट}$।<br>
  • इसलिए कन्या लग्न में जन्म लेने के लिए सूर्योदय के बाद के इष्टकाल का सूक्ष्म अनुपात निकाला जाता है।
</div>
'''
    pages.append(make_page(15, "लग्न साधन • Ascendant", "स्वदेशीय राशि-उदय मान निकालने की कलन विधि", p15))

    # Page 16: इष्टकाल साधन
    p16 = '''
<p>सूर्योदय से लेकर जन्म-समय तक बीते हुए समय को वैदिक ज्योतिष में <strong>इष्टकाल (Ishtakaal)</strong> कहते हैं।</p>

<div style="background:#f1f5f9; border-left:4px solid #b45309; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>इष्टकाल साधन कलन विधि (Hindi Algorithm):</strong><br>
  <strong>चरण १:</strong> जन्म समय (घंटा:मिनट) में से स्थानीय सूर्योदय का समय घटाएं।<br>
  <strong>चरण २:</strong> यदि जन्म सूर्योदय से पूर्व (ब्रह्ममुहूर्त/रात्रि) हुआ हो, तो पूर्व दिवस के सूर्योदय से समय जोड़ें।<br>
  <strong>चरण ३:</strong> प्राप्त घंटों को २.५ से गुणा करके घटी-पल प्राप्त करें:<br>
  $$\text{इष्टकाल (घटी-पल)} = \text{व्यतीत घंटे} \times २.५$$
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong style="color:#854d0e;">जातक 'क' पर प्रत्यक्ष इष्टकाल गणना:</strong><br>
  • जन्म समय: ०३:४५ AM (२८ अक्टूबर १९९४)<br>
  • २७ अक्टूबर का सूर्योदय: ०५:५६ AM IST<br>
  • सूर्योदय से जन्म तक बीता समय $= २१\text{ घंटा } ४९\text{ मिनट} = २१.८१६७\text{ घंटे}$<br>
  • <strong>इष्टकाल = २१.८१६७ × २.५ = ५४ घटी ३२ पल</strong>
</div>
'''
    pages.append(make_page(16, "लग्न साधन • Ascendant", "इष्टकाल साधन: घटी-पल रूपांतरण एवं कलन विधि", p16))

    # Page 17: लग्न स्पष्ट त्रिकोणमितीय सूत्र
    p17 = '''
<p>आधुनिक उच्च-परिशुद्धता खगोलीय त्रिकोणमिति द्वारा लग्न स्पष्ट ($\lambda_{\text{Asc}}$) ज्ञात करने का यथार्थ समीकरण:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.8rem; border-radius:6px; font-size:0.82rem; margin:0.7rem 0;">
  <strong style="color:#38bdf8;">📐 लग्न स्पष्ट समीकरण (Trigonometric Ascendant Equation):</strong><br>
  $$\tan(\lambda_{\text{Asc}}) = \frac{-\cos(\theta)}{\sin(\theta) \times \cos(\varepsilon) + \tan(\phi) \times \sin(\varepsilon)}$$<br>
  जहाँ:<br>
  • $\theta = \text{LST (स्थानीय नाक्षत्र समय कोण / RAMC)}$<br>
  • $\varepsilon = \text{क्रांतिवृत्त झुकाव (Obliquity) } = २३.४३९९६^\circ$<br>
  • $\phi = \text{जन्म स्थान का अक्षांश } = २४.०५^\circ \text{ उत्तर}$
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.82rem;">
  <strong style="color:#166534;">चरणबद्ध गणना:</strong><br>
  १. $\theta = ८८.६२^\circ \implies \cos(\theta) = ०.०२४०८, \sin(\theta) = ०.९९९७$<br>
  २. हर (Denominator) $= ०.९९९७ \times \cos(२३.४४^\circ) + \tan(२४.०५^\circ) \times \sin(२३.४४^\circ) = १.०९५१$<br>
  ३. सायन लग्न $= १८८.५१^\circ$ (तुला ८° ३१')<br>
  ४. निरयण लग्न $= सायन - अयनांश = १८८.५१^\circ - २३.८०^\circ = \mathbf{१६४.७१^\circ}$ (कन्या १४° ४२')
</div>
'''
    pages.append(make_page(17, "लग्न साधन • Ascendant", "लग्न स्पष्ट: गोलीय त्रिकोणमिति एवं सूक्ष्म सूत्र", p17))

    # Page 18: दशम भाव (MC) साधन
    p18 = '''
<p>आकाश के सर्वोच्च बिंदु जहां स्थानीय याम्योत्तर (Meridian) क्रांतिवृत्त को काटता है, उसे <strong>दशम भाव मध्य (Medium Coeli - MC)</strong> कहते हैं:</p>

<div style="background:#f1f5f9; border-left:4px solid #0284c7; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>दशम भाव (MC) साधन सूत्र:</strong><br>
  $$\tan(\lambda_{\text{MC}}) = \frac{\tan(\theta)}{\cos(\varepsilon)}$$<br>
  जहाँ $\theta = \text{RAMC (LST कोण)}$ एवं $\varepsilon = \text{Obliquity}$
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.82rem;">
  <strong style="color:#854d0e;">जातक 'क' पर प्रत्यक्ष दशम भाव गणना:</strong><br>
  • $\theta = ८८.६२००^\circ, \varepsilon = २३.४३९९६^\circ$<br>
  • सायन $\text{MC} = ८८.४९^\circ$ (मिथुन २८° २९')<br>
  • निरयण $\text{MC} = ८८.४९^\circ - २३.८०३७^\circ = \mathbf{६४.६८^\circ}$ (मिथुन ४° ४१')<br>
  • <strong>ज्योतिषीय फल:</strong> दशम भाव का स्वामी बुध है, जो कर्म क्षेत्र में बौद्धिक, विश्लेषणात्मक एवं तकनीकी सफलता दर्शाता है।
</div>
'''
    pages.append(make_page(18, "भाव साधन • Houses", "दशम भाव (MC) एवं याम्योत्तर मध्य साधन सूत्र", p18))

    # Page 19: भाव विभाजन प्रणालियां
    p19 = '''
<p>वैदिक ज्योतिष में १२ भावों के विस्तार को लेकर दो प्रमुख शास्त्रीय पद्धतियां प्रचलित हैं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">पद्धति</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">सिद्धांत एवं विभाजन नियम</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">प्रामाणिक संदर्भ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>१. संपूर्ण राशि भाव (Whole Sign)</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">जिस राशि में लग्न पड़े, वह संपूर्ण राशि (०° से ३०°) प्रथम भाव होती है। अगली राशि द्वितीय भाव होती है।</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">महर्षि पराशर, जैमिनी एवं भृगु नंदी नाड़ी द्वारा सर्वोपरि मान्य।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.4rem; border:1px solid #cbd5e1;"><strong>२. श्रीपति भाव (Sripati / Porphyry)</strong></td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">लग्न को प्रथम भाव मध्य और MC को दशम भाव मध्य मानकर चतुर्थांशों को ३ समान भागों में बांटना।</td>
      <td style="padding:0.4rem; border:1px solid #cbd5e1;">श्रीपति पद्धति, भाव-चलित एवं षड्बल गणना में प्रयुक्त।</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong>ग्रंथ का निर्देश:</strong> ग्रह स्थिति, दृष्टि, योग एवं दशा फलित के लिए <strong>Whole Sign (संपूर्ण राशि भाव)</strong> को ही महर्षि पराशर ने प्रधानता दी है।
</div>
'''
    pages.append(make_page(19, "भाव साधन • Houses", "श्रीपति भाव विभाजन बनाम संपूर्ण राशि भाव सिद्धांत", p19))

    # Page 20: जातक 'क' १२ भाव तालिका
    p20 = '''
<p>जातक 'क' की जन्म कुण्डली के १२ भावों का संपूर्ण राशि चक्र एवं अधिपति तालिका:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.35rem; border:1px solid #334155;">भाव</th>
      <th style="padding:0.35rem; border:1px solid #334155;">राशि</th>
      <th style="padding:0.35rem; border:1px solid #334155;">अंश विस्तार</th>
      <th style="padding:0.35rem; border:1px solid #334155;">भावाधिपति</th>
      <th style="padding:0.35rem; border:1px solid #334155;">स्थित ग्रह</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">१ (तनु)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कन्या</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१६४° ४२'</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">बुध</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">लग्न बिंदु</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">२ (धन)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१९४° ४२'</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शुक्र</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सूर्य, बुध, शुक्र, राहु</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">३ (सहज)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">वृश्चिक</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२२४° ४२'</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मंगल</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">गुरु</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">४ (सुख)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">धनु</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२५४° ४२'</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">गुरु</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">-</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">६ (रिपु)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कुंभ</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">३१४° ४२'</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शनि</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शनि (स्वक्षेत्री)</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">११ (लाभ)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कर्क</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१०४° ४२'</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">चंद्रमा</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">चंद्रमा (स्वक्षेत्री)</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">१२ (व्यय)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सिंह</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१३४° ४२'</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सूर्य</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मंगल</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>विशेष योग:</strong> लग्नेश बुध द्वितीय (वाणी/धन) में, लाभेश चंद्रमा एकादश (लाभ) में स्वक्षेत्री, एवं षष्ठेश शनि षष्ठ भाव में स्वक्षेत्री हैं।
</div>
'''
    pages.append(make_page(20, "केस स्टडी • Case Study", "जातक 'क' की संपूर्ण १२ भाव स्पष्ट तालिका", p20))

    # Page 21: ग्रह गतिकी एवं मंदस्पष्ट
    p21 = '''
<p>सूर्य सिद्धांत के अनुसार ग्रहों की दो गतियां होती हैं: औसत (Mean) और यथार्थ (True)।</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>मंदस्पष्ट (Equation of Centre) साधन सूत्र:</strong><br>
  १. मंद केंद्र ($M$) निकालें: $M = \text{मध्यम ग्रह} - \text{मंदोच्च (Apogee)}$<br>
  २. मंदफल ($C$) का सूत्र:<br>
  $$C = \left(\frac{\text{मंदपरिधि}}{३६०^\circ}\right) \times \sin(M)$$<br>
  ३. मंदस्पष्ट ग्रह $= \text{मध्यम ग्रह} \mp C$ (केंद्र के पद अनुसार धन/ऋण)
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong>ग्रहों की दैनिक औसत गति (कला प्रति दिन):</strong><br>
  • सूर्य: ५९' ०८'' • चंद्र: ७९०' ३५'' • मंगल: ३१' २७''<br>
  • बुध: २५३' १२'' • गुरु: ४' ५९'' • शुक्र: ९६' ०८'' • शनि: २' ००''
</div>
'''
    pages.append(make_page(21, "ग्रह गतिकी • Planetary Motion", "ग्रहों की मध्यम एवं मंदस्पष्ट गति कलन विधि", p21))

    # Page 22: शीघ्रस्पष्ट एवं भू-केंद्रीय कोण
    p22 = '''
<p>सूर्य-केंद्रीय (Heliocentric) गति को पृथ्वी से देखने पर जो कोण प्राप्त होता है, उसे <strong>शीघ्रस्पष्ट (Geocentric Longitude)</strong> कहते हैं:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 शीघ्रफल समीकरण:</strong><br>
  १. शीघ्र केंद्र ($S$) निकालें: $S = \text{शीघ्रोच्च (सूर्य)} - \text{मंदस्पष्ट ग्रह}$<br>
  २. शीघ्रफल ($E$) का सूत्र:<br>
  $$\tan(E) = \frac{r \times \sin(S)}{R + r \times \cos(S)}$$<br>
  जहाँ $R = १\text{ AU (पृथ्वी की दूरी)}$ तथा $r = \text{ग्रह की कक्षा त्रिज्या}$।
</div>

<div style="background:#f0fdf4; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong>तात्विक अर्थ:</strong> पृथ्वी के स्वयं गतिमान होने के कारण बाहरी ग्रहों (मंगल, गुरु, शनि) में जो कोणीय विचलन दृष्टिगोचर होता है, वही शीघ्रफल है।
</div>
'''
    pages.append(make_page(22, "ग्रह गतिकी • Planetary Motion", "शीघ्रस्पष्ट एवं भू-केंद्रीय कोणीय संशोधन सूत्र", p22))

    # Page 23: वक्री गति (Retrograde)
    p23 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ वक्री गति रहस्यम् सारावल्याम् ॥</strong><br>
  <em>"वक्रा गतिः समाख्याता ग्रहाणां सूर्यसंनिधौ । वक्रं गताः शुभाः श्रेष्ठाः क्रूराश्चातीव दारुणाः ॥"</em>
</div>

<p><strong>खगोलीय कारण:</strong> जब तेज गति वाली पृथ्वी धीमी गति वाले बाहरी ग्रह (मंगल, गुरु, शनि) को आंतरिक कक्षा से पार करती है, तो पृष्ठभूमि के तारों के सापेक्ष वह ग्रह उल्टा चलता प्रतीत होता है, इसे <strong>वक्री (Retrograde)</strong> कहते हैं।</p>

<div style="background:#f1f5f9; border-left:4px solid #b45309; padding:0.6rem; font-size:0.8rem; margin:0.6rem 0;">
  <strong>सूर्य से कोणीय दूरी की वक्री शर्तें:</strong><br>
  • मंगल: सूर्य से $१३७^\circ$ से $२२३^\circ$ पर वक्री<br>
  • गुरु: सूर्य से $११५^\circ$ से $२४५^\circ$ पर वक्री<br>
  • शनि: सूर्य से $१०९^\circ$ से $२५१^\circ$ पर वक्री<br>
  • बुध: सूर्य से अधिकतम $२०^\circ$ आगे होने पर वक्री<br>
  • शुक्र: सूर्य से अधिकतम $२९^\circ$ आगे होने पर वक्री
</div>

<div style="background:#f0fdf4; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>जातक 'क' कुण्डली परीक्षण:</strong> जातक की कुण्डली में शनि $८^\circ ३४'$ कुंभ में हैं और सूर्य $१०^\circ २५'$ तुला में हैं। अंतर $= ११८^\circ$ है, अतः <strong>शनि देव वक्री हैं</strong> (चेष्टा बल में पूर्ण बली)।
</div>
'''
    pages.append(make_page(23, "ग्रह गतिकी • Planetary Motion", "वक्री गति (Retrograde) की खगोलीय परिधि एवं शर्तें", p23))

    # Page 24: अस्त परिधि (Combustion)
    p24 = '''
<p>जब कोई ग्रह सूर्य के अत्यंत निकट आ जाता है, तो सूर्य के प्रखर प्रकाश में वह नग्न आंखों से दिखाई नहीं देता। इसे <strong>अस्त (Combustion)</strong> कहते हैं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">सामान्य अस्त परिधि</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">वक्री अवस्था में अस्त</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">फलित प्रभाव</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">चंद्रमा</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१२°</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">-</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">अमावस्या दोष, बलहीन।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">मंगल</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१७°</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">-</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">साहस में कमी, रक्त विकार।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">बुध</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१४°</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१२°</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">बुधादित्य योग में अस्त दोष न्यून।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">गुरु</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">११°</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">-</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">ज्ञान मंद, संतान विलंब।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">शुक्र</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१०°</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">८°</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">विवाह एवं सुख में कमी।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">शनि</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१५°</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">-</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कर्म में अत्यधिक संघर्ष।</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>जातक 'क' परीक्षण:</strong> सूर्य $१०^\circ २५'$ तुला पर है। बुध $२२^\circ २६'$ तुला पर ($१२^\circ ०१'$ अंतर - अस्त सीमा रेखा), शुक्र $१२^\circ ०७'$ तुला पर ($१^\circ ४२'$ अंतर - <strong>शुक्र अस्त</strong>)।
</div>
'''
    pages.append(make_page(24, "ग्रह गतिकी • Planetary Motion", "ग्रहों की अस्त परिधि (Combustion) गणितीय सीमाएं", p24))

    # Page 25: उपग्रह साधन: मांदी एवं गुलिक
    p25 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ गुलिक-मांदी साधनम् ॥</strong><br>
  <em>"दिनमानं भजेदष्टौ भागास्तेषां पृथक् पृथक् । शनैर्भागो भवेन्मन्दी गुलिकस्तत्सुतो मतः ॥"</em>
</div>

<p><strong>साधन विधि:</strong> दिनमान (अथवा रात्रिमान) को आठ बराबर भागों में विभाजित करें। दिन में वार-स्वामी के क्रम से और रात्रि में ५वें वार-स्वामी के क्रम से गणना की जाती है। शनि का भाग <strong>गुलिक/मांदी</strong> कहलाता है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">शुक्रवार (जातक 'क' का जन्म दिन) की रात्रि में गुलिक खंड:</strong><br>
  • शुक्रवार रात्रि क्रम: १. मंगल, २. सूर्य, ३. शुक्र, ४. बुध, ५. चंद्रमा, <strong>६. शनि (गुलिक)</strong>, ७. गुरु<br>
  • रात्रिमान $= ७२४.५\text{ मिनट}$। १ खंड $= ७२४.५ / ८ = ९०.५६\text{ मिनट}$<br>
  • गुलिक उदय काल $= सूर्यास्त + ५ \times ९०.५६ = १७:२१ + ०७:३३ = ००:५४ AM$<br>
  • उस समय उदित लग्न $= \mathbf{सिंह १४^\circ २२'}$ (द्वादश भाव में गुलिक स्पष्ट)।
</div>
'''
    pages.append(make_page(25, "उपग्रह साधन • Upagrahas", "मांदी एवं गुलिक उदय काल साधन गणित", p25))

    # Page 26: यमगण्ड एवं काल
    p26 = '''
<p>गुलिक के समान अन्य अप्रकाश उपग्रहों का साधन भी दिनमान/रात्रिमान के अष्टम भाग से किया जाता है:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">उपग्रह</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">स्वामी ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">तात्विक प्रभाव</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">जातक 'क' कुण्डली स्थिति</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>१. गुलिक / मांदी</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">शनि</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">अत्यंत विषैला, संचित कर्म कष्ट</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">द्वादश भाव (सिंह १४°)</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>२. यमगण्ड</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">गुरु</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कार्यों में अचानक विघ्न</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">तृतीय भाव (वृश्चिक २२°)</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>३. काल</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">सूर्य</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">पिता एवं राजभय</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">द्वितीय भाव (तुला २८°)</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>४. अर्धप्रहर</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">बुध</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">बुद्धि भ्रम, अस्थिरता</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">प्रथम भाव (कन्या १८°)</td></tr>
  </tbody>
</table>

<div style="background:#f1f5f9; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong>फलित सूत्र:</strong> जिस भाव में गुलिक बैठता है, उस भाव के फलों का हनन करता है। द्वादश में गुलिक जातक को वैराग्य, विदेश वास एवं साधना की ओर प्रेरित करता है।
</div>
'''
    pages.append(make_page(26, "उपग्रह साधन • Upagrahas", "यमगण्ड, काल, अर्धप्रहर एवं अष्टम भाग गणित", p26))

    # Page 27: धूमादि ५ अप्रकाश ग्रह
    p27 = '''
<p>महर्षि पराशर ने सूर्य स्पष्ट के आधार पर ५ गणितीय अप्रकाश ग्रहों का निरूपण किया है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 धूमादि ५ ग्रहों के सटीक बीजगणितीय सूत्र:</strong><br>
  १. धूम $= \text{सूर्य स्पष्ट} + १३३^\circ २०'$<br>
  २. व्यतीपात $= ३६०^\circ - \text{धूम}$<br>
  ३. परिवेष $= \text{व्यतीपात} + १८०^\circ$<br>
  ४. इंद्रधनुष $= ३६०^\circ - \text{परिवेष}$<br>
  ५. उपकेतु $= \text{इंद्रधनुष} + १६^\circ ४०'$ ($= \text{सूर्य} - ३०^\circ$)
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' पर प्रत्यक्ष गणना:</strong><br>
  • सूर्य $= १९०^\circ २५'$ (तुला १०° २५')<br>
  • <strong>धूम:</strong> $१९०^\circ २५' + १३३^\circ २०' = ३२३^\circ ४५'$ (कुंभ २३° ४५')<br>
  • <strong>व्यतीपात:</strong> $३६०^\circ - ३२३^\circ ४५' = ३६^\circ १५'$ (वृषभ ६° १५')<br>
  • <strong>परिवेष:</strong> $३६^\circ १५' + १८०^\circ = २१६^\circ १५'$ (वृश्चिक ६° १५')<br>
  • <strong>इंद्रधनुष:</strong> $३६०^\circ - २१६^\circ १५' = १४३^\circ ४५'$ (सिंह २३° ४५')<br>
  • <strong>उपकेतु:</strong> $१४३^\circ ४५' + १६^\circ ४०' = १६०^\circ २५'$ (कन्या १०° २५')
</div>
'''
    pages.append(make_page(27, "उपग्रह साधन • Upagrahas", "धूमादि ५ अप्रकाश ग्रहों के गणितीय समीकरण", p27))

    # Page 28: जातक 'क' ग्रह गतिकी समरी
    p28 = '''
<p>जातक 'क' के जन्मकालीन समस्त ९ मुख्य ग्रहों एवं उपग्रहों की गतिकी, वक्रता एवं अंश तालिका:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.35rem; border:1px solid #334155;">ग्रह</th>
      <th style="padding:0.35rem; border:1px solid #334155;">राशि</th>
      <th style="padding:0.35rem; border:1px solid #334155;">अंश स्पष्ट</th>
      <th style="padding:0.35rem; border:1px solid #334155;">नक्षत्र (चरण)</th>
      <th style="padding:0.35rem; border:1px solid #334155;">गति / अवस्था</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">सूर्य</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१०° २५' ३६''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">स्वाति (२)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">नीच, प्रत्यक्ष</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;">चंद्रमा</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कर्क</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१६° ३७' १२''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पुष्य (४)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">स्वक्षेत्री, पक्षबली</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">मंगल</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सिंह</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१° ४१' ०५''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पूर्वाफाल्गुनी (३)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मित्रक्षेत्री</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;">बुध</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२२° २६' ४०''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">विशाखा (१)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मित्रक्षेत्री</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">गुरु</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">वृश्चिक</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२४° ०९' ५०''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">ज्येष्ठा (३)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मित्रक्षेत्री</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;">शुक्र</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१२° ०७' १८''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">स्वाति (२)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">स्वक्षेत्री (मूलत्रिकोण), अस्त</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">शनि</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कुंभ</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">०८° ३४' १२''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शतभिषा (१)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>स्वक्षेत्री, वक्री</strong></td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;">राहु (मध्य)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१° ०१' ३०''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">विशाखा (१)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सदा वक्री</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">केतु (मध्य)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मेष</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१° ०१' ३०''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">भरणी (३)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सदा वक्री</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.5rem; font-size:0.8rem;">
  <strong>खंड १ संपूर्ण:</strong> अब समस्त खगोलीय, लग्न एवं ग्रह स्पष्ट मान सिद्ध हो चुके हैं। अगले खंड में हम पंचांग एवं दशा का गणित सिद्ध करेंगे।
</div>
'''
    pages.append(make_page(28, "केस स्टडी • Case Study", "जातक 'क' की संपूर्ण ग्रह स्पष्ट एवं गतिकी तालिका", p28))

    return pages

# Update get_pages_part1 to call append
_orig_part1 = get_pages_part1
def get_pages_part1():
    pages = _orig_part1()
    return append_pages_13_to_28(pages)
