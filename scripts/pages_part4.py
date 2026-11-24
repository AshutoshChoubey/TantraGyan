#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 4: Pages 85 to 108 of the 108-page Vedic Kundali Ganita Vichar Mahagranth.
Covers: Jaimini Chara Karakas, Bhrigu Nandi Nadi (BNN), Transits & Sade Sati, Kundali Milan (36 Gunas), 15-Step Pipeline & Conclusion.
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

def get_pages_part4():
    pages = []

    # Page 85: जैमिनी ज्योतिष एवं दृष्टि सूत्र
    p85 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ जैमिनिसूत्रे राशिदृष्टिः ॥</strong><br>
  <em>"चराः स्थिरान् पश्यन्ति मुक्त्वा पार्श्वस्थम् । स्थिराश्चरान् तथैव च । द्विस्वभावाः परस्परम् ॥"</em>
</div>

<p><strong>जैमिनी ज्योतिष का मूल आधार:</strong> पराशरी ज्योतिष में ग्रह दृष्टि (Planetary Aspects) प्रधान है, जबकि महर्षि जैमिनी ने <strong>राशि दृष्टि (Sign Aspects)</strong> को प्रधानता दी है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 जैमिनी राशि दृष्टि के ३ अचूक नियम:</strong><br>
  १. <strong>चर राशियां (१, ४, ७, १०):</strong> अपने निकटवर्ती स्थिर को छोड़कर शेष तीनों स्थिर राशियों (२, ५, ८, ११) को पूर्ण दृष्टि से देखती हैं।<br>
  २. <strong>स्थिर राशियां (२, ५, ८, ११):</strong> अपने निकटवर्ती चर को छोड़कर शेष तीनों चर राशियों को देखती हैं।<br>
  ३. <strong>द्विस्वभाव राशियां (३, ६, ९, १२):</strong> परस्पर एक दूसरे को पूर्ण दृष्टि से देखती हैं।
</div>
'''
    p85 += get_jaimini_ladder_svg()

    pages.append(make_page(85, "जैमिनी सूत्र • Jaimini", "जैमिनी ज्योतिष के मूल सिद्धांत एवं राशि दृष्टि सूत्र", p85))

    # Page 86: ७ चर कारक साधन
    p86 = '''
<p>राहु और केतु को छोड़कर शेष ७ ग्रहों के अंशों को अवरोही क्रम (Descending Order: ३०° से ०°) में व्यवस्थित करने पर <strong>७ चर कारक (Chara Karakas)</strong> प्राप्त होते हैं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">कारक</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">अंश वरीयता</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">कारकत्व विषय</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>१. आत्मकारक (AK)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">सर्वोच्च अंश (२९° - २२°)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">आत्मा, जीवन का अंतिम लक्ष्य, मुक्ति।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>२. अमात्यकारक (AmK)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">द्वितीय सर्वोच्च अंश</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">करियर, बुद्धि, कर्म, आजीविका।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>३. भ्रातृकारक (BK)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">तृतीय अंश</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">भाई-बहन, सहकर्मी, गुरु, मित्र।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>४. मातृकारक (MK)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">चतुर्थ अंश</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">माता, आंतरिक सुख, गृह, वाहन।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>५. पितृकारक (PiK)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">पंचम अंश</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">पिता, पूर्वज, धर्म, परंपरा।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>६. ज्ञातिरक (GK)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">षष्ठ अंश</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">शत्रु, रोग, विवाद, प्रतिस्पर्धा।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>७. दारकारक (DK)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">न्यूनतम अंश</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">जीवनसाथी, व्यापार साझेदार, विवाह।</td></tr>
  </tbody>
</table>
'''
    pages.append(make_page(86, "जैमिनी सूत्र • Jaimini", "७ चर कारक साधन विधि: अंशों का अवरोही क्रम", p86))

    # Page 87: आत्मकारक एवं कारकांश
    p87 = '''
