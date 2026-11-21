# 02 — Page-by-Page Redesign: TantraGyan Portal (`index.html`)

## 1. Audit Findings Addressed
- `TG-UI-001`: Gradient text on `.flagship-main-heading` in `index.html`.
- `TG-UI-003`: Saturated radial spotlight glow (`.book-aura-glow`) in `index.html`.
- `TG-UI-004`: Low-contrast text on badges and metadata tags in `index.html`.

## 2. Target File
- `index.html`

## 3. Issues & Remediation Plan
1. **Gradient Text Removal:**
   - In `.flagship-main-heading` (lines 1197–1200):
     - Replace `-webkit-background-clip: text; -webkit-text-fill-color: transparent; background: linear-gradient(...)` with solid high-contrast `#ffffff` with subtle gold text glow or drop shadow for crisp readability.
2. **Radial Hazy Spotlight Glow Subdual:**
   - In `.book-aura-glow` (lines 1381–1403):
     - Subdue opacity (`opacity: 0.15` instead of `0.45`) or eliminate the large hazy gradient cloud behind the 3D book cover, allowing the 3D book cover, its gold frame, and natural drop-shadow to stand out crisply without AI cloud slop.
3. **Contrast Elevation:**
   - Ensure secondary metadata text meets WCAG AA contrast standards (> 4.5:1).

## 4. Protected Content
- **100% Immunity:** Do NOT alter the 3D book cover, opening animation, book descriptions, chapter lists, or external links.

## 5. Acceptance Criteria
- `index.html` has zero `gradient-text` warnings.
- 3D book animations and interactions work smoothly.
