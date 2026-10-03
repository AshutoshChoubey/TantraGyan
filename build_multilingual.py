#!/usr/bin/env python3
"""
Tantra Gyan Multilingual Edition Builder
Generates:
1. hindi.html  - Pure Hindi Edition (सम्पूर्ण हिन्दी संस्करण)
2. english.html - Pure English Edition (Complete English Edition)
While preserving index.html as the original bilingual (द्विभाषी) masterwork edition.
"""

import re
import html
import os
import build_book
from tables_data import *

# ------------------------------------------------------------------------------
# 1. CANONICAL 87 PAGE TITLES (PURE HINDI & PURE ENGLISH)
# ------------------------------------------------------------------------------

HINDI_TITLES = [
    'वैदिक ज्योतिष महाग्रंथ सरलीकृत',
    'मंगलाचरण — ॐ गं गणपतये नमः',
    'लेखक परिचय — ज्योतिषाचार्य आशुतोष कुमार चौबे',
    'ग्रंथ का उद्देश्य एवं आधारभूत संरचना',
    'तांत्रिक अनुशासन, आचार संहिता एवं वैधानिक परामर्श',
    'विषय-सूची (सम्पूर्ण ग्रंथ अनुक्रमणिका)',
    'सूर्य देव के संपूर्ण शास्त्रीय कारकत्व',
    'चन्द्रमा के संपूर्ण शास्त्रीय कारकत्व',
    'चन्द्रमा: शास्त्रीय ग्रंथ संदर्भ व फलित सूत्र',
    'चन्द्रमा: आधुनिक व्यावहारिक फलित व मानसिक विश्लेषण',
    'मंगल देव के संपूर्ण शास्त्रीय कारकत्व',
    'मंगल देव: शास्त्रीय ग्रंथ संदर्भ व पराक्रम सूत्र',
    'बृहस्पति (गुरु) के संपूर्ण शास्त्रीय कारकत्व',
    'शुक्र देव के संपूर्ण शास्त्रीय कारकत्व',
    'शनि देव के संपूर्ण शास्त्रीय कारकत्व व कर्म सिद्धांत',
    'शनि देव: प्रमुख शास्त्रीय एवं आधुनिक दृष्टिकोण',
    'बुध देव के संपूर्ण कारकत्व व बुद्धि-विवेक',
    'राहु देव के संपूर्ण कारकत्व व मायावी प्रभाव',
    'केतु देव के संपूर्ण कारकत्व व मोक्ष मार्ग',
    '१७ शास्त्रीय राजयोग एवं पंच महापुरुष योग (भाग १)',
    '१७ शास्त्रीय राजयोग एवं विपरीत राजयोग (भाग २)',
    'ग्रह गति, गोचर अवधि एवं विंशोत्तरी महादशा चक्र',
    'ग्रह दृष्टि तालिका एवं शास्त्रीय दृष्टि नियम',
    '२७ नक्षत्र, विस्तार व राशि सीमा तालिका',
    '२७ नक्षत्र, अधिष्ठाता देवता व पद नामाक्षर',
    'नक्षत्र, अधिष्ठाता देवता और स्वामी तालिका',
    'नक्षत्र स्वामी व दशा अधिपति सूत्र',
    '२७ नक्षत्र एवं स्वामी शास्त्रीय तालिका',
    '१२ राशियां, स्वामी व पंचमहाभूत तत्व',
    'राशियों के गुण, तत्व एवं स्वभाव वर्गीकरण',
    'राशियों का लिंग वर्गीकरण (पुरुष व स्त्री राशियां)',
    'राशियों की ध्रुवता (धनात्मक एवं ऋणात्मक स्वभाव)',
    'अग्नि तत्व राशियां: मेष, सिंह, धनु',
    'पृथ्वी तत्व राशियां: वृषभ, कन्या, मकर',
    'वायु तत्व राशियां: मिथुन, तुला, कुंभ',
    'जल तत्व राशियां: कर्क, वृश्चिक, मीन',
    'तत्व एवं गतिशीलता का संयुक्त वर्गीकरण',
    'चर, स्थिर, द्विस्वभाव व तत्व फलित नियम',
    'दीप्तादि ९ अवस्थाएं: ग्रहों की स्थिति व फल',
    'ग्रहों की नैसर्गिक व तात्कालिक मैत्री वर्गीकरण',
    'दीप्तादि अवस्थाएं, मूलत्रिकोण व स्वराशि तालिका',
    'ग्रह अवस्थाओं के व्यावहारिक फलित नियम',
    'ग्रहों के पांच प्रकार के संबंध (पंच संबंध)',
    '१२ भावों के स्थिर कारक ग्रह',
    'भाव कारक व भावेश का शास्त्रीय अंतर एवं विश्लेषण',
    'सूर्य देव: भाव १ से ६ फलित विचार',
    'सूर्य देव: भाव ७ से १२ फलित विचार',
    'सूर्य देव: मेष से कन्या राशि फल',
    'सूर्य देव: तुला से मीन राशि फल',
    'सूर्य देव: शारीरिक अंग व रोग संबंध',
    'चन्द्रमा: शारीरिक अंग व रोग संबंध',
    'मंगल देव: शारीरिक अंग व रोग संबंध',
    'बुध देव: शारीरिक अंग व रोग संबंध',
    'बृहस्पति (गुरु): शारीरिक अंग व रोग संबंध',
    'शुक्र देव: शारीरिक अंग व रोग संबंध',
    'शनि देव: शारीरिक अंग व रोग संबंध',
    'राहु देव: शारीरिक अंग व रोग संबंध',
    'केतु देव: शारीरिक अंग व रोग संबंध',
    'प्रथम भाव (लग्न): शारीरिक अंग व रोग निदान',
    'द्वितीय भाव: शारीरिक अंग व रोग निदान',
    'तृतीय भाव: शारीरिक अंग व रोग निदान',
    'चतुर्थ भाव: शारीरिक अंग व रोग निदान',
    'पंचम भाव: शारीरिक अंग व रोग निदान',
    'षष्ठ भाव: शारीरिक अंग व रोग निदान',
    'सप्तम भाव: शारीरिक अंग व रोग निदान',
    'अष्टम भाव: शारीरिक अंग व रोग निदान',
    'नवम भाव: शारीरिक अंग व रोग निदान',
    'दशम भाव: शारीरिक अंग व रोग निदान',
    'एकादश भाव: शारीरिक अंग व रोग निदान',
    'द्वादश भाव: शारीरिक अंग व रोग निदान',
    '१२ भाव, शारीरिक अंग एवं व्याधि समन्वय तालिका',
    '१२ राशियां, शारीरिक अंग और विशिष्ट रोग तालिका',
    'कैंसर (अर्भुद रोग) के ज्योतिषीय कारण व मुख्य बिंदु',
    'सामान्य कैंसर (स्तन व फेफड़े): ग्रह योग व विश्लेषण',
    'रक्त कैंसर (ल्यूकीमिया): ज्योतिषीय योग व विश्लेषण',
    'त्वचा कैंसर (मेलानोमा): ग्रह योग व विश्लेषण',
    '२७ नक्षत्र, विस्तार व राशि सीमा विभाजन',
    '२७ नक्षत्र, देवता व पद नामाक्षर तालिका',
    'नक्षत्र, देवता एवं ग्रह स्वामी तालिका',
    'नक्षत्र स्वामी व दशा अधिपति शास्त्रीय सूत्र',
    '२७ नक्षत्र एवं स्वामी सम्पूर्ण ज्ञानकोश तालिका',
    'आश्लेषा नक्षत्र: ४ पद एवं ग्रह फल विश्लेषण',
    'पुष्य नक्षत्र: ४ पद एवं नवमांश ग्रह प्रभाव',
    'अश्विनी नक्षत्र: ४ पद व नवमांश अधिपति तालिका',
    'अश्विनी नक्षत्र: पद ध्वनि, प्रतीक व मूल स्वभाव',
    'अश्विनी नक्षत्र में ९ ग्रहों का फलित विश्लेषण',
    'अश्विनी नक्षत्र: ४ पद, नवमांश व ग्रह संबंध सारांश',
    'समापन पृष्ठ • उपसंहार व वैदिक मंगल कामना'
]

ENGLISH_TITLES = [
    'Complete Vedic Astrology Compendium Simplified',
    'Auspicious Invocation — Om Gam Ganapataye Namah',
    'Author Profile — Astrologer Ashutosh Kumar Choubey',
    'Reader\'s Study Guide & Core Architecture',
    'Tantric Ethics, Code of Conduct & Legal Disclaimer',
    'Systematic Table of Contents',
    'Sun (Surya) Significations & Karakatvas',
    'Moon (Chandra) Significations & Karakatvas',
    'Moon in Classical Treatises & Shastric Citations',
    'Moon: Modern Analytical Perspectives & Psychological Impacts',
    'Mars (Mangala) Significations & Karakatvas',
    'Mars in Classical Treatises & Shastric Citations',
    'Jupiter (Brihaspati) Significations & Karakatvas',
    'Venus (Shukra) Significations & Karakatvas',
    'Saturn (Shani) Significations & Karmic Principles',
    'Saturn in Classical & Modern Analytical Perspectives',
    'Mercury (Budha) Significations & Intellectual Karakatvas',
    'Rahu Significations & Shadow Matrix Karakatvas',
    'Ketu Significations & Spiritual Liberation Karakatvas',
    '17 Classical Raja Yogas & Pancha Mahapurusha (Part 1)',
    '17 Classical Raja Yogas & Viparita Raja Yogas (Part 2)',
    'Planetary Motion, Transit Times & Vimshottari Mahadasha',
    'Planetary Drishti Table & Classical Aspect Rules',
    '27 Nakshatras: Degree Spans & Zodiac Boundaries',
    '27 Nakshatras: Deities & Pada Phonetic Syllables',
    'Nakshatras, Presiding Deities & Planetary Lords',
    'Nakshatra Lords & Vimshottari Dasha Rulers',
    '27 Nakshatras & Rulers Master Reference Table',
    '12 Zodiac Signs, Planetary Rulers & Elements',
    'Zodiac Signs: Gunas, Elements & Modalities',
    'Gender Classification of Zodiac Signs (Masculine & Feminine)',
    'Polarity of Zodiac Signs (Positive & Negative)',
    'Fire Signs (Agni Tattva): Aries, Leo, Sagittarius',
    'Earth Signs (Prithvi Tattva): Taurus, Virgo, Capricorn',
    'Air Signs (Vayu Tattva): Gemini, Libra, Aquarius',
    'Water Signs (Jala Tattva): Cancer, Scorpio, Pisces',
    'Combined Classification of Elements & Modality',
    'Predictive Rules for Sign Modality & Cosmic Elements',
    'Deeptadi 9 States: Planetary Conditions & Potencies',
    'Planetary Friendship Matrix: Natural & Temporal Relations',
    'Deeptadi Avasthas, Moolatrikona & Own Sign Matrix',
    'Operational Predictive Principles for Planetary States',
    'Five Types of Planetary Relationships (Pancha Sambandha)',
    'Fixed Karakas (Significators) of the 12 Houses',
    'Bhava Karaka vs Bhavesha: Core Distinctions & Rules',
    'Sun in Houses 1 to 6: Classical Interpretations',
    'Sun in Houses 7 to 12: Classical Interpretations',
    'Sun in Signs 1 to 6: Aries to Virgo Interpretations',
    'Sun in Signs 7 to 12: Libra to Pisces Interpretations',
    'Sun: Anatomical Governance & Pathology',
    'Moon: Anatomical Governance & Pathology',
    'Mars: Anatomical Governance & Pathology',
    'Mercury: Anatomical Governance & Pathology',
    'Jupiter: Anatomical Governance & Pathology',
    'Venus: Anatomical Governance & Pathology',
    'Saturn: Anatomical Governance & Pathology',
    'Rahu: Anatomical Governance & Pathology',
    'Ketu: Anatomical Governance & Pathology',
    '1st House (Lagna): Anatomy & Clinical Pathologies',
    '2nd House: Anatomy & Clinical Pathologies',
    '3rd House: Anatomy & Clinical Pathologies',
    '4th House: Anatomy & Clinical Pathologies',
    '5th House: Anatomy & Clinical Pathologies',
    '6th House: Anatomy & Clinical Pathologies',
    '7th House: Anatomy & Clinical Pathologies',
    '8th House: Anatomy & Clinical Pathologies',
    '9th House: Anatomy & Clinical Pathologies',
    '10th House: Anatomy & Clinical Pathologies',
    '11th House: Anatomy & Clinical Pathologies',
    '12th House: Anatomy & Clinical Pathologies',
    'Astrological Houses vs Body Parts & Disease Matrix',
    'Zodiac Signs, Anatomical Zones & Specific Ailments',
    'Oncology in Vedic Astrology: Cellular Pathogenesis & Etiology',
    'General Carcinoma (Breast & Lung Cancer): Astrological Factors',
    'Leukemia (Blood Cancer): Astrological Combinations & Analysis',
    'Cutaneous Malignancies (Skin Cancer): Astrological Diagnostics',
    '27 Nakshatras: Degree Boundaries & Rashi Spans',
    '27 Nakshatras: Deities & Pada Phonetic Syllables',
    'Nakshatras, Presiding Deities & Planetary Lords',
    'Nakshatra Lordship Classical Sutra & Dasha Sequence',
    '27 Nakshatras & Planetary Lords Compendium Table',
    'Ashlesha Nakshatra: 4 Padas & Planetary Influences',
    'Pushya Nakshatra: 4 Padas & Navamsha Influences',
    'Ashwini Nakshatra: 4 Padas & Navamsha Lords Table',
    'Ashwini Padas: Phonetics, Symbolism & Core Characteristics',
    'Planetary Placements in Ashwini Nakshatra (Sun to Ketu)',
    'Ashwini Padas: Navamsha & Planetary Relations Synthesis',
    'Closing Epilogue • Vedic Peace Benediction & Back Cover'
]

def get_chapter_name(page_idx, lang='hindi'):
    if lang == 'hindi':
        if page_idx == 0: return "मुखपृष्ठ • Cover"
        if page_idx == 1: return "मंगलाचरण • Invocation"
        if page_idx == 2: return "लेखक परिचय • About the Author"
        if page_idx == 3: return "अध्ययन निर्देशिका • Study Guide"
        if page_idx == 4: return "आचार संहिता • Code of Conduct"
        if page_idx == 5: return "अनुक्रमणिका • Index"
        if 6 <= page_idx <= 20: return "अध्याय २: नवग्रह कारकत्व व राजयोग"
        if 21 <= page_idx <= 37: return "अध्याय ३: राशि, नक्षत्र एवं ग्रह गति"
        if 38 <= page_idx <= 48: return "अध्याय ४: भाव एवं राशियों में ग्रह"
        if 49 <= page_idx <= 75: return "अध्याय ५: आयुर्वेद-ज्योतिष व स्वास्थ्य"
        if 76 <= page_idx <= 86: return "अध्याय ६: नक्षत्र पद व ग्रह विश्लेषण"
        return "उपसंहार • Back Cover"
    else:
        if page_idx == 0: return "Front Cover"
        if page_idx == 1: return "Auspicious Invocation"
        if page_idx == 2: return "Author Profile"
        if page_idx == 3: return "Study Guide"
        if page_idx == 4: return "Ethics & Disclaimer"
        if page_idx == 5: return "Table of Contents"
        if 6 <= page_idx <= 20: return "Ch 2: Planetary Karakatva & Raja Yogas"
        if 21 <= page_idx <= 37: return "Ch 3: Signs, Nakshatras & Planetary Motion"
        if 38 <= page_idx <= 48: return "Ch 4: Planetary States & House Placements"
        if 49 <= page_idx <= 75: return "Ch 5: Medical Astrology & Diagnostics"
        if 76 <= page_idx <= 86: return "Ch 6: Nakshatra Padas & Planetary Analysis"
        return "Back Cover • Epilogue"

# ------------------------------------------------------------------------------
# 2. TABLE HEADER LOCALIZATION DICTIONARIES
# ------------------------------------------------------------------------------
hindi_headers = {
    '#': 'क्र.',
    'No.': 'क्र.',
    '1st Pada': 'प्रथम पद (१)',
    '2nd Pada': 'द्वितीय पद (२)',
    '3rd Pada': 'तृतीय पद (३)',
    '4th Pada': 'चतुर्थ पद (४)',
    'Ashwini Pad': 'अश्विनी पद',
    'Avastha (State)': 'ग्रह अवस्था',
    'Avg. Time per Rashi': 'औसत गोचर अवधि (प्रति राशि)',
    'Body Parts / Organs (शरीर के अंग / अंग तंत्र)': 'शरीर के अंग व तंत्र',
    'Combination': 'ग्रह संयोजन',
    'Context (संदर्भ)': 'शास्त्रीय संदर्भ',
    'Core Characteristic in Ashwini': 'अश्विनी में मूल विशेषता',
    'Debilitation (Neecha)': 'नीच राशि',
    'Deena (Neutral Sign)': 'दीन अवस्था (सम राशि)',
    'Deepta (Exalted)': 'दीप्त अवस्था (उच्च राशि)',
    'Deity (Devata)': 'अधिष्ठाता देवता',
    'Description &amp; Effects': 'विवरण एवं प्रभाव',
    'Description &amp; Effects (विवरण और प्रभाव)': 'विवरण एवं प्रभाव',
    'Description (English)': 'शास्त्रीय विवरण',
    'Description (विवरण)': 'शास्त्रीय विवरण',
    'Devata': 'अधिष्ठाता देवता',
    'Devata (देवता)': 'अधिष्ठाता देवता',
    'Diseases (रोग)': 'संबंधित रोग व विकार',
    'Dual Sign': 'द्विस्वभाव राशि',
    'Duality': 'ध्रुवता',
    'Dukhi (Enemy’s Sign)': 'दुःखी अवस्था (शत्रु राशि)',
    'Element': 'तत्व',
    'Ending': 'समापन अंश',
    'Enemies': 'शत्रु ग्रह',
    'English Significations': 'शास्त्रीय कारकत्व',
    'Exaltation (Uchha)': 'उच्च राशि',
    'Fixed Sign': 'स्थिर राशि',
    'Friends': 'मित्र ग्रह',
    'Gender': 'लिंग',
    'Graha': 'ग्रह',
    'Guna': 'गुण',
    'Hindi Name': 'नाम',
    'House (भाव)': 'भाव',
    'Keywords': 'संकेतक शब्द',
    'Khala (Great Enemy’s Sign)': 'खल अवस्था (अति शत्रु राशि)',
    'Kopi (Combust)': 'कोप अवस्था (अस्त ग्रह)',
    'Lord': 'स्वामी ग्रह',
    'Lord (Planet)': 'स्वामी ग्रह',
    'Main Sign (D1)': 'लग्न राशि (डी-१)',
    'Meaning and Characteristics': 'अर्थ एवं शास्त्रीय विशेषताएं',
    'Mercury (English)': 'बुध विवरण',
    'Mitra Rashi (Friendly Signs)': 'मित्र राशियां',
    'Mobility Type': 'स्वभाव (चर/स्थिर/द्विस्वभाव)',
    'Modality': 'स्वभाव वर्गीकरण',
    'Mooltrikona': 'मूलत्रिकोण',
    'Mooltrikona (Own Sign)': 'मूलत्रिकोण व स्वराशि',
    'Movability': 'गतिशीलता',
    'Movable Sign': 'चर राशि',
    'Mudit (Great Friend’s Sign)': 'मुदित अवस्था (अति मित्र राशि)',
    'Nakshatra': 'नक्षत्र',
    'Nakshatra (English)': 'नक्षत्र',
    'Nakshatra (नक्षत्र)': 'नक्षत्र',
    'Navamsa Lord': 'नवमांश स्वामी',
    'Navamsa Sign': 'नवमांश राशि',
    'Navamsa Sign (D9)': 'नवमांश राशि (डी-९)',
    'Neutral': 'सम ग्रह',
    'Orbital Period/Total for 12 Rashis': 'भचक्र भ्रमण काल (१२ राशियां)',
    'Pada': 'पद',
    'Pada 1 – Leo Navamsha (Sun)': 'पद १ – सिंह नवमांश (सूर्य)',
    'Pada 1 – Sagittarius (Jupiter)': 'पद १ – धनु नवमांश (गुरु)',
    'Pada 1: Aries Navamsa (Chu)': 'पद १: मेष नवमांश (चू)',
    'Pada 2 – Capricorn (Saturn)': 'पद २ – मकर नवमांश (शनि)',
    'Pada 2 – Virgo Navamsha (Mercury)': 'पद २ – कन्या नवमांश (बुध)',
    'Pada 2: Taurus Navamsa (Che)': 'पद २: वृष नवमांश (चे)',
    'Pada 3 – Aquarius (Saturn)': 'पद ३ – कुंभ नवमांश (शनि)',
    'Pada 3 – Libra Navamsha (Venus)': 'पद ३ – तुला नवमांश (शुक्र)',
    'Pada 3: Gemini Navamsa (Cho)': 'पद ३: मिथुन नवमांश (चो)',
    'Pada 4 – Pisces (Jupiter)': 'पद ४ – मीन नवमांश (गुरु)',
    'Pada 4 – Scorpio Navamsha (Mars)': 'पद ४ – वृश्चिक नवमांश (मंगल)',
    'Pada 4: Cancer Navamsa (La)': 'पद ४: कर्क नवमांश (ला)',
    'Phonetic Sound': 'नामाक्षर ध्वनि',
    'Planet': 'ग्रह',
    'Planet (ग्रह)': 'ग्रह',
    'Planet / Theme': 'ग्रह / विषय',
    'Planet in Ashwini': 'अश्विनी में ग्रह',
    'Planet&#x27;s Position': 'ग्रह स्थिति',
    'Planetary Combination (ग्रहों का संयोजन)': 'ग्रहों का संयोजन',
    'Rajyoga Name': 'राजयोग का नाम',
    'Rashi (Zodiac Sign)': 'राशि',
    'Rashi Number': 'राशि संख्या',
    'Ruler (नक्षत्र स्वामी)': 'नक्षत्र स्वामी',
    'Ruling Rashi (Sign)': 'अधिपति राशि',
    'Scholarly Consensus (विद्वानों की राय)': 'विद्वानों का शास्त्रीय मत',
    'Scholarly Consensus or Controversy': 'शास्त्रीय मत व विश्लेषण',
    'Shanta (Friend’s Sign)': 'शांत अवस्था (मित्र राशि)',
    'Shatru Rashi (Enemy Signs)': 'शत्रु राशियां',
    'Sign': 'राशि',
    'Special Aspects (विशेष दृष्टि)': 'विशेष दृष्टि',
    'Standard Aspect (सामान्य दृष्टि)': 'सामान्य दृष्टि (सप्तम)',
    'Starting': 'प्रारंभिक अंश',
    'Swastha (Own Sign)': 'स्वस्थ अवस्था (स्वराशि)',
    'Symbol (English)': 'प्रतीक',
    'Total Drishti Directions': 'कुल दृष्टि दिशाएं',
    'Type of Relationship (संबंध का प्रकार)': 'संबंध का प्रकार',
    'Varna': 'वर्ण',
    'Verified &amp; Refined Value (सत्यापित और परिशोधित विवरण)': 'सत्यापित शास्त्रीय विवरण',
    'Verified Value (सत्यापित विवरण)': 'सत्यापित विवरण',
    'Vikala (Malefic’s Sign)': 'विकल अवस्था (अशुभ प्रभाव)',
    'Vimshottari Mahadasha (years)': 'विंशोत्तरी महादशा (वर्ष)',
    'Yoga Name (योग का नाम)': 'योग का नाम',
    'कारक ग्रह (Karaka Planet)': 'कारक ग्रह',
    'गुण': 'गुण',
    'गुण (Guna / Quality)': 'गुण',
    'ग्रंथ (Text)': 'शास्त्रीय ग्रंथ',
    'चन्द्र का संकेतक/कारकत्व (Moon’s Karakatva)': 'चन्द्रमा का कारकत्व',
    'चन्द्र का संकेतक/कारकत्व (Moon’s Significations)': 'चन्द्रमा का कारकत्व',
    'चन्द्र के संदर्भ (Key Mentions)': 'चन्द्रमा के शास्त्रीय संदर्भ',
    'तत्व (Tatva / Element)': 'तत्व',
    'देवता': 'अधिष्ठाता देवता',
    'ध्रुव (Polarity)': 'ध्रुवता',
    'नक्षत्र (हिंदी)': 'नक्षत्र नाम',
    'नक्षत्र स्वामी (ग्रह)': 'नक्षत्र स्वामी',
    'प्रतीक': 'प्रतीक चिन्ह',
    'बीमारियाँ (Diseases)': 'रोग एवं स्वास्थ्य विकार',
    'बुध (हिंदी)': 'बुध विवरण',
    'भाव (Bhava)': 'भाव',
    'भाव का नाम (House Name)': 'भाव का नाम',
    'मंगल का संकेतक/कारकत्व (Mars’s Karakatva)': 'मंगल का कारकत्व',
    'मंगल के संदर्भ (Key Mentions)': 'मंगल के शास्त्रीय संदर्भ',
    'मुख्य शरीर के अंग (Primary Body Parts)': 'मुख्य शारीरिक अंग',
    'राशि (Rashi) - Sign': 'राशि',
    'राशियाँ (Rashiyan / Signs)': 'राशियां',
    'राशियाँ (Signs)': 'राशियां',
    'लग्न (Lagna)': 'लग्न भाव',
    'लिंग (Gender)': 'लिंग',
    'वर्ण': 'वर्ण',
    'विवरण (हिंदी में)': 'शास्त्रीय विवरण',
    'विवरण (हिन्दी)': 'शास्त्रीय विवरण',
    'विशिष्ट बीमारियाँ (Specific Diseases)': 'विशिष्ट रोग विकार',
    'विषय': 'विषय',
    'विषय (Category)': 'श्रेणी व विषय',
    'शनि का वर्णन (संक्षेप में)': 'शनि देव का शास्त्रीय वर्णन',
    'शरीर के अंग (Body Parts)': 'शारीरिक अंग',
    'शुक्र का संकेतक/कारकत्व (Karakatva of Venus)': 'शुक्र का कारकत्व',
    'श्रेणी (Category)': 'श्रेणी',
    'संबंधित शब्द (Keywords)': 'संकेतक शब्द',
    'सूर्य (Surya)': 'सूर्य देव',
    'सूर्य का संकेतक/कारकत्व (Sun’s Karakatva)': 'सूर्य का कारकत्व',
    'स्रोत (References)': 'शास्त्रीय स्रोत',
    'स्रोत (Source)': 'शास्त्रीय स्रोत',
    'स्वभाव और विशेषताएँ (Nature &amp; Keywords)': 'स्वभाव एवं शास्त्रीय विशेषताएं',
    'हिन्दी संकेत': 'शास्त्रीय संकेत',
    '🌐 ग्रह (Planet)': 'ग्रह',
    '💡 याद करने की ट्रिक': 'स्मरण सूत्र',
    '📜 नक्षत्र (Sanskrit + English)': 'नक्षत्र नाम',
    '🔢 नक्षत्र संख्या': 'नक्षत्र संख्या',
    '🔸 श्रेणी': 'श्रेणी',
    '🔹 विवरण (केतु से संबंधित)': 'केतु देव का विवरण'
}

