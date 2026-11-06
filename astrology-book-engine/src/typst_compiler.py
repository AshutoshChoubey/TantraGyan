#!/usr/bin/env python3
"""
Typst Publishing Compiler for Astrology Book Engine
===================================================
Translates manuscript chapters into modern Typst markup and compiles
ultra-high resolution trade-paperback (6x9in) vector PDFs.
Base Reference: https://github.com/typst/typst & https://github.com/wandmalfarbe/pandoc-latex-template
"""

import os
import re
import typst
import yaml

def escape_typst(text):
    """Escapes special Typst markup characters in plain text."""
    if not text:
        return ""
    # Escape @, $, #
    text = text.replace('\\', '\\\\')
    text = text.replace('@', '\\@')
    text = text.replace('$', '\\$')
    return text

def convert_md_to_typst(md_text, assets_dir):
    """Converts manuscript markdown into idiomatic Typst markup."""
    # Escape standalone @ symbols (like @TantraGyan108) so Typst doesn't treat them as citations
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

        # Callout directives
        if s.startswith('::: shloka'):
            m = re.search(r'\[(.*?)\]', s)
            source = m.group(1) if m else "शास्त्रीय प्रमाण"
            out.append(f'\n#rect(fill: rgb("#fffdf5"), stroke: (left: 3pt + rgb("#b45309"), rest: 0.6pt + rgb("#d97706")), radius: 4pt, width: 100%, inset: 11pt)[\n  #align(center)[#text(size: 9pt, weight: "bold", fill: rgb("#78350f"))[ॐ {source.upper()}]]\n')
            in_shloka = True
            i += 1
            continue
        elif s.startswith('::: yoga'):
            m = re.search(r'\[(.*?)\]', s)
            title = m.group(1) if m else "राजयोग"
            out.append(f'\n#rect(fill: rgb("#fefce8"), stroke: (left: 3.5pt + rgb("#ca8a04"), rest: 0.6pt + rgb("#eab308")), radius: 4pt, width: 100%, inset: 11pt)[\n  #text(size: 9.5pt, weight: "bold", fill: rgb("#78350f"))[⚜ RAJA YOGA: {title}]\n')
            in_yoga = True
            i += 1
            continue
        elif s.startswith('::: formula'):
            m = re.search(r'\[(.*?)\]', s)
            title = m.group(1) if m else "फलित सूत्र"
            out.append(f'\n#rect(fill: rgb("#f8fafc"), stroke: (left: 3.5pt + rgb("#334155"), rest: 0.6pt + rgb("#94a3b8")), radius: 4pt, width: 100%, inset: 11pt)[\n  #text(size: 9.5pt, weight: "bold", fill: rgb("#0f172a"))[📐 SUTRA: {title}]\n')
            in_formula = True
            i += 1
            continue
        elif s.startswith('::: warning'):
            m = re.search(r'\[(.*?)\]', s)
            title = m.group(1) if m else "सावधान"
            out.append(f'\n#rect(fill: rgb("#fff1f2"), stroke: (left: 3.5pt + rgb("#dc2626"), rest: 0.6pt + rgb("#f87171")), radius: 4pt, width: 100%, inset: 11pt)[\n  #text(size: 9.5pt, weight: "bold", fill: rgb("#991b1b"))[⚠️ CAVEAT: {title}]\n')
            in_warning = True
            i += 1
            continue
        elif s.startswith('::: chart'):
            m = re.search(r'\[(.*?)\]', s)
            chart_name = m.group(1).strip() if m else "lagna_chart"
            svg_path = f"assets/icons/{chart_name}.svg"
            out.append(f'\n#align(center)[\n  #image("{svg_path}", width: 85%)\n]\n')
            # Skip until :::
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

        # In shloka lines
        if in_shloka:
            out.append(f'  #align(center)[#text(size: 11pt, weight: "bold", fill: rgb("#451a03"))[{s}]]\n')
            i += 1
            continue

        # Headings
        if s.startswith('# '):
            title = s[2:].strip()
            out.append(f'\n#heading(level: 1)[{title}]\n')
            i += 1
            continue
        elif s.startswith('## '):
            title = s[3:].strip()
            out.append(f'#heading(level: 2)[{title}]\n')
            i += 1
            continue
        elif s.startswith('### '):
            title = s[4:].strip()
            out.append(f'#heading(level: 3)[{title}]\n')
            i += 1
            continue
        elif s.startswith('#### '):
            title = s[5:].strip()
            out.append(f'#heading(level: 4)[{title}]\n')
            i += 1
            continue

        # Tables
        if '|' in s:
            table_lines.append(s)
            in_table = True
            i += 1
            continue
        elif in_table:
            # End of table, convert table_lines
            typst_table = parse_markdown_table_to_typst(table_lines)
            out.append(typst_table)
            table_lines = []
            in_table = False

        # Horizontal rule
        if s in ['---', '***', '___']:
            out.append('\n#line(length: 100%, stroke: 0.5pt + rgb("#ca8a04"))\n')
            i += 1
            continue

        # Bold & Italics
        s = re.sub(r'\*\*(.*?)\*\*', r'#strong[\1]', s)
        s = re.sub(r'\*(.*?)\*', r'#emph[\1]', s)

        out.append(s + '\n')
        i += 1

    if in_table and table_lines:
        out.append(parse_markdown_table_to_typst(table_lines))

    return "".join(out)


