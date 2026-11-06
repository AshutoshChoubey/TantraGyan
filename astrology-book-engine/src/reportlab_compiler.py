#!/usr/bin/env python3
"""
ReportLab + Devanagari Shaper Publication Compiler
==================================================
Compiles the Tantra Gyan Vedic Astrology Manuscript into a print-ready PDF
using ReportLab and HarfBuzz visual-order Devanagari shaping (devanagari-reportlab).
"""

import os
import re
from devanagari_reportlab import Shaper
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.pagesizes import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle


def compile_reportlab_book(metadata, chapters, output_pdf, base_dir):
    """
    Compiles manuscript chapters into a publication-grade PDF with devanagari-reportlab.
    """
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

    # Standard trade paperback 6 x 9 inches
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=(6 * inch, 9 * inch),
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch
    )

    shaper = Shaper()
    base_styles = shaper.styles(body_size=10)

    # Custom styles
    title_style = ParagraphStyle(
        "GrandTitle",
        parent=base_styles["title"],
        fontSize=20,
        leading=26,
        textColor=colors.HexColor("#78350f"),
        alignment=1, # Center
        spaceAfter=12
    )

    subtitle_style = ParagraphStyle(
        "GrandSubtitle",
        parent=base_styles["heading"],
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#854d0e"),
        alignment=1,
        spaceAfter=16
    )

    author_style = ParagraphStyle(
        "AuthorStyle",
        parent=base_styles["body"],
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#1e293b"),
        alignment=1,
        spaceAfter=8
    )

    verse_style = ParagraphStyle(
        "MangalaVerse",
        parent=base_styles["quote"],
        fontSize=11,
        leading=18,
        textColor=colors.HexColor("#78350f"),
        alignment=1,
        spaceBefore=14,
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        "ChapterH1",
        parent=base_styles["heading"],
        fontSize=15,
        leading=20,
        textColor=colors.HexColor("#78350f"),
        spaceBefore=16,
        spaceAfter=10,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        "SectionH2",
        parent=base_styles["heading"],
        fontSize=12,
        leading=17,
        textColor=colors.HexColor("#854d0e"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        "BookBody",
        parent=base_styles["body"],
        fontSize=9.5,
        leading=14.5,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=7
    )

    callout_style = ParagraphStyle(
        "CalloutText",
        parent=base_styles["body"],
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor("#78350f"),
        spaceBefore=4,
        spaceAfter=4
    )

    story = []

    # -------------------------------------------------------------
    # 1. GRAND TITLE PAGE
    # -------------------------------------------------------------
    story.append(Spacer(1, 0.4 * inch))
    story.append(shaper.paragraph(metadata.get("title", ""), title_style))
    story.append(shaper.paragraph(metadata.get("english_title", ""), subtitle_style))
    story.append(Spacer(1, 0.2 * inch))
    story.append(shaper.paragraph(metadata.get("subtitle", ""), body_style))
    story.append(Spacer(1, 0.4 * inch))

    story.append(shaper.paragraph(f"<b>ग्रंथकार:</b> {metadata.get('author_hindi')} ({metadata.get('author')})", author_style))
    story.append(shaper.paragraph(metadata.get("author_title", ""), author_style))
    story.append(Spacer(1, 0.3 * inch))

    story.append(HRFlowable(width="80%", thickness=0.8, color=colors.HexColor("#ca8a04"), spaceAfter=15))
    story.append(shaper.paragraph(f"{metadata.get('publisher')} • {metadata.get('edition')}", author_style))
    story.append(shaper.paragraph(f"{metadata.get('website')} • {metadata.get('youtube')}", author_style))

    story.append(PageBreak())

    # -------------------------------------------------------------
    # 2. COPYRIGHT & MANGALACHARAN
    # -------------------------------------------------------------
    story.append(shaper.paragraph("<b>वैधानिक सूचना एवं सर्वाधिकार</b>", h2_style))
    story.append(shaper.paragraph(metadata.get("copyright", ""), body_style))
    story.append(shaper.paragraph(f"ISBN: {metadata.get('isbn')} • प्रकाशन वर्ष: {metadata.get('year')}", body_style))
    story.append(shaper.paragraph(f"प्रकाशक: {metadata.get('publisher')}", body_style))
    story.append(Spacer(1, 0.3 * inch))

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
        [shaper.paragraph("<b>प्रकरण</b>", body_style), shaper.paragraph("<b>विषय विवरण</b>", body_style)]
    ]
    toc_rows.append([
        shaper.paragraph("<b>वर्ण परिचय</b>", body_style),
        shaper.paragraph("नवग्रह शास्त्रीय स्वरूप, वर्ण एवं प्रतीक चक्र", body_style)
    ])

    for ch in chapters:
        toc_rows.append([
            shaper.paragraph(f"<b>भाग {ch.get('number', '')}</b>", body_style),
            shaper.paragraph(f"<b>{ch.get('title', '')}</b><br/>{ch.get('english_title', '')}", body_style)
        ])

    toc_table = Table(toc_rows, colWidths=[1.2 * inch, 3.5 * inch])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#fef3c7")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#78350f")),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
    ]))
    story.append(toc_table)

    story.append(PageBreak())

    # -------------------------------------------------------------
    # 4. DEDICATED NAVAGRAHA REFERENCE PLATE
    # -------------------------------------------------------------
    story.append(shaper.paragraph("नवग्रह शास्त्रीय स्वरूप, वर्ण एवं प्रतीक परिचय", h1_style))
    story.append(shaper.paragraph("बृहत्पाराशर होरा शास्त्र एवं फलदीपिका अनुसार नवग्रहों का खगोलीय स्वरूप, रत्न, धातु एवं मर्यादा", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#d97706"), spaceAfter=10))

    graha_catalog = [
        ("सूर्य (Sun)", "शास्त्रीय वर्ण: रक्त / ताम्रवर्ण", "अग्नि • तेजस", "माणिक्य • तांबा", "मेष १०° / तुला १०°", "आत्मा, पिता, राजसत्ता"),
        ("चन्द्र (Moon)", "शास्त्रीय वर्ण: श्वेत / चन्द्रकान्ति", "वरुण • जल", "मोती • चांदी", "वृषभ ३° / वृश्चिक ३°", "मन, माता, मानसिक शांति"),
        ("मंगल (Mars)", "शास्त्रीय वर्ण: रक्तवर्ण (कुज)", "कार्तिकेय • अग्नि", "मूंगा • तांबा", "मकर २८° / कर्क २८°", "पराक्रम, भ्राता, शौर्य"),
        ("बुध (Mercury)", "शास्त्रीय वर्ण: हरित / श्याम", "विष्णु • पृथ्वी", "पन्ना • कांसा", "कन्या १५° / मीन १५°", "बुद्धि, वाणी, व्यापार"),
        ("गुरु (Jupiter)", "शास्त्रीय वर्ण: पीत / कनकवर्ण", "इन्द्र/ब्रह्मा • आकाश", "पुखराज • स्वर्ण", "कर्क ५° / मकर ५°", "ज्ञान, धर्म, संतान"),
        ("शुक्र (Venus)", "शास्त्रीय वर्ण: चित्र / शुभ्र श्वेत", "इंद्राणी • जल", "हीरा • चांदी", "मीन २७° / कन्या २७°", "प्रेम, ऐश्वर्य, कला"),
        ("शनि (Saturn)", "शास्त्रीय वर्ण: कृष्ण / नीलवर्ण", "यमराज • वायु", "नीलम • लोहा", "तुला २०° / मेष २०°", "कर्म, न्याय, वैराग्य"),
        ("राहु (Rahu)", "शास्त्रीय स्वरूप: धूम्रवर्ण (तम)", "सर्प • तमोगुण", "गोमेद • सीसा", "मिथुन / धनु", "कूटनीति, विदेश, पराक्रम"),
        ("केतु (Ketu)", "शास्त्रीय स्वरूप: चित्र / धूम्रवर्ण", "चित्रगुप्त • तमोगुण", "लहसुनिया • मिश्र धातु", "धनु / मिथुन", "मोक्ष, अंतर्ज्ञान, वैराग्य"),
        ("लग्न (Ascendant)", "शास्त्रीय स्वरूप: उदित लग्न", "पूर्व क्षितिज", "आत्मतत्त्व", "तनु भाव मर्यादा", "सम्पूर्ण कुण्डली का आधार")
    ]

    graha_rows = [
        [
            shaper.paragraph("<b>ग्रह</b>", body_style),
            shaper.paragraph("<b>शास्त्रीय वर्ण / स्वरूप</b>", body_style),
            shaper.paragraph("<b>तत्व</b>", body_style),
            shaper.paragraph("<b>रत्न / धातु</b>", body_style),
            shaper.paragraph("<b>उच्च / नीच</b>", body_style),
            shaper.paragraph("<b>मुख्य कारकत्व</b>", body_style),
        ]
    ]

    for g in graha_catalog:
        graha_rows.append([
            shaper.paragraph(f"<b>{g[0]}</b>", body_style),
            shaper.paragraph(g[1], body_style),
            shaper.paragraph(g[2], body_style),
            shaper.paragraph(g[3], body_style),
            shaper.paragraph(g[4], body_style),
            shaper.paragraph(g[5], body_style),
        ])

    graha_table = Table(graha_rows, colWidths=[0.85 * inch, 0.95 * inch, 0.65 * inch, 0.75 * inch, 0.75 * inch, 0.75 * inch])
    graha_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#fef3c7")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#78350f")),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(graha_table)

    story.append(PageBreak())

    # -------------------------------------------------------------
    # 5. CHAPTER CONTENT
    # -------------------------------------------------------------
    for ch in chapters:
        ch_title = ch.get("title", "")
        ch_num = ch.get("number", "")
        raw_text = ch.get("raw_text", "")

        story.append(shaper.paragraph(f"अध्याय {ch_num}: {ch_title}", h1_style))
        story.append(shaper.paragraph(ch.get("english_title", ""), subtitle_style))
        story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#ca8a04"), spaceAfter=12))

        # Parse chapter lines into reportlab flowables
        lines = raw_text.split("\n")
        in_shloka = False
        shloka_buffer = []

        for line in lines:
            s_line = line.strip()
            if not s_line:
                if shloka_buffer:
                    verse_text = "<br/>".join(shloka_buffer)
                    story.append(shaper.paragraph(verse_text, verse_style))
                    shloka_buffer = []
                    in_shloka = False
                continue

            # Front-matter YAML skip
            if s_line.startswith("---") or s_line.startswith("title:") or s_line.startswith("chapter:"):
                continue

            # Headings
            if s_line.startswith("## "):
                h_text = s_line[3:].strip()
                story.append(shaper.paragraph(h_text, h2_style))
            elif s_line.startswith("### "):
                h_text = s_line[4:].strip()
                story.append(shaper.paragraph(f"<b>{h_text}</b>", body_style))
            # Shlokas
            elif "॥" in s_line or s_line.startswith(">"):
                clean_v = s_line.lstrip("> ").strip()
                shloka_buffer.append(clean_v)
            # Callout block
            elif s_line.startswith("[!") or s_line.startswith(":::") or s_line.startswith("> [!"):
                continue
            # Markdown charts / images
            elif s_line.startswith("![") or "<svg" in s_line:
                continue
            # Tables: skip raw pipes, let text flow
            elif s_line.startswith("|"):
                continue
            else:
                if shloka_buffer:
                    verse_text = "<br/>".join(shloka_buffer)
                    story.append(shaper.paragraph(verse_text, verse_style))
                    shloka_buffer = []

                # Format bold markers
                formatted = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', s_line)
                story.append(shaper.paragraph(formatted, body_style))

        if shloka_buffer:
            verse_text = "<br/>".join(shloka_buffer)
            story.append(shaper.paragraph(verse_text, verse_style))

        story.append(PageBreak())

    # Build the document
    doc.build(story)
    print(f"✓ Target 1C (ReportLab Devanagari) Complete: {output_pdf}")
    return output_pdf