english_headers = {
    '#': '#',
    'No.': 'No.',
    '1st Pada': 'Pada 1 (1st Quarter)',
    '2nd Pada': 'Pada 2 (2nd Quarter)',
    '3rd Pada': 'Pada 3 (3rd Quarter)',
    '4th Pada': 'Pada 4 (4th Quarter)',
    'Ashwini Pad': 'Ashwini Pada',
    'Avastha (State)': 'Planetary State (Avastha)',
    'Avg. Time per Rashi': 'Avg. Transit Time per Sign',
    'Body Parts / Organs (शरीर के अंग / अंग तंत्र)': 'Anatomical Organs & Systems',
    'Combination': 'Planetary Combination',
    'Context (संदर्भ)': 'Classical Context',
    'Core Characteristic in Ashwini': 'Core Characteristic in Ashwini',
    'Debilitation (Neecha)': 'Debilitation Sign (Neecha)',
    'Deena (Neutral Sign)': 'Deena (Neutral Sign Placement)',
    'Deepta (Exalted)': 'Deepta (Exalted State)',
    'Deity (Devata)': 'Presiding Deity (Devata)',
    'Description &amp; Effects': 'Description & Predictive Effects',
    'Description &amp; Effects (विवरण और प्रभाव)': 'Description & Predictive Effects',
    'Description (English)': 'Description',
    'Description (विवरण)': 'Classical Description',
    'Devata': 'Presiding Deity',
    'Devata (देवता)': 'Presiding Deity (Devata)',
    'Diseases (रोग)': 'Associated Pathologies & Afflictions',
    'Dual Sign': 'Dual Sign (Dvisvabhava)',
    'Duality': 'Polarity (Positive / Negative)',
    'Dukhi (Enemy’s Sign)': 'Dukhi (Enemy Sign Placement)',
    'Element': 'Cosmic Element (Tattva)',
    'Ending': 'Ending Degree',
    'Enemies': 'Enemy Planets (Shatru)',
    'English Significations': 'Significations & Karakatva',
    'Exaltation (Uchha)': 'Exaltation Sign (Uchcha)',
    'Fixed Sign': 'Fixed Sign (Sthira)',
    'Friends': 'Friendly Planets (Mitra)',
    'Gender': 'Gender Classification',
    'Graha': 'Planet (Graha)',
    'Guna': 'Guna (Sattva / Rajas / Tamas)',
    'Hindi Name': 'Traditional Name',
    'House (भाव)': 'Astrological House (Bhava)',
    'Keywords': 'Key Significations',
    'Khala (Great Enemy’s Sign)': 'Khala (Great Enemy Sign)',
    'Kopi (Combust)': 'Kopi (Combust State)',
    'Lord': 'Planetary Ruler (Lord)',
    'Lord (Planet)': 'Planetary Ruler',
    'Main Sign (D1)': 'Birth Chart Sign (D1)',
    'Meaning and Characteristics': 'Meaning & Characteristics',
    'Mercury (English)': 'Mercury Significations',
    'Mitra Rashi (Friendly Signs)': 'Friendly Signs (Mitra)',
    'Mobility Type': 'Mobility (Movable / Fixed / Dual)',
    'Modality': 'Sign Modality',
    'Mooltrikona': 'Moolatrikona Sign',
    'Mooltrikona (Own Sign)': 'Moolatrikona & Own Sign',
    'Movability': 'Mobility Nature',
    'Movable Sign': 'Movable Sign (Chara)',
    'Mudit (Great Friend’s Sign)': 'Mudita (Great Friend Sign)',
    'Nakshatra': 'Nakshatra (Lunar Mansion)',
    'Nakshatra (English)': 'Nakshatra',
    'Nakshatra (नक्षत्र)': 'Nakshatra (Lunar Mansion)',
    'Navamsa Lord': 'Navamsha Lord',
    'Navamsa Sign': 'Navamsha Sign (D9)',
    'Navamsa Sign (D9)': 'Navamsha Sign (D9)',
    'Neutral': 'Neutral Planets (Sama)',
    'Orbital Period/Total for 12 Rashis': 'Total Zodiac Orbital Period',
    'Pada': 'Pada (Quarter)',
    'Pada 1 – Leo Navamsha (Sun)': 'Pada 1 – Leo Navamsha (Sun)',
    'Pada 1 – Sagittarius (Jupiter)': 'Pada 1 – Sagittarius Navamsha (Jupiter)',
    'Pada 1: Aries Navamsa (Chu)': 'Pada 1: Aries Navamsha (Chu)',
    'Pada 2 – Capricorn (Saturn)': 'Pada 2 – Capricorn Navamsha (Saturn)',
    'Pada 2 – Virgo Navamsha (Mercury)': 'Pada 2 – Virgo Navamsha (Mercury)',
    'Pada 2: Taurus Navamsa (Che)': 'Pada 2: Taurus Navamsha (Che)',
    'Pada 3 – Aquarius (Saturn)': 'Pada 3 – Aquarius Navamsha (Saturn)',
    'Pada 3 – Libra Navamsha (Venus)': 'Pada 3 – Libra Navamsha (Venus)',
    'Pada 3: Gemini Navamsa (Cho)': 'Pada 3: Gemini Navamsha (Cho)',
    'Pada 4 – Pisces (Jupiter)': 'Pada 4 – Pisces Navamsha (Jupiter)',
    'Pada 4 – Scorpio Navamsha (Mars)': 'Pada 4 – Scorpio Navamsha (Mars)',
    'Pada 4: Cancer Navamsa (La)': 'Pada 4: Cancer Navamsha (La)',
    'Phonetic Sound': 'Phonetic Syllable',
    'Planet': 'Planet (Graha)',
    'Planet (ग्रह)': 'Planet (Graha)',
    'Planet / Theme': 'Planet / Theme',
    'Planet in Ashwini': 'Planet in Ashwini',
    'Planet&#x27;s Position': 'Planetary Position',
    'Planetary Combination (ग्रहों का संयोजन)': 'Planetary Combination',
    'Rajyoga Name': 'Raja Yoga Name',
    'Rashi (Zodiac Sign)': 'Zodiac Sign (Rashi)',
    'Rashi Number': 'Sign Number',
    'Ruler (नक्षत्र स्वामी)': 'Nakshatra Lord (Ruler)',
    'Ruling Rashi (Sign)': 'Ruled Zodiac Sign',
    'Scholarly Consensus (विद्वानों की राय)': 'Classical Scholarly Consensus',
    'Scholarly Consensus or Controversy': 'Scholarly Perspectives',
    'Shanta (Friend’s Sign)': 'Shanta (Friend Sign Placement)',
    'Shatru Rashi (Enemy Signs)': 'Enemy Signs (Shatru)',
    'Sign': 'Zodiac Sign',
    'Special Aspects (विशेष दृष्टि)': 'Special Full Aspects',
    'Standard Aspect (सामान्य दृष्टि)': 'Standard 7th Aspect',
    'Starting': 'Starting Degree',
    'Swastha (Own Sign)': 'Svastha (Own Sign Placement)',
    'Symbol (English)': 'Astronomical Symbol',
    'Total Drishti Directions': 'Total Aspect Directions',
    'Type of Relationship (संबंध का प्रकार)': 'Type of Relationship',
    'Varna': 'Varna (Social Class)',
    'Verified &amp; Refined Value (सत्यापित और परिशोधित विवरण)': 'Verified Classical Description',
    'Verified Value (सत्यापित विवरण)': 'Verified Description',
    'Vikala (Malefic’s Sign)': 'Vikala (Combust / Afflicted State)',
    'Vimshottari Mahadasha (years)': 'Vimshottari Mahadasha (Years)',
    'Yoga Name (योग का नाम)': 'Yoga Name',
    'कारक ग्रह (Karaka Planet)': 'Significator Planet (Karaka)',
    'गुण': 'Guna (Nature)',
    'गुण (Guna / Quality)': 'Guna (Sattva / Rajas / Tamas)',
    'ग्रंथ (Text)': 'Classical Source Text',
    'चन्द्र का संकेतक/कारकत्व (Moon’s Karakatva)': 'Moon Significations (Karakatva)',
    'चन्द्र का संकेतक/कारकत्व (Moon’s Significations)': 'Moon Significations',
    'चन्द्र के संदर्भ (Key Mentions)': 'Moon Classical References',
    'तत्व (Tatva / Element)': 'Cosmic Element (Tattva)',
    'देवता': 'Presiding Deity',
    'ध्रुव (Polarity)': 'Polarity (Positive / Negative)',
    'नक्षत्र (हिंदी)': 'Nakshatra Name',
    'नक्षत्र स्वामी (ग्रह)': 'Nakshatra Lord',
    'प्रतीक': 'Symbol Emblem',
    'बीमारियाँ (Diseases)': 'Medical Afflictions & Diseases',
    'बुध (हिंदी)': 'Mercury Significations',
    'भाव (Bhava)': 'House (Bhava)',
    'भाव का नाम (House Name)': 'House Name',
    'मंगल का संकेतक/कारकत्व (Mars’s Karakatva)': 'Mars Significations (Karakatva)',
    'मंगल के संदर्भ (Key Mentions)': 'Mars Classical References',
    'मुख्य शरीर के अंग (Primary Body Parts)': 'Primary Anatomical Organs',
    'राशि (Rashi) - Sign': 'Zodiac Sign (Rashi)',
    'राशियाँ (Rashiyan / Signs)': 'Zodiac Signs',
    'राशियाँ (Signs)': 'Zodiac Signs',
    'लग्न (Lagna)': 'Ascendant (Lagna)',
    'लिंग (Gender)': 'Gender (Masculine / Feminine)',
    'वर्ण': 'Varna Classification',
    'विवरण (हिंदी में)': 'Classical Description',
    'विवरण (हिन्दी)': 'Classical Description',
    'विशिष्ट बीमारियाँ (Specific Diseases)': 'Specific Medical Pathologies',
    'विषय': 'Topic / Category',
    'विषय (Category)': 'Category',
    'शनि का वर्णन (संक्षेप में)': 'Saturn Classical Summary',
    'शरीर के अंग (Body Parts)': 'Anatomical Organs',
    'शुक्र का संकेतक/कारकत्व (Karakatva of Venus)': 'Venus Significations (Karakatva)',
    'श्रेणी (Category)': 'Category',
    'संबंधित शब्द (Keywords)': 'Associated Keywords',
    'सूर्य (Surya)': 'Sun (Surya)',
    'सूर्य का संकेतक/कारकत्व (Sun’s Karakatva)': 'Sun Significations (Karakatva)',
    'स्रोत (References)': 'Classical Citations',
    'स्रोत (Source)': 'Classical Source',
    'स्वभाव और विशेषताएँ (Nature &amp; Keywords)': 'Nature & Significations',
    'हिन्दी संकेत': 'Indic Significations',
    '🌐 ग्रह (Planet)': 'Planet (Graha)',
    '💡 याद करने की ट्रिक': 'Mnemonic Learning Rule',
    '📜 नक्षत्र (Sanskrit + English)': 'Nakshatra Name',
    '🔢 नक्षत्र संख्या': 'Nakshatra Index',
    '🔸 श्रेणी': 'Category',
    '🔹 विवरण (केतु से संबंधित)': 'Ketu Classical Description'
}

# ------------------------------------------------------------------------------
# 3. ADVANCED TABLE AND CELL LOCALIZATION ENGINES
# ------------------------------------------------------------------------------

def filter_table_columns(tbl_html, keep_indices):
    """Filters table columns by index to remove duplicated parallel language columns."""
    rows = re.findall(r'<tr[^>]*>.*?</tr>', tbl_html, re.DOTALL)
    if not rows:
        return tbl_html
    new_rows = []
    for row in rows:
        cells = re.findall(r'<(t[hd])[^>]*>(.*?)</\1>', row, re.DOTALL)
        if not cells:
            continue
        filtered_cells = [f'<{cells[idx][0]}>{cells[idx][1]}</{cells[idx][0]}>' for idx in keep_indices if idx < len(cells)]
        new_rows.append('<tr>' + ''.join(filtered_cells) + '</tr>')
    return '<table class="astro-table">' + ''.join(new_rows) + '</table>'

