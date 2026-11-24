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
