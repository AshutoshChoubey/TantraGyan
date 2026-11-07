#!/usr/bin/env python3
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
html_file = ROOT / "test.html"
output_dir = ROOT / "output"
pdf_file = output_dir / "astrology-test.pdf"

output_dir.mkdir(exist_ok=True)

if not html_file.exists():
    raise FileNotFoundError(f"File not found: {html_file}")

required_fonts = [
    "NotoSerifDevanagari-Regular.ttf",
    "NotoSerifDevanagari-Bold.ttf",
    "NotoSansDevanagari-Regular.ttf",
    "NotoSansDevanagari-Bold.ttf",
    "NotoSerif-Regular.ttf",
    "NotoSerif-Bold.ttf",
]

for font in required_fonts:
    if not (ROOT / "fonts" / font).exists():
        raise FileNotFoundError(f"Missing font: {font}")

# Vivliostyle build
command = [
    "vivliostyle",
    "build",
    str(html_file),
    "-s",
    "A4",
    "-o",
    str(pdf_file),
]

print(f"⚙️ Running Vivliostyle build: {' '.join(command)}")
try:
    res = subprocess.run(command, check=True, capture_output=True, text=True)
    if res.stdout:
        print(res.stdout)
except subprocess.CalledProcessError as e:
    print(f"❌ Vivliostyle error: {e}")
    if e.stderr:
        print(e.stderr)
    sys.exit(1)

print(f"✅ Generated: {pdf_file} ({pdf_file.stat().st_size / 1024:.1f} KB)")

# Run Check 1: pdffonts
if shutil.which("pdffonts"):
    print("\n🔍 Check 1 — Font embedding (pdffonts):")
    p = subprocess.run(["pdffonts", str(pdf_file)], capture_output=True, text=True)
    print(p.stdout)

# Run Check 2: pdftotext
if shutil.which("pdftotext"):
    print("\n🔍 Check 2 — Text extraction (pdftotext):")
    p = subprocess.run(["pdftotext", "-layout", str(pdf_file), "-"], capture_output=True, text=True)
    print(p.stdout[:1500])

# Run Check 3: pdftoppm
if shutil.which("pdftoppm"):
    proof_prefix = output_dir / "proof"
    print(f"\n🔍 Check 3 — Visual rendering (pdftoppm -> {proof_prefix}):")
    subprocess.run(["pdftoppm", "-png", "-r", "200", str(pdf_file), str(proof_prefix)], check=True)
    proof_files = list(output_dir.glob("proof-*.png"))
    print(f"Rendered {len(proof_files)} proof images:")
    for pf in sorted(proof_files):
        print(f"  - {pf.name} ({pf.stat().st_size / 1024:.1f} KB)")

