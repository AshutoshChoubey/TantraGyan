# 01 — Design System Fixes: TantraGyan Stylesheets

## 1. Audit Findings Addressed
- `TG-UI-002`: Asymmetrical `border-left: 4px` on rounded containers in `css/book.css` and `css/tables.css`.

## 2. Target Files
- `css/book.css`
- `css/tables.css`

## 3. Issues & Remediation Plan
1. In `css/book.css`:
   - Line 1750: `.author-profile-box` combines `border-radius: 8px` with `border-left: 4px solid var(--accent-gold)`.
     - *Fix:* Remove `border-left: 4px solid var(--accent-gold)`. Use uniform structural border `border: 1px solid var(--page-border)` and enhance subtle surface background `background: rgba(179, 127, 25, 0.08)`.
   - Line 2033: `.index-card` combines `border-radius: 8px` with `border-left: 4px solid var(--accent-gold)`.
     - *Fix:* Remove `border-left: 4px solid var(--accent-gold)`. Use clean uniform border `border: 1px solid var(--page-border)` and highlight on hover `border-color: var(--accent-gold)`.
2. In `css/tables.css`:
   - Line 214: `.rule-card` combines `border-radius: 8px` with `border-left: 4px solid var(--accent-gold)`.
     - *Fix:* Remove `border-left: 4px solid var(--accent-gold)`. Use uniform `border: 1px solid var(--page-border)` with subtle tint.
   - Line 555: `.med-diagnosis-box` combines `border-radius: 8px` with `border-left: 4px solid var(--accent-crimson)`.
     - *Fix:* Remove `border-left: 4px solid var(--accent-crimson)`. Use uniform `border: 1px solid rgba(220, 38, 38, 0.25)` and background `rgba(220, 38, 38, 0.04)`.

## 4. Protected Content
- Do not modify font definitions, book page sizing, or printing rules.

## 5. Acceptance Criteria
- `css/book.css` and `css/tables.css` have zero `side-tab` warnings.
