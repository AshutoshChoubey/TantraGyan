#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compiles Tantra Sadhana Siddhi Mahagranth into a colorful, publication-grade
Masterpiece Vector PDF using Vivliostyle CLI.
Replicates the vibrant Web View aesthetic with crisp SVG rendering.
"""

import os
import re
import subprocess
import time

BASE_DIR = "/Users/apple/Movies/ap/TantraGyan"
WEB_HTML = os.path.join(BASE_DIR, "tantra-sadhana-siddhi.html")
PRINT_HTML = os.path.join(BASE_DIR, "tantra-sadhana-print.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "tantra-sadhana-siddhi-protocol.pdf")

def generate_print_html():
    with open(WEB_HTML, "r", encoding="utf-8") as f:
        web_content = f.read()

    # Extract all chapters from web_content
    ch_matches = re.findall(r'<section class="chapter-section" id="([^"]+)">(.*?)</section>', web_content, re.DOTALL)
    
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
        content: "तंत्र साधना सिद्धि महाग्रंथ";
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
      font-size: 9.8pt;
      line-height: 1.65;
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
      background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 40%, #ffedd5 100%);
      border: 10mm solid #78350f;
      position: relative;
    }

    .cover-top-emblem {
      margin-top: 10mm;
    }

    .cover-top-emblem img {
      width: 125px;
      height: 125px;
      filter: drop-shadow(0 4px 10px rgba(180,83,9,0.3));
    }

    .cover-title-group {
      margin: 8mm 0;
    }

    .cover-mantra-header {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 13pt;
      font-weight: 800;
      color: #991b1b;
      margin-bottom: 5mm;
      letter-spacing: 0.05em;
    }

    .cover-main-title {
      font-family: 'Noto Serif Devanagari', 'Cinzel', serif;
      font-size: 26pt;
      font-weight: 900;
      color: #78350f;
      line-height: 1.25;
      margin-bottom: 4mm;
      text-shadow: 0 1px 2px rgba(120,53,15,0.15);
    }

    .cover-sub-title {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 13.5pt;
      font-weight: 700;
      color: #b45309;
      line-height: 1.4;
      margin-bottom: 5mm;
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
      margin: 6mm auto;
    }

    .cover-meta-summary {
      font-size: 9pt;
      color: #334155;
      line-height: 1.6;
      max-width: 140mm;
      margin: 0 auto;
    }

    .cover-bottom-author-block {
      margin-bottom: 10mm;
      border-top: 1.5pt solid #ca8a04;
      padding-top: 6mm;
      width: 85%;
    }

    .cover-author-title {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 15pt;
      font-weight: 900;
      color: #78350f;
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
      background: #fffdf5;
      border: 1.5pt solid #b45309;
      border-radius: 8pt;
      padding: 12mm 15mm;
      margin: 20mm auto;
      max-width: 150mm;
      box-shadow: 0 4pt 15pt rgba(180,83,9,0.08);
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
      color: #78350f;
      text-align: center;
      margin-bottom: 8mm;
      border-bottom: 2pt solid #ca8a04;
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
      color: #78350f;
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

    .chapter-subtitle {
      font-size: 9pt;
      font-weight: 600;
      color: #64748b;
      margin-top: 1.5mm;
    }

    /* Headings */
    h3.subhead {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 11.5pt;
      font-weight: 800;
      color: #b45309;
      margin: 5mm 0 2.5mm;
      border-left: 3.5pt solid #b45309;
      padding-left: 2.5mm;
      break-after: avoid;
      page-break-after: avoid;
    }

    h4.subhead-small {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 10pt;
      font-weight: 700;
      color: #991b1b;
      margin: 3.5mm 0 1.5mm;
      break-after: avoid;
      page-break-after: avoid;
    }

    p {
      margin-bottom: 2.8mm;
      text-align: justify;
      word-break: normal;
    }

    /* Sanskrit Mantra Cards */
    .mantra-box {
      background: linear-gradient(135deg, #fffdf8, #fffbeb);
      border: 1.5pt solid #d97706;
      border-left: 4.5pt solid #b45309;
      border-radius: 4pt;
      padding: 4mm 5mm;
      margin: 4.5mm 0;
      text-align: center;
      break-inside: avoid;
      page-break-inside: avoid;
    }

    .mantra-sanskrit {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 11pt;
      font-weight: 700;
      color: #991b1b;
      line-height: 1.8;
      margin-bottom: 2mm;
    }

    .mantra-meaning {
      font-size: 8.5pt;
      color: #57534e;
      line-height: 1.55;
      font-style: italic;
    }

    /* Rule / Info Cards */
    .rule-card {
      border-left: 3.5pt solid #b45309;
      background: #fffdf5;
      border-top: 0.5pt solid #fed7aa;
      border-right: 0.5pt solid #fed7aa;
      border-bottom: 0.5pt solid #fed7aa;
      border-radius: 0 4pt 4pt 0;
      padding: 3.5mm 4.5mm;
      margin: 4mm 0;
      break-inside: avoid;
      page-break-inside: avoid;
      font-size: 9.2pt;
    }

    .rule-card.warning {
      border-left-color: #dc2626;
      background: #fef2f2;
      border-color: #fecaca;
    }

    .rule-card.success {
      border-left-color: #059669;
      background: #f0fdf4;
      border-color: #bbf7d0;
    }

    .rule-card.info {
      border-left-color: #0284c7;
      background: #f0f9ff;
      border-color: #bae6fd;
    }

    /* Table Styles */
    .table-container {
      margin: 4mm 0;
      border: 1pt solid #cbd5e1;
      border-radius: 4pt;
      overflow: hidden;
      break-inside: avoid;
      page-break-inside: avoid;
    }

    table.data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8.5pt;
      line-height: 1.45;
    }

    table.data-table th {
      background: #fef3c7;
      color: #78350f;
      font-family: 'Noto Serif Devanagari', serif;
      font-weight: 800;
      text-align: left;
      padding: 2.5mm 3.5mm;
      border-bottom: 1.5pt solid #ca8a04;
    }

    table.data-table td {
      padding: 2.2mm 3.5mm;
      border-bottom: 0.5pt solid #e2e8f0;
      color: #1e293b;
    }

    table.data-table tr:nth-child(even) td {
      background-color: #fafaf9;
    }

    /* Diagram / Visual Plate Container */
    .diagram-plate {
      margin: 5mm 0;
      text-align: center;
      background: #ffffff;
      border: 1pt solid #fed7aa;
      border-radius: 6pt;
      padding: 4mm;
      break-inside: avoid;
      page-break-inside: avoid;
      box-shadow: 0 2pt 8pt rgba(180,83,9,0.06);
    }

    .diagram-img {
      width: 100%;
      max-width: 155mm;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .diagram-caption {
      margin-top: 2.5mm;
      font-size: 8.4pt;
      font-weight: 700;
      color: #78350f;
      font-style: italic;
    }

    /* Step List */
    .step-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 2.5mm;
      margin: 3.5mm 0;
    }

    .step-item {
      display: flex;
      gap: 3mm;
      align-items: flex-start;
      background: #ffffff;
      border: 1pt solid #e2e8f0;
      border-radius: 4pt;
      padding: 2.5mm 3.5mm;
      break-inside: avoid;
      page-break-inside: avoid;
      font-size: 9pt;
    }

    .step-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 20pt;
      height: 20pt;
      border-radius: 50%;
      background: #b45309;
      color: #ffffff;
      font-weight: 800;
      font-size: 8pt;
      flex-shrink: 0;
    }

    .step-content strong {
      display: block;
      color: #78350f;
      font-size: 9.5pt;
      margin-bottom: 1mm;
    }

    .step-content p {
      margin-bottom: 0;
      font-size: 8.8pt;
    }
    """

    # Assemble complete HTML
    html_out = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="utf-8">
  <title>तंत्र साधना सिद्धि महाग्रंथ • Vivliostyle Masterpiece Edition</title>
  <style>
{vivlio_css}
  </style>