<p>कुण्डली में जो ग्रह सर्वाधिक अंशों पर होता है, वह <strong>आत्मकारक (Atmakaraka - AK)</strong> कहलाता है:</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>कारकांश लग्न (Karakamsha Lagna):</strong><br>
  आत्मकारक ग्रह नवांश कुण्डली (D9) में जिस राशि में स्थित होता है, उस राशि को लग्न बनाकर जो कुण्डली बनती है, उसे <strong>कारकांश कुण्डली</strong> कहते हैं। यह आत्मा के मोक्ष एवं आध्यात्मिक अभिरुचियों का दर्पण है।
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong style="color:#854d0e;">जातक 'क' कुण्डली में आत्मकारक:</strong><br>
  • ग्रहों के अंश: <strong>गुरु: २४° ०९'</strong>, बुध: २२° २६', मंगल: २१° ४१', चंद्र: १६° ३७', शुक्र: १२° ०७', सूर्य: १०° २५', शनि: ०८° ३४'।<br>
  • <strong>आत्मकारक (AK) = देवगुरु बृहस्पति (Jupiter)</strong>।<br>
  • गुरु नवांश (D9) में <strong>कर्क राशि (उच्च)</strong> में हैं ➔ <strong>कारकांश लग्न = कर्क</strong>।<br>
  • <em>फल:</em> आत्मा का मूल स्वभाव अध्यात्म, वेदांत, ग्रंथ-रचना एवं ज्ञान का प्रसार है।
</div>
'''
    pages.append(make_page(87, "जैमिनी सूत्र • Jaimini", "आत्मकारक (AK) एवं कारकांश लग्न का रहस्य", p87))

    # Page 88: आरूढ़ पद एवं उपपद लग्न
    p88 = '''
<p>भाव से भावेश जितनी दूरी पर बैठा हो, भावेश से उतनी ही दूरी आगे चलने पर प्राप्त राशि को <strong>आरूढ़ पद (Arudha Pada)</strong> कहते हैं:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 आरूढ़ पद प्रक्षेपण सूत्र:</strong><br>
  आरूढ़ पद = (भावेश की राशि + भावेश की दूरी - १) को १२ से भाग देने पर प्राप्त शेष राशि<br>
  • <strong>अपवाद नियम:</strong> यदि पद उसी भाव में या ७वें भाव में पड़े, तो १०वां भाव पद माना जाता है।<br>
  • <strong>आरूढ़ लग्न (AL):</strong> प्रथम भाव का पद (संसार में जातक की सामाजिक छवि)।<br>
  • <strong>उपपद लग्न (UL):</strong> द्वादश भाव का पद (वैवाहिक जीवन का वास्तविक यथार्थ)।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' का आरूढ़ लग्न (AL):</strong><br>
  • लग्न: कन्या (६)। लग्नेश बुध द्वितीय भाव (तुला - ७) में है (दूरी = २ भाव)।<br>
  • तुला से २ भाव आगे = वृश्चिक (८)। अतः <strong>आरूढ़ लग्न (AL) = वृश्चिक</strong>।
