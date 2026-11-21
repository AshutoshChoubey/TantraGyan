# Visual Authenticity Engine — TantraGyan

The **Visual Authenticity Engine** is an integrated design-auditing and code-quality validation framework for **TantraGyan** (`https://github.com/AshutoshChoubey/TantraGyan`).

It enables the engineer and AI agents to systematically identify and eliminate generic AI template tropes, excessive glow effects, clashing borders, and maintainability anti-patterns, while **strictly preserving sacred texts, classical manuscript data, PDF books, book-opening 3D animations, and page-turning sounds**.

---

## 🎯 Architecture & Provenance

- **Vendored Detection Core**: Powered by Paul Bakaus's [Impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0).
- **Project Wrapper**: `visual-authenticity/bin/engine.mjs` orchestrates scans, isolates application source, and formats audit findings.
- **Third-Party Notices**: Located in `visual-authenticity/third-party/`.
- **Agent Skill Discovery**: Integrated natively with Google Antigravity in `.agent/skills/impeccable/`.

---

## 📁 Directory Structure

```text
visual-authenticity/
├── bin/
│   └── engine.mjs                  # CLI runner and orchestrator
├── toolkit/                        # Vendored upstream Impeccable core
├── third-party/                    # Licenses and attribution records
├── context/                        # Baseline architectural manifests
│   ├── PROJECT_OVERVIEW.md
│   ├── ARCHITECTURE_MAP.md
│   ├── ROUTE_AND_PAGE_INVENTORY.md
│   ├── COMPONENT_INVENTORY.md
│   ├── DESIGN_SYSTEM_BASELINE.md
│   ├── FUNCTIONALITY_BASELINE.md
│   ├── CONTENT_PROTECTION_RULES.md
│   └── AUDIT_PROGRESS.md
├── audit/                          # Structured audit findings
│   ├── AI_DESIGN_FINDINGS.md
│   ├── FRONTEND_QUALITY_FINDINGS.md
│   ├── BACKEND_QUALITY_FINDINGS.md
│   ├── COMPONENT_REVIEW.md
│   ├── DESIGN_SYSTEM_REVIEW.md
│   ├── ARCHITECTURE_REVIEW.md
│   ├── AUDIT_SUMMARY.md
│   ├── DETECTION_RESULTS.json
│   └── COVERAGE_MANIFEST.json
└── progress/                       # Remediation tracking manifests
    ├── SCAN_PROGRESS.md
    ├── IMPLEMENTATION_PROGRESS.md
    ├── COMPLETED_FINDINGS.md
    ├── DEFERRED_FINDINGS.md
    ├── VERIFICATION_RESULTS.md
    └── NEXT_ACTIONS.md
```

---

## 🚀 Usage

### 1. Source Scan
Run design detection across TantraGyan stylesheets and reader pages:
```bash
node visual-authenticity/bin/engine.mjs detect
```

### 2. Status & Path Check
```bash
node visual-authenticity/bin/engine.mjs status
```

---

## 🛡️ Protection Guidelines
TantraGyan is a sacred repository of Vedic astrology, Bhrigu Nandi Nadi, and Tantra Sadhana. All remediations must strictly preserve:
1. **Sacred Texts & Books:** Zero alterations to scriptural texts, translations, shlokas, verses, mantras, or astrological formulas.
2. **Book Manuscripts & PDFs:** No modification to generated PDFs (`tantra-gyan-vedic-jyotish-mahagranth.pdf`, `bhrigu-nandi-nadi-karma-samyojan.pdf`, `tantra-sadhana-siddhi-protocol.pdf`).
3. **Interactive Book Experience:** The interactive book-opening animation and sound effects (`js/sound.js`, `js/sounds-data.js`) must be 100% retained.
4. **Authentic Astrological Imagery:** Kundali birth charts, yantras, and mandala graphics.
