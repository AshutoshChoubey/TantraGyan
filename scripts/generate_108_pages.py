#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aggregates all 108 sacred pages of the Vedic Kundali Ganita Vichar Mahagranth.
Tantra Gyan Research Center • https://t.worldgyan.com
"""

import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CURRENT_DIR))

from pages_part1 import get_pages_part1
from pages_part2 import get_pages_part2
from pages_part3 import get_pages_part3
from pages_part4 import get_pages_part4

def get_all_108_pages():
    all_pages = []
    all_pages.extend(get_pages_part1())
    all_pages.extend(get_pages_part2())
    all_pages.extend(get_pages_part3())
    all_pages.extend(get_pages_part4())
    return all_pages

if __name__ == "__main__":
    pages = get_all_108_pages()
    print(f"✓ Successfully generated {len(pages)} sacred pages for the 3D Flipbook Reader!")
