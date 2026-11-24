# 📜 Prompt 13: Canva Styling, SVG Diagrams & 3D Book Art Specifications
## Visual Design Architecture for Flagship Vol 4

---

## 1. Book Visual Identity Tokens
- **Theme Name:** **Royal Emerald & Celestial Cyan** (Budha-Brihaspati Intelligence & Cosmic Wisdom)
- **Primary Color:** `#059669` (Royal Emerald Green)
- **Secondary Accent:** `#0284c7` (Celestial Cyan / Azure)
- **Border Gold/Emerald:** `#10b981` (Vibrant Emerald Glow) & `#c89d3d` (Vedic Brass Gold)
- **Surface Dark (Obsidian):** `#090d16` (Deep Cosmic Indigo-Black)
- **Surface Light (Parchment):** `#faf6ee` (Classical Palm-Leaf Manuscript Ivory)
- **Typography Suite:**
  - Headings: `Cinzel`, `Noto Serif Devanagari`, Georgia, serif
  - Body: `Poppins`, `Noto Sans Devanagari`, sans-serif
  - Math & Tables: `JetBrains Mono`, `Fira Code`, monospace

---

## 2. 3D Hardcover Book Showcase Mockup (Homepage Card 4)
- **Card Container:** `#book-ganita.featured-book-card`
- **Aura Glow:** `.emerald-aura` with gradient:
  ```css
  background: radial-gradient(circle, rgba(16, 185, 129, 0.4) 0%, rgba(2, 132, 199, 0.25) 50%, transparent 75%);
  ```
- **Book Spine & Front Cover Mockup:**
  - Embossed golden/emerald Sanskrit typography:
    - Main Title: **वैदिक कुण्डली विचार एवं गणित महाग्रंथ**
    - Subtitle: **खगोलीय सूत्र, 16 वर्ग चक्र एवं फलित संयोजन**
    - English Title: **The Cosmic Algorithm**
    - Author: **ज्योतिषाचार्य आशुतोष कुमार चौबे**
  - Cosmic Geometry: Central golden Sri Yantra interlocked with a 12-house North Indian Kundali diamond chart and planetary orbits.
  - Ribbon: `👑 FLAGSHIP VOL 4` in Emerald/Cyan gradient (`linear-gradient(135deg, #059669, #0284c7)`).

---

## 3. High-Legibility SVG Diagram Standards
Every diagram generated for the book must strictly satisfy:
1. **High Contrast:** White/ivory lines (`#f8fafc`, `#38bdf8`, `#34d399`) on dark backgrounds or crisp dark ink (`#1e293b`, `#0f766e`) on parchment.
2. **Text Wrapping & Zero Overflow:** Labels must use `<tspan>` or bounded layout; font size minimum 14px for node titles, 12px for subtitles.
3. **Responsive Vector Rendering:** `viewBox="0 0 800 600"` with `width="100%"` and `preserveAspectRatio="xMidYMid meet"`.
4. **Diagram Types Required in Book:**
   - Diagram 1: The Ecliptic & Horizon (Julian Day, RAMC, Ascendant rising angle).
   - Diagram 2: The Panchanga Solilunar Engine (Sun-Moon angular separation & 5 limbs).
   - Diagram 3: The 120-Year Vimshottari Recursive Tree (MD $\to$ AD $\to$ PD $\to$ SD).
   - Diagram 4: The 4 Vishnu Pillars (Kendras) & 3 Lakshmi Houses (Trikonas).
   - Diagram 5: The 337 Ashtakavarga Point Grid & Kakshya Slices.
   - Diagram 6: The 16 Varga Harmonic Divisions (D1 to D60).
   - Diagram 7: The 4 BNN Directional Trines (Dharma, Artha, Kama, Moksha).
   - Diagram 8: The 7.5-Year Sade Sati Transit Wave.
   - Diagram 9: The 36 Guna Ashta Koota Balance Scale.
   - Diagram 10: The 81-Square Sarvatobhadra Chakra.

---

## 4. Canva Integration Workflow
1. Use Canva brand templates for book cover artwork, chapter splash headers, and marketing banners.
2. Bulk creation parameters for generating 13 chapter banner images with consistent typography and color palettes.