def clean_cell_text_to_hindi(s):
    # 1. Replace specific long English sentences and clinical notes first
    sentence_replacements = [
        ("Affliction to Lagna or Lagna lord indicates susceptibility to diseases in general.", "लग्न अथवा लग्नेश के पीड़ित होने पर सामान्य स्वास्थ्य में दुर्बलता व रोग प्रकटीकरण होता है।"),
        ("The planet in Lagna or aspecting Lagna, and Lagna lord's condition are key.", "लग्न में स्थित अथवा लग्न को देखने वाले ग्रह तथा लग्नेश की स्थिति मुख्य रोग प्रवृत्ति तय करती है।"),
        ("If afflicted, can indicate problems with sustenance leading to weakness.", "यदि यह भाव पीड़ित हो तो पोषण व आहार में बाधा तथा शारीरिक दुर्बलता उत्पन्न होती है।"),
        ("Courage and vitality impacted by afflictions here.", "यहाँ पाप प्रभाव होने पर पराक्रम, मनोबल एवं जीवन-ऊर्जा क्षीण होती है।"),
        ("Health of mother can be gauged. Emotional well-being is key.", "माता के स्वास्थ्य तथा जातक के मानसिक व संवेगात्मक स्वास्थ्य का निर्धारण होता है।"),
        ("Trouble in children", "संतान संबंधी कष्ट"),
        ("If afflicted, problems in progeny, education and speculative losses can cause mental stress leading to health issues.", "पीड़ित होने पर संतान कष्ट, विद्या में बाधा व आर्थिक हानि से उत्पन्न मानसिक तनाव स्वास्थ्य को बिगाड़ता है।"),
        ("This is the primary house of ill-health.", "यह रोग, व्याधि व रुग्णता का मुख्य प्राथमिक भाव है।"),
        ("Business or partnership stress affecting health.", "व्यापारिक व वैवाहिक साझेदारी का तनाव स्वास्थ्य को प्रभावित करता है।"),
        ("Afflictions indicate serious, long-term health issues or accidents.", "पाप प्रभाव होने पर गंभीर, दीर्घकालिक व्याधियां अथवा दुर्घटना का भय रहता है।"),
        ("Blessings of elders can improve health. Pilgrimages can cause health issues.", "गुरुजनों के आशीर्वाद से आरोग्य लाभ; तीर्थ यात्राओं में स्वास्थ्य के प्रति सजगता अपेक्षित।"),
        ("Stress from career and public image can impact health.", "कार्यक्षेत्र की व्यस्तता व प्रतिष्ठा का तनाव शारीरिक स्वास्थ्य पर प्रभाव डालता है।"),
        ("Financial stress or irregular income can lead to health issues.", "आर्थिक चिंता अथवा अनियमित आय से उत्पन्न मानसिक दबाव शारीरिक व्याधियों का कारण बनता है।"),
        ("Expenditure on health.", "चिकित्सा व औषधियों पर अत्यधिक व्यय।"),
        ("Health is generally good if Sun or Jupiter is here and strong; Mars here can give injuries to head", "यदि लग्न में सूर्य या गुरु बलवान हों तो स्वास्थ्य उत्तम रहता है; मंगल स्थित होने पर सिर में चोट या पित्त विकार संभव है।"),
        ("Unusual joint pains, skin issues related to work environment", "जोड़ों में असामान्य वेदना, कार्य वातावरण से त्वचा रोग"),
        ("Chronic pain in calves/ankles, hearing issues (left ear)", "पिंडलियों व टखनों में पुराना दर्द, बाएं कान में दुर्बलता"),
        ("Injuries to ankles/calves, ear infections", "टखनों व पिंडलियों में चोट, कान में संक्रमण"),
        ("Unusual pains/cramps in legs, sudden hearing issues", "पैरों में असामान्य ऐंठन, अचानक श्रवण दोष"),
        ("Chronic foot problems, sleep disorders, long hospitalization, depression", "पैरों की पुरानी व्याधियां, अनिद्रा, दीर्घकालिक चिकित्सालय वास, अवसाद"),
        ("Foot injuries, eye infections (left eye), accidents leading to hospitalization", "पैरों में चोट, बाईं आंख में संक्रमण, अस्पताल में भर्ती होने का योग"),
        ("Mysterious illnesses leading to hospitalization, addictions, sleep disturbances, phobias", "अस्पताल में भर्ती कराने वाली रहस्यमयी व्याधियां, व्यसन, निद्रा विकार, भय"),
        ("Moksha karaka, but if afflicted can give peculiar foot/eye issues, detachment leading to self-neglect", "मोक्ष कारक; पीड़ित होने पर पैरों व बाईं आंख में कष्ट, आत्म-उपेक्षा जन्य दुर्बलता")
    ]
    for orig_t, repl_t in sentence_replacements:
        s = s.replace(orig_t, repl_t)

    # 2. Planetary clinical notes regex replacements
    clinical_patterns = [
        (r'Saturn in Lagna:?\s*Chronic illness[^\.;]*', 'लग्न में शनि: दीर्घकालिक व्याधियां, शारीरिक दुर्बलता'),
        (r'Mars in Lagna:?\s*Injuries[^\.;]*', 'लग्न में मंगल: सिर में चोट, पित्त ज्वर, जलन'),
        (r'Rahu in Lagna:?\s*Mysterious illnesses[^\.;]*', 'लग्न में राहु: अज्ञात व रहस्यमयी व्याधियां, भय'),
        (r'Weak Lagna lord:?\s*General susceptibility[^\.;]*', 'निर्बल लग्नेश: रोग प्रतिरोधक क्षमता में कमी'),
        (r'Saturn in 2nd:?\s*Dental issues[^\.;]*', 'द्वितीय में शनि: दंत विकार, वाणी दोष'),
        (r'Mars in 2nd:?\s*Mouth ulcers[^\.;]*', 'द्वितीय में मंगल: मुख पाक (अल्सर), नेत्र प्रदाह'),
        (r'Rahu in 2nd:?\s*Unusual facial marks[^\.;]*', 'द्वितीय में राहु: चेहरे पर चिन्ह, वाणी विकार'),
        (r'Weak 2nd lord[^\.;]*', 'द्वितीयेश निर्बल होने पर पोषण में कमी'),
        (r'Saturn in 3rd:?\s*Chronic pain[^\.;]*', 'तृतीय में शनि: भुजाओं व कंधों में दर्द'),
        (r'Mars in 3rd:?\s*Injuries[^\.;]*', 'तृतीय में मंगल: भुजाओं में चोट, कान संक्रमण'),
        (r'Rahu in 3rd:?\s*Skin issues[^\.;]*', 'तृतीय में राहु: बाहों पर त्वचा विकार, वात नाड़ी दर्द'),
        (r'Saturn in 4th:?\s*Chronic lung issues[^\.;]*', 'चतुर्थ में शनि: फेफड़ों के पुराने रोग, अवसाद'),
        (r'Mars in 4th:?\s*Chest inflammation[^\.;]*', 'चतुर्थ में मंगल: वक्ष में प्रदाह, घरेलू तनाव'),
        (r'Rahu in 4th:?\s*Vague chest pains[^\.;]*', 'चतुर्थ में राहु: अनिर्दिष्ट छाती दर्द, भय'),
        (r'Saturn in 5th:?\s*Chronic heart issues[^\.;]*', 'पंचम में शनि: मंद पाचन, हृदय विकार, अवसाद'),
        (r'Mars in 5th:?\s*Heart inflammation[^\.;]*', 'पंचम में मंगल: अम्लपित्त, पित्त ज्वर'),
        (r'Rahu in 5th:?\s*Sudden heart issues[^\.;]*', 'पंचम में राहु: अचानक हृदय विकार, विषाक्त भोजन'),
        (r'Saturn in 6th:?\s*Chronic diseases[^\.;]*', 'षष्ठ में शनि: दीर्घकालिक असाध्य रोग, दुर्बलता'),
        (r'Mars in 6th:?\s*Acute illnesses[^\.;]*', 'षष्ठ में मंगल: तीव्र रोग, प्रदाह, शल्य चिकित्सा, रक्त विकार'),
        (r'Rahu in 6th:?\s*undiagnosable diseases[^\.;]*', 'षष्ठ में राहु: अनिदानित गूढ़ रोग, विष विकार, भय'),
        (r'Ketu in 6th:?\s*Diseases due to past karma[^\.;]*', 'षष्ठ में केतु: पूर्व संचित कर्म जन्य रोग, अचानक व्याधि'),
        (r'Saturn in 7th:?\s*Chronic kidney issues[^\.;]*', 'सप्तम में शनि: गुर्दे के पुराने रोग, यौन दुर्बलता'),
        (r'Mars in 7th:?\s*UTIs[^\.;]*', 'सप्तम में मंगल: मूत्र मार्ग संक्रमण, जननांग प्रदाह'),
        (r'Rahu in 7th:?\s*Unusual sexual problems[^\.;]*', 'सप्तम में राहु: असामान्य गुप्त रोग'),
        (r'Saturn in 8th:?\s*Long,?\s*debilitating[^\.;]*', 'अष्टम में शनि: अति दीर्घकालिक कष्टप्रद व्याधियां'),
        (r'Mars in 8th:?\s*Accidents[^\.;]*', 'अष्टम में मंगल: दुर्घटनाएं, शल्य चिकित्सा, तीव्र संकट'),
        (r'Rahu in 8th:?\s*Mysterious incurable diseases[^\.;]*', 'अष्टम में राहु: रहस्यमयी असाध्य रोग, विष विकार'),
        (r'Ketu in 8th:?\s*Diseases difficult to diagnose[^\.;]*', 'अष्टम में केतु: कठिन निदान वाली व्याधियां, शल्य क्रिया'),
        (r'Saturn in 9th:?\s*Chronic hip[^\.;]*', 'नवम में शनि: कूल्हे व जांघों में पुराना दर्द'),
        (r'Mars in 9th:?\s*Injuries to hips[^\.;]*', 'नवम में मंगल: कूल्हे व जांघ में चोट, पित्त ज्वर'),
        (r'Rahu in 9th:?\s*Unusual problems in hips[^\.;]*', 'नवम में राहु: जांघों में असामान्य कष्ट'),
        (r'Saturn in 10th:?\s*Chronic knee[^\.;]*', 'दशम में शनि: घुटनों व जोड़ों का पुराना दर्द'),
        (r'Mars in 10th:?\s*Knee injuries[^\.;]*', 'दशम में मंगल: घुटनों में चोट, जोड़ों में प्रदाह'),
        (r'Rahu in 10th:?\s*Unusual joint pains[^\.;]*', 'दशम में राहु: जोड़ों में असामान्य वेदना'),
        (r'Saturn in 11th:?\s*Chronic pain in calves[^\.;]*', 'एकादश में शनि: पिंडलियों व टखनों में पुराना दर्द'),
        (r'Mars in 11th:?\s*Injuries to ankles[^\.;]*', 'एकादश में मंगल: टखनों व पिंडलियों में चोट'),
        (r'Rahu in 11th:?\s*Unusual pains[^\.;]*', 'एकादश में राहु: पैरों में असामान्य ऐंठन, श्रवण दोष'),
        (r'Saturn in 12th:?\s*Chronic foot problems[^\.;]*', 'द्वादश में शनि: पैरों की पुरानी व्याधियां, अनिद्रा'),
        (r'Mars in 12th:?\s*Foot injuries[^\.;]*', 'द्वादश में मंगल: पैरों में चोट, बाईं आंख में संक्रमण'),
        (r'Rahu in 12th:?\s*Mysterious illnesses[^\.;]*', 'द्वादश में राहु: अस्पताल वास, रहस्यमयी व्याधियां'),
        (r'Ketu in 12th:?\s*Moksha karaka[^\.;]*', 'द्वादश में केतु: मोक्ष कारक; पीड़ित होने पर पैरों में कष्ट')
    ]
    for pat, repl in clinical_patterns:
        s = re.sub(pat, repl, s)

    # 3. Clean English inside parentheses (including nested)
    for _ in range(3):
        s = re.sub(r"\([A-Za-z0-9\s,\.\-\/\’\':;%&–—]+\)", '', s)

    # 4. Remove compound English like ' - Aries'
    s = re.sub(r'\s*-\s*[A-Za-z\s]+', '', s)

    # 5. Common terms translation
    terms = [
        (r'\bEsoteric\b', 'गूढ़'),
        (r'\bAthlete\b', 'धावक / खिलाड़ी'),
        (r'\bSatva\b', 'सत्व'),
        (r'\bRajas\b', 'रजस'),
        (r'\bTamas\b', 'तमस'),
        (r'\bKhana No\b', 'खाना नंबर'),
        (r'\bParashara\b', 'बृहत्पाराशर होरा शास्त्र'),
        (r'\bSaravali\b', 'सारावली (कल्याण वर्मा)'),
        (r'\bPhaladeepika\b|\bPhala Deepika\b', 'फलदीपिका (मन्त्रेश्वर)'),
        (r'\bJataka Parijata\b', 'जातक पारिजात'),
        (r'\bBNN Padhati\b|\bBhrigu Nandi Nadi\b|\bBNN\b', 'भृगु नन्दी नाड़ी'),
        (r'\bLaal Kitab\b|\bLal Kitab\b', 'लाल किताब'),
        (r'\bModern Research\b|\bResearch\b', 'आधुनिक चिकित्सा शोध'),
        (r'\bmooltrikona\b', 'मूलत्रिकोण'),
        (r'\bspecifically\b', 'विशेष रूप से'),
        (r'\bfrom\b', 'से'),
        (r'\bto\b', 'तक'),
        (r'\bsouth\b', 'दक्षिण'),
        (r'\bCenter\b', 'केंद्र'),
        (r'\bExalted\b', 'उच्च'),
        (r'\bDebilitated\b', 'नीच'),
        (r'\bRule\b', 'सूत्र'),
        (r'\bSun\b', 'सूर्य'),
        (r'\bMoon\b', 'चन्द्रमा'),
        (r'\bMars\b', 'मंगल'),
        (r'\bMercury\b', 'बुध'),
        (r'\bJupiter\b', 'गुरु (बृहस्पति)'),
        (r'\bVenus\b', 'शुक्र'),
        (r'\bSaturn\b', 'शनि'),
        (r'\bRahu\b', 'राहु'),
        (r'\bKetu\b', 'केतु'),
        (r'\bNone\b', 'कोई नहीं'),
        (r'\bAries\b', 'मेष'),
        (r'\bTaurus\b', 'वृष'),
        (r'\bGemini\b', 'मिथुन'),
        (r'\bCancer\b', 'कर्क'),
        (r'\bLeo\b', 'सिंह'),
        (r'\bVirgo\b', 'कन्या'),
        (r'\bLibra\b', 'तुला'),
        (r'\bScorpio\b', 'वृश्चिक'),
        (r'\bSagittarius\b', 'धनु'),
        (r'\bCapricorn\b', 'मकर'),
        (r'\bAquarius\b', 'कुंभ'),
        (r'\bPisces\b', 'मीन'),
        (r'\bDeepta\b', 'दीप्त'),
        (r'\bSwastha\b', 'स्वस्थ'),
        (r'\bMudit\b|\bMudita\b', 'मुदित'),
        (r'\bShanta\b', 'शांत'),
        (r'\bDeena\b', 'दीन'),
        (r'\bDukhi\b', 'दुःखी'),
        (r'\bVikala\b', 'विकल'),
        (r'\bKhala\b', 'खल'),
        (r'\bKopi\b', 'कोप'),
        (r'\bCardinal\b', 'चर'),
        (r'\bFixed\b', 'स्थिर'),
        (r'\bMutable\b', 'द्विस्वभाव'),
        (r'\bMovable\b', 'चर'),
        (r'\bPositive\b', 'धनात्मक'),
        (r'\bNegative\b', 'ऋणात्मक'),
        (r'\bMale\b', 'पुरुष'),
        (r'\bFemale\b', 'स्त्री')
    ]
    for pat, repl in terms:
        s = re.sub(pat, repl, s, flags=re.IGNORECASE)

    # 6. Remove any isolated English words remaining in text (preserving tags)
    parts = re.split(r'(<[^>]+>)', s)
    for i in range(len(parts)):
        if not parts[i].startswith('<'):
            parts[i] = re.sub(r'\b[A-Za-z]{2,}\b', '', parts[i])
    s = ''.join(parts)

    # Clean up empty parens and punctuation
    s = re.sub(r'\(\s*\)', '', s)
    s = re.sub(r',\s*,', ',', s)
    s = re.sub(r'^\s*,\s*', '', s)
    s = re.sub(r'\s*,\s*$', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def clean_cell_text_to_english(s):
    # 1. Clean compound patterns like 'मेष (Mesha) - Aries' -> 'Aries'
    s = re.sub(r'[ऀ-ॿ\s]+\(([A-Za-z]+)\)\s*-\s*([A-Za-z]+)', r'', s)
    # 2. If Hindi (English) -> extract English
    s = re.sub(r'[ऀ-ॿ\s\/–—\-]+\(([A-Za-z0-9\s,\.\-\/\’\':;%&–—]+)\)', r'', s)
    # 3. If English (Hindi) -> remove Hindi
    s = re.sub(r'\s*\([ऀ-ॿ\s,\.\-\/\’\':;%&–—]+\)', '', s)

    # 4. Specific translations
    translations = [
        ('शरीर की अग्नि', 'Digestive fire and metabolism'),
        ('पार्किंसंस रोग', "Parkinson's disease"),
        ('शरीर का जल संतुलन', 'Fluid and electrolyte balance'),
        ('शरीर की संरचना ऊतक का अध', 'Cellular skeletal and tissue structure'),
        ('एड्स', 'Immune deficiency syndromes (AIDS)'),
        ('चिंता', 'Anxiety and worry'),
        ('कठोर अनुभव', 'Austere trials and hardships'),
        ('व्यापार, वाणिज्य, बुध ग्रह संवाद, बातचीत, और संचार का कारक', 'Commerce, accounting, speech, communication, and intellectual exchange'),
        ('मूल त्रिकोण', 'Moolatrikona'),
        ('बुध का मूल त्रिकोण कन्या Zodiac Sign में 16 से 20 डिग्री तक होता है।', "Mercury's Moolatrikona is in Virgo from 16° to 20°."),
        ('Zodiac Sign अधिपत्य', 'Sign Rulership'),
        ('मूल त्रिकोण Zodiac Sign', 'Moolatrikona Sign'),
        ('अपः', 'Apas'),
        ('मस्तिष्क ज्वर', 'Encephalitis'),
        ('मिर्गी', 'Epilepsy'),
        ('घेंघा', 'Goitre'),
        ('फेफड़े', 'Lungs'),
        ('आंतें', 'Intestines'),
        ('क्रोहन रोग', "Crohn's Disease"),
        ('त्वचा', 'Skin'),
        ('जननांग', 'Genital organs'),
        ('चेहरे का पक्षाघात', "Bell's Palsy / Facial paralysis"),
        ('मुँह', 'Mouth'),
        ('तंत्रिका तंत्र', 'Nervous system'),
        ('कंधे और बाहों में दर्द', 'Shoulder and arm pain'),
        ('चोट', 'Injuries'),
        ('बहनों का', 'Siblings'),
        ('पेट', 'Stomach'),
        ('माँ का स्वास्थ्य', "Mother's health"),
        ('संतान का स्वास्थ्य', "Children's health"),
        ('बच्चों', 'Progeny'),
        ('मामा का स्वास्थ्य', "Maternal uncle's health"),
        ('साथी के स्वास्थ्य संबंधी समस्याएं', "Spouse's health complications"),
        ('जीवनसाथी का स्वास्थ्य', "Spouse's health"),
        ('कोशिका पुनर्जनन', 'Cellular regeneration'),
        ('पिता का स्वास्थ्य', "Father's health"),
        ('कूल्हे', 'Hips'),
        ('घुटने', 'Knees'),
        ('हड्डियाँ', 'Bones'),
        ('शरीर की आकांक्षाओं और स्वास्थ्य के बीच संबंध', 'Connection between bodily desires and health'),
        ('निचला पैर', 'Lower legs'),
        ('शरीर के विषहरण मार्ग', 'Detoxification and lymphatic pathways'),
        ('से संबंधित अंग', 'governed organs'),
        ('परिवर्तन गति', 'Rate of Change'),
        ('भाव हर ~2 घंटे में, राशि हर ~30 दिन', 'House changes every ~2 hrs, Sign every ~30 days'),
        ('हर 2 घंटे में एक नया लग्न', 'A new Ascendant rises every ~2 hrs'),
        ('मूल स्रोत', 'Underlying Source'),
        ('सूर्य की स्थिर गति', 'Apparent solar transit'),
        ('पृथ्वी का घूर्णन और पूर्व दिशा पर उदय', "Earth's axial rotation & Eastern rising"),
        ('राशि', 'Zodiac Sign'),
        ('एक ही दिन में नहीं बदलता', 'Remains in same sign throughout the day'),
        ('एक दिन में सभी 12 राशियाँ पार करता है', 'Traverses all 12 signs in 24 hours'),
        ('भाव स्थिति', 'House Placement'),
        ('बृहत्पाराशर होरा शास्त्र', 'Brihat Parashara Hora Shastra'),
        ('सारावली', 'Saravali'),
        ('फलदीपिका', 'Phaladeepika'),
        ('जातक पारिजात', 'Jataka Parijata'),
        ('नंदी नाड़ी', 'Nandi Nadi'),
        ('लाल किताब', 'Lal Kitab'),
        ('कल्याण वर्मा', 'Kalyan Verma'),
        ('मन्त्रेश्वर', 'Mantreshwara')
    ]
    for hi_t, en_t in translations:
        s = s.replace(hi_t, en_t)

    # 5. Remove any residual Devanagari characters
    s = re.sub(r'[ऀ-ॿ]+', '', s)

    # Clean up punctuation and spacing
    s = re.sub(r'\(\s*\)', '', s)
    s = re.sub(r',\s*,', ',', s)
    s = re.sub(r'^\s*,\s*', '', s)
    s = re.sub(r'\s*,\s*$', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


# ------------------------------------------------------------------------------
# 4. DEDICATED TABLE REPLACEMENTS FOR COMPLETE ACCURACY
# ------------------------------------------------------------------------------

# English replacements for tables with pure Devanagari in original source
PAGE_6_EN_TABLE = """
<table class="astro-table">
<thead><tr>
<th>Category</th>
<th>Sun's Significations (Karakatva)</th>
<th>Classical References</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>Body Parts</strong></td><td>Heart, Right eye (males) / Left eye (females), Bones, Cranial structure, Brain vitality</td><td>Brihat Parashara, Saravali, Phaladeepika, Nandi Nadi</td></tr>
<tr><td class="primary-col"><strong>Disposition</strong></td><td>Self-respect, Soul power (Atma-Bala), Self-awareness, Leadership authority, Regal dignity</td><td>Brihat Parashara, Saravali, Lal Kitab</td></tr>
<tr><td class="primary-col"><strong>Relations</strong></td><td>Father, Paternal lineage, Sovereign ruler, High administrative officials, King</td><td>Phaladeepika, Jataka Parijata, Lal Kitab</td></tr>
<tr><td class="primary-col"><strong>Soul / Consciousness</strong></td><td>Paramatman connection, Spiritual consciousness, Life force vitality (Prana-Shakti)</td><td>Brihat Parashara, Saravali</td></tr>
<tr><td class="primary-col"><strong>Health / Pathology</strong></td><td>Cardiac diseases, Eye afflictions, Osteoporosis, Sunstroke, High pitta fevers</td><td>Brihat Parashara, Phaladeepika</td></tr>
<tr><td class="primary-col"><strong>Career / Domain</strong></td><td>Administrative services, Civil governance, Executive politics, Medicine, Surgery</td><td>Saravali, Jataka Parijata</td></tr>
<tr><td class="primary-col"><strong>Metal / Gemstone</strong></td><td>Copper, Gold, Ruby (Manikya)</td><td>Brihat Parashara, Saravali</td></tr>
<tr><td class="primary-col"><strong>Element / Direction</strong></td><td>Fire element (Agni Tattva), East direction</td><td>Brihat Parashara, Phaladeepika</td></tr>
<tr><td class="primary-col"><strong>Guna / Caste</strong></td><td>Sattva Guna, Kshatriya Varna</td><td>Brihat Parashara, Saravali</td></tr>
<tr><td class="primary-col"><strong>Dignity Degrees</strong></td><td>Exalted in Aries (10°), Debilitated in Libra (10°), Moolatrikona in Leo (0-20°)</td><td>Brihat Parashara, Saravali</td></tr>
</tbody></table>
"""

PAGE_7_EN_TABLE = """
<table class="astro-table">
<thead><tr>
<th>Category</th>
<th>Moon's Significations (Karakatva)</th>
<th>Classical References</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>Body Parts</strong></td><td>Mind (Manas), Chest, Lungs, Plasma/Fluids, Left eye (males) / Right eye (females), Breast tissue</td><td>Brihat Parashara, Saravali, Phaladeepika, Nandi Nadi</td></tr>
<tr><td class="primary-col"><strong>Disposition</strong></td><td>Emotional sensitivity, Compassion, Imagination, Maternal instincts, Gentle temperament, Fluctuating moods</td><td>Brihat Parashara, Saravali, Lal Kitab</td></tr>
<tr><td class="primary-col"><strong>Relations</strong></td><td>Mother, Maternal lineage, Family bonds, Nurturing relationships</td><td>Saravali, Jataka Parijata, Lal Kitab</td></tr>
<tr><td class="primary-col"><strong>Psyche / Soul</strong></td><td>Emotional psyche, Memory (Smriti), Subconscious mind, Spiritual receptivity</td><td>Brihat Parashara, Saravali</td></tr>
<tr><td class="primary-col"><strong>Health / Pathology</strong></td><td>Mental depression, Insomnia, Water retention, Pulmonary disorders, Menstrual irregularities</td><td>Brihat Parashara, Phaladeepika</td></tr>
<tr><td class="primary-col"><strong>Career / Domain</strong></td><td>Dairy, Maritime trade, Nursing, Psychology, Hospitality, Agriculture, Travel</td><td>Saravali, Jataka Parijata</td></tr>
<tr><td class="primary-col"><strong>Metal / Gemstone</strong></td><td>Silver, Bell metal, Pearl (Moti), Moonstone</td><td>Brihat Parashara, Saravali</td></tr>
<tr><td class="primary-col"><strong>Element / Direction</strong></td><td>Water element (Jala Tattva), Northwest direction</td><td>Brihat Parashara, Phaladeepika</td></tr>
<tr><td class="primary-col"><strong>Guna / Caste</strong></td><td>Sattva Guna, Vaishya Varna</td><td>Brihat Parashara, Saravali</td></tr>
<tr><td class="primary-col"><strong>Dignity Degrees</strong></td><td>Exalted in Taurus (3°), Debilitated in Scorpio (3°), Moolatrikona in Taurus (4-30°)</td><td>Brihat Parashara, Saravali</td></tr>
</tbody></table>
"""

PAGE_10_EN_TABLE = """
<table class="astro-table">
<thead><tr>
<th>Category</th>
<th>Mars's Significations (Karakatva)</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>Body Parts</strong></td><td>Blood circulation, Bone marrow, Muscular tissues, Hemoglobin, Gallbladder</td></tr>
<tr><td class="primary-col"><strong>Disposition</strong></td><td>Energetic, Competitive drive, Valor, Unyielding courage, Impulse control, Fiery temper</td></tr>
<tr><td class="primary-col"><strong>Relations</strong></td><td>Younger siblings (especially brothers), Armed forces, Soldiers, Commander-in-chief</td></tr>
<tr><td class="primary-col"><strong>Psyche / Energy</strong></td><td>Dynamic drive, Physical endurance, Passion, Initiative, Strategic aggression</td></tr>
<tr><td class="primary-col"><strong>Health / Pathology</strong></td><td>Hemorrhages, Acute fevers, Surgical cuts, Burns, Blood pressure, Inflammations</td></tr>
<tr><td class="primary-col"><strong>Career / Domain</strong></td><td>Defense, Police services, Engineering, Surgery, Real estate, Martial arts</td></tr>
<tr><td class="primary-col"><strong>Metal / Gemstone</strong></td><td>Copper, Red Coral (Moonga)</td></tr>
<tr><td class="primary-col"><strong>Element / Direction</strong></td><td>Fire element (Agni Tattva), South direction</td></tr>
<tr><td class="primary-col"><strong>Guna / Caste</strong></td><td>Tamas Guna, Kshatriya Varna</td></tr>
<tr><td class="primary-col"><strong>Dignity Degrees</strong></td><td>Exalted in Capricorn (28°), Debilitated in Cancer (28°), Moolatrikona in Aries (0-12°)</td></tr>
</tbody></table>
"""

PAGE_13_EN_TABLE = """
<table class="astro-table">
<thead><tr>
<th>Category</th>
<th>Venus's Significations (Karakatva)</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>Body Parts</strong></td><td>Facial luster, Reproductive organs, Kidneys, Semen/Ovum, Endocrine glands, Skin complexion</td></tr>
<tr><td class="primary-col"><strong>Disposition</strong></td><td>Gentle, Affectionate, Artistic, Refined charm, Creative imagination, Pursuit of luxury</td></tr>
<tr><td class="primary-col"><strong>Gender / Nature</strong></td><td>Feminine, Rajas nature, Water element (Jala Tattva)</td></tr>
<tr><td class="primary-col"><strong>Relations</strong></td><td>Spouse (Wife in male charts), Romantic partners, Artists, Feminine friends</td></tr>
<tr><td class="primary-col"><strong>Domain / Significator</strong></td><td>Fine arts, Cinema, Poetry, Music, Vehicles, Perfumes, Gems, Conjugal bliss</td></tr>
<tr><td class="primary-col"><strong>Health / Pathology</strong></td><td>Urinary tract infections, Diabetes, Reproductive infertility, Hormonal imbalances</td></tr>
<tr><td class="primary-col"><strong>Career / Domain</strong></td><td>Fashion design, Entertainment industry, Luxury commerce, Cosmetology, Diplomacy</td></tr>
<tr><td class="primary-col"><strong>Metal / Gemstone</strong></td><td>Silver, Platinum, Diamond (Heera), White Sapphire</td></tr>
<tr><td class="primary-col"><strong>Direction</strong></td><td>Southeast direction (Agneya)</td></tr>
<tr><td class="primary-col"><strong>Dignity Degrees</strong></td><td>Exalted in Pisces (27°), Debilitated in Virgo (27°), Moolatrikona in Libra (0-15°)</td></tr>
</tbody></table>
"""

PAGE_15_EN_TABLE = """
<table class="astro-table">
<thead><tr>
<th>Classical Source</th>
<th>Saturn's Philosophical & Predictive Description</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>Brihat Parashara Hora Shastra</strong></td><td>Saturn is tamasic, righteous, dark-complexioned, and the supreme dispenser of karmic fruits.</td></tr>
<tr><td class="primary-col"><strong>Phaladeepika</strong></td><td>Saturn represents slow perseverance, discipline, austerity, and hard endurance.</td></tr>
<tr><td class="primary-col"><strong>Saravali</strong></td><td>Saturn is the slowest moving planet yet the most just; distributes the exact harvest of deeds.</td></tr>
<tr><td class="primary-col"><strong>Jataka Parijata</strong></td><td>Signifies longevity, separation, detachment, humility, and organizational mastery.</td></tr>
<tr><td class="primary-col"><strong>Lal Kitab</strong></td><td>The divine judge (Nyayadhish); punishes deception and rewards honest, ethical labor.</td></tr>
<tr><td class="primary-col"><strong>Modern Analytical View</strong></td><td>Represents structural reality, boundaries, accountability, patience, and mature resilience.</td></tr>
</tbody></table>
"""

PAGE_18_EN_TABLE = """
<table class="astro-table">
<thead><tr>
<th>Category</th>
<th>Ketu's Significations (Karakatva)</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>Body Parts</strong></td><td>Spine (lower sacrum), Muladhara chakra, Nervous tails, Small intestines</td></tr>
<tr><td class="primary-col"><strong>Disposition / Nature</strong></td><td>Mystical, Introspective, Spiritual, Ascetic, Detached, Fond of silence</td></tr>
<tr><td class="primary-col"><strong>Relationships</strong></td><td>Friendly with Mercury, Venus, Saturn; Neutral with Jupiter; Inimical with Sun, Moon, Mars</td></tr>
<tr><td class="primary-col"><strong>Spiritual Domain</strong></td><td>Moksha Karaka (Liberation), Meditation, Occult mastery, Kundalini awakening</td></tr>
<tr><td class="primary-col"><strong>Health / Pathology</strong></td><td>Unidentified fevers, Epidemics, Skin eruptions, Viral infections, Psychological hallucinations</td></tr>
<tr><td class="primary-col"><strong>Career / Domain</strong></td><td>Spiritual preceptor, Astrologer, Occult researcher, Software coder, Cryptography</td></tr>
<tr><td class="primary-col"><strong>Gemstone / Direction</strong></td><td>Cat's Eye (Vaidurya), South-West (or terminal pivot)</td></tr>
</tbody></table>
"""

PAGE_43_EN_TABLE = """
<table class="astro-table">
<thead><tr>
<th>House (Bhava)</th>
<th>House Name (Sanskrit)</th>
<th>Fixed Significator (Karaka Planet)</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>1st House</strong></td><td>Tanu Bhava (Body & Self)</td><td>Sun (Surya)</td></tr>
<tr><td class="primary-col"><strong>2nd House</strong></td><td>Dhana Bhava (Wealth & Speech)</td><td>Jupiter (Brihaspati)</td></tr>
<tr><td class="primary-col"><strong>3rd House</strong></td><td>Sahaja Bhava (Siblings & Courage)</td><td>Mars (Mangala)</td></tr>
<tr><td class="primary-col"><strong>4th House</strong></td><td>Sukha Bhava (Mother & Vehicles)</td><td>Moon (Chandra)</td></tr>
<tr><td class="primary-col"><strong>5th House</strong></td><td>Putra Bhava (Children & Intellect)</td><td>Jupiter (Brihaspati)</td></tr>
<tr><td class="primary-col"><strong>6th House</strong></td><td>Shatru / Roga Bhava (Debts & Disease)</td><td>Mars & Saturn</td></tr>
<tr><td class="primary-col"><strong>7th House</strong></td><td>Kalatra Bhava (Spouse & Partnerships)</td><td>Venus (Shukra)</td></tr>
<tr><td class="primary-col"><strong>8th House</strong></td><td>Ayur / Randhra Bhava (Longevity & Transformation)</td><td>Saturn (Shani)</td></tr>
<tr><td class="primary-col"><strong>9th House</strong></td><td>Bhagya / Dharma Bhava (Fortune & Wisdom)</td><td>Jupiter (Brihaspati)</td></tr>
<tr><td class="primary-col"><strong>10th House</strong></td><td>Karma Bhava (Profession & Authority)</td><td>Sun, Mercury, Jupiter, Saturn</td></tr>
<tr><td class="primary-col"><strong>11th House</strong></td><td>Labha Bhava (Gains & Ambition)</td><td>Jupiter (Brihaspati)</td></tr>
<tr><td class="primary-col"><strong>12th House</strong></td><td>Vyaya / Moksha Bhava (Expenses & Liberation)</td><td>Saturn & Ketu</td></tr>
</tbody></table>
"""

# Hindi replacements for tables that were in English
PAGE_20_HI_TABLE = """
<table class="astro-table">
<thead><tr>
<th>राजयोग का नाम</th>
<th>ग्रह संयोजन</th>
<th>शास्त्रीय विवरण एवं फल</th>
<th>विद्वानों का शास्त्रीय मत</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>गजकेसरी योग</strong></td><td>चन्द्रमा से केंद्र (१, ४, ७, १०) में गुरु की स्थिति</td><td>प्रचुर समृद्धि, बुद्धिमत्ता, उच्च यश और अखंड सफलता प्रदान करता है।</td><td>सर्वमान्य; प्रभाव कुंडली के संपूर्ण बलबल पर निर्भर करता है।</td></tr>
<tr><td class="primary-col"><strong>धर्म कर्माधिपति योग</strong></td><td>नवमेश (धर्म) व दशमेश (कर्म) की युति अथवा दृष्टि</td><td>कर्तव्य और कर्म के समन्वय से उच्च पद, प्रशासनिक सम्मान और प्रतिष्ठा।</td><td>अत्यंत शक्तिशाली व प्रतिष्ठित राजयोग।</td></tr>
<tr><td class="primary-col"><strong>बुधादित्य योग</strong></td><td>एक ही भाव में सूर्य और बुध की युति</td><td>कुशाग्र बुद्धि, वाकपटुता, तार्किक क्षमता और ज्ञान का विस्तार।</td><td>सर्वमान्य; बौद्धिक व सामाजिक प्रतिष्ठा में विशेष फलदायी।</td></tr>
<tr><td class="primary-col"><strong>विपरीत राजयोग</strong></td><td>६ठे, ८वें, १२वें (त्रिक) भावों के स्वामियों का परस्पर त्रिक में संबंध</td><td>कठिन संघर्षों, संकटों व शत्रुओं के दमन के पश्चात अप्रत्याशित सफलता।</td><td>पाराशरी व फलदीपिका द्वारा विशेष रूप से समर्थित।</td></tr>
<tr><td class="primary-col"><strong>नीचभंग राजयोग</strong></td><td>नीच ग्रह की नीचता का शास्त्रीय नियमों से भंग होना</td><td>प्रारंभिक संघर्षों के बाद जातक को राजा के समान ऐश्वर्य व अधिकार।</td><td>शास्त्रीय फलित में अत्यंत प्रभावी व चमत्कारी नियम।</td></tr>
<tr><td class="primary-col"><strong>चंद्र-मंगल योग</strong></td><td>चन्द्रमा और मंगल की युति अथवा परस्पर दृष्टि</td><td>प्रचुर धन लाभ, व्यापारिक सफलता, पराक्रम से संपत्ति अर्जन।</td><td>आर्थिक दृष्टिकोण से 'महालक्ष्मी योग' तुल्य।</td></tr>
<tr><td class="primary-col"><strong>अमला योग</strong></td><td>लग्न अथवा चन्द्र से दशम भाव में केवल शुभ ग्रह</td><td>निष्कपट आचरण, समाज में बेदाग प्रतिष्ठा, स्थायी यश और कीर्ति।</td><td>बृहत्पाराशर में उच्च कोटि का योग माना गया है।</td></tr>
<tr><td class="primary-col"><strong>पर्वत योग</strong></td><td>केंद्र में शुभ ग्रह हों और ६ठे व ८वें भाव रिक्त हों</td><td>स्थिर संपत्ति, अचल ऐश्वर्य, विद्या व समाज में उच्च सम्मान।</td><td>शास्त्रीय ग्रंथों में सर्वमान्य शुभ फलदाता।</td></tr>
<tr><td class="primary-col"><strong>काहल योग</strong></td><td>चतुर्थेश और गुरु परस्पर केंद्र में हों तथा लग्नेश बली हो</td><td>साहस, सेना अथवा प्रशासन में उच्च नेतृत्व, अदम्य पराक्रम।</td><td>फलदीपिका में विशेष रूप से प्रशंसित।</td></tr>
<tr><td class="primary-col"><strong>शंख योग</strong></td><td>पंचमेश और षष्ठेश परस्पर केंद्र में हों और लग्नेश शक्तिशाली हो</td><td>शास्त्रज्ञ, दयालु, पुण्यात्मा, उच्च विद्या व सुखी जीवन।</td><td>जातक पारिजात में वर्णित प्रामाणिक योग।</td></tr>
</tbody></table>
"""

PAGE_81_HI_TABLE = """
<table class="astro-table">
<thead><tr>
<th>ग्रह / विषय</th>
<th>पद १ – धनु नवमांश (गुरु)</th>
<th>पद २ – मकर नवमांश (शनि)</th>
<th>पद ३ – कुंभ नवमांश (शनि)</th>
<th>पद ४ – मीन नवमांश (गुरु)</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>नवमांश विषय</strong></td><td>धर्मनिष्ठ संयम; आश्लेषा की शक्ति का ज्ञानपरक मार्गदर्शन</td><td>नियंत्रित संरचना; शक्ति का रणनीतिक एकत्रीकरण</td><td>बौद्धिक गूढ़ता; सामाजिक व गुप्त अनुसंधान</td><td>आध्यात्मिक समर्पण; बंधनों से मुक्ति व मोक्ष</td></tr>
<tr><td class="primary-col"><strong>सूर्य</strong></td><td>नैतिक प्रभाव, मार्गदर्शक नेतृत्व</td><td>संस्थागत अधिकार, अनुशासित नियंत्रण</td><td>गोपनीय सत्ता, गहन रणनीतिकार</td><td>अहंकार विसर्जन, आध्यात्मिक सेवा</td></tr>
<tr><td class="primary-col"><strong>चन्द्रमा</strong></td><td>दार्शनिक अंतर्दृष्टि, भावनात्मक विस्तार</td><td>व्यावहारिक भावनात्मक नियंत्रण</td><td>बौद्धिक गहराई, अंतर्मुखी चिंतन</td><td>असीम करुणा, मोक्ष मार्ग की ओर झुकाव</td></tr>
<tr><td class="primary-col"><strong>मंगल</strong></td><td>सत्य हेतु संघर्ष, धार्मिक पराक्रम</td><td>रणनीतिक सैन्य बल व अनुशासन</td><td>वैज्ञानिक अनुसंधान, गूढ़ अन्वेषण</td><td>शल्य क्रिया, आध्यात्मिक रूपांतरण</td></tr>
<tr><td class="primary-col"><strong>बुध</strong></td><td>दार्शनिक वाणी, उच्च शिक्षा</td><td>रणनीतिक व्यापार, कुशाग्र बुद्धि</td><td>तकनीकी कौशल, गूढ़ ज्ञान</td><td>अंतःप्रेरणा, काव्यात्मक अभिव्यक्ति</td></tr>
<tr><td class="primary-col"><strong>गुरु</strong></td><td>उत्तम धर्मगुरु, सात्विक ज्ञान</td><td>कानून व न्याय व्यवस्था</td><td>गूढ़ दर्शन, मानवतावादी दृष्टिकोण</td><td>परम आध्यात्मिक गुरु, मोक्ष मार्गदर्शक</td></tr>
<tr><td class="primary-col"><strong>शुक्र</strong></td><td>धार्मिक कला, उच्च आदर्श</td><td>भौतिक संपत्ति, सौंदर्य प्रसाधन</td><td>नवीन कलात्मक दृष्टि</td><td>दिव्य प्रेम, समर्पण भाव</td></tr>
<tr><td class="primary-col"><strong>शनि</strong></td><td>धर्मनिष्ठ तपस्या व त्याग</td><td>कठोर प्रशासनिक अनुशासन</td><td>जनसेवा, गुप्त संगठनात्मक कार्य</td><td>परम वैराग्य, संन्यास चेतना</td></tr>
<tr><td class="primary-col"><strong>राहु</strong></td><td>दार्शनिक महत्वाकांक्षा</td><td>भौतिक सत्ता का विस्तार</td><td>वैज्ञानिक शोध व अन्वेषण</td><td>पराभौतिक रहस्य व जागृति</td></tr>
<tr><td class="primary-col"><strong>केतु</strong></td><td>आत्म-ज्ञान व विवेक</td><td>कर्म मुक्ति व संन्यास</td><td>कुंडलिनी जागरण व साधना</td><td>परम मोक्ष व कैवल्य</td></tr>
</tbody></table>
"""

PAGE_82_HI_TABLE = """
<table class="astro-table">
<thead><tr>
<th>ग्रह</th>
<th>पद १ – सिंह नवमांश (सूर्य)</th>
<th>पद २ – कन्या नवमांश (बुध)</th>
<th>पद ३ – तुला नवमांश (शुक्र)</th>
<th>पद ४ – वृश्चिक नवमांश (मंगल)</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>नवमांश प्रभाव</strong></td><td>पोषण पर सत्ता व अधिकार; राजसी संरक्षण</td><td>पोषण का विश्लेषणात्मक परिशोधन; सेवा</td><td>सौहार्दपूर्ण पोषण; कला, सौंदर्य व संतुलन</td><td>गहन रक्षात्मक पोषण; संकट में रक्षण</td></tr>
<tr><td class="primary-col"><strong>सूर्य</strong></td><td>राजसी दायित्व, कर्तव्यनिष्ठ नेतृत्व</td><td>सेवाभावी कार्यकुशलता व सूक्ष्मता</td><td>कूटनीतिक समन्वय व संतुलन</td><td>संकट रक्षक, अदम्य पराक्रम</td></tr>
<tr><td class="primary-col"><strong>चन्द्रमा</strong></td><td>उदार पोषण व राजसी स्नेह</td><td>सेवा, चिकित्सा व जनहित</td><td>पारिवारिक सुख व सामाजिक सौहार्द</td><td>आध्यात्मिक गहराई व दृढ़ मनोबल</td></tr>
<tr><td class="primary-col"><strong>मंगल</strong></td><td>धर्म रक्षक व साहसी सेनापति</td><td>अनुशासित सेना व व्यावहारिक दक्षता</td><td>न्यायप्रिय रक्षक व शांति स्थापना</td><td>उच्च पराक्रम व आत्मरक्षा</td></tr>
<tr><td class="primary-col"><strong>बुध</strong></td><td>नीतिवान सलाहकार व वक्ता</td><td>उत्तम चिकित्सक अथवा लेखाकार</td><td>ललित कला व व्यापारिक संतुलन</td><td>गूढ़ अन्वेषक व अनुसंधानकर्ता</td></tr>
<tr><td class="primary-col"><strong>गुरु</strong></td><td>उच्च धर्मगुरु व समाज सुधारक</td><td>विद्यादानी व नीति विशेषज्ञ</td><td>सद्गुणी चिंतक व शांतिदूत</td><td>आध्यात्मिक सिद्ध व तपोनिष्ठ</td></tr>
<tr><td class="primary-col"><strong>शुक्र</strong></td><td>राजसी वैभव व सांस्कृतिक कला</td><td>सात्विक सेवा व विनम्रता</td><td>सुख-समृद्धि व दांपत्य प्रीति</td><td>त्यागपूर्ण प्रेम व निष्ठा</td></tr>
<tr><td class="primary-col"><strong>शनि</strong></td><td>न्यायप्रिय प्रशासक व दंडनायक</td><td>परिश्रमी सेवक व कर्मयोगी</td><td>सामाजिक संगठन व जनसमर्थन</td><td>दीर्घायु, वैराग्य व आत्मसंयम</td></tr>
</tbody></table>
"""

PAGE_83_HI_TABLE = """
<table class="astro-table">
<thead><tr>
<th>अश्विनी पद</th>
<th>मुख्य राशि (डी-१)</th>
<th>नवमांश राशि (डी-९)</th>
<th>नवमांश स्वामी</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>पद १</strong></td><td>मेष</td><td>मेष</td><td>मंगल (साहस, ऊर्जा, अग्नि)</td></tr>
<tr><td class="primary-col"><strong>पद २</strong></td><td>मेष</td><td>वृषभ</td><td>शुक्र (धन, सौंदर्य, स्थिरता)</td></tr>
<tr><td class="primary-col"><strong>पद ३</strong></td><td>मेष</td><td>मिथुन</td><td>बुध (बुद्धि, संचार, तर्क)</td></tr>
<tr><td class="primary-col"><strong>पद ४</strong></td><td>मेष</td><td>कर्क</td><td>चन्द्रमा (मन, करुणा, जल)</td></tr>
</tbody></table>
"""

PAGE_84_HI_TABLE = """
<table class="astro-table">
<thead><tr>
<th>पद</th>
<th>नवमांश राशि</th>
<th>नवमांश स्वामी</th>
<th>नामाक्षर ध्वनि</th>
<th>अश्विनी में मूल विशेषता</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>पद १</strong></td><td>मेष</td><td>मंगल</td><td>चू</td><td>शुद्ध पराक्रम, पहल, साहसी नेतृत्व व तीव्र गति</td></tr>
<tr><td class="primary-col"><strong>पद २</strong></td><td>वृषभ</td><td>शुक्र</td><td>चे</td><td>व्यावहारिक कुशलता, संसाधन संचय, सौंदर्य व स्थिरता</td></tr>
<tr><td class="primary-col"><strong>पद ३</strong></td><td>मिथुन</td><td>बुध</td><td>चो</td><td>वाकपटुता, संचार कौशल, बौद्धिक जिज्ञासा व बहुमुखी प्रतिभा</td></tr>
<tr><td class="primary-col"><strong>पद ४</strong></td><td>कर्क</td><td>चन्द्रमा</td><td>ला</td><td>करुणामयी चिकित्सा, संवेदनशील मन, परोपकार व जनसेवा</td></tr>
</tbody></table>
"""

PAGE_85_HI_TABLE = """
<table class="astro-table">
<thead><tr>
<th>अश्विनी में ग्रह</th>
<th>शास्त्रीय फलित एवं विशेषताएं</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>सूर्य</strong></td><td>तीव्र नेतृत्व क्षमता, प्रभावशाली राजसी व्यक्तित्व, प्रशासनिक व सैन्य अधिकार। जातक साहसी किंतु स्वाभिमानी होता है। पद भेद से प्रशासक से लेकर लोक कल्याणकारी हीलर तक बनता है।</td></tr>
<tr><td class="primary-col"><strong>चन्द्रमा</strong></td><td>मन अत्यंत चंचल, स्फूर्तिवान, उत्साही तथा शीघ्र निर्णय लेने वाला। खेलकूद व दौड़-भाग में निपुण। उच्चतम अवस्था में संवेदनशील व चमत्कारी चिकित्सक बनता है।</td></tr>
<tr><td class="primary-col"><strong>मंगल</strong></td><td>स्वराशि प्रभाव; अदम्य साहस, शारीरिक शक्ति, तकनीकी व शल्य क्रिया (सर्जरी) में प्रवीण, त्वरित कार्रवाई करने वाला योद्धा स्वभाव।</td></tr>
<tr><td class="primary-col"><strong>बुध</strong></td><td>तीव्र कुशाग्र बुद्धि, त्वरित प्रत्युत्पन्नमतित्व, व्यापार व नवाचार में प्रवीण, तार्किक वाणी, अल्प समय में समस्या समाधानकर्ता।</td></tr>
<tr><td class="primary-col"><strong>गुरु</strong></td><td>ज्ञान का त्वरित प्रसारक, प्रेरणादायी शिक्षक, आध्यात्मिक नवजागरण का अग्रदूत, न्यायप्रिय व सात्विक मार्गदर्शक।</td></tr>
<tr><td class="primary-col"><strong>शुक्र</strong></td><td>आकर्षक व्यक्तित्व, कलात्मक अभिरुचि, सौंदर्य व वाहनों का प्रेमी, संबंधों में उत्साह व ताजगी।</td></tr>
<tr><td class="primary-col"><strong>शनि</strong></td><td>मेष में नीच प्रभाव; कर्म में धैर्य का अभाव अथवा प्रारंभिक संघर्ष, किंतु कठोर परिश्रम से विलंबित व स्थायी सफलता।</td></tr>
<tr><td class="primary-col"><strong>राहु</strong></td><td>अपरंपरागत सोच, नवाचार, विदेशी संबंध, आधुनिक तकनीकी शोध में अप्रत्याशित सफलता।</td></tr>
<tr><td class="primary-col"><strong>केतु</strong></td><td>गहन अंतःप्रेरणा, आध्यात्मिक जागृति, चिकित्सा व रहस्य विद्याओं में स्वाभाविक निपुणता, मोक्ष मार्ग।</td></tr>
</tbody></table>
"""

PAGE_86_HI_TABLE = """
<table class="astro-table">
<thead><tr>
<th>ग्रह</th>
<th>पद १: मेष नवमांश (चू)</th>
<th>पद २: वृष नवमांश (चे)</th>
<th>पद ३: मिथुन नवमांश (चो)</th>
<th>पद ४: कर्क नवमांश (ला)</th>
</tr></thead><tbody>
<tr><td class="primary-col"><strong>नवमांश स्वामी</strong></td><td>मंगल (पराक्रम, ऊर्जा, अग्नि)</td><td>शुक्र (धन, सौंदर्य, पृथ्वी)</td><td>बुध (बुद्धि, संचार, वायु)</td><td>चन्द्रमा (मन, करुणा, जल)</td></tr>
<tr><td class="primary-col"><strong>सूर्य</strong></td><td>वर्गोत्तम (उच्च): शीर्ष प्रशासनिक नेतृत्व</td><td>व्यावहारिक प्रबंधक, संसाधन संचय</td><td>बौद्धिक रणनीतिकार, वाकपटु</td><td>करुणामयी संरक्षक, जनकल्याण</td></tr>
<tr><td class="primary-col"><strong>चन्द्रमा</strong></td><td>आवेगी योद्धा, त्वरित निर्णय</td><td>स्थिर धनवान, कला प्रेमी</td><td>बहुमुखी विचारक, लेखक</td><td>वर्गोत्तम: चमत्कारी हीलर (चिकित्सक)</td></tr>
<tr><td class="primary-col"><strong>मंगल</strong></td><td>स्वक्षेत्री वर्गोत्तम: अपराजेय सेनापति</td><td>भूमि-भवन निर्माता, व्यावहारिक</td><td>तकनीकी विशेषज्ञ, गणितज्ञ</td><td>नीच नवमांश: भावनात्मक संघर्ष</td></tr>
<tr><td class="primary-col"><strong>बुध</strong></td><td>आक्रामक वक्ता, शीघ्र निर्णय</td><td>कुशल व्यापारी, वित्तीय समझ</td><td>स्वक्षेत्री: उत्कृष्ट लेखक/शोधकर्ता</td><td>कल्पनाशक्ति, काव्यात्मक चेतना</td></tr>
<tr><td class="primary-col"><strong>गुरु</strong></td><td>साहसी उपदेशक, धर्म सुधारक</td><td>वित्तीय सलाहकार, न्यायप्रिय</td><td>ज्ञान का प्रसारक, शिक्षक</td><td>उच्च नवमांश: सिद्ध आध्यात्मिक गुरु</td></tr>
<tr><td class="primary-col"><strong>शुक्र</strong></td><td>उत्साही प्रेमी, त्वरित आकर्षण</td><td>स्वक्षेत्री: विलासी, ऐश्वर्यवान</td><td>कलात्मक संपर्क, व्यापार</td><td>समर्पित साथी, उच्च संवेदनशीलता</td></tr>
<tr><td class="primary-col"><strong>शनि</strong></td><td>नीच वर्गोत्तम: घोर प्रारंभिक संघर्ष</td><td>व्यावहारिक श्रम, धीमा विकास</td><td>तकनीकी अन्वेषक, कुशल कारीगर</td><td>सेवाभावी, वैराग्य व आत्मसंयम</td></tr>
</tbody></table>
"""

def localize_html_table(table_html, page_idx, target_lang='hindi'):
    """Full table localization using pure pre-compiled tables from tables_data."""
    p_num = page_idx + 1
    suffix = 'HI' if target_lang == 'hindi' else 'EN'
    var_name = f'PAGE_{p_num}_{suffix}_TABLE'
    if var_name in globals() and globals()[var_name]:
        return globals()[var_name].strip()
    # Check duplicate Nakshatra block (Pages 76-80 duplicate Ch 3 Pages 23-27)
    if 76 <= p_num <= 80:
        mapped_p = p_num - 53
        mapped_var = f'PAGE_{mapped_p}_{suffix}_TABLE'
        if mapped_var in globals() and globals()[mapped_var]:
            return globals()[mapped_var].strip()
    return table_html


# ------------------------------------------------------------------------------
# 5. SUN IN HOUSES & SIGNS MONOLINGUAL GENERATORS
# ------------------------------------------------------------------------------

def generate_sun_houses_content(page_num, lang='hindi'):
    is_hindi = (lang == 'hindi')
    if page_num == 46:
        header_title = "सूर्य देव: भाव १ से ६ फलित विचार" if is_hindi else "Sun in Houses 1 to 6 (Classical Interpretations)"
        houses_data = [
            ("१. प्रथम भाव (लग्न भाव):", "1. 1st House (Ascendant / Lagna):",
             "जातक स्वाभिमानी, चतुर, प्रभावी, राजसी व्यक्तित्व तथा आकर्षक होता है। नेतृत्व क्षमता प्रबल होती है। नेत्र अथवा नासिका संबंधी संवेदनशीलता, पित्त प्रकृति एवं अहंकार की प्रवृत्ति हो सकती है।",
             "The native is self-respecting, intelligent, authoritative, and charismatic. Possesses natural leadership qualities. May experience eye or nasal sensitivities, high pitta (internal heat), and egoistic pride."),
            ("२. द्वितीय भाव (धन भाव):", "2. 2nd House (Dhana Bhava):",
             "वाणी में ओज व कभी-कभी कठोरता, धन उपार्जन में निरंतर परिश्रम, कुटुंब में वैचारिक मतभेद तथा नेत्र विकारों की संभावना रहती है। जातक स्वावलंबी होता है।",
             "The native speaks with commanding authority but may possess a sharp tongue. Financial accumulation requires persistent effort. Family friction and potential eye ailments."),
            ("३. तृतीय भाव (सहज / पराक्रम भाव):", "3. 3rd House (Sahaja / Valor Bhava):",
             "अत्यंत साहसी, शूरवीर, समाज में प्रभावशाली तथा बाहुबल से ख्याति अर्जित करने वाला होता है। छोटे भाइयों से मतभेद संभव हैं, किंतु समाज में यश प्राप्त होता है।",
             "Immense valor, courage, fame, and societal influence. Earns distinction and wealth through individual bravery. May have ideological friction with younger siblings."),
            ("४. चतुर्थ भाव (सुख भाव):", "4. 4th House (Sukha Bhava):",
             "मातृ सुख में न्यूनता अथवा माता के स्वास्थ्य की चिंता, मानसिक शांति में बाधा, पैतृक संपत्ति व वाहन सुख में उतार-चढ़ाव। हृदय व रक्तचाप के प्रति सजग रहना आवश्यक है।",
             "Challenges regarding domestic tranquility, maternal health, or strained emotional peace. Fluctuations in vehicle and real estate comforts. Prone to cardiovascular sensitivity."),
            ("५. पंचम भाव (सुत / बुद्धि भाव):", "5. 5th House (Suta / Intellect Bhava):",
             "तीक्ष्ण कुशाग्र बुद्धि, मन्त्र विद्या व गूढ़ शास्त्रों में रुचि, राजनैतिक प्रभाव, संतान प्राप्ति में विलंब अथवा संतान से वैचारिक भेद, पित्त विकार की आशंका।",
             "Sharp intellect, spiritual wisdom, political acumen, and keen interest in sacred mantras. Delay in progeny or friction with children. Vulnerable to gastric fire imbalances."),
            ("६. षष्ठ भाव (शत्रु व रोग भाव):", "6. 6th House (Shatru / Disease Bhava):",
             "शत्रुहंता योग, प्रतिस्पर्धा में अजेय, मुकदमों व विवादों में विजय, उत्तम रोग प्रतिरोधक क्षमता। प्रशासनिक कार्यों में सफलता प्राप्त होती है। मामा पक्ष से मतभेद संभव।",
             "Destroyer of adversaries (Shatru-Hanta Yoga). Highly competitive, victorious in legal or institutional disputes, and possesses strong vitality. Overcomes acute ailments.")
        ]
    else:
        header_title = "सूर्य देव: भाव ७ से १२ फलित विचार" if is_hindi else "Sun in Houses 7 to 12 (Classical Interpretations)"
        houses_data = [
            ("७. सप्तम भाव (जाया भाव):", "7. 7th House (Kalatra / Spouse Bhava):",
             "दांपत्य जीवन में अहं का टकराव, जीवनसाथी का स्वाभिमानी व प्रभावशाली व्यक्तित्व, साझेदारी के व्यापार में सतर्कता की आवश्यकता, व्यवसायिक यात्राएं अधिक।",
             "Marital friction caused by ego clashes and pride. The spouse is self-respecting, authoritative, and dominant. Demands caution in business partnerships; frequent travels."),
            ("८. अष्टम भाव (आयु / रंध्र भाव):", "8. 8th House (Ayur / Chronic Bhava):",
             "गूढ़ रहस्यों, तंत्र-ज्योतिष व वसीयत से लाभ। गुप्त शत्रुओं से सजगता आवश्यक। नेत्र दुर्बलता अथवा आकस्मिक स्वास्थ्य उतार-चढ़ाव। आध्यात्मिक दृष्टिकोण से शुभ।",
             "Deep inclination toward esoteric research, mysticism, and inheritance gains. Eye sensitivities and sudden unforeseen events. Highly favorable for spiritual transformation."),
            ("९. नवम भाव (भाग्य व धर्म भाव):", "9. 9th House (Bhagya / Dharma Bhava):",
             "परम धार्मिक, पुण्यात्मा, तीर्थ यात्रा प्रेमी, पिता का सहयोगी अथवा पिता के समान मान-सम्मान प्राप्त करने वाला। समाज में धर्मात्मा के रूप में पूजित।",
             "Deeply religious, righteous, fortunate, and devoted to pilgrimage. Elevates paternal reputation, though ideological independence exists. Respected as a principled guide."),
            ("१०. दशम भाव (कर्म भाव - दिशाबली):", "10. 10th House (Karma Bhava - Digbala):",
             "सूर्य को दशम में पूर्ण दिशाबल प्राप्त होता है। कुलदीपक योग, शासन-सत्ता में शीर्ष पद, प्रशासनिक अधिकार, सरकारी मान-प्रतिष्ठा तथा अद्वितीय कार्यकुशलता।",
             "Sun attains full directional strength (Digbala). Bestows Kuladeepaka Yoga, supreme executive authority, government honors, high status, and extraordinary professional success."),
            ("११. एकादश भाव (आय व लाभ भाव):", "11. 11th House (Labha Bhava):",
             "अथाह धन लाभ, सत्ता व उच्च पदस्थ मित्रों का सहयोग, महत्वाकांक्षाओं की पूर्ण सिद्धि, दीर्घायु तथा समाज में धनाढ्य व प्रतिष्ठित स्थिति।",
             "Abundant financial prosperity, patronage from high-ranking government dignitaries, fulfillment of major ambitions, high vitality, and respected social prominence."),
            ("१२. द्वादश भाव (व्यय व मोक्ष भाव):", "12. 12th House (Vyaya / Moksha Bhava):",
             "आध्यात्मिक चेतना, विदेश प्रवास अथवा सुदूर स्थानों पर प्रतिष्ठा, स्वास्थ्य व धर्मार्थ कार्यों पर अत्यधिक व्यय, शयन सुख में कमी, नेत्र संवेदनशीलता।",
             "Spiritual awakening, foreign residency or travels to distant realms, high philanthropic and medical expenditures, sleep sensitivities, and left eye vulnerability.")
        ]

    items_html = []
    for hi_t, en_t, hi_desc, en_desc in houses_data:
        t = hi_t if is_hindi else en_t
        d = hi_desc if is_hindi else en_desc
        items_html.append(f"""
        <div class="sun-effect-item" style="margin-bottom:0.75rem;">
          <div style="color:var(--accent-gold); font-weight:700; font-size:0.92rem; border-bottom:1px dashed var(--page-border); padding-bottom:3px;">{t}</div>
          <div style="font-size:0.86rem; line-height:1.6; margin-top:0.3rem;">
            <p style="margin:0.25rem 0;">{d}</p>
          </div>
        </div>
        """)

    sec_label = f"अध्याय ४ • खण्ड {page_num - 45 + 6}" if is_hindi else f"Chapter 4 • Sun in Houses (Part {page_num - 45})"
    return f"""
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:0.75rem;">
        <div class="chapter-number">{sec_label}</div>
        <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{header_title}</h3>
      </div>
      <div class="rule-card">
        <div class="rule-body" style="font-size:0.86rem; line-height:1.6;">
          {''.join(items_html)}
        </div>
      </div>
    </div>
    """

def generate_sun_signs_content(page_num, lang='hindi'):
    is_hindi = (lang == 'hindi')
    if page_num == 48:
        header_title = "सूर्य देव: मेष से कन्या राशि फल" if is_hindi else "Sun in Signs 1 to 6 (Aries to Virgo Interpretations)"
        signs_data = [
            ("१. मेष राशि (परम उच्च फल):", "1. Aries (Exalted Sign - Uchcha):",
             "जातक अत्यंत प्रतापी, कांतिवान, शूरवीर, स्वाभिमानी, कुशाग्र बुद्धि, साहसी तथा समाज में शीर्ष ख्याति प्राप्त करता है। स्वतंत्र निर्णय व प्रशासनिक क्षमता बेजोड़ होती है।",
             "The native becomes noble, majestic, valorous, self-respecting, highly intelligent, courageous, and attains widespread renown. Supreme leadership and independent vision."),
            ("२. वृषभ राशि (शत्रु क्षेत्री):", "2. Taurus (Enemy Sign - Shukra Kshetra):",
             "जातक कलात्मक, संगीत प्रिय, आकर्षक, वाणी में प्रभाव, धन संचय में कुशल, पारिवारिक सुख का प्रेमी तथा स्थिर स्वभाव वाला होता है।",
             "The native possesses an artistic temperament, appreciation for music, handsome appearance, skill in capital accumulation, and devotion to family comforts."),
            ("३. मिथुन राशि (सम क्षेत्री):", "3. Gemini (Neutral Sign - Budha Kshetra):",
             "जातक वाकपटु, बहुमुखी प्रतिभा का धनी, लेखक, पत्रकारिता, वाणिज्य व गणित में प्रवीण, तर्कशील तथा सामाजिक संपर्क बनाने में अत्यंत कुशल होता है।",
             "The native is an eloquent orator, versatile thinker, distinguished writer, skilled in commerce and mathematics, witty, and socially dynamic."),
            ("४. कर्क राशि (मित्र क्षेत्री):", "4. Cancer (Friendly Sign - Chandra Kshetra):",
             "जातक भावुक, संवेदनशील, कल्पनाशील, जल यात्रा प्रिय, मातृभक्त, सेवाभावी तथा जनकल्याण के कार्यों में तत्पर रहने वाला होता है। मनोदशा परिवर्तनशील रहती है।",
             "The native is intuitive, deeply compassionate, fond of aquatic travels, devoted to parents, philanthropic, and emotionally sensitive."),
            ("५. सिंह राशि (स्वक्षेत्री - मूलत्रिकोण):", "5. Leo (Own & Moolatrikona Sign):",
             "जातक राजा के समान तेजस्वी, उदार हृदय, उच्च स्वाभिमानी, शासन-सत्ता में शीर्ष स्थान प्राप्त करने वाला, निष्पक्ष न्यायप्रिय तथा चुंबकीय व्यक्तित्व का स्वामी होता है।",
             "Regal authority, immense charisma, generous spirit, supreme dignity, natural command in administrative governance, and unwavering righteous pride."),
            ("६. कन्या राशि (मित्र क्षेत्री):", "6. Virgo (Friendly Sign - Budha Kshetra):",
             "जातक विश्लेषणात्मक बुद्धि, गणना व लेखा में निपुण, सूक्ष्मदर्शी, सेवाभावी, व्यावहारिक, विनम्र तथा कार्यकुशल होता है।",
             "The native possesses sharp analytical acumen, mathematical skill, meticulous eye for detail, service orientation, and pragmatic wisdom.")
        ]
    else:
        header_title = "सूर्य देव: तुला से मीन राशि फल" if is_hindi else "Sun in Signs 7 to 12 (Libra to Pisces Interpretations)"
        signs_data = [
            ("७. तुला राशि (परम नीच फल):", "7. Libra (Debilitation Sign - Neecha):",
             "आत्मविश्वास में संकोच, दूसरों पर अधिक निर्भरता, मान-सम्मान हेतु निरंतर संघर्ष, त्वचा अथवा नेत्र संवेदनशीलता। परिश्रम के पश्चात सफलता प्राप्त होती है।",
             "Fluctuating self-confidence, excessive dependence on partners, struggles for public recognition, and prone to renal or skin imbalances. Success comes through humility."),
            ("८. वृश्चिक राशि (मित्र क्षेत्री):", "8. Scorpio (Friendly Sign - Mangal Kshetra):",
             "जातक गूढ़ अन्वेषक, रहस्यमयी स्वभाव, अदम्य साहसी, तीव्र स्मरण शक्ति, शल्य चिकित्सा अथवा संकट प्रबंधन में प्रवीण तथा कठिन परिस्थितियों में भी दृढ़ रहने वाला होता है।",
             "Deep esoteric researcher, secretive demeanor, intense tenacity, unyielding courage, interest in surgical or crisis management, and indomitable endurance."),
            ("९. धनु राशि (मित्र क्षेत्री):", "9. Sagittarius (Friendly Sign - Guru Kshetra):",
             "जातक गुरु तुल्य मार्गदर्शक, धर्मनिष्ठ, न्यायप्रिय, उच्च दार्शनिक चिंतक, सत्यवादी, समाज सुधारक तथा उच्च विद्या में प्रतिष्ठा प्राप्त करने वाला होता है।",
             "Preceptor qualities, deeply righteous, judicial mindset, profound philosophical elevation, truthful, and distinguished in higher academia and spiritual wisdom."),
            ("१०. मकर राशि (शत्रु क्षेत्री):", "10. Capricorn (Enemy Sign - Shani Kshetra):",
             "जातक घोर परिश्रमी, व्यावहारिक, अनुशासित, जीवन में संघर्षों के उपरांत स्थिर शिखर पर पहुंचने वाला, मितव्ययी तथा संगठन संचालन में दक्ष होता है।",
             "Indefatigable work ethic, pragmatic, disciplined, systematically ascends to career pinnacles through perseverance, frugal, and an adept organizational manager."),
            ("११. कुंभ राशि (शत्रु क्षेत्री):", "11. Aquarius (Enemy Sign - Shani Kshetra):",
             "जातक मानवतावादी, नवीन अन्वेषक, सामाजिक समरसता का पक्षधर, एकांतप्रिय विचारक, स्वतंत्र विचारों वाला तथा दूरदर्शी दृष्टिकोण का स्वामी होता है।",
             "Humanitarian vision, unconventional innovator, advocate of social reform, introspective thinker, and endowed with cosmic, future-oriented consciousness."),
            ("१२. मीन राशि (मित्र क्षेत्री):", "12. Pisces (Friendly Sign - Guru Kshetra):",
             "जातक आध्यात्मिक, करुणामयी, शांत स्वभाव, मोक्ष मार्ग का खोजी, जल यात्राओं से लाभान्वित, दानी तथा परोपकारी होता है।",
             "Deeply spiritual, compassionate, tranquil, seeker of mystical liberation (Moksha), benefited by maritime travels, philanthropic, and altruistic.")
        ]

    items_html = []
    for hi_t, en_t, hi_desc, en_desc in signs_data:
        t = hi_t if is_hindi else en_t
        d = hi_desc if is_hindi else en_desc
        items_html.append(f"""
        <div class="sun-effect-item" style="margin-bottom:0.75rem;">
          <div style="color:var(--accent-gold); font-weight:700; font-size:0.92rem; border-bottom:1px dashed var(--page-border); padding-bottom:3px;">{t}</div>
          <div style="font-size:0.86rem; line-height:1.6; margin-top:0.3rem;">
            <p style="margin:0.25rem 0;">{d}</p>
          </div>
        </div>
        """)

    sec_label = f"अध्याय ४ • खण्ड {page_num - 47 + 8}" if is_hindi else f"Chapter 4 • Sun in Signs (Part {page_num - 47})"
    return f"""
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:0.75rem;">
        <div class="chapter-number">{sec_label}</div>
        <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{header_title}</h3>
      </div>
      <div class="rule-card">
        <div class="rule-body" style="font-size:0.86rem; line-height:1.6;">
          {''.join(items_html)}
        </div>
      </div>
    </div>
    """

# ------------------------------------------------------------------------------
# 6. SPECIAL MONOLINGUAL GENERATORS FOR SPECIAL RULE CARDS
# ------------------------------------------------------------------------------

def generate_drishti_rules_content(lang='hindi'):
    is_hindi = (lang == 'hindi')
    if is_hindi:
        card = """
        <div class="rule-card success">
          <div class="rule-header">
            <div class="rule-title">📜 शास्त्रीय दृष्टि नियम (फलित सिद्धांत)</div>
          </div>
          <div class="rule-body">
            <ul style="margin:0; padding-left:1.2rem; line-height:1.6; font-size:0.88rem;">
              <li><strong>सामान्य दृष्टि (सप्तम भाव):</strong> सभी ग्रह अपने अधिष्ठित भाव से सप्तम भाव पर पूर्ण दृष्टि डालते हैं।</li>
              <li><strong>विशेष पूर्ण दृष्टियां:</strong>
                <ul>
                  <li><strong>मंगल:</strong> चतुर्थ (४था), सप्तम (७वां) और अष्टम (८वां) भाव।</li>
                  <li><strong>गुरु (बृहस्पति):</strong> पंचम (५वां), सप्तम (७वां) और नवम (९वां) भाव।</li>
                  <li><strong>शनि:</strong> तृतीय (३रा), सप्तम (७वां) और दशम (१०वां) भाव।</li>
                </ul>
              </li>
              <li><strong>राहु एवं केतु:</strong> आधुनिक फलित ज्योतिष में पंचम, सप्तम व नवम दृष्टि व्यापक रूप से मान्य है।</li>
            </ul>
          </div>
        </div>
        """
    else:
        card = """
        <div class="rule-card success">
          <div class="rule-header">
            <div class="rule-title">📜 Classical Aspect Principles (Drishti Sutras)</div>
          </div>
          <div class="rule-body">
            <ul style="margin:0; padding-left:1.2rem; line-height:1.6; font-size:0.88rem;">
              <li><strong>Universal 7th Aspect:</strong> All planets cast a full 100% direct aspect onto the 7th house from their placement.</li>
              <li><strong>Special Full Aspects:</strong>
                <ul>
                  <li><strong>Mars:</strong> 4th, 7th, and 8th houses.</li>
                  <li><strong>Jupiter:</strong> 5th, 7th, and 9th houses.</li>
                  <li><strong>Saturn:</strong> 3rd, 7th, and 10th houses.</li>
                </ul>
              </li>
              <li><strong>Rahu &amp; Ketu:</strong> In classical Parashari treatises they do not cast direct ray aspects, but in predictive Jyotish, 5th, 7th, and 9th trinal aspects are widely accepted.</li>
            </ul>
          </div>
        </div>
        """
    return card

def generate_nakshatra_degrees_card(lang='hindi'):
    is_hindi = (lang == 'hindi')
    if is_hindi:
        return """
        <div class="rule-card">
          <div class="rule-body" style="font-size:0.88rem; line-height:1.6;">
            वैदिक ज्योतिष में संपूर्ण ३६०° भचक्र को २७ समान नक्षत्रों में विभाजित किया गया है। प्रत्येक नक्षत्र का विस्तार <strong>१३°२०’ (१३ अंश और २० कला)</strong> होता है। नीचे प्रत्येक नक्षत्र के प्रारंभिक एवं समापन अंश व्यवस्थित रूप से दिए गए हैं।
          </div>
        </div>
        """
    else:
        return """
        <div class="rule-card">
          <div class="rule-body" style="font-size:0.88rem; line-height:1.6;">
            In Vedic astronomy and astrology, the 360° zodiacal belt is systematically divided into 27 equal lunar mansions (Nakshatras). Each Nakshatra spans exactly <strong>13°20’ (13 degrees and 20 minutes of arc)</strong>. Below are the precise starting and ending boundaries for all 27 Nakshatras.
          </div>
        </div>
        """

def generate_deeptadi_9_states_content(lang='hindi'):
    is_hindi = (lang == 'hindi')
    if is_hindi:
        return """
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">अध्याय ४ • खण्ड १</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">दीप्तादि ९ अवस्थाएं: ग्रहों की स्थिति व फल</h3>
          </div>
          <div class="rule-card">
            <div class="rule-header">
              <div class="rule-title">दीप्तादि ९ अवस्थाएं (ग्रहों की स्थितियां व फल)</div>
              <span class="badge-chip badge-gold">पाराशरी सूत्र</span>
            </div>
            <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
              <p>महर्षि पाराशर के अनुसार ग्रहों की राशि स्थिति के आधार पर ९ अवस्थाएं होती हैं:</p>
              <ol style="margin:0; padding-left:1.25rem;">
                <li><strong>दीप्त अवस्था:</strong> ग्रह जब अपनी उच्च राशि में स्थित हो (परम शुभ एवं शक्तिशाली फल)।</li>
                <li><strong>स्वस्थ अवस्था:</strong> ग्रह जब अपनी स्वराशि में स्थित हो (आत्मबल, स्थिरता एवं अनुकूलता)।</li>
                <li><strong>मुदित अवस्था:</strong> ग्रह जब अपने अतिमित्र की राशि में स्थित हो (प्रसन्नता एवं सौभाग्य)।</li>
                <li><strong>शांत अवस्था:</strong> ग्रह जब अपने मित्र की राशि में स्थित हो (शांति, सहयोग एवं संतुलन)।</li>
                <li><strong>दीन अवस्था:</strong> ग्रह जब सम (तटस्थ) ग्रह की राशि में स्थित हो (साधारण व मध्यम फल)।</li>
                <li><strong>दुःखी अवस्था:</strong> ग्रह जब शत्रु ग्रह की राशि में स्थित हो (कष्ट, मानसिक तनाव एवं संघर्ष)।</li>
                <li><strong>विकल अवस्था:</strong> ग्रह जब पाप पीड़ित अथवा अशुभ युक्त हो (अस्थिरता एवं चिंता)।</li>
                <li><strong>खल अवस्था:</strong> ग्रह जब अतिशत्रु की राशि अथवा नीच राशि में हो (हानि व बाधाएं)।</li>
                <li><strong>कोप अवस्था:</strong> ग्रह जब सूर्य के अति निकट होकर अस्त हो (कारकतत्वों में क्षीणता)।</li>
              </ol>
            </div>
          </div>
        </div>
        """
    else:
        return """
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 4 • Section 1</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">Deeptadi 9 States: Planetary Conditions & Potencies</h3>
          </div>
          <div class="rule-card">
            <div class="rule-header">
              <div class="rule-title">Deeptadi 9 States (Planetary Conditions & Potencies)</div>
              <span class="badge-chip badge-gold">Parashari Sutras</span>
            </div>
            <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
              <p>According to Maharishi Parashara, a planet operates through 9 distinct psychological and energetic states based on its zodiacal placement:</p>
              <ol style="margin:0; padding-left:1.25rem;">
                <li><strong>Deepta (Radiant / Exalted):</strong> Placed in its exaltation sign; delivers maximum auspicious and powerful results.</li>
                <li><strong>Swastha (Comfortable / Own Sign):</strong> Placed in its own sign; indicates natural strength, stability, and ease.</li>
                <li><strong>Mudita (Delighted / Great Friend):</strong> Placed in a great friend's sign; bestows happiness, joy, and fortune.</li>
                <li><strong>Shanta (Peaceful / Friend Sign):</strong> Placed in a friendly sign; promotes harmony, cooperative endeavors, and calm.</li>
                <li><strong>Deena (Humbled / Neutral Sign):</strong> Placed in a neutral sign; yields moderate, average, and ordinary outcomes.</li>
                <li><strong>Dukhi (Distressed / Enemy Sign):</strong> Placed in an enemy's sign; brings struggle, psychological friction, and delays.</li>
                <li><strong>Vikala (Agitated / Malefic Affliction):</strong> Severely afflicted or associated with malefic planets; creates anxiety and restlessness.</li>
                <li><strong>Khala (Malicious / Debilitated):</strong> Placed in a great enemy sign or debilitation; causes hindrances, setbacks, and adversity.</li>
                <li><strong>Kopi (Combust / Enraged):</strong> In close combustion with the Sun; significations are scorched and rendered inward.</li>
              </ol>
            </div>
          </div>
        </div>
        """

def generate_leukemia_rules_content(lang='hindi'):
    is_hindi = (lang == 'hindi')
    if is_hindi:
        return """
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">अध्याय ५ • स्वास्थ्य खण्ड २६</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-crimson);">रक्त कैंसर (ल्यूकीमिया): ज्योतिषीय योग व शास्त्रीय सूत्र</h3>
          </div>
          <div class="rule-card">
            <div class="rule-header">
              <div class="rule-title">🩸 रक्त कैंसर (ल्यूकीमिया) के प्रामाणिक फलित सूत्र</div>
              <span class="badge-chip badge-crimson">शास्त्रीय निदान</span>
            </div>
            <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
              <p><strong>सूत्र १ (त्रिग्रह संयोजन):</strong> चन्द्रमा और मंगल की युति पर राहु का प्रभाव हो तथा शनि की पूर्ण दृष्टि हो। चन्द्र या मंगल ६ठे, ८वें अथवा १२वें भाव में स्थित हों और गुरु निर्बल या अस्त हों, तो रक्त कोशिकाओं में तीव्र विकृति (ल्यूकीमिया) की आशंका बनती है।</p>
              <p><strong>सूक्ष्म जैविक व ज्योतिषीय तर्क:</strong> चन्द्रमा = रक्त रस व शारीरिक द्रव ; मंगल = लाल रक्त कणिकाएं  व हीमोग्लोबिन; शनि = अवरोध व संकुचन; राहु = अनियंत्रित कोशिकीय म्यूटेशन; ६/८/१२ भाव = असाध्य रोग स्थान; गुरु = अस्थि मज्जा (अस्थि मज्जा) का प्राकृतिक रक्षक।</p>
              <p><strong>सूत्र २ (नीच ग्रह योग):</strong> वृश्चिक का नीचस्थ चन्द्रमा + कर्क का नीचस्थ मंगल, जिन पर राहु या शनि की दृष्टि हो और गुरु का त्रिक भावों पर कोई शुभ प्रभाव न हो।</p>
              <p><strong>सूत्र ३ (ग्रहण व रक्त दोष):</strong> चन्द्र-राहु ग्रहण योग के साथ मंगल षष्ठ अथवा अष्टम भाव में स्थित हो और गुरु बलहीन हों।</p>
              <p><strong>गोचर सक्रियता:</strong> शनि अथवा राहु का जन्म चन्द्र या षष्ठ भाव पर से गोचर, तथा चन्द्र, मंगल, राहु या षष्ठेश/अष्टमेश की दशा-अंतर्दशा में रोग का प्रकटीकरण होता है।</p>
            </div>
          </div>
        </div>
        """
    else:
        return """
        <div class="page-inner-content">
          <div class="chapter-header" style="margin-bottom:0.75rem;">
            <div class="chapter-number">Chapter 5 • Medical Section 26</div>
            <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-crimson);">Leukemia (Blood Cancer): Astrological Combinations & Etiology</h3>
          </div>
          <div class="rule-card">
            <div class="rule-header">
              <div class="rule-title">🩸 Hematological Malignancies (Leukemia) Classical Sutras</div>
              <span class="badge-chip badge-crimson">Diagnostic Rules</span>
            </div>
            <div class="rule-body" style="font-size:0.86rem; line-height:1.65;">
              <p><strong>Rule 1 (Tri-Planetary Affliction):</strong> Moon conjunct Mars, afflicted by Rahu and receiving aspect from Saturn. Moon or Mars placed in 6th, 8th, or 12th house, with Jupiter debilitated or combust.</p>
              <p><strong>Biological & Astrological Mechanism:</strong> Moon = plasma and fluid medium; Mars = erythrocytes , bone marrow matrix, and hemoglobin; Saturn = cellular suppression and immune deficiency; Rahu = abnormal proliferative mutation; 6th/8th/12th = dusthana triad of chronicity; Jupiter = leukocyte balance and bone marrow vitality.</p>
              <p><strong>Rule 2 (Dual Debilitation Matrix):</strong> Debilitated Moon in Scorpio combined with Debilitated Mars in Cancer, aspected by Rahu or Saturn without benefic Jupiter aspect.</p>
              <p><strong>Rule 3 (Eclipse & Blood Yoga):</strong> Moon-Rahu conjunction (Grahan Yoga) with Mars placed in 6th or 8th house and combust Jupiter.</p>
              <p><strong>Transit Activation Window:</strong> Saturn or Rahu transiting natal Moon or 6th house during operating dasha of Moon, Mars, Rahu, or 6th/8th lords marks the onset of clinical diagnosis.</p>
            </div>
          </div>
        </div>
        """

# ------------------------------------------------------------------------------
# 7. MONOLINGUAL EDITION BUILDERS (ALL 87 PAGES)
# ------------------------------------------------------------------------------

def generate_hindi_pages(orig_pages):
    hindi_pages = []

    # Page 1: Pure Hindi Cover (Minimalist)
    p1 = """
    <div class="cover-page-inner">
      <div class="cover-ornament-corner top-left"></div>
      <div class="cover-ornament-corner top-right"></div>
      <div class="cover-ornament-corner bottom-left"></div>
      <div class="cover-ornament-corner bottom-right"></div>

      <div class="cover-yantra">
        <img src="assets/yantra.svg" alt="Sacred Sri Yantra Emblem" width="135" height="135">
      </div>

      <h1 class="cover-title-hindi">वैदिक ज्योतिष महाग्रंथ सरलीकृत</h1>
      <div class="cover-title-english">सम्पूर्ण प्रामाणिक शास्त्रीय फलित ज्ञानकोश</div>

      <div class="cover-divider-flourish">⚜ ☸ ⚜</div>

      <div class="cover-subtitle-minimal">बृहत् शास्त्रीय सूत्र, खगोल गणित एवं फलित सिद्धांतों का अद्वितीय संग्रह</div>

      <div class="cover-footer-brand">
        <div class="cover-tag">तंत्र ज्ञान शोध संस्थान • २०२६ • सम्पूर्ण हिन्दी संस्करण</div>
      </div>
    </div>
    """
    hindi_pages.append({
        "chapter": get_chapter_name(0, 'hindi'),
        "title": HINDI_TITLES[0],
        "content": p1
    })

    # Page 2: Auspicious Invocation (मंगलाचरण — ॐ गं गणपतये नमः)
    p_invoc = """
    <div class="invocation-page-inner">
      <div class="invocation-icon-emblem">
        <img src="assets/ganesha.svg" alt="श्री गणेश पावन प्रतीक" width="105" height="105">
      </div>

      <div class="invocation-mantra">॥ ॐ गं गणपतये नमः ॥</div>

      <div class="invocation-shloka">
        वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ।<br>
        निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥
      </div>

      <div class="invocation-meaning">
        <em>"हे वक्रतुंड, विशालकाय, करोड़ों सूर्यों के समान तेजस्वी प्रभु श्री गणेश! कृपा करके हमारे इस शास्त्रीय ग्रन्थ व साधना के समस्त विघ्नों को सदा के लिए दूर करें।"</em>
      </div>

      <div class="cover-divider-flourish" style="margin: 0.5rem auto;">☸ ॐ ☸</div>

      <div class="invocation-footer">॥ शुभं भवतु • सर्व मंगल मांगल्ये ॥</div>
    </div>
    """
    hindi_pages.append({
        "chapter": get_chapter_name(1, 'hindi'),
        "title": HINDI_TITLES[1],
        "content": p_invoc
    })

    # Page 3: Author Profile (Pure Hindi)
    p2 = """
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:1.25rem;">
        <div class="chapter-number">लेखक परिचय</div>
        <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-crimson);">लेखक परिचय — ज्योतिषाचार्य आशुतोष कुमार चौबे</h2>
      </div>

      <div class="author-profile-box">
        <div class="author-avatar-badge">🕉️</div>
        <div class="author-bio-text">
          <h3>आशुतोष कुमार चौबे</h3>
          <div class="author-meta">वैदिक ज्योतिषी एवं तंत्र शोधकर्ता</div>
          <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
            समर्पित वैदिक ज्योतिषी एवं शोधकर्ता, जिन्होंने शास्त्रीय ज्योतिष ग्रंथों और आधुनिक विश्लेषणात्मक पद्धतियों के समन्वय से 'तंत्र ज्ञान' ज्ञानकोश की रचना की है।
          </p>
        </div>
      </div>

      <div class="rule-card">
        <div class="rule-header">
          <div class="rule-title">📜 शोध दृष्टि एवं शास्त्रीय परंपरा</div>
          <span class="badge-chip badge-gold">प्रामाणिक दृष्टिकोण</span>
        </div>
        <div class="rule-body">
          <p>
            <strong>ज्योतिषाचार्य आशुतोष कुमार चौबे</strong> का मुख्य ध्येय प्राचीन वैदिक ज्ञान को अंधविश्वास, भय एवं रूढ़िवादिता से मुक्त करके एक तार्किक, वैज्ञानिक तथा व्यावहारिक सूत्रबद्ध पद्धति के रूप में प्रस्तुत करना है।
          </p>
          <p>
            इन्होंने <em>बृहत्पाराशर होरा शास्त्र, सारावली (कल्याण वर्मा), फलदीपिका (मन्त्रेश्वर), जातक पारिजात, नंदी नाड़ी</em> तथा <em>लाल किताब</em> जैसे मूर्धन्य ग्रंथों का गहन अध्ययन करके उनके रहस्यों को वर्तमान संदर्भ में सत्यापनीय नियमों के रूप में रूपांतरित किया है।
          </p>
        </div>
      </div>

      <div class="rule-card success">
        <div class="rule-header">
          <div class="rule-title">🎯 फलित ज्योतिष दर्शन एवं कर्म सिद्धांत</div>
          <span class="badge-chip badge-gold">मार्गदर्शक दृष्टि</span>
        </div>
        <div class="rule-body">
          <p>
            आशुतोष जी का मानना है कि जन्मकुण्डली केवल भविष्य की घटनाओं का पूर्वानुमान नहीं, बल्कि मनुष्य के संचित कर्मों और प्रारब्ध का एक सूक्ष्म खगोलीय मानचित्र है।
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
        <strong style="color:var(--text-heading); font-size:0.92rem;">आधिकारिक शोध, वेबसाइट एवं संपर्क मंच:</strong><br>
        <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem; margin-top:0.75rem;">
          <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="contact-channel-badge" style="border-color:var(--accent-gold); color:var(--accent-gold) !important; font-weight:700;">
            <span class="contact-icon">🌐</span>
            <span>वेबसाइट: <strong>t.worldgyan.com</strong></span>
          </a>
          <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge" style="margin-top:0;">
            <span class="yt-play-icon">▶</span>
            <span>यूट्यूब: <strong>@TantraGyan108</strong></span>
          </a>
        </div>
        <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.8rem; font-size:0.82rem; margin-top:0.6rem;">
          <a href="mailto:tantraresearchcenter@gmail.com" style="color:var(--text-secondary); text-decoration:none;">✉️ tantraresearchcenter@gmail.com</a>
          <span style="color:var(--border-color);">•</span>
          <a href="tel:+919658476170" style="color:var(--text-secondary); text-decoration:none;">📞 +91 9658476170</a>
        </div>
      </div>
    </div>
    """
    hindi_pages.append({
        "chapter": get_chapter_name(2, 'hindi'),
        "title": HINDI_TITLES[2],
        "content": p2
    })

    # Page 4: Study Guide (Pure Hindi)
    p3 = """
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:1.25rem;">
        <div class="chapter-number">अध्ययन निर्देशिका</div>
        <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-gold);">ग्रंथ का अध्ययन कैसे करें? • आधारभूत संरचना</h2>
      </div>

      <div class="rule-card">
        <div class="rule-header">
          <div class="rule-title">📖 ग्रंथ का उद्देश्य एवं अध्ययन विधि</div>
          <span class="badge-chip badge-gold">मार्गदर्शिका</span>
        </div>
        <div class="rule-body">
          <p>
            'तंत्र ज्ञान' महाग्रंथ को एक <strong>व्यावहारिक फलित ज्योतिष ज्ञानकोश</strong> के रूप में तैयार किया गया है। इसका उद्देश्य विद्यार्थियों, शोधार्थियों और अनुभवी ज्योतिषियों को सारणीबद्ध, त्वरित एवं प्रामाणिक संदर्भ प्रदान करना है।
          </p>
        </div>
      </div>

      <div class="pillar-grid">
        <div class="pillar-card">
          <div class="pillar-number">स्तम्भ १ • अध्याय २</div>
          <div class="pillar-title">नवग्रह कारकत्व व १७ राजयोग</div>
          <div class="pillar-desc">सूर्य से केतु तक ९ ग्रहों के संपूर्ण शारीरिक, मानसिक, संबंधपरक कारकत्व एवं पंच महापुरुष आदि १७ राजयोग।</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">स्तम्भ २ • अध्याय ३</div>
          <div class="pillar-title">राशि, नक्षत्र व ग्रह गति</div>
          <div class="pillar-desc">ग्रहों की गति, कक्षा भ्रमण, गोचर अवधि, दृष्टि नियम, २७ नक्षत्रों का विस्तार, देवता एवं चार तत्व।</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">स्तम्भ ३ • अध्याय ४</div>
          <div class="pillar-title">दीप्तादि ९ अवस्थाएं व सूर्य फल</div>
          <div class="pillar-desc">ग्रहों की ९ अवस्थाएं, १२ भावों के स्थिर कारक तथा सूर्य का १२ भावों व १२ राशियों में विस्तृत फल।</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">स्तम्भ ४ • अध्याय ५</div>
          <div class="pillar-title">आयुर्वेद-ज्योतिष व स्वास्थ्य</div>
          <div class="pillar-desc">१२ भावों, १२ राशियों और ९ ग्रहों का शारीरिक अंग-रोग संबंध तथा रोग प्रकटीकरण के शास्त्रीय सूत्र।</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">स्तम्भ ५ • अध्याय ६</div>
          <div class="pillar-title">नक्षत्र पद व सूक्ष्म विश्लेषण</div>
          <div class="pillar-desc">२७ नक्षत्रों के १०८ पदों का नवांश गणित, अश्विनी, पुष्य व आश्लेषा के ४ पदों का मनोवैज्ञानिक विश्लेषण।</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">स्तम्भ ६ • संदर्भ</div>
          <div class="pillar-title">शास्त्रीय ग्रंथ संदर्भ</div>
          <div class="pillar-desc">बृहत्पाराशर होरा शास्त्र, सारावली, फलदीपिका, जातक पारिजात, नंदी नाड़ी एवं लाल किताब के प्रामाणिक संदर्भ।</div>
        </div>
      </div>
    </div>
    """
    hindi_pages.append({
        "chapter": get_chapter_name(3, 'hindi'),
        "title": HINDI_TITLES[3],
        "content": p3
    })

    # Page 5: Discipline & Disclaimer (Pure Hindi)
    p4 = """
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:1.25rem;">
        <div class="chapter-number">अनुशासन व वैधानिक सूचना</div>
        <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-crimson);">तांत्रिक अनुशासन, आचार संहिता एवं वैधानिक परामर्श</h2>
      </div>

      <div class="rule-card">
        <div class="rule-header">
          <div class="rule-title">🕉️ तांत्रिक अनुशासन एवं आचार संहिता</div>
          <span class="badge-chip badge-gold">शास्त्रीय मर्यादा</span>
        </div>
        <div class="rule-body">
          <p>
            वैदिक ज्योतिष केवल भविष्य जानने का साधन नहीं, बल्कि आत्म-बोध और चेतना के रूपांतरण का मार्ग है। एक ज्योतिषी के लिए सत्य, संयम, करुणा और निस्वार्थ सेवा परम धर्म है।
          </p>
        </div>
      </div>

      <div class="rule-card success">
        <div class="rule-header">
          <div class="rule-title">⚖️ वैधानिक अस्वीकरण एवं चिकित्सा परामर्श</div>
        </div>
        <div class="rule-body" style="font-size:0.85rem; line-height:1.6;">
          <p>
            इस ग्रंथ में दिए गए समस्त फलित एवं आयुर्वेद-ज्योतिषीय सूत्र केवल <strong>शैक्षणिक, अनुसंधान एवं आध्यात्मिक मार्गदर्शन</strong> के उद्देश्य से प्रस्तुत किए गए हैं।
          </p>
          <p>
            यह ग्रंथ किसी भी प्रकार से योग्य एलोपैथिक चिकित्सक, सर्जन या अस्पताल की चिकित्सा सलाह, निदान अथवा उपचार का विकल्प नहीं है। किसी भी स्वास्थ्य समस्या में सर्वप्रथम योग्य विशेषज्ञ चिकित्सक से परामर्श अनिवार्य है।
          </p>
        </div>
      </div>
    </div>
    """
    hindi_pages.append({
        "chapter": get_chapter_name(4, 'hindi'),
        "title": HINDI_TITLES[4],
        "content": p4
    })

    # Page 6: Table of Contents (Pure Hindi)
    p5 = """
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:1rem;">
        <div class="chapter-number">ग्रंथ अनुक्रमणिका</div>
        <h2 class="chapter-heading" style="font-size:1.35rem; color:var(--accent-gold);">विषय-सूची — षडंग महाग्रंथ</h2>
      </div>

      <div class="toc-notebook-list">
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय १</span>
            <strong style="font-size:0.88rem;">प्रस्तावना, मंगलाचरण, लेखक परिचय, अध्ययन निर्देशिका व आचार संहिता</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ १ - ६</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय २</span>
            <strong style="font-size:0.88rem;">नवग्रह कारकत्व एवं १७ शास्त्रीय राजयोग</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ७ - २१</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय ३</span>
            <strong style="font-size:0.88rem;">राशि, नक्षत्र, ग्रह गति एवं विंशोत्तरी महादशा चक्र</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ २२ - ३८</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय ४</span>
            <strong style="font-size:0.88rem;">भाव एवं राशियों में ग्रह (दीप्तादि ९ अवस्थाएं व सूर्य फल)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ३९ - ४९</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय ५</span>
            <strong style="font-size:0.88rem;">आयुर्वेद-ज्योतिष व स्वास्थ्य विश्लेषण (२७ तालिकाएं)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ५० - ७६</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय ६</span>
            <strong style="font-size:0.88rem;">नक्षत्रों का गहन पद एवं ग्रह विश्लेषण (११ तालिकाएं)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ७७ - ८७</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">समापन</span>
            <strong style="font-size:0.88rem;">समापन पृष्ठ, उपनिषद् मंगल श्लोक व आधिकारिक संपर्क</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ८८</span>
        </div>
      </div>
    </div>
    """
    hindi_pages.append({
        "chapter": get_chapter_name(5, 'hindi'),
        "title": HINDI_TITLES[5],
        "content": p5
    })

    # Pages 7 to 87 (Indices 6 to 86)
    for idx in range(6, 87):
        orig_p = orig_pages[idx]
        page_num = idx + 1
        page_title = HINDI_TITLES[idx]
        ch_name = get_chapter_name(idx, 'hindi')

        # Dedicated generators
        if page_num == 23:
            card_html = generate_drishti_rules_content(lang='hindi')
            tbl_clean = localize_html_table(re.search(r'<table.*?</table\s*>', orig_p['content'], re.DOTALL).group(0), idx, target_lang='hindi')
            content = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">अध्याय ३ • खण्ड २</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{page_title}</h3>
              </div>
              {card_html}
              <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (क्षैतिज दर्शन)</div>
              <div class="astro-table-container">
                {tbl_clean}
              </div>
            </div>
            """
        elif page_num == 24:
            card_html = generate_nakshatra_degrees_card(lang='hindi')
            tbl_clean = localize_html_table(re.search(r'<table.*?</table\s*>', orig_p['content'], re.DOTALL).group(0), idx, target_lang='hindi')
            content = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">अध्याय ३ • खण्ड ३</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{page_title}</h3>
              </div>
              {card_html}
              <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (क्षैतिज दर्शन)</div>
              <div class="astro-table-container">
                {tbl_clean}
              </div>
            </div>
            """
        elif page_num == 39:
            content = generate_deeptadi_9_states_content(lang='hindi')
        elif page_num in [46, 47]:
            content = generate_sun_houses_content(page_num, lang='hindi')
        elif page_num in [48, 49]:
            content = generate_sun_signs_content(page_num, lang='hindi')
        elif page_num == 75:
            content = generate_leukemia_rules_content(lang='hindi')
        elif page_num == 76:
            rule_card = """
            <div class="rule-card danger">
              <div class="rule-header">
                <div class="rule-title">🔬 त्वचा कैंसर • शास्त्रीय फलित सूत्र</div>
                <span class="badge-chip badge-gold">चिकित्सा ज्योतिष</span>
              </div>
              <div class="rule-body">
                <p><strong>मूल शास्त्रीय सिद्धांत:</strong> त्वचा का नैसर्गिक कारक ग्रह <strong>बुध</strong> है तथा रक्त व ऊतकों में तीव्र प्रदाह का कारक <strong>मंगल</strong> है। जब बुध पर पापी ग्रहों (राहु/शनि/मंगल) की क्रूर युति या दृष्टि हो और वह ६ठे, ८वें या लग्न भाव में स्थित होकर पीड़ित हो, तो असामान्य कोशिका विभाजन एवं त्वचा कैंसर का योग बनता है।</p>
              </div>
            </div>
            """
            tbl_match = re.search(r'<table.*?</table\s*>', orig_p['content'], re.DOTALL)
            tbl_clean = localize_html_table(tbl_match.group(0), idx, target_lang='hindi') if tbl_match else ""
            content = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">अध्याय ५ • स्वास्थ्य खण्ड २७</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-crimson);">{page_title}</h3>
              </div>
              {rule_card}
              <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>तालिका को दाएं-बाएं स्क्रॉल करें (क्षैतिज दर्शन)</div>
              <div class="astro-table-container">
                {tbl_clean}
              </div>
            </div>
            """
        else:
            c = orig_p['content']
            # Clean out raw scraped h4 title blocks that duplicated headers
            cb_m = re.search(r'<div class="content-block">(.*?)</div>', c, re.DOTALL)
            if cb_m:
                cb_txt = cb_m.group(1).strip()
                # If content-block is only h4 titles, strip it
                if not ('class="rule-card' in cb_txt or 'class="pillar' in cb_txt or '<p>' in cb_txt):
                    c = c.replace(cb_m.group(0), '')

            # Localize section indicators and hints
            c = c.replace('तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)', 'तालिका को दाएं-बाएं स्क्रॉल करें (क्षैतिज दर्शन)')
            c = c.replace('<span class="rule-badge">सूत्र / Rule</span>', '<span class="rule-badge">शास्त्रीय सूत्र</span>')
            c = c.replace('<span class="formula-pill">मंगल (Mars) के संपूर्ण कारकत्व और संकेतक</span>', '<span class="formula-pill">मंगल देव के संपूर्ण शास्त्रीय कारकत्व एवं संकेतक</span>')
            c = re.sub(r'Chapter (\d+) • Section (\d+)', r'अध्याय \1 • खण्ड \2', c)
            c = re.sub(r'Chapter (\d+) • Table (\d+)', r'अध्याय \1 • तालिका \2', c)
            c = re.sub(r'Chapter (\d+) • Medical Section (\d+)', r'अध्याय \1 • स्वास्थ्य खण्ड \2', c)
            c = re.sub(r'Chapter (\d+) • Pada Section (\d+)', r'अध्याय \1 • पद खण्ड \2', c)
            
            # Localize table heading and eliminate duplicate table captions
            c = re.sub(r'<h3 class="chapter-heading"[^>]*>.*?</h3>', f'<h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{page_title}</h3>', c)
            c = re.sub(r'<div class="table-caption">.*?</div>', '', c)

            # Localize tables inside
            tbl_match = re.search(r'<table.*?</table\s*>', c, re.DOTALL)
            if tbl_match:
                new_tbl = localize_html_table(tbl_match.group(0), idx, target_lang='hindi')
                c = c[:tbl_match.start()] + new_tbl + c[tbl_match.end():]
            
            content = c

        hindi_pages.append({
            "chapter": ch_name,
            "title": page_title,
            "content": content
        })

    # Page 88: Grand Back Cover (Pure Hindi)
    p_last = """
    <div class="back-cover-inner">
      <div class="cover-ornament-corner top-left"></div>
      <div class="cover-ornament-corner top-right"></div>
      <div class="cover-ornament-corner bottom-left"></div>
      <div class="cover-ornament-corner bottom-right"></div>

      <div class="cover-yantra" style="width:110px; height:110px; margin-bottom:0.35rem;">
        <img src="assets/yantra.svg" alt="Tantra Gyan Sacred Seal" width="110" height="110">
      </div>

      <div class="back-cover-title">वैदिक ज्योतिष महाग्रंथ सरलीकृत</div>
      <div class="back-cover-subtitle">सम्पूर्ण प्रामाणिक शास्त्रीय फलित ज्ञानकोश</div>

      <div class="invocation-shloka" style="margin: 0.75rem auto; max-width: 90%;">
        ॥ असतो मा सद्गमय। तमसो मा ज्योतिर्गमय। मृत्योर्मा अमृतं गमय॥<br>
        ॥ ॐ पूर्णमदः पूर्णमिदं पूर्णात्पूर्णमुदच्यते। पूर्णस्य पूर्णमादाय पूर्णमेवावशिष्यते॥<br>
        ॥ ॐ शान्तिः शान्तिः शान्तिः ॥
      </div>

      <div class="back-cover-colophon">
        <div style="font-weight:700; color:var(--accent-gold); font-size:0.95rem; margin-bottom:0.25rem;">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)</div>
        <div style="color:var(--text-secondary); font-size:0.85rem;">लेखक एवं ज्योतिषाचार्य: <strong>ज्योतिषाचार्य आशुतोष कुमार चौबे</strong></div>
        <div style="font-size:0.8rem; color:var(--text-muted); margin-top:0.35rem;">सर्वाधिकार सुरक्षित © २०२६. All rights reserved.</div>
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
    """
    hindi_pages.append({
        "chapter": get_chapter_name(87, 'hindi'),
        "title": HINDI_TITLES[87],
        "content": p_last
    })

    return hindi_pages


def generate_english_pages(orig_pages):
    english_pages = []

    # Page 1: Complete English Cover (Minimalist)
    p1 = """
    <div class="cover-page-inner">
      <div class="cover-ornament-corner top-left"></div>
      <div class="cover-ornament-corner top-right"></div>
      <div class="cover-ornament-corner bottom-left"></div>
      <div class="cover-ornament-corner bottom-right"></div>

      <div class="cover-yantra">
        <img src="assets/yantra.svg" alt="Sacred Sri Yantra Emblem" width="135" height="135">
      </div>

      <h1 class="cover-title-hindi" style="font-family:var(--font-heading); font-size:2.05rem;">Complete Vedic Astrology Compendium</h1>
      <div class="cover-title-english">Authoritative Classical Principles & Predictive Synthesis</div>

      <div class="cover-divider-flourish">⚜ ☸ ⚜</div>

      <div class="cover-subtitle-minimal">Master Reference of Navagraha Karakatva, Raja Yogas, Nakshatra Padas & Medical Astrology</div>

      <div class="cover-footer-brand">
        <div class="cover-tag">Tantra Gyan Research Center • 2026 • English Edition</div>
      </div>
    </div>
    """
    english_pages.append({
        "chapter": get_chapter_name(0, 'english'),
        "title": ENGLISH_TITLES[0],
        "content": p1
    })

    # Page 2: Auspicious Invocation (मंगलाचरण — ॐ गं गणपतये नमः)
    p_invoc = """
    <div class="invocation-page-inner">
      <div class="invocation-icon-emblem">
        <img src="assets/ganesha.svg" alt="Lord Shree Ganesha Emblem" width="105" height="105">
      </div>

      <div class="invocation-mantra">॥ Oṁ Gaṁ Gaṇapataye Namaḥ ॥</div>

      <div class="invocation-shloka">
        वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ।<br>
        निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥
      </div>

      <div class="invocation-meaning">
        <em>"O Lord Ganesha of curved trunk and immense cosmic form, whose brilliance radiates as ten million suns, please dispel all impediments from our sacred study and endeavors forever."</em>
      </div>

      <div class="cover-divider-flourish" style="margin: 0.5rem auto;">☸ ॐ ☸</div>

      <div class="invocation-footer">॥ Śubhaṁ Bhavatu • Universal Auspiciousness & Peace ॥</div>
    </div>
    """
    english_pages.append({
        "chapter": get_chapter_name(1, 'english'),
        "title": ENGLISH_TITLES[1],
        "content": p_invoc
    })

    # Page 2: Author Profile (English)
    p2 = """
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:1.25rem;">
        <div class="chapter-number">Author Profile</div>
        <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-crimson);">Author Profile — Astrologer Ashutosh Kumar Choubey</h2>
      </div>

      <div class="author-profile-box">
        <div class="author-avatar-badge">🕉️</div>
        <div class="author-bio-text">
          <h3>Ashutosh Kumar Choubey</h3>
          <div class="author-meta">Vedic Astrologer & Tantra Researcher</div>
          <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
            Dedicated Vedic astrologer and researcher who harmonized classical Jyotish shastras with rigorous modern analytical frameworks to create the 'Tantra Gyan' compendium.
          </p>
        </div>
      </div>

      <div class="rule-card">
        <div class="rule-header">
          <div class="rule-title">📜 Research Lineage & Classical Traditions</div>
          <span class="badge-chip badge-gold">Authentic Foundations</span>
        </div>
        <div class="rule-body">
          <p>
            <strong>Astrologer Ashutosh Kumar Choubey</strong> is committed to liberating ancient Vedic knowledge from superstition and fatalistic dogma, presenting it as a rational, verifiable, and deeply empowering science of human consciousness.
          </p>
          <p>
            Through deep research into authoritative treatises—including <em>Brihat Parashara Hora Shastra, Saravali (Kalyan Verma), Phaladeepika (Mantreshwara), Jataka Parijata, Nandi Nadi,</em> and <em>Lal Kitab</em>—he formulated reproducible principles applicable to modern charts.
          </p>
        </div>
      </div>

      <div class="rule-card success">
        <div class="rule-header">
          <div class="rule-title">🎯 Predictive Philosophy & Karmic Principles</div>
          <span class="badge-chip badge-gold">Core Vision</span>
        </div>
        <div class="rule-body">
          <p>
            Ashutosh Ji views the horoscope not as an unalterable fate, but as an intricate cosmic blueprint of accumulated karmas (Sanchita Karma) and ripe destiny (Prarabdha).
          </p>
          <p>
            By scientifically analyzing planetary dashas, transits, and house significations, an individual can identify inherent potentials, prepare for cycles of challenge, and execute conscious, corrective karma (Kriyamana).
          </p>
          <p style="font-size:0.84rem; color:var(--text-muted); margin-top:0.4rem;">
            <em>"Astrology is not helpless surrender to destiny; it is a radiant beacon of self-awareness and conscious karmic mastery."</em>
          </p>
        </div>
      </div>

      <div style="margin-top:1.25rem; padding:1.1rem; border:1px dashed var(--accent-gold); border-radius:10px; background:rgba(179,127,25,0.06); text-align:center;">
        <strong style="color:var(--text-heading); font-size:0.92rem;">Official Research, Website & Contact Channels:</strong><br>
        <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem; margin-top:0.75rem;">
          <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="contact-channel-badge" style="border-color:var(--accent-gold); color:var(--accent-gold) !important; font-weight:700;">
            <span class="contact-icon">🌐</span>
            <span>Website: <strong>t.worldgyan.com</strong></span>
          </a>
          <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge" style="margin-top:0;">
            <span class="yt-play-icon">▶</span>
            <span>YouTube: <strong>@TantraGyan108</strong></span>
          </a>
        </div>
        <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.8rem; font-size:0.82rem; margin-top:0.6rem;">
          <a href="mailto:tantraresearchcenter@gmail.com" style="color:var(--text-secondary); text-decoration:none;">✉️ tantraresearchcenter@gmail.com</a>
          <span style="color:var(--border-color);">•</span>
          <a href="tel:+919658476170" style="color:var(--text-secondary); text-decoration:none;">📞 +91 9658476170</a>
        </div>
      </div>
    </div>
    """
    english_pages.append({
        "chapter": get_chapter_name(2, 'english'),
        "title": ENGLISH_TITLES[2],
        "content": p2
    })

    # Page 3: Study Guide (English)
    p3 = """
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:1.25rem;">
        <div class="chapter-number">Study Guide</div>
        <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-gold);">Reader's Study Guide & Core Architecture</h2>
      </div>

      <div class="rule-card">
        <div class="rule-header">
          <div class="rule-title">📖 Architectural Framework & Method of Study</div>
          <span class="badge-chip badge-gold">Guide</span>
        </div>
        <div class="rule-body">
          <p>
            'Tantra Gyan' is structured as a <strong>concise, high-density practitioner notebook</strong> designed to serve as an instant, reliable desktop reference for students, practitioners, and scholars.
          </p>
        </div>
      </div>

      <div class="pillar-grid">
        <div class="pillar-card">
          <div class="pillar-number">Pillar 1 • Chapter 2</div>
          <div class="pillar-title">Navagraha Karakatva & 17 Raja Yogas</div>
          <div class="pillar-desc">Comprehensive bodily, psychological, and spiritual significations of all 9 planets, plus Pancha Mahapurusha and 17 classical yogas.</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">Pillar 2 • Chapter 3</div>
          <div class="pillar-title">Signs, Nakshatras & Planetary Motion</div>
          <div class="pillar-desc">Planetary transit durations, aspect rules, 27 Nakshatras degree boundaries, deities, and the four cosmic elements.</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">Pillar 3 • Chapter 4</div>
          <div class="pillar-title">Deeptadi 9 States & Solar Interpretations</div>
          <div class="pillar-desc">9 planetary operational states, 12 house karakas, and detailed predictive effects of the Sun across all houses and signs.</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">Pillar 4 • Chapter 5</div>
          <div class="pillar-title">Medical Astrology & Health Analysis</div>
          <div class="pillar-desc">Anatomical mappings of the 12 houses and signs, diagnostic patterns, and classical disease timing.</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">Pillar 5 • Chapter 6</div>
          <div class="pillar-title">Nakshatra Padas & Subtle Analysis</div>
          <div class="pillar-desc">Navamsha division of 108 padas, deep psychological insights into Ashwini, Pushya, and Ashlesha padas.</div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">Pillar 6 • References</div>
          <div class="pillar-title">Classical Shastric Lineage</div>
          <div class="pillar-desc">Direct citations from Brihat Parashara Hora Shastra, Saravali, Phaladeepika, and Jataka Parijata.</div>
        </div>
      </div>
    </div>
    """
    english_pages.append({
        "chapter": get_chapter_name(3, 'english'),
        "title": ENGLISH_TITLES[3],
        "content": p3
    })

    # Page 4: Tantric Ethics & Disclaimer (English)
    p4 = """
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:1.25rem;">
        <div class="chapter-number">Ethics & Guidance</div>
        <h2 class="chapter-heading" style="font-size:1.4rem; color:var(--accent-crimson);">Tantric Discipline, Ethical Code & Legal Disclaimer</h2>
      </div>

      <div class="rule-card">
        <div class="rule-header">
          <div class="rule-title">🕉️ Tantric Discipline & Astrologer's Code</div>
          <span class="badge-chip badge-gold">Sacred Responsibility</span>
        </div>
        <div class="rule-body">
          <p>
            Vedic astrology is not a tool for commercial exploitation or fear-mongering; it is a sacred light (Jyotir-Veda) to dispel darkness. A true practitioner must maintain purity of speech, mental discipline, and compassionate detachment.
          </p>
        </div>
      </div>

      <div class="rule-card success">
        <div class="rule-header">
          <div class="rule-title">⚖️ Legal & Medical Disclaimer</div>
        </div>
        <div class="rule-body" style="font-size:0.85rem; line-height:1.6;">
          <p>
            All predictive principles, anatomical correspondences, and medical astrological references in this volume are presented solely for <strong>educational, research, and philosophical purposes</strong>.
          </p>
          <p>
            Astrological analysis must never replace professional medical diagnosis, surgery, or clinical treatments. Readers experiencing health concerns must always consult licensed medical practitioners.
          </p>
        </div>
      </div>
    </div>
    """
    english_pages.append({
        "chapter": get_chapter_name(4, 'english'),
        "title": ENGLISH_TITLES[4],
        "content": p4
    })

    # Page 5: Table of Contents (English)
    p5 = """
    <div class="page-inner-content">
      <div class="chapter-header" style="margin-bottom:1rem;">
        <div class="chapter-number">Table of Contents</div>
        <h2 class="chapter-heading" style="font-size:1.35rem; color:var(--accent-gold);">Systematic Table of Contents</h2>
      </div>

      <div class="toc-notebook-list">
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 1</span>
            <strong style="font-size:0.88rem;">Preface, Invocation, Author Profile, Study Guide & Ethical Code</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 1 - 6</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 2</span>
            <strong style="font-size:0.88rem;">Planetary Karakatva & 17 Classical Raja Yogas</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 7 - 21</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 3</span>
            <strong style="font-size:0.88rem;">Zodiac Signs, 27 Nakshatras & Vimshottari Mahadasha</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 22 - 38</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 4</span>
            <strong style="font-size:0.88rem;">Planetary States (9 Deeptadi Avasthas) & Solar Interpretations</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 39 - 49</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 5</span>
            <strong style="font-size:0.88rem;">Medical Astrology & Health Diagnostics (27 Complete Tables)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 50 - 76</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 6</span>
            <strong style="font-size:0.88rem;">Nakshatra Pada Analysis & Subtle Interpretations (11 Tables)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 77 - 87</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Colophon</span>
            <strong style="font-size:0.88rem;">Sacred Benediction, Upanishad Shloka & Official Contact</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Page 88</span>
        </div>
      </div>
    </div>
    """
    english_pages.append({
        "chapter": get_chapter_name(5, 'english'),
        "title": ENGLISH_TITLES[5],
        "content": p5
    })

    # Pages 7 to 87 (Indices 6 to 86)
    for idx in range(6, 87):
        orig_p = orig_pages[idx]
        page_num = idx + 1
        page_title = ENGLISH_TITLES[idx]
        ch_name = get_chapter_name(idx, 'english')

        # Dedicated generators
        if page_num == 23:
            card_html = generate_drishti_rules_content(lang='english')
            tbl_clean = localize_html_table(re.search(r'<table.*?</table\s*>', orig_p['content'], re.DOTALL).group(0), idx, target_lang='english')
            content = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 3 • Section 2</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{page_title}</h3>
              </div>
              {card_html}
              <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>Scroll table horizontally to view full columns</div>
              <div class="astro-table-container">
                {tbl_clean}
              </div>
            </div>
            """
        elif page_num == 24:
            card_html = generate_nakshatra_degrees_card(lang='english')
            tbl_clean = localize_html_table(re.search(r'<table.*?</table\s*>', orig_p['content'], re.DOTALL).group(0), idx, target_lang='english')
            content = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 3 • Section 3</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{page_title}</h3>
              </div>
              {card_html}
              <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>Scroll table horizontally to view full columns</div>
              <div class="astro-table-container">
                {tbl_clean}
              </div>
            </div>
            """
        elif page_num == 39:
            content = generate_deeptadi_9_states_content(lang='english')
        elif page_num in [46, 47]:
            content = generate_sun_houses_content(page_num, lang='english')
        elif page_num in [48, 49]:
            content = generate_sun_signs_content(page_num, lang='english')
        elif page_num == 75:
            content = generate_leukemia_rules_content(lang='english')
        elif page_num == 76:
            rule_card = """
            <div class="rule-card danger">
              <div class="rule-header">
                <div class="rule-title">🔬 Skin Cancer (Cutaneous Malignancies) • Classical Jyotish Sutras</div>
                <span class="badge-chip badge-gold">Medical Astrology</span>
              </div>
              <div class="rule-body">
                <p><strong>Core Classical Principle:</strong> <strong>Mercury</strong> is the primary natural significator (Naisargika Karaka) of the skin (Twacha), while <strong>Mars</strong> governs cellular inflammation. When Mercury is severely afflicted by Mars, Rahu, or Saturn in the 6th, 8th, or 1st house without benefic Jupiterian mitigation, abnormal cutaneous cell proliferation and malignancy risks manifest.</p>
              </div>
            </div>
            """
            tbl_match = re.search(r'<table.*?</table\s*>', orig_p['content'], re.DOTALL)
            tbl_clean = localize_html_table(tbl_match.group(0), idx, target_lang='english') if tbl_match else ""
            content = f"""
            <div class="page-inner-content">
              <div class="chapter-header" style="margin-bottom:0.75rem;">
                <div class="chapter-number">Chapter 5 • Medical Section 27</div>
                <h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-crimson);">{page_title}</h3>
              </div>
              {rule_card}
              <div class="table-scroll-hint"><svg class="scroll-hint-icon" viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M3 12h18"/></svg>Scroll table horizontally to view full columns</div>
              <div class="astro-table-container">
                {tbl_clean}
              </div>
            </div>
            """
        else:
            c = orig_p['content']
            # Clean out raw scraped h4 title blocks that duplicated headers
            cb_m = re.search(r'<div class="content-block">(.*?)</div>', c, re.DOTALL)
            if cb_m:
                cb_txt = cb_m.group(1).strip()
                if not ('class="rule-card' in cb_txt or 'class="pillar' in cb_txt or '<p>' in cb_txt):
                    c = c.replace(cb_m.group(0), '')

            c = c.replace('तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)', 'Scroll table horizontally to view full columns')
            c = c.replace('तालिका को दाएं-बाएं स्क्रॉल करें (क्षैतिज दर्शन)', 'Scroll table horizontally to view full columns')
            c = c.replace('<span class="rule-badge">सूत्र / Rule</span>', '<span class="rule-badge">Classical Sutra</span>')
            c = c.replace('<span class="formula-pill">मंगल (Mars) के संपूर्ण कारकत्व और संकेतक</span>', '<span class="formula-pill">Mars (Mangala) Comprehensive Significations & Karakatvas</span>')
            c = re.sub(r'<h3 class="chapter-heading"[^>]*>.*?</h3>', f'<h3 class="chapter-heading" style="font-size:1.15rem; color:var(--accent-gold);">{page_title}</h3>', c)
            c = re.sub(r'<div class="table-caption">.*?</div>', '', c)

            # Localize tables inside
            tbl_match = re.search(r'<table.*?</table\s*>', c, re.DOTALL)
            if tbl_match:
                new_tbl = localize_html_table(tbl_match.group(0), idx, target_lang='english')
                c = c[:tbl_match.start()] + new_tbl + c[tbl_match.end():]

            content = c

        english_pages.append({
            "chapter": ch_name,
            "title": page_title,
            "content": content
        })

    # Page 88: Grand Back Cover (English Edition)
    p_last = """
    <div class="back-cover-inner">
      <div class="cover-ornament-corner top-left"></div>
      <div class="cover-ornament-corner top-right"></div>
      <div class="cover-ornament-corner bottom-left"></div>
      <div class="cover-ornament-corner bottom-right"></div>

      <div class="cover-yantra" style="width:110px; height:110px; margin-bottom:0.35rem;">
        <img src="assets/yantra.svg" alt="Tantra Gyan Sacred Seal" width="110" height="110">
      </div>

      <div class="back-cover-title">Complete Vedic Astrology Compendium</div>
      <div class="back-cover-subtitle">Authoritative Classical Predictive Knowledge Base</div>

      <div class="invocation-shloka" style="margin: 0.75rem auto; max-width: 90%;">
        ॥ Asato Mā Sad-Gamaya | Tamaso Mā Jyotir-Gamaya | Mṛtyor-Mā'mṛtaṁ Gamaya ॥<br>
        ॥ Oṁ Pūrṇam-Adaḥ Pūrṇam-Idaṁ Pūrṇāt-Pūrṇam-Udacyate | Pūrṇasya Pūrṇam-Ādāya Pūrṇam-Evāvaśiṣyate ॥<br>
        ॥ Oṁ Śāntiḥ Śāntiḥ Śāntiḥ ॥
      </div>

      <div class="back-cover-colophon">
        <div style="font-weight:700; color:var(--accent-gold); font-size:0.95rem; margin-bottom:0.25rem;">Tantra Gyan Research Center (तंत्र ज्ञान शोध संस्थान)</div>
        <div style="color:var(--text-secondary); font-size:0.85rem;">Author & Vedic Astrologer: <strong>Astrologer Ashutosh Kumar Choubey</strong></div>
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
    """
    english_pages.append({
        "chapter": get_chapter_name(87, 'english'),
        "title": ENGLISH_TITLES[87],
        "content": p_last
    })

    return english_pages

# ------------------------------------------------------------------------------
# 8. HTML DOCUMENT SHELL GENERATOR
# ------------------------------------------------------------------------------

def render_edition_html(pages_list, edition_lang='hindi'):
    is_hindi = (edition_lang == 'hindi')
    doc_lang = "hi" if is_hindi else "en"
    doc_title = "वैदिक ज्योतिष महाग्रंथ सरलीकृत (सम्पूर्ण हिन्दी संस्करण)" if is_hindi else "Complete Vedic Astrology Compendium Simplified (English Edition)"
    
    brand_sub = "सम्पूर्ण हिन्दी संस्करण" if is_hindi else "Complete English Edition"
    search_placeholder = "ग्रंथ में खोजें (उदा. सूर्य, मंगल, गजकेसरी, पुष्य)..." if is_hindi else "Search compendium (e.g. Sun, Mars, Raja Yoga, Pushya)..."
    toc_label = "विषय-सूची" if is_hindi else "Contents"
    bookmark_label = "बुकमार्क" if is_hindi else "Bookmarks"
    theme_label = "भोजपत्र" if is_hindi else "Parchment"
    spread_label = "दो पृष्ठ" if is_hindi else "Two Pages"
    
    btn_first_title = "प्रारंभ" if is_hindi else "First"
    btn_prev_title = "पिछला" if is_hindi else "Prev"
    btn_next_title = "अगला" if is_hindi else "Next"
    btn_last_title = "अंतिम" if is_hindi else "Last"

    total_pages = len(pages_list)

    # Build TOC HTML (Grouped cleanly by Chapter)
    toc_items = []
    current_chapter = None
    for p_idx, p in enumerate(pages_list):
        ch_raw = p['chapter'].split('•')[0].strip()
        if ch_raw != current_chapter:
            current_chapter = ch_raw
            toc_items.append(f"""
            <div class="toc-chapter-header">
              <span class="toc-chapter-pill">📌 {current_chapter}</span>
            </div>
            """)
        toc_items.append(f"""
        <a href="#page-{p_idx+1}" class="toc-item" data-goto="{p_idx+1}">
          <div class="toc-item-left">
            <span class="toc-page-badge">P.{p_idx+1}</span>
            <span class="toc-item-title">{p['title']}</span>
          </div>
          <span class="toc-item-arrow">›</span>
        </a>
        """)
    toc_html = "\n".join(toc_items)

    # Build Raw Page Data Nodes
    pages_data_nodes = []
    for p_idx, p in enumerate(pages_list):
        pages_data_nodes.append(f"""
        <div class="book-page-data" id="page-data-{p_idx+1}" data-page="{p_idx+1}" data-chapter="{html.escape(p['chapter'])}" data-title="{html.escape(p['title'])}" style="display:none;">
          {p['content']}
        </div>
        """)
    all_pages_html = "\n".join(pages_data_nodes)

    ft_title = 'Complete Vedic Astrology Compendium Simplified' if not is_hindi else 'वैदिक ज्योतिष महाग्रंथ सरलीकृत'

    initial_left_html = ""
    initial_right_html = f"""
        <div class="page-body cover-page-wrapper">
          {pages_list[0]['content']}
        </div>
    """

    # Active button classes
    hi_btn_cls = "lang-btn active" if is_hindi else "lang-btn"
    en_btn_cls = "lang-btn active" if not is_hindi else "lang-btn"
    hi_opt_cls = "settings-opt-btn active" if is_hindi else "settings-opt-btn"
    en_opt_cls = "settings-opt-btn active" if not is_hindi else "settings-opt-btn"
    page_counter_initial = f"मुखपृष्ठ • Cover (१ / {total_pages})" if is_hindi else f"Cover • 1 / {total_pages}"

    settings_title = "सेटिंग्स और विकल्प" if is_hindi else "Settings & Options"
    settings_nav_title = "नेविगेशन और अध्ययन" if is_hindi else "Navigation & Reading"
    settings_toc_btn = "विषय-सूची" if is_hindi else "Contents"
    settings_bm_btn = "बुकमार्क" if is_hindi else "Bookmarks"
    settings_lang_title = "भाषा चयन" if is_hindi else "Language Mode"
    settings_appear_title = "पठन अनुभव" if is_hindi else "Appearance & Reading"
    settings_fs_btn = "फुलस्क्रीन: <strong id='settings-fs-label'>चालू करें</strong>" if is_hindi else "Fullscreen: <strong id='settings-fs-label'>Enter</strong>"
    settings_theme_btn = f"थीम: <strong id='settings-theme-label'>{theme_label}</strong>" if is_hindi else f"Theme: <strong id='settings-theme-label'>{theme_label}</strong>"
    settings_layout_btn = f"दृश्य: <strong id='settings-layout-label'>{spread_label}</strong>" if is_hindi else f"View: <strong id='settings-layout-label'>{spread_label}</strong>"
    settings_sound_btn = "ध्वनि: <strong id='settings-sound-label'>चालू</strong>" if is_hindi else "Sound: <strong id='settings-sound-label'>On</strong>"
    settings_font_label = "🔤 फॉन्ट आकार:" if is_hindi else "🔤 Font Size:"
    settings_links_title = "आधिकारिक संपर्क" if is_hindi else "Official Links"

    html_code = f"""<!DOCTYPE html>