</div>
'''
    pages.append(make_page(88, "जैमिनी सूत्र • Jaimini", "आरूढ़ पद (AL) एवं उपपद लग्न (UL) प्रक्षेपण सूत्र", p88))

    # Page 89: भृगु नंदी नाड़ी (BNN) ४ दिशा त्रिकोण
    p89 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ भृगु नंदी नाड़ी दिशा दर्शनम् ॥</strong><br>
  <em>"पूर्वे धर्मो भवेत् ज्ञातो दक्षिणे चार्थसंज्ञकः । पश्चिमे काम इत्युक्त उत्तरे मोक्ष उच्यते ॥"</em>
</div>

<p>भृगु नंदी नाड़ी (BNN) में १२ राशियों को ४ दिशा त्रिकोणों में विभाजित किया गया है। एक ही त्रिकोण की राशियां परस्पर १००\% युत मानी जाती हैं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">दिशा</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">त्रिकोण राशियां</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">जीवन पुरुषार्थ</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">कारकत्व</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>पूर्व (East)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">मेष (१), सिंह (५), धनु (९)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">धर्म त्रिकोण (Dharma)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कर्तव्य, आत्मा, पिता, मान-सम्मान।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>दक्षिण (South)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">वृषभ (२), कन्या (६), मकर (१०)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">अर्थ त्रिकोण (Artha)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">धन, व्यवसाय, नौकरी, भौतिक संपदा।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>पश्चिम (West)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">मिथुन (३), तुला (७), कुंभ (११)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">काम त्रिकोण (Kama)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">इच्छाएं, मित्र, सामाजिक संबंध, यात्रा।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>उत्तर (North)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कर्क (४), वृश्चिक (८), मीन (१२)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">मोक्ष त्रिकोण (Moksha)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">आध्यात्म, साधना, गुप्त विद्याएं, मुक्ति।</td></tr>
  </tbody>
</table>
'''
    pages.append(make_page(89, "भृगु नंदी नाड़ी • BNN", "भृगु नंदी नाड़ी (BNN): ४ दिशा त्रिकोण दर्शन", p89))

    # Page 90: नाड़ी दृष्टि सूत्र
    p90 = '''
<p>BNN में ग्रहों का आपसी संबंध पारंपरिक पराशरी दृष्टियों के स्थान पर <strong>दिशिक एवं कोणीय त्रिकोणों</strong> से देखा जाता है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 BNN के ४ प्राथमिक दृष्टि संबंध:</strong><br>
  १. <strong>१-५-९ संबंध (समान दिशा):</strong> एक ही त्रिकोण में बैठे ग्रह १००% युति में होते हैं।<br>
  २. <strong>२-१२ संबंध (अग्र-पश्चात्):</strong> २रा ग्रह अगले कदम पर तथा १२वां ग्रह पीछे से प्रभाव डालता है।<br>
  ३. <strong>३-७-११ संबंध (पूरक दिशा):</strong> ७वां ग्रह प्रत्यक्ष सम्मुख तथा ३-११ परस्पर सहायक होते हैं।<br>
  ४. <strong>वक्री ग्रह का प्रभाव:</strong> वक्री ग्रह अपने पिछले भाव से भी पूर्ण सक्रिय रहता है।
</div>
'''
    pages.append(make_page(90, "भृगु नंदी नाड़ी • BNN", "नाड़ी दृष्टि सूत्र: १-५-९, २-१२ एवं ३-७-११ संयोजन", p90))

    # Page 91: कर्माधिपति शनि एवं जीवकारक गुरु
    p91 = '''
<p>भृगु नंदी नाड़ी में दो ग्रह संपूर्ण मानव जीवन के धुरी हैं:</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>१. जीवकारक गुरु (Jupiter = Soul / Life):</strong><br>
  गुरु स्वयं जातक की जीवन शक्ति, प्राण एवं चेतना है। गुरु जिस दिशा में बैठे और उसके १-५-९ में जो ग्रह हों, जातक का जीवन उन्हीं ऊर्जाओं से संचालित होता है।<br><br>
  <strong>२. कर्माधिपति शनि (Saturn = Profession / Karma):</strong><br>
  शनि मनुष्य का कर्म है। शनि जिस राशि में हो और उसके २-१२, १-५-९ में जो ग्रह हों, वही जातक की वास्तविक आजीविका और प्रारब्ध कर्म निर्धारित करते हैं।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' पर नाड़ी योग:</strong><br>
  • <strong>गुरु (उत्तर - जल त्रिकोण / वृश्चिक):</strong> इसके त्रिकोण (कर्क) में <strong>चंद्रमा</strong> स्थित है ➔ <strong>गुरु + चंद्र नाड़ी योग</strong> (अत्यंत पवित्र हृदय, ज्ञान का प्रकाशक)।<br>
  • <strong>शनि (पश्चिम - वायु त्रिकोण / कुंभ):</strong> इसके त्रिकोण (तुला) में <strong>बुध, शुक्र, राहु</strong> स्थित हैं ➔ <strong>शनि + बुध + शुक्र योग</strong> (तकनीकी, लेखन, कला एवं बड़े बौद्धिक प्रोजेक्ट्स का स्वामी)।
</div>
'''
    pages.append(make_page(91, "भृगु नंदी नाड़ी • BNN", "कर्माधिपति शनि एवं जीवकारक गुरु का नाड़ी संयोजन", p91))

    # Page 92: जातक 'क' जैमिनी व BNN समरी
    p92 = '''
<p>जातक 'क' की कुण्डली के समस्त जैमिनी चर कारक एवं BNN नाड़ी दिशा तालिका:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.35rem; border:1px solid #334155;">चर कारक</th>
      <th style="padding:0.35rem; border:1px solid #334155;">ग्रह</th>
      <th style="padding:0.35rem; border:1px solid #334155;">अंश स्पष्ट</th>
      <th style="padding:0.35rem; border:1px solid #334155;">BNN दिशा</th>
      <th style="padding:0.35rem; border:1px solid #334155;">फलित प्रभाव</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>आत्मकारक (AK)</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">गुरु</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२४° ०९' ५०''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">उत्तर (मोक्ष)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">आध्यात्मिक नेतृत्व, शोध।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>अमात्यकारक (AmK)</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">बुध</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२२° २६' ४०''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पश्चिम (काम)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">वाणिज्य, कोडिंग, लेखन।</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>भ्रातृकारक (BK)</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मंगल</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">२१° ४१' ०५''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पूर्व (धर्म)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">साहस, ऊर्जा, पराक्रम।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>मातृकारक (MK)</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">चंद्रमा</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१६° ३७' १२''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">उत्तर (मोक्ष)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मातृ कृपा, मानसिक शांति।</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>पितृकारक (PiK)</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शुक्र</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१२° ०७' १८''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पश्चिम (काम)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कला, संस्कृति, वैभव।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>ज्ञातिरक (GK)</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सूर्य</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">१०° २५' ३६''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पश्चिम (काम)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">प्रतिस्पर्धा विजय।</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>दारकारक (DK)</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शनि</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">०८° ३४' १२''</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पश्चिम (काम)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">स्थिर एवं गंभीर जीवनसाथी।</td></tr>
  </tbody>
</table>
'''
    pages.append(make_page(92, "केस स्टडी • Case Study", "जातक 'क' के चर कारक एवं BNN तालिका", p92))

    # Pages 93 to 98: गोचर वेधशाला एवं साढ़े साती
    p93 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ गोचर विचार रहस्यम् ॥</strong><br>
  <em>"जन्मराशेस्तु ये भावाः शुभाशुभा फलप्रदाः । गोचरेण परीक्षेत देशकालविभागतः ॥"</em>
