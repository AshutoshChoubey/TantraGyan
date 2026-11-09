#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TantraGyan QA Architecture • Pillar 3: Frontend Validation Tests
Validates HTML syntax, DOM hierarchy, navigation bar responsiveness, sections, and theme support.
"""

import os
import re
import unittest
from html.parser import HTMLParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_tags:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack.pop()
        if last_tag != tag:
            self.errors.append(f"Mismatched tags: opened <{last_tag}> at line {pos[0]} but closed </{tag}> at line {self.getpos()[0]}")

class FrontendValidationPillar(unittest.TestCase):

    def test_01_html_tag_validity(self):
        html_files = [
            "index.html",
            "tantra-sadhana-siddhi.html",
            "bhrigu-nandi-nadi.html",
            "sadhana-reader.html",
            "bnn-reader.html"
        ]
        for fname in html_files:
            fpath = os.path.join(BASE_DIR, fname)
            v = TagValidator()
            with open(fpath, "r", encoding="utf-8") as f:
                v.feed(f.read())
            self.assertEqual(len(v.errors), 0, f"HTML tag errors in {fname}: {v.errors[:3]}")

    def test_02_mobile_navbar_responsive_css(self):
        readers = ["tantra-sadhana-siddhi.html", "bhrigu-nandi-nadi.html"]
        for r in readers:
            fpath = os.path.join(BASE_DIR, r)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Verify media query for mobile <= 768px
            self.assertIn("@media (max-width: 768px)", content, f"Missing mobile media query in {r}")
            
            # Verify navbar height constraint (must be 48px to occupy < 6% screen)
            self.assertTrue(
                "height: 48px;" in content or "max-height: 48px;" in content,
                f"Navbar height must be explicitly restricted to 48px in {r}"
            )
            
            # Verify text hiding on mobile for icon-only presentation
            self.assertIn(".brand-section .nav-btn span:last-child", content)
            self.assertIn(".nav-tools .nav-btn span:last-child", content)
            self.assertIn(".brand-text span", content)

    def test_03_chapter_sections_presence(self):
        web_reader = os.path.join(BASE_DIR, "tantra-sadhana-siddhi.html")
        with open(web_reader, "r", encoding="utf-8") as f:
            html = f.read()

        for ch_num in range(1, 9):
            ch_id = f'id="ch{ch_num}"'
            self.assertIn(ch_id, html, f"Missing Chapter {ch_num} section in Tantra Sadhana web reader")

        # Verify Hawan Samagree Gallery Grid with 6 cards
        self.assertIn('class="hawan-gallery-grid"', html)
        hawan_cards = re.findall(r'class="hawan-card"', html)
        self.assertEqual(len(hawan_cards), 6, "Expected exactly 6 hawan samagree cards in Chapter 8")

    def test_04_theme_support(self):
        fpath = os.path.join(BASE_DIR, "tantra-sadhana-siddhi.html")
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn('toggleTheme()', html, "Theme toggle function must be wired")
        self.assertIn('[data-theme="dark"]', html, "Dark theme CSS must be present")

if __name__ == "__main__":
    unittest.main()

