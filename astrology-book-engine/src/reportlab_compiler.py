#!/usr/bin/env python3
"""
ReportLab + Devanagari Shaper Publication Compiler
==================================================
Compiles the Tantra Gyan Vedic Astrology Manuscript into a print-ready PDF
using ReportLab and HarfBuzz visual-order Devanagari shaping (devanagari-reportlab).
"""

import os
import re
import glob

# Runtime patch to devanagari_reportlab for advanced HTML tags & auto inline markup
def patch_devanagari_reportlab():
    try:
        import devanagari_reportlab.markup as drm
        import devanagari_reportlab.shaper as drs

        drm.INLINE_TAGS = ("b", "i", "u", "s", "super", "sub", "br", "nobr", "font", "a")
        drm._INLINE_TAG_RE = re.compile(
            r"(</?(?:(?:b|i|u|s|super|sub|br|nobr)\b|(?:font|a)(?:\s+[^>]+)?)\s*/?>)",
            re.IGNORECASE,
        )

        orig_markup = drs.Shaper.markup
        def patched_markup(self, value: object, *, linebreaks: bool = False, allow_inline_markup: bool = True) -> str:
            return orig_markup(self, value, linebreaks=linebreaks, allow_inline_markup=allow_inline_markup)
        drs.Shaper.markup = patched_markup
    except Exception as e:
        pass

patch_devanagari_reportlab()

from devanagari_reportlab import Shaper
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.pagesizes import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle

try:
    import cairosvg
except ImportError:
    cairosvg = None


PLANET_COLOR_MAP = {
    "सूर्य": "#b45309",
    "चन्द्र": "#475569",
    "चन्द्रमा": "#475569",
    "मंगल": "#b91c1c",
    "बुध": "#047857",
    "गुरु": "#a16207",
    "बृहस्पति": "#a16207",
    "शुक्र": "#be185d",
    "शनि": "#1e293b",
    "राहु": "#475569",
    "केतु": "#7c2d12",
    "लग्न": "#0f766e",
}


def clean_markdown_inline(text):
    """
    Cleans markdown formatting into ReportLab paragraph markup:
    - [label](url) -> <a href="url"><font color="#2563eb"><u>label</u></font></a>
    - **bold** -> <b>bold</b>
    - *italic* -> <i>italic</i>
    - Applies Shastric planetary colors to bold planet names
    """
    if not text:
        return ""

    # Replace markdown links: [text](url) -> <a href="url"><font color="#2563eb"><u>text</u></font></a>
    def replace_link(match):
        label = match.group(1)
        url = match.group(2)
        return f'<a href="{url}"><font color="#2563eb"><u>{label}</u></font></a>'

    formatted = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, text)

    # Replace bold markers: **text** -> <b>text</b>
    formatted = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', formatted)

    # Replace italic markers: *text* -> <i>text</i>
    formatted = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'<i>\1</i>', formatted)

    # Colorize planet bold tags
    for p_name, hex_c in PLANET_COLOR_MAP.items():
        pattern = re.compile(rf'<b>({re.escape(p_name)}(?:[^\<]*?))</b>')
        formatted = pattern.sub(rf'<font color="{hex_c}"><b>\1</b></font>', formatted)

    return formatted


def ensure_raster_charts(base_dir):
    """Pre-converts SVG charts to high-res PNG for ReportLab if cairosvg is present."""
    icon_dir = os.path.join(base_dir, "assets", "icons")
    raster_dir = os.path.join(base_dir, "assets", "raster_charts")
    os.makedirs(raster_dir, exist_ok=True)

    if not cairosvg:
        return raster_dir

    svg_files = glob.glob(os.path.join(icon_dir, "*.svg"))
    for svg_file in svg_files:
        name = os.path.splitext(os.path.basename(svg_file))[0]
        png_path = os.path.join(raster_dir, f"{name}.png")
        if not os.path.exists(png_path) or os.path.getmtime(png_path) < os.path.getmtime(svg_file):
            try:
                cairosvg.svg2png(url=svg_file, write_to=png_path, output_width=1200)
            except Exception as e:
                print(f"Warning: could not convert {svg_file} to PNG: {e}")
    return raster_dir


