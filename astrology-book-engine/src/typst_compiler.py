#!/usr/bin/env python3
"""
Typst Publishing Compiler for Astrology Book Engine (Masterwork Edition)
========================================================================
Translates manuscript chapters into modern, academic-grade Typst markup
and compiles ultra-high resolution trade-paperback (A5 / 6x9in) vector PDFs.
Features:
- Authentic Vedic Jyotish color-coded planetary typography with 3D sphere icons
- Dedicated Full-Color Navagraha Reference Plate
- Royal ornamental framed title and dedication pages
- Proportional responsive tables with header accents and zero horizontal overflow
- Classical shloka, yoga, and sutra callout boxes
- Symmetrical chapter headers with decorative hairline rules
"""

import os
import re
import typst
import yaml

# Authentic Vedic Jyotish Planet Color Palette & 3D Icons for Typst
TYPST_PLANET_SPECS = [
    # (key, icon, pattern, text_color, bg_color, border_color)
    ('sun', 'sun.png', r'(?<![क-हअ-औ्])(?:सूर्य\s*\(\s*Sun\s*\)|सूर्यदेव|सूर्य|\bSun\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#c2410c")', 'rgb("#ffedd5")', 'rgb("#ea580c")'),
    ('moon', 'moon.png', r'(?<![क-हअ-औ्])(?:चन्द्र\s*\(\s*Moon\s*\)|चंद्र\s*\(\s*Moon\s*\)|चन्द्रमा|चंद्रमा|चन्द्र|चंद्र|\bMoon\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#334155")', 'rgb("#f1f5f9")', 'rgb("#94a3b8")'),
    ('mars', 'mars.png', r'(?<![क-हअ-औ्])(?:मंगल\s*\(\s*Mars\s*\)|मंगलदेव|मंगल|\bMars\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#dc2626")', 'rgb("#fee2e2")', 'rgb("#ef4444")'),
    ('mercury', 'mercury.png', r'(?<![क-हअ-औ्])(?:बुध\s*\(\s*Mercury\s*\)|बुधदेव|बुध|\bMercury\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#047857")', 'rgb("#d1fae5")', 'rgb("#10b981")'),
    ('jupiter', 'jupiter.png', r'(?<![क-हअ-औ्])(?:(?:गुरु\s*/\s*बृहस्पति|बृहस्पति|देवगुरु|गुरु(?!\s*जन))\s*\(\s*Jupiter\s*\)|बृहस्पति|देवगुरु|गुरु(?!\s*जन)|\bJupiter\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#b45309")', 'rgb("#fef3c7")', 'rgb("#f59e0b")'),
    ('venus', 'venus.png', r'(?<![क-हअ-औ्])(?:शुक्र\s*\(\s*Venus\s*\)|शुक्रदेव|शुक्र|\bVenus\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#be185d")', 'rgb("#fce7f3")', 'rgb("#f43f5e")'),
    ('saturn', 'saturn.png', r'(?<![क-हअ-औ्])(?:शनि\s*\(\s*Saturn\s*\)|शनिदेव|शनैश्चर|शनि|\bSaturn\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#1d4ed8")', 'rgb("#dbeafe")', 'rgb("#3b82f6")'),
    ('rahu', 'rahu.png', r'(?<![क-हअ-औ्])(?:राहु\s*\(\s*Rahu\s*\)|राहु|\bRahu\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#09090b")', 'rgb("#f4f4f5")', 'rgb("#27272a")'),
    ('ketu', 'ketu.png', r'(?<![क-हअ-औ्])(?:केतु\s*\(\s*Ketu\s*\)|केतु|\bKetu\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#52525b")', 'rgb("#f4f4f5")', 'rgb("#71717a")'),
]

TYPST_DIGNITY_RULES = [
    (r'(?<![क-हअ-औ्])उच्च(?![क-हअ-औ्ा-ौ])', 'rgb("#047857")', 'rgb("#d1fae5")', 'rgb("#10b981")'),
    (r'(?<![क-हअ-औ्])नीच(?![क-हअ-औ्ा-ौ])', 'rgb("#dc2626")', 'rgb("#fee2e2")', 'rgb("#ef4444")'),
    (r'(?<![क-हअ-औ्])मूलत्रिकोण(?![क-हअ-औ्ा-ौ])', 'rgb("#6b21a8")', 'rgb("#f3e8ff")', 'rgb("#c084fc")'),
    (r'(?<![क-हअ-औ्])स्वराशि(?![क-हअ-औ्ा-ौ])', 'rgb("#b45309")', 'rgb("#fef3c7")', 'rgb("#f59e0b")'),
]


