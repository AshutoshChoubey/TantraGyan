# 📜 Prompt 14: Visual Authenticity Audit & Impeccable Quality Standards
## Source Toolkit: `TantraGyan/visual-authenticity/`

---

## 1. Core Visual Authenticity Mission
The **Visual Authenticity Engine** (integrated in `TantraGyan/visual-authenticity/bin/engine.mjs`) protects the sacred dignity of Tantra Gyan from generic AI tropes, amateur layout flaws, and maintainability anti-patterns.

All content, reader templates, and book pages for Flagship Vol 4 must strictly adhere to the following rules:

---

## 2. The 10 Anti-AI Design Invariants
1. **Zero Generic AI Tropes:**
   - No floating neon glassmorphism blobs that obscure text.
   - No gratuitous outer box-shadows or radioactive neon borders (`#00ffcc` or `#ff00ff`).
   - Use warm, classical parchment tones (`#faf6ee`, `#fffdf8`) or refined obsidian dark modes (`#090d16`).
2. **Zero Text Clutter & Disclaimers:**
   - Absolutely no LLM disclaimers ("As an AI", "Please consult a professional", "Astrological predictions are speculative").
   - Maintain the voice of a confident, classical Vedic scholar and master mathematician.
3. **Typography Legibility Standards:**
   - Headings: Minimum 22px to 32px with robust line-height (1.3 to 1.4).
   - Paragraph Body: 15px to 17px with generous line-height (1.7 to 1.85) for fatigue-free reading.
   - Code & Mathematical Formulas: 13.5px to 14.5px monospace with crisp contrasting background.
4. **Table & Formula Bounds:**
   - All tables must be responsive with `overflow-x: auto` wrappers.
   - Cells must never cause horizontal viewport clipping or page overflow.
   - Numbers and scores must be cleanly centered or aligned.
5. **Interactive Experience Preservation:**
   - The realistic page-turn animation and authentic sound effects (`js/sound.js`, `js/sounds-data.js`) must be preserved and wired seamlessly into `kundali-ganita-reader.html`.
   - Side-drawer TOC must be accessible via keyboard (ESC to close, Tab navigation).
6. **Accessibility (a11y) Verification:**
   - High color contrast ratio (WCAG AA compliant, $\ge 4.5:1$ for normal text, $\ge 3:1$ for large headings).
   - Clear focus indicators on interactive buttons, links, and sliders.
   - Meaningful `aria-label` tags on all icon buttons and flip controls.

---

## 3. Automated Audit Execution
Before any deployment or pull request:
```bash
# 1. Run detection scanner across all pages
node visual-authenticity/bin/engine.mjs detect

# 2. Check engine status and review findings
node visual-authenticity/bin/engine.mjs status
```
Remediate any reported finding immediately.