</head>
<body>

  <!-- FRONT COVER PAGE -->
  <section class="print-cover-sheet" id="cover">
    <div class="cover-top-emblem">
      <div style="font-size:1.8rem; margin-bottom:2mm;">🔱 卐 🪔</div>
      <img src="assets/yantra.svg" alt="Sacred Sri Yantra Emblem">
    </div>

    <div class="cover-title-group">
      <div class="cover-mantra-header">॥ ॐ नमः शिवाय • ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे ॥</div>
      <h1 class="cover-main-title">तंत्र साधना सिद्धि महाग्रंथ</h1>
      <div class="cover-sub-title">41-दिवसीय प्रत्यक्ष प्रयोग, सवा लाख जप एवं सिद्ध कुंजिका गुप्त विधि-विधान</div>
      <div class="cover-en-title">Tantra Sadhana Siddhi • 41-Day Empirical Sadhana Protocols & Secret Rituals</div>
      <div class="cover-divider"></div>
      <p class="cover-meta-summary">
        सवा लाख (1,25,000) पंचाक्षरी जप, श्री सिद्ध कुंजिका स्तोत्र 21 पाठ, वेदी निर्माण द्वैत दीप विज्ञान, 8:30 PM–10:40 PM मिनट-दर-मिनट अनुष्ठान, स्वास्थ्य प्रबंधन एवं संपुट रहस्य का प्रामाणिक तंत्र कल्प।
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
      <div style="font-family:'Noto Serif Devanagari',serif; font-size:13pt; font-weight:700; color:#78350f; line-height:1.9;">
        ॥ नमो देव्यै महादेव्यै शिवायै सततं नमः ।<br>
        नमः प्रकृत्यै भद्रायै नियताः प्रणताः स्म ताम् ॥<br><br>
        ॥ ॐ ह्रीं बटुकाय आपदुद्धारणाय कुरु कुरु बटुकाय ह्रीं ॐ ॥
      </div>
      <div style="width:40%; height:1.5pt; background:#ca8a04; margin:5mm auto;"></div>
      <p style="font-size:9.5pt; color:#1e293b; line-height:1.75; text-align:center;">
        यह महाग्रंथ समस्त निष्ठावान साधकों, शोधार्थियों एवं शिव-शक्ति के अनन्य उपासकों के कल्याणार्थ तंत्र ज्ञान शोध संस्थान द्वारा सप्रेम समर्पित है।
      </p>
    </div>
  </section>

  <!-- TABLE OF CONTENTS -->
  <section class="print-toc-sheet" id="toc">
    <h2 class="toc-title">ग्रंथ अनुक्रमणिका • Table of Contents</h2>
    <ul class="toc-list">
      <li class="toc-item"><a href="#ch1"><span class="toc-item-title">अध्याय 1: 41-दिवसीय पंचाक्षरी महासाधना एवं 1,25,000 जप सिद्धि</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch2"><span class="toc-item-title">अध्याय 2: तांत्रिक वेदी निर्माण, द्वैत दीप विज्ञान एवं 7-पद सामग्री क्रम</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch3"><span class="toc-item-title">अध्याय 3: दैनिक साधना काल-तालिका (8:30 PM – 10:40 PM मिनट-दर-मिनट)</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch4"><span class="toc-item-title">अध्याय 4: स्वास्थ्य प्रबंधन, त्रि-स्तरीय प्रोटोकॉल एवं पोषण दिशानिर्देश</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch5"><span class="toc-item-title">अध्याय 5: षड्विध तांत्रिक यम-नियम, प्राणायाम एवं स्वप्न-स्वर विज्ञान</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch6"><span class="toc-item-title">अध्याय 6: श्री सिद्ध कुंजिका स्तोत्र संपुट विधान एवं शीघ्र विवाह सिद्धि</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch7"><span class="toc-item-title">अध्याय 7: श्री सिद्ध कुंजिका स्तोत्र सम्पूर्ण मूल पाठ एवं न्यास-विधान</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#ch8"><span class="toc-item-title">अध्याय 8: अनुष्ठान समापन, दशांश हवन, आरती एवं आसन-उत्थापन महामंत्र</span><span class="toc-dots"></span></a></li>
      <li class="toc-item"><a href="#author"><span class="toc-item-title">उपसंहार: प्रणेता परिचय एवं ग्रंथ समर्पण</span><span class="toc-dots"></span></a></li>
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
    print(f"\n🚀 Running Vivliostyle build for Tantra Sadhana Siddhi...")
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
