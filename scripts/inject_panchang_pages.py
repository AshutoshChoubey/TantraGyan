#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tantra Gyan • Inject Comprehensive Panchang Guide into Reader and Book Editions
Creates 8 dedicated rich-text and SVG-rendered pages (100 to 107) and renumbers Back Cover to 108.
Total Pages: 108 (Sacred Astrological Number).
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
READER_HTML_PATH = os.path.join(BASE_DIR, "reader.html")
BOOK_HTML_PATH = os.path.join(BASE_DIR, "book.html")
INDEX_HTML_PATH = os.path.join(BASE_DIR, "index.html")

def generate_panchang_pages_html():
    """Generates the HTML for pages 100 through 108."""
    return '''
    <!-- ==========================================================================
         CHAPTER 7: सम्पूर्ण पंचांग फलित निर्देशिका (COMPREHENSIVE PANCHANG GUIDE)
         Five Limbs of Time, 5 Cosmic Elements, 7 Vaars, 30 Tithis, 27 Nakshatras,
         27 Yogas, 11 Karanas & Predictive Synthesis
         Author: Astrologer Ashutosh Kumar Choubey • Tantra Gyan Research Center
         ========================================================================== -->

    <!-- PAGE 100: Panchanga Foundations, 5 Cosmic Elements & 7 Solar Days -->
    <article class="book-page-data" id="page-data-100" data-page="100" data-chapter="Ch 7: सम्पूर्ण पंचांग फलित निर्देशिका" data-title="पंचांग आधार: पंच-महाभूत एवं 7 सौर वार फलित" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page 100: पंचांग आधार: पंच-महाभूत एवं 7 सौर वार फलित">
      <meta itemprop="position" content="100">
      <meta itemprop="name" content="पंचांग आधार: पंच-महाभूत एवं 7 सौर वार फलित">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">Chapter 7 • Panchanga Foundations & Vaar</div>
          <h3 class="chapter-heading" style="font-size:1.18rem; color:var(--accent-gold);">पंचांग आधार: पंच-महाभूत एवं 7 सौर वार फलित विश्लेषण</h3>
          <div class="chapter-subheading" style="font-size:0.86rem; color:var(--text-muted); font-style:italic;">The Five Limbs of Time, Cosmic Elements (Pancha Mahabhutas) & 7 Solar Days Predictive Roster</div>
        </div>

        <p style="font-size:0.88rem; line-height:1.6; margin-bottom:0.75rem;">
          वैदिक खगोल-विज्ञान में <strong>'पञ्चाङ्ग'</strong> (Pancha = 5, Anga = अंग) सूर्य (आत्मा/चेतना) और चन्द्रमा (मन/प्राण) के कोणीय विन्यास से उद्भूत <strong>मानव चेतना व प्रारब्ध का त्रि-आयामी मानचित्र</strong> है। इसके पाँचों अंग प्रकृति के पंच-महाभूतों को नियंत्रित करते हैं:
        </p>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:0.45rem; margin-bottom:0.85rem;">
          <div style="background:rgba(234,88,12,0.1); border:1px solid #ea580c; border-radius:6px; padding:0.4rem 0.55rem; text-align:center;">
            <strong style="color:#ea580c; font-size:0.82rem;">वार • Agni (Fire)</strong>
            <div style="font-size:0.74rem; color:var(--text-main);">शारीरिक ऊर्जा व आयुष्य</div>
          </div>
          <div style="background:rgba(2,132,199,0.1); border:1px solid #0284c7; border-radius:6px; padding:0.4rem 0.55rem; text-align:center;">
            <strong style="color:#0284c7; font-size:0.82rem;">तिथि • Jala (Water)</strong>
            <div style="font-size:0.74rem; color:var(--text-main);">मानसिक सुख व समृद्धि</div>
          </div>
          <div style="background:rgba(124,58,237,0.1); border:1px solid #7c3aed; border-radius:6px; padding:0.4rem 0.55rem; text-align:center;">
            <strong style="color:#7c3aed; font-size:0.82rem;">नक्षत्र • Vayu (Air)</strong>
            <div style="font-size:0.74rem; color:var(--text-main);">अवचेतन मन व प्रारब्ध</div>
          </div>
          <div style="background:rgba(217,119,6,0.1); border:1px solid #d97706; border-radius:6px; padding:0.4rem 0.55rem; text-align:center;">
            <strong style="color:#d97706; font-size:0.82rem;">योग • Akasha (Ether)</strong>
            <div style="font-size:0.74rem; color:var(--text-main);">स्वास्थ्य व आत्मिक शांति</div>
          </div>
          <div style="background:rgba(5,150,105,0.1); border:1px solid #059669; border-radius:6px; padding:0.4rem 0.55rem; text-align:center;">
            <strong style="color:#059669; font-size:0.82rem;">करण • Prithvi (Earth)</strong>
            <div style="font-size:0.74rem; color:var(--text-main);">दैनिक कर्म व सफलता</div>
          </div>
        </div>

        <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)</div>
        <div class="astro-table-container">
          <div class="table-container">
            <div class="table-responsive">
              <table class="astro-table">
                <thead>
                  <tr>
                    <th>वार (Solar Day)</th>
                    <th>अधिपति ग्रह</th>
                    <th>महाभूत</th>
                    <th>मनोवैज्ञानिक प्ररूप (Archetype)</th>
                    <th>फलित लक्षण एवं स्वाभाविक प्रवृत्तियाँ (Predictive Traits)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="primary-col"><strong>रविवार (Ravivaar)</strong></td>
                    <td>सूर्य (Surya)</td>
                    <td>अग्नि (Agni)</td>
                    <td>संप्रभु / प्रशासक (The Sovereign)</td>
                    <td>स्वाभाविक आत्मविश्वास, गरिमा, उच्च महत्वाकांक्षा, ओजस्वी व्यक्तित्व। अहंकार, हठधर्मिता एवं अक्षमता के प्रति असहिष्णुता।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>सोमवार (Somvaar)</strong></td>
                    <td>चन्द्र (Chandra)</td>
                    <td>जल (Jala)</td>
                    <td>पोषणकर्त्ता / राजनयिक (The Nurturer)</td>
                    <td>प्रगाढ़ अंतःप्रज्ञा, संवेदनशीलता, पारिवारिक दायित्व, कल्पनाशीलता। चित्त की चंचलता, अति-भावुकता एवं अनिर्णय।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>मंगलवार (Mangalvaar)</strong></td>
                    <td>मंगल (Mangal)</td>
                    <td>अग्नि (Agni)</td>
                    <td>योद्धा / अग्रदूत (The Warrior)</td>
                    <td>उच्च ऊर्जा, साहसिक निर्णय, स्पष्टवादिता, तकनीकी रुझान, त्वरित प्रतिक्रिया। उतावलापन, कलह-प्रियता एवं तीखा क्रोध।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>बुधवार (Budhvaar)</strong></td>
                    <td>बुध (Budh)</td>
                    <td>पृथ्वी (Prithvi)</td>
                    <td>विद्वान / व्यापारी (The Scholar)</td>
                    <td>तीक्ष्ण विश्लेषण, वाक्-पटुता, तार्किक बुद्धि, बहुमुखी प्रतिभा व वाणिज्यिक चातुर्य। मानसिक व्यग्रता व अति-आलोचना।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>गुरुवार (Guruvaar)</strong></td>
                    <td>बृहस्पति (Guru)</td>
                    <td>आकाश (Akasha)</td>
                    <td>दार्शनिक / नीति-परामर्शदाता (The Sage)</td>
                    <td>उदात्त विवेक, आशावादी दृष्टिकोण, नैतिक दृढ़ता, गुरुत्व एवं ज्ञान के प्रति निष्ठा। सैद्धांतिक हठ व यथार्थ की उपेक्षा।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>शुक्रवार (Shukravaar)</strong></td>
                    <td>शुक्र (Shukra)</td>
                    <td>जल (Jala)</td>
                    <td>कलाकार / समरसता-संस्थापक (Harmonizer)</td>
                    <td>परिष्कृत सुरुचि, सौन्दर्य-बोध, मधुर व्यवहार, कूटनीति, विलासिता व सम्बंध-प्रियता। संघर्ष से पलायन व भोग-विलास की अति।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>शनिवार (Shanivaar)</strong></td>
                    <td>शनि (Shani)</td>
                    <td>वायु (Vayu)</td>
                    <td>तपस्वी / रणनीतिकार (The Strategist)</td>
                    <td>असाधारण धैर्य, कठोर श्रम-साधना, गहन यथार्थवाद, कर्तव्य-परायणता व अनुशासनात्मक शक्ति। संकोच व निराशावादी अंतर्मुखता।</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- PAGE 101: 30 Tithis & 5 Functional Categories -->
    <article class="book-page-data" id="page-data-101" data-page="101" data-chapter="Ch 7: सम्पूर्ण पंचांग फलित निर्देशिका" data-title="30 तिथियां, 5 श्रेणियां एवं फलित प्रभाव" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page 101: 30 तिथियां, 5 श्रेणियां एवं फलित प्रभाव">
      <meta itemprop="position" content="101">
      <meta itemprop="name" content="30 तिथियां, 5 श्रेणियां एवं फलित प्रभाव">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">Chapter 7 • Tithi Section 2</div>
          <h3 class="chapter-heading" style="font-size:1.18rem; color:var(--accent-gold);">30 तिथियां, 5 श्रेणियां एवं फलित प्रभाव</h3>
          <div class="chapter-subheading" style="font-size:0.86rem; color:var(--text-muted); font-style:italic;">30 Lunar Phases, 5 Functional Categories & Psychological Natal Archetypes</div>
        </div>

        <p style="font-size:0.88rem; line-height:1.6; margin-bottom:0.75rem;">
          सूर्य और चन्द्रमा के मध्य प्रति 12° के कोणीय विस्तार को 'तिथि' कहते हैं। शुक्ल पक्ष विस्तार व निर्माण का तथा कृष्ण पक्ष शोधन व अंतर्मुखता का द्योतक है।
        </p>

        <div style="background:rgba(200,157,61,0.08); border-left:3px solid var(--accent-gold); padding:0.45rem 0.85rem; border-radius:4px; font-size:0.83rem; margin-bottom:0.75rem;">
          <strong>पंच-तिथि श्रेणियां:</strong> 
          <strong>नंदा (1,6,11 - अग्नि):</strong> उत्सव व ललित कलाएं | 
          <strong>भद्रा (2,7,12 - पृथ्वी):</strong> स्थायी निर्माण व निवेश | 
          <strong>जया (3,8,13 - वायु):</strong> प्रतियोगिता व साहस | 
          <strong>रिक्ता (4,9,14 - जल):</strong> संहार, तंत्र व विघ्न निवारण | 
          <strong>पूर्णा (5,10,15/30 - आकाश):</strong> महायज्ञ व पूर्णत्व सिद्धि।
        </div>

        <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)</div>
        <div class="astro-table-container">
          <div class="table-container">
            <div class="table-responsive">
              <table class="astro-table">
                <thead>
                  <tr>
                    <th>तिथि (Tithi)</th>
                    <th>श्रेणी (Category)</th>
                    <th>अधिष्ठाता देवता</th>
                    <th>जन्मकालिक मानसिक प्रवृत्ति व फलित (Predictive Archetype)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td class="primary-col"><strong>प्रतिपदा (1)</strong></td><td>नंदा (Nanda)</td><td>अग्नि देव (Agni)</td><td>अग्रगामी चेतना, नेतृत्व, नवीन उपक्रमों का सूत्रपात, आत्म-निर्भरता।</td></tr>
                  <tr><td class="primary-col"><strong>द्वितीया (2)</strong></td><td>भद्रा (Bhadra)</td><td>ब्रह्मा (Brahma)</td><td>सत्य-निष्ठा, वाक्-सिद्धि, पारिवारिक आकर्षण, संचित धन एवं स्थायित्व।</td></tr>
                  <tr><td class="primary-col"><strong>तृतीया (3)</strong></td><td>जया (Jaya)</td><td>गौरी / पार्वती</td><td>पराक्रम, भ्रातृ-सुख, कलात्मक प्रतिभा, संघर्ष पर सहज विजय।</td></tr>
                  <tr><td class="primary-col"><strong>चतुर्थी (4)</strong></td><td>रिक्ता (Rikta)</td><td>श्री गणेश (Ganesha)</td><td>तीक्ष्ण बुद्धि, गुप्त रहस्यों का ज्ञाता, बाधाओं को चीरने का सामर्थ्य, हठ।</td></tr>
                  <tr><td class="primary-col"><strong>पंचमी (5)</strong></td><td>पूर्णा (Poorna)</td><td>नाग देव (Nagas)</td><td>प्रगाढ़ ज्ञान, काम-कला में प्रवीण, सम्मोहन, नैतिक समृद्धि व दीर्घायु।</td></tr>
                  <tr><td class="primary-col"><strong>षष्ठी (6)</strong></td><td>नंदा (Nanda)</td><td>कार्तिकेय (Kartikeya)</td><td>सामरिक रणनीति, यश, शत्रु-दमन, संगठन क्षमता, शारीरिक स्फूर्ति।</td></tr>
                  <tr><td class="primary-col"><strong>सप्तमी (7)</strong></td><td>भद्रा (Bhadra)</td><td>सूर्य देव (Surya)</td><td>आत्म-सम्मान, तेजस्वी मुखमंडल, उत्तम स्वास्थ्य, राजकीय प्रतिष्ठा।</td></tr>
                  <tr><td class="primary-col"><strong>अष्टमी (8)</strong></td><td>जया (Jaya)</td><td>शिव / रुद्र (Rudra)</td><td>तीव्र तप-बल, आध्यात्मिक रूपांतरण, गूढ़ विज्ञानों में रुचि, दृढ़ता।</td></tr>
                  <tr><td class="primary-col"><strong>नवमी (9)</strong></td><td>रिक्ता (Rikta)</td><td>माँ दुर्गा (Durga)</td><td>निर्भीक स्वभाव, अन्याय का प्रतिरोध, प्रचंड संकल्प, तीव्र वाणी।</td></tr>
                  <tr><td class="primary-col"><strong>दशमी (10)</strong></td><td>पूर्णा (Poorna)</td><td>यमराज / धर्म</td><td>धर्म-परायणता, नियम-पालन, सामाजिक प्रतिष्ठा, नीतिवान आचरण।</td></tr>
                  <tr><td class="primary-col"><strong>एकादशी (11)</strong></td><td>नंदा (Nanda)</td><td>विश्वेदेवा</td><td>निर्मल मति, उपवास/तप में रुचि, आध्यात्मिक विवेक, ऐश्वर्य।</td></tr>
                  <tr><td class="primary-col"><strong>द्वादशी (12)</strong></td><td>भद्रा (Bhadra)</td><td>विष्णु (Vishnu)</td><td>सर्व-प्रिय, उदार हृदय, लोकोपकारी, अनुबंधों में अखंड सफलता।</td></tr>
                  <tr><td class="primary-col"><strong>त्रयोदशी (13)</strong></td><td>जया (Jaya)</td><td>कामदेव</td><td>सौन्दर्य, अनुग्रह, मित्रता, आकर्षण एवं आनंदमयी जीवन शैली।</td></tr>
                  <tr><td class="primary-col"><strong>चतुर्दशी (14)</strong></td><td>रिक्ता (Rikta)</td><td>कालिका / शिव</td><td>प्रचंड ऊर्जा, तंत्र साधना की क्षमता, तीव्र आक्रामकता, शोध वृत्ति।</td></tr>
                  <tr><td class="primary-col"><strong>पूर्णिमा (15)</strong></td><td>पूर्णा (Poorna)</td><td>चन्द्रमा (Chandra)</td><td>पूर्ण मानस बल, भावनात्मक संतुलन, सर्वमान्य ख्याति, संपदा।</td></tr>
                  <tr><td class="primary-col"><strong>अमावस्या (30)</strong></td><td>पूर्णा (Poorna)</td><td>पितृगण (Pitrus)</td><td>गहन दार्शनिक अंतर्दृष्टि, पितृ-ऋण शोधन, गूढ़ ज्ञान, वैराग्य भावना।</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- PAGE 102: 27 Nakshatras Complete Roster (Part 1: Ashwini to Purva Phalguni) -->
    <article class="book-page-data" id="page-data-102" data-page="102" data-chapter="Ch 7: सम्पूर्ण पंचांग फलित निर्देशिका" data-title="27 नक्षत्र फलित ज्ञानकोश (भाग 1: अश्विनी से पूर्वाफाल्गुनी)" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page 102: 27 नक्षत्र फलित ज्ञानकोश (भाग 1: अश्विनी से पूर्वाफाल्गुनी)">
      <meta itemprop="position" content="102">
      <meta itemprop="name" content="27 नक्षत्र फलित ज्ञानकोश (भाग 1: अश्विनी से पूर्वाफाल्गुनी)">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">Chapter 7 • Nakshatra Roster Part 1</div>
          <h3 class="chapter-heading" style="font-size:1.18rem; color:var(--accent-gold);">27 नक्षत्र फलित ज्ञानकोश (भाग 1: अश्विनी से पूर्वाफाल्गुनी)</h3>
          <div class="chapter-subheading" style="font-size:0.86rem; color:var(--text-muted); font-style:italic;">27 Lunar Mansions Predictive Roster — Degrees, Deities, Planetary Lords & Natal Traits</div>
        </div>

        <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)</div>
        <div class="astro-table-container">
          <div class="table-container">
            <div class="table-responsive">
              <table class="astro-table">
                <thead>
                  <tr>
                    <th>नक्षत्र (Nakshatra)</th>
                    <th>विस्तार (Span)</th>
                    <th>देवता</th>
                    <th>स्वामी</th>
                    <th>प्रतीक</th>
                    <th>फलित लक्षण व जन्मकालिक स्वभाव</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td class="primary-col"><strong>1. अश्विनी (Ashwini)</strong></td><td>0°00'-13°20' मेष</td><td>अश्विनी कुमार</td><td>केतु</td><td>अश्व मुख</td><td>तीव्र गति, आरोग्य-प्रदाता, साहसी, नवीन उपक्रमों का प्रवर्तक, स्वतंत्रचेता।</td></tr>
                  <tr><td class="primary-col"><strong>2. भरणी (Bharani)</strong></td><td>13°20'-26°40' मेष</td><td>यमराज</td><td>शुक्र</td><td>योनि</td><td>तीव्र सहनशक्ति, सत्य का अन्वेषक, सामाजिक सीमाओं को चुनौती देने वाला।</td></tr>
                  <tr><td class="primary-col"><strong>3. कृत्तिका (Krittika)</strong></td><td>26°40' मेष-10°00' वृष</td><td>अग्नि देव</td><td>सूर्य</td><td>अग्नि शिखा</td><td>तीक्ष्ण बुद्धि, अदम्य ऊर्जा, पाक-कला, आलोचक दृष्टि, शोधक स्वभाव।</td></tr>
                  <tr><td class="primary-col"><strong>4. रोहिणी (Rohini)</strong></td><td>10°00'-23°20' वृष</td><td>प्रजापति</td><td>चन्द्र</td><td>रथ</td><td>अनुपम सौन्दर्य, आकर्षक नेत्र, कला-प्रेम, भौतिक समृद्धि, मोह-माया।</td></tr>
                  <tr><td class="primary-col"><strong>5. मृगशिरा (Mrigashira)</strong></td><td>23°20' वृष-6°40' मिथुन</td><td>सोम/चन्द्र</td><td>मंगल</td><td>हिरण मस्तक</td><td>सतत खोज, चंचल बुद्धि, यात्रा-प्रिय, संशयवादी, संवेदनशील।</td></tr>
                  <tr><td class="primary-col"><strong>6. आर्द्रा (Ardra)</strong></td><td>6°40'-20°00' मिथुन</td><td>रुद्र</td><td>राहु</td><td>अश्रु बिंदु</td><td>तूफानी बौद्धिक क्षमता, विघटनकारी परिवर्तन, तकनीकी शोध, गहन रूपांतरण।</td></tr>
                  <tr><td class="primary-col"><strong>7. पुनर्वसु (Punarvasu)</strong></td><td>20°00' मिथुन-3°20' कर्क</td><td>अदिति</td><td>गुरु</td><td>बाण तरकश</td><td>पुनरागमन, सात्विक संतोष, आध्यात्मिकता, उदारता, सुरक्षित जीवन।</td></tr>
                  <tr><td class="primary-col"><strong>8. पुष्य (Pushya)</strong></td><td>3°20'-16°40' कर्क</td><td>बृहस्पति</td><td>शनि</td><td>पुष्प/थन</td><td>सर्वोच्च पोषणकर्ता, धार्मिक निष्ठा, ज्ञान, स्थिर बुद्धि, सामाजिक प्रतिष्ठा।</td></tr>
                  <tr><td class="primary-col"><strong>9. आश्लेषा (Ashlesha)</strong></td><td>16°40'-30°00' कर्क</td><td>सर्प</td><td>बुध</td><td>कुण्डलित सर्प</td><td>गूढ़ बुद्धि, सम्मोहन, रणनीतिक सतर्कता, दार्शनिक गहराई, तीखा बचाव।</td></tr>
                  <tr><td class="primary-col"><strong>10. मघा (Magha)</strong></td><td>0°00'-13°20' सिंह</td><td>पितृगण</td><td>केतु</td><td>सिंहासन</td><td>राजसी गौरव, पैतृक परंपरा का संवाहक, नेतृत्व, स्वाभिमान, अधिकार।</td></tr>
                  <tr><td class="primary-col"><strong>11. पूर्वाफाल्गुनी (P. Phalguni)</strong></td><td>13°20'-26°40' सिंह</td><td>भग</td><td>शुक्र</td><td>शय्या</td><td>विलासिता, दांपत्य प्रेम, संगीत, मनोरंजन, सामाजिक लोकप्रियता।</td></tr>
                  <tr><td class="primary-col"><strong>12. उत्तराफाल्गुनी (U. Phalguni)</strong></td><td>26°40' सिंह-10°00' कन्या</td><td>अर्यमा</td><td>सूर्य</td><td>चारपाई पाए</td><td>मित्रता, अनुबंध, निष्ठावान संरक्षक, परोपकार, प्रशासनिक पद।</td></tr>
                  <tr><td class="primary-col"><strong>13. हस्त (Hasta)</strong></td><td>10°00'-23°20' कन्या</td><td>सविता/सूर्य</td><td>चन्द्र</td><td>बंद मुट्ठी</td><td>शिल्प-कला, जादुई हाथ, वाक-चातुर्य, अंक-ज्योतिष, व्यापार।</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- PAGE 103: 27 Nakshatras Complete Roster (Part 2: Chitra to Revati) -->
    <article class="book-page-data" id="page-data-103" data-page="103" data-chapter="Ch 7: सम्पूर्ण पंचांग फलित निर्देशिका" data-title="27 नक्षत्र फलित ज्ञानकोश (भाग 2: चित्रा से रेवती)" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page 103: 27 नक्षत्र फलित ज्ञानकोश (भाग 2: चित्रा से रेवती)">
      <meta itemprop="position" content="103">
      <meta itemprop="name" content="27 नक्षत्र फलित ज्ञानकोश (भाग 2: चित्रा से रेवती)">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">Chapter 7 • Nakshatra Roster Part 2</div>
          <h3 class="chapter-heading" style="font-size:1.18rem; color:var(--accent-gold);">27 नक्षत्र फलित ज्ञानकोश (भाग 2: चित्रा से रेवती)</h3>
          <div class="chapter-subheading" style="font-size:0.86rem; color:var(--text-muted); font-style:italic;">27 Lunar Mansions Predictive Roster — Degrees, Deities, Planetary Lords & Natal Traits</div>
        </div>

        <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)</div>
        <div class="astro-table-container">
          <div class="table-container">
            <div class="table-responsive">
              <table class="astro-table">
                <thead>
                  <tr>
                    <th>नक्षत्र (Nakshatra)</th>
                    <th>विस्तार (Span)</th>
                    <th>देवता</th>
                    <th>स्वामी</th>
                    <th>प्रतीक</th>
                    <th>फलित लक्षण व जन्मकालिक स्वभाव</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td class="primary-col"><strong>14. चित्रा (Chitra)</strong></td><td>23°20' कन्या-6°40' तुला</td><td>विश्वकर्मा</td><td>मंगल</td><td>चमकता रत्न</td><td>अद्वितीय रचनाकारिता, वास्तु-कला, सौन्दर्य-सृजन, आकर्षक व्यक्तित्व।</td></tr>
                  <tr><td class="primary-col"><strong>15. स्वाति (Swati)</strong></td><td>6°40'-20°00' तुला</td><td>वायु देव</td><td>राहु</td><td>वायु अंकुर</td><td>स्वतंत्रता-प्रिय, लचीलापन, कूटनीति, व्यापारिक दूरदर्शिता, विनम्रता।</td></tr>
                  <tr><td class="primary-col"><strong>16. विशाखा (Vishakha)</strong></td><td>20°00' तुला-3°20' वृश्चिक</td><td>इन्द्राग्नि</td><td>गुरु</td><td>तोरण द्वार</td><td>एकनिष्ठ लक्ष्य-साधना, महत्वाकांक्षा, विजय-पिपासा, अथक परिश्रम।</td></tr>
                  <tr><td class="primary-col"><strong>17. अनुराधा (Anuradha)</strong></td><td>3°20'-16°40' वृश्चिक</td><td>मित्र देव</td><td>शनि</td><td>कमल पुष्प</td><td>मैत्री, भक्ति, संगठनात्मक क्षमता, विदेश गमन, विपत्ति में भी खिला रहना।</td></tr>
                  <tr><td class="primary-col"><strong>18. ज्येष्ठा (Jyeshtha)</strong></td><td>16°40'-30°00' वृश्चिक</td><td>इन्द्र देव</td><td>बुध</td><td>कुंडल/ताबीज</td><td>ज्येष्ठता, संरक्षण क्षमता, गुप्त शक्ति, अहंकार से संघर्ष, अधिकार।</td></tr>
                  <tr><td class="primary-col"><strong>19. मूल (Mula)</strong></td><td>0°00'-13°20' धनु</td><td>निऋति</td><td>केतु</td><td>बंधी जड़ें</td><td>मूल कारणों की खोज, संपूर्ण रूपांतरण, विनाश से नव-सृजन, तीक्ष्णता।</td></tr>
                  <tr><td class="primary-col"><strong>20. पूर्वाषाढ़ा (P. Ashadha)</strong></td><td>13°20'-26°40' धनु</td><td>अपः (जल)</td><td>शुक्र</td><td>सूप / पंखा</td><td>अपराजेयता, वाक्-प्रभाव, जल-तत्व सम्बंध, जन-समर्थन, आत्मविश्वास।</td></tr>
                  <tr><td class="primary-col"><strong>21. उत्तराषाढ़ा (U. Ashadha)</strong></td><td>26°40' धनु-10°00' मकर</td><td>विश्वेदेवा</td><td>सूर्य</td><td>हाथी दांत</td><td>शाश्वत विजय, विनम्र नेतृत्व, सत्य-निष्ठा, दृढ़ संकल्प, वैश्विक आदर।</td></tr>
                  <tr><td class="primary-col"><strong>22. श्रवण (Shravana)</strong></td><td>10°00'-23°20' मकर</td><td>विष्णु</td><td>चन्द्र</td><td>तीन पदचिह्न</td><td>श्रवण शक्ति, शिष्यत्व, ज्ञान-संग्रह, मौखिक परंपरा का रक्षक, सुख्याति।</td></tr>
                  <tr><td class="primary-col"><strong>23. धनिष्ठा (Dhanishta)</strong></td><td>23°20' मकर-6°40' कुंभ</td><td>अष्ट वसु</td><td>मंगल</td><td>डमरू/मृदंग</td><td>संगीत, लय-ताल, अकूत संपदा, दानशीलता, समूह नेतृत्व, एकाकीपन।</td></tr>
                  <tr><td class="primary-col"><strong>24. शतभिषा (Shatabhisha)</strong></td><td>6°40'-20°00' कुंभ</td><td>वरुण देव</td><td>राहु</td><td>100 चिकित्सक</td><td>रहस्यमयी वैद्य, गोपनीय अनुसंधान, तारों व अंतरिक्ष का ज्ञाता, एकांतवास।</td></tr>
                  <tr><td class="primary-col"><strong>25. पूर्वाभाद्रपद (P. Bhadrapada)</strong></td><td>20°00' कुंभ-3°20' मीन</td><td>अजैकपाद</td><td>गुरु</td><td>द्वि-मुख खड्ग</td><td>तीव्र तप, द्वैत व्यक्तित्व, गूढ़ तंत्र, आत्म-बलिदान, आध्यात्मिक ज्वार।</td></tr>
                  <tr><td class="primary-col"><strong>26. उत्तराभाद्रपद (U. Bhadrapada)</strong></td><td>3°20'-16°40' मीन</td><td>अहिर्बुध्न्य</td><td>शनि</td><td>गहन सर्प</td><td>अगाध शांति, कुंडलिनी जागरण, ध्यान, उदारता, गंभीर दार्शनिक दृष्टि।</td></tr>
                  <tr><td class="primary-col"><strong>27. रेवती (Revati)</strong></td><td>16°40'-30°00' मीन</td><td>पूषा</td><td>बुध</td><td>मछली युग्म</td><td>अंतिम मोक्ष, पशु-प्रेम, सुरक्षित यात्रा, सर्व-समृद्धि, करुणा व माधुर्य।</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- PAGE 104: 27 Yogas & Mathematical Formula -->
    <article class="book-page-data" id="page-data-104" data-page="104" data-chapter="Ch 7: सम्पूर्ण पंचांग फलित निर्देशिका" data-title="27 योग: सौर-चन्द्र कोणीय गणित व फलित सूत्र" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page 104: 27 योग: सौर-चन्द्र कोणीय गणित व फलित सूत्र">
      <meta itemprop="position" content="104">
      <meta itemprop="name" content="27 योग: सौर-चन्द्र कोणीय गणित व फलित सूत्र">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">Chapter 7 • 27 Yogas Section 4</div>
          <h3 class="chapter-heading" style="font-size:1.18rem; color:var(--accent-gold);">27 योग: सौर-चन्द्र कोणीय गणित व फलित सूत्र</h3>
          <div class="chapter-subheading" style="font-size:0.86rem; color:var(--text-muted); font-style:italic;">The 27 Yogas: Soli-Lunar Angular Sum Formula, Nature & Natal Health Alignment</div>
        </div>

        <div style="background:rgba(217,119,6,0.08); border:1px solid #d97706; border-radius:6px; padding:0.45rem 0.85rem; font-size:0.85rem; margin-bottom:0.75rem;">
          <strong>गणितीय सूत्र (Formula):</strong> 
          <code style="color:var(--accent-gold); font-weight:700;">Yoga Index = ⌊(Longitude(Sun) + Longitude(Moon)) / 13°20'⌋ + 1</code><br>
          <span style="font-size:0.78rem; color:var(--text-muted);">योग आकाश तत्व (Akasha) से सम्बद्ध है, जो जातक के समग्र स्वास्थ्य, आभामंडल एवं जीवन-पथ की सहजता को निर्धारित करता है।</span>
        </div>

        <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)</div>
        <div class="astro-table-container">
          <div class="table-container">
            <div class="table-responsive">
              <table class="astro-table">
                <thead>
                  <tr>
                    <th>क्र.</th>
                    <th>योग (Yoga)</th>
                    <th>स्वरूप (Nature)</th>
                    <th>अधिष्ठाता</th>
                    <th>फलित लक्षण व जन्मकालिक प्रभाव</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>1</td><td class="primary-col"><strong>विष्कम्भ</strong></td><td>अशुभ (Challenging)</td><td>यमराज</td><td>पराक्रमी किंतु प्रारंभिक जीवन में अवरोध; शत्रुओं पर अंततः विजय।</td></tr>
                  <tr><td>2</td><td class="primary-col"><strong>प्रीति</strong></td><td>शुभ (Auspicious)</td><td>विष्णु</td><td>सौम्य, मिलनसार, सर्व-प्रिय, दांपत्य व सामाजिक जीवन में मधुरता।</td></tr>
                  <tr><td>3</td><td class="primary-col"><strong>आयुष्मान्</strong></td><td>शुभ (Auspicious)</td><td>चन्द्र</td><td>उत्तम स्वास्थ्य, दीर्घायु, पारिवारिक सुख, भौतिक स्थिरता।</td></tr>
                  <tr><td>4</td><td class="primary-col"><strong>सौभाग्य</strong></td><td>शुभ (Auspicious)</td><td>ब्रह्मा</td><td>सर्वतोमुखी सौभाग्य, राजकीय प्रतिष्ठा, ऐश्वर्य एवं उच्च कुल-सम्मान।</td></tr>
                  <tr><td>5</td><td class="primary-col"><strong>शोभन</strong></td><td>शुभ (Auspicious)</td><td>बृहस्पति</td><td>रूपवान, तेजस्वी, सदाचारी, कला एवं विद्या में विशेष प्रवीण।</td></tr>
                  <tr><td>6</td><td class="primary-col"><strong>अतिगण्ड</strong></td><td>अशुभ (Challenging)</td><td>चन्द्र</td><td>बाल्यावस्था में स्वास्थ्य कष्ट, माता के लिए संवेदनशील, संघर्षशील।</td></tr>
                  <tr><td>7</td><td class="primary-col"><strong>सुकर्मा</strong></td><td>शुभ (Auspicious)</td><td>इन्द्र</td><td>सत्कर्मों में तत्पर, कार्य-कुशल, न्यायप्रिय, समाज में सम्मानित।</td></tr>
                  <tr><td>8</td><td class="primary-col"><strong>धृति</strong></td><td>शुभ (Auspicious)</td><td>जल/वरुण</td><td>अगाध धैर्य, विपत्ति में शांत चित्त, अध्ययनशील, भूमि-संपत्ति लाभ।</td></tr>
                  <tr><td>9</td><td class="primary-col"><strong>शूल</strong></td><td>अशुभ (Challenging)</td><td>सर्प</td><td>उदर-पीड़ा अथवा शारीरिक शूल, आक्रामक स्वभाव; साधना श्रेयस्कर।</td></tr>
                  <tr><td>10</td><td class="primary-col"><strong>गण्ड</strong></td><td>अशुभ (Challenging)</td><td>अग्नि</td><td>आकस्मिक विपत्तियाँ, तीव्र महत्वाकांक्षा, पारिवारिक दायित्व।</td></tr>
                  <tr><td>11</td><td class="primary-col"><strong>वृद्धि</strong></td><td>शुभ (Auspicious)</td><td>सूर्य</td><td>धन-धान्य में निरंतर वृद्धि, व्यापारिक विस्तार, यशस्वी जीवन।</td></tr>
                  <tr><td>12</td><td class="primary-col"><strong>ध्रुव</strong></td><td>शुभ (Auspicious)</td><td>भूमि</td><td>अटल संकल्प, एकाग्र बुद्धि, अचल संपत्ति, दीर्घकालिक सफलता।</td></tr>
                  <tr><td>13</td><td class="primary-col"><strong>व्याघात</strong></td><td>अशुभ (Challenging)</td><td>वायु</td><td>तीव्र क्रोधी, साहसिक व सामरिक कार्यों में सफल, सतर्कता अपेक्षित।</td></tr>
                  <tr><td>14</td><td class="primary-col"><strong>हर्षण</strong></td><td>शुभ (Auspicious)</td><td>भग</td><td>सदा प्रसन्नचित्त, हास्य-विनोद प्रिय, मित्रों का चहेता, भाग्यवान।</td></tr>
                  <tr><td>15</td><td class="primary-col"><strong>वज्र</strong></td><td>अशुभ (Challenging)</td><td>वरुण</td><td>वज्र समान कठोर संकल्प, संपदा; सम्बंधों में कठोरता से बचें।</td></tr>
                  <tr><td>16</td><td class="primary-col"><strong>सिद्धि</strong></td><td>शुभ (Auspicious)</td><td>गणेश</td><td>समस्त कार्यों में सिद्धि, मंत्र-विद्या, तीव्र स्मरण शक्ति, सुखी।</td></tr>
                  <tr><td>17</td><td class="primary-col"><strong>व्यतीपात</strong></td><td>अत्यंत अशुभ</td><td>रुद्र</td><td>आकस्मिक उथल-पुथल, बाल्य संघर्ष; सूर्य-शांति व रुद्राभिषेक अनिवार्य।</td></tr>
                  <tr><td>18</td><td class="primary-col"><strong>वरीयान्</strong></td><td>शुभ (Auspicious)</td><td>कुबेर</td><td>विलासी, ऐश्वर्यवान, संगीत व ललित कलाओं का पारखी, संपन्न।</td></tr>
                  <tr><td>19</td><td class="primary-col"><strong>परिघ</strong></td><td>अशुभ (Challenging)</td><td>विश्वकर्मा</td><td>विरोधी तत्वों से घिरा रहना; मध्यम आयु के पश्चात विजय व स्थिरता।</td></tr>
                  <tr><td>20</td><td class="primary-col"><strong>शिव</strong></td><td>अत्यंत शुभ</td><td>महादेव</td><td>शांत, वैरागी, सर्व-कल्याणकारी, ज्ञानवान, धर्म-संस्थापक।</td></tr>
                  <tr><td>21</td><td class="primary-col"><strong>सिद्ध</strong></td><td>शुभ (Auspicious)</td><td>कार्तिकेय</td><td>धार्मिक स्वभाव, गुप्त विद्याओं में रुचि, परोपकारी, निष्कलंक यश।</td></tr>
                  <tr><td>22</td><td class="primary-col"><strong>साध्य</strong></td><td>शुभ (Auspicious)</td><td>सावित्री</td><td>साधना-प्रिय, विनम्र, शिष्टाचार-युक्त, कठिन लक्ष्यों को साधक।</td></tr>
                  <tr><td>23</td><td class="primary-col"><strong>शुभ</strong></td><td>शुभ (Auspicious)</td><td>लक्ष्मी</td><td>निर्मल चरित्र, लक्ष्मी अनुग्रह, उत्तम रूप-रंग, सर्व-प्रिय।</td></tr>
                  <tr><td>24</td><td class="primary-col"><strong>शुक्ल</strong></td><td>शुभ (Auspicious)</td><td>पार्वती</td><td>सत्यवादी, ज्ञान-पिपासु, स्वच्छता प्रिय, पवित्र जीवन।</td></tr>
                  <tr><td>25</td><td class="primary-col"><strong>ब्रह्म</strong></td><td>अत्यंत शुभ</td><td>अश्विनी</td><td>शास्त्रों का ज्ञाता, परब्रह्म निष्ठा, परम विद्वान, सर्वमान्य।</td></tr>
                  <tr><td>26</td><td class="primary-col"><strong>इन्द्र</strong></td><td>शुभ (Auspicious)</td><td>इन्द्राणी</td><td>राजसी ठाठ, समूह का अधिपति, नीतिवान, ऐश्वर्य भोगी।</td></tr>
                  <tr><td>27</td><td class="primary-col"><strong>वैधृति</strong></td><td>अत्यंत अशुभ</td><td>दिति</td><td>मानसिक द्वंद्व, जीवन में अस्थिरता; सूर्य-गायत्री जप श्रेयस्कर।</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- PAGE 105: 11 Karanas (7 Movable & 4 Fixed) -->
    <article class="book-page-data" id="page-data-105" data-page="105" data-chapter="Ch 7: सम्पूर्ण पंचांग फलित निर्देशिका" data-title="11 करण: 7 चर व 4 स्थिर करण कर्म-दक्षता" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page 105: 11 करण: 7 चर व 4 स्थिर करण कर्म-दक्षता">
      <meta itemprop="position" content="105">
      <meta itemprop="name" content="11 करण: 7 चर व 4 स्थिर करण कर्म-दक्षता">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">Chapter 7 • Karana Section 5</div>
          <h3 class="chapter-heading" style="font-size:1.18rem; color:var(--accent-gold);">11 करण: 7 चर व 4 स्थिर करण कर्म-दक्षता</h3>
          <div class="chapter-subheading" style="font-size:0.86rem; color:var(--text-muted); font-style:italic;">The 11 Karanas: Half-Tithi Spans, Deities & Vocational Execution Profiles</div>
        </div>

        <p style="font-size:0.88rem; line-height:1.6; margin-bottom:0.75rem;">
          करण एक तिथि का आधा भाग (6° का कोणीय अंतर) होता है। एक चन्द्र मास में कुल 60 करण होते हैं — 7 चर करण (8 बार चक्राकार) एवं 4 स्थिर करण (माह में एक बार)। करण पृथ्वी तत्व (Prithvi) का प्रतिनिधित्व करता है जो कर्म निष्पादन का आधार है।
        </p>

        <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)</div>
        <div class="astro-table-container">
          <div class="table-container">
            <div class="table-responsive">
              <table class="astro-table">
                <thead>
                  <tr>
                    <th>करण (Karana)</th>
                    <th>प्रकार (Type)</th>
                    <th>अधिष्ठाता देवता</th>
                    <th>व्यावसायिक व व्यावहारिक फलित स्वभाव (Execution Profile)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="primary-col"><strong>1. बव (Bava)</strong></td>
                    <td>चर (Movable)</td>
                    <td>इन्द्र (Indra)</td>
                    <td>उद्यमशील, साहसी, नवीन उपक्रमों का निर्भीक संचालक, राज्य-मान्य। उच्च प्रशासनिक क्षमता।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>2. बालव (Balava)</strong></td>
                    <td>चर (Movable)</td>
                    <td>ब्रह्मा (Brahma)</td>
                    <td>कुशाग्र बुद्धि, अध्ययनशील, धार्मिक अनुष्ठानों में दक्ष, सुरुचिपूर्ण, आस्तिक विचारधारा।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>3. कौलव (Kaulava)</strong></td>
                    <td>चर (Movable)</td>
                    <td>मित्र (Mitra)</td>
                    <td>मैत्री-परायण, सौहार्दपूर्ण सम्बंध निर्माता, कला व संगीत प्रिय, उदार, सामाजिक ख्याति।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>4. तैतिल (Taitila)</strong></td>
                    <td>चर (Movable)</td>
                    <td>अर्यमा (Aryaman)</td>
                    <td>कर्तव्यनिष्ठ, सेवा-भावी, निष्ठावान, न्यायप्रिय एवं लोक-कल्याणकारी योजनाओं में अग्रणी।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>5. गर (Gara)</strong></td>
                    <td>चर (Movable)</td>
                    <td>पृथ्वी (Bhoomi)</td>
                    <td>कृषि, रियल एस्टेट, भारी उद्योग व व्यावहारिक धरातल पर कठोर श्रम में सफल। अचल संपत्ति।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>6. वणिज (Vanija)</strong></td>
                    <td>चर (Movable)</td>
                    <td>लक्ष्मी (Lakshmi)</td>
                    <td>अद्वितीय वाणिज्यिक चातुर्य, वित्तीय निवेश, क्रय-विक्रय व व्यापार में विपुल लाभ।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>7. विष्टि / भद्रा (Vishti)</strong></td>
                    <td>चर (Movable)</td>
                    <td>यमराज (Yama)</td>
                    <td>तीक्ष्ण, संहारक व सामरिक कर्मों में अजेय। शुभ कार्यों में रुकावट; तंत्र, शल्य-कर्म व युद्ध में सिद्ध।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>8. शकुनि (Shakuni)</strong></td>
                    <td>स्थिर (Fixed)</td>
                    <td>कलि / गरुड़</td>
                    <td>औषध विज्ञान, रसायन, दूरगामी रणनीतियाँ, गूढ़ शोध; कानूनी व नैतिक सतर्कता आवश्यक।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>9. चतुष्पद (Chatushpada)</strong></td>
                    <td>स्थिर (Fixed)</td>
                    <td>वृषभ / शिव</td>
                    <td>पशु-पालन, गो-सेवा, कृषि संपदा, स्थिर संपत्ति का स्वामी, धार्मिक निष्ठा, धीर-गंभीर।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>10. नाग (Naga)</strong></td>
                    <td>स्थिर (Fixed)</td>
                    <td>नागराज (Naga)</td>
                    <td>पाताल विद्याएं, खनन, भूगर्भ, गुप्त अनुसंधान, विष-चिकित्सा, सम्मोहन व अचल संकल्प शक्ति।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>11. किंस्तुघ्न (Kimstughna)</strong></td>
                    <td>स्थिर (Fixed)</td>
                    <td>वायु (Vayu)</td>
                    <td>सर्व-कल्याणकारी, शुभ कार्यों का प्रवर्तक, ऐश्वर्यवान, परोपकारी, यशस्वी व सदाचारी।</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- PAGE 106: Panchang Predictive Synthesis Matrix -->
    <article class="book-page-data" id="page-data-106" data-page="106" data-chapter="Ch 7: सम्पूर्ण पंचांग फलित निर्देशिका" data-title="पंचांग फलित संश्लेषण विधान व त्रि-स्तरीय सूत्र" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page 106: पंचांग फलित संश्लेषण विधान व त्रि-स्तरीय सूत्र">
      <meta itemprop="position" content="106">
      <meta itemprop="name" content="पंचांग फलित संश्लेषण विधान व त्रि-स्तरीय सूत्र">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">Chapter 7 • Predictive Synthesis Section 6</div>
          <h3 class="chapter-heading" style="font-size:1.18rem; color:var(--accent-gold);">पंचांग फलित संश्लेषण विधान व त्रि-स्तरीय सूत्र</h3>
          <div class="chapter-subheading" style="font-size:0.86rem; color:var(--text-muted); font-style:italic;">How to Synthesize Panchang for Predictive Analysis: The Three-Tier Cosmic Framework</div>
        </div>

        <p style="font-size:0.88rem; line-height:1.6; margin-bottom:0.75rem;">
          पंचांग के पाँच अंगों को पृथक देखने के बजाय <strong>त्रि-स्तरीय समन्वित संरचना</strong> में परखना चाहिए:
        </p>

        <div style="background:rgba(200,157,61,0.06); border:1.5px solid var(--border-gold); border-radius:8px; padding:0.85rem 1rem; margin-bottom:0.85rem;">
          <h4 style="font-size:0.95rem; color:var(--text-heading); margin-bottom:0.4rem;">त्रि-स्तरीय पंचांग संश्लेषण ढाँचा (The Three-Tier Model):</h4>
          <ul style="font-size:0.85rem; line-height:1.65; padding-left:1.2rem; color:var(--text-main);">
            <li><strong>1. स्थूल आधार (Physical Vessel — वार + करण):</strong> वार जीवन-शक्ति (Agni) और करण कार्य-निष्पादन (Prithvi) है। यदि दोनों के अधिपति परस्पर मित्र हैं, तो जातक जो सोचता है उसे धरातल पर 100% साकार करता है।</li>
            <li><strong>2. अंतःकरण कोर (Astral Core — तिथि + नक्षत्र):</strong> तिथि बाहरी मन (Jala) और नक्षत्र अवचेतन संस्कार (Vayu) है। यह संयोजन जातक की इच्छाओं, भावनात्मक स्थिरता और आंतरिक सुख को तय करता है।</li>
            <li><strong>3. आत्मिक संवाहक (Spiritual Conduit — योग):</strong> योग (Akasha) वह ईथरिक माध्यम है जिससे चेतना का प्रवाह होता है। शुभ योग जीवन के अवरोधों को सहजता से पिघला देता है।</li>
          </ul>
        </div>

        <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)</div>
        <div class="astro-table-container">
          <div class="table-container">
            <div class="table-responsive">
              <table class="astro-table">
                <thead>
                  <tr>
                    <th>संश्लेषण घटक</th>
                    <th>महाभूत सम्बंध</th>
                    <th>फलित क्षेत्र</th>
                    <th>सामंजस्य होने पर फल (Harmonious)</th>
                    <th>विरोध होने पर फल (Conflicting)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="primary-col"><strong>वार + करण</strong></td>
                    <td>अग्नि + पृथ्वी</td>
                    <td>स्वास्थ्य, करियर व निष्पादन</td>
                    <td>अथक परिश्रम, व्यावहारिक सफलता, जो ठाना वह पूर्ण किया।</td>
                    <td>ऊर्जा का बिखराव, योजनाओं का अधूरा छूटना, शारीरिक थकान।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>तिथि + नक्षत्र</strong></td>
                    <td>जल + वायु</td>
                    <td>मनोभाव, सुख व सम्बंध</td>
                    <td>मानसिक शांति, अंतर्ज्ञान, सम्बंधों में प्रगाढ़ता, कलात्मक विकास।</td>
                    <td>मन में द्वंद्व, भावनात्मक असुरक्षा, अनिर्णय की स्थिति।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>योग (सम्पूर्ण कुंडली)</strong></td>
                    <td>आकाश</td>
                    <td>आत्मिक संरेखण व भाग्य</td>
                    <td>कुंडली के दोष स्वतः शांत, न्यूनतम घर्षण में सफलता।</td>
                    <td>अनपेक्षित रुकावटें; सूर्य-साधना व रुद्राभिषेक अनिवार्य।</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- PAGE 107: Dominant Element Override & Cosmic Mandala Plate -->
    <article class="book-page-data" id="page-data-107" data-page="107" data-chapter="Ch 7: सम्पूर्ण पंचांग फलित निर्देशिका" data-title="पंच-महाभूत अधिभावी नियम व विरोधाभास समाधान" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page 107: पंच-महाभूत अधिभावी नियम व विरोधाभास समाधान">
      <meta itemprop="position" content="107">
      <meta itemprop="name" content="पंच-महाभूत अधिभावी नियम व विरोधाभास समाधान">
      <div class="page-inner-content">
        <div class="chapter-header" style="margin-bottom:0.75rem;">
          <div class="chapter-number">Chapter 7 • Dominant Elements & Mandala</div>
          <h3 class="chapter-heading" style="font-size:1.18rem; color:var(--accent-gold);">पंच-महाभूत अधिभावी नियम व विरोधाभास समाधान</h3>
          <div class="chapter-subheading" style="font-size:0.86rem; color:var(--text-muted); font-style:italic;">Dominant Element Override Protocol, Resolving Internal Contradictions & Cosmic Mandala</div>
        </div>

        <!-- Sacred Panchanga Mandala SVG Plate -->
        <div class="visual-chart-plate full-page-chart" style="margin: 0.5rem auto 0.85rem auto; text-align: center;">
          <img src="assets/icons/panchang_mandala_chart.svg" alt="पञ्चाङ्ग पञ्च-महाभूत काल-संयोजन महामण्डल (Vedic Panchanga Mandala)" style="width:100%; max-width:520px; height:auto; display:block; margin:0 auto; border-radius:12px; box-shadow:0 6px 24px rgba(0,0,0,0.12);" loading="lazy">
          <div class="chart-caption" style="margin-top:0.4rem; font-size:0.82rem; font-style:italic; color:var(--text-muted); text-align:center;">
            चित्र 7.1: पञ्चाङ्ग पञ्च-महाभूत काल-संयोजन महामण्डल — वार (अग्नि), तिथि (जल), नक्षत्र (वायु), योग (आकाश), करण (पृथ्वी) एवं मध्य में कालपुरुष चेतना
          </div>
        </div>

        <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)</div>
        <div class="astro-table-container">
          <div class="table-container">
            <div class="table-responsive">
              <table class="astro-table">
                <thead>
                  <tr>
                    <th>अधिभावी तत्व (Dominant Element)</th>
                    <th>पंचांग संयोजन उदाहरण</th>
                    <th>जातक का अंतिम जीवन-प्रारूप (Predictive Outcome)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="primary-col"><strong>अग्नि तत्व प्रधान (Fire)</strong></td>
                    <td>रविवार + प्रतिपदा (नंदा) + कृत्तिका</td>
                    <td>प्रचंड नेतृत्व, प्रशासनिक प्रभुत्व, स्वतंत्र उद्यम, पित्त प्रकृति, क्षमा का अभाव।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>जल तत्व प्रधान (Water)</strong></td>
                    <td>सोमवार + पूर्णिमा (पूर्णा) + रोहिणी/रेवती</td>
                    <td>अगाध अंतर्ज्ञान, कला-साधना, कफ प्रकृति, प्रचुर संपदा, अत्यधिक संवेदनशीलता।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>वायु तत्व प्रधान (Air)</strong></td>
                    <td>शनिवार + तृतीया (जया) + स्वाति/शतभिषा</td>
                    <td>बौद्धिक क्रांति, यायावर जीवन, वात प्रकृति, तकनीकी आविष्कार, स्वतंत्र वैराग्य।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>पृथ्वी तत्व प्रधान (Earth)</strong></td>
                    <td>बुधवार + द्वितीया (भद्रा) + गर/वणिज</td>
                    <td>ठोस व्यावसायिक सफलता, विशाल अचल संपत्ति, यथार्थवादी दृष्टि, भौतिक समृद्धि।</td>
                  </tr>
                  <tr>
                    <td class="primary-col"><strong>आकाश तत्व प्रधान (Ether)</strong></td>
                    <td>गुरुवार + पंचमी (पूर्णा) + ब्रह्म/शिव योग</td>
                    <td>संत-हृदय, उच्च आध्यात्मिक ज्ञान, नीति-परामर्श, सर्व-स्वीकार्यता, मोक्ष मार्ग।</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div style="margin-top:0.65rem; background:rgba(217,119,6,0.06); border-left:3px solid var(--accent-gold); padding:0.45rem 0.75rem; font-size:0.8rem; color:var(--text-main);">
          <strong>विरोधाभास समाधान सूत्र (Contradiction Protocol):</strong> यदि नक्षत्र शुभ (उदा. पुष्य) हो किंतु तिथि रिक्ता (उदा. चतुर्दशी) हो, तो जातक का प्रारंभिक जीवन संघर्षमय रहेगा, किंतु उत्तरार्ध में पुष्य का ज्ञान व तप उसे अपार सिद्धि व यश प्रदान करेगा।
        </div>
      </div>
    </article>

    <!-- PAGE 108: Colophon & Closing Vedic Shlokas (Back Cover) -->
    <article class="book-page-data" id="page-data-108" data-page="108" data-chapter="उपसंहार • Back Cover" data-title="समापन पृष्ठ • उपसंहार व वैदिक मंगल कामना" itemscope itemtype="https://schema.org/Chapter" role="region" aria-label="Page 108: समापन पृष्ठ • उपसंहार व वैदिक मंगल कामना">
      <meta itemprop="position" content="108">
      <meta itemprop="name" content="समापन पृष्ठ • उपसंहार व वैदिक मंगल कामना">
      <div class="back-cover-inner">
        <div class="cover-ornament-corner top-left"></div>
        <div class="cover-ornament-corner top-right"></div>
        <div class="cover-ornament-corner bottom-left"></div>
        <div class="cover-ornament-corner bottom-right"></div>

        <div class="cover-yantra" style="width:110px; height:110px; margin-bottom:0.35rem;">
          <img src="assets/yantra.svg" alt="Tantra Gyan Sacred Seal" width="110" height="110">
        </div>

        <div class="back-cover-title">वैदिक ज्योतिष महाग्रंथ सरलीकृत</div>
        <div class="back-cover-subtitle">सम्पूर्ण प्रामाणिक शास्त्रीय फलित ज्ञानकोश • 108 पवित्र महापृष्ठ संस्करण</div>

        <div class="invocation-shloka" style="margin: 0.75rem auto; max-width: 90%;">
          ॥ असतो मा सद्गमय। तमसो मा ज्योतिर्गमय। मृत्योर्मा अमृतं गमय॥<br>
          ॥ ॐ पूर्णमदः पूर्णमिदं पूर्णात्पूर्णमुदच्यते। पूर्णस्य पूर्णमादाय पूर्णमेवावशिष्यते॥<br>
          ॥ ॐ शान्तिः शान्तिः शान्तिः ॥
        </div>

        <div class="back-cover-colophon">
          <div style="font-weight:700; color:var(--accent-gold); font-size:0.95rem; margin-bottom:0.25rem;">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</div>
          <div style="color:var(--text-secondary); font-size:0.85rem;">लेखक एवं ज्योतिषाचार्य: <strong>Ashutosh Kumar Choubey</strong></div>
          <div style="font-size:0.8rem; color:var(--text-muted); margin-top:0.35rem;">Copyright © 2026. All rights reserved.</div>
        </div>

        <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem; margin-top:0.4rem;">
          <span class="contact-channel-badge" style="border-color:var(--accent-gold); color:var(--accent-gold) !important; font-size:0.82rem;">
            <span class="contact-icon">🌐</span> <strong>t.worldgyan.com</strong>
          </span>
          <span class="youtube-channel-badge" style="margin-top:0; font-size:0.82rem;">
            <span class="yt-play-icon">▶</span> <strong>@TantraGyan108</strong>
          </span>
          <span class="contact-channel-badge" style="font-size:0.82rem;">
            <span class="contact-icon">✉️</span> <strong>tantraresearchcenter@gmail.com</strong>
          </span>
        </div>
      </div>
    </article>
'''

