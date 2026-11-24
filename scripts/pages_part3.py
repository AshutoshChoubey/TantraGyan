#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 3: Pages 55 to 84 of the 108-page Vedic Kundali Ganita Vichar Mahagranth.
Covers: 16 Divisional Charts (Shodashavarga D1-D60), Ashtakavarga (337 Bindus, Shodhana & Kakshya), Shadbala (6-fold strength).
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

def get_pages_part3():
    pages = []

    # Page 55: षोडशवर्ग का महत्व
    p55 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ षोडशवर्ग रहस्यम् बृहत्पाराशरे ॥</strong><br>
  <em>"वर्गैस्तु जायते ज्ञानं ग्रहाणां बलमुत्तमम् । लग्नस्य च बलं ज्ञेयं वर्गेभ्यः सूक्ष्मदर्शने ॥"</em>
</div>

<p><strong>सिद्धांत:</strong> लग्न कुण्डली (D1) यदि वृक्ष का तना है, तो वर्ग कुण्डलियाँ (D2 से D60) उसकी शाखाएं, फल एवं पत्तियां हैं। किसी ग्रह का D1 में शुभ बैठना केवल बाह्य आवरण है; वह ग्रह अपने भीतर कितना आत्मिक बल रखता है, इसका रहस्य केवल वर्ग कुण्डलियां ही प्रकट करती हैं।</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>महर्षि पराशर द्वारा स्वीकृत ४ प्रमुख वर्ग समूह:</strong><br>
  • <strong>षड्वर्ग (६ वर्ग):</strong> D1, D2, D3, D9, D12, D30 (प्रारंभिक फलित हेतु)<br>
  • <strong>सप्तवर्ग (७ वर्ग):</strong> षड्वर्ग + D7 (सप्तांश)<br>
  • <strong>दशवर्ग (१० वर्ग):</strong> सप्तवर्ग + D10, D16, D60<br>
  • <strong>षोडशवर्ग (१६ वर्ग):</strong> पूर्ण सूक्ष्म फलित हेतु D1 से D60 तक के सभी १६ वर्ग।
</div>
'''
    p55 += get_shodashavarga_tree_svg()

    pages.append(make_page(55, "षोडशवर्ग • Divisional Charts", "षोडशवर्ग का महत्व: वृक्ष एवं शाखाओं का सिद्धांत", p55))

    # Page 56: होरा चक्र (D2)
    p56 = '''
