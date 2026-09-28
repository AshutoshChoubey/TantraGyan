#!/usr/bin/env python3
"""
Tantra Gyan Multilingual Edition Builder
Generates:
1. hindi.html  - Pure Hindi Edition (सम्पूर्ण हिन्दी संस्करण)
2. english.html - Pure English Edition (Complete English Edition)
While preserving index.html as the original bilingual (द्विभाषी) edition.
"""

import re
import html
import os
import build_book

# ------------------------------------------------------------------------------
# 1. TABLE HEADER LOCALIZATION DICTIONARIES
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
    'गुण (Guna / Quality)': 'गुण (सत्व/रज/तम)',
    'ग्रंथ (Text)': 'शास्त्रीय ग्रंथ',
    'चन्द्र का संकेतक/कारकत्व (Moon’s Karakatva)': 'चन्द्रमा का कारकत्व',
    'चन्द्र का संकेतक/कारकत्व (Moon’s Significations)': 'चन्द्रमा का कारकत्व',
    'चन्द्र के संदर्भ (Key Mentions)': 'चन्द्रमा के शास्त्रीय संदर्भ',
    'तत्व (Tatva / Element)': 'तत्व (अग्नि/पृथ्वी/वायु/जल)',
    'देवता': 'अधिष्ठाता देवता',
    'ध्रुव (Polarity)': 'ध्रुवता (धनात्मक/ऋणात्मक)',
    'नक्षत्र (हिंदी)': 'नक्षत्र नाम',
    'नक्षत्र स्वामी (ग्रह)': 'नक्षत्र स्वामी (ग्रह)',
    'प्रतीक': 'प्रतीक चिन्ह',
    'बीमारियाँ (Diseases)': 'रोग एवं स्वास्थ्य विकार',
    'बुध (हिंदी)': 'बुध विवरण',
    'भाव (Bhava)': 'भाव (स्थान)',
    'भाव का नाम (House Name)': 'भाव का नाम',
    'मंगल का संकेतक/कारकत्व (Mars’s Karakatva)': 'मंगल का कारकत्व',
    'मंगल के संदर्भ (Key Mentions)': 'मंगल के शास्त्रीय संदर्भ',
    'मुख्य शरीर के अंग (Primary Body Parts)': 'मुख्य शारीरिक अंग',
    'राशि (Rashi) - Sign': 'राशि',
    'राशियाँ (Rashiyan / Signs)': 'राशियां',
    'राशियाँ (Signs)': 'राशियां',
    'लग्न (Lagna)': 'लग्न भाव',
    'लिंग (Gender)': 'लिंग (स्त्री/पुरुष)',
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
    'हिन्दी संकेत': 'हिन्दी संकेत',
    '🌐 ग्रह (Planet)': 'ग्रह',
    '💡 याद करने की ट्रिक': 'स्मरण सूत्र (शास्त्रीय ट्रिक)',
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
    'Body Parts / Organs (शरीर के अंग / अंग तंत्र)': 'Body Parts & Anatomical Systems',
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
    'Diseases (रोग)': 'Associated Diseases & Afflictions',
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
    'विषय': 'Topic',
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
# 2. CONTENT LOCALIZATION ENGINES
# ------------------------------------------------------------------------------

def localize_html_table(table_html, target_lang='hindi'):
    """Replaces table headers and cell text according to target language."""
    mapping = hindi_headers if target_lang == 'hindi' else english_headers

    # Replace th contents
    def replace_th(m):
        full_tag = m.group(1)
        inner = m.group(2)
        clean_inner = re.sub(r'<[^>]+>', ' ', inner).strip()
        clean_inner = re.sub(r'\s+', ' ', clean_inner)
        new_text = mapping.get(clean_inner, inner)
        return f'<th{full_tag}>{new_text}</th>'

    res = re.sub(r'<th([^>]*)>(.*?)</th>', replace_th, table_html, flags=re.DOTALL)

    # Clean cells
    if target_lang == 'hindi':
        # Remove English in brackets like (Heart), (Right Eye), etc.
        def clean_td_hindi(m):
            tag = m.group(1)
            content = m.group(2)
            # Remove (English Words)
            cleaned = re.sub(r'\s*\([A-Za-z0-9\s,\.\-\/\’\']+\)', '', content)
            # Remove stray empty commas
            cleaned = re.sub(r',\s*,', ',', cleaned)
            cleaned = re.sub(r',\s*$', '', cleaned)
            return f'<td{tag}>{cleaned}</td>'
        res = re.sub(r'<td([^>]*)>(.*?)</td>', clean_td_hindi, res, flags=re.DOTALL)
    else:
        # English: convert bilingual cells like "हृदय (Heart)" to "Heart"
        def clean_td_english(m):
            tag = m.group(1)
            content = m.group(2)
            # Convert Dev + (English) to English
            cleaned = re.sub(r'[\u0900-\u097F\s\/]+\(([A-Za-z0-9\s,\.\-\/\’\']+)\)', r'\1', content)
            return f'<td{tag}>{cleaned}</td>'
        res = re.sub(r'<td([^>]*)>(.*?)</td>', clean_td_english, res, flags=re.DOTALL)

    return res