</div>

<p><strong>सिद्धांत:</strong> जन्म कुण्डली जन्म समय का स्थिर बीज है, जबकि <strong>गोचर (Transit)</strong> वर्तमान में चल रहा ऋतु चक्र है। जब तक गोचर अनुकूल न हो, जन्मकालीन दशा का फल फलीभूत नहीं हो सकता। गोचर सदा <strong>जन्मकालीन चंद्र राशि</strong> से देखा जाता है।</p>
'''
    p93 += get_bnn_trines_svg()

    pages.append(make_page(93, "गोचर वेधशाला • Transits", "गोचर का शास्त्रीय सिद्धांत: चंद्र लग्न से भ्रमण", p93))

    # Page 94: गोचर वेध एवं विपरीत वेध
    p94 = '''
<p>जब कोई ग्रह शुभ स्थान में गोचर करता है, परंतु किसी अन्य भाव में कोई ग्रह बैठा हो, तो वह शुभ फल में बाधा डालता है; इसे <strong>वेध (Vedha)</strong> कहते हैं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">शुभ गोचर स्थान (चंद्र से)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">वेध (बाधा) स्थान</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">सूर्य</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">३, ६, १०, ११</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">क्रमशः ९, १२, ४, ५</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">चंद्रमा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१, ३, ६, ७, १०, ११</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">क्रमशः ५, ९, १२, २, ४, ८</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">गुरु</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">२, ५, ७, ९, ११</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">क्रमशः १२, ४, ३, १०, ८</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">शनि</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">३, ६, ११</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">क्रमशः १२, ९, ५</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>अपवाद:</strong> पिता-पुत्र में वेध नहीं होता (सूर्य और शनि, तथा चंद्र और बुध आपस में वेध नहीं करते)।
</div>
'''
    pages.append(make_page(94, "गोचर वेधशाला • Transits", "गोचर वेध एवं विपरीत वेध चक्र सूत्र", p94))

    # Page 95: दोहरा गोचर सिद्धांत (Double Transit)
    p95 = '''
<p>किसी भी महत्वपूर्ण जीवन घटना (विवाह, संतान, पदोन्नति, गृह निर्माण) के घटित होने के लिए <strong>गुरु एवं शनि का संयुक्त गोचर प्रभाव</strong> अनिवार्य है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 दोहरे गोचर का नियम (Double Transit Theorem):</strong><br>
  १. <strong>शनि देव (संसाधन एवं कर्म):</strong> अपनी स्थिति या दृष्टि से संबंधित भाव/भावेश को संचित करते हैं।<br>
  २. <strong>देवगुरु बृहस्पति (कृपा एवं विस्तार):</strong> अपनी स्थिति या दृष्टि से उस भाव को आशीर्वाद देकर घटना को मूर्त रूप प्रदान करते हैं।<br>
  ३. जब शनि और गुरु दोनों एक साथ किसी एक भाव या भावेश को प्रभावित करते हैं, तो उस भाव का फल अवश्य घटित होता है।
