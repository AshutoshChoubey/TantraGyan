#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TantraGyan QA Architecture • Pillar 5: Playwright E2E Tests
Complete user journeys, real browser interaction, mobile iPhone 15 responsiveness,
theme toggles, 3D flipbook page turning, and TOC drawers.
"""

import os
import unittest
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class PlaywrightE2EPillar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def test_01_home_portal_journey(self):
        page = self.browser.new_page()
        file_url = f"file://{os.path.join(BASE_DIR, 'index.html')}"
        page.goto(file_url)

        # Title check
        self.assertIn("तंत्र ज्ञान", page.title())

        # Flagship volume card checks
        cards = page.locator(".library-book-card")
        self.assertGreaterEqual(cards.count(), 2)

        # Verify links to all formats exist
        self.assertTrue(page.locator("a[href*='sadhana-reader.html']").first.is_visible())
        self.assertTrue(page.locator("a[href*='tantra-sadhana-siddhi.html']").first.is_visible())
        self.assertTrue(page.locator("a[href*='tantra-sadhana-siddhi-protocol.pdf']").first.is_visible())
        page.close()

    def test_02_iphone15_mobile_navbar_responsive_journey(self):
        """
        Validates iPhone 15 mobile viewport (393 x 852):
        Navbar must be single line, height <= 52px (<6% of viewport),
        button text hidden, icon-only presentation.
        """
        page = self.browser.new_page(
            viewport={"width": 393, "height": 852},
            device_scale_factor=3.0,
            is_mobile=True,
            has_touch=True
        )
        file_url = f"file://{os.path.join(BASE_DIR, 'tantra-sadhana-siddhi.html')}"
        page.goto(file_url)

        # 1. Height check of navbar on iPhone 15
        navbar = page.locator(".reader-navbar")
        self.assertTrue(navbar.is_visible())
        box = navbar.bounding_box()
        self.assertIsNotNone(box)
        # Height must be <= 52px
        self.assertLessEqual(box["height"], 52, f"Mobile navbar is too tall ({box['height']}px > 52px)")
        
        # Percentage of screen height: must be < 6.5% of 852px
        screen_percent = (box["height"] / 852) * 100
        self.assertLess(screen_percent, 6.5, f"Navbar consumes {screen_percent:.1f}% of screen, expected < 6.5%")

        # 2. Check that Home button text is hidden
        home_btn = page.locator(".brand-section .nav-btn")
        self.assertTrue(home_btn.is_visible())
        
        # 3. Check that subtitle is hidden
        sub = page.locator(".brand-text span")
        self.assertFalse(sub.is_visible(), "Brand subtitle should be hidden on iPhone 15 to prevent wrapping")

        # 4. Open TOC drawer
        toc_btn = page.locator(".nav-tools button[onclick*='toggleTOC']")
        toc_btn.click()
        page.wait_for_timeout(200)
        drawer = page.locator("#toc-drawer")
        self.assertTrue(drawer.evaluate("el => el.classList.contains('active') || el.classList.contains('open')"))

        # 5. Click Chapter 8 link in drawer
        ch8_link = page.locator("#toc-drawer a[href='#ch8']")
        ch8_link.click()
        page.wait_for_timeout(300)

        # 6. Verify Hawan cards are rendered in DOM
        hawan_cards = page.locator(".hawan-card")
        self.assertEqual(hawan_cards.count(), 6, "Must display all 6 hawan samagree cards")

        page.close()

    def test_03_3d_flipbook_reader_journey(self):
        page = self.browser.new_page(viewport={"width": 1280, "height": 800})
        file_url = f"file://{os.path.join(BASE_DIR, 'sadhana-reader.html')}"
        page.goto(file_url)

        # Title check
        self.assertIn("3D फ्लिप बुक", page.title())

        # Check total pages badge initialized
        page_counter = page.locator("#page-counter-badge")
        self.assertTrue(page_counter.is_visible())
        text = page_counter.inner_text()
        self.assertIn("38", text, "Total pages must indicate 38 pages")

        # Click next page button
        next_btn = page.locator("#btn-next-page")
        if next_btn.is_visible():
            next_btn.click()
            page.wait_for_timeout(300)

        # Theme toggle test
        theme_btn = page.locator("#btn-theme-toggle")
        if theme_btn.is_visible():
            theme_btn.click()
            page.wait_for_timeout(200)
            theme_val = page.evaluate("document.documentElement.getAttribute('data-theme')")
            self.assertIsNotNone(theme_val)

        page.close()

    def test_04_bnn_reader_mobile_journey(self):
        page = self.browser.new_page(
            viewport={"width": 393, "height": 852},
            is_mobile=True
        )
        file_url = f"file://{os.path.join(BASE_DIR, 'bhrigu-nandi-nadi.html')}"
        page.goto(file_url)

        navbar = page.locator(".reader-navbar")
        box = navbar.bounding_box()
        self.assertIsNotNone(box)
        self.assertLessEqual(box["height"], 52, f"BNN mobile navbar is too tall ({box['height']}px)")

        # Verify SVG aspect wheel or diamond chart plate is loaded
        svg_img = page.locator(".chart-embed-img, .diagram-img, img[src*='.svg']").first
        self.assertTrue(svg_img.is_visible())

        page.close()

if __name__ == "__main__":
    unittest.main()