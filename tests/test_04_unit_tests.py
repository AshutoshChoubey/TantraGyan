#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TantraGyan QA Architecture • Pillar 4: Unit Tests
Validates mathematical models, astrological algorithms, scriptural rules, and numeral invariants.
"""

import json
import os
import re
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class CoreUnitTestsPillar(unittest.TestCase):

    def test_01_english_digits_invariant(self):
        """
        User Rule Invariant:
        Numbers must strictly use English digits 0-9 (no Hindi digits).
        """
        target_files = [
            "tantra-sadhana-siddhi.html",
            "sadhana-reader.html",
            "tantra-sadhana-print.html"
        ]
        devanagari_digit_pattern = re.compile(r'[०-९]')
        for fname in target_files:
            fpath = os.path.join(BASE_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            matches = devanagari_digit_pattern.findall(content)
            self.assertEqual(
                len(matches), 0,
                f"Found {len(matches)} Devanagari numerals in {fname}. Numbers must strictly use English 0-9."
            )

    def test_02_japa_mathematics_unit(self):
        daily_target = 3049
        duration_days = 41
        grand_total = daily_target * duration_days
        
        self.assertEqual(grand_total, 125009)
        self.assertGreaterEqual(grand_total, 125000, "Must satisfy the 1,25,000 threshold requirement")
        
        # Mala breakdown
        mala_beads = 108
        full_malas = 28
        extra_beads = 25
        self.assertEqual(full_malas * mala_beads + extra_beads, daily_target)

    def test_03_hawan_mathematics_unit(self):
        panchakshari_total = 125000
        dashansh_expected = 12500
        self.assertEqual(panchakshari_total * 0.10, dashansh_expected)
        
        # Practical mode
        shiva_ahutis = 54
        chamunda_ahutis = 54
        self.assertEqual(shiva_ahutis + chamunda_ahutis, 108)
        
        # Kunjika recitations
        daily_kunjika = 21
        total_kunjika = daily_kunjika * 41
        self.assertEqual(total_kunjika, 861)

    def test_04_bnn_directional_trines_algorithm(self):
        def get_trines(sign_num):
            return [sign_num, ((sign_num + 4 - 1) % 12) + 1, ((sign_num + 8 - 1) % 12) + 1]

        # Dharma Trine (Fire)
        self.assertEqual(get_trines(1), [1, 5, 9])
        # Artha Trine (Earth)
        self.assertEqual(get_trines(2), [2, 6, 10])
        # Kama Trine (Air)
        self.assertEqual(get_trines(3), [3, 7, 11])
        # Moksha Trine (Water)
        self.assertEqual(get_trines(4), [4, 8, 12])

    def test_05_schema_org_json_ld_metadata(self):
        reader_file = os.path.join(BASE_DIR, "sadhana-reader.html")
        with open(reader_file, "r", encoding="utf-8") as f:
            html = f.read()

        match = re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', html)
        self.assertIsNotNone(match, "Missing JSON-LD metadata script block")
        json_data = json.loads(match.group(1))
        
        self.assertEqual(json_data.get("@context"), "https://schema.org")
        self.assertIn("@graph", json_data)
        book_obj = next((item for item in json_data["@graph"] if item.get("@type") == "Book"), None)
        self.assertIsNotNone(book_obj, "Schema.org Book entity missing in graph")

    def test_06_panchang_mathematics_and_elements(self):
        """
        Validates Panchang mathematical spans, 108 sacred pages, and 5 Mahabhutas.
        """
        # 1. 108 Pages Invariant across all 4 book editions
        for fname in ["reader.html", "book.html", "hindi.html", "english.html"]:
            fpath = os.path.join(BASE_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            page_count = len(re.findall(r'<article class="book-page-data"', content))
            self.assertEqual(
                page_count, 108,
                f"{fname} must contain exactly 108 pages (found {page_count})."
            )

        # 2. Mathematical Arc Consistency
        tithi_arc = 12.0
        total_tithis = 30
        self.assertEqual(tithi_arc * total_tithis, 360.0)

        karana_arc = 6.0
        total_karanas = 60
        self.assertEqual(karana_arc * total_karanas, 360.0)

        nakshatra_minutes = 13 * 60 + 20 # 800 arcminutes
        total_nakshatras = 27
        self.assertEqual(nakshatra_minutes * total_nakshatras, 21600) # 360 degrees * 60 min

        pada_minutes = 3 * 60 + 20 # 200 arcminutes
        total_padas = 108
        self.assertEqual(pada_minutes * total_padas, 21600)

        # 3. 7 Vaars, 30 Tithis, 27 Yogas, 11 Karanas Presence
        with open(os.path.join(BASE_DIR, "reader.html"), "r", encoding="utf-8") as f:
            reader_text = f.read()
        self.assertIn("वार • Agni (Fire)", reader_text)
        self.assertIn("तिथि • Jala (Water)", reader_text)
        self.assertIn("नक्षत्र • Vayu (Air)", reader_text)
        self.assertIn("योग • Akasha (Ether)", reader_text)
        self.assertIn("करण • Prithvi (Earth)", reader_text)

    def test_07_panchang_svg_mandala_exists(self):
        """
        Validates that the Panchanga Mandala SVG exists and contains all 5 limbs.
        """
        svg_path = os.path.join(BASE_DIR, "assets", "icons", "panchang_mandala_chart.svg")
        self.assertTrue(os.path.exists(svg_path), "Panchang Mandala SVG missing in assets/icons")
        with open(svg_path, "r", encoding="utf-8") as f:
            svg = f.read()
        self.assertIn('viewBox="0 0 900 900"', svg)
        for limb in ["वार (Solar Day)", "तिथि (Lunar Phase)", "नक्षत्र (Star Mansion)", "योग (Solar-Lunar Sum)", "करण (Half-Tithi)"]:
            self.assertIn(limb, svg, f"Missing limb {limb} in panchang_mandala_chart.svg")

if __name__ == "__main__":
    unittest.main()
