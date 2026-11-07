"""
Enterprise North Indian Diamond SVG Visualizer
Renders authentic Parashara's Light & AstroSage diamond Kundali layouts.
Features:
- Dedicated royal header banner at the very top of the SVG (DOB, TOB, Place, Ayanamsha)
- Complete zero-overlap separation between metadata and House 1 (Lagna diamond)
- Rashi numbers positioned symmetrically at the crossing / intersection lines
- Exalted (Ex), Debilitated (Db), Retrograde (R), and Combustion (*) markers alongside degrees
- Intelligent vertical centering and spacing for multi-planet conjunctions
"""

from typing import Dict, List, Any, Tuple
from datetime import datetime
from .planet_icons import PLANET_ICONS_B64
from .constants import ZODIAC_NAMES

# Authentic Vedic Jyotish Planet Color Palette (Parashari Symbolism)
PLANET_PALETTE = {
    "Su": {"fill": "#c2410c", "name": "Saffron (Bhagwa)", "dot": "#ea580c"},
    "Mo": {"fill": "#475569", "name": "Pearl Gray (Chandra)", "dot": "#94a3b8"},
    "Ma": {"fill": "#dc2626", "name": "Fiery Red (Mangal)", "dot": "#ef4444"},
    "Me": {"fill": "#059669", "name": "Emerald Green (Budha)", "dot": "#10b981"},
    "Ju": {"fill": "#d97706", "name": "Golden Turmeric Yellow (Guru)", "dot": "#f59e0b"},
    "Ve": {"fill": "#be185d", "name": "Diamond Rose (Shukra)", "dot": "#f43f5e"},
    "Sa": {"fill": "#1d4ed8", "name": "Cosmic Blue (Shani)", "dot": "#3b82f6"},
    "Ra": {"fill": "#09090b", "name": "Shadow Black (Rahu)", "dot": "#27272a"},
    "Ke": {"fill": "#71717a", "name": "Smokey Ash (Ketu)", "dot": "#a1a1aa"},
    "Asc": {"fill": "#6b21a8", "name": "Regal Amethyst (Lagna)", "dot": "#a855f7"},
    "Ur": {"fill": "#65a30d", "name": "Chartreuse Yellow (Uranus)", "dot": "#84cc16"},
}

# Adjusted centroids for standard 400x400 viewBox
SAFE_HOUSE_COORDINATES_400 = {
    # Kendras (Diamonds - Spacious)
    1:  {"rashi": (200, 68),  "planets": (200, 108)},
    4:  {"rashi": (120, 200), "planets": (110, 200)},
    7:  {"rashi": (200, 332), "planets": (200, 292)},
    10: {"rashi": (280, 200), "planets": (290, 200)},

    # Triangles (Tighter clearance - pulled away from border apexes)
    2:  {"rashi": (105, 42),  "planets": (118, 72)},
    3:  {"rashi": (42, 105),  "planets": (72, 122)},
    5:  {"rashi": (42, 295),  "planets": (72, 278)},
    6:  {"rashi": (105, 358), "planets": (118, 328)},
    8:  {"rashi": (295, 358), "planets": (282, 328)},
    9:  {"rashi": (358, 295), "planets": (328, 278)},
    11: {"rashi": (358, 105), "planets": (328, 122)},
    12: {"rashi": (295, 42),  "planets": (282, 72)}
}

# Optimized safe centroids for 540x615 enterprise diamond chart:
# Chart frame X: 18..522 (width=504), Y: 95..595 (height=500), Center crossing: (270, 345)
SAFE_HOUSE_COORDINATES = {
    # Kendras (Diamonds - Spacious)
    1:  {"rashi": (270, 310), "planets": (270, 200), "r": (270, 310), "px": 270, "py": 200, "align": "middle"},
    4:  {"rashi": (232, 345), "planets": (144, 345), "r": (232, 345), "px": 144, "py": 345, "align": "middle"},
    7:  {"rashi": (270, 380), "planets": (270, 485), "r": (270, 380), "px": 270, "py": 485, "align": "middle"},
    10: {"rashi": (308, 345), "planets": (396, 345), "r": (308, 345), "px": 396, "py": 345, "align": "middle"},

    # Triangles (Tighter clearance - calibrated to exact geometric centroids safe zones)
    2:  {"rashi": (200, 122), "planets": (144, 146), "r": (200, 122), "px": 144, "py": 146, "align": "middle"},
    3:  {"rashi": (55, 275),  "planets": (75, 215),  "r": (55, 275),  "px": 75,  "py": 215,  "align": "middle"},
    5:  {"rashi": (55, 415),  "planets": (75, 475),  "r": (55, 415),  "px": 75,  "py": 475,  "align": "middle"},
    6:  {"rashi": (200, 568), "planets": (144, 538), "r": (200, 568), "px": 144, "py": 538, "align": "middle"},
    8:  {"rashi": (340, 568), "planets": (396, 538), "r": (340, 568), "px": 396, "py": 538, "align": "middle"},
    9:  {"rashi": (485, 415), "planets": (465, 475), "r": (485, 415), "px": 465, "py": 475, "align": "middle"},
    11: {"rashi": (485, 275), "planets": (465, 215), "r": (485, 275), "px": 465, "py": 215, "align": "middle"},
    12: {"rashi": (340, 122), "planets": (396, 146), "r": (340, 122), "px": 396, "py": 146, "align": "middle"},
}


