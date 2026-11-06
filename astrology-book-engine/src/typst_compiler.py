#!/usr/bin/env python3
"""
Typst Publishing Compiler for Astrology Book Engine (Masterwork Edition)
========================================================================
Translates manuscript chapters into modern, academic-grade Typst markup
and compiles ultra-high resolution trade-paperback (A5 / 6x9in) vector PDFs.
Features:
- Authentic Vedic Jyotish color-coded planetary typography
- Royal ornamental framed title and dedication pages
- Proportional responsive tables with header accents and zero horizontal overflow
- Classical shloka, yoga, and sutra callout boxes
- Symmetrical chapter headers with decorative hairline rules
"""

import os
import re
import typst
import yaml

# Authentic Vedic Jyotish Planet Color Palette for Typst
TYPST_PLANET_COLORS = [
    # Sun - Saffron
    (r'(?<![क-हअ-औ्])(?:सूर्य\s*\(\s*Sun\s*\)|सूर्यदेव|सूर्य|\bSun\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#c2410c")'),
    # Moon - Pearl / Silver Gray
    (r'(?<![क-हअ-औ्])(?:चन्द्र\s*\(\s*Moon\s*\)|चंद्र\s*\(\s*Moon\s*\)|चन्द्रमा|चंद्रमा|चन्द्र|चंद्र|\bMoon\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#475569")'),
    # Mars - Fiery Crimson Red
    (r'(?<![क-हअ-औ्])(?:मंगल\s*\(\s*Mars\s*\)|मंगलदेव|मंगल|\bMars\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#dc2626")'),
    # Mercury - Emerald Green
    (r'(?<![क-हअ-औ्])(?:बुध\s*\(\s*Mercury\s*\)|बुधदेव|बुध|\bMercury\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#047857")'),
    # Jupiter - Golden Turmeric Yellow
    (r'(?<![क-हअ-औ्])(?:(?:गुरु\s*/\s*बृहस्पति|बृहस्पति|देवगुरु|गुरु(?!\s*जन))\s*\(\s*Jupiter\s*\)|बृहस्पति|देवगुरु|गुरु(?!\s*जन)|\bJupiter\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#b45309")'),
    # Venus - Diamond Rose Pink
    (r'(?<![क-हअ-औ्])(?:शुक्र\s*\(\s*Venus\s*\)|शुक्रदेव|शुक्र|\bVenus\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#be185d")'),
    # Saturn - Deep Cosmic Royal Blue
    (r'(?<![क-हअ-औ्])(?:शनि\s*\(\s*Saturn\s*\)|शनिदेव|शनैश्चर|शनि|\bSaturn\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#1d4ed8")'),
    # Rahu - Shadow Obsidian Black
    (r'(?<![क-हअ-औ्])(?:राहु\s*\(\s*Rahu\s*\)|राहु|\bRahu\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#09090b")'),
    # Ketu - Smokey Ash Shadow Gray
    (r'(?<![क-हअ-औ्])(?:केतु\s*\(\s*Ketu\s*\)|केतु|\bKetu\b)(?![क-हअ-औ्ा-ौ])', 'rgb("#52525b")'),
]


def apply_typst_planet_colors(text):
    """Wraps matched planetary names in their signature Typst colored bold spans."""
    for pattern, color_expr in TYPST_PLANET_COLORS:
        text = re.sub(
            pattern,
            lambda m: f'#text(fill: {color_expr}, weight: "bold")[{m.group(0)}]',
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

    # Dynamic proportional column sizing to eliminate horizontal overflow
    if num_cols == 7:
        cols_str = "(1.1fr, 1.8fr, 1.8fr, 1.3fr, 1.1fr, 1.1fr, 1.1fr)"
        text_size = "7.2pt"
        inset_str = "(x: 3.5pt, y: 4.5pt)"
    elif num_cols == 6:
        cols_str = "(0.8fr, 1.4fr, 1.2fr, 1.2fr, 1.4fr, 1.4fr)"
        text_size = "7.2pt"
        inset_str = "(x: 3.5pt, y: 4.5pt)"
    elif num_cols == 5:
        cols_str = "(0.9fr, 1.4fr, 2.2fr, 1.3fr, 1.3fr)"
        text_size = "7.8pt"
        inset_str = "(x: 4.5pt, y: 5pt)"
    elif num_cols == 4:
        cols_str = "(1.2fr, 1.4fr, 1.2fr, 2.2fr)"
        text_size = "8.2pt"
        inset_str = "(x: 5pt, y: 5.5pt)"
    elif num_cols == 3:
        cols_str = "(1.3fr, 2.2fr, 2.5fr)"
        text_size = "8.5pt"
        inset_str = "(x: 6pt, y: 6pt)"
    else:
        cols_str = f"{num_cols}"
        text_size = "8.5pt"
        inset_str = "(x: 6pt, y: 6pt)"

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
  #text(size: {text_size})[
    #table(
      columns: {cols_str},
      fill: (x, y) => if y == 0 {{ rgb("#fef3c7") }} else if calc.odd(y) {{ rgb("#fbfaf7") }} else {{ none }},
      stroke: (x, y) => if y == 0 {{ (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#e2e8f0")) }} else {{ 0.4pt + rgb("#e2e8f0") }},
      inset: {inset_str},
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
            out.append(f'  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[{s}]]\n')
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

        # Apply authentic Jyotish planet colors to prose
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
  margin: (top: 2.2cm, bottom: 2.2cm, inside: 2.4cm, outside: 1.8cm),
  header: context {{
    let page_num = counter(page).get().first()
    if page_num > 4 {{
      if calc.odd(page_num) {{
        align(right)[
          #text(size: 7.8pt, fill: rgb("#78350f"), font: ("Cinzel", "Georgia"))[
            TANTRA GYAN • VEDIC ASTROLOGY #h(1fr) #page_num
          ]
          #v(-3pt)
          #line(length: 100%, stroke: 0.4pt + rgb("#e2e8f0"))
        ]
      }} else {{
        align(left)[
          #text(size: 7.8pt, fill: rgb("#78350f"), font: ("Cinzel", "Georgia"))[
            #page_num #h(1fr) {metadata.get("english_title", "")}
          ]
          #v(-3pt)
          #line(length: 100%, stroke: 0.4pt + rgb("#e2e8f0"))
        ]
      }}
    }}
  }}
)

#set text(
  font: ("Devanagari MT", "Kohinoor Devanagari", "Georgia", "Palatino"),
  size: 9.2pt,
  lang: "hi"
)

#set par(justify: true, leading: 0.72em)

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

    # Compile with Typst
    typst.compile(typ_file, output=output_pdf, root=base_dir)
    print(f"✓ Typst PDF successfully compiled: {output_pdf}")
    return output_pdf