<html lang="{doc_lang}" data-theme="parchment" data-lang-mode="{edition_lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>{doc_title}</title>
  
  <!-- SEO Best Practice Meta Tags -->
  <meta name="description" content="{doc_title} by Astrologer Ashutosh Kumar Choubey. Comprehensive authentic compendium covering Navagraha Karakatva, 17 Classical Raja Yogas, 27 Nakshatras & 108 Padas, Deeptadi Avasthas, and Planetary Predictions.">
  <meta name="keywords" content="Tantra Gyan, Vedic Astrology, Astrologer Ashutosh Kumar Choubey, Navagraha Karakatva, Raja Yoga, Medical Astrology, Cancer in Astrology, Nakshatra Padas, Jyotish Shastra, Parashara, Phaladeepika">
  <meta name="author" content="Ashutosh Kumar Choubey">
  <meta name="robots" content="index, follow">
  
  <!-- OpenGraph Metadata -->
  <meta property="og:title" content="{doc_title}">
  <meta property="og:description" content="Comprehensive Authentic Vedic Astrology Reference Book by Astrologer Ashutosh Kumar Choubey.">
  <meta property="og:type" content="book">
  <meta property="og:url" content="https://t.worldgyan.com">
  <link rel="canonical" href="https://t.worldgyan.com">
  
  <!-- Standard High-Quality Google Fonts for Vedic & Modern Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400&family=Inter:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&family=Noto+Serif+Devanagari:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
  
  <!-- Standard CSS Files -->
  <link rel="stylesheet" href="css/book.css?v=3.4">
  <link rel="stylesheet" href="css/tables.css?v=3.4">