def format_single_planet(p: Any, count: int = 1) -> str:
    """
    Formats an individual planet entry (dictionary or plain string) for compact SVG text embedding.
    Preserves authentic Vedic Jyotish palette colors, retrograde (R), dignity (Ex)/(Db), and combust (Asth).
    """
    if isinstance(p, str):
        return p
    if not isinstance(p, dict):
        return str(p)

    sym = p.get("symbol", "")
    is_retro = p.get("is_retrograde", False) and sym not in ["Ra", "Ke", "Asc"]
    d_code = p.get("dignity_code", "")
    is_combust = p.get("is_combust", False) or p.get("is_asth", False)

    badges = []
    if is_retro:
        badges.append('<tspan fill="#c2410c" font-weight="800" class="retro">(R)</tspan>')
    if d_code == "EXALTED":
        badges.append('<tspan fill="#047857" font-weight="800" class="exalted">(Ex)</tspan>')
    elif d_code == "DEBILITATED":
        badges.append('<tspan fill="#b91c1c" font-weight="800" class="debilitated">(Db)</tspan>')
    if is_combust:
        badges.append('<tspan fill="#dc2626" font-weight="800" class="combust">(Asth)</tspan>')
    badge_str = "".join(badges)

    dms = p.get("dms", "")
    if count >= 4:
        deg = dms.split("°")[0] + "°" if "°" in dms else (dms.split("'")[0] + "'" if "'" in dms else dms)
    elif count == 3:
        deg = dms.split("'")[0] + "'" if "'" in dms else (dms.split("°")[0] + "°" if "°" in dms else dms)
    else:
        deg = dms.split("'")[0] + "'" if "'" in dms else (dms.split("°")[0] + "°" if "°" in dms else dms)

    p_fill = PLANET_PALETTE.get(sym, {}).get("fill", "#1c1917")
    if deg:
        return f'<tspan fill="{p_fill}" font-weight="900">{sym}</tspan>{badge_str} <tspan fill="{p_fill}" font-weight="600" font-family="\'SF Mono\', monospace">{deg}</tspan>'
    return f'<tspan fill="{p_fill}" font-weight="900">{sym}</tspan>{badge_str}'


def format_house_planets_svg(planets_list: list, center_x: float, center_y: float) -> str:
    """
    Renders SVG text nodes with dynamic vertical stacking (1 planet per row, next row layout)
    and adaptive font scaling to guarantee planets never bleed over the diamond chart diagonal lines.
    - 1 planet: centered vertically, font-size: 11px
    - 2 planets: 2 separate rows (1 per row), font-size: 11px, dy: 14px
    - 3 planets: 3 separate rows (1 per row), font-size: 9.5px, dy: 12.5px
    - 4+ planets (Stelliums): 4+ separate rows (1 per row), font-size: 8.5px, dy: 11px
    """
    count = len(planets_list)
    if count == 0:
        return ""

    if count >= 4:
        font_size = "8.5px"
        line_height = 11.0
    elif count == 3:
        font_size = "9.5px"
        line_height = 12.5
    else:
        font_size = "11px"
        line_height = 14.0

    total_height = (count - 1) * line_height
    start_y_offset = -(total_height / 2.0)

    rows = [format_single_planet(p, count) for p in planets_list]

    svg_text = [
        f'<text xml:space="preserve" x="{center_x:.1f}" y="{(center_y + start_y_offset):.1f}" '
        f'text-anchor="middle" dominant-baseline="central" pointer-events="none" '
        f'style="font-size: {font_size}; font-weight: bold; fill: #1c1917; font-family: -apple-system, BlinkMacSystemFont, sans-serif;">'
    ]

    for idx, row_str in enumerate(rows):
        if idx == 0:
            svg_text.append(f'<tspan x="{center_x:.1f}">{row_str}</tspan>')
        else:
            svg_text.append(f'<tspan x="{center_x:.1f}" dy="{line_height:.1f}px">{row_str}</tspan>')

    svg_text.append('</text>')
    return "".join(svg_text)

