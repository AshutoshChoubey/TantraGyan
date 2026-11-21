# AI Design Findings — TantraGyan

## 1. Executive Summary
The Visual Authenticity Engine scanned the stylesheets and core reader pages of TantraGyan. The audit identified common AI template design patterns ("vibe coded" indicators) while verifying that the underlying manuscripts, Sanskrit texts, and interactive book components are intact.

## 2. Key Findings

### TG-UI-001: Linear Gradient Text Clipping on Flagship Headings
- **Files:** `index.html` (line 1197)
- **Problem:** `.flagship-main-heading` uses `-webkit-background-clip: text` with a 4-stop linear gradient (`#ffffff -> #fef08a -> #f59e0b -> #d97706`).
- **Impact:** Decreases legibility and contrast against dark backgrounds, creating a generic AI-generated aesthetic.
- **Remediation:** Replace with solid high-contrast foreground color (`#ffffff` or `var(--accent-gold)`).

### TG-UI-002: Asymmetrical Side-Tab Accent Borders on Rounded Containers
- **Files:**
  - `css/book.css` (lines 1750, 2033: `.author-profile-box`, `.index-card`)
  - `css/tables.css` (lines 214, 555: `.rule-card`, `.med-diagnosis-box`)
  - `bnn.html` (line 1773: `#author`)
  - `reader.html` (lines 2146, 10196: `.disclaimer-box`, callout blocks)
  - `tantra-sadhana-siddhi.html` (lines 415, 463)
  - `sadhana-reader.html` (line 419)
- **Problem:** Rounded cards (`border-radius: 8px`) combine a 1px border with a thick 4px or 5px left-stripe accent border (`border-left: 4px solid var(--accent-gold)`).
- **Impact:** The asymmetrical left stripe on a rounded container is a recognized AI template indicator and visual clash.
- **Remediation:** Standardize to uniform 1px structural borders with subtle surface background tints (`rgba(217, 119, 6, 0.05)`).

### TG-UI-003: Saturated Radial Spotlight Glows (`.book-aura-glow`)
- **Files:** `index.html` (lines 1381–1403: `.book-aura-glow.gold-aura`, `.indigo-aura`, `.crimson-aura`)
- **Problem:** Large floating radial gradient overlays behind 3D books create a hazy cloud effect.
- **Impact:** Classic AI landing page decoration that obscures clean book silhouettes.
- **Remediation:** Subdue or remove radial hazy clouds, allowing the realistic 3D book and its natural depth shadow to stand cleanly.

### TG-UI-004: Low-Contrast UI Labels & Badges
- **Files:** `index.html`, `reader.html`, `bnn.html`
- **Problem:** Certain secondary metadata tags and badges use low-contrast amber or light gray text failing the WCAG AA 4.5:1 ratio.
- **Remediation:** Adjust text color values to meet or exceed 4.5:1 against dark backgrounds (`#f8fafc` or `#fbbf24`).
