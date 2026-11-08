#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compiles Bhrigu Nandi Nadi: Karma-Samyojan Sutra into a colorful, publication-grade
Masterpiece Vector PDF using Vivliostyle CLI.
Replicates the vibrant Web View aesthetic with crisp SVG rendering.
"""

import os
import re
import subprocess
import time

BASE_DIR = "/Users/apple/Movies/ap/TantraGyan"
WEB_HTML = os.path.join(BASE_DIR, "bhrigu-nandi-nadi.html")
PRINT_HTML = os.path.join(BASE_DIR, "bhrigu-nandi-nadi-print.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "bhrigu-nandi-nadi-karma-samyojan.pdf")

def generate_print_html():
    with open(WEB_HTML, "r", encoding="utf-8") as f:
        web_content = f.read()

    # Extract all chapters from web_content
    ch_matches = re.findall(r'<section class="chapter-section" id="([^"]+)"[^>]*>(.*?)</section>', web_content, re.DOTALL)
    
    # CSS Paged Media stylesheet for Vivliostyle
    vivlio_css = """
    @import url("https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&family=Noto+Serif+Devanagari:wght@500;600;700;800;900&family=Poppins:wght@400;500;600;700;800&display=swap");

    @page {
      size: A4 portrait;
      margin-top: 18mm;
      margin-bottom: 20mm;
      margin-left: 18mm;
      margin-right: 18mm;
      @bottom-center {
        content: "— " counter(page) " —";
        font-family: 'Noto Serif Devanagari', serif;
        font-size: 8.5pt;
        font-weight: 700;
        color: #b45309;
      }
    }

    @page :left {
      @top-left {
        content: "भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र";
        font-family: 'Noto Sans Devanagari', sans-serif;
        font-size: 7.8pt;
        font-weight: 700;
        color: #b45309;
      }
      @top-right {
        content: "तंत्र ज्ञान शोध संस्थान • t.worldgyan.com";
        font-family: 'Poppins', sans-serif;
        font-size: 7.2pt;
        font-weight: 600;
        color: #64748b;
      }
    }

    @page :right {
      @top-left {
        content: string(ch-title);
        font-family: 'Noto Sans Devanagari', sans-serif;
        font-size: 7.8pt;
        font-weight: 700;
        color: #78350f;
      }
      @top-right {
        content: "ज्योतिषाचार्य आशुतोष कुमार चौबे";
        font-family: 'Noto Sans Devanagari', sans-serif;
        font-size: 7.8pt;
        font-weight: 600;
        color: #b45309;
      }
    }

    @page cover-page {
      margin: 0;
      @top-left { content: none; }
      @top-right { content: none; }
      @bottom-center { content: none; }
    }

    @page toc-page {
      @top-left { content: "अनुक्रमणिका • TABLE OF CONTENTS"; font-size: 8pt; color: #b45309; }
      @top-right { content: none; }
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Poppins', 'Noto Sans Devanagari', -apple-system, sans-serif;
      font-size: 9.5pt;
      line-height: 1.62;
      color: #1c1917;
      background-color: #ffffff;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }

    /* Grand Cover Page */
    .print-cover-sheet {
      page: cover-page;
      break-after: page;
      page-break-after: always;
      height: 297mm;
      width: 210mm;
      padding: 24mm 20mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      text-align: center;
      background: linear-gradient(135deg, #fdfbf7 0%, #fef3c7 40%, #e0e7ff 100%);
      border: 10mm solid #1e1b4b;
      position: relative;
    }

    .cover-top-emblem {
      margin-top: 8mm;
    }

    .cover-top-emblem img {
      width: 125px;
      height: 125px;
      filter: drop-shadow(0 4px 10px rgba(49,46,129,0.3));
    }

    .cover-title-group {
      margin: 6mm 0;
    }

    .cover-mantra-header {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 13pt;
      font-weight: 800;
      color: #312e81;
      margin-bottom: 4mm;
      letter-spacing: 0.05em;
    }

    .cover-main-title {
      font-family: 'Noto Serif Devanagari', 'Cinzel', serif;
      font-size: 26pt;
      font-weight: 900;
      color: #1e1b4b;
      line-height: 1.25;
      margin-bottom: 3.5mm;
      text-shadow: 0 1px 2px rgba(30,27,75,0.15);
    }

    .cover-sub-title {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 13.5pt;
      font-weight: 700;
      color: #b45309;
      line-height: 1.4;
      margin-bottom: 4mm;
    }

    .cover-en-title {
      font-family: 'Cinzel', serif;
      font-size: 10pt;
      font-weight: 700;
      color: #475569;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }

    .cover-divider {
      width: 60%;
      height: 2pt;
      background: linear-gradient(to right, transparent, #b45309, transparent);
      margin: 5mm auto;
    }

    .cover-meta-summary {
      font-size: 9pt;
      color: #334155;
      line-height: 1.6;
      max-width: 145mm;
      margin: 0 auto;
    }

    .cover-bottom-author-block {
      margin-bottom: 8mm;
      border-top: 1.5pt solid #818cf8;
      padding-top: 5mm;
      width: 85%;
    }

    .cover-author-title {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 15pt;
      font-weight: 900;
      color: #1e1b4b;
    }

    .cover-author-sub {
      font-size: 8.8pt;
      color: #475569;
      margin-top: 2mm;
    }

    /* Dedication Page */
    .print-dedication-sheet {
      break-after: page;
      page-break-after: always;
      padding: 25mm 15mm;
      text-align: center;
    }

    .dedication-box {
      background: #faf5ff;
      border: 1.5pt solid #7c3aed;
      border-radius: 8pt;
      padding: 12mm 15mm;
      margin: 20mm auto;
      max-width: 150mm;
      box-shadow: 0 4pt 15pt rgba(124,58,237,0.08);
    }

    /* Table of Contents */
    .print-toc-sheet {
      page: toc-page;
      break-after: page;
      page-break-after: always;
      padding-top: 5mm;
    }

    .toc-title {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 17pt;
      font-weight: 800;
      color: #1e1b4b;
      text-align: center;
      margin-bottom: 8mm;
      border-bottom: 2pt solid #818cf8;
      padding-bottom: 3mm;
    }

    .toc-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 3.5mm;
    }

    .toc-item a {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      text-decoration: none;
      color: #1e293b;
      font-size: 9.6pt;
    }

    .toc-item-title {
      font-weight: 700;
      color: #1e1b4b;
    }

    .toc-dots {
      flex-grow: 1;
      border-bottom: 1.2pt dotted #cbd5e1;
      margin: 0 3mm;
      height: 1pt;
    }

    .toc-item a::after {
      content: target-counter(attr(href), page);
      font-weight: 800;
      color: #b45309;
    }

    /* Chapter Structure */
    .print-chapter {
      break-before: page;
      page-break-before: always;
      margin-bottom: 10mm;
    }

    .chapter-header {
      border-bottom: 2pt solid #ca8a04;
      padding-bottom: 3.5mm;
      margin-bottom: 5mm;
    }

    .chapter-num {
      display: inline-block;
      font-size: 8pt;
      font-weight: 800;
      color: #b45309;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 1.5mm;
    }

    .chapter-title {
      string-set: ch-title content();
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 16pt;
      font-weight: 900;
      color: #78350f;
      line-height: 1.3;
    }

    .chapter-title-en {
      font-size: 9pt;
      font-weight: 600;
      color: #64748b;
      margin-top: 1.5mm;
    }

    p {
      margin-bottom: 2.8mm;
      text-align: justify;
      word-break: normal;
    }

    /* Rule Cards */
    .rule-card {
      background: #fffdf8;
      border: 1pt solid #fed7aa;
      border-left: 4.5pt solid #b45309;
      border-radius: 4pt;
      padding: 3mm 4mm;
      margin-bottom: 3.5mm;
      break-inside: avoid;
      page-break-inside: avoid;
      font-size: 9.2pt;
    }

    .rule-title {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 10.2pt;
      font-weight: 800;
      color: #78350f;
      margin-bottom: 1.5mm;
    }

    .rule-body {
      color: #1e293b;
      line-height: 1.55;
    }

    /* Diagram / Visual Plate Container */
    .chart-embed-box {
      margin: 5mm 0;
      text-align: center;
      background: #ffffff;
      border: 1pt solid #cbd5e1;
      border-radius: 6pt;
      padding: 4mm;
      break-inside: avoid;
      page-break-inside: avoid;
      box-shadow: 0 2pt 8pt rgba(0,0,0,0.06);
    }

    .chart-embed-img {
      width: 100%;
      max-width: 155mm;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .chart-caption {
      margin-top: 2.5mm;
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 8.8pt;
      font-weight: 800;
      color: #78350f;
    }

    .chart-sub-caption {
      font-size: 7.6pt;
      color: #64748b;
      margin-top: 1mm;
      font-style: italic;
    }

    /* Tables */
    .table-title-bar {
      background: #fef3c7;
      border: 1pt solid #cbd5e1;
      border-bottom: none;
      border-radius: 4pt 4pt 0 0;
      padding: 2.5mm 3.5mm;
      margin-top: 4mm;
      break-inside: avoid;
      page-break-inside: avoid;
      break-after: avoid;
      page-break-after: avoid;
    }

    .table-title-bar h4 {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 9.5pt;
      font-weight: 800;
      color: #78350f;
    }

    .styled-table-wrap {
      width: 100%;
      border: 1pt solid #cbd5e1;
      border-radius: 0 0 4pt 4pt;
      margin-bottom: 4mm;
      break-inside: avoid;
      page-break-inside: avoid;
    }

    table.bnn-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8pt;
      line-height: 1.35;
    }

    table.bnn-table th {
      background: #fef3c7;
      color: #78350f;
      font-family: 'Noto Serif Devanagari', serif;
      font-weight: 800;
      padding: 2mm 2.5mm;
      border: 0.5pt solid #cbd5e1;
      border-bottom: 1.5pt solid #ca8a04;
    }

    table.bnn-table td {
      padding: 1.8mm 2.5mm;
      border: 0.5pt solid #cbd5e1;
      vertical-align: middle;
      color: #1e293b;
    }

    table.bnn-table tr:nth-child(even) td {
      background-color: #fafaf9;
    }

    /* Badges */
    .planet-badge {
      display: inline-block;
      font-weight: 700;
      border-radius: 2pt;
      padding: 0.2pt 3pt;
      font-size: 0.88em;
      white-space: nowrap;
    }

    .badge-exalted { background: #dcfce7; color: #15803d; border: 0.5pt solid #22c55e; }
    .badge-debilitated { background: #fee2e2; color: #b91c1c; border: 0.5pt solid #ef4444; }
    .badge-mooltrikona { background: #fef3c7; color: #a16207; border: 0.5pt solid #f59e0b; }
    .badge-friendly { background: #eff6ff; color: #1d4ed8; border: 0.5pt solid #3b82f6; }
    .badge-enemy { background: #fdf2f8; color: #be185d; border: 0.5pt solid #ec4899; }
    """

    # Assemble complete HTML
    html_out = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="utf-8">
  <title>भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र • Vivliostyle Masterpiece Edition</title>
  <style>
{vivlio_css}
  </style>
</head>
<body>

  <!-- FRONT COVER PAGE -->
  <section class="print-cover-sheet" id="cover">
    <div class="cover-top-emblem">
      <div style="font-size:1.8rem; margin-bottom:2mm;">☸ 📜 ⚜</div>
      <img src="assets/yantra.svg" alt="Sacred Sri Yantra Emblem">
    </div>

    <div class="cover-title-group">
      <div class="cover-mantra-header">॥ नमस्तस्मै मुनीन्द्राय भृगवे ज्ञानरूपिणे ॥</div>
      <h1 class="cover-main-title">भृगु नंदी नाड़ी: कर्म-संयोजन सूत्र</h1>
      <div class="cover-sub-title">Bhrigu Nandi Nadi: Karma-Samyojan Sutra</div>
      <div class="cover-en-title">Classical Nadi Astrology • Conjunctions, Directions & Transit Formulas</div>
      <div class="cover-divider"></div>
      <p class="cover-meta-summary">
        महर्षि भृगु एवं नंदीश्वर द्वारा प्रतिपादित प्राचीन नाड़ी ज्योतिष का प्रामाणिक, वैज्ञानिक एवं सुस्पष्ट निरूपण। ग्रह-संयोग, दिशा-आधारित 1-5-9 त्रिकोण दृष्टि, जीव-कर्म कारक संबंध, 18 डायमंड चार्ट्स, 16 शास्त्रीय सारणियां व गोचर सूत्र।
      </p>
    </div>

    <div class="cover-bottom-author-block">
      <div class="cover-author-title">ज्योतिषाचार्य आशुतोष कुमार चौबे</div>
      <div class="cover-author-sub">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) • 2026</div>
      <div style="font-size:8pt; color:#64748b; margin-top:1.5mm;">आधिकारिक शोध मंच: https://t.worldgyan.com • सर्वाधिकार सुरक्षित</div>
    </div>
  </section>

  <!-- DEDICATION & MANGALACHARAN -->
  <section class="print-dedication-sheet" id="dedication">
    <div style="font-size:2rem; margin-bottom:5mm;">☸ 🔱 📜</div>
    <div class="dedication-box">
      <div style="font-family:'Noto Serif Devanagari',serif; font-size:13pt; font-weight:700; color:#4c1d95; line-height:1.9;">
        ॥ नमस्तस्मै मुनीन्द्राय भृगवे ज्ञानरूपिणे ।<br>
        येन नाडी-प्रदीपेन दृश्यते भुवनत्रयम् ॥<br><br>
        ॥ नन्दीश्वरं महाप्राज्ञं कर्म-संयोजन-प्रभुम् ।<br>
        नमामि ज्ञान-दातारं काल-चक्र-प्रवर्तकम् ॥
      </div>
      <div style="width:40%; height:1.5pt; background:#818cf8; margin:5mm auto;"></div>
      <p style="font-size:9.5pt; color:#1e293b; line-height:1.75; text-align:center;">
        यह ग्रंथ पंडित आर. जी. राव (Pandit R.G. Rao) द्वारा 1950 के दशक में संहिताबद्ध भृगु नंदी नाड़ी (BNN) पद्धति के समस्त मूल सूत्रों, 18 डायमंड चार्ट्स, 16 बृहत् सारणियों और अचूक फलित भविष्यवाणियों का एक संपूर्ण प्रामाणिक संदर्भ-ग्रंथ है।
      </p>
    </div>
  </section>

  <!-- TABLE OF CONTENTS -->
  <section class="print-toc-sheet" id="toc">
    <h2 class="toc-title">ग्रंथ अनुक्रमणिका • Table of Contents</h2>
    <ul class="toc-list">
      <li class="toc-item"><a href="#ch1"><span class="toc-item-title">अध्याय 1: भृगु नंदी नाड़ी के मूल सिद्धांत एवं व्याकरण</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch2"><span class="toc-item-title">अध्याय 2: दिशा-आधारित दृष्टि एवं 1-5-9 त्रिकोण संबंध</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch3"><span class="toc-item-title">अध्याय 3: जीव कारक (गुरु) एवं कर्म कारक (शनि) फलित</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch4"><span class="toc-item-title">अध्याय 4: ग्रह-संयोग एवं युति सूत्र (Planetary Combinations)</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch5"><span class="toc-item-title">अध्याय 5: त्रि-ग्रह संयोग एवं विशिष्ट नाड़ी राजयोग</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch6"><span class="toc-item-title">अध्याय 6: नाड़ी विवाह एवं दाम्पत्य जीवन फलित</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch7"><span class="toc-item-title">अध्याय 7: प्रगति, गोचर एवं भृगु बिंदु काल-निर्धारण</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch8"><span class="toc-item-title">अध्याय 8: 7-चरणीय बी.एन.एन. फलित निर्णय प्रवाह</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#author"><span class="toc-item-title">उपसंहार: लेखक परिचय एवं संदर्भ</span><span class="toc-dots"></span></a></li>
    </ul>
  </section>
"""

    # Append all chapters
    for ch_id, ch_body in ch_matches:
        html_out += f"""
  <section class="print-chapter" id="{ch_id}">
    {ch_body}
  </section>
"""

    html_out += """
</body>
</html>
"""
    with open(PRINT_HTML, "w", encoding="utf-8") as f:
        f.write(html_out.strip())
    print(f"✅ Generated {PRINT_HTML} ({os.path.getsize(PRINT_HTML):,} bytes)")

def compile_pdf():
    print(f"\n🚀 Running Vivliostyle build for Bhrigu Nandi Nadi...")
    cmd = [
        "vivliostyle",
        "build",
        PRINT_HTML,
        "-s", "A4",
        "-o", OUTPUT_PDF,
        "--timeout", "300"
    ]
    t0 = time.time()
    subprocess.run(cmd, check=True)
    dur = time.time() - t0
    size_mb = os.path.getsize(OUTPUT_PDF) / (1024 * 1024)
    print(f"🎉 Vivliostyle Build Succeeded!")
    print(f"   Output: {OUTPUT_PDF}")
    print(f"   Size: {size_mb:.2f} MB | Time: {dur:.2f}s")

if __name__ == "__main__":
    generate_print_html()
    compile_pdf()

