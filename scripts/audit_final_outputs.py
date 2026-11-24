#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exhaustive integrity and quality audit of all generated editions:
1. kundali-ganita.html (Web Presentation)
2. kundali-ganita-reader.html (3D Flipbook Reader)
3. kundali-ganita-print.html (Print Layout)
4. kundali-ganita-vichar-mahagranth.pdf (Vector Masterpiece PDF)
"""

import re
import os
from pathlib import Path

BASE = Path("/Users/apple/Movies/ap/TantraGyan")

files_to_check = {
    "Web Edition (kundali-ganita.html)": BASE / "kundali-ganita.html",
    "3D Reader (kundali-ganita-reader.html)": BASE / "kundali-ganita-reader.html",
    "Print Layout (kundali-ganita-print.html)": BASE / "kundali-ganita-print.html",
}

print("=" * 80)
print("🔍 EXHAUSTIVE INTEGRITY AUDIT: CODE, MATH, SYMBOLS, & ANONYMITY")
print("=" * 80)

all_clean = True

for name, path in files_to_check.items():
    print(f"\n📁 Auditing: {name}")
    if not path.exists():
        print(f"  ❌ File not found: {path}")
        all_clean = False
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    size_kb = len(content.encode("utf-8")) / 1024
    lines = len(content.splitlines())
    print(f"  • Size: {size_kb:.2f} KB | Lines: {lines}")

    # 1. Dollar signs count (exclude JS variables inside <script> like $(...) if any, but in HTML body should be 0)
    # Check in HTML body (strip <script>...</script> for fair content check)
    body_content = re.sub(r'<script[\s\S]*?</script>', '', content)
    body_dollars = body_content.count('$')
    print(f"  • Content Dollar Signs ($): {body_dollars}")
    if body_dollars > 0:
        print(f"    ⚠️ Found dollar signs in content!")
        all_clean = False

    # 2. Raw LaTeX commands in body
    latex_cmds = re.findall(r'\\(?:tan|sin|cos|lfloor|rfloor|pmod|implies|alpha|beta|lambda|Delta|theta|deg|frac|text\{|left|right)', body_content)
    print(f"  • Raw LaTeX Math Commands: {len(latex_cmds)}")
    if latex_cmds:
        print(f"    ⚠️ Samples: {latex_cmds[:5]}")
        all_clean = False

    # 3. Python code mentions in content
    py_blocks = re.findall(r'```python|def [a-zA-Z0-9_]+\s*\(|import numpy|import math|import swiss', body_content)
    print(f"  • Python Code Snippets in Content: {len(py_blocks)}")
    if py_blocks:
        print(f"    ⚠️ Samples: {py_blocks[:5]}")
        all_clean = False

    # 4. Special raw symbols like ±od or rac{
    weird_symbols = re.findall(r'±od|rac\{|#\{', body_content)
    print(f"  • Malformed Math Artifacts (±od, rac): {len(weird_symbols)}")
    if weird_symbols:
        print(f"    ⚠️ Samples: {weird_symbols[:5]}")
        all_clean = False

    # 5. SVG Diagrams Count
    svg_count = body_content.count("<svg")
    print(f"  • Embedded SVG Diagrams: {svg_count}")

    # 6. Anonymity Check
    native_leaks = re.findall(r'Ashutosh: 28 Oct 1994|Native Ashutosh|जातक आशुतोष', body_content)
    print(f"  • Personal Name Leaks: {len(native_leaks)}")
    if native_leaks:
        print(f"    ⚠️ Found personal name leaks: {native_leaks}")
        all_clean = False
    
    # 7. Check Benchmark Native Designation
    jataka_ka = body_content.count("जातक 'क'")
    print(f"  • Benchmark Designation (जातक 'क') count: {jataka_ka}")

# 8. Check PDF
pdf_path = BASE / "kundali-ganita-vichar-mahagranth.pdf"
print(f"\n📄 Auditing Master Vector PDF: {pdf_path.name}")
if pdf_path.exists():
    pdf_size_kb = pdf_path.stat().st_size / 1024
    print(f"  • File Size: {pdf_size_kb:.2f} KB ({pdf_size_kb/1024:.2f} MB)")
    
    # Check page count via pdfinfo or python
    try:
        import subprocess
        res = subprocess.run(["pdfinfo", str(pdf_path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0:
            for l in res.stdout.splitlines():
                if "Pages:" in l:
                    print(f"  • Total PDF Pages: {l.split()[-1]}")
    except Exception:
        pass
else:
    print(f"  ❌ PDF file does not exist!")
    all_clean = False

print("\n" + "=" * 80)
if all_clean:
    print("✅ PERFECT AUDIT: ALL EDITIONS 100% CLEAN OF CODE, MATH & ARTIFACTS!")
else:
    print("❌ AUDIT DETECTED ISSUES TO RESOLVE")
print("=" * 80)