def apply_typst_planet_colors(text):
    """Wraps matched planetary names in their signature Typst colored bold spans with 3D icons."""
    for key, icon, pat, text_col, bg_col, border_col in TYPST_PLANET_SPECS:
        text = re.sub(
            pat,
            lambda m, ic=icon, tc=text_col, bg=bg_col, bc=border_col: (
                f'#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: {bg}, stroke: 0.35pt + {bc})['
                f'#image("/assets/images/planets/{ic}", width: 7pt) #h(1pt)'
                f'#text(fill: {tc}, weight: "bold")[{m.group(0)}]'
                f']'
            ),
            text
        )
    for pat, text_col, bg_col, border_col in TYPST_DIGNITY_RULES:
        text = re.sub(
            pat,
            lambda m, tc=text_col, bg=bg_col, bc=border_col: (
                f'#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: {bg}, stroke: 0.35pt + {bc})['
                f'#text(fill: {tc}, weight: "bold", size: 0.85em)[{m.group(0)}]'
                f']'
            ),
            text
        )
    return text


def parse_markdown_table_to_typst(lines):
    """
    Converts a Markdown table into a Typst #table() with proportional columns,
    custom text scaling for dense tables, and authentic Jyotish palette styling.
    """
    rows = []
    for l in lines:
        if re.match(r'^\s*\|?\s*:?-+:?\s*\|', l):
            continue  # Separator line
        parts = [c.strip() for c in l.split('|')]
        if parts and parts[0] == '':
            parts.pop(0)
        if parts and parts[-1] == '':
            parts.pop(-1)
        if parts:
            rows.append(parts)

    if not rows:
        return ""

    num_cols = len(rows[0])

    # Dynamic proportional column sizing with generous room for explanation columns
    if num_cols == 7:
        cols_str = "(1.0fr, 1.5fr, 1.5fr, 1.2fr, 1.0fr, 1.0fr, 1.0fr)"
        text_size = "6.8pt"
        inset_str = "(x: 2.8pt, y: 3.5pt)"
    elif num_cols == 6:
        cols_str = "(0.8fr, 1.2fr, 1.2fr, 1.2fr, 1.4fr, 1.4fr)"
        text_size = "7.0pt"
        inset_str = "(x: 3.0pt, y: 4.0pt)"
    elif num_cols == 5:
        cols_str = "(0.9fr, 1.4fr, 1.6fr, 1.3fr, 1.8fr)"
        text_size = "7.2pt"
        inset_str = "(x: 3.2pt, y: 4.2pt)"
    elif num_cols == 4:
        cols_str = "(1.1fr, 1.3fr, 1.4fr, 3.2fr)"
        text_size = "7.5pt"
        inset_str = "(x: 3.8pt, y: 4.5pt)"
    elif num_cols == 3:
        cols_str = "(1.1fr, 1.4fr, 3.5fr)"
        text_size = "7.8pt"
        inset_str = "(x: 4.2pt, y: 5.0pt)"
    else:
        cols_str = f"{num_cols}"
        text_size = "7.8pt"
        inset_str = "(x: 4.5pt, y: 5.0pt)"

    cells = []
    for r_idx, row in enumerate(rows):
        for cell in row:
            cell_fmt = re.sub(r'\*\*(.*?)\*\*', r'#strong[\1]', cell)
            cell_fmt = re.sub(r'\*(.*?)\*', r'#emph[\1]', cell_fmt)
            cell_fmt = apply_typst_planet_colors(cell_fmt)

            if r_idx == 0:
                cells.append(f'[#text(weight: "bold", fill: rgb("#78350f"))[{cell_fmt}]]')
            else:
                cells.append(f'[{cell_fmt}]')

    return f"""
#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: {text_size})[
    #table(
      columns: {cols_str},
      fill: (x, y) => if y == 0 {{ rgb("#fef3c7") }} else if calc.odd(y) {{ rgb("#f8fafc") }} else {{ rgb("#ffffff") }},
      stroke: (x, y) => if y == 0 {{ (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) }} else {{ 0.4pt + rgb("#cbd5e1") }},
      inset: {inset_str},
      align: (x, y) => if y == 0 {{ center + horizon }} else {{ left + horizon }},
      {', '.join(cells)}
    )
  ]
]
"""


