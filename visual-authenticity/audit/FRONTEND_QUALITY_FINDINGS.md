# Frontend Code Quality Findings — TantraGyan

## 1. Scope
Detailed review of CSS structure, inline styles, DOM hierarchy, and interactive book components.

## 2. Findings

### TG-CODE-001: Redundant Hardcoded Inline Styles
- Multiple callout containers in `reader.html` and `bnn.html` repeat inline `style="border-left: 4px solid ...; background: ...; border-radius: 8px;"` instead of reusing CSS classes defined in `css/tables.css` and `css/book.css`.
- **Remediation:** Centralize callout box styling into canonical utility classes.

### TG-CODE-002: Inconsistent Border Radius Standards
- Border radius values fluctuate between 4px, 6px, 8px, 14px, and 40px across different reader pages.
- **Remediation:** Standardize card containers to a coherent 8px radius standard.

### TG-CODE-003: Keyboard & Screen Reader Accessibility
- Verify all interactive chapter links, audio toggles, and search buttons have appropriate `aria-label` or `title` attributes.
