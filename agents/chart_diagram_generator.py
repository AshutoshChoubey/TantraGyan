"""
Chart Diagram Generator Agent (Google Antigravity SDK Pattern)
Generates high-contrast, mathematically precise SVG diagrams, North Indian Kundali charts,
and visual calculation maps for book chapters and digital reader.
"""

from typing import Dict, Any, List


class ChartDiagramGeneratorAgent:
    """Agent that creates crisp, responsive vector SVG diagrams and astrological charts."""

    def __init__(self):
        pass

    def generate_north_indian_kundali_svg(
        self,
        planets_by_house: Dict[int, List[str]],
        asc_sign: str = "Virgo (Kanya)",
        title: str = "जन्म कुण्डली (Janm Kundli D1)",
    ) -> str:
        """Generates a classical North Indian diamond birth chart in high-contrast vector SVG."""
        # 12 Houses coordinate map for North Indian Diamond Chart (width: 600, height: 600)
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%" class="vedic-diamond-chart" style="background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
  <defs>
    <linearGradient id="goldBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c89d3d" />
      <stop offset="50%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
    <radialGradient id="centerGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="rgba(16, 185, 129, 0.15)" />
      <stop offset="100%" stop-color="transparent" />
    </radialGradient>
  </defs>

  <!-- Background Aura -->
  <rect width="600" height="600" fill="#090d16" rx="12" />
  <circle cx="300" cy="300" r="240" fill="url(#centerGlow)" />

  <!-- Outer Border & Inner Diamond Lines -->
  <rect x="20" y="20" width="560" height="560" fill="none" stroke="url(#goldBorder)" stroke-width="2.5" />
  
  <!-- Diagonal X Lines -->
  <line x1="20" y1="20" x2="580" y2="580" stroke="#c89d3d" stroke-width="1.8" />
  <line x1="580" y1="20" x2="20" y2="580" stroke="#c89d3d" stroke-width="1.8" />
  
  <!-- Central Diamond Rhombus (Houses 1, 4, 7, 10 Kendras) -->
  <polygon points="300,20 580,300 300,580 20,300" fill="none" stroke="#10b981" stroke-width="2.2" />

  <!-- Header Banner -->
  <rect x="150" y="28" width="300" height="34" rx="6" fill="rgba(5, 150, 105, 0.3)" stroke="#10b981" stroke-width="1" />
  <text x="300" y="51" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">{title}</text>

  <!-- House Labels & Occupants -->
  <!-- House 1 (Top Center Diamond) -->
  <text x="300" y="110" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">1st House (Lagna)</text>
  <text x="300" y="135" fill="#34d399" font-size="12" text-anchor="middle">{asc_sign}</text>
  <text x="300" y="165" fill="#f8fafc" font-size="14" font-weight="600" text-anchor="middle">{" ".join(planets_by_house.get(1, ["—"]))}</text>

  <!-- House 2 (Top Left Triangle) -->
  <text x="160" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">2H</text>
  <text x="160" y="115" fill="#f8fafc" font-size="13" text-anchor="middle">{" ".join(planets_by_house.get(2, ["—"]))}</text>

  <!-- House 3 (Left Top Triangle) -->
  <text x="80" y="160" fill="#94a3b8" font-size="11" text-anchor="middle">3H</text>
  <text x="80" y="195" fill="#f8fafc" font-size="13" text-anchor="middle">{" ".join(planets_by_house.get(3, ["—"]))}</text>

  <!-- House 4 (Left Center Diamond) -->
  <text x="160" y="300" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">4th House (Sukha)</text>
  <text x="160" y="330" fill="#f8fafc" font-size="14" font-weight="600" text-anchor="middle">{" ".join(planets_by_house.get(4, ["—"]))}</text>

  <!-- House 5 (Left Bottom Triangle) -->
  <text x="80" y="440" fill="#94a3b8" font-size="11" text-anchor="middle">5H</text>
  <text x="80" y="475" fill="#f8fafc" font-size="13" text-anchor="middle">{" ".join(planets_by_house.get(5, ["—"]))}</text>

  <!-- House 6 (Bottom Left Triangle) -->
  <text x="160" y="520" fill="#94a3b8" font-size="11" text-anchor="middle">6H</text>
  <text x="160" y="545" fill="#f8fafc" font-size="13" text-anchor="middle">{" ".join(planets_by_house.get(6, ["—"]))}</text>

  <!-- House 7 (Bottom Center Diamond) -->
  <text x="300" y="450" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">7th House (Jaya / Kalatra)</text>
  <text x="300" y="480" fill="#f8fafc" font-size="14" font-weight="600" text-anchor="middle">{" ".join(planets_by_house.get(7, ["—"]))}</text>

  <!-- House 8 (Bottom Right Triangle) -->
  <text x="440" y="520" fill="#94a3b8" font-size="11" text-anchor="middle">8H</text>
  <text x="440" y="545" fill="#f8fafc" font-size="13" text-anchor="middle">{" ".join(planets_by_house.get(8, ["—"]))}</text>

  <!-- House 9 (Right Bottom Triangle) -->
  <text x="520" y="440" fill="#94a3b8" font-size="11" text-anchor="middle">9H</text>
  <text x="520" y="475" fill="#f8fafc" font-size="13" text-anchor="middle">{" ".join(planets_by_house.get(9, ["—"]))}</text>

  <!-- House 10 (Right Center Diamond) -->
  <text x="440" y="300" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">10th House (Karma)</text>
  <text x="440" y="330" fill="#f8fafc" font-size="14" font-weight="600" text-anchor="middle">{" ".join(planets_by_house.get(10, ["—"]))}</text>

  <!-- House 11 (Right Top Triangle) -->
  <text x="520" y="160" fill="#94a3b8" font-size="11" text-anchor="middle">11H</text>
  <text x="520" y="195" fill="#f8fafc" font-size="13" text-anchor="middle">{" ".join(planets_by_house.get(11, ["—"]))}</text>

  <!-- House 12 (Top Right Triangle) -->
  <text x="440" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">12H</text>
  <text x="440" y="115" fill="#f8fafc" font-size="13" text-anchor="middle">{" ".join(planets_by_house.get(12, ["—"]))}</text>

