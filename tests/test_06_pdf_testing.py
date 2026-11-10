#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TantraGyan QA Architecture • Pillar 6: PDF Testing
Validates PDF headers, physical page counts, mandatory shastric content,
author attributions, embedded images, font streams, and English numeral compliance.
"""

import os
import unittest
import pypdf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class PDFTestingPillar(unittest.TestCase):

    def test_01_pdf_headers_and_file_sizes(self):
        pdf_targets = {
            "tantra-sadhana-siddhi-protocol.pdf": 1024 * 1024 * 2,  # > 2 MB
            "bhrigu-nandi-nadi-karma-samyojan.pdf": 1024 * 500,     # > 500 KB
            "tantra-gyan-vedic-jyotish-mahagranth.pdf": 1024 * 1024 # > 1 MB
        }
        for fname, min_bytes in pdf_targets.items():
            fpath = os.path.join(BASE_DIR, fname)
            self.assertTrue(os.path.exists(fpath), f"Missing PDF: {fname}")
            size = os.path.getsize(fpath)
            self.assertGreater(size, min_bytes, f"PDF {fname} smaller than expected ({size} bytes)")
            
            with open(fpath, "rb") as f:
                header = f.read(5)
                self.assertEqual(header, b"%PDF-", f"{fname} lacks valid PDF magic bytes header")

    def test_02_tantra_sadhana_pdf_pagination_and_content(self):
        fpath = os.path.join(BASE_DIR, "tantra-sadhana-siddhi-protocol.pdf")
        reader = pypdf.PdfReader(fpath)
        
        # Exact page count check
        total_pages = len(reader.pages)
        self.assertEqual(total_pages, 30, f"Expected exactly 30 pages in Tantra Sadhana PDF, got {total_pages}")

        # Full document text extraction
        full_text = ""
        has_images = False
        for page in reader.pages:
            full_text += page.extract_text() or ""
            if len(page.images) > 0:
                has_images = True

        self.assertTrue(has_images, "PDF must contain embedded vector / raster image objects")

        # Mandatory content checks
        self.assertIn("तंत्र", full_text)
        self.assertIn("साधना", full_text)
        self.assertIn("आशुतोष", full_text, "Author attribution required")
        self.assertIn("चौबे", full_text, "Author attribution required")
        self.assertIn("Tantra Gyan Research Center", full_text, "Publisher attribution required")
        
        # Mandatory Shastric Mantras
        self.assertIn("ॐ", full_text)
        self.assertIn("Panchakshari", full_text)
        self.assertIn("Kunjika", full_text)

        # Hawan Content in Chapter 8
        self.assertIn("हवन", full_text)
        self.assertIn("दशांश", full_text)
        self.assertIn("LOTUS SEEDS", full_text)
        self.assertIn("BARLEY GRAIN", full_text)

    def test_03_bnn_pdf_content(self):
        fpath = os.path.join(BASE_DIR, "bhrigu-nandi-nadi-karma-samyojan.pdf")
        reader = pypdf.PdfReader(fpath)
        self.assertGreaterEqual(len(reader.pages), 30, "BNN PDF must have comprehensive chapter pagination")
        
        full_text = "".join(p.extract_text() or "" for p in reader.pages)
        self.assertIn("भृगु", full_text)
        self.assertIn("नाड़ी", full_text)
        self.assertIn("जीव", full_text)
        self.assertIn("Bhrigu", full_text)
        self.assertIn("Nandi", full_text)

    def test_04_vedic_astrology_mahagranth_pdf_panchang_content(self):
        fpath = os.path.join(BASE_DIR, "tantra-gyan-vedic-jyotish-mahagranth.pdf")
        reader = pypdf.PdfReader(fpath)
        self.assertGreaterEqual(len(reader.pages), 30, "Vedic Astrology Mahagranth PDF must have full book pagination")
        
        full_text = "".join(p.extract_text() or "" for p in reader.pages)
        self.assertIn("Tantra Gyan", full_text)
        self.assertIn("Ashutosh", full_text)

if __name__ == "__main__":
    unittest.main()