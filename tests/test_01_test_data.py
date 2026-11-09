#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TantraGyan QA Architecture • Pillar 1: Test Data Validation
Validates deterministic fixtures, boundary conditions, and mathematical models.
"""

import json
import os
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURES_DIR = os.path.join(BASE_DIR, "tests", "test_data")

class TestDataPillar(unittest.TestCase):
    
    def test_01_astro_fixtures_integrity(self):
        filepath = os.path.join(FIXTURES_DIR, "astro_test_fixtures.json")
        self.assertTrue(os.path.exists(filepath), f"Missing {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Verify 9 Vedic Planets
        self.assertIn("planets", data)
        self.assertEqual(len(data["planets"]), 9, "Must contain all 9 Navagrahas")
        planet_ids = [p["id"] for p in data["planets"]]
        expected_planets = ["sun", "moon", "mars", "mercury", "jupiter", "venus", "saturn", "rahu", "ketu"]
        for exp in expected_planets:
            self.assertIn(exp, planet_ids)
            
        # Verify 4 Directional Trines (Dharma, Artha, Kama, Moksha)
        self.assertIn("directional_trines", data)
        trines = data["directional_trines"]
        self.assertEqual(len(trines), 4)
        self.assertEqual(trines["east_dharma"]["signs"], [1, 5, 9])
        self.assertEqual(trines["south_artha"]["signs"], [2, 6, 10])
        self.assertEqual(trines["west_kama"]["signs"], [3, 7, 11])
        self.assertEqual(trines["north_moksha"]["signs"], [4, 8, 12])
        
    def test_02_mantra_sadhana_fixtures_math(self):
        filepath = os.path.join(FIXTURES_DIR, "mantra_sadhana_fixtures.json")
        self.assertTrue(os.path.exists(filepath), f"Missing {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        model = data["mathematical_model"]
        # Mathematical checks
        self.assertEqual(model["total_days"], 41)
        self.assertEqual(model["daily_japa"], 3049)
        self.assertGreaterEqual(model["daily_japa"] * model["total_days"], model["target_japa"],
                                "Accumulated japa must reach or exceed 1,25,000")
        
        # Mala bead checks
        full_malas = model["daily_full_malas"] * model["beads_per_mala"]
        total_daily = full_malas + model["daily_loose_beads"]
        self.assertEqual(total_daily, model["daily_japa"], "Mala arithmetic must equal daily japa")
        
        # Hawan ahuti checks
        hawan = data["hawan_editions"]
        self.assertEqual(hawan["vidhi_a_practical"]["total_ahutis"], 108)
        self.assertEqual(hawan["vidhi_b_dashansh"]["total_ahutis"], 12500)
        self.assertEqual(hawan["vidhi_b_dashansh"]["total_ahutis"], model["target_japa"] * 0.1,
                         "Dashansh must be exactly 10% of 1,25,000")
        
        # 6 Hawan ingredients check
        ingredients = data["hawan_ingredients"]
        self.assertEqual(len(ingredients), 6, "Must define exactly 6 hawan ingredients")
        for ing in ingredients:
            img_path = os.path.join(BASE_DIR, ing["file"])
            self.assertTrue(os.path.exists(img_path), f"Ingredient image {img_path} must exist locally")
            
    def test_03_user_profiles_devices(self):
        filepath = os.path.join(FIXTURES_DIR, "user_profiles.json")
        self.assertTrue(os.path.exists(filepath), f"Missing {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        self.assertIn("devices", data)
        iphone15 = next((d for d in data["devices"] if "iPhone 15" in d["name"]), None)
        self.assertIsNotNone(iphone15, "iPhone 15 test profile must exist")
        self.assertEqual(iphone15["viewport"]["width"], 393)
        self.assertEqual(iphone15["viewport"]["height"], 852)
        self.assertLessEqual(iphone15["max_nav_height_px"], 52, "Navbar on mobile must be capped at 52px")

if __name__ == "__main__":
    unittest.main()

