#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TantraGyan QA Architecture • Pillar 2: Backend Generator Tests
Validates build pipelines, file outputs, static asset dependencies, and reproducibility.
"""

import os
import unittest
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class BackendPipelinePillar(unittest.TestCase):

    def test_01_generator_scripts_exist(self):
        scripts = [
            "scripts/build_bnn_book.py",
            "scripts/build_tantra_sadhana_web.py",
            "scripts/build_full_sadhana_reader.py",
            "scripts/build_tantra_sadhana_vivliostyle.py"
        ]
        for s in scripts:
            full_path = os.path.join(BASE_DIR, s)
            self.assertTrue(os.path.exists(full_path), f"Missing generator script: {s}")
            self.assertGreater(os.path.getsize(full_path), 500, f"Script {s} is suspiciously small")

    def test_02_generated_html_files_integrity(self):
        html_targets = {
            "index.html": 80000,
            "tantra-sadhana-siddhi.html": 100000,
            "bhrigu-nandi-nadi.html": 120000,
            "sadhana-reader.html": 150000,
            "bnn-reader.html": 150000,
            "tantra-sadhana-print.html": 90000,
            "bnn.html": 120000
        }
        for filename, min_size in html_targets.items():
            path = os.path.join(BASE_DIR, filename)
            self.assertTrue(os.path.exists(path), f"Build output {filename} missing")
            size = os.path.getsize(path)
            self.assertGreater(size, min_size, f"{filename} is smaller than expected ({size} < {min_size} bytes)")

    def test_03_static_assets_presence(self):
        # 1. Hawan Images (6 sacred ingredients)
        hawan_imgs = [
            "assets/images/hawan/samidha_mango.jpg",
            "assets/images/hawan/cow_ghee.jpg",
            "assets/images/hawan/black_sesame.jpg",
            "assets/images/hawan/barley_jau.jpg",
            "assets/images/hawan/kamalgatta.jpg",
            "assets/images/hawan/hawan_samagri.jpg"
        ]
        for img in hawan_imgs:
            img_path = os.path.join(BASE_DIR, img)
            self.assertTrue(os.path.exists(img_path), f"Missing hawan asset: {img}")
            self.assertGreater(os.path.getsize(img_path), 10000, f"Corrupt image {img}")

        # 2. Sacred Yantra & SVG Icons
        yantra_path = os.path.join(BASE_DIR, "assets", "yantra.svg")
        self.assertTrue(os.path.exists(yantra_path), "Missing assets/yantra.svg")
        
        svg_icons = glob.glob(os.path.join(BASE_DIR, "assets", "icons", "*.svg"))
        self.assertGreaterEqual(len(svg_icons), 6, f"Expected at least 6 SVG diagram plates, found {len(svg_icons)}")

        # 3. CSS & JS Core Engine
        core_files = [
            "css/book.css",
            "css/tables.css",
            "js/book-engine.js",
            "js/book-ui.js",
            "js/sound.js",
            "js/sounds-data.js"
        ]
        for cf in core_files:
            cf_path = os.path.join(BASE_DIR, cf)
            self.assertTrue(os.path.exists(cf_path), f"Missing core file: {cf}")

if __name__ == "__main__":
    unittest.main()
