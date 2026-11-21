# 00 — Master Audit Prompt: TantraGyan Visual Authenticity

## 1. Objective
Perform a comprehensive, automated design-system and code-quality audit across the **TantraGyan** sacred reader and publication repository using the project-owned **Visual Authenticity Engine** (`visual-authenticity/bin/engine.mjs`).

Identify generic AI-generated "vibe coded" design artifacts, legibility issues, low-contrast UI controls, and code smells, while strictly protecting all book manuscripts, sacred texts, 3D book-opening animations, and audio effects.

---

## 2. Target Repositories & Scopes
- **Target Project:** TantraGyan (`/Users/apple/Movies/ap/TantraGyan`)
- **Core Files to Audit:**
  - `css/book.css`
  - `css/tables.css`
  - `index.html`
  - `reader.html`
  - `book.html`
  - `bnn.html`
  - `bnn-reader.html`
  - `sadhana-reader.html`
  - `tantra-sadhana-siddhi.html`

---

## 3. Mandatory Protection Guidelines
1. **Zero Text Modification:** Do not alter any scriptural shloka, mantra, Hindi/English commentary, or astrological table.
2. **Preserve Book Opening Animation:** Do NOT modify the 3D book cover opening animations or 3D transform perspectives.
3. **Preserve Audio Effects:** Do NOT alter page flip sounds or acoustic synthesis in `js/sound.js`.
4. **Preserve PDF & Manuscript Artifacts:** Retain all generated PDFs and publishing scripts intact.

---

## 4. Audit Execution Steps
1. Execute the Visual Authenticity Engine CLI detector:
   ```bash
   node visual-authenticity/bin/engine.mjs detect css index.html reader.html bnn.html bnn-reader.html sadhana-reader.html tantra-sadhana-siddhi.html
   ```
2. Parse raw detector findings into `visual-authenticity/audit/DETECTION_RESULTS.json`.
3. Synthesize the findings into structured markdown reports:
   - `visual-authenticity/audit/AI_DESIGN_FINDINGS.md`
   - `visual-authenticity/audit/FRONTEND_QUALITY_FINDINGS.md`
   - `visual-authenticity/audit/AUDIT_SUMMARY.md`
4. Formulate actionable remediation prompts in `prompts/visual-authenticity/` targeting only verified visual and design issues.