</svg>'''
        return svg

    def generate_panchanga_wheel_svg(self) -> str:
        """Generates a visual diagram showing the 5 limbs of time (Panchanga)."""
        svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 400" width="100%" height="100%" style="background:#090d16; border-radius:12px; font-family:'Noto Sans Devanagari', sans-serif;">
  <defs>
    <linearGradient id="panchangaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
  </defs>

  <rect width="700" height="400" fill="#090d16" rx="12" />
  
  <!-- Title -->
  <text x="350" y="40" fill="#f8fafc" font-size="18" font-weight="800" text-anchor="middle">पंचांग के पांच दिव्य अंग (The 5 Limbs of Cosmic Time)</text>
  <text x="350" y="65" fill="#94a3b8" font-size="13" text-anchor="middle">सूर्य और चंद्रमा के कोणीय संयोग से निर्मित काल-विज्ञान</text>

  <!-- 5 Limb Cards -->
  <!-- Limb 1: Tithi -->
  <rect x="30" y="100" width="115" height="240" rx="10" fill="#0f172a" stroke="#059669" stroke-width="1.5" />
  <circle cx="87" cy="140" r="22" fill="rgba(5, 150, 105, 0.2)" />
  <text x="87" y="146" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">१</text>
  <text x="87" y="185" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">तिथि</text>
  <text x="87" y="208" fill="#38bdf8" font-size="11" text-anchor="middle">चंद्र-सूर्य दूरी (12°)</text>
  <text x="87" y="240" fill="#cbd5e1" font-size="11.5" text-anchor="middle">संबंध एवं</text>
  <text x="87" y="258" fill="#cbd5e1" font-size="11.5" text-anchor="middle">समृद्धि का फल</text>
  <rect x="42" y="290" width="91" height="26" rx="4" fill="rgba(5, 150, 105, 0.3)" />
  <text x="87" y="307" fill="#6ee7b7" font-size="11" font-weight="600" text-anchor="middle">जल तत्व</text>

  <!-- Limb 2: Vaara -->
  <rect x="160" y="100" width="115" height="240" rx="10" fill="#0f172a" stroke="#c89d3d" stroke-width="1.5" />
  <circle cx="217" cy="140" r="22" fill="rgba(200, 157, 61, 0.2)" />
  <text x="217" y="146" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">२</text>
  <text x="217" y="185" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">वार</text>
  <text x="217" y="208" fill="#fbbf24" font-size="11" text-anchor="middle">सूर्योदय का दिन</text>
  <text x="217" y="240" fill="#cbd5e1" font-size="11.5" text-anchor="middle">शारीरिक ऊर्जा</text>
  <text x="217" y="258" fill="#cbd5e1" font-size="11.5" text-anchor="middle">एवं आयु का बल</text>
  <rect x="172" y="290" width="91" height="26" rx="4" fill="rgba(200, 157, 61, 0.3)" />
  <text x="217" y="307" fill="#fcd34d" font-size="11" font-weight="600" text-anchor="middle">अग्नि तत्व</text>

  <!-- Limb 3: Nakshatra -->
  <rect x="290" y="100" width="120" height="240" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
  <circle cx="350" cy="140" r="22" fill="rgba(2, 132, 199, 0.2)" />
  <text x="350" y="146" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">३</text>
  <text x="350" y="185" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">नक्षत्र</text>
  <text x="350" y="208" fill="#38bdf8" font-size="11" text-anchor="middle">चंद्रमा का घर (13°20')</text>
  <text x="350" y="240" fill="#cbd5e1" font-size="11.5" text-anchor="middle">चित्त की प्रकृति</text>
  <text x="350" y="258" fill="#cbd5e1" font-size="11.5" text-anchor="middle">एवं पूर्वजन्म संस्कार</text>
  <rect x="304" y="290" width="92" height="26" rx="4" fill="rgba(2, 132, 199, 0.3)" />
  <text x="350" y="307" fill="#7dd3fc" font-size="11" font-weight="600" text-anchor="middle">वायु तत्व</text>

  <!-- Limb 4: Yoga -->
  <rect x="425" y="100" width="115" height="240" rx="10" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5" />
  <circle cx="482" cy="140" r="22" fill="rgba(124, 58, 237, 0.2)" />
  <text x="482" y="146" fill="#c084fc" font-size="15" font-weight="700" text-anchor="middle">४</text>
  <text x="482" y="185" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">योग</text>
  <text x="482" y="208" fill="#c084fc" font-size="11" text-anchor="middle">सूर्य + चंद्र योग (13°20')</text>
  <text x="482" y="240" fill="#cbd5e1" font-size="11.5" text-anchor="middle">जीवन की आंतरिक</text>
  <text x="482" y="258" fill="#cbd5e1" font-size="11.5" text-anchor="middle">शांति एवं संयम</text>
  <rect x="437" y="290" width="91" height="26" rx="4" fill="rgba(124, 58, 237, 0.3)" />
  <text x="482" y="307" fill="#d8b4fe" font-size="11" font-weight="600" text-anchor="middle">आकाश तत्व</text>

  <!-- Limb 5: Karana -->
  <rect x="555" y="100" width="115" height="240" rx="10" fill="#0f172a" stroke="#ea580c" stroke-width="1.5" />
  <circle cx="612" cy="140" r="22" fill="rgba(234, 88, 12, 0.2)" />
  <text x="612" y="146" fill="#fb923c" font-size="15" font-weight="700" text-anchor="middle">५</text>
  <text x="612" y="185" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">करण</text>
  <text x="612" y="208" fill="#fb923c" font-size="11" text-anchor="middle">आधी तिथि (6°)</text>
  <text x="612" y="240" fill="#cbd5e1" font-size="11.5" text-anchor="middle">कार्य सिद्धि एवं</text>
  <text x="612" y="258" fill="#cbd5e1" font-size="11.5" text-anchor="middle">सफलता का सामर्थ्य</text>
  <rect x="567" y="290" width="91" height="26" rx="4" fill="rgba(234, 88, 12, 0.3)" />
  <text x="612" y="307" fill="#fed7aa" font-size="11" font-weight="600" text-anchor="middle">पृथ्वी तत्व</text>

</svg>'''
        return svg