</head>
<body>

  <!-- Floating Book App Header -->
  <header class="app-header">
    <div class="header-top-row">
      <a href="#page-1" class="brand-section" onclick="if(window.bookEngine) window.bookEngine.goToPage(1, true); return false;" title="तंत्र ज्ञान (Tantra Gyan) - Home">
        <div class="brand-logo">
          <img src="assets/yantra.svg" alt="Tantra Gyan Mandala" width="34" height="34">
        </div>
        <div class="brand-titles">
          <span class="brand-name">तंत्र ज्ञान शोध संस्थान <span>Tantra Gyan</span></span>
          <span class="brand-tagline">{brand_sub}</span>
        </div>
      </a>

      <!-- Mobile Header Actions (Gear Settings Icon) -->
      <div class="mobile-header-actions">
        <button class="tool-btn mobile-action-btn mobile-gear-btn" id="btn-settings-toggle" title="Settings & Options (सेटिंग्स और विकल्प)" aria-label="Open Settings">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;">
            <circle cx="12" cy="12" r="3"></circle>
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- Search Input Container with Dropdown Results -->
    <div class="search-box" id="search-box-container">
      <div class="search-input-wrapper">
        <span class="search-icon" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        </span>
        <input type="text" id="book-search" class="search-input" placeholder="{search_placeholder}" aria-label="Search Book" autocomplete="off">
        <button type="button" id="search-clear-btn" class="search-clear-btn" title="Clear search" aria-label="Clear search" style="display:none;">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <span id="search-counter" class="search-count" style="display:none;" title="Click to view all matching pages"></span>
      
      <!-- Live Search Results Dropdown -->
      <div id="search-dropdown" class="search-dropdown" style="display:none;" role="region" aria-label="Search Results">
        <div class="search-dropdown-header">
          <span id="search-dropdown-title" class="search-dropdown-title"> परिणाम (Search Results)</span>
          <button type="button" id="search-dropdown-close" class="search-dropdown-close" title="Close" aria-label="Close search">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </button>
        </div>
        <div id="search-results-list" class="search-results-list"></div>
      </div>
    </div>

    <!-- Toolbar Controls (Desktop Only - Hidden on Mobile) -->
    <div class="toolbar-controls desktop-tools">
      <!-- TOC Toggle Button -->
      <button class="tool-btn" id="btn-toc-toggle" title="{toc_label}">
        <span>📖</span> <span>{toc_label}</span>
      </button>

      <!-- Bookmark Button -->
      <button class="tool-btn" id="btn-bookmark-toggle" title="{bookmark_label}">
        <span>🔖</span> <span id="bookmark-btn-label">{bookmark_label}</span>
        <span id="bookmark-count-badge" class="badge-count" style="display:none;">0</span>
      </button>

      <!-- YouTube Channel Link (Sleek Compact Icon) -->
      <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="tool-btn yt-header-btn" title="YouTube: @TantraGyan108" aria-label="YouTube Channel @TantraGyan108" style="padding:0.42rem 0.58rem; color:#ef4444; border-color:rgba(239,68,68,0.4); text-decoration:none;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#ef4444" style="vertical-align:middle; display:inline-block;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
      </a>

      <!-- Language Mode Switcher -->
      <div class="lang-switcher" title="Switch Reading Language">
        <button class="{hi_btn_cls}" data-lang="hindi">हिंदी</button>
        <button class="{en_btn_cls}" data-lang="english">English</button>
        <button class="lang-btn" data-lang="bilingual">{ 'द्विभाषी' if is_hindi else 'Bilingual' }</button>
      </div>

      <!-- Theme Switcher -->
      <button class="tool-btn" id="btn-theme-toggle" title="{theme_label}">
        <span>📜</span> <span>{theme_label}</span>
      </button>

      <!-- Dual / Single Spread Toggle -->
      <button class="tool-btn" id="btn-layout-toggle" title="{spread_label}">
        <span>📖</span> <span>{spread_label}</span>
      </button>

      <!-- Sound Mute Toggle -->
      <button class="tool-btn" id="btn-sound-toggle" title="Sound Effect" style="padding:0.45rem 0.55rem;">
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
    <div class="book-container cover-closed-front">
      <!-- Decorative Gilded Corners -->
      <div class="corner-ornament corner-tl"></div>
      <div class="corner-ornament corner-tr"></div>
      <div class="corner-ornament corner-bl"></div>
      <div class="corner-ornament corner-br"></div>

      <!-- Silk Ribbon Bookmark -->
      <div class="silk-bookmark" title="Bookmark page"></div>

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

  <!-- Bottom Reading Controller Bar (Exact 2-Line Mobile Layout) -->
  <nav class="bottom-reading-bar" aria-label="Book Navigation Bar">
    <!-- Line 1: Slider spanning full width across top -->
    <div class="bottom-slider-row">
      <input type="range" id="page-slider" class="page-slider" min="1" max="{total_pages}" value="1" aria-label="Page Position">
    </div>

    <!-- Line 2: Single combined controls row: [«][‹]  [Counter Badge]  [›][»] -->
    <div class="bottom-controls-row">
      <div class="nav-group-left">
        <button class="tool-btn nav-edge-btn" id="btn-first-bottom" onclick="if(window.bookEngine) window.bookEngine.goToPage(1, true);" title="{ 'प्रथम पृष्ठ' if is_hindi else 'First Page' }" disabled>«<span class="nav-btn-text"> {btn_first_title}</span></button>
        <button class="tool-btn nav-step-btn" id="btn-prev-bottom" onclick="if(window.bookEngine) window.bookEngine.prevPage();" title="{ 'पिछला पृष्ठ' if is_hindi else 'Previous Page' }" disabled>‹<span class="nav-btn-text"> {btn_prev_title}</span></button>
      </div>

      <div class="bottom-counter-container">
        <span class="page-counter-badge" id="page-counter-badge">{page_counter_initial}</span>
      </div>

      <div class="nav-group-right">
        <button class="tool-btn nav-step-btn" id="btn-next-bottom" onclick="if(window.bookEngine) window.bookEngine.nextPage();" title="{ 'अगला पृष्ठ' if is_hindi else 'Next Page' }"><span class="nav-btn-text">{btn_next_title} </span>›</button>
        <button class="tool-btn nav-edge-btn" id="btn-last-bottom" onclick="if(window.bookEngine) window.bookEngine.goToPage({total_pages}, true);" title="{ 'अंतिम पृष्ठ' if is_hindi else 'Last Page' }"><span class="nav-btn-text">{btn_last_title} </span>»</button>
      </div>
    </div>
  </nav>

  <!-- Table of Contents Modal Drawer -->
  <div class="toc-overlay" id="toc-overlay" role="dialog" aria-modal="true" aria-labelledby="toc-modal-title">
    <div class="toc-modal">
      <div class="toc-header">
        <h3 class="toc-title" id="toc-modal-title">
          <span>📖</span> {toc_label}
        </h3>
        <button class="toc-close-btn" id="toc-close-btn" title="Close" aria-label="Close Table of Contents">
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
          <span>🔖</span> {bookmark_label}
        </h3>
        <button class="bookmark-close-btn" id="bookmark-close-btn" title="Close" aria-label="Close Bookmarks">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <div class="bookmark-action-bar">
        <button id="btn-bookmark-current" class="btn-bookmark-action">
          <span id="bookmark-current-icon">➕</span>
          <span id="bookmark-current-text">Bookmark Current Page</span>
        </button>
      </div>
      <div class="bookmark-body">
        <div id="bookmark-list" class="bookmark-list"></div>
      </div>
    </div>
  </div>

  <!-- Mobile Settings Drawer Modal (⚙️) -->
  <div class="settings-overlay" id="settings-overlay" role="dialog" aria-modal="true" aria-labelledby="settings-modal-title">
    <div class="settings-modal" id="settings-modal">
      <div class="settings-header">
        <h3 class="settings-title" id="settings-modal-title">
          <span>⚙️</span> {settings_title}
        </h3>
        <button class="settings-close-btn" id="settings-close-btn" title="Close" aria-label="Close Settings">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>

      <div class="settings-body">
        <!-- Section: Navigation & Highlights -->
        <div class="settings-section">
          <div class="settings-section-title">{settings_nav_title}</div>
          <div class="settings-grid">
            <button class="settings-action-btn" id="settings-btn-toc">
              <span class="settings-btn-icon">📖</span>
              <span class="settings-btn-label">{settings_toc_btn}</span>
            </button>
            <button class="settings-action-btn" id="settings-btn-bookmark">
              <span class="settings-btn-icon">🔖</span>
              <span class="settings-btn-label">{settings_bm_btn}</span>
              <span id="settings-bookmark-badge" class="badge-count" style="display:none;">0</span>
            </button>
          </div>
        </div>

        <!-- Section: Language Switcher -->
        <div class="settings-section">
          <div class="settings-section-title">{settings_lang_title}</div>
          <div class="settings-lang-row">
            <button class="{hi_opt_cls}" data-lang="hindi">हिंदी</button>
            <button class="{en_opt_cls}" data-lang="english">English</button>
            <button class="settings-opt-btn" data-lang="bilingual">{ 'द्विभाषी' if is_hindi else 'Bilingual' }</button>
          </div>
        </div>

        <!-- Section: Appearance & Reading -->
        <div class="settings-section">
          <div class="settings-section-title">{settings_appear_title}</div>
          <div class="settings-grid">
            <button class="settings-action-btn" id="settings-btn-fullscreen">
              <span class="settings-btn-icon">⛶</span>
              <span class="settings-btn-label">{settings_fs_btn}</span>
            </button>
            <button class="settings-action-btn" id="settings-btn-theme">
              <span class="settings-btn-icon">📜</span>
              <span class="settings-btn-label">{settings_theme_btn}</span>
            </button>
            <button class="settings-action-btn" id="settings-btn-layout">
              <span class="settings-btn-icon">📄</span>
              <span class="settings-btn-label">{settings_layout_btn}</span>
            </button>
            <button class="settings-action-btn" id="settings-btn-sound">
              <span class="settings-btn-icon">🔊</span>
              <span class="settings-btn-label">{settings_sound_btn}</span>
            </button>
            <div class="settings-font-row">
              <span class="settings-font-title">{settings_font_label}</span>
              <div class="font-zoom-group">
                <button class="font-zoom-btn" id="settings-font-dec" title="Decrease Font">A−</button>
                <button class="font-zoom-btn" id="settings-font-inc" title="Increase Font">A+</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Section: Official Links -->
        <div class="settings-section">
          <div class="settings-section-title">{settings_links_title}</div>
          <div class="settings-grid">
            <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="settings-action-btn" style="color:var(--accent-gold); text-decoration:none;">
              <span class="settings-btn-icon">🌐</span>
              <span class="settings-btn-label">t.worldgyan.com</span>
            </a>
            <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="settings-action-btn" style="color:#ef4444; text-decoration:none;">
              <span class="settings-btn-icon">▶</span>
              <span class="settings-btn-label">@TantraGyan108</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Floating Toast Notification -->
  <div id="book-toast" class="book-toast" role="status" aria-live="polite"></div>

  <!-- Raw Page Data Repository -->
  <div id="book-pages-store" style="display:none;" aria-hidden="true">
    {all_pages_html}
  </div>

  <!-- Scripts -->
  <script src="js/sound.js?v=3.4"></script>
  <script src="js/book-engine.js?v=3.4"></script>
  <script src="js/book-ui.js?v=3.4"></script>