def compile_reportlab_book(metadata, chapters, output_pdf, base_dir):
    """
    Compiles manuscript chapters into a publication-grade PDF with devanagari-reportlab.
    """
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
    raster_dir = ensure_raster_charts(base_dir)

    # Standard trade paperback 6 x 9 inches
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=(6 * inch, 9 * inch),
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch
    )

    shaper = Shaper()
    base_styles = shaper.styles(body_size=9.2)

    # Typography styles
    title_style = ParagraphStyle(
        "GrandTitle",
        parent=base_styles["title"],
        fontSize=20,
        leading=26,
        textColor=colors.HexColor("#78350f"),
        alignment=1, # Center
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        "GrandSubtitle",
        parent=base_styles["heading"],
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#854d0e"),
        alignment=1,
        spaceAfter=14
    )

    author_style = ParagraphStyle(
        "AuthorStyle",
        parent=base_styles["body"],
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#1e293b"),
        alignment=1,
        spaceAfter=6
    )

    verse_style = ParagraphStyle(
        "MangalaVerse",
        parent=base_styles["quote"],
        fontSize=10,
        leading=17,
        textColor=colors.HexColor("#78350f"),
        alignment=1,
        spaceBefore=8,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        "ChapterH1",
        parent=base_styles["heading"],
        fontSize=15,
        leading=20,
        textColor=colors.HexColor("#78350f"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        "SectionH2",
        parent=base_styles["heading"],
        fontSize=12,
        leading=17,
        textColor=colors.HexColor("#854d0e"),
        spaceBefore=12,
        spaceAfter=5,
        keepWithNext=True
    )

    h3_style = ParagraphStyle(
        "SubSectionH3",
        parent=base_styles["heading"],
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#78350f"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    h4_style = ParagraphStyle(
        "SubSubSectionH4",
        parent=base_styles["heading"],
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#1e293b"),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        "BookBody",
        parent=base_styles["body"],
        fontSize=9.2,
        leading=14.5,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        "BookBullet",
        parent=base_styles["body"],
        fontSize=9.0,
        leading=14.0,
        textColor=colors.HexColor("#1e293b"),
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=4
    )

    list_style = ParagraphStyle(
        "BookList",
        parent=base_styles["body"],
        fontSize=9.0,
        leading=14.0,
        textColor=colors.HexColor("#1e293b"),
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=4
    )

    callout_title_style = ParagraphStyle(
        "CalloutTitle",
        parent=base_styles["heading"],
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#78350f"),
        spaceAfter=3
    )

    callout_body_style = ParagraphStyle(
        "CalloutBody",
        parent=base_styles["body"],
        fontSize=8.8,
        leading=13.2,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=2
    )

    caption_style = ParagraphStyle(
        "FigureCaption",
        parent=base_styles["body"],
        fontSize=8.0,
        leading=11.0,
        textColor=colors.HexColor("#64748b"),
        alignment=1, # Center
        spaceAfter=6
    )

    table_cell_style = ParagraphStyle(
        "TableCell",
        parent=base_styles["body"],
        fontSize=7.2,
        leading=9.5,
        textColor=colors.HexColor("#1e293b")
    )

    table_header_style = ParagraphStyle(
        "TableHeader",
        parent=base_styles["body"],
        fontSize=7.5,
        leading=10.0,
        textColor=colors.HexColor("#78350f")
    )

    story = []

    # -------------------------------------------------------------
    # 1. GRAND TITLE PAGE
    # -------------------------------------------------------------
    story.append(Spacer(1, 0.4 * inch))
    story.append(shaper.paragraph(clean_markdown_inline(metadata.get("title", "")), title_style))
    story.append(shaper.paragraph(clean_markdown_inline(metadata.get("english_title", "")), subtitle_style))
    story.append(Spacer(1, 0.15 * inch))
    story.append(shaper.paragraph(clean_markdown_inline(metadata.get("subtitle", "")), body_style))
    story.append(Spacer(1, 0.35 * inch))

    author_name = f"<b>ग्रंथकार:</b> {metadata.get('author_hindi')} ({metadata.get('author')})"
    story.append(shaper.paragraph(clean_markdown_inline(author_name), author_style))
    story.append(shaper.paragraph(clean_markdown_inline(metadata.get("author_title", "")), author_style))
    story.append(Spacer(1, 0.25 * inch))

    story.append(HRFlowable(width="80%", thickness=0.8, color=colors.HexColor("#ca8a04"), spaceAfter=14))
    story.append(shaper.paragraph(clean_markdown_inline(f"{metadata.get('publisher')} • {metadata.get('edition')}"), author_style))
    website_line = f'<a href="{metadata.get("website")}"><font color="#2563eb"><u>{metadata.get("website")}</u></font></a> • {metadata.get("youtube")}'
    story.append(shaper.paragraph(clean_markdown_inline(website_line), author_style))

    story.append(PageBreak())

    # -------------------------------------------------------------
    # 2. COPYRIGHT & MANGALACHARAN
    # -------------------------------------------------------------
    story.append(shaper.paragraph("<b>वैधानिक सूचना एवं सर्वाधिकार (Copyright & Legal Notice)</b>", h2_style))
    story.append(shaper.paragraph(clean_markdown_inline(metadata.get("copyright", "")), body_style))
    story.append(shaper.paragraph(clean_markdown_inline(f"ISBN: {metadata.get('isbn')} • प्रकाशन वर्ष: {metadata.get('year')}"), body_style))
    story.append(shaper.paragraph(clean_markdown_inline(f"प्रकाशक: {metadata.get('publisher')}"), body_style))
    story.append(Spacer(1, 0.25 * inch))

    story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#e2e8f0"), spaceAfter=12))

    story.append(shaper.paragraph("वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ।<br/>निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥", verse_style))
    story.append(shaper.paragraph("यह ग्रंथ समस्त गुरुजनों, वैदिक ऋषियों एवं ज्ञान के जिज्ञासुओं को सप्रेम समर्पित है।", author_style))

    story.append(PageBreak())

    # -------------------------------------------------------------
    # 3. TABLE OF CONTENTS
    # -------------------------------------------------------------
    story.append(shaper.paragraph("ग्रंथ अनुक्रमणिका • Table of Contents", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#854d0e"), spaceAfter=12))

    toc_rows = [
        [shaper.paragraph("<b>प्रकरण</b>", table_header_style), shaper.paragraph("<b>विषय विवरण</b>", table_header_style)]
    ]
    toc_rows.append([
        shaper.paragraph("<b>वर्ण परिचय</b>", table_cell_style),
        shaper.paragraph("नवग्रह शास्त्रीय स्वरूप, वर्ण एवं प्रतीक चक्र", table_cell_style)
    ])

    for ch in chapters:
        toc_rows.append([
            shaper.paragraph(f"<b>भाग {ch.get('number', '')}</b>", table_cell_style),
            shaper.paragraph(f"<b>{ch.get('title', '')}</b><br/>{ch.get('english_title', '')}", table_cell_style)
        ])

    toc_table = Table(toc_rows, colWidths=[1.1 * inch, 3.8 * inch])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#fef3c7")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#78350f")),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(toc_table)

    story.append(PageBreak())

    # -------------------------------------------------------------
    # 4. NAVAGRAHA REFERENCE PLATE (FITS EXACTLY ON ONE PAGE)
    # -------------------------------------------------------------
    story.append(shaper.paragraph("नवग्रह शास्त्रीय स्वरूप, वर्ण एवं प्रतीक परिचय", ParagraphStyle(
        "NavH1", parent=base_styles["heading"], fontSize=13, leading=16, textColor=colors.HexColor("#78350f"), spaceAfter=3
    )))
    story.append(shaper.paragraph("बृहत्पाराशर होरा शास्त्र एवं फलदीपिका अनुसार नवग्रहों का खगोलीय स्वरूप, रत्न, धातु एवं मर्यादा", ParagraphStyle(
        "NavSub", parent=base_styles["body"], fontSize=8.2, leading=11, textColor=colors.HexColor("#854d0e"), spaceAfter=5
    )))
    story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#d97706"), spaceAfter=6))

    graha_catalog = [
        ("sun", "सूर्य (Sun)", "#b45309", "शास्त्रीय वर्ण: रक्त / ताम्रवर्ण", "अग्नि • तेजस", "माणिक्य • तांबा", "मेष 10° / तुला 10°", "आत्मा, पिता, राजसत्ता"),
        ("moon", "चन्द्र (Moon)", "#475569", "शास्त्रीय वर्ण: श्वेत / चन्द्रकान्ति", "वरुण • जल", "मोती • चांदी", "वृषभ 3° / वृश्चिक 3°", "मन, माता, मानसिक शांति"),
        ("mars", "मंगल (Mars)", "#b91c1c", "शास्त्रीय वर्ण: रक्तवर्ण (कुज)", "कार्तिकेय • अग्नि", "मूंगा • तांबा", "मकर 28° / कर्क 28°", "पराक्रम, भ्राता, शौर्य"),
        ("mercury", "बुध (Mercury)", "#047857", "शास्त्रीय वर्ण: हरित / श्याम", "विष्णु • पृथ्वी", "पन्ना • कांसा", "कन्या 15° / मीन 15°", "बुद्धि, वाणी, व्यापार"),
        ("jupiter", "गुरु (Jupiter)", "#a16207", "शास्त्रीय वर्ण: पीत / कनकवर्ण", "इन्द्र/ब्रह्मा • आकाश", "पुखराज • स्वर्ण", "कर्क 5° / मकर 5°", "ज्ञान, धर्म, संतान"),
        ("venus", "शुक्र (Venus)", "#be185d", "शास्त्रीय वर्ण: चित्र / शुभ्र श्वेत", "इंद्राणी • जल", "हीरा • चांदी", "मीन 27° / कन्या 27°", "प्रेम, ऐश्वर्य, कला"),
        ("saturn", "शनि (Saturn)", "#1e293b", "शास्त्रीय वर्ण: कृष्ण / नीलवर्ण", "यमराज • वायु", "नीलम • लोहा", "तुला 20° / मेष 20°", "कर्म, न्याय, वैराग्य"),
        ("rahu", "राहु (Rahu)", "#475569", "शास्त्रीय स्वरूप: धूम्रवर्ण (तम)", "सर्प • तमोगुण", "गोमेद • सीसा", "मिथुन / धनु", "कूटनीति, विदेश, पराक्रम"),
        ("ketu", "केतु (Ketu)", "#7c2d12", "शास्त्रीय स्वरूप: चित्र / धूम्रवर्ण", "चित्रगुप्त • तमोगुण", "लहसुनिया • मिश्र", "धनु / मिथुन", "मोक्ष, अंतर्ज्ञान, वैराग्य"),
        ("lagna", "लग्न (Ascendant)", "#0f766e", "शास्त्रीय स्वरूप: उदित लग्न", "पूर्व क्षितिज", "आत्मतत्त्व", "तनु भाव मर्यादा", "सम्पूर्ण कुण्डली का आधार")
    ]

    icon_dir = os.path.join(base_dir, "assets", "images", "planets", "48")

    graha_headers = ["ग्रह", "शास्त्रीय वर्ण / स्वरूप", "तत्व", "रत्न / धातु", "उच्च / नीच", "मुख्य कारकत्व"]
    graha_rows = [ [shaper.paragraph(f"<b>{h}</b>", table_header_style) for h in graha_headers] ]

    for key, name, hex_c, varna, tattva, ratna, uchha, karaka in graha_catalog:
        icon_p = os.path.join(icon_dir, f"{key}.png")
        img = Image(icon_p, width=11, height=11) if os.path.exists(icon_p) else None
        name_p = shaper.paragraph(f'<font color="{hex_c}"><b>{name}</b></font>', table_cell_style)
        planet_cell = [img, name_p] if img else [name_p]
        graha_rows.append([
            planet_cell,
            shaper.paragraph(varna, table_cell_style),
            shaper.paragraph(tattva, table_cell_style),
            shaper.paragraph(ratna, table_cell_style),
            shaper.paragraph(uchha, table_cell_style),
            shaper.paragraph(karaka, table_cell_style),
        ])

    col_widths = [1.05 * inch, 0.95 * inch, 0.65 * inch, 0.70 * inch, 0.75 * inch, 0.80 * inch]
    graha_table = Table(graha_rows, colWidths=col_widths)
    graha_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#fef3c7")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(graha_table)

    story.append(PageBreak())

    # -------------------------------------------------------------
    # 5. CHAPTER CONTENT PARSER
    # -------------------------------------------------------------
    def render_callout_box(title, text_lines, kind="shloka"):
        bg_color = colors.HexColor("#fffbeb")
        left_color = colors.HexColor("#d97706")
        border_color = colors.HexColor("#fde68a")
        title_color = colors.HexColor("#b45309")

        if kind == "formula":
            bg_color = colors.HexColor("#f0f9ff")
            left_color = colors.HexColor("#0284c7")
            border_color = colors.HexColor("#bae6fd")
            title_color = colors.HexColor("#0369a1")
        elif kind == "yoga":
            bg_color = colors.HexColor("#ecfdf5")
            left_color = colors.HexColor("#059669")
            border_color = colors.HexColor("#a7f3d0")
            title_color = colors.HexColor("#047857")
        elif kind == "warning":
            bg_color = colors.HexColor("#fff7ed")
            left_color = colors.HexColor("#ea580c")
            border_color = colors.HexColor("#fed7aa")
            title_color = colors.HexColor("#c2410c")

        c_title_style = ParagraphStyle(
            f"CallTitle_{kind}", parent=callout_title_style, textColor=title_color
        )

        inner = []
        if title:
            inner.append(shaper.paragraph(f"<b>{clean_markdown_inline(title)}</b>", c_title_style))

        if kind == "shloka":
            shloka_html = "<br/>".join(text_lines)
            inner.append(shaper.paragraph(shloka_html, verse_style))
        else:
            for l in text_lines:
                inner.append(shaper.paragraph(clean_markdown_inline(l), callout_body_style))

        t = Table([[inner]], colWidths=[4.9 * inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), bg_color),
            ('LINELEFT', (0, 0), (0, -1), 2.5, left_color),
            ('BOX', (0, 0), (-1, -1), 0.5, border_color),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        return t

    def render_markdown_table(table_lines):
        clean_lines = [l.strip() for l in table_lines if l.strip() and not re.match(r'^\|[\s\:\-\|]+$', l.strip())]
        if not clean_lines:
            return None

        parsed_rows = []
        for line in clean_lines:
            cols = [c.strip() for c in line.strip('|').split('|')]
            parsed_rows.append(cols)

        if not parsed_rows:
            return None

        num_cols = len(parsed_rows[0])
        total_width = 4.9 * inch
        # Heuristic col widths
        col_w = total_width / num_cols
        widths = [col_w] * num_cols
        if num_cols == 3:
            widths = [1.0 * inch, 1.2 * inch, 2.7 * inch]
        elif num_cols == 4:
            widths = [1.0 * inch, 0.9 * inch, 1.2 * inch, 1.8 * inch]
        elif num_cols == 5:
            widths = [0.8 * inch, 0.8 * inch, 1.0 * inch, 1.1 * inch, 1.2 * inch]

        t_rows = []
        for r_idx, row in enumerate(parsed_rows):
            is_hdr = (r_idx == 0)
            c_style = table_header_style if is_hdr else table_cell_style
            row_flowables = []
            for col_idx, cell in enumerate(row):
                cell_fmt = clean_markdown_inline(cell)
                if is_hdr:
                    cell_fmt = f"<b>{cell_fmt}</b>"
                row_flowables.append(shaper.paragraph(cell_fmt, c_style))
            # Pad if cols are mismatched
            while len(row_flowables) < num_cols:
                row_flowables.append(shaper.paragraph("", c_style))
            t_rows.append(row_flowables[:num_cols])

        t = Table(t_rows, colWidths=widths)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#fef3c7")),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ]))
        return t

    for ch in chapters:
        ch_title = ch.get("title", "")
        ch_num = ch.get("number", "")
        raw_text = ch.get("raw_text", "")

        story.append(shaper.paragraph(f"अध्याय {ch_num}: {ch_title}", h1_style))
        story.append(shaper.paragraph(clean_markdown_inline(ch.get("english_title", "")), subtitle_style))
        story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#ca8a04"), spaceAfter=10))

        lines = raw_text.split("\n")
        in_yaml = False
        in_custom_block = False
        block_kind = None
        block_title = ""
        block_lines = []

        in_table = False
        table_lines = []

        in_shloka = False
        shloka_lines = []

        for line in lines:
            s_line = line.strip()

            # Front-matter toggle
            if s_line.startswith("---"):
                in_yaml = not in_yaml
                continue
            if in_yaml:
                continue

            # End of custom block
            if in_custom_block:
                if s_line.startswith(":::"):
                    if block_kind == "chart":
                        chart_name = block_title.strip()
                        png_candidate = os.path.join(raster_dir, f"{chart_name}.png")
                        if os.path.exists(png_candidate):
                            story.append(Spacer(1, 4))
                            img = Image(png_candidate, width=3.3 * inch, height=3.55 * inch)
                            img.hAlign = 'CENTER'
                            story.append(img)
                            story.append(Spacer(1, 4))
                        if block_lines:
                            caption = " ".join([l.strip() for l in block_lines if l.strip()])
                            story.append(shaper.paragraph(clean_markdown_inline(f"<i>{caption}</i>"), caption_style))
                            story.append(Spacer(1, 6))
                    else:
                        box = render_callout_box(block_title, block_lines, block_kind)
                        if box:
                            story.append(box)
                            story.append(Spacer(1, 6))
                    in_custom_block = False
                    block_kind = None
                    block_title = ""
                    block_lines = []
                else:
                    block_lines.append(s_line)
                continue

            # Start of custom block
            if s_line.startswith(":::"):
                # Flush pending table or shloka
                if in_table:
                    t_flow = render_markdown_table(table_lines)
                    if t_flow:
                        story.append(t_flow)
                        story.append(Spacer(1, 6))
                    in_table = False
                    table_lines = []
                if in_shloka:
                    box = render_callout_box("", shloka_lines, "shloka")
                    story.append(box)
                    story.append(Spacer(1, 6))
                    in_shloka = False
                    shloka_lines = []

                # Parse ::: kind [title]
                match = re.match(r'^:::\s*(\w+)(?:\s*\[(.*?)\])?', s_line)
                if match:
                    block_kind = match.group(1).lower()
                    block_title = match.group(2) or ""
                    in_custom_block = True
                    block_lines = []
                continue

            # Table rows
            if s_line.startswith("|"):
                in_table = True
                table_lines.append(s_line)
                continue
            else:
                if in_table:
                    t_flow = render_markdown_table(table_lines)
                    if t_flow:
                        story.append(t_flow)
                        story.append(Spacer(1, 6))
                    in_table = False
                    table_lines = []

            # Blank lines
            if not s_line:
                if in_shloka:
                    box = render_callout_box("", shloka_lines, "shloka")
                    story.append(box)
                    story.append(Spacer(1, 6))
                    in_shloka = False
                    shloka_lines = []
                continue

            # Skip title duplicates
            if s_line.startswith("# अध्याय") or s_line.startswith("## Chapter"):
                continue

            # Headings
            if s_line.startswith("## "):
                h_text = clean_markdown_inline(s_line[3:].strip())
                story.append(shaper.paragraph(h_text, h2_style))
            elif s_line.startswith("### "):
                h_text = clean_markdown_inline(s_line[4:].strip())
                story.append(shaper.paragraph(h_text, h3_style))
            elif s_line.startswith("#### "):
                h_text = clean_markdown_inline(s_line[5:].strip())
                story.append(shaper.paragraph(h_text, h4_style))

            # Shlokas outside :::
            elif "॥" in s_line:
                clean_v = s_line.lstrip("> ").strip()
                in_shloka = True
                shloka_lines.append(clean_v)

            # Bullet items
            elif s_line.startswith("- ") or s_line.startswith("* "):
                if in_shloka:
                    box = render_callout_box("", shloka_lines, "shloka")
                    story.append(box)
                    story.append(Spacer(1, 6))
                    in_shloka = False
                    shloka_lines = []
                b_text = clean_markdown_inline(s_line[2:].strip())
                story.append(shaper.paragraph(f"•  {b_text}", bullet_style))

            # Numbered items
            elif re.match(r'^(?:\d+|[0-9]+)\.\s+', s_line):
                if in_shloka:
                    box = render_callout_box("", shloka_lines, "shloka")
                    story.append(box)
                    story.append(Spacer(1, 6))
                    in_shloka = False
                    shloka_lines = []
                l_text = clean_markdown_inline(s_line)
                story.append(shaper.paragraph(l_text, list_style))

            # Images
            elif s_line.startswith("![") or "<svg" in s_line:
                continue

            # Standard body paragraphs
            else:
                if in_shloka:
                    box = render_callout_box("", shloka_lines, "shloka")
                    story.append(box)
                    story.append(Spacer(1, 6))
                    in_shloka = False
                    shloka_lines = []

                p_text = clean_markdown_inline(s_line)
                story.append(shaper.paragraph(p_text, body_style))

        # Flush any trailing blocks
        if in_table:
            t_flow = render_markdown_table(table_lines)
            if t_flow:
                story.append(t_flow)
        if in_shloka:
            box = render_callout_box("", shloka_lines, "shloka")
            story.append(box)

        story.append(PageBreak())

    # -------------------------------------------------------------
    # 6. RUNNING HEADERS & FOOTERS (PAGES >= 4)
    # -------------------------------------------------------------
    def on_later_pages(canvas, document):
        if document.page <= 3:
            return

        canvas.saveState()
        # Running header
        canvas.setFont(shaper.font_name, 7.5)
        canvas.setFillColor(colors.HexColor("#854d0e"))
        canvas.drawString(0.55 * inch, 8.45 * inch, shaper.shape("तंत्र ज्ञान • वैदिक ज्योतिष महाग्रंथ"))
        canvas.drawRightString((6 - 0.55) * inch, 8.45 * inch, "Tantra Gyan Research Center")
        canvas.setStrokeColor(colors.HexColor("#ca8a04"))
        canvas.setLineWidth(0.5)
        canvas.line(0.55 * inch, 8.40 * inch, (6 - 0.55) * inch, 8.40 * inch)

        # Running footer
        canvas.setStrokeColor(colors.HexColor("#e2e8f0"))
        canvas.setLineWidth(0.5)
        canvas.line(0.55 * inch, 0.55 * inch, (6 - 0.55) * inch, 0.55 * inch)
        canvas.setFont(shaper.font_name, 8)
        canvas.setFillColor(colors.HexColor("#64748b"))
        page_txt = shaper.shape(f"— पृष्ठ {document.page} —")
        canvas.drawCentredString(3 * inch, 0.40 * inch, page_txt)
        canvas.restoreState()

    # Build the document
    doc.build(story, onLaterPages=on_later_pages)
    print(f"✓ Target 1C (ReportLab Devanagari) Complete: {output_pdf}")
    return output_pdf