# ------------------------------------------------------------------------------
# 3. BUILD HINDI EDITION PAGES
# ------------------------------------------------------------------------------
def generate_hindi_pages(orig_pages):
    hindi_pages = []
    
    # Page 1: Pure Hindi Cover
    p1 = """
    <div class="cover-page-inner">
      <div class="cover-tag">प्रामाणिक वैदिक ज्योतिष महाग्रंथ • डिजिटल संस्करण २०२६ • सम्पूर्ण हिन्दी संस्करण</div>
      
      <div class="cover-yantra">
        <img src="assets/yantra.svg" alt="Sacred Sri Yantra Emblem" width="130" height="130" style="filter: drop-shadow(0 4px 15px rgba(200, 157, 61, 0.45));">
      </div>

      <h1 class="cover-title-hindi" style="font-size:2.2rem; margin-bottom:0.75rem;">तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ</h1>
      <h2 class="cover-title-english" style="font-size:1.05rem; color:var(--accent-gold); font-family:var(--font-heading); letter-spacing:0.04em;">सम्पूर्ण प्रामाणिक शास्त्रीय फलित ज्ञानकोश</h2>

      <div class="cover-divider"></div>

      <p class="cover-subtitle">
        <strong>नवग्रह कारकत्व, १७ शास्त्रीय राजयोग, २७ नक्षत्र व १०८ पद विश्लेषण, दीप्तादि ९ अवस्थाएं एवं १२ भाव-राशि फल।</strong><br>
        <span style="font-size:0.85rem; color:var(--text-muted); display:inline-block; margin-top:0.4rem;">
          बृहत् शास्त्रीय सूत्र, खगोल गणित एवं फलित सिद्धांतों का अद्वितीय संग्रह
        </span>
      </p>

      <div class="cover-author-block">
        <div class="cover-author-label">लेखक एवं ज्योतिषाचार्य</div>
        <div class="cover-author-name">ज्योतिषाचार्य आशुतोष कुमार चौबे</div>
        <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem; margin-top:0.75rem;">
          <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="contact-channel-badge" style="border-color:var(--accent-gold); color:var(--accent-gold) !important; font-weight:700;">
            <span class="contact-icon">🌐</span>
            <span>वेबसाइट: <strong>t.worldgyan.com</strong></span>
          </a>
          <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge" style="margin-top:0;">
            <span class="yt-play-icon">▶</span>
            <span>यूट्यूब मंच: <strong>@TantraGyan108</strong></span>
          </a>
        </div>
      </div>
    </div>
    """
    hindi_pages.append({
        "chapter": "मुखपृष्ठ",
        "title": "तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ",
        "content": p1
    })

    # Page 2: Author Profile (Pure Hindi)
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
        "chapter": "लेखक परिचय",
        "title": "ज्योतिषाचार्य आशुतोष कुमार चौबे",
        "content": p2
    })

    # Page 3: Study Guide (Pure Hindi)
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
        "chapter": "अध्ययन निर्देशिका",
        "title": "ग्रंथ की आधारभूत संरचना",
        "content": p3
    })

    # Page 4: Discipline & Disclaimer (Pure Hindi)
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
        "chapter": "आचार संहिता",
        "title": "अनुशासन व वैधानिक परामर्श",
        "content": p4
    })

    # Page 5: Table of Contents (Pure Hindi)
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
            <strong style="font-size:0.88rem;">प्रस्तावना, लेखक परिचय, अध्ययन निर्देशिका व आचार संहिता</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ १ - ५</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय २</span>
            <strong style="font-size:0.88rem;">नवग्रह कारकत्व एवं १७ शास्त्रीय राजयोग</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ६ - २०</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय ३</span>
            <strong style="font-size:0.88rem;">राशि, नक्षत्र, ग्रह गति एवं विंशोत्तरी महादशा चक्र</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ २१ - ३७</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय ४</span>
            <strong style="font-size:0.88rem;">भाव एवं राशियों में ग्रह (दीप्तादि ९ अवस्थाएं व सूर्य फल)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ३८ - ४७</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय ५</span>
            <strong style="font-size:0.88rem;">आयुर्वेद-ज्योतिष व स्वास्थ्य विश्लेषण (२७ तालिकाएं)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ४८ - ७४</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">अध्याय ६</span>
            <strong style="font-size:0.88rem;">नक्षत्रों का गहन पद एवं ग्रह विश्लेषण (११ तालिकाएं)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ७५ - ८५</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">समापन</span>
            <strong style="font-size:0.88rem;">समापन पृष्ठ, मंगल श्लोक व आधिकारिक संपर्क</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">पृष्ठ ८६</span>
        </div>
      </div>
    </div>
    """
    hindi_pages.append({
        "chapter": "अनुक्रमणिका",
        "title": "विषय-सूची (सम्पूर्ण हिन्दी)",
        "content": p5
    })

    # Pages 6 to 86: Transform tables and content to Pure Hindi
    for idx in range(5, len(orig_pages) - 1):
        p = orig_pages[idx]
        ch = p['chapter']
        # Localize chapter name
        ch_hi = ch.replace('Ch 2:', 'अध्याय २:').replace('Ch 3:', 'अध्याय ३:').replace('Ch 4:', 'अध्याय ४:').replace('Ch 5:', 'अध्याय ५:').replace('Ch 6:', 'अध्याय ६:')
        
        # Localize content: Section indicators and hints
        c = p['content']
        c = c.replace('तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)', 'तालिका को दाएं-बाएं स्क्रॉल करें (क्षैतिज दर्शन)')
        c = re.sub(r'Chapter (\d+) • Section (\d+)', r'अध्याय \1 • खण्ड \2', c)
        c = re.sub(r'Chapter (\d+) • Table (\d+)', r'अध्याय \1 • तालिका \2', c)
        c = re.sub(r'Chapter (\d+) • Medical Section (\d+)', r'अध्याय \1 • स्वास्थ्य खण्ड \2', c)
        c = re.sub(r'Chapter (\d+) • Pada Section (\d+)', r'अध्याय \1 • पद खण्ड \2', c)
        c = re.sub(r'Chapter (\d+) • Sun in Houses', r'अध्याय \1 • भावों में सूर्य', c)
        c = re.sub(r'Chapter (\d+) • Sun in Signs', r'अध्याय \1 • राशियों में सूर्य', c)
        
        # Localize table contents
        c = localize_html_table(c, target_lang='hindi')
        
        hindi_pages.append({
            "chapter": ch_hi,
            "title": p['title'],
            "content": c
        })

    # Page 87: Sacred Colophon (Pure Hindi)
    p_last = """
    <div class="cover-page-inner" style="border: 2px solid var(--accent-gold);">
      <div class="cover-tag">समापन पृष्ठ • उपनिषद् मंगल कामना</div>

      <div class="shloka-box" style="margin:1.5rem 0; width:100%;">
        <div class="shloka-sanskrit">
          ॐ असतो मा सद्गमय । तमसो मा ज्योतिर्गमय ।<br>
          मृत्योर्मा अमृतं गमय । ॐ शान्तिः शान्तिः शान्तिः ॥
        </div>
        <div class="shloka-meaning">
          "हे ईश्वर, हमें असत्य से सत्य की ओर, अंधकार से दिव्य प्रकाश की ओर, तथा नश्वरता से अमरता की ओर ले चलिए। तीनों तापों की शांति हो।"
        </div>
        <span class="shloka-source">बृहदारण्यकोपनिषद् (१.३.२८)</span>
      </div>

      <div style="max-width:500px; margin:1rem auto; font-size:0.88rem; line-height:1.6; color:var(--text-secondary);">
        <p>
          यह महाग्रंथ वैदिक ज्योतिष, खगोल गणित एवं शास्त्रीय सिद्धांतों का सारगर्भित संकलन है। 
          आशा है कि यह ग्रंथ सभी जिज्ञासुओं, शोधार्थियों एवं अभ्यासकर्ताओं के लिए एक विश्वसनीय मार्गदर्शक सिद्ध होगा।
        </p>
      </div>

      <div class="cover-author-block" style="margin-top:auto;">
        <div class="cover-author-label">तंत्र ज्ञान संस्थान • सर्वाधिकार सुरक्षित</div>
        <div class="cover-author-name">ज्योतिषाचार्य आशुतोष कुमार चौबे</div>
        <div class="cover-author-role">कॉपीराइट © २०२६. All rights reserved.</div>
        <div style="margin-top:0.85rem; display:flex; flex-direction:column; align-items:center; gap:0.6rem;">
          <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem;">
            <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="contact-channel-badge" style="border-color:var(--accent-gold); color:var(--accent-gold) !important; font-weight:700;">
              <span class="contact-icon">🌐</span>
              <span>वेबसाइट: <strong>t.worldgyan.com</strong></span>
            </a>
            <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge" style="margin-top:0;">
              <span class="yt-play-icon">▶</span>
              <span>यूट्यूब: <strong>@TantraGyan108</strong></span>
            </a>
          </div>
          <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.8rem; font-size:0.86rem; margin-top:0.25rem;">
            <a href="mailto:tantraresearchcenter@gmail.com" style="color:var(--text-secondary); text-decoration:none; font-weight:600;">✉️ tantraresearchcenter@gmail.com</a>
            <span style="color:var(--border-color);">•</span>
            <a href="tel:+919658476170" style="color:var(--text-secondary); text-decoration:none; font-weight:600;">📞 +91 9658476170</a>
          </div>
        </div>
      </div>
    </div>
    """
    hindi_pages.append({
        "chapter": "समापन",
        "title": "उपनिषद् मंगल कामना",
        "content": p_last
    })

    return hindi_pages


# ------------------------------------------------------------------------------
# 4. BUILD ENGLISH EDITION PAGES
# ------------------------------------------------------------------------------
def generate_english_pages(orig_pages):
    english_pages = []
    
    # Page 1: Complete English Cover
    p1 = """
    <div class="cover-page-inner">
      <div class="cover-tag">Authentic Vedic Astrology Compendium • Digital Edition 2026 • English Edition</div>
      
      <div class="cover-yantra">
        <img src="assets/yantra.svg" alt="Sacred Sri Yantra Emblem" width="130" height="130" style="filter: drop-shadow(0 4px 15px rgba(200, 157, 61, 0.45));">
      </div>

      <h1 class="cover-title-hindi" style="font-size:2.1rem; margin-bottom:0.75rem; font-family:var(--font-heading); color:var(--accent-gold);">Tantra Gyan: Complete Vedic Astrology Compendium</h1>
      <h2 class="cover-title-english" style="font-size:1.05rem; color:var(--text-heading); letter-spacing:0.04em;">Authoritative Classical Sutras, Astronomical Motion & Predictive Principles</h2>

      <div class="cover-divider"></div>

      <p class="cover-subtitle">
        <strong>Navagraha Karakatva, 17 Classical Raja Yogas, 27 Nakshatras & 108 Pada Analysis, 9 Deeptadi Avasthas, and Comprehensive House-Sign Interpretations.</strong><br>
        <span style="font-size:0.85rem; color:var(--text-muted); display:inline-block; margin-top:0.4rem;">
          A High-Density Master Reference for Modern Practitioners and Scholars
        </span>
      </p>

      <div class="cover-author-block">
        <div class="cover-author-label">Author & Astrologer</div>
        <div class="cover-author-name">Astrologer Ashutosh Kumar Choubey</div>
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
      </div>
    </div>
    """
    english_pages.append({
        "chapter": "Front Cover",
        "title": "Tantra Gyan: Vedic Astrology Compendium",
        "content": p1
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
        "chapter": "Author Profile",
        "title": "Astrologer Ashutosh Kumar Choubey",
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
        "chapter": "Study Guide",
        "title": "Reader's Study Guide & Architecture",
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
        "chapter": "Ethics & Disclaimer",
        "title": "Ethical Code & Legal Disclaimer",
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
            <strong style="font-size:0.88rem;">Preface, Author Profile, Study Guide & Ethical Code</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 1 - 5</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 2</span>
            <strong style="font-size:0.88rem;">Planetary Karakatva & 17 Classical Raja Yogas</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 6 - 20</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 3</span>
            <strong style="font-size:0.88rem;">Zodiac Signs, 27 Nakshatras & Vimshottari Mahadasha</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 21 - 37</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 4</span>
            <strong style="font-size:0.88rem;">Planetary States (9 Deeptadi Avasthas) & Solar Interpretations</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 38 - 47</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 5</span>
            <strong style="font-size:0.88rem;">Medical Astrology & Health Diagnostics (27 Complete Tables)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 48 - 74</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Chapter 6</span>
            <strong style="font-size:0.88rem;">Nakshatra Pada Analysis & Subtle Interpretations (11 Tables)</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Pages 75 - 85</span>
        </div>
        <div class="toc-notebook-row">
          <div>
            <span class="badge-chip badge-gold" style="font-size:0.7rem; margin-right:0.4rem;">Colophon</span>
            <strong style="font-size:0.88rem;">Sacred Benediction, Upanishad Shloka & Official Contact</strong>
          </div>
          <span style="font-family:var(--font-heading); color:var(--accent-gold); font-size:0.82rem; font-weight:700;">Page 86</span>
        </div>
      </div>
    </div>
    """
    english_pages.append({
        "chapter": "Table of Contents",
        "title": "Systematic Table of Contents",
        "content": p5
    })

    # Pages 6 to 86: Transform tables and content to English
    for idx in range(5, len(orig_pages) - 1):
        p = orig_pages[idx]
        ch = p['chapter']
        # Localize chapter name
        ch_en = ch.replace('Ch 2: नवग्रह कारकत्व व राजयोग', 'Ch 2: Planetary Karakatva & Raja Yogas') \
                  .replace('Ch 3: राशि, नक्षत्र एवं ग्रह गति', 'Ch 3: Signs, Nakshatras & Planetary Motion') \
                  .replace('Ch 4: भाव एवं राशियों में ग्रह', 'Ch 4: Planetary States & House Placements') \
                  .replace('Ch 5: मेडिकल व स्वास्थ्य ज्योतिष', 'Ch 5: Medical Astrology & Diagnostics') \
                  .replace('Ch 6: नक्षत्र पद व ग्रह विश्लेषण', 'Ch 6: Nakshatra Padas & Planetary Analysis')
        
        # Localize content: Section indicators and hints
        c = p['content']
        c = c.replace('तालिका को दाएं-बाएं स्क्रॉल करें (Scroll table horizontally)', 'Scroll table horizontally to view full columns')
        
        # Localize table contents
        c = localize_html_table(c, target_lang='english')
        
        english_pages.append({
            "chapter": ch_en,
            "title": p['title'],
            "content": c
        })

    # Page 87: Sacred Colophon (English)
    p_last = """
    <div class="cover-page-inner" style="border: 2px solid var(--accent-gold);">
      <div class="cover-tag">Sacred Colophon • Upanishadic Benediction</div>

      <div class="shloka-box" style="margin:1.5rem 0; width:100%;">
        <div class="shloka-sanskrit">
          Om Asato Ma Sadgamaya | Tamaso Ma Jyotirgamaya |<br>
          Mrityorma Amritam Gamaya | Om Shantih Shantih Shantih ||
        </div>
        <div class="shloka-meaning">
          "Lead me from falsehood to eternal truth, from darkness to cosmic radiant light, from mortality to spiritual immortality. Om Peace, Peace, Peace."
        </div>
        <span class="shloka-source">Brihadaranyaka Upanishad (1.3.28)</span>
      </div>

      <div style="max-width:500px; margin:1rem auto; font-size:0.88rem; line-height:1.6; color:var(--text-secondary);">
        <p>
          This monumental compendium synthesizes authoritative Vedic astronomy, mathematical precision, and classical predictive shastras.
          May this sacred work illuminate the path for all dedicated practitioners, researchers, and seekers of truth.
        </p>
      </div>

      <div class="cover-author-block" style="margin-top:auto;">
        <div class="cover-author-label">Tantra Gyan Sacred Publication</div>
        <div class="cover-author-name">Astrologer Ashutosh Kumar Choubey</div>
        <div class="cover-author-role">Copyright © 2026. All rights reserved.</div>
        <div style="margin-top:0.85rem; display:flex; flex-direction:column; align-items:center; gap:0.6rem;">
          <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.6rem;">
            <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="contact-channel-badge" style="border-color:var(--accent-gold); color:var(--accent-gold) !important; font-weight:700;">
              <span class="contact-icon">🌐</span>
              <span>Website: <strong>t.worldgyan.com</strong></span>
            </a>
            <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="youtube-channel-badge" style="margin-top:0;">
              <span class="yt-play-icon">▶</span>
              <span>YouTube: <strong>@TantraGyan108</strong></span>
            </a>
          </div>
          <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:0.8rem; font-size:0.86rem; margin-top:0.25rem;">
            <a href="mailto:tantraresearchcenter@gmail.com" style="color:var(--text-secondary); text-decoration:none; font-weight:600;">✉️ tantraresearchcenter@gmail.com</a>
            <span style="color:var(--border-color);">•</span>
            <a href="tel:+919658476170" style="color:var(--text-secondary); text-decoration:none; font-weight:600;">📞 +91 9658476170</a>
          </div>
        </div>
      </div>
    </div>
    """
    english_pages.append({
        "chapter": "Colophon",
        "title": "Sacred Benediction & Colophon",
        "content": p_last
    })

    return english_pages