def convert_md_to_typst(md_text, assets_dir):
    """Converts manuscript markdown into idiomatic, publication-grade Typst markup."""
    # Escape standalone @ symbols (like @TantraGyan108)
    md_text = re.sub(r'@([a-zA-Z0-9_]+)', r'\\@\1', md_text)
    lines = md_text.split('\n')
    out = []
    in_shloka = False
    in_yoga = False
    in_formula = False
    in_warning = False
    in_table = False
    table_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        # Callout Directives
        if s.startswith('::: shloka'):
            m = re.search(r'\[(.*?)\]', s)
            source = m.group(1) if m else "शास्त्रीय प्रमाण"
            out.append(f"""
#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ {source.upper()}]
    ]
  ]
  #v(0.2cm)
""")
            in_shloka = True
            i += 1
            continue

        elif s.startswith('::: yoga'):
            m = re.search(r'\[(.*?)\]', s)
            title = m.group(1) if m else "शास्त्रीय राजयोग"
            out.append(f"""
#rect(
  fill: rgb("#fffbeb"),
  stroke: (left: 3.5pt + rgb("#d97706"), rest: 0.5pt + rgb("#fde68a")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#ca8a04"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[RAJA YOGA • {title}]
  ]
  #v(0.2cm)
""")
            in_yoga = True
            i += 1
            continue

        elif s.startswith('::: formula'):
            m = re.search(r'\[(.*?)\]', s)
            title = m.group(1) if m else "फलित सूत्र"
            out.append(f"""
#rect(
  fill: rgb("#f8fafc"),
  stroke: (left: 3.5pt + rgb("#334155"), rest: 0.5pt + rgb("#cbd5e1")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#f1f5f9"), stroke: 0.6pt + rgb("#64748b"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#1e293b"))[SUTRA • {title}]
  ]
  #v(0.2cm)
""")
            in_formula = True
            i += 1
            continue

        elif s.startswith('::: warning'):
            m = re.search(r'\[(.*?)\]', s)
            title = m.group(1) if m else "सावधान"
            out.append(f"""
#rect(
  fill: rgb("#fff1f2"),
  stroke: (left: 3.5pt + rgb("#dc2626"), rest: 0.5pt + rgb("#fecaca")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fee2e2"), stroke: 0.6pt + rgb("#ef4444"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#991b1b"))[CAVEAT • {title}]
  ]
  #v(0.2cm)
""")
            in_warning = True
            i += 1
            continue

        elif s.startswith('::: chart'):
            m = re.search(r'\[(.*?)\]', s)
            chart_name = m.group(1).strip() if m else "lagna_chart"
            svg_path = f"assets/icons/{chart_name}.svg"
            out.append(f'\n#align(center)[\n  #image("{svg_path}", width: 85%)\n]\n')
            # Collect and render caption
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(':::'):
                caption_line = lines[i].strip()
                if caption_line:
                    out.append(f'#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[{caption_line}]]\n')
                i += 1
            i += 1
            continue

        elif s == ':::':
            out.append(']\n')
            in_shloka = in_yoga = in_formula = in_warning = False
            i += 1
            continue

        # In shloka lines (sacred verse formatting)
        if in_shloka:
            out.append(f'  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[{s}]]\n')
            i += 1
            continue

        # Headings (Mapped to Typst levels)
        if s.startswith('# '):
            title = s[2:].strip()
            out.append(f'\n= {title}\n')
            i += 1
            continue
        elif s.startswith('## '):
            title = s[3:].strip()
            out.append(f'== {title}\n')
            i += 1
            continue
        elif s.startswith('### '):
            title = s[4:].strip()
            out.append(f'=== {title}\n')
            i += 1
            continue
        elif s.startswith('#### '):
            title = s[5:].strip()
            out.append(f'==== {title}\n')
            i += 1
            continue

        # Tables
        if '|' in s:
            table_lines.append(s)
            in_table = True
            i += 1
            continue
        elif in_table:
            # End of table
            typst_table = parse_markdown_table_to_typst(table_lines)
            out.append(typst_table)
            table_lines = []
            in_table = False

        # Horizontal rule
        if s in ['---', '***', '___']:
            out.append('\n#v(0.3cm)\n#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]\n#v(0.3cm)\n')
            i += 1
            continue

        # Bold & Italics
        s = re.sub(r'\*\*(.*?)\*\*', r'#strong[\1]', s)
        s = re.sub(r'\*(.*?)\*', r'#emph[\1]', s)

        # Apply authentic Jyotish planet colors & icons to prose
        s = apply_typst_planet_colors(s)

        out.append(s + '\n')
        i += 1

    if in_table and table_lines:
        out.append(parse_markdown_table_to_typst(table_lines))

    return "".join(out)


