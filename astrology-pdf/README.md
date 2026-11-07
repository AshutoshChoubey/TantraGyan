# Astrology Sanskrit & Devanagari PDF Publishing Engine
## Recommended Architecture: Python + Vivliostyle + Chromium

This standalone test project demonstrates publication-grade typesetting and typography for mixed Sanskrit, Hindi, and English Vedic Astrology literature.

---

### 1. Production Architecture Stack

| Layer | Technology | Function |
|---|---|---|
| **Orchestration** | Python 3 | Manuscript parsing, chart generation, font checks, automation |
| **Document Design** | HTML5 + W3C Paged Media CSS | Book typography, tables, margins, headers, page numbers |
| **Text Shaping** | Chromium + HarfBuzz | Pixel-perfect Devanagari OpenType shaping, conjuncts, matras |
| **Book Pagination** | Vivliostyle CLI (`@vivliostyle/cli`) | Professional multi-page layout, spreads, print-ready PDF |
| **Visual Charts** | Vector SVG | Pure mathematical geometry (North Indian diamond & South Indian charts) |

---

### 2. Typographical Font Stack (OFL-1.1)

All fonts are stored in `fonts/` and embedded directly into the PDF:

- **Sanskrit & Hindi Body**: `Noto Serif Devanagari` (Regular 400, Bold 700)
  - Full support for complex ligatures, matras (मात्राएं), halanta (हलंत), and repha (रेफ/रकार).
- **Charts, Tables & Badges**: `Noto Sans Devanagari` (Regular 400, Bold 700)
  - Crisp, modern sans-serif legibility for compact cell widths and chart coordinates.
- **English Body & Titles**: `Noto Serif` (Regular 400, Bold 700)
  - Professional editorial serif font matching the weight and ascender heights of Devanagari.

---

### 3. Project Structure

```
astrology-pdf/
├── fonts/
│   ├── NotoSerifDevanagari-Regular.ttf
│   ├── NotoSerifDevanagari-Bold.ttf
│   ├── NotoSansDevanagari-Regular.ttf
│   ├── NotoSansDevanagari-Bold.ttf
│   ├── NotoSerif-Regular.ttf
│   └── NotoSerif-Bold.ttf
├── test.html          # Clean HTML5 source with W3C CSS Paged Media
├── generate.py        # Python build script running Vivliostyle
├── verify.py          # 3-Step automated verification suite
├── output/
│   ├── astrology-test.pdf   # Generated publication-quality PDF
│   ├── proof-page-1.png     # 200 DPI visual proof (Page 1)
│   └── proof-page-2.png     # 200 DPI visual proof (Page 2)
└── README.md
```

---

### 4. Running the Engine & Verification

```bash
# 1. Generate the PDF via Vivliostyle
python3 generate.py

# 2. Run the 3-step verification suite (Font embedding, Text extraction, Proof PNGs)
python3 verify.py
```

### 5. Verification Results

1. **Check 1 — Font Embedding**:
   - `NotoSerifDevanagari-Bold` (Type0, Embedded: Yes)
   - `NotoSerifDevanagari-Regular` (Type0, Embedded: Yes)
   - `NotoSansDevanagari-Bold` (Type0, Embedded: Yes)
   - `NotoSansDevanagari-Regular` (Type0, Embedded: Yes)
   - `NotoSerif-Regular` (Type0, Embedded: Yes)
   - Zero missing glyphs / zero tofu.

2. **Check 2 — Text Extraction**:
   - All complex conjuncts (`कर्मण्येवाधिकारस्ते`, `ज्योतिष`, `श्रीमद्भगवद्गीता`, `त्र्यंबकम्`, `बृहस्पति`, `कुण्डली`, `लग्न`) verified intact.

3. **Check 3 — Visual Rendering**:
   - 200 DPI proof images generated: `proof-page-1.png` and `proof-page-2.png`.

---

### 6. Live Localhost Preview Links

- **PDF Document**: [http://localhost:8899/astrology-pdf/output/astrology-test.pdf](http://localhost:8899/astrology-pdf/output/astrology-test.pdf)
- **Proof Image Page 1**: [http://localhost:8899/astrology-pdf/output/proof-page-1.png](http://localhost:8899/astrology-pdf/output/proof-page-1.png)
- **Proof Image Page 2**: [http://localhost:8899/astrology-pdf/output/proof-page-2.png](http://localhost:8899/astrology-pdf/output/proof-page-2.png)

