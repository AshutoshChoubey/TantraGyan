"""
Configuration and constants for Tantra Gyan Book Publishing Agents.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Any


@dataclass
class BookConfig:
    """Master configuration for the flagship book publishing system."""

    book_id: str = "kundali-ganita"
    flagship_volume: int = 4
    title_hi: str = "वैदिक कुण्डली विचार एवं गणित महाग्रंथ: खगोलीय सूत्र, 16 वर्ग चक्र एवं फलित संयोजन"
    title_en: str = "The Cosmic Algorithm: Vedic Horoscope Mathematics & Destiny Decoded"
    subtitle_hi: str = "स्विस एफेमेरिस, 120-वर्षीय विंशोत्तरी दशा, 337 अष्टकवर्ग बिंदु एवं 85 विवाह नियमों का सरलतम मानव व्याख्यान"
    author: str = "ज्योतिषाचार्य आशुतोष कुमार चौबे"
    tagline: str = "From Swiss Ephemeris & Astronomy to 120-Year Dashas, 337 Ashtakavarga Bindus, 85 Marriage Rules & 23 Life Verticals"

    # Color Palette Tokens
    theme_primary: str = "#059669"  # Royal Emerald Green (Mercury / Mathematics)
    theme_secondary: str = "#0284c7"  # Celestial Cyan (Jupiter / Wisdom)
    theme_gold: str = "#c89d3d"  # Vedic Gold
    theme_dark_bg: str = "#090d16"  # Deep Obsidian Black
    theme_parchment_bg: str = "#faf6ee"  # Classical Manuscript Ivory

    # Paths
    project_root: Path = field(default_factory=lambda: Path("/Users/apple/Movies/ap/TantraGyan"))
    formulas_source_dir: Path = field(
        default_factory=lambda: Path("/Users/apple/Movies/ap/vedic-astrology-kundali-studio/architecture_and_design/calculation_formulas_and_engines")
    )
    prompts_dir: Path = field(
        default_factory=lambda: Path("/Users/apple/Movies/ap/TantraGyan/prompts/kundali-ganita-vichar-book")
    )
    output_html_reader: str = "kundali-ganita-reader.html"
    output_html_web: str = "kundali-ganita.html"
    output_pdf_file: str = "kundali-ganita-vichar-mahagranth.pdf"

    # Reference Native Profile for Worked Examples
    reference_native: Dict[str, Any] = field(
        default_factory=lambda: {
            "name": "Ashutosh",
            "dob": "28 October 1994",
            "tob": "03:45:00 AM IST",
            "pob": "Garhwa, Jharkhand, India",
            "lat": 24.05,
            "lon": 83.65,
            "tz": 5.5,
            "jd": 2449653.427083,
            "ayanamsha": "23° 47' 11.8'' (Lahiri)",
            "lagna": "Virgo (Kanya) 09° 21' 10'' - Uttara Phalguni Pada 4",
            "moon_sign": "Cancer (Karka) 13° 10' 17'' - Pushya Pada 3",
        }
    )

    # Canva Integration Settings
    canva_folder_id: str = "FAHbySExszs"
    canva_brand_kit_id: str = "kAFsa11bjyE"


BOOK_META = {
    "title_hi": "वैदिक कुण्डली विचार एवं गणित महाग्रंथ: खगोलीय सूत्र, 16 वर्ग चक्र एवं फलित संयोजन",
    "title_en": "The Cosmic Algorithm: Vedic Horoscope Mathematics & Destiny Decoded",
    "author": "ज्योतिषाचार्य आशुतोष कुमार चौबे",
    "volume": 4
}

THEME_CONFIG = {
    "primary_emerald": "#059669",
    "accent_cyan": "#0284c7",
    "gold_accent": "#c89d3d",
    "bg_dark": "#090d16",
    "bg_parchment": "#faf6ee"
}

CHAPTER_ROSTER = [
    {"num": 1, "hi_title": "खगोलीय आधार एवं लग्न स्थिति गणित", "en_title": "Astronomical Ephemeris & House Cusps", "engine_file": "01_JANM_KUNDLI_EPHEMERIS_CALCULATIONS.md"},
    {"num": 2, "hi_title": "पंचांग रहस्य: काल के पांच दिव्य अंग", "en_title": "Panchanga & Solar Timings", "engine_file": "02_PANCHANGA_AND_SOLAR_TIMINGS.md"},
    {"num": 3, "hi_title": "विंशोत्तरी दशा: 120-वर्षीय जीवन चक्र", "en_title": "Vimshottari Dasha 120-Year Tree", "engine_file": "03_VIMSHOTTARI_DASHA_120_YEAR_TREE.md"},
    {"num": 4, "hi_title": "पराशरी महायोग एवं संसूचन मैट्रिक्स", "en_title": "Parashari Raja & Dhana Yogas", "engine_file": "04_PARASHARI_YOGAS_DETECTION_MATRICES.md"},
    {"num": 5, "hi_title": "अष्टकवर्ग विज्ञान: 337 बिंदु एवं शोधन", "en_title": "Ashtakavarga 337 Bindus & Reductions", "engine_file": "05_ASHTAKAVARGA_337_BINDUS_AND_REDUCTIONS.md"},
    {"num": 6, "hi_title": "16 वर्ग कुण्डलियाँ: D1 से D60 तक", "en_title": "16 Varga Divisional Charts (D1 to D60)", "engine_file": "06_VARGA_DIVISIONAL_CHARTS_SUITE_D1_TO_D60.md"},
    {"num": 7, "hi_title": "जैमिनी उपदेश सूत्र एवं भृगु नंदी नाड़ी", "en_title": "Jaimini Sutras & Bhrigu Nandi Nadi", "engine_file": "07_JAIMINI_UPADESHA_SUTRAS_AND_BNN_CORE.md"},
    {"num": 8, "hi_title": "गोचर वेधशाला एवं शनि साढ़े साती", "en_title": "Transit Observatory & Sade Sati", "engine_file": "08_TRANSIT_OBSERVATORY_GOCHAR_AND_SADE_SATI.md"},
    {"num": 9, "hi_title": "वैवाहिक फलित एवं 85-नियम पराशरी मैट्रिक्स", "en_title": "Marriage Engine & 85 Parashari Rules", "engine_file": "09_MARRIAGE_ENGINE_AND_85_RULE_PREDICTION.md"},
    {"num": 10, "hi_title": "कुण्डली मिलान: अष्टकूट 36 गुण एवं मेलापक", "en_title": "Kundli Milan & 36 Guna Ashtakoota", "engine_file": "10_KUNDLI_MILAN_ASHTAKOOT_36_GUNAS_AND_MASTER_SCORE.md"},
    {"num": 11, "hi_title": "23 जीवन क्षेत्र भविष्यफल इंजन", "en_title": "23 Predictive Life Domain Engines", "engine_file": "11_TWENTY_THREE_PREDICTIVE_DOMAIN_ENGINES.md"},
    {"num": 12, "hi_title": "अरिष्ट भंग एवं शुभ मुहूर्त संहिता", "en_title": "Misfortune Mitigation & Electional Muhurat", "engine_file": "12_MISFORTUNE_COMPENDIUM_AND_MUHURAT_ENGINES.md"},
    {"num": 13, "hi_title": "महा-संयोजन: सम्पूर्ण कुण्डली विवेचन गाइड", "en_title": "Grand Synthesis & Astrological Counseling", "engine_file": "00_MASTER_INDEX_AND_SYSTEM_PIPELINE.md"},
]

