# Architecture Map — TantraGyan

## 1. System Architecture
TantraGyan is a multi-tier publishing architecture combining static and client-rendered interactive reading engines with serverless/static distribution.

```
                    ┌─────────────────────────┐
                    │    TantraGyan Core      │
                    │   Static HTML / PWA     │
                    └────────────┬────────────┘
                                 │
     ┌───────────────────────────┼───────────────────────────┐
     │                           │                           │
┌────▼─────────────┐    ┌────────▼─────────┐    ┌────────────▼─────────────┐
│  Book Reader UI  │    │  Astrology Engine│    │  Publishing Pipeline     │
│  js/book-ui.js   │    │  js/book-engine  │    │  scripts/build_*.py      │
│  js/sound.js     │    │  scripts/gen_*   │    │  Typst & Vivliostyle     │
│  css/book.css    │    │  tables_data.py  │    │  High-res Master PDFs    │
└──────────────────┘    └──────────────────┘    └──────────────────────────┘
```

## 2. Reading Engine Components
- **Turn-page & Flip Engine:** `js/book-ui.js` provides fluid page transitions with authentic 3D spatial transforms.
- **Synthesized Audio:** `js/sound.js` and `js/sounds-data.js` provide realistic parchment paper turning acoustics.
- **Search & Navigation:** In-memory keyword search across book chapters, stanzas, and planetary tables.
- **Print & PDF Layout:** Specialized print stylesheets (`bhrigu-nandi-nadi-print.html`, `tantra-sadhana-print.html`) for commercial printing.
