#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the complete Flagship Vol 4 suite for Tantra Gyan:
1. kundali-ganita-reader.html (108-Page 3D Digital Interactive Flipbook Reader)
2. kundali-ganita.html (Complete Responsive Web Presentation Edition - 0% Python code, 100% Hindi formulas)
3. kundali-ganita-print.html (Print & PDF Generation Source)
4. kundali-ganita-vichar-mahagranth.pdf (100+ Page Vector PDF compiled via Chrome Headless)

Title: वैदिक कुण्डली विचार एवं गणित महाग्रंथ: खगोलीय सूत्र, 16 वर्ग चक्र एवं फलित संयोजन
English: The Cosmic Algorithm: Vedic Horoscope Mathematics & Destiny Decoded
Author: ज्योतिषाचार्य आशुतोष कुमार चौबे
Tantra Gyan Research Center • https://t.worldgyan.com
"""

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/apple/Movies/ap/TantraGyan")
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

READER_TEMPLATE_SRC = PROJECT_ROOT / "reader.html"
OUTPUT_READER = PROJECT_ROOT / "kundali-ganita-reader.html"
OUTPUT_WEB = PROJECT_ROOT / "kundali-ganita.html"
OUTPUT_PRINT = PROJECT_ROOT / "kundali-ganita-print.html"
OUTPUT_PDF = PROJECT_ROOT / "kundali-ganita-vichar-mahagranth.pdf"

from generate_108_pages import get_all_108_pages
from build_exhaustive_kundali_ganita_content import build_master_publications

def build_pages():
    """Returns the complete set of 108 sacred pages."""
    return get_all_108_pages()

def main():
    print("=" * 80)
    print("🕉️ Building Flagship Vol 4: वैदिक कुण्डली विचार एवं गणित महाग्रंथ (108-Page Master Suite)")
    print("=" * 80)

    pages_list = build_pages()
    print(f"Generated {len(pages_list)} rich pages for Kundali Ganita Vichar Mahagranth.")

    # 1. Assemble kundali-ganita-reader.html using exact structure from reader.html
    with open(READER_TEMPLATE_SRC, "r", encoding="utf-8") as f:
        template_lines = f.readlines()

    first_art_idx = next(i for i, l in enumerate(template_lines) if '<article class="book-page-data"' in l)
    last_art_idx = next(i for i in range(len(template_lines)-1, -1, -1) if '</article>' in template_lines[i])

    reader_top = "".join(template_lines[:first_art_idx])
    reader_bot = "".join(template_lines[last_art_idx+1:])

    # Customize reader top metadata
    reader_top = reader_top.replace("Ashutosh: 28 Oct 1994", "जातक 'क' (Benchmark Case Study): 28 Oct 1994")
    reader_top = reader_top.replace("Native Ashutosh", "जातक 'क' (Benchmark Native)")
    reader_top = reader_top.replace(
        "<title>वैदिक ज्योतिष महाग्रंथ सरलीकृत | Complete Vedic Astrology Compendium Simplified</title>",
        "<title>वैदिक कुण्डली विचार एवं गणित महाग्रंथ (3D फ्लिप बुक) • The Cosmic Algorithm 3D Reader</title>"
    )
    reader_top = reader_top.replace(
        'title="वैदिक ज्योतिष महाग्रंथ मुखपृष्ठ"',
        'title="वैदिक कुण्डली विचार एवं गणित महाग्रंथ"'
    )
    reader_top = reader_top.replace(
        'तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ',
        'वैदिक कुण्डली विचार एवं गणित महाग्रंथ (The Cosmic Algorithm)'
    )
    reader_top = reader_top.replace('p > 88', 'p > 108')
    reader_top = reader_top.replace('p > 40', 'p > 108')
    reader_top = reader_top.replace("localStorage.getItem('tantra_book_page')", "localStorage.getItem('tantra_ganita_flip_page')")
    reader_top = reader_top.replace("localStorage.setItem('tantra_book_page'", "localStorage.setItem('tantra_ganita_flip_page'")
    reader_top = reader_top.replace('max="100"', 'max="108"')
    reader_top = reader_top.replace('max="40"', 'max="108"')
    reader_top = reader_top.replace('href="astrology-book-engine/dist/web/index.html"', 'href="kundali-ganita.html"')
    reader_top = reader_top.replace('href="tantra-gyan-vedic-jyotish-mahagranth.pdf"', 'href="kundali-ganita-vichar-mahagranth.pdf"')
    reader_top = reader_top.replace('download="Tantra-Gyan-Vedic-Jyotish-Maha-Granth.pdf"', 'download="Kundali-Ganita-Vichar-Mahagranth.pdf"')
    reader_top = reader_top.replace("Page 1 of 100", "Page 1 of 108")
    reader_top = reader_top.replace("Page 1 of 40", "Page 1 of 108")

    # Inject prominent navigation buttons into the 3D Reader header
    custom_nav = '''
      <div style="display:flex; align-items:center; gap:0.5rem; margin-left:auto;">
        <a href="kundali-ganita.html" class="reader-nav-btn" title="सम्पूर्ण वेब संस्करण पढ़ें" style="background:#059669; color:#fff; padding:0.35rem 0.85rem; border-radius:6px; font-size:0.78rem; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.3rem;">🌐 वेब संस्करण</a>
        <a href="kundali-ganita-vichar-mahagranth.pdf" class="reader-nav-btn" download title="मास्टर PDF डाउनलोड करें" style="background:#0284c7; color:#fff; padding:0.35rem 0.85rem; border-radius:6px; font-size:0.78rem; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.3rem;">📥 मास्टर PDF</a>
        <a href="media/concept_animations/3d_ephemeris_simulation.html" target="_blank" class="reader-nav-btn" title="3D खगोलीय सिमुलेशन" style="background:rgba(255,255,255,0.12); color:#e2e8f0; border:1px solid #10b981; padding:0.35rem 0.85rem; border-radius:6px; font-size:0.78rem; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.3rem;">🌌 3D सिमुलेशन</a>
      </div>
'''
    if '<button id="btn-toggle-sound"' in reader_top:
        reader_top = reader_top.replace('<button id="btn-toggle-sound"', custom_nav + '\n      <button id="btn-toggle-sound"')

    # Write out kundali-ganita-reader.html
    with open(OUTPUT_READER, "w", encoding="utf-8") as f:
        f.write(reader_top)
        for p in pages_list:
            f.write(p)
        f.write(reader_bot)

    print(f"✓ Created 3D Interactive Flipbook Reader: {OUTPUT_READER}")

    # 2. Build Massive Web Presentation Edition, Print Media Layout & Vector PDF
    build_master_publications(
        output_web=OUTPUT_WEB,
        output_print=OUTPUT_PRINT,
        output_pdf=OUTPUT_PDF,
        output_reader=OUTPUT_READER,
        reader_src=READER_TEMPLATE_SRC,
        pages_list=pages_list
    )

    print("=" * 80)
    print("🎉 Flagship Vol 4 Exhaustive 108-Page Suite Successfully Completed!")
    print("=" * 80)

if __name__ == "__main__":
    main()
