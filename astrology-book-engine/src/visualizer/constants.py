"""
Classical Vedic Jyotish Constants
"""

ZODIAC_SIGNS = [
    {"index": 0, "name": "Aries", "sanskrit": "Mesha", "symbol": "Ari", "lord": "Ma", "element": "Fire"},
    {"index": 1, "name": "Taurus", "sanskrit": "Vrishabha", "symbol": "Tau", "lord": "Ve", "element": "Earth"},
    {"index": 2, "name": "Gemini", "sanskrit": "Mithuna", "symbol": "Gem", "lord": "Me", "element": "Air"},
    {"index": 3, "name": "Cancer", "sanskrit": "Karkata", "symbol": "Can", "lord": "Mo", "element": "Water"},
    {"index": 4, "name": "Leo", "sanskrit": "Simha", "symbol": "Leo", "lord": "Su", "element": "Fire"},
    {"index": 5, "name": "Virgo", "sanskrit": "Kanya", "symbol": "Vir", "lord": "Me", "element": "Earth"},
    {"index": 6, "name": "Libra", "sanskrit": "Tula", "symbol": "Lib", "lord": "Ve", "element": "Air"},
    {"index": 7, "name": "Scorpio", "sanskrit": "Vrischika", "symbol": "Sco", "lord": "Ma", "element": "Water"},
    {"index": 8, "name": "Sagittarius", "sanskrit": "Dhanus", "symbol": "Sag", "lord": "Ju", "element": "Fire"},
    {"index": 9, "name": "Capricorn", "sanskrit": "Makara", "symbol": "Cap", "lord": "Sa", "element": "Earth"},
    {"index": 10, "name": "Aquarius", "sanskrit": "Kumbha", "symbol": "Aqu", "lord": "Sa", "element": "Air"},
    {"index": 11, "name": "Pisces", "sanskrit": "Meena", "symbol": "Pis", "lord": "Ju", "element": "Water"}
]

ZODIAC_NAMES = [z["name"] for z in ZODIAC_SIGNS]
ZODIAC_SANSKRIT = [z["sanskrit"] for z in ZODIAC_SIGNS]
SIGN_LORDS = [z["lord"] for z in ZODIAC_SIGNS]