def update_reader_html():
    with open(READER_HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update session storage bounds check (p > 88 -> p > 108)
    content = re.sub(r'p\s*>\s*88', 'p > 108', content)
    content = re.sub(r'p\s*>\s*100', 'p > 108', content)

    # 2. Update numberOfPages in JSON-LD
    content = re.sub(r'"numberOfPages":\s*\d+', '"numberOfPages": 108', content)

    # 3. Update slider and bottom bar
    content = re.sub(r'id="page-slider"\s+class="page-slider"\s+min="1"\s+max="\d+"',
                     'id="page-slider" class="page-slider" min="1" max="108"', content)
    content = re.sub(r'id="page-counter-badge">Cover\s*•\s*1\s*/\s*\d+<',
                     'id="page-counter-badge">Cover • 1 / 108<', content)
    content = re.sub(r'goToPage\(88,\s*true\)', 'goToPage(108, true)', content)
    content = re.sub(r'goToPage\(100,\s*true\)', 'goToPage(108, true)', content)

    # 4. Update Index page (page-data-6)
    old_index_target = '''    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(108, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Colophon</span>
        <div class="index-card-info">
          <strong class="index-card-title">समापन पृष्ठ, मंगल श्लोक व आधिकारिक संपर्क</strong>
          <span class="index-card-desc">Benediction, Upanishad Shloka & Contacts</span>
        </div>
      </div>
      <span class="index-page-range">Page 100</span>
    </div>'''
    
    # We will search for the card before colophon
    ch6_index_card = '''    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(89, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 6</span>
        <div class="index-card-info">
          <strong class="index-card-title">नक्षत्रों का गहन पद एवं ग्रह विश्लेषण (अश्विनी, आश्लेषा, पुष्य)</strong>
          <span class="index-card-desc">Deep Pada Matrices, Degrees & Navamsha Reference</span>
        </div>
      </div>
      <span class="index-page-range">Pages 89 - 99</span>
    </div>'''

    new_index_cards = ch6_index_card + '''

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(100, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Ch 7</span>
        <div class="index-card-info">
          <strong class="index-card-title">सम्पूर्ण पंचांग फलित निर्देशिका (वार, तिथि, नक्षत्र, योग, करण)</strong>
          <span class="index-card-desc">Five Limbs of Time, Elements, 27 Yogas, 11 Karanas & Synthesis</span>
        </div>
      </div>
      <span class="index-page-range">Pages 100 - 107</span>
    </div>

    <div class="index-card" onclick="if(window.bookEngine) window.bookEngine.goToPage(108, true);">
      <div class="index-card-left">
        <span class="index-chapter-badge">Colophon</span>
        <div class="index-card-info">
          <strong class="index-card-title">समापन पृष्ठ, मंगल श्लोक व आधिकारिक संपर्क</strong>
          <span class="index-card-desc">Benediction, Upanishad Shloka & Contacts</span>
        </div>
      </div>
      <span class="index-page-range">Page 108</span>
    </div>'''

    # Pattern match for old Ch 6 card + old Colophon card in page-data-6
    pattern_index = re.compile(
        r'<div class="index-card" onclick="if\(window\.bookEngine\) window\.bookEngine\.goToPage\(89, true\);">.*?'
        r'<div class="index-card" onclick="if\(window\.bookEngine\) window\.bookEngine\.goToPage\(\d+, true\);">\s*'
        r'<div class="index-card-left">\s*<span class="index-chapter-badge">Colophon</span>.*?'
        r'<span class="index-page-range">Page \d+</span>\s*</div>',
        re.DOTALL
    )
    content = pattern_index.sub(new_index_cards, content)

    # 5. Update TOC drawer (replace old P.100 item with Ch 7 items + P.108)
    toc_panchang = '''        <div class="toc-chapter-header">
          <span class="toc-chapter-pill">📌 Ch 7: सम्पूर्ण पंचांग फलित निर्देशिका</span>
        </div>
        

    <a href="#page-100" class="toc-item" data-goto="100">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.100</span>
        <span class="toc-item-title">पंचांग आधार: पंच-महाभूत एवं 7 सौर वार फलित</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>
    

    <a href="#page-101" class="toc-item" data-goto="101">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.101</span>
        <span class="toc-item-title">30 तिथियां, 5 श्रेणियां एवं फलित प्रभाव</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>
    

    <a href="#page-102" class="toc-item" data-goto="102">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.102</span>
        <span class="toc-item-title">27 नक्षत्र फलित ज्ञानकोश (भाग 1: अश्विनी से पूर्वाफाल्गुनी)</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>
    

    <a href="#page-103" class="toc-item" data-goto="103">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.103</span>
        <span class="toc-item-title">27 नक्षत्र फलित ज्ञानकोश (भाग 2: चित्रा से रेवती)</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>
    

    <a href="#page-104" class="toc-item" data-goto="104">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.104</span>
        <span class="toc-item-title">27 योग: सौर-चन्द्र कोणीय गणित व फलित सूत्र</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>
    

    <a href="#page-105" class="toc-item" data-goto="105">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.105</span>
        <span class="toc-item-title">11 करण: 7 चर व 4 स्थिर करण कर्म-दक्षता</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>
    

    <a href="#page-106" class="toc-item" data-goto="106">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.106</span>
        <span class="toc-item-title">पंचांग फलित संश्लेषण विधान व त्रि-स्तरीय सूत्र</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>
    

    <a href="#page-107" class="toc-item" data-goto="107">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.107</span>
        <span class="toc-item-title">पंच-महाभूत अधिभावी नियम व विरोधाभास समाधान</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>
    

        <div class="toc-chapter-header">
          <span class="toc-chapter-pill">📌 उपसंहार</span>
        </div>
        

    <a href="#page-108" class="toc-item" data-goto="108">
      <div class="toc-item-left">
        <span class="toc-page-badge">P.108</span>
        <span class="toc-item-title">समापन पृष्ठ • उपसंहार व वैदिक मंगल कामना</span>
      </div>
      <span class="toc-item-arrow">›</span>
    </a>'''

    toc_pattern = re.compile(
        r'<div class="toc-chapter-header">\s*<span class="toc-chapter-pill">📌 उपसंहार</span>\s*</div>\s*'
        r'<a href="#page-100" class="toc-item" data-goto="100">.*?</a>',
        re.DOTALL
    )
    content = toc_pattern.sub(toc_panchang, content)

    # 6. Replace old page-data-100 with pages 100 to 108
    panchang_pages = generate_panchang_pages_html()
    article_pattern = re.compile(
        r'<article class="book-page-data" id="page-data-100".*?</article>',
        re.DOTALL
    )
    content = article_pattern.sub(panchang_pages.strip(), content)

    with open(READER_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully updated reader.html with 108 pages and Panchang Guide")

    # Mirror to book.html
    with open(BOOK_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully mirrored updated reader.html to book.html")

def update_index_html():
    with open(INDEX_HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update book 1 thumb tag & desc
    content = content.replace("Vol 1 • 100 Pages", "Vol 1 • 108 Pages")
    content = content.replace("100 पृष्ठ • 12 चक्र", "108 पृष्ठ • 13 चक्र • सम्पूर्ण पंचांग फलित निर्देशिका")
    content = content.replace("दीप्तादि अवस्थाएं व आयुर्-ज्योतिष।",
                              "दीप्तादि अवस्थाएं, आयुर्-ज्योतिष एवं सम्पूर्ण पंचांग फलित निर्देशिका (वार, तिथि, नक्षत्र, योग, करण)।")

    # Check if plate 27 is already added
    if 'panchang_mandala_chart.svg' not in content:
        # Add Plate 27 to plates showcase grid
        plate_27_html = '''
        <!-- Plate 27: Vedic Panchanga Mandala Chart -->
        <a href="reader.html#page-107" class="plate-thumb-card" title="27. पञ्चाङ्ग पञ्च-महाभूत काल-संयोजन महामण्डल चक्र (वार, तिथि, नक्षत्र, योग, करण)">
          <div class="plate-img-wrap">
            <img src="assets/icons/panchang_mandala_chart.svg" alt="पञ्चाङ्ग पञ्च-महाभूत काल-संयोजन महामण्डल चक्र" class="plate-thumb-img" loading="lazy">
            <span class="plate-badge" style="background:rgba(217,119,6,0.25); color:#fde68a; border-color:rgba(217,119,6,0.5);">पंचांग महामण्डल</span>
          </div>
          <div class="plate-thumb-name">27. पञ्चाङ्ग पञ्च-महाभूत महामण्डल चक्र</div>
          <div class="plate-thumb-desc">वार (अग्नि), तिथि (जल), नक्षत्र (वायु), योग (आकाश), करण (पृथ्वी) व संश्लेषण</div>
          <div class="plate-thumb-page">📖 वैदिक ज्योतिष अध्याय 7 →</div>
        </a>
      </div>'''
        content = content.replace('</div>\n    </section>\n\n    <!-- 20+ Diamond Charts Plate Showcase -->', '</div>\n    </section>')
        # Insert before the closing </div> of plates-grid
        content = re.sub(r'(<!-- Plate 26:.*?</div\s*>\s*</a>\s*)(</div>\s*</section>)',
                         r'\1' + plate_27_html + r'\n    </section>', content, flags=re.DOTALL)

    with open(INDEX_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully updated index.html with 108 pages & Plate 27")

if __name__ == "__main__":
    update_reader_html()
    update_index_html()
