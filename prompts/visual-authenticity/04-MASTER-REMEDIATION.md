# 04 — Master Remediation Prompt: TantraGyan Visual Authenticity

## 1. Executive Directive
Execute all verified low-risk visual authenticity remediations sequentially across TantraGyan:
1. `01-DESIGN-SYSTEM-FIXES.md` (Stylesheets `css/book.css` and `css/tables.css`)
2. `02-PAGE-BY-PAGE-REDESIGN.md` (`index.html`)
3. `03-READER-SIDE-TABS-FIXES.md` (`reader.html`, `bnn.html`, `sadhana-reader.html`, `tantra-sadhana-siddhi.html`)

## 2. Invariant Rules
- Strict text immutability: zero changes to shlokas, mantras, Sanskrit verses, astrological formulas, or commentary.
- Strict animation immutability: retain 3D book-opening transforms and acoustic page flip sounds.

## 3. Post-Remediation Verification
1. Run `node visual-authenticity/bin/engine.mjs detect css/book.css css/tables.css index.html`.
2. Confirm zero `side-tab` and zero `gradient-text` warnings.
3. Verify Git remote points to `AshutoshChoubey/TantraGyan.git`.
4. Stage, commit, and push changes to `origin main`.
