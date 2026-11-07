#!/usr/bin/env python3
import sys
from pathlib import Path
import fitz # PyMuPDF

ROOT = Path(__file__).resolve().parent
output_dir = ROOT / "output"
pdf_file = output_dir / "astrology-test.pdf"

if not pdf_file.exists():
    print(f"❌ PDF not found: {pdf_file}")
    sys.exit(1)

doc = fitz.open(pdf_file)
print(f"============================================================")
print(f"📄 PDF Inspection: {pdf_file.name}")
print(f"   Pages: {len(doc)} | Size: {pdf_file.stat().st_size / 1024:.1f} KB")
print(f"============================================================")

# Check 1: Font Embedding
print("\n[CHECK 1: Font Embedding Verification]")
print(f"{'Page':<6} {'Font Name':<35} {'Type':<12} {'Embedded':<10}")
print("-" * 65)
embedded_fonts = set()
for page_num in range(len(doc)):
    page = doc[page_num]
    font_list = page.get_fonts(full=True)
    for f in font_list:
        # f: (xref, ext, type, basefont, name, encoding, ...)
        basefont = f[3]
        ftype = f[2]
        is_embedded = "yes" if f[0] > 0 else "no"
        embedded_fonts.add(basefont)
        print(f"{page_num + 1:<6} {basefont:<35} {ftype:<12} {is_embedded:<10}")

# Check 2: Text Extraction
print("\n[CHECK 2: Text Extraction & Devanagari Integrity]")
print("-" * 65)
full_text = ""
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text("text")
    full_text += text
    print(f"--- Page {page_num + 1} ---")
    print(text.strip())
    print()

# Check for crucial conjuncts
test_terms = [
    "कर्मण्येवाधिकारस्ते",
    "ज्योतिष",
    "श्रीमद्भगवद्",
    "त्र्यंबकम्",
    "बृहस्पति",
    "कुण्डली",
    "लग्न"
]
print("\n[Devanagari Keyword Spot-Check]")
for term in test_terms:
    found = term in full_text
    status = "✅ PASS" if found else "❌ MISSING"
    print(f"  {term:<25}: {status}")

# Check 3: Visual Rendering (proof PNGs)
print("\n[CHECK 3: Visual Proof Rendering (200 DPI)]")
print("-" * 65)
proof_files = []
for page_num in range(len(doc)):
    page = doc[page_num]
    pix = page.get_pixmap(dpi=200)
    proof_path = output_dir / f"proof-page-{page_num + 1}.png"
    pix.save(proof_path)
    proof_files.append(proof_path)
    print(f"  📸 Saved proof: {proof_path.name} ({pix.width}x{pix.height} px, {proof_path.stat().st_size / 1024:.1f} KB)")

print("\n🎉 Validation complete!")