# ------------------------------------------------------------------------------
# 5. HTML SHELL BUILDER
# ------------------------------------------------------------------------------
def render_edition_html(pages_list, edition_lang='hindi'):
    is_hindi = (edition_lang == 'hindi')
    doc_lang = "hi" if is_hindi else "en"
    doc_title = "तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ (सम्पूर्ण हिन्दी संस्करण)" if is_hindi else "Tantra Gyan: Complete Vedic Astrology Compendium (English Edition)"
    
    brand_sub = "सम्पूर्ण हिन्दी संस्करण" if is_hindi else "Complete English Edition"
    search_placeholder = "ग्रंथ में खोजें (उदा. सूर्य, मंगल, गजकेसरी, पुष्य)..." if is_hindi else "Search compendium (e.g. Sun, Mars, Raja Yoga, Pushya)..."
    toc_label = "विषय-सूची" if is_hindi else "Contents"
    bookmark_label = "बुकमार्क" if is_hindi else "Bookmarks"
    theme_label = "भोजपत्र" if is_hindi else "Parchment"
    spread_label = "दो पृष्ठ" if is_hindi else "Two Pages"
    
    btn_first_title = "प्रारंभ" if is_hindi else "First"
    btn_prev_title = "‹ पिछला" if is_hindi else "‹ Prev"
    btn_next_title = "अगला ›" if is_hindi else "Next ›"
    btn_last_title = "अंतिम" if is_hindi else "Last"

    total_pages = len(pages_list)

    # Build TOC HTML
    toc_items = []
    for p_idx, p in enumerate(pages_list):
        toc_items.append(f"""
        <a href="#page-{p_idx+1}" class="toc-item" data-goto="{p_idx+1}">
          <div class="toc-item-left">
            <span class="toc-chapter-badge">P.{p_idx+1}</span>
            <span class="toc-item-title">{p['title']}</span>
          </div>
          <span class="toc-page-num">{p['chapter'].split('•')[0].strip()}</span>
        </a>
        """)
    toc_html = "\n".join(toc_items)

    # Build Page Data Nodes
    pages_data_html = []
    for p_idx, p in enumerate(pages_list):
        pages_data_html.append(f"""
        <div class="book-page-data" id="page-data-{p_idx+1}" data-page="{p_idx+1}" data-chapter="{html.escape(p['chapter'])}" data-title="{html.escape(p['title'])}" style="display:none;">
          {p['content']}
        </div>
        """)
    all_pages_html = "\n".join(pages_data_html)

    # Active classes for lang buttons
    hi_active = ' active' if is_hindi else ''
    en_active = ' active' if not is_hindi else ''

    return f"""<!DOCTYPE html>
<html lang="{doc_lang}" data-theme="parchment" data-lang-mode="{edition_lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>{doc_title}</title>
  
  <meta name="description" content="{doc_title} by Astrologer Ashutosh Kumar Choubey. Comprehensive authentic Vedic astrology reference.">
  <meta name="keywords" content="Tantra Gyan, Vedic Astrology, Astrologer Ashutosh Kumar Choubey, Navagraha Karakatva, Raja Yoga, Medical Astrology, Cancer in Astrology, Nakshatra Padas, Jyotish Shastra">
  <meta name="author" content="Ashutosh Kumar Choubey">
  <meta name="robots" content="index, follow">
  
  <meta property="og:title" content="{doc_title}">
  <meta property="og:description" content="Comprehensive Authentic Vedic Astrology Reference Book by Astrologer Ashutosh Kumar Choubey.">
  <meta property="og:type" content="book">
  <meta property="og:url" content="https://t.worldgyan.com">
  <link rel="canonical" href="https://t.worldgyan.com">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400&family=Noto+Serif+Devanagari:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="css/book.css">
  <link rel="stylesheet" href="css/tables.css">
  
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Book",
    "name": "{doc_title}",
    "url": "https://t.worldgyan.com",
    "author": {{
      "@type": "Person",
      "name": "Ashutosh Kumar Choubey",
      "url": "https://t.worldgyan.com"
    }},
    "numberOfPages": {total_pages},
    "inLanguage": "{doc_lang}"
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
        <span class="brand-tagline">{brand_sub}</span>
      </div>
    </a>

    <!-- Toolbar Controls -->
    <div class="toolbar-controls">
      <!-- Search Input Container -->
      <div class="search-box" id="search-box-container">
        <span class="search-icon">🔍</span>
        <input type="text" id="book-search" class="search-input" placeholder="{search_placeholder}" aria-label="Search Book" autocomplete="off">
        <button type="button" id="search-clear-btn" class="search-clear-btn" title="Clear search" style="display:none;">✕</button>
        <span id="search-counter" class="search-count" title="Matching pages"></span>
        
        <div id="search-dropdown" class="search-dropdown" style="display:none;" role="region" aria-label="Search Results">
          <div class="search-dropdown-header">
            <span id="search-dropdown-title" class="search-dropdown-title">🔍 परिणाम (Search Results)</span>
            <button type="button" id="search-dropdown-close" class="search-dropdown-close" title="Close">✕</button>
          </div>
          <div id="search-results-list" class="search-results-list"></div>
        </div>
      </div>

      <!-- TOC Toggle Button -->
      <button class="tool-btn" id="btn-toc-toggle" title="Table of Contents">
        <span>📖</span> <span>{toc_label}</span>
      </button>

      <!-- Bookmark Button -->
      <button class="tool-btn" id="btn-bookmark-toggle" title="Saved Bookmarks">
        <span>🔖</span> <span id="bookmark-btn-label">{bookmark_label}</span>
        <span id="bookmark-count-badge" class="badge-count" style="display:none;">0</span>
      </button>

      <!-- Official Website Link -->
      <a href="https://t.worldgyan.com" target="_blank" rel="noopener" class="tool-btn website-header-btn" title="Website: t.worldgyan.com" style="color:var(--accent-gold); font-weight:700; border-color:rgba(200,157,61,0.4); text-decoration:none;">
        <span style="font-size:0.95rem;">🌐</span> <span>t.worldgyan.com</span>
      </a>

      <!-- YouTube Channel Link -->
      <a href="https://www.youtube.com/@TantraGyan108" target="_blank" rel="noopener" class="tool-btn yt-header-btn" title="YouTube: @TantraGyan108" style="color:#ef4444; font-weight:700; border-color:rgba(239,68,68,0.4); text-decoration:none;">
        <span style="font-size:0.95rem;">▶</span> <span>@TantraGyan108</span>
      </a>

      <!-- Language Mode Switcher -->
      <div class="lang-switcher" title="Switch Reading Language">
        <button class="lang-btn{hi_active}" data-lang="hindi">🇮🇳 हिंदी</button>
        <button class="lang-btn{en_active}" data-lang="english">🇬🇧 English</button>
        <button class="lang-btn" data-lang="bilingual">🌐 द्विभाषी</button>
      </div>

      <!-- Theme Switcher -->
      <button class="tool-btn" id="btn-theme-toggle" title="Toggle Theme">
        <span>📜</span> <span>{theme_label}</span>
      </button>

      <!-- Dual / Single Spread Toggle -->
      <button class="tool-btn" id="btn-layout-toggle" title="Toggle Spread Layout">
        <span>📖</span> <span>{spread_label}</span>
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
      <div class="corner-ornament corner-tl"></div>
      <div class="corner-ornament corner-tr"></div>
      <div class="corner-ornament corner-bl"></div>
      <div class="corner-ornament corner-br"></div>

      <div class="silk-bookmark" title="Click to bookmark this page"></div>
      <div class="book-spine-crease"></div>

      <button class="nav-arrow-btn nav-prev" id="btn-prev-page" title="Previous Page">‹</button>
      <button class="nav-arrow-btn nav-next" id="btn-next-page" title="Next Page">›</button>

      <div class="book-pages-wrapper">
        <section class="page-sheet left-page" id="left-page-container" aria-label="Left Page"></section>
        <section class="page-sheet right-page" id="right-page-container" aria-label="Right Page"></section>
      </div>
    </div>
  </main>

  <!-- Bottom Reading Controller Bar -->
  <nav class="bottom-reading-bar" aria-label="Book Navigation Bar">
    <div style="display:flex; align-items:center; gap:0.35rem;">
      <button class="tool-btn nav-edge-btn" onclick="if(window.bookEngine) window.bookEngine.goToPage(1, true);" title="First Page">⇤ {btn_first_title}</button>
      <button class="tool-btn nav-step-btn" id="btn-prev-bottom" onclick="if(window.bookEngine) window.bookEngine.prevPage();" title="Previous Page">{btn_prev_title}</button>
    </div>

    <div class="slider-container">
      <input type="range" id="page-slider" class="page-slider" min="1" max="{total_pages}" value="1" aria-label="Page Position">
      <span class="page-counter-badge" id="page-counter-badge">Page 1 of {total_pages}</span>
    </div>

    <div style="display:flex; align-items:center; gap:0.35rem;">
      <button class="tool-btn nav-step-btn" id="btn-next-bottom" onclick="if(window.bookEngine) window.bookEngine.nextPage();" title="Next Page">{btn_next_title}</button>
      <button class="tool-btn nav-edge-btn" onclick="if(window.bookEngine) window.bookEngine.goToPage({total_pages}, true);" title="Last Page">{btn_last_title} ⇥</button>
    </div>
  </nav>

  <!-- Table of Contents Modal Drawer -->
  <div class="toc-overlay" id="toc-overlay" role="dialog" aria-modal="true" aria-labelledby="toc-modal-title">
    <div class="toc-modal">
      <div class="toc-header">
        <h3 class="toc-title" id="toc-modal-title">
          <span>📖</span> {toc_label}
        </h3>
        <button type="button" class="toc-close-btn" id="toc-close-btn" title="Close">✕</button>
      </div>
      <div class="toc-body">
        <div class="toc-list" id="toc-list-items">
          {toc_html}
        </div>
      </div>
    </div>
  </div>

  <!-- Bookmarks Modal Overlay -->
  <div class="bookmark-overlay" id="bookmark-overlay" role="dialog" aria-modal="true" aria-labelledby="bookmark-modal-title">
    <div class="bookmark-modal" id="bookmark-modal">
      <div class="bookmark-header">
        <h3 class="bookmark-title" id="bookmark-modal-title">
          <span>🔖</span> {bookmark_label}
        </h3>
        <button type="button" class="bookmark-close-btn" id="bookmark-close-btn" title="Close">✕</button>
      </div>
      <div class="bookmark-action-bar">
        <button type="button" class="btn-bookmark-action" id="btn-bookmark-current">
          <span>★</span> <span>{'वर्तमान पृष्ठ सहेजें' if is_hindi else 'Bookmark Current Page'}</span>
        </button>
      </div>
      <div class="bookmark-body">
        <div id="bookmark-list" class="bookmark-list"></div>
      </div>
    </div>
  </div>

  <!-- Toast Notification Alert -->
  <div class="book-toast" id="book-toast" role="status" aria-live="polite"></div>

  <!-- Raw Page Data Repository -->
  <div class="book-pages-store" style="display:none;" aria-hidden="true">
    {all_pages_html}
  </div>

  <!-- Scripts -->
  <script src="js/sound.js"></script>
  <script src="js/book-engine.js"></script>
  <script src="js/book-ui.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      if (window.bookUI) {{
        window.bookUI.init();
      }}
    }});
  </script>
</body>
</html>
"""

# ------------------------------------------------------------------------------
# 6. EXECUTE COMPILATION
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    orig_pages = build_book.pages
    print(f"Loaded {len(orig_pages)} original bilingual pages.")

    # 1. Generate hindi.html
    print("Building pure Hindi edition (hindi.html)...")
    hindi_pages = generate_hindi_pages(orig_pages)
    hindi_html = render_edition_html(hindi_pages, edition_lang='hindi')
    hindi_file = "/Users/apple/Movies/ap/TantraGyan/hindi.html"
    with open(hindi_file, "w", encoding="utf-8") as f:
        f.write(hindi_html)
    print(f"Successfully generated {hindi_file} ({len(hindi_pages)} pages)!")

    # 2. Generate english.html
    print("Building pure English edition (english.html)...")
    english_pages = generate_english_pages(orig_pages)
    english_html = render_edition_html(english_pages, edition_lang='english')
    english_file = "/Users/apple/Movies/ap/TantraGyan/english.html"
    with open(english_file, "w", encoding="utf-8") as f:
        f.write(english_html)
    print(f"Successfully generated {english_file} ({len(english_pages)} pages)!")