</div>
'''
    pages.append(make_page(95, "गोचर वेधशाला • Transits", "दोहरा गोचर सिद्धांत: गुरु व शनि का संयुक्त प्रभाव", p95))

    # Page 96: शनि साढ़े साती के ३ चरण
    p96 = '''
<p>जब शनि देव जन्मकालीन चंद्रमा से १२वें, प्रथम (चंद्र राशि) अथवा द्वितीय भाव में गोचर करते हैं, तो इसे <strong>शनि साढ़े साती (७.५ वर्ष)</strong> कहते हैं:</p>

<div style="background:#f1f5f9; border-left:4px solid #b45309; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>साढ़े साती के ३ चरण (४५° कक्षा):</strong><br>
  • <strong>प्रथम चरण (१२वां भाव):</strong> मानसिक चिंता, व्यर्थ व्यय, अनिद्रा, सिर पर प्रभाव।<br>
  • <strong>द्वितीय चरण (जन्म चंद्र पर):</strong> शारीरिक कष्ट, कार्य में अत्यधिक संघर्ष, हृदय/छाती पर प्रभाव।<br>
  • <strong>तृतीय चरण (द्वितीय भाव):</strong> आर्थिक दबाव, पारिवारिक मतभेद, वाणी पर प्रभाव, पैर से प्रस्थान।
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong>शनि की ढैय्या (२.५ वर्ष):</strong> चंद्र राशि से चौथे (कंटक शनि) या आठवें (अष्टम शनि) भाव में शनि का गोचर ढैय्या कहलाता है।
</div>
'''
    pages.append(make_page(96, "गोचर वेधशाला • Transits", "शनि साढ़े साती: ३ चरण (४५° कक्षा) एवं ढैय्या", p96))

    # Page 97: साढ़े साती फल कथन के अपवाद
    p97 = '''
<p>साढ़े साती सदा कष्टकारी नहीं होती। इसके ५ शास्त्रीय शुभ अपवाद:</p>

<ol style="font-size:0.8rem; line-height:1.6; padding-left:1.2rem;">
  <li><strong>स्वक्षेत्री अथवा उच्च शनि:</strong> यदि शनि मकर, कुंभ या तुला राशि में हो, तो साढ़े साती में जातक को महान पद एवं सत्ता मिलती है।</li>
  <li><strong>चंद्रमा की स्थिति:</strong> यदि जन्म कुण्डली में चंद्रमा स्वक्षेत्री (कर्क) या उच्च (वृषभ) हो, तो शनि का नकारात्मक प्रभाव न्यूनतम हो जाता है।</li>
  <li><strong>अष्टकवर्ग बिंदु:</strong> यदि गोचरस्थ राशि में शनि के BAV में ४ या अधिक बिंदु हों, और SAV में ३०+ बिंदु हों, तो साढ़े साती वरदान सिद्ध होती है।</li>
  <li><strong>लग्नेश मित्रता:</strong> वृषभ, तुला, मकर, कुंभ लग्नों के लिए शनि परम मित्र हैं, अतः शुभ फल देते हैं।</li>
</ol>
'''
    p97 += get_sade_sati_wave_svg()

    pages.append(make_page(97, "गोचर वेधशाला • Transits", "साढ़े साती फल कथन के शास्त्रीय अपवाद एवं नियम", p97))

    # Page 98: जातक 'क' वर्तमान गोचर विश्लेषण
    p98 = '''
<p>जातक 'क' का वर्तमान गोचर एवं साढ़े साती विश्लेषण:</p>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.7rem; font-size:0.82rem;">
  <strong style="color:#166534;">जातक 'क' गोचर स्थिति:</strong><br>
  • जन्म चंद्र: <strong>कर्क राशि</strong><br>
  • वर्तमान में शनि कुंभ राशि (कर्क से अष्टम भाव) में गोचररत हैं ➔ <strong>अष्टम शनि ढैय्या</strong>।<br>
  • <strong>कवच एवं सुरक्षा:</strong> जन्म कुण्डली में शनि कुंभ में स्वक्षेत्री (३४ SAV बिंदु) हैं। जातक पर वर्तमान में <strong>भाग्येश शुक्र की महादशा</strong> चल रही है। अतः यह ढैय्या कष्ट देने के स्थान पर गहन आध्यात्मिक शोध, ग्रंथ-रचना एवं दीर्घकालिक ज्ञान की सिद्धि करा रही है।
