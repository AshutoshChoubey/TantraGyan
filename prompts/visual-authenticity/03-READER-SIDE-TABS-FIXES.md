# 03 — Reader Side-Tab Normalization: TantraGyan Readers

## 1. Audit Findings Addressed
- `TG-UI-002`: Asymmetrical side-tab borders on rounded callout boxes in `reader.html`, `bnn.html`, `sadhana-reader.html`, and `tantra-sadhana-siddhi.html`.

## 2. Target Files
- `bnn.html`
- `reader.html`
- `sadhana-reader.html`
- `tantra-sadhana-siddhi.html`

## 3. Issues & Remediation Plan
1. In `bnn.html` (line 1773):
   - Replace `style="border-left: 5px solid var(--accent-gold); background: var(--bg-surface);"` with clean uniform structural border `border: 1px solid var(--border-gold); background: var(--bg-surface);`.
2. In `reader.html` (lines 2146, 10196, 10641):
   - Normalize inline `border-left: 4px` / `border-left: 3px` on rounded callout boxes into uniform 1px borders with subtle surface background tint.
3. In `tantra-sadhana-siddhi.html` (lines 415, 463):
   - Standardize side-tab callouts to uniform 1px borders.
4. In `sadhana-reader.html` (line 419):
   - Standardize callout box border.

## 4. Protected Content
- **100% Immunity:** Do NOT change any book text, verse, title, mantra, or astrological data.

## 5. Acceptance Criteria
- Zero side-tab warnings on rounded boxes in reader documents.