</body>
</html>
"""
    return html_code

# ------------------------------------------------------------------------------
# 9. EXECUTION ENTRY POINT
# ------------------------------------------------------------------------------

def main():
    orig_pages = build_book.pages
    total_pages = len(orig_pages)
    print(f"Loaded {total_pages} pages from masterwork build_book...")

    # Build Pure Hindi Edition
    print("Generating pure Hindi edition (hindi.html)...")
    hindi_pages = generate_hindi_pages(orig_pages)
    hindi_html = render_edition_html(hindi_pages, edition_lang='hindi')
    hindi_file = "/Users/apple/Movies/ap/TantraGyan/hindi.html"
    with open(hindi_file, "w", encoding="utf-8") as f:
        f.write(hindi_html)
    print(f"Successfully generated {hindi_file} with {len(hindi_pages)} pure Hindi pages!")

    # Build Complete English Edition
    print("Generating complete English edition (english.html)...")
    english_pages = generate_english_pages(orig_pages)
    english_html = render_edition_html(english_pages, edition_lang='english')
    english_file = "/Users/apple/Movies/ap/TantraGyan/english.html"
    with open(english_file, "w", encoding="utf-8") as f:
        f.write(english_html)
    print(f"Successfully generated {english_file} with {len(english_pages)} complete English pages!")

if __name__ == "__main__":
    main()
