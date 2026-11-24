#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compiles Flagship Vol 4: 'वैदिक कुण्डली विचार एवं गणित महाग्रंथ'
into a publication-grade Masterpiece Vector PDF using Vivliostyle / Chrome Headless.
"""

import os
import re
import subprocess
import time

BASE_DIR = "/Users/apple/Movies/ap/TantraGyan"
WEB_HTML = os.path.join(BASE_DIR, "kundali-ganita.html")
PRINT_HTML = os.path.join(BASE_DIR, "kundali-ganita-print.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "kundali-ganita-vichar-mahagranth.pdf")

def generate_print_html():
    with open(WEB_HTML, "r", encoding="utf-8") as f:
        web_content = f.read()

    articles = re.findall(r'<article class="chapter-card" id="([^"]+)"[^>]*>(.*?)</article>', web_content, re.DOTALL)

    css = """
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
        color: #059669;
      }
    }

    @page :left {
      @top-left {
        content: "वैदिक कुण्डली विचार एवं गणित महाग्रंथ";
        font-family: 'Noto Sans Devanagari', sans-serif;
        font-size: 7.8pt;
        font-weight: 700;
        color: #059669;
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
        content: "खगोलीय सूत्र, 16 वर्ग चक्र एवं फलित संयोजन";
        font-family: 'Noto Sans Devanagari', sans-serif;
        font-size: 7.8pt;
        font-weight: 700;
        color: #065f46;
      }
      @top-right {
        content: "ज्योतिषाचार्य आशुतोष कुमार चौबे";
        font-family: 'Noto Sans Devanagari', sans-serif;
        font-size: 7.8pt;
        font-weight: 600;
        color: #059669;
      }
    }

    @page cover-page {
      margin: 0;
      @top-left { content: none; }
      @top-right { content: none; }
      @bottom-center { content: none; }
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Poppins', 'Noto Sans Devanagari', -apple-system, sans-serif;
      font-size: 9.5pt;
      line-height: 1.65;
      color: #1c1917;
      background-color: #ffffff;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }

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
      background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 40%, #e0f2fe 100%);
      border: 10mm solid #064e3b;
      position: relative;
    }

    .print-chapter {
      break-before: page;
      page-break-before: always;
      padding: 5mm 0;
    }

    .chapter-title {
      font-family: 'Noto Serif Devanagari', serif;
      font-size: 16pt;
      color: #065f46;
      border-bottom: 2pt solid #10b981;
      padding-bottom: 3mm;
      margin-bottom: 5mm;
    }

    .story-callout {
      background: rgba(2, 132, 199, 0.08);
      border-left: 3pt solid #0284c7;
      padding: 4mm 5mm;
      margin: 4mm 0;
      border-radius: 2mm;
    }

    .takeaway-box {
      background: rgba(5, 150, 105, 0.08);
      border: 1pt solid #10b981;
      padding: 4mm 5mm;
      margin: 4mm 0;
      border-radius: 2mm;
    }

    table.data-table {
      width: 100%;
      border-collapse: collapse;
      margin: 4mm 0;
      font-size: 8.5pt;
    }
    table.data-table th, table.data-table td {
      border: 0.5pt solid #cbd5e1;
      padding: 2.5mm;
      text-align: center;
    }
    table.data-table th {
      background: #0f766e;
      color: #ffffff;
    }
    """

    html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="utf-8">
  <title>वैदिक कुण्डली विचार एवं गणित महाग्रंथ • The Cosmic Algorithm (Print Edition)</title>
  <style>{css}</style>
</head>
<body>
  <!-- Cover Page -->
  <section class="print-cover-sheet">
    <div>
      <div style="font-size:12pt; color:#059669; font-weight:700; letter-spacing:2pt; margin-bottom:8mm;">॥ श्री गणेशाय नमः • ॐ नमः शिवाय ॥</div>
      <div style="font-size:11pt; color:#0284c7; font-weight:700; text-transform:uppercase; letter-spacing:1.5pt;">👑 FLAGSHIP VOL 4 • THE MASTER COMPENDIUM</div>
    </div>

    <div style="margin:10mm 0;">
      <h1 style="font-family:'Noto Serif Devanagari',serif; font-size:26pt; font-weight:900; color:#064e3b; line-height:1.35; margin-bottom:4mm;">
        वैदिक कुण्डली विचार एवं गणित महाग्रंथ
      </h1>
      <div style="font-size:14pt; color:#0284c7; font-weight:700; margin-bottom:4mm;">
        खगोलीय सूत्र, 16 वर्ग चक्र एवं फलित संयोजन
      </div>
      <div style="font-size:11.5pt; color:#475569; font-weight:600; letter-spacing:0.5pt;">
        The Cosmic Algorithm: Vedic Horoscope Mathematics & Destiny Decoded
      </div>
    </div>

    <div style="width:75%; height:2pt; background:linear-gradient(90deg, #10b981, #0284c7); margin:0 auto;"></div>

    <p style="font-size:10pt; color:#334155; line-height:1.75; max-width:150mm; margin:0 auto; text-align:center;">
      स्विस एफेमेरिस, 120-वर्षीय विंशोत्तरी दशा, 337 अष्टकवर्ग बिंदु, 16 वर्ग कुण्डलियाँ एवं 85 विवाह नियमों का सम्पूर्ण प्रामाणिक गणितीय एवं फलित संदर्भ-ग्रंथ।
    </p>

    <div style="border-top:1.5pt solid #059669; border-bottom:1.5pt solid #059669; padding:4mm 10mm; width:80%;">
      <div style="font-size:11pt; font-weight:700; color:#064e3b;">प्रणेता: ज्योतिषाचार्य आशुतोष कुमार चौबे</div>
      <div style="font-size:9pt; color:#64748b;">तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) • https://t.worldgyan.com</div>
    </div>
  </section>
"""

    for art_id, art_body in articles:
        html += f"""
  <section class="print-chapter" id="{art_id}">
    {art_body}
  </section>
"""

    html += """
</body>
</html>"""

    with open(PRINT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Generated {PRINT_HTML} ({os.path.getsize(PRINT_HTML):,} bytes)")

def compile_pdf():
    print(f"\n🚀 Compiling PDF for Flagship Vol 4...")
    # Try vivliostyle first
    try:
        cmd = [
            "/Users/apple/.nvm/versions/node/v24.21.0/bin/vivliostyle",
            "build",
            PRINT_HTML,
            "-s", "A4",
            "-o", OUTPUT_PDF,
            "--timeout", "120"
        ]
        t0 = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if res.returncode == 0 and os.path.exists(OUTPUT_PDF) and os.path.getsize(OUTPUT_PDF) > 1000:
            dur = time.time() - t0
            size_mb = os.path.getsize(OUTPUT_PDF) / (1024 * 1024)
            print(f"🎉 Vivliostyle Build Succeeded: {OUTPUT_PDF} ({size_mb:.2f} MB in {dur:.2f}s)")
            return
        else:
            print(f"Vivliostyle output: {res.stderr[:200]}")
    except Exception as e:
        print(f"Vivliostyle attempt: {e}")

    # Fallback to headless Chrome print-to-pdf
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.exists(chrome_path):
        print("Using Google Chrome Headless Print-to-PDF...")
        cmd = [
            chrome_path,
            "--headless=new",
            "--disable-gpu",
            f"--print-to-pdf={OUTPUT_PDF}",
            f"file://{PRINT_HTML}"
        ]
        t0 = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if os.path.exists(OUTPUT_PDF):
            dur = time.time() - t0
            size_mb = os.path.getsize(OUTPUT_PDF) / (1024 * 1024)
            print(f"🎉 Chrome Headless PDF Succeeded: {OUTPUT_PDF} ({size_mb:.2f} MB in {dur:.2f}s)")

if __name__ == "__main__":
    generate_print_html()
    compile_pdf()