<p>प्रत्येक राशि को दो बराबर भागों (१५°-१५°) में विभाजित करके धन एवं संपत्ति का विश्लेषण <strong>होरा चक्र (D2)</strong> कहलाता है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 होरा विभाजन नियम (सूर्य एवं चंद्र होरा):</strong><br>
  • <strong>विषम राशियों (१, ३, ५, ७, ९, ११) में:</strong><br>
  - प्रथम १५°: <strong>सूर्य की होरा (सिंह)</strong><br>
  - द्वितीय १५°: <strong>चंद्रमा की होरा (कर्क)</strong><br>
  • <strong>सम राशियों (२, ४, ६, ८, १०, १२) में:</strong><br>
  - प्रथम १५°: <strong>चंद्रमा की होरा (कर्क)</strong><br>
  - द्वितीय १५°: <strong>सूर्य की होरा (सिंह)</strong>
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' कुण्डली में होरा स्थिति:</strong><br>
  • सूर्य (१०° २५' तुला - विषम): प्रथम १५° ➔ <strong>सूर्य होरा (सिंह)</strong><br>
  • चंद्रमा (१६° ३७' कर्क - सम): द्वितीय १५° ➔ <strong>सूर्य होरा (सिंह)</strong><br>
  • <em>फल:</em> अधिकांश ग्रह सूर्य होरा में होने से जातक का धन स्व-अर्जित, स्वावलंबी एवं साहसिक कार्यों से आएगा।
</div>
'''
    pages.append(make_page(56, "षोडशवर्ग • Divisional Charts", "होरा चक्र (D2): धन, कोष एवं संपत्ति साधन गणित", p56))

    # Page 57: द्रेष्काण चक्र (D3)
    p57 = '''
<p>राशि को ३ समान भागों (१०°-१०°) में विभाजित करने पर <strong>द्रेष्काण चक्र (D3)</strong> बनता है, जो भाई-बहन एवं पराक्रम दर्शाता है:</p>

<div style="background:#f1f5f9; border-left:4px solid #0284c7; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>द्रेष्काण निर्धारण नियम:</strong><br>
  • प्रथम १०° (०° - १०°): वही राशि स्वयं (१म भाव)<br>
  • द्वितीय १०° (१०° - २०°): उस राशि से ५वीं राशि (त्रिकोण १)<br>
  • तृतीय १०° (२०° - ३०°): उस राशि से ९वीं राशि (त्रिकोण २)
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong>२२वां द्रेष्काण (खगोलीय छिद्र):</strong><br>
  लग्न के अंश जिस द्रेष्काण में पड़ते हैं, उससे ठीक २२वां द्रेष्काण (८वें भाव का द्रेष्काण) अत्यंत अनिष्टकारी माना जाता है। उसका अधिपति 'ख्रेश' कहलाता है।<br>
  जातक 'क' का लग्न कन्या १४° ४२' (द्वितीय द्रेष्काण ➔ मकर) है। २२वां द्रेष्काण <strong>सिंह राशि</strong> में पड़ता है, जिसका स्वामी सूर्य है।
</div>
'''
    pages.append(make_page(57, "षोडशवर्ग • Divisional Charts", "द्रेष्काण चक्र (D3) एवं २२वां द्रेष्काण रहस्य", p57))

    # Page 58: चतुर्थांश (D4) एवं सप्तांश (D7)
    p58 = '''
<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">वर्ग चक्र</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">विभाजन मान</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">विभाजन कलन विधि</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">कारक विषय</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>चतुर्थांश (D4)</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">७° ३०'</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">१, ४, ७, १०वीं राशि का क्रम (केंद्र क्रम)।</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">भूमि, भवन, अचल संपत्ति, भाग्य।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>सप्तांश (D7)</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४° १७' ०८''</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">विषम राशि में उसी राशि से, सम राशि में ७वीं राशि से निरंतर।</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">संतान सुख, वंश वृद्धि, पौत्र-पौत्री।</td>
    </tr>
  </tbody>
</table>

<div style="background:#f0fdf4; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>जातक 'क' चतुर्थांश (D4):</strong> चतुर्थेश गुरु उच्च नवांश में होने एवं D4 में शुभ स्थित होने से प्रचुर भू-संपत्ति एवं गृह-सुख का योग बनता है।
</div>
'''
    p58 += get_navamsha_grid_svg()

    pages.append(make_page(58, "षोडशवर्ग • Divisional Charts", "चतुर्थांश (D4) एवं सप्तांश (D7) साधन विधि", p58))

    # Page 59: नवमांश चक्र (D9) निर्माण विधि
    p59 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ नवमांश निर्माण सूत्रम् ॥</strong><br>
  <em>"मेषादिषु चरे ज्ञेयं सिंहादि स्थिरराशिषु । धनुराद्ये द्विस्वभावे नवांशक्रम ईरितः ॥"</em>
</div>

<p>राशि के ९वें भाग (३° २०' = २०० कला) को <strong>नवमांश (Navamsha - D9)</strong> कहते हैं। यह कुण्डली का हृदय है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 नवमांश गणना का सार्वभौमिक सूत्र:</strong><br>
  • <strong>चर राशियां (मेष, कर्क, तुला, मकर):</strong> उसी राशि से गणना आरंभ (१, २, ३...)।<br>
  • <strong>स्थिर राशियां (वृषभ, सिंह, वृश्चिक, कुंभ):</strong> उस राशि से ९वीं राशि से आरंभ।<br>
  • <strong>द्विस्वभाव राशियां (मिथुन, कन्या, धनु, मीन):</strong> उस राशि से ५वीं राशि से आरंभ।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' लग्न का नवमांश:</strong><br>
  • लग्न: कन्या १४° ४२' (द्विस्वभाव राशि)<br>
  • नवमांश संख्या =  १४° ४२' / ३° २०'  + १ =  १४.७ / ३.३३३  + १ = ५वां नवमांश।<br>
  • कन्या (६) से ५वीं राशि = १० (मकर)। मकर से ५वीं = वृषभ (२)।<br>
  • <strong>परिणाम:</strong> जातक 'क' का नवमांश लग्न <strong>वृषभ</strong> है (स्थिर, शुक्र शासित)।
</div>
'''
    pages.append(make_page(59, "षोडशवर्ग • Divisional Charts", "नवमांश चक्र (D9): निर्माण की चरणबद्ध कलन विधि", p59))

    # Page 60: वर्गोत्तम एवं पुष्कर नवमांश
    p60 = '''
<p>जब कोई ग्रह D1 (लग्न कुण्डली) और D9 (नवमांश) दोनों में <strong>एक ही राशि</strong> में स्थित हो, तो उसे <strong>वर्गोत्तम (Vargottama)</strong> कहते हैं:</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>वर्गोत्तम ग्रह का प्रभाव:</strong><br>
  वर्गोत्तम ग्रह अपनी मूल प्रकृति में उच्च ग्रह के समान शुभ एवं अमोघ फल देता है। यदि वह नीच राशि में भी हो, तो उसका नीचत्व मिटकर जातक को असाधारण प्रतिष्ठा दिलाता है।
</div>

<div style="background:#fefce8; border:1px solid #fef08a; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong style="color:#854d0e;">जातक 'क' कुण्डली में वर्गोत्तम ग्रह परीक्षण:</strong><br>
  • <strong>चंद्रमा:</strong> D1 में कर्क १६° ३७' (स्वक्षेत्री) तथा D9 में भी कर्क राशि ➔ <strong>स्वक्षेत्री वर्गोत्तम</strong> (अत्यंत दुर्लभ वरदान; अगाध स्मृति एवं अंतर्दृष्टि)।<br>
  • <strong>पुष्कर नवमांश:</strong> चंद्रमा पुष्य नक्षत्र के चतुर्थ चरण में होने से पुष्कर नवमांश में भी स्थित हैं, जो कुण्डली को दिव्य सुरक्षा प्रदान करता है।
</div>
'''
    pages.append(make_page(60, "षोडशवर्ग • Divisional Charts", "वर्गोत्तम ग्रह, पुष्कर नवमांश एवं आत्मिक शक्ति", p60))

    # Page 61: दशमांश चक्र (D10)
    p61 = '''
<p>आजीविका, करियर, सत्ता, सम्मान एवं सामाजिक प्रभाव के सूक्ष्म अध्ययन हेतु <strong>दशमांश चक्र (D10)</strong> अनिवार्य है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 दशमांश (D10) साधन सूत्र:</strong><br>
  • १ भाग का मान = ३०° / १० = ३° ००' (१८० कला)<br>
  • <strong>विषम राशियों में:</strong> उसी राशि से निरंतर गणना करें।<br>
  • <strong>सम राशियों में:</strong> उस राशि से ९वीं राशि से गणना आरंभ करें।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong style="color:#166534;">जातक 'क' दशमांश (D10) फलित:</strong><br>
  • D1 में दशमेश बुध है। D10 में बुध केंद्र में बलवान होकर बैठे हैं।<br>
  • गुरु और सूर्य का D10 में प्रभाव जातक को स्वतंत्र शोध, परामर्श, लेखन, एवं उच्च प्रतिष्ठा के क्षेत्र में स्थापित करता है।
</div>
'''
    pages.append(make_page(61, "षोडशवर्ग • Divisional Charts", "दशमांश चक्र (D10): आजीविका एवं सामाजिक प्रतिष्ठा", p61))

    # Page 62: द्वादशांश (D12) एवं षोडशांश (D16)
    p62 = '''
<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">वर्ग चक्र</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">विभाजन</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">गणना सूत्र</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">विचारणीय विषय</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>द्वादशांश (D12)</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">२° ३०'</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">उसी राशि से निरंतर १२ राशियां।</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">माता-पिता का सुख, पितृ ऋण, पूर्व जन्म कर्म।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>षोडशांश (D16)</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१° ५२' ३०''</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">मेष, सिंह, धनु से चक्रवत गणना।</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">वाहन सुख, आंतरिक शांति, यात्रा कष्ट।</td>
    </tr>
  </tbody>
</table>

<div style="background:#f1f5f9; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>रहस्य:</strong> यदि D1 में चतुर्थ भाव पीड़ित हो परंतु D16 में चतुर्थेश उच्च हो, तो जातक को अंततः सुखद वाहन एवं उत्तम आवास की प्राप्ति होती है।
</div>
'''
    pages.append(make_page(62, "षोडशवर्ग • Divisional Charts", "द्वादशांश (D12) एवं षोडशांश (D16) साधन", p62))

    # Page 63: विंशांश (D20) से सप्तविंशांश (D27)
    p63 = '''
<p>उच्च आध्यात्मिक एवं मानसिक शक्तियों के विश्लेषण हेतु उच्चतर वर्ग:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">वर्ग</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">विस्तार</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">अध्यात्म एवं मानसिक फलित</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>विंशांश (D20)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१° ३०'</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">इष्टदेव की पहचान, मंत्र साधना में सिद्धि, गुप्त आध्यात्मिक ज्ञान।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>चतुर्विंशांश (D24)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१° १५'</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">उच्चतर विद्या, मेधा शक्ति, अकादमिक शोध एवं प्रज्ञा।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>सप्तविंशांश (D27)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१° ०६' ४०''</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">शारीरिक शक्ति, जीवनी शक्ति (Vitality) एवं अंतर्निहित प्रतिरोधक क्षमता।</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>जातक 'क' विंशांश (D20):</strong> गुरु और केतु का शुभ संबंध होने से जातक का झुकाव तंत्र, वेद एवं प्राचीन गूढ़ विधाओं के पुनरुद्धार की ओर स्वाभाविक है।
</div>
'''
    pages.append(make_page(63, "षोडशवर्ग • Divisional Charts", "विंशांश (D20), चतुर्विंशांश (D24) एवं D27", p63))

    # Page 64: त्रिंशांश चक्र (D30)
    p64 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ त्रिंशांश रहस्यम् ॥</strong><br>
  <em>"त्रिंशांशे दुष्टफलं ज्ञेयं पापानां च विशेषतः..."</em>
</div>

<p>ग्रहों के अनिष्ट, रोग, दुर्घटना एवं पाप-कर्म के क्षरण को मापने के लिए <strong>त्रिंशांश चक्र (D30)</strong> सर्वाधिक प्रामाणिक है। इसमें सूर्य और चंद्र का कोई भाग नहीं होता; केवल ५ तारा ग्रहों का अधिकार होता है:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">राशि प्रकार</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">मंगल (५°)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">शनि (५°)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">गुरु (८°)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">बुध (७°)</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">शुक्र (५°)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>विषम राशि</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">०° - ५°</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५° - १०°</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१०° - १८°</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१८° - २५°</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">२५° - ३०°</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>सम राशि</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">२५° - ३०°</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">२०° - २५°</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१२° - २०°</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५° - १२°</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">०° - ५°</td>
    </tr>
  </tbody>
</table>
'''
    pages.append(make_page(64, "षोडशवर्ग • Divisional Charts", "त्रिंशांश चक्र (D30): अनिष्ट, रोग एवं अरिष्ट का गणित", p64))

    # Page 65: षष्ट्यंश चक्र (D60)
    p65 = '''
<p>महर्षि पराशर ने षोडशवर्ग में सर्वाधिक महत्व <strong>षष्ट्यंश चक्र (D60)</strong> को दिया है (विंशोपका बल में ४ अंक out of २०):</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 षष्ट्यंश (D60) साधन सूत्र:</strong><br>
  • १ षष्ट्यंश का मान = ३०° / ६० = ०° ३०' (३० कला)<br>
  • D60 Index =  ग्रह देशांतर (कला) / ३०  + १<br>
  • कुल ६० षष्ट्यंशों के विशिष्ट देवता/प्रकृति होती है (घोर, राक्षस, देव, अमृत, आदि)।
</div>

<div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:0.6rem; font-size:0.8rem;">
  <strong>पूर्व जन्म संचित प्रारब्ध:</strong> जुड़वां बच्चों की D1 से D30 तक की कुण्डली समान हो सकती है, परंतु उनके जीवन में भिन्नता D60 के सूक्ष्म ३० कला के अंतर से आती है।
</div>
'''
    pages.append(make_page(65, "षोडशवर्ग • Divisional Charts", "षष्ट्यंश (D60): संचित प्रारब्ध एवं सूक्ष्म संस्कार", p65))

    # Page 66: जातक 'क' वर्ग चक्र समरी
    p66 = '''
<p>जातक 'क' के प्रमुख वर्ग चक्रों में ग्रहों की स्थिति एवं बल की सारांश तालिका:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.35rem; border:1px solid #334155;">ग्रह</th>
      <th style="padding:0.35rem; border:1px solid #334155;">D1 (लग्न)</th>
      <th style="padding:0.35rem; border:1px solid #334155;">D9 (नवमांश)</th>
      <th style="padding:0.35rem; border:1px solid #334155;">D10 (दशमांश)</th>
      <th style="padding:0.35rem; border:1px solid #334155;">वर्ग बल / स्थिति</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">सूर्य</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला (नीच)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मकर</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मेष (उच्च)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">D10 में उच्च, कर्मठ</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>चंद्रमा</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कर्क (स्व)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>कर्क (स्व)</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">वृषभ (उच्च)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>स्वक्षेत्री वर्गोत्तम</strong></td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">मंगल</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सिंह</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">सिंह</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">अग्नि तत्व प्रधान</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;">बुध</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मेष</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मिथुन (स्व)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">D10 में स्वक्षेत्री</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">गुरु</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">वृश्चिक</td><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>कर्क (उच्च)</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1;">धनु (स्व)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">D9 उच्च, D10 स्व</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;">शुक्र</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला (स्व)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मकर</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मीन (उच्च)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">D1 स्व, D10 उच्च</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;">शनि</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कुंभ (स्व)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मेष (नीच)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कुंभ (स्व)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">वक्री, चेष्टाबली</td></tr>
  </tbody>
</table>
'''
    pages.append(make_page(66, "केस स्टडी • Case Study", "जातक 'क' के प्रमुख वर्ग चक्र (D1, D9, D10) समरी", p66))

    # Pages 67 to 76: अष्टकवर्ग प्रणाली
    p67 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ अष्टकवर्ग प्रशंसा बृहत्पाराशरे ॥</strong><br>
  <em>"न तथा जायते ज्ञानं केवलैर्ग्रहराशिभिः । अष्टवर्गविधानज्ञः सर्वज्ञो भवति ध्रुवम् ॥"</em>
</div>

<p><strong>अष्टकवर्ग का आधार:</strong> कोई भी ग्रह केवल अपने स्थित भाव से फल नहीं देता, बल्कि वह ७ ग्रहों (सूर्य, चंद्र, मंगल, बुध, गुरु, शुक्र, शनि) तथा लग्न से अपने संबंधों के आधार पर प्रत्येक राशि में शुभ बिंदु (रेखा/बिंदु) देता है।</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.6rem; font-size:0.8rem; margin:0.6rem 0;">
  <strong>बिंदु प्रणाली:</strong><br>
  • दक्षिण भारतीय परंपरा: शुभ अंक = बिंदु<br>
  • उत्तर भारतीय परंपरा: शुभ अंक = रेखा, अशुभ = करण / बिंदु<br>
  इस महाग्रंथ में सर्वमान्य <strong>शुभ बिंदु (Auspicious Points)</strong> का प्रयोग किया गया है।
</div>
'''
    p67 += get_ashtakavarga_wheel_svg()

    pages.append(make_page(67, "अष्टकवर्ग • Ashtakavarga", "अष्टकवर्ग का तात्विक आधार एवं बिंदु प्रणाली", p67))

    # Page 68: सूर्य, चंद्र, मंगल का BAV
    p68 = '''
<p>प्रत्येक ग्रह का अपना व्यक्तिगत अष्टकवर्ग <strong>भिन्नाष्टकवर्ग (BAV)</strong> कहलाता है:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">कुल बिंदु</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">औसत/राशि</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">शुभ बिंदु देने के प्रमुख स्थान</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>सूर्य</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४८</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">स्वयं से १, २, ४, ७, ८, ९, १०, ११; मंगल से १, २, ४...</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>चंद्रमा</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४९</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४.०८</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">स्वयं से ३, ६, ७, ८, १०, ११; शुक्र से ३, ४, ५, ७...</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>मंगल</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३९</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३.२५</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">स्वयं से १, २, ४, ७, ८, १०, ११; सूर्य से ३, ५, ६...</td></tr>
  </tbody>
</table>

<div style="background:#fefce8; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>नियम:</strong> किसी राशि में यदि ग्रह के BAV में ५ या अधिक बिंदु हों, तो उस राशि में गोचर करते समय वह ग्रह अत्यंत शुभ फल देता है।
</div>
'''
    pages.append(make_page(68, "अष्टकवर्ग • Ashtakavarga", "सूर्य, चंद्र एवं मंगल का भिन्नाष्टकवर्ग (BAV)", p68))

    # Page 69: बुध, गुरु, शुक्र का BAV
    p69 = '''
<p>सौम्य एवं ज्ञान कारक ग्रहों का भिन्नाष्टकवर्ग वितरण:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">कुल बिंदु</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">औसत/राशि</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">विचारणीय फल</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>बुध</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५४</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४.५०</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">बुद्धि, वाणिज्य, लेखन एवं तार्किक क्षमता।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>गुरु</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५६</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४.६७</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">ज्ञान, धर्म, संतान, गुरु कृपा एवं समृद्धि।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>शुक्र</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५२</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४.३३</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">वैवाहिक सुख, कला, वाहन एवं ऐश्वर्य।</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>विशेषता:</strong> देवगुरु बृहस्पति सर्वाधिक ५६ बिंदु प्रदान करते हैं, इसलिए गुरु का अष्टकवर्ग सर्वाधिक कल्याणकारी होता है।
</div>
'''
    pages.append(make_page(69, "अष्टकवर्ग • Ashtakavarga", "बुध, गुरु एवं शुक्र का भिन्नाष्टकवर्ग (BAV)", p69))

    # Page 70: शनि एवं लग्न का अष्टकवर्ग
    p70 = '''
<p>कर्मफलदाता शनि देव एवं लग्न का अष्टकवर्ग साधन:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">शनि का भिन्नाष्टकवर्ग (३९ बिंदु):</strong><br>
  • सूर्य से: १, २, ४, ७, ८, १०, ११ (७ बिंदु)<br>
  • चंद्र से: ३, ६, ११ (३ बिंदु)<br>
  • मंगल से: ३, ५, ६, १०, ११, १२ (६ बिंदु)<br>
  • बुध से: ६, ८, ९, १०, ११, १२ (६ बिंदु)<br>
  • गुरु से: ५, ६, ११, १२ (४ बिंदु)<br>
  • शुक्र से: ६, ११, १२ (३ बिंदु)<br>
  • शनि से: ३, ५, ६, ११ (४ बिंदु)<br>
  • लग्न से: १, ३, ४, ६, १०, ११ (६ बिंदु)<br>
  कुल योग = ७ + ३ + ६ + ६ + ४ + ३ + ४ + ६ = ३९ बिंदु
</div>
'''
    pages.append(make_page(70, "अष्टकवर्ग • Ashtakavarga", "शनि का भिन्नाष्टकवर्ग एवं लग्न का अष्टकवर्ग", p70))

    # Page 71: सर्वाष्टकवर्ग (SAV) एवं ३३७ बिंदु
    p71 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ सर्वाष्टकवर्ग रहस्यम् ॥</strong><br>
  <em>"सप्तविंशत्यधिकानि त्रीणि शतानि बिन्दवः । सर्वाष्टके समाख्याताः..."</em>
</div>

<p>सातों ग्रहों (सूर्य से शनि) के भिन्नाष्टकवर्ग का कुल योग <strong>३३७ बिंदु</strong> होता है:</p>
<div style="text-align:center; font-weight:bold; font-size:0.95rem; color:#0f172a; margin:0.5rem 0;">
  ४८ (सूर्य) + ४९ (चंद्र) + ३९ (मंगल) + ५४ (बुध) + ५६ (गुरु) + ५२ (शुक्र) + ३९ (शनि) = ३३७
</div>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>२८-बिंदु स्वर्ण नियम (Golden Threshold):</strong><br>
  • ३३७ / १२ = २८.०८ बिंदु प्रति भाव (औसत)।<br>
  • <strong>२८ बिंदु:</strong> तटस्थ (Neutral)<br>
  • <strong>२८ से अधिक बिंदु (२९ - ४०+):</strong> अत्यंत शुभ, बलवान, जीवन में समृद्धि व सफलता।<br>
  • <strong>२८ से कम बिंदु (२० - २७):</strong> संघर्ष, अल्प फल, देरी।<br>
  • <strong>२० से कम बिंदु:</strong> अत्यंत दुर्बल, विशेष सावधानी।
</div>
'''
    pages.append(make_page(71, "अष्टकवर्ग • Ashtakavarga", "सर्वाष्टकवर्ग (SAV): ३३७ बिंदु एवं २८-बिंदु नियम", p71))

    # Page 72: अष्टकवर्ग शोधन १: त्रिकोण शोधन
    p72 = '''
<p>अष्टकवर्ग के वास्तविक फलित हेतु दो शास्त्रीय शोधन किए जाते हैं। पहला है <strong>त्रिकोण शोधन (Trikona Shodhana)</strong>:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 त्रिकोण शोधन के ४ त्रिकोण समूह:</strong><br>
  १. <strong>अग्नि त्रिकोण:</strong> मेष (१), सिंह (५), धनु (९)<br>
  २. <strong>पृथ्वी त्रिकोण:</strong> वृषभ (२), कन्या (६), मकर (१०)<br>
  ३. <strong>वायु त्रिकोण:</strong> मिथुन (३), तुला (७), कुंभ (११)<br>
  ४. <strong>जल त्रिकोण:</strong> कर्क (४), वृश्चिक (८), मीन (१२)<br><br>
  <strong>कलन विधि नियम:</strong><br>
  • त्रिकोण की तीनों राशियों में से जो न्यूनतम मान हो, उसे तीनों में से घटा दें।<br>
  • यदि किसी राशि में ० हो, तो कोई परिवर्तन नहीं होगा।<br>
  • यदि तीनों राशियां समान हों, तो तीनों को शून्य (०) कर दिया जाता है।
</div>
'''
    pages.append(make_page(72, "अष्टकवर्ग • Ashtakavarga", "अष्टकवर्ग शोधन १: त्रिकोण शोधन कलन विधि", p72))

    # Page 73: अष्टकवर्ग शोधन २: एकाधिपत्य शोधन
    p73 = '''
<p>त्रिकोण शोधन के उपरांत एक ही ग्रह की दो राशियों (मंगल: मेष-वृश्चिक, बुध: मिथुन-कन्या, गुरु: धनु-मीन, शुक्र: वृषभ-तुला, शनि: मकर-कुंभ) का शोधन <strong>एकाधिपत्य शोधन</strong> कहलाता है:</p>

<div style="background:#f1f5f9; border-left:4px solid #b45309; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>एकाधिपत्य शोधन के प्रमुख नियम:</strong><br>
  १. यदि दोनों राशियों में से किसी एक में ग्रह बैठा हो और दूसरी खाली हो, तो खाली राशि के बिंदु समाप्त (०) हो जाते हैं।<br>
  २. यदि दोनों राशियों में ग्रह बैठे हों, तो कोई शोधन नहीं होता (मान यथावत रहते हैं)।<br>
  ३. यदि दोनों राशियां खाली हों, तो दोनों में से न्यूनतम मान दोनों में रख दिया जाता है।<br>
  ४. सूर्य (सिंह) और चंद्र (कर्क) की केवल एक-एक राशि होने से उनका एकाधिपत्य शोधन नहीं होता।
</div>
'''
    pages.append(make_page(73, "अष्टकवर्ग • Ashtakavarga", "अष्टकवर्ग शोधन २: एकाधिपत्य शोधन कलन विधि", p73))

    # Page 74: शोधपिंड एवं राशिपिंड
    p74 = '''
<p>शोधन के उपरांत आयुर्दाय एवं गोचर फलित के लिए <strong>पिंड (Pinda)</strong> की गणना की जाती है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 राशिपिंड एवं ग्रहपिंड सूत्र:</strong><br>
  १. <strong>राशि गुणक:</strong> मेष (७), वृषभ (१०), मिथुन (८), कर्क (४), सिंह (१०), कन्या (५), तुला (७), वृश्चिक (८), धनु (९), मकर (५), कुंभ (११), मीन (१२)।<br>
  राशिपिंड = \sum (शोधित बिंदु × राशि गुणक)<br>
  २. <strong>ग्रह गुणक:</strong> सूर्य (५), चंद्र (५), मंगल (८), बुध (५), गुरु (१०), शुक्र (७), शनि (५)।<br>
  ग्रहपिंड = \sum (ग्रह युक्त राशि के बिंदु × ग्रह गुणक)<br>
  शोधपिंड = राशिपिंड + ग्रहपिंड
</div>
'''
    pages.append(make_page(74, "अष्टकवर्ग • Ashtakavarga", "शोधपिंड, राशिपिंड एवं ग्रहपिंड साधन सूत्र", p74))

    # Page 75: कक्षी गोचर प्रणाली
    p75 = '''
<p>अष्टकवर्ग में किसी घटना के घटने का सटीक समय निकालने के लिए प्रत्येक राशि (३०°) को ८ भागों में बांटा जाता है, जिसे <strong>कक्षी (Kakshya)</strong> कहते हैं:</p>

<div style="background:#f1f5f9; border-left:4px solid #10b981; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>कक्षी का विभाजन मान:</strong> ३०° / ८ = ३° ४५' (२२५ कला)<br>
  <strong>कक्षी क्रम (मंद से तीव्र):</strong><br>
  १. शनि (०° - ३° ४५') • २. गुरु (३° ४५' - ७° ३०')<br>
  ३. मंगल (७° ३०' - ११° १५') • ४. सूर्य (११° १५' - १५° ००')<br>
  ५. शुक्र (१५° ००' - १८° ४५') • ६. बुध (१८° ४५' - २२° ३०')<br>
  ७. चंद्र (२२° ३०' - २६° १५') • ८. लग्न (२६° १५' - ३०° ००')
</div>

<div style="background:#fefce8; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>गोचर फल रहस्य:</strong> जब कोई गोचरस्थ ग्रह उस कक्षी में प्रवेश करता है जिस कक्षी के स्वामी ने उस राशि में बिंदु दिया हो, तभी उस गोचर का शुभ फल मिलता है।
</div>
'''
    pages.append(make_page(75, "अष्टकवर्ग • Ashtakavarga", "कक्षी गोचर प्रणाली एवं सटीक समय निर्धारण", p75))

    # Page 76: जातक 'क' SAV तालिका
    p76 = '''
<p>जातक 'क' की कुण्डली के समस्त १२ भावों के सर्वाष्टकवर्ग (SAV) बिंदुओं की मास्टर तालिका:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.35rem; border:1px solid #334155;">भाव</th>
      <th style="padding:0.35rem; border:1px solid #334155;">राशि</th>
      <th style="padding:0.35rem; border:1px solid #334155;">SAV बिंदु</th>
      <th style="padding:0.35rem; border:1px solid #334155;">२८ बिंदु से तुलना</th>
      <th style="padding:0.35rem; border:1px solid #334155;">फलित संकेत</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">१</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कन्या</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>३०</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">+२ (शुभ)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">उत्तम स्वास्थ्य, तेजस्वी व्यक्तित्व।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">२</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">तुला</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>३३</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">+५ (अति शुभ)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">अकूत धन संग्रह, मधुर वाणी।</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">६</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कुंभ</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>३४</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">+६ (अति शुभ)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">शत्रु हंता, प्रतियोगिता में अजेय।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">१०</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">मिथुन</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>३२</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">+४ (शुभ)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कार्यक्षेत्र में निरंतर उन्नति।</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">११</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">कर्क</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>३४</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">+६ (अति शुभ)</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">आय व्यय से अधिक (१२वें में २४)।</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.5rem; font-size:0.8rem;">
  <strong>स्वर्ण नियम सत्यापन:</strong> ११वें भाव में ३४ बिंदु और १२वें में २४ बिंदु होने से जातक का धन कभी क्षय नहीं होता; आय सदा व्यय पर भारी रहती है।
</div>
'''
    pages.append(make_page(76, "केस स्टडी • Case Study", "जातक 'क' का संपूर्ण सर्वाष्टकवर्ग एवं फलित", p76))

    # Pages 77 to 84: षड्बल एवं भाव बल
    p77 = '''
<div style="background:#fefce8; border:1px solid #fef08a; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin-bottom:0.7rem;">
  <strong>॥ षड्बल रहस्यम् बृहत्पाराशरे ॥</strong><br>
  <em>"स्थानदिक्कालचेष्टाश्च नैसर्गो दृग्बलं तथा । षडेतानि बलान्याहुर्ग्रहाणां सूक्ष्मवेदिनः ॥"</em>
</div>

<p>ग्रहों के ६-आयामी सामर्थ्य को <strong>षड्बल (Shadbala)</strong> कहते हैं। इसकी माप <strong>रूपा (Rupa)</strong> अथवा <strong>विरूपा (Virupa)</strong> में की जाती है (१ रूपा = ६० विरूपा):</p>

<ol style="font-size:0.8rem; line-height:1.6; padding-left:1.2rem;">
  <li><strong>स्थान बल (Positional):</strong> उच्च, सप्तवर्गज, ओझ-युग्म, केंद्र, द्रेष्काण बल।</li>
  <li><strong>दिक् बल (Directional):</strong> विशिष्ट दिशा में प्राप्त बल।</li>
  <li><strong>काल बल (Temporal):</strong> नतोन्नति, पक्ष, त्रिभाग, अयन, वर्षादि बल।</li>
  <li><strong>चेष्टा बल (Motional):</strong> ग्रहों की गति, वक्रता एवं गतिज ऊर्जा।</li>
  <li><strong>नैसर्गिक बल (Natural):</strong> सूर्य से शनि तक का प्राकृतिक प्रकाश बल।</li>
  <li><strong>दृग्बल (Aspectual):</strong> शुभ एवं पापी ग्रहों की दृष्टि से प्राप्त बल।</li>
</ol>
'''
    p77 += get_shadbala_pillars_svg()

    pages.append(make_page(77, "षड्बल • Shadbala", "षड्बल की अवधारणा एवं ६ प्रकार के बल", p77))

    # Page 78: स्थान बल
    p78 = '''
<p>स्थान बल के अंतर्गत ५ उप-बल आते हैं, जो ग्रह की राशि स्थिति पर निर्भर करते हैं:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">📐 उच्च बल (Uchcha Bala) साधन सूत्र:</strong><br>
  उच्च बल (विरूपा) = \fउच्च बल (विरूपा) = |ग्रह देशांतर - परमनीच बिंदु| ÷ ३<br>
  (अधिकतम मान = ६० विरूपा = १ रूपा उच्च बिंदु पर, नीच पर = ०)
</div>

<div style="background:#f1f5f9; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  <strong>सप्तवर्गज बल:</strong> ग्रह अपने मूलत्रिकोण में ४५ विरूपा, स्वक्षेत्र में ३०, मित्रक्षेत्र में १५, सम में ७.५, शत्रु में ३.७५ तथा अतिशत्रु में १.८७५ विरूपा प्राप्त करता है (D1 से D30 तक ७ वर्गों में योग)।
</div>
'''
    pages.append(make_page(78, "षड्बल • Shadbala", "स्थान बल: उच्च बल एवं सप्तवर्गज बल सूत्र", p78))

    # Page 79: दिक् बल (Directional Strength)
    p79 = '''
<p>प्रत्येक ग्रह किसी विशिष्ट भाव (दिशा) में पूर्ण <strong>दिक् बली (६० विरूपा)</strong> होता है:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">दिशा</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">भाव</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">दिक् बली ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1; text-align:left;">शून्य दिक् बल स्थान</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>पूर्व (East)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१म (लग्न)</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;"><strong>बुध एवं गुरु</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">सप्तम भाव (पश्चिम)</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>उत्तर (North)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४था भाव</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;"><strong>चंद्रमा एवं शुक्र</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">दशम भाव (दक्षिण)</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>पश्चिम (West)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">७वां भाव</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;"><strong>शनि</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">प्रथम भाव (पूर्व)</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>दक्षिण (South)</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">१०वां भाव</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;"><strong>सूर्य एवं मंगल</strong></td><td style="padding:0.35rem; border:1px solid #cbd5e1;">चतुर्थ भाव (उत्तर)</td></tr>
  </tbody>
</table>

<div style="background:#0f172a; color:#f8fafc; padding:0.6rem; border-radius:6px; font-size:0.8rem;">
  दिक् बल = \fदिक् बल (विरूपा) = |ग्रह देशांतर - दिक् बल शून्य बिंदु| ÷ ३ (अधिकतम ६० विरूपा)
</div>
'''
    pages.append(make_page(79, "षड्बल • Shadbala", "दिक् बल: दिशा बल साधन एवं भाव स्थिति", p79))

    # Page 80: काल बल एवं अयन बल
    p80 = '''
<p>समय के प्रभाव से प्राप्त होने वाला <strong>काल बल (Temporal Strength)</strong>:</p>

<div style="background:#f1f5f9; border-left:4px solid #0284c7; padding:0.7rem; font-size:0.82rem; margin:0.6rem 0;">
  <strong>काल बल के प्रमुख घटक:</strong><br>
  १. <strong>पक्ष बल:</strong> शुक्ल पक्ष में शुभ ग्रह (गुरु, शुक्र, बुध, पूर्ण चंद्र) बली होते हैं। कृष्ण पक्ष में पाप ग्रह (सूर्य, मंगल, शनि) बली होते हैं।<br>
  २. <strong>दिवा-रात्रि बल:</strong> दिन में सूर्य, गुरु, शुक्र बली; रात्रि में चंद्र, मंगल, शनि बली; बुध सदा बली।<br>
  ३. <strong>अयन बल:</strong> उत्तर गोलार्ध (उत्तरायण) में सूर्य, मंगल, गुरु, शुक्र बली; दक्षिण गोलार्ध (दक्षिणायन) में चंद्र, शनि बली।
</div>
'''
    pages.append(make_page(80, "षड्बल • Shadbala", "काल बल: नतोन्नति, पक्ष बल एवं अयन बल", p80))

    # Page 81: चेष्टा बल (Motional Strength)
    p81 = '''
<p>ग्रहों की गतिज ऊर्जा एवं वक्रता से प्राप्त होने वाला बल <strong>चेष्टा बल (Cheshta Bala)</strong> कहलाता है:</p>

<div style="background:#0f172a; color:#f8fafc; padding:0.7rem; border-radius:6px; font-size:0.82rem; margin:0.6rem 0;">
  <strong style="color:#38bdf8;">८ गतियों का चेष्टा बल मान:</strong><br>
  १. वक्री (Retrograde): <strong>६० विरूपा (पूर्ण बली)</strong><br>
  २. अनुवक्री (Alternate Retrograde): ३० विरूपा<br>
  ३. विकला (Stationary): १५ विरूपा<br>
  ४. मंदा (Slow): ३० विरूपा<br>
  ५. मंदतरा (Very Slow): १५ विरूपा<br>
  ६. समा (Mean): ७.५ विरूपा<br>
  ७. चरा (Fast): ४५ विरूपा<br>
  ८. अतिचरा (Accelerated): ३० विरूपा
</div>

<div style="background:#f0fdf4; padding:0.5rem; border-radius:6px; font-size:0.8rem;">
  <strong>जातक 'क' कुण्डली:</strong> शनि देव वक्री हैं, अतः शनि को <strong>पूर्ण ६० विरूपा चेष्टा बल</strong> प्राप्त है।
</div>
'''
    pages.append(make_page(81, "षड्बल • Shadbala", "चेष्टा बल: ग्रहों की गतिज ऊर्जा एवं वक्र बल", p81))

    # Page 82: दृग्बल एवं नैसर्गिक बल
    p82 = '''
<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#e2e8f0; color:#0f172a;">
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">बल प्रकार</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">सिद्धांत</th>
      <th style="padding:0.4rem; border:1px solid #cbd5e1;">गणितीय मान</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>नैसर्गिक बल (Natural)</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">ग्रहों का स्वाभाविक प्रकाश/तेज। यह जन्म समय पर निर्भर नहीं करता, सदा स्थिर रहता है।</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">सूर्य (६०), चंद्र (५१.४), शुक्र (४२.८), गुरु (३४.३), बुध (२५.७), मंगल (१७.१), शनि (८.६ विरूपा)।</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:0.35rem; border:1px solid #cbd5e1;"><strong>दृग्बल (Aspectual)</strong></td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">शुभ ग्रहों की दृष्टि से धनात्मक (+), तथा पाप ग्रहों की दृष्टि से ऋणात्मक (-) विरूपा प्राप्त होते हैं।</td>
      <td style="padding:0.35rem; border:1px solid #cbd5e1;">दृष्टि कोण अनुसार अधिकतम ± १५ से ± ६० विरूपा।</td>
    </tr>
  </tbody>
</table>
'''
    pages.append(make_page(82, "षड्बल • Shadbala", "दृग्बल एवं नैसर्गिक बल साधन सूत्र", p82))

    # Page 83: कुल षड्बल न्यूनतम सीमाएं
    p83 = '''
<p>किसी ग्रह को बली (Strong) कहलाने के लिए महर्षि पराशर द्वारा निर्धारित न्यूनतम रूपा सीमाएं:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.4rem; border:1px solid #334155;">ग्रह</th>
      <th style="padding:0.4rem; border:1px solid #334155;">न्यूनतम विरूपा</th>
      <th style="padding:0.4rem; border:1px solid #334155;">न्यूनतम रूपा</th>
      <th style="padding:0.4rem; border:1px solid #334155; text-align:left;">पर्याप्त बल का प्रभाव</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">सूर्य</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३९०</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">६.५ रूपा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">आत्मविश्वास, नेत्र ज्योति, सरकारी सम्मान।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">चंद्रमा</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३६०</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">६.० रूपा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">मानसिक शांति, जनप्रियता, मातृ सुख।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">मंगल</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३००</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५.० रूपा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">पराक्रम, भूमि लाभ, रक्त शुद्धता।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">बुध</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">४२०</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">७.० रूपा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">तर्क, गणित, वाक-चातुर्य, व्यवसाय।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">गुरु</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३९०</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">६.५ रूपा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">ज्ञान, धर्म, संतान, सर्वत्र रक्षा।</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.35rem; border:1px solid #cbd5e1;">शुक्र</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३३०</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५.५ रूपा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">कला, काम सुख, धन, वाहन।</td></tr>
    <tr><td style="padding:0.35rem; border:1px solid #cbd5e1;">शनि</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">३००</td><td style="padding:0.35rem; border:1px solid #cbd5e1; text-align:center;">५.० रूपा</td><td style="padding:0.35rem; border:1px solid #cbd5e1;">धैर्य, सेवा, संगठन, दीर्घायु।</td></tr>
  </tbody>
</table>
'''
    pages.append(make_page(83, "षड्बल • Shadbala", "कुल षड्बल अनुपात एवं रूपात्मक न्यूनतम सीमाएं", p83))

    # Page 84: जातक 'क' षड्बल स्कोरकार्ड
    p84 = '''
<p>जातक 'क' के समस्त ग्रहों का कुल षड्बल स्कोर एवं बली ग्रहों की वरीयता सूची:</p>

<table style="width:100%; border-collapse:collapse; margin:0.7rem 0; font-size:0.78rem;">
  <thead>
    <tr style="background:#0f172a; color:#f8fafc;">
      <th style="padding:0.35rem; border:1px solid #334155;">ग्रह</th>
      <th style="padding:0.35rem; border:1px solid #334155;">कुल रूपा</th>
      <th style="padding:0.35rem; border:1px solid #334155;">न्यूनतम आवश्यकता</th>
      <th style="padding:0.35rem; border:1px solid #334155;">अनुपात (%)</th>
      <th style="padding:0.35rem; border:1px solid #334155;">अवस्था</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>१. शनि</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>८.२५</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">५.०</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">१६५%</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">अति बली (स्वक्षेत्री, वक्री)</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>२. गुरु</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>७.८०</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">६.५</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">१२०%</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पूर्ण बली (D9 उच्च)</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>३. चंद्रमा</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>७.१०</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">६.०</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">११८%</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पूर्ण बली (वर्गोत्तम)</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>४. शुक्र</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>६.४५</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">५.५</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">११७%</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">पूर्ण बली (स्वक्षेत्री)</td></tr>
    <tr><td style="padding:0.3rem; border:1px solid #cbd5e1;"><strong>५. बुध</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;"><strong>७.१५</strong></td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">७.०</td><td style="padding:0.3rem; border:1px solid #cbd5e1; text-align:center;">१०२%</td><td style="padding:0.3rem; border:1px solid #cbd5e1;">बली (लग्नेश)</td></tr>
  </tbody>
</table>

<div style="background:#f0fdf4; border-left:4px solid #10b981; padding:0.5rem; font-size:0.8rem;">
  <strong>खंड ३ संपूर्ण:</strong> षोडशवर्ग, अष्टकवर्ग एवं षड्बल का सूक्ष्म गणित सिद्ध हुआ। अब हम खंड ४ में जैमिनी, नाड़ी एवं वैवाहिक मिलान का गणित प्रस्तुत करेंगे।
</div>
'''
    pages.append(make_page(84, "केस स्टडी • Case Study", "जातक 'क' का संपूर्ण षड्बल स्कोरकार्ड एवं बल", p84))

    return pages

print("Part 3 defined")