def compile_typst_book(metadata, chapters, output_pdf, base_dir):
    """
    Renders the complete manuscript into an elegant Typst document and compiles
    into an ultra-high resolution vector PDF.
    """
    typ_file = os.path.join(base_dir, "dist", "pdf", "astrology-book.typ")
    os.makedirs(os.path.dirname(typ_file), exist_ok=True)

    clean_youtube = metadata.get("youtube", "").replace("@", "\\@")
    clean_website = metadata.get("website", "")

    header_block = f"""
// ==============================================================================
// TANTRA GYAN VEDIC ASTROLOGY COMPENDIUM - TYPST MASTERWORK ACADEMIC EDITION
// ==============================================================================

#set page(
  paper: "a5",
  margin: (top: 1.2cm, bottom: 1.2cm, inside: 1.2cm, outside: 1.2cm),
  header: context {{
    let page_num = counter(page).get().first()
    if page_num > 4 {{
      if calc.odd(page_num) {{
        align(right)[
          #text(size: 7.5pt, fill: rgb("#78350f"), font: ("Cinzel", "Georgia", "Noto Sans Devanagari"))[
            TANTRA GYAN • VEDIC ASTROLOGY #h(1fr) #page_num
          ]
          #v(-3pt)
          #line(length: 100%, stroke: 0.4pt + rgb("#cbd5e1"))
        ]
      }} else {{
        align(left)[
          #text(size: 7.5pt, fill: rgb("#78350f"), font: ("Cinzel", "Georgia", "Noto Sans Devanagari"))[
            #page_num #h(1fr) {metadata.get("english_title", "")}
          ]
          #v(-3pt)
          #line(length: 100%, stroke: 0.4pt + rgb("#cbd5e1"))
        ]
      }}
    }}
  }},
  footer: context {{
    let page_num = counter(page).get().first()
    if page_num > 4 {{
      align(center)[
        #text(size: 7.5pt, fill: rgb("#94a3b8"))[— पृष्ठ #page_num —]
      ]
    }}
  }}
)

#set text(
  font: ("Noto Serif Devanagari", "Noto Sans Devanagari", "Devanagari MT", "Georgia", "Palatino"),
  size: 9.2pt,
  lang: "hi"
)

#set par(justify: true, leading: 0.70em)

// Masterwork Show Rules for Headings
#show heading.where(level: 1): it => {{
  v(0.8cm)
  align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#d97706"), radius: 3pt, inset: (x: 8pt, y: 3.5pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[TANTRA GYAN • VEDIC COMPENDIUM]
    ]
    #v(0.35cm)
    #text(size: 16pt, weight: "bold", fill: rgb("#78350f"))[#it.body]
    #v(0.2cm)
    #line(length: 45%, stroke: 1.2pt + rgb("#d97706"))
    #v(0.5cm)
  ]
}}

#show heading.where(level: 2): it => {{
  v(0.5cm)
  text(size: 11pt, weight: "bold", fill: rgb("#92400e"), style: "italic")[#it.body]
  v(0.2cm)
}}

#show heading.where(level: 3): it => {{
  v(0.45cm)
  rect(fill: rgb("#fffdf5"), stroke: (left: 3pt + rgb("#d97706")), inset: (left: 6pt, y: 2pt))[
    #text(size: 10pt, weight: "bold", fill: rgb("#78350f"))[#it.body]
  ]
  v(0.2cm)
}}

#show heading.where(level: 4): it => {{
  v(0.35cm)
  text(size: 9.5pt, weight: "bold", fill: rgb("#451a03"))[#it.body]
  v(0.15cm)
}}

// --- FRONT MATTER: GRAND COVER PAGE ---
#align(center + horizon)[
  #block(
    stroke: 1.8pt + rgb("#b45309"),
    inset: 14pt,
    radius: 4pt,
    width: 100%,
    [
      #block(
        stroke: 0.6pt + rgb("#d97706"),
        inset: 12pt,
        width: 100%,
        [
          #v(0.2cm)
          #image("assets/icons/yantra.svg", width: 38%)
          #v(0.6cm)
          #text(size: 19pt, weight: "bold", fill: rgb("#78350f"))[{metadata.get("title")}]
          #v(0.2cm)
          #text(size: 10.5pt, weight: "bold", fill: rgb("#b45309"), font: ("Cinzel", "Georgia"))[{metadata.get("english_title")}]
          #v(0.35cm)
          #line(length: 60%, stroke: 1pt + rgb("#d97706"))
          #v(0.3cm)
          #text(size: 9pt, style: "italic", fill: rgb("#57534e"))[{metadata.get("subtitle")}]
          #v(0.8cm)
          #text(size: 8pt, fill: rgb("#78350f"), tracking: 1pt)[ग्रंथकार एवं ज्योतिषाचार्य] \\
          #v(0.12cm)
          #text(size: 13pt, weight: "bold", fill: rgb("#78350f"))[{metadata.get("author_hindi")}] \\
          #text(size: 9.5pt, fill: rgb("#57534e"), font: ("Cinzel", "Georgia"))[({metadata.get("author")})] \\
          #text(size: 8pt, fill: rgb("#71717a"))[{metadata.get("author_title")}]
          #v(0.7cm)
          #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#d97706"), radius: 3pt, inset: (x: 8pt, y: 3pt))[
            #text(size: 7.5pt, weight: "bold", fill: rgb("#78350f"))[प्रथम शास्त्रीय मुद्रण संस्करण • Trade Paperback Masterwork Edition]
          ]
          #v(0.35cm)
          #text(size: 8pt, fill: rgb("#64748b"))[{metadata.get("publisher")} • {metadata.get("year")}]
        ]
      )
    ]
  )
]

#pagebreak()

// Copyright & Dedication
#text(size: 8.5pt, fill: rgb("#475569"))[
  #strong[{metadata.get("title")}] \\
  #emph[{metadata.get("english_title")}] \\
  {metadata.get("copyright")} \\
  ISBN: {metadata.get("isbn")} \\
  प्रकाशक: {metadata.get("publisher")} \\
  वेबसाइट: {clean_website} • यूट्यूब: {clean_youtube}
]

#v(2cm)
#align(center)[
  #image("assets/icons/ganesha.svg", width: 14%)
  #v(0.4cm)
  #text(size: 11pt, weight: "bold", fill: rgb("#78350f"), style: "italic")[
    वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ। \\
    निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥
  ]
  #v(0.4cm)
  #text(size: 9.5pt, fill: rgb("#57534e"))[
    यह ग्रंथ समस्त गुरुजनों, वैदिक ऋषियों एवं जिज्ञासुओं को सप्रेम समर्पित है।
  ]
]

#pagebreak()

// Table of Contents
#outline(title: "ग्रंथ अनुक्रमणिका • Table of Contents", depth: 2, indent: auto)

#pagebreak()

// Dedicated Full-Color Navagraha Reference Plate
#align(center)[
  #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#d97706"), radius: 3pt, inset: (x: 8pt, y: 3pt))[
    #text(size: 7.5pt, weight: "bold", fill: rgb("#78350f"))[शास्त्रीय ग्रह स्वरूप चक्र • PARASHARI COLOR PALETTE]
  ]
  #v(0.2cm)
  #text(size: 14pt, weight: "bold", fill: rgb("#78350f"))[नवग्रह शास्त्रीय स्वरूप, वर्ण एवं प्रतीक परिचय]
  #v(0.12cm)
  #text(size: 8pt, style: "italic", fill: rgb("#57534e"))[बृहत्पाराशर होरा शास्त्र एवं फलदीपिका अनुसार नवग्रहों का खगोलीय स्वरूप, रत्न, धातु, वर्ण एवं उच्च-नीच मर्यादा]
  #v(0.35cm)
]

#grid(
  columns: (1fr, 1fr),
  gutter: 7pt,
  // 1. Sun
  rect(fill: rgb("#fff7ed"), stroke: 0.6pt + rgb("#ea580c"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/sun.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#c2410c"), size: 8pt)[सूर्य • Sun (Su)] \\ #text(size: 6.5pt, fill: rgb("#7c2d12"))[शास्त्रीय वर्ण: रक्त / ताम्रवर्ण]],
      [#align(right)[#text(size: 10pt, fill: rgb("#ea580c"))[☉]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#451a03"))[
      *देवता / तत्व:* अग्नि • तेजस | *रत्न:* माणिक्य • तांबा \\
      *उच्च / नीच:* मेष 10° / तुला 10° | *कारकत्व:* आत्मा, पिता, राजसत्ता
    ]
  ],
  // 2. Moon
  rect(fill: rgb("#f8fafc"), stroke: 0.6pt + rgb("#94a3b8"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/moon.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#334155"), size: 8pt)[चन्द्र • Moon (Mo)] \\ #text(size: 6.5pt, fill: rgb("#475569"))[शास्त्रीय वर्ण: श्वेत / चन्द्रकान्ति]],
      [#align(right)[#text(size: 10pt, fill: rgb("#94a3b8"))[☽]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#1e293b"))[
      *देवता / तत्व:* वरुण • जल तत्व | *रत्न:* मोती • चांदी \\
      *उच्च / नीच:* वृषभ 3° / वृश्चिक 3° | *कारकत्व:* मन, माता, मानसिक शांति
    ]
  ],
  // 3. Mars
  rect(fill: rgb("#fef2f2"), stroke: 0.6pt + rgb("#ef4444"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/mars.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#dc2626"), size: 8pt)[मंगल • Mars (Ma)] \\ #text(size: 6.5pt, fill: rgb("#991b1b"))[शास्त्रीय वर्ण: रक्तवर्ण (कुज)]],
      [#align(right)[#text(size: 10pt, fill: rgb("#ef4444"))[♂]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#7f1d1d"))[
      *देवता / तत्व:* कार्तिकेय • अग्नि | *रत्न:* मूंगा • तांबा \\
      *उच्च / नीच:* मकर 28° / कर्क 28° | *कारकत्व:* पराक्रम, भ्राता, शौर्य
    ]
  ],
  // 4. Mercury
  rect(fill: rgb("#f0fdf4"), stroke: 0.6pt + rgb("#10b981"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/mercury.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#047857"), size: 8pt)[बुध • Mercury (Me)] \\ #text(size: 6.5pt, fill: rgb("#065f46"))[शास्त्रीय वर्ण: हरित / श्याम]],
      [#align(right)[#text(size: 10pt, fill: rgb("#10b981"))[☿]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#064e3b"))[
      *देवता / तत्व:* विष्णु • पृथ्वी | *रत्न:* पन्ना • कांसा \\
      *उच्च / नीच:* कन्या 15° / मीन 15° | *कारकत्व:* बुद्धि, वाणी, व्यापार
    ]
  ],
  // 5. Jupiter
  rect(fill: rgb("#fffbeb"), stroke: 0.6pt + rgb("#f59e0b"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/jupiter.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#b45309"), size: 8pt)[गुरु • Jupiter (Ju)] \\ #text(size: 6.5pt, fill: rgb("#92400e"))[शास्त्रीय वर्ण: पीत / कनकवर्ण]],
      [#align(right)[#text(size: 10pt, fill: rgb("#f59e0b"))[♃]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#78350f"))[
      *देवता / तत्व:* इन्द्र / ब्रह्मा • आकाश | *रत्न:* पुखराज • स्वर्ण \\
      *उच्च / नीच:* कर्क 5° / मकर 5° | *कारकत्व:* ज्ञान, धर्म, संतान, विवेक
    ]
  ],
  // 6. Venus
  rect(fill: rgb("#fdf2f8"), stroke: 0.6pt + rgb("#f43f5e"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/venus.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#be185d"), size: 8pt)[शुक्र • Venus (Ve)] \\ #text(size: 6.5pt, fill: rgb("#9d174d"))[शास्त्रीय वर्ण: चित्र / शुभ्र श्वेत]],
      [#align(right)[#text(size: 10pt, fill: rgb("#f43f5e"))[♀]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#831843"))[
      *देवता / तत्व:* इंद्राणी • जल तत्व | *रत्न:* हीरा • चांदी \\
      *उच्च / नीच:* मीन 27° / कन्या 27° | *कारकत्व:* प्रेम, ऐश्वर्य, कला, दांपत्य
    ]
  ],
  // 7. Saturn
  rect(fill: rgb("#eff6ff"), stroke: 0.6pt + rgb("#3b82f6"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/saturn.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#1d4ed8"), size: 8pt)[शनि • Saturn (Sa)] \\ #text(size: 6.5pt, fill: rgb("#1e40af"))[शास्त्रीय वर्ण: कृष्ण / नीलवर्ण]],
      [#align(right)[#text(size: 11pt, fill: rgb("#3b82f6"))[♄]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#1e3a8a"))[
      *देवता / तत्व:* यमराज • वायु तत्व | *रत्न:* नीलम • लोहा \\
      *उच्च / नीच:* तुला 20° / मेष 20° | *कारकत्व:* कर्म, न्याय, वैराग्य, दीर्घायु
    ]
  ],
  // 8. Rahu
  rect(fill: rgb("#f4f4f5"), stroke: 0.6pt + rgb("#27272a"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/rahu.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#09090b"), size: 8pt)[राहु • Rahu (Ra)] \\ #text(size: 6.5pt, fill: rgb("#27272a"))[शास्त्रीय स्वरूप: धूम्रवर्ण (तमोगुणी)]],
      [#align(right)[#text(size: 10pt, fill: rgb("#27272a"))[☊]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#09090b"))[
      *देवता / तत्व:* सर्प • तमोगुण (छाया) | *रत्न:* गोमेद • सीसा \\
      *उच्च / नीच:* मिथुन / धनु | *कारकत्व:* कूटनीति, विद्रोही भाव, विदेश
    ]
  ],
  // 9. Ketu
  rect(fill: rgb("#f4f4f5"), stroke: 0.6pt + rgb("#71717a"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/ketu.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#52525b"), size: 8pt)[केतु • Ketu (Ke)] \\ #text(size: 6.5pt, fill: rgb("#52525b"))[शास्त्रीय स्वरूप: चित्र / धूम्रवर्ण]],
      [#align(right)[#text(size: 10pt, fill: rgb("#71717a"))[☋]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#27272a"))[
      *देवता / तत्व:* चित्रगुप्त • तमोगुण (छाया) | *रत्न:* लहसुनिया • मिश्र धातु \\
      *उच्च / नीच:* धनु / मिथुन | *कारकत्व:* मोक्ष, अंतर्ज्ञान, वैराग्य, मौन
    ]
  ],
  // 10. Lagna
  rect(fill: rgb("#faf5ff"), stroke: 0.6pt + rgb("#a855f7"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/lagna.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#6b21a8"), size: 8pt)[लग्न • Ascendant (Asc)] \\ #text(size: 6.5pt, fill: rgb("#7e22ce"))[शास्त्रीय स्वरूप: उदित लग्न (तनु भाव)]],
      [#align(right)[#text(size: 10pt, fill: rgb("#a855f7"))[✦]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#581c87"))[
      *स्वरूप:* कालपुरुष प्रथम भाव (तनु भाव) | *दिग्बल:* पूर्व क्षितिज \\
      *मर्यादा:* देह सौष्ठव, तेज, आत्मबल, जीवन गति
    ]
  ]
)
"""

    chapter_blocks = []
    for ch in chapters:
        md_text = ch.get("raw_text", "")
        typst_content = convert_md_to_typst(md_text, os.path.join(base_dir, "assets"))
        chapter_blocks.append(f"\n#pagebreak()\n{typst_content}\n")

    full_typst = header_block + "".join(chapter_blocks)

    with open(typ_file, "w", encoding="utf-8") as f:
        f.write(full_typst)

    print(f"✓ Generated Typst document: {typ_file}")

    # Compile with Typst and bundled OpenType Noto Sans Devanagari fonts
    fonts_dir = os.path.join(base_dir, "assets", "fonts")
    font_paths = [fonts_dir] if os.path.exists(fonts_dir) else None
    typst.compile(typ_file, output=output_pdf, root=base_dir, font_paths=font_paths)
    print(f"✓ Typst PDF successfully compiled: {output_pdf}")
    return output_pdf