def parse_markdown_table_to_typst(lines):
    """Converts a Markdown table into a Typst #table()."""
    rows = []
    for l in lines:
        if re.match(r'^\s*\|?\s*:?-+:?\s*\|', l):
            continue # separator line
        parts = [c.strip() for c in l.split('|')]
        # Drop empty edge parts
        if parts and parts[0] == '':
            parts.pop(0)
        if parts and parts[-1] == '':
            parts.pop(-1)
        if parts:
            rows.append(parts)

    if not rows:
        return ""

    num_cols = len(rows[0])
    cells = []
    for r_idx, row in enumerate(rows):
        for cell in row:
            # Bold headers
            cell_fmt = re.sub(r'\*\*(.*?)\*\*', r'#strong[\1]', cell)
            if r_idx == 0:
                cells.append(f'[#text(weight: "bold", fill: rgb("#78350f"))[{cell_fmt}]]')
            else:
                cells.append(f'[{cell_fmt}]')

    return f"""
#align(center)[
  #table(
    columns: {num_cols},
    fill: (x, y) => if y == 0 {{ rgb("#fef08a") }} else if calc.odd(y) {{ rgb("#f8fafc") }} else {{ none }},
    stroke: 0.5pt + rgb("#cbd5e1"),
    inset: (x: 6pt, y: 5pt),
    {', '.join(cells)}
  )
]
"""


def compile_typst_book(metadata, chapters, output_pdf, base_dir):
    """
    Renders the complete manuscript into a Typst document and compiles
    into an ultra-high resolution vector PDF.
    """
    typ_file = os.path.join(base_dir, "dist", "pdf", "astrology-book.typ")
    os.makedirs(os.path.dirname(typ_file), exist_ok=True)

    clean_youtube = metadata.get("youtube", "").replace("@", "\\@")
    clean_website = metadata.get("website", "")

    header_block = f"""
// Tantra Gyan Vedic Astrology Compendium - Typst Masterwork Edition
#set page(
  paper: "a5",
  margin: (top: 2cm, bottom: 2cm, inside: 2.2cm, outside: 1.8cm),
  header: context {{
    let page_num = counter(page).get().first()
    if page_num > 4 {{
      if calc.odd(page_num) {{
        align(right, text(size: 8pt, fill: rgb("#78350f"))[
          तंत्र ज्ञान • VEDIC ASTROLOGY COMPENDIUM #h(1fr) #page_num
        ])
      }} else {{
        align(left, text(size: 8pt, fill: rgb("#78350f"))[
          #page_num #h(1fr) {metadata.get("english_title", "")}
        ])
      }}
    }}
  }}
)

#set text(
  font: ("Devanagari MT", "Kohinoor Devanagari", "Georgia", "Palatino", "Serif"),
  size: 9.5pt,
  lang: "hi"
)

#set par(justify: true, leading: 0.72em)

// --- FRONT MATTER ---
#align(center + horizon)[
  #image("assets/icons/yantra.svg", width: 35%)
  #v(1.5cm)
  #text(size: 22pt, weight: "bold", fill: rgb("#78350f"))[{metadata.get("title")}]
  #v(0.3cm)
  #text(size: 13pt, weight: "bold", fill: rgb("#b45309"))[{metadata.get("english_title")}]
  #v(0.5cm)
  #text(size: 10pt, style: "italic", fill: rgb("#57534e"))[{metadata.get("subtitle")}]
  #v(1.5cm)
  #text(size: 9pt, fill: rgb("#78350f"))[ग्रंथकार एवं ज्योतिषाचार्य] \\
  #text(size: 14pt, weight: "bold", fill: rgb("#78350f"))[{metadata.get("author_hindi")} ({metadata.get("author")})] \\
  #text(size: 9pt, fill: rgb("#64748b"))[{metadata.get("author_title")}]
  #v(1.5cm)
  #line(length: 60%, stroke: 0.5pt + rgb("#cbd5e1"))
  #text(size: 9pt, fill: rgb("#64748b"))[{metadata.get("publisher")} • {metadata.get("year")}]
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