</div>
'''
    pages.append(make_page(98, "केस स्टडी • Case Study", "जातक 'क' का वर्तमान गोचर एवं ढैय्या विश्लेषण", p98))

    # Pages 99 to 104: वैवाहिक मिलान एवं ३६ गुण
    p99 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ वैवाहिक ज्योतिष आधार ॥</strong><br>
  <em>"सप्तमं जायास्थानं कलत्रं काममेव च । शुक्राद्गुरुमुखाद्वापि विचार्यं यत्नतो बुधैः ॥"</em>
</div>

<p>विवाह सुख के ४ अनिवार्य आधार स्तंभ: (१) सप्तम भाव एवं भावेश, (२) नैसर्गिक कारक शुक्र (पुरुष हेतु) एवं गुरु (स्त्री हेतु), (३) नवमांश कुण्डली (D9), तथा (४) अष्टकूट मिलान (३६ गुण)।</p>
'''
    pages.append(make_page(99, "विवाह मिलान • Matrimony", "वैवाहिक ज्योतिष के ४ स्तंभ: सप्तम, शुक्र एवं गुरु", p99))

    # Page 100: मांगलिक विचार एवं १६ परिहार
    p100 = '''
<p>जब मंगल १, ४, ७, ८ अथवा १२वें भाव में स्थित हो, तो <strong>मांगलिक दोष (Kuja Dosha)</strong> कहलाता है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">शास्त्रीय परिहार नियम (Cancellations):</strong><br>
  १. यदि वर और कन्या दोनों की कुण्डली में समान भाव में मंगल या कोई पापी ग्रह हो, तो दोष स्वतः नष्ट होता है।<br>
  २. मेष का मंगल लग्न में, वृश्चिक का चतुर्थ में, मकर का सप्तम में, कुंभ का अष्टम में, धनु का द्वादश में दोष नहीं बनाता।<br>
  ३. गुरु की दृष्टि मंगल पर होने से मांगलिक दोष पूर्णतः निष्प्रभावी हो जाता है।
</div>
'''
    pages.append(make_page(100, "विवाह मिलान • Matrimony", "मांगलिक विचार: परिभाषा एवं १६ शास्त्रीय परिहार", p100))

    # Page 101: अष्टकूट मिलान १: कूट १-४
    p101 = '''
<p>वर-वधू के चंद्र नक्षत्र एवं राशि के आधार पर ३६ गुणों का विभाजन:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">कूट नाम</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">अधिकतम अंक</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">परीक्षण आधार</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">तात्विक विचार</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>१. वर्ण (Varna)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">राशि अनुसार ४ वर्ण</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">अहंकार, कार्यशैली, सामाजिक सामंजस्य।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>२. वश्य (Vashya)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">२</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">मानव, जलचर, चतुष्पाद...</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">परस्पर आकर्षण, नियंत्रण, आज्ञाकारिता।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>३. तारा (Tara)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">९ तारा चक्र (जन्म, संपत...)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">भाग्य वृद्धि, स्वास्थ्य, आयु सुरक्षा।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>४. योनि (Yoni)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">१४ पशु प्रतीक</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">शारीरिक एवं दांपत्य रति सामंजस्य।</td></tr>
  </tbody>
</table>
'''
    p101 += get_ashtakoot_gauge_svg()

    pages.append(make_page(101, "विवाह मिलान • Matrimony", "अष्टकूट मिलान १: वर्ण, वश्य, तारा एवं योनि कूट", p101))

    # Page 102: अष्टकूट मिलान २: कूट ५-८
    p102 = '''
<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">कूट नाम</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">अधिकतम अंक</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">परीक्षण आधार</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">तात्विक विचार</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>५. ग्रहमैत्री</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">चंद्र राशि स्वामियों की मित्रता</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">मानसिक विचार, दृष्टिकोण, जीवन मूल्य।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>६. गण (Gana)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">६</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">देव, मनुष्य, राक्षस</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">स्वभाव, आदतें, जीवनशैली की संगतता।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>७. भकूट (Bhakoot)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">७</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">राशियों की परस्पर दूरी (२-१२, ६-८)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">वंश वृद्धि, आर्थिक समृद्धि, दीर्घायु।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>८. नाड़ी (Nadi)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;"><strong>८</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">आदि, मध्य, अंत्य (त्रिदोष)</td><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>आनुवंशिकी (Genetics), संतान आरोग्य, जीवन।</strong></td></tr>
  </tbody>
</table>
<div style="text-align:center; font-weight:bold; font-size:0.9rem; margin-top:0.4rem;">
  कुल योग = १ + २ + ३ + ४ + ५ + ६ + ७ + ८ = ३६ गुण (१८+ शुभ, २४+ उत्तम)
</div>
'''
    pages.append(make_page(102, "विवाह मिलान • Matrimony", "अष्टकूट मिलान २: ग्रहमैत्री, गण, भकूट एवं नाड़ी", p102))

    # Page 103: नाड़ी एवं भकूट दोष परिहार
    p103 = '''
<p>नाड़ी दोष (८ अंक) एवं भकूट दोष (७ अंक) के प्रामाणिक शास्त्रीय परिहार:</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>नाड़ी दोष परिहार (BPHS नियम):</strong><br>
  १. यदि वर-वधू का नक्षत्र एक हो परंतु <strong>चरण भिन्न</strong> हों, तो नाड़ी दोष नहीं लगता।<br>
  २. यदि नक्षत्र भिन्न हों परंतु राशि एक हो, तो दोष नष्ट हो जाता है।<br>
  ३. यदि राशि भिन्न हो परंतु नक्षत्र एक हो, तो दोष भंग होता है।<br>
  ४. रोहिणी, मृगशिरा, आर्द्रा, पुष्य, विशाखा, श्रवण, उत्तराभाद्रपद में नाड़ी दोष मान्य नहीं।
</div>
'''
    pages.append(make_page(103, "विवाह मिलान • Matrimony", "नाड़ी दोष एवं भकूट दोष के शास्त्रीय परिहार नियम", p103))

    # Page 104: संपूर्ण मेलापक मूल्यांकन
    p104 = '''
<p>विवाह निर्णय के लिए समग्र मूल्यांकन चेकलिस्ट:</p>

<ol style="font-size:0.8rem; line-height:1.6; padding-left:1.2rem;">
  <li><strong>आयु एवं स्वास्थ्य (प्रथम व अष्टम भाव):</strong> दोनों की कुण्डली में दीर्घायु योग हो।</li>
  <li><strong>चरित्र एवं मन (चंद्रमा व लग्न):</strong> मानसिक स्थिरता एवं परस्पर सम्मान।</li>
  <li><strong>गुण मिलान (अष्टकूट):</strong> कम से कम १८ गुण मिलें, नाड़ी दोष का परिहार हो।</li>
  <li><strong>दशा सामंजस्य:</strong> विवाह के समय दोनों की अनुकूल महादशा-अंतर्दशा चल रही हो।</li>
  <li><strong>सप्तमेश व शुक्र/गुरु स्थिति:</strong> वैवाहिक सुख के कारक ग्रह पाप-कर्तरी में न हों।</li>
</ol>
'''
    pages.append(make_page(104, "विवाह मिलान • Matrimony", "संपूर्ण मेलापक मूल्यांकन एवं विवाह निर्णय चेकलिस्ट", p104))

    # Pages 105 to 108: महा-पाइपलाइन एवं उपसंहार
    p105 = '''
<div style="background:#0f172a; color:#f8fafc; padding:0.8rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong style="color:#38bdf8;">🌟 १५-चरणीय संपूर्ण कुण्डली विवेचन महा-पाइपलाइन:</strong><br>
  १. पंचांग शुद्धि ➔ २. लग्न व लग्नेश बल ➔ ३. चंद्र राशि व मन ➔ ४. सूर्य व आत्मा ➔<br>
  ५. भाव स्पष्ट ➔ ६. षोडशवर्ग (D9, D10) ➔ ७. षड्बल मापन ➔ ८. अष्टकवर्ग (SAV) ➔<br>
  ९. पराशरी राजयोग ➔ १०. जैमिनी चर कारक ➔ ११. भृगु नंदी नाड़ी ➔ १२. विंशोत्तरी दशा ➔<br>
  १३. गोचर वेध ➔ १४. अरिष्ट भंग ➔ <strong>१५. सात्विक समाधान।</strong>
</div>
'''
    p105 += get_pipeline_flow_svg()

    pages.append(make_page(105, "महा-पाइपलाइन • Synthesis", "१५-चरणीय संपूर्ण कुण्डली विवेचन महा-पाइपलाइन", p105))

    # Page 106: जातक 'क' समग्र कुण्डली विवेचन
    p106 = '''
<p>जातक 'क' की समग्र कुण्डली का सर्वांगीण फलादेश संश्लेषण:</p>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.7rem; font-size:0.82rem;">
  <strong style="color:#166534;">जातक 'क' समग्र फलित सारांश:</strong><br>
  • <strong>व्यक्तित्व:</strong> कन्या लग्न (बुध) एवं कर्क चंद्र (पुष्य) से युक्त जातक असाधारण रूप से तीव्र बुद्धि, प्रखर स्मरण शक्ति, एवं परोपकारी स्वभाव का धनी है।<br>
  • <strong>आजीविका:</strong> दशमेश बुध का द्वितीय में भाग्येश शुक्र के साथ बैठना और D10 में स्वक्षेत्री होना जातक को उच्च बौद्धिक, कोडिंग, लेखन, एवं प्राचीन विज्ञान के पुनर्निर्माण में वैश्विक ख्याति दिलाता है।<br>
  • <strong>दशा प्रभाव:</strong> वर्तमान २०-वर्षीय शुक्र महादशा जीवन में स्थाई संपदा, मान-सम्मान एवं महान ग्रंथों की रचना करा रही है।
</div>
'''
    pages.append(make_page(106, "केस स्टडी • Case Study", "जातक 'क' की समग्र कुण्डली का सर्वांगीण फलादेश", p106))

    # Page 107: सात्विक समाधान एवं साधना
    p107 = '''
<p>वैदिक ज्योतिष भय दिखाने का व्यवसाय नहीं, आत्म-चेतना को जगाने का पावन दीप है। सात्विक समाधान के ३ स्तंभ:</p>

<ol style="font-size:0.82rem; line-height:1.6; padding-left:1.2rem;">
  <li><strong>मंत्र साधना (ध्वनि ऊर्जा):</strong> इष्टदेव का नित्य गायत्री अथवा बीज मंत्र जप।</li>
  <li><strong>दान एवं सेवा (कर्म शुद्धि):</strong> पीड़ित ग्रह से संबंधित वस्तुओं का निष्काम भाव से दान।</li>
  <li><strong>रत्न एवं वनस्पति (प्रकाश ऊर्जा):</strong> केवल योगकारक एवं शुभ भावेशों के शुद्ध रत्न धारण।</li>
</ol>
'''
    pages.append(make_page(107, "साधना एवं समाधान • Remedies", "सात्विक समाधान, मंत्र विज्ञान एवं रत्न परामर्श", p107))

    # Page 108: प्रशस्ति एवं ग्रंथ समाप्ति
    p108 = '''
<div style="text-align:center; padding:1.2rem 0.5rem;">
  <div style="font-size:1.1rem; font-weight:800; color:#854d0e; margin-bottom:0.5rem;">॥ श्री कृष्णार्पणमस्तु • ॐ तत्सत् ॥</div>
  <p style="font-size:0.85rem; line-height:1.7; color:#334155;">
    इस प्रकार <strong>वैदिक कुण्डली विचार एवं गणित महाग्रंथ</strong> के समस्त १०८ पवित्र पृष्ठ पूर्ण हुए। यह ग्रंथ ब्रह्मांड के खगोलीय गणित, ऋषि पराशर के अमर सूत्रों, और आधुनिक काल-गणना का एक अभेद्य सेतु है। साधक एवं शोधार्थी इस ग्रंथ के प्रकाश में काल के रहस्यों का साक्षात्कार करें।
  </p>

  <div style="background:#f1f5f9; border-radius:8px; padding:0.8rem; margin:1rem auto; max-width:400px; font-size:0.78rem; text-align:left;">
    <strong>ग्रंथ संदर्भ एवं प्रमाण ग्रंथ सूची:</strong><br>
    १. बृहत्पाराशरहोराशास्त्रम् (महर्षि पराशर)<br>
    २. सूर्यसिद्धांत (मय दानव / सौर परंपरा)<br>
    ३. सारावली (कल्याण वर्मा)<br>
    ४. फलदीपिका (मंत्रेश्वर)<br>
    ५. जातक पारिजात (वैद्यनाथ दीक्षित)<br>
    ६. जैमिनी उपदेश सूत्र (महर्षि जैमिनी)
  </div>

  <div style="font-size:0.78rem; color:#64748b; margin-top:1rem;">
    <strong>तंत्र ज्ञान शोध संस्थान</strong> • आधिकारिक प्रकाशन • https://t.worldgyan.com
  </div>
</div>
'''
    pages.append(make_page(108, "अंतिम पृष्ठ • Colophon", "प्रशस्ति, शास्त्रीय संदर्भ ग्रंथ सूची एवं ग्रंथ समाप्ति", p108))

    return pages

print("Part 4 defined")