def generate_diamond_chart_svg(
    house_occupants: Dict[int, List[Dict[str, Any]]],
    lagna_sign_idx: int,
    chart_title: str = "D1 • RASHI CHAKRA (LAGNA)",
    birth_meta: Dict[str, Any] = None,
    width: int = 540,
    height: int = 615
) -> str:
    """
    Renders pure vector SVG for North Indian Diamond Chart:
    - High-contrast black geometrical borders and diamond lines.
    - Dedicated Vedic Jyotish colors for each planet (Saffron Sun, Pearl Moon, Red Mars,
      Emerald Mercury, Golden Guru, Rose-Magenta Venus, Blue Saturn, Black Rahu, Smoke Ketu).
    - Dedicated royal header banner inside the SVG at Y: 10 to 88.
    - Fixed North Indian Diamond from Y: 95 to 595.
    - Rashi numbers positioned safely on the intersection crossing points.
    - Exalted (Ex), Debilitated (Db), Retrograde (R), Combust (Asth) tags.
    """
    if birth_meta is None:
        birth_meta = {
            "name": "Ashutosh Kumar Choubey",
            "dob": "1994-10-28",
            "tob": "03:45:00",
            "place": "Garhwa, Jharkhand, India",
            "ayanamsa": "Lahiri (Chitrapaksha)"
        }

    name_str = birth_meta.get("name") or "Ashutosh Kumar Choubey"
    dob_str = birth_meta.get("dob") or birth_meta.get("date", "--")
    tob_str = birth_meta.get("tob") or birth_meta.get("time", "--")
    place_str = birth_meta.get("place") or birth_meta.get("city_name", "Birth Location")
    ayanamsa_str = birth_meta.get("ayanamsa", "Lahiri (Chitrapaksha)")

    coords = SAFE_HOUSE_COORDINATES_400 if (width == 400 and height == 400) else SAFE_HOUSE_COORDINATES

    svg_parts = [
        f'<svg viewBox="0 0 {width} {height}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="select-none">',
        '  <defs>',
        '    <linearGradient id="parchmentBg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fffef9"/>',
        '      <stop offset="50%" stop-color="#fdfbf3"/>',
        '      <stop offset="100%" stop-color="#faf4e6"/>',
        '    </linearGradient>',
        '    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ffffff"/>',
        '      <stop offset="100%" stop-color="#fefcf6"/>',
        '    </linearGradient>',
        '    <filter id="subtleShadow" x="-3%" y="-3%" width="106%" height="106%">',
        '      <feDropShadow dx="1" dy="2" stdDeviation="3" flood-color="#78350f" flood-opacity="0.10"/>',
        '    </filter>',
        '    <!-- Embedded High-Resolution 3D Realistic Planet Icons -->',
    ]

    # Embed pre-compiled 48x48 Base64 3D planet icons into SVG <defs>
    for sym_key, b64_href in PLANET_ICONS_B64.items():
        svg_parts.append(f'    <image id="icon-{sym_key}" href="{b64_href}" width="14" height="14" preserveAspectRatio="xMidYMid meet"/>')

    svg_parts.extend([
        '  </defs>',
        '  <style>',
        '    @import url("https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700;800;900&amp;display=swap");',
        '    .header-box { fill: url(#headerGrad); stroke: #09090b; stroke-width: 1.8; filter: url(#subtleShadow); }',
        '    .header-inner { fill: none; stroke: #52525b; stroke-width: 0.8; stroke-dasharray: 4,2; }',
        '    .header-chart-type { font-size: 11px; font-weight: 800; fill: #09090b; font-family: "Noto Sans Devanagari", "Devanagari MT", "Kohinoor Devanagari", -apple-system, sans-serif; text-anchor: middle; }',
        '    .header-name { font-size: 14.5px; font-weight: 900; fill: #78350f; font-family: "Noto Sans Devanagari", "Devanagari MT", "Kohinoor Devanagari", -apple-system, sans-serif; text-anchor: middle; }',
        '    .header-meta { font-size: 10px; font-weight: 600; fill: #292524; font-family: "Noto Sans Devanagari", "Devanagari MT", "Kohinoor Devanagari", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; text-anchor: middle; }',
        '    .header-sub { font-size: 8.5px; font-weight: 500; fill: #71717a; font-family: "Noto Sans Devanagari", "Devanagari MT", "Kohinoor Devanagari", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; text-anchor: middle; }',
        '    .chart-bg { fill: url(#parchmentBg); filter: url(#subtleShadow); }',
        '    .chart-border { fill: none; stroke: #09090b; stroke-width: 2.6; }',
        '    .chart-inner-border { fill: none; stroke: #3f3f46; stroke-width: 1.0; stroke-dasharray: 4,2; }',
        '    .grid-line { fill: none; stroke: #09090b; stroke-width: 2.0; stroke-linejoin: round; }',
        '    .rashi-num { font-size: 13.5px; font-weight: 900; fill: #09090b; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; opacity: 0.98; paint-order: stroke fill; stroke: #fffdf7; stroke-width: 3.5px; stroke-linejoin: round; }',
        '    .planet-text { font-size: 12px; font-weight: 800; font-family: "Noto Sans Devanagari", "Devanagari MT", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }',
        '    .deg-text { font-size: 9.5px; fill: #52525b; font-weight: 500; font-family: "SF Mono", monospace; }',
        '    .exalted { fill: #047857; font-weight: 800; }',
        '    .debilitated { fill: #b91c1c; font-weight: 800; }',
        '    .retro { fill: #c2410c; font-weight: 800; }',
        '    .combust { fill: #dc2626; font-weight: 800; }',
        '    .center-cross-dot { fill: #09090b; }',
        '  </style>',

        # -------------------------------------------------------------
        # 1. DEDICATED ORNATE TOP HEADER BOX (DOB, TOB, Place, Ayanamsha)
        # -------------------------------------------------------------
        '  <!-- Top Header Box Above Diamond -->',
        '  <rect x="18" y="10" width="504" height="78" rx="8" class="header-box"/>',
        '  <rect x="22" y="14" width="496" height="70" rx="6" class="header-inner"/>',
        f'  <text x="{width//2}" y="28" class="header-chart-type">{chart_title}</text>',
        f'  <text x="{width//2}" y="47" class="header-name">{name_str}</text>',
        f'  <text x="{width//2}" y="65" class="header-meta">'
        f'DOB: <tspan fill="#881337" font-weight="700">{dob_str}</tspan>  |  '
        f'TOB: <tspan fill="#881337" font-weight="700">{tob_str}</tspan>  |  '
        f'Place: <tspan fill="#881337" font-weight="700">{place_str}</tspan>'
        f'</text>',
        f'  <text x="{width//2}" y="78" class="header-sub">'
        f'Ayanamsha: {ayanamsa_str}  •  System: Whole Sign (Equal Rasi-Bhava)'
        f'</text>',

        # -------------------------------------------------------------
        # 2. DIAMOND KUNDALI BODY (Y: 95 to 595)
        # -------------------------------------------------------------
        '  <!-- Diamond Kundali Outer Frame -->',
        '  <rect x="18" y="95" width="504" height="500" rx="8" class="chart-bg"/>',
        '  <rect x="18" y="95" width="504" height="500" rx="8" class="chart-border"/>',
        '  <rect x="23" y="100" width="494" height="490" rx="6" class="chart-inner-border"/>',

        '  <!-- Diagonal Crossing Lines -->',
        '  <line x1="18" y1="95" x2="522" y2="595" class="grid-line"/>',
        '  <line x1="522" y1="95" x2="18" y2="595" class="grid-line"/>',

        '  <!-- Inner Diamond Rhombus Connecting Midpoints -->',
        '  <polygon points="270,95 522,345 270,595 18,345" class="grid-line"/>',

        '  <!-- Center Crossing Accent Dot -->',
        '  <circle cx="270" cy="345" r="3" class="center-cross-dot"/>'
    ])

    # -------------------------------------------------------------
    # 3. RENDER RASHI NUMBERS & PLANETS FOR ALL 12 HOUSES
    # -------------------------------------------------------------
    for h in range(1, 13):
        # Classical Rashi number: (Lagna_sign + (h - 1)) % 12 + 1
        rashi_num = ((lagna_sign_idx + (h - 1)) % 12) + 1
        rx, ry = coords[h]["rashi"]
        px, py = coords[h]["planets"]

        # 1. House/Rashi Number
        svg_parts.append(f'  <text x="{rx}" y="{ry}" text-anchor="middle" class="rashi-num">{rashi_num}</text>')

        # 2. Render Occupying Planets: 1 Planet per Row (Vertical Next-Row Layout)
        planets = house_occupants.get(h, [])
        if planets:
            num_planets = len(planets)

            # Adaptive vertical line height, icon size, font sizes, and character width estimates
            if num_planets >= 4:
                line_height = 14.5
                icon_sz = 12
                icon_y_offset = -6.0
                sym_font_size = "11.5px"
                deg_font_size = "8.5px"
                char_w_sym = 6.8
                char_w_badge = 5.2
                char_w_deg = 5.0
            elif num_planets == 3:
                line_height = 17.0
                icon_sz = 13
                icon_y_offset = -6.5
                sym_font_size = "12.0px"
                deg_font_size = "9.0px"
                char_w_sym = 7.2
                char_w_badge = 5.5
                char_w_deg = 5.2
            else:  # 1 or 2 planets
                line_height = 20.0
                icon_sz = 14
                icon_y_offset = -7.0
                sym_font_size = "12.5px"
                deg_font_size = "9.5px"
                char_w_sym = 7.5
                char_w_badge = 5.8
                char_w_deg = 5.5

            total_block_h = (num_planets - 1) * line_height
            adjusted_py = py - (total_block_h / 2.0)

            for idx, p in enumerate(planets):
                y_pos = adjusted_py + (idx * line_height)

                # Parse dictionary or plain string
                if isinstance(p, dict):
                    sym = p.get("symbol", "")
                    dms = p.get("dms", "")
                    is_retro = p.get("is_retrograde", False) and sym not in ["Ra", "Ke", "Asc"]
                    d_code = p.get("dignity_code", "")
                    is_combust = p.get("is_combust", False) or p.get("is_asth", False)
                else:
                    p_str = str(p)
                    parts = p_str.split()
                    raw_sym = parts[0] if parts else ""
                    is_retro = "(R)" in p_str
                    d_code = "EXALTED" if "(Ex)" in p_str else ("DEBILITATED" if "(Db)" in p_str else "")
                    is_combust = "(Asth)" in p_str
                    sym = raw_sym.replace("(R)", "").replace("(Ex)", "").replace("(Db)", "").replace("(Asth)", "")
                    dms = parts[-1] if len(parts) > 1 else ""

                # Degree string: concise for dense houses to avoid horizontal overflow
                if num_planets >= 4:
                    deg_short = dms.split("°")[0] + "°" if "°" in dms else (dms.split("'")[0] + "'" if "'" in dms else dms)
                else:
                    deg_short = dms.split("'")[0] + "'" if "'" in dms else (dms.split("°")[0] + "°" if "°" in dms else dms)

                # Badges & Suffixes
                badges = []
                badge_chars = 0
                if is_retro:
                    badges.append('<tspan class="retro font-bold text-amber-700">(R)</tspan>')
                    badge_chars += 3
                if d_code == "EXALTED":
                    badges.append('<tspan class="exalted font-bold text-emerald-700">(Ex)</tspan>')
                    badge_chars += 4
                elif d_code == "DEBILITATED":
                    badges.append('<tspan class="debilitated font-bold text-rose-700">(Db)</tspan>')
                    badge_chars += 4
                if is_combust:
                    badges.append('<tspan class="combust font-bold text-red-600">(Asth)</tspan>')
                    badge_chars += 6

                badge_str = "".join(badges)

                # Fetch dedicated Vedic Jyotish color for each planet
                planet_cfg = PLANET_PALETTE.get(sym, {"fill": "#09090b"})
                p_fill = planet_cfg.get("fill", "#09090b")

                # Horizontal positioning: center the composite (Icon + Planet Symbol + Badges + Degree) around anchor px
                sym_len = len(sym)
                deg_len = len(deg_short)
                text_width = (sym_len * char_w_sym) + (badge_chars * char_w_badge) + (deg_len * char_w_deg) + (3.0 if deg_short else 0.0)
                total_row_width = icon_sz + 3.5 + text_width
                start_x = px - (total_row_width / 2.0)
                icon_x = start_x
                icon_y = y_pos + icon_y_offset
                text_x = start_x + icon_sz + 3.5

                deg_tspan = f' <tspan fill="{p_fill}" font-weight="600" font-size="{deg_font_size}" font-family="\'SF Mono\', monospace">{deg_short}</tspan>' if deg_short else ""

                icon_b64 = PLANET_ICONS_B64.get(sym, "")
                if icon_b64:
                    img_element = f'<image href="{icon_b64}" x="{icon_x:.1f}" y="{icon_y:.1f}" width="{icon_sz}" height="{icon_sz}"/>'
                else:
                    img_element = f'<circle cx="{icon_x + icon_sz/2:.1f}" cy="{icon_y + icon_sz/2:.1f}" r="{icon_sz/2:.1f}" fill="{p_fill}"/>'

                svg_parts.append(
                    f'  <!-- House {h} Planet {sym}: Vertical Next-Row Placement -->'
                    f'  {img_element}'
                    f'  <text x="{text_x:.1f}" y="{y_pos:.1f}" text-anchor="start" dominant-baseline="central" pointer-events="none" class="planet-text">'
                    f'<tspan fill="{p_fill}" font-weight="900" font-size="{sym_font_size}">{sym}</tspan>{badge_str}'
                    f'{deg_tspan}'
                    f'</text>'
                )

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def generate_ashtakavarga_diamond_svg(
    sav_houses: Dict[int, int],
    bav: Dict[str, List[int]],
    lagna_sign_idx: int,
    birth_meta: Dict[str, Any] = None,
    chart_title: str = "SAV • ASHTAKAVARGA CHAKRA (337 BINDUS)",
    width: int = 540,
    height: int = 615
) -> str:
    """
    Renders pure vector SVG for North Indian Diamond Ashtakavarga Chart:
    - Fixed North Indian Diamond from Y: 95 to 595.
    - Rashi numbers at crossings (House 1 = Lagna Rashi).
    - In each house compartment (1-12):
      1. SAV Bindu score with color-coded classification:
         >= 30: Strong (Emerald / Vriddhi)
         28-29: Average (Amber / Sama)
         < 28: Delicate (Rose / Alpa)
      2. Detailed 7-Graha BAV breakdown points for that house:
         Su, Mo, Ma, Me, Ju, Ve, Sa points.
    - Top header box with Native Name, Total Bindus (337), Median (28), and Ayanamsha.
    """
    if birth_meta is None:
        birth_meta = {
            "name": "Ashutosh Kumar Choubey",
            "dob": "1994-10-28",
            "tob": "03:45:00",
            "place": "Garhwa, Jharkhand, India",
            "ayanamsa": "Lahiri (Chitrapaksha)"
        }

    name_str = birth_meta.get("name") or "Ashutosh Kumar Choubey"
    dob_str = birth_meta.get("dob") or birth_meta.get("date", "--")
    tob_str = birth_meta.get("tob") or birth_meta.get("time", "--")
    place_str = birth_meta.get("place") or birth_meta.get("city_name", "Birth Location")
    ayanamsa_str = birth_meta.get("ayanamsa", "Lahiri (Chitrapaksha)")

    total_sav = sum(sav_houses.values()) if sav_houses else 337
    h1_sav = sav_houses.get(1, 28)
    h7_sav = sav_houses.get(7, 28)

    house_anchors = {
        1:  {"r": (270, 310), "px": 270, "py": 200},
        2:  {"r": (200, 122), "px": 144, "py": 146},
        3:  {"r": (55, 275),  "px": 75,  "py": 215},
        4:  {"r": (232, 345), "px": 144, "py": 345},
        5:  {"r": (55, 415),  "px": 75,  "py": 475},
        6:  {"r": (200, 568), "px": 144, "py": 538},
        7:  {"r": (270, 380), "px": 270, "py": 485},
        8:  {"r": (340, 568), "px": 396, "py": 538},
        9:  {"r": (485, 415), "px": 465, "py": 475},
        10: {"r": (308, 345), "px": 396, "py": 345},
        11: {"r": (485, 275), "px": 465, "py": 215},
        12: {"r": (340, 122), "px": 396, "py": 146},
    }

    svg_parts = [
        f'<svg viewBox="0 0 {width} {height}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="select-none">',
        '  <defs>',
        '    <linearGradient id="savParchmentBg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#fffef9"/>',
        '      <stop offset="50%" stop-color="#fdfbf5"/>',
        '      <stop offset="100%" stop-color="#fbf6eb"/>',
        '    </linearGradient>',
        '    <linearGradient id="savHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ffffff"/>',
        '      <stop offset="100%" stop-color="#fefbf2"/>',
        '    </linearGradient>',
        '    <filter id="savShadow" x="-3%" y="-3%" width="106%" height="106%">',
        '      <feDropShadow dx="1" dy="2" stdDeviation="3" flood-color="#78350f" flood-opacity="0.10"/>',
        '    </filter>',
        '  </defs>',
        '  <style>',
        '    @import url("https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700;800;900&amp;display=swap");',
        '    .header-box { fill: url(#savHeaderGrad); stroke: #09090b; stroke-width: 1.8; filter: url(#savShadow); }',
        '    .header-inner { fill: none; stroke: #52525b; stroke-width: 0.8; stroke-dasharray: 4,2; }',
        '    .header-chart-type { font-size: 11px; font-weight: 800; fill: #09090b; font-family: "Noto Sans Devanagari", "Devanagari MT", "Kohinoor Devanagari", -apple-system, sans-serif; text-anchor: middle; }',
        '    .header-name { font-size: 14.5px; font-weight: 900; fill: #78350f; font-family: "Noto Sans Devanagari", "Devanagari MT", "Kohinoor Devanagari", -apple-system, sans-serif; text-anchor: middle; }',
        '    .header-meta { font-size: 10px; font-weight: 600; fill: #292524; font-family: "Noto Sans Devanagari", "Devanagari MT", "Kohinoor Devanagari", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; text-anchor: middle; }',
        '    .header-sub { font-size: 8.5px; font-weight: 500; fill: #71717a; font-family: "Noto Sans Devanagari", "Devanagari MT", "Kohinoor Devanagari", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; text-anchor: middle; }',
        '    .chart-bg { fill: url(#savParchmentBg); filter: url(#savShadow); }',
        '    .chart-border { fill: none; stroke: #09090b; stroke-width: 2.6; }',
        '    .chart-inner-border { fill: none; stroke: #3f3f46; stroke-width: 1.0; stroke-dasharray: 4,2; }',
        '    .grid-line { fill: none; stroke: #09090b; stroke-width: 2.0; stroke-linejoin: round; }',
        '    .rashi-num { font-size: 13.5px; font-weight: 900; fill: #09090b; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; opacity: 0.98; paint-order: stroke fill; stroke: #fffdf7; stroke-width: 3.5px; stroke-linejoin: round; }',
        '    .center-cross-dot { fill: #09090b; }',
        '  </style>',

        '  <!-- Top Header Box Above Diamond -->',
        '  <rect x="18" y="10" width="504" height="78" rx="8" class="header-box"/>',
        '  <rect x="22" y="14" width="496" height="70" rx="6" class="header-inner"/>',
        f'  <text x="{width//2}" y="28" class="header-chart-type">{chart_title}</text>',
        f'  <text x="{width//2}" y="47" class="header-name">{name_str}</text>',
        f'  <text x="{width//2}" y="65" class="header-meta">'
        f'Total Bindus: <tspan fill="#065f46" font-weight="800">{total_sav}</tspan>  |  '
        f'H1 Vitality: <tspan fill="#881337" font-weight="700">{h1_sav}</tspan>  |  '
        f'H7 Marriage: <tspan fill="#881337" font-weight="700">{h7_sav}</tspan>  |  '
        f'Median: <tspan fill="#881337" font-weight="700">28/House</tspan>'
        f'</text>',
        f'  <text x="{width//2}" y="78" class="header-sub">'
        f'Ayanamsha: {ayanamsa_str}  •  Framework: BPHS 337-Bindu Nirayana'
        f'</text>',

        '  <!-- Diamond Kundali Outer Frame -->',
        '  <rect x="18" y="95" width="504" height="500" rx="8" class="chart-bg"/>',
        '  <rect x="18" y="95" width="504" height="500" rx="8" class="chart-border"/>',
        '  <rect x="23" y="100" width="494" height="490" rx="6" class="chart-inner-border"/>',

        '  <!-- Diagonal Crossing Lines -->',
        '  <line x1="18" y1="95" x2="522" y2="595" class="grid-line"/>',
        '  <line x1="522" y1="95" x2="18" y2="595" class="grid-line"/>',

        '  <!-- Inner Diamond Rhombus Connecting Midpoints -->',
        '  <polygon points="270,95 522,345 270,595 18,345" class="grid-line"/>',

        '  <!-- Center Crossing Accent Dot -->',
        '  <circle cx="270" cy="345" r="3" class="center-cross-dot"/>'
    ]

    for h in range(1, 13):
        anchor = house_anchors[h]
        rashi_num = ((lagna_sign_idx + (h - 1)) % 12) + 1
        rx, ry = anchor["r"]
        svg_parts.append(f'  <text x="{rx}" y="{ry}" text-anchor="middle" class="rashi-num">{rashi_num}</text>')

        px = anchor["px"]
        py = anchor["py"]
        points = sav_houses.get(h, 28)

        if points >= 30:
            status_text = "STRONG"
            score_color = "#047857"
            badge_bg = "#ecfdf5"
            badge_border = "#10b981"
            badge_text = "#065f46"
        elif points >= 28:
            status_text = "AVERAGE"
            score_color = "#b45309"
            badge_bg = "#fffbeb"
            badge_border = "#f59e0b"
            badge_text = "#78350f"
        else:
            status_text = "DELICATE"
            score_color = "#be123c"
            badge_bg = "#fff1f2"
            badge_border = "#f43f5e"
            badge_text = "#881337"

        # Sign index for house h
        s_idx = (lagna_sign_idx + h - 1) % 12
        su = bav.get("Su", [0]*12)[s_idx] if bav else 0
        mo = bav.get("Mo", [0]*12)[s_idx] if bav else 0
        ma = bav.get("Ma", [0]*12)[s_idx] if bav else 0
        me = bav.get("Me", [0]*12)[s_idx] if bav else 0
        ju = bav.get("Ju", [0]*12)[s_idx] if bav else 0
        ve = bav.get("Ve", [0]*12)[s_idx] if bav else 0
        sa = bav.get("Sa", [0]*12)[s_idx] if bav else 0

        # Score badge container and planet breakdown
        svg_parts.append(f'  <!-- House {h} Ashtakavarga SAV & BAV points -->')
        svg_parts.append(f'  <rect x="{px - 38}" y="{py - 24}" width="76" height="26" rx="6" fill="{badge_bg}" stroke="{badge_border}" stroke-width="1.2"/>')
        svg_parts.append(f'  <text x="{px}" y="{py - 5}" text-anchor="middle" font-size="19px" font-weight="900" fill="{score_color}" font-family="\'Cinzel\', \'Georgia\', serif">{points}</text>')
        svg_parts.append(f'  <text x="{px}" y="{py + 8}" text-anchor="middle" font-size="8.5px" font-weight="800" fill="{badge_text}" font-family="-apple-system, sans-serif" letter-spacing="0.4px">SAV • {status_text}</text>')
        svg_parts.append(f'  <text x="{px}" y="{py + 21}" text-anchor="middle" font-size="8px" font-weight="700" fill="#334155" font-family="\'SF Mono\', monospace">Su:{su} Mo:{mo} Ma:{ma} Me:{me}</text>')
        svg_parts.append(f'  <text x="{px}" y="{py + 31}" text-anchor="middle" font-size="8px" font-weight="700" fill="#334155" font-family="\'SF Mono\', monospace">Ju:{ju} Ve:{ve} Sa:{sa}</text>')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def generate_gochar_diamond_svg(
    transit_table: List[Dict[str, Any]],
    lagna_sign_idx: int,
    birth_meta: Dict[str, Any] = None,
    chart_title: str = "GOCHAR • REAL-TIME TRANSIT CHAKRA (ON NATAL LAGNA)",
    width: int = 540,
    height: int = 615
) -> str:
    """
    Renders pure vector SVG for North Indian Diamond Gochar (Real-Time Transit) Chart:
    - Lagna of the chart is the native's NATAL LAGNA (House 1 = Natal Lagna Rashi).
    - Occupants in each house (1-12) are the REAL-TIME TRANSIT PLANETS (Gochar planets).
    - Each transit planet has its 3D planet icon, classical Jyotish color, retrograde marker,
      transit degree, and dignity.
    - Top header box displays Real-Time Transit Timestamp, Native Name, and Natal Lagna.
    """
    if birth_meta is None:
        birth_meta = {
            "name": "Ashutosh Kumar Choubey",
            "place": "Current Observatory",
            "ayanamsa": "Lahiri (Chitrapaksha)"
        }

    if isinstance(transit_table, dict):
        transit_table = transit_table.get("transit_planets", [])
    elif not isinstance(transit_table, list):
        transit_table = []

    # Group transit planets by house_from_lagna (1 to 12)
    house_occupants: Dict[int, List[Dict[str, Any]]] = {h: [] for h in range(1, 13)}
    for p in transit_table:
        h = p.get("house_from_lagna", 1)
        if 1 <= h <= 12:
            d_code = ""
            dig = p.get("dignity", "").upper()
            if "EXALT" in dig:
                d_code = "EXALTED"
            elif "DEBIL" in dig:
                d_code = "DEBILITATED"

            house_occupants[h].append({
                "symbol": p["symbol"],
                "dms": p.get("degree_dms", ""),
                "is_retrograde": p.get("is_retrograde", False),
                "dignity_code": d_code,
                "is_combust": False
            })

    lagna_name = ZODIAC_NAMES[lagna_sign_idx] if 0 <= lagna_sign_idx < 12 else "Lagna"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    gochar_meta = {
        "name": birth_meta.get("name") or "Ashutosh Kumar Choubey",
        "dob": f"Live Gochar: {now_str}",
        "tob": "Current UT/IST",
        "place": f"Natal Lagna: {lagna_name} ({lagna_sign_idx + 1})",
        "ayanamsa": birth_meta.get("ayanamsa", "Lahiri (Chitrapaksha)")
    }

    return generate_diamond_chart_svg(
        house_occupants=house_occupants,
        lagna_sign_idx=lagna_sign_idx,
        chart_title=chart_title,
        birth_meta=gochar_meta,
        width=width,
        height=height
    )

