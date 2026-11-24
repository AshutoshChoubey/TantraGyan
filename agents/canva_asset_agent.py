"""
Canva Asset & Bulk Design Agent for Tantra Gyan
Part of the Google Antigravity SDK Multi-Agent Suite for Flagship Vol 4.

Automates:
1. Canva folder management (Folder ID: FAHbySExszs)
2. Bulk-creation dataset generation (CSV / JSON) for all 13 chapters
3. Design template specification mapping
"""

import os
import json
import csv
from typing import Dict, Any, List
try:
    from .config import CHAPTER_ROSTER, BOOK_META, THEME_CONFIG
except (ImportError, ValueError):
    from config import CHAPTER_ROSTER, BOOK_META, THEME_CONFIG

CANVA_FOLDER_ID = "FAHbySExszs"
CANVA_FOLDER_NAME = "Tantra Gyan - Kundali Ganita Vichar Mahagranth"

class CanvaAssetAgent:
    def __init__(self, output_dir: str = "data/canva"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_bulk_dataset(self) -> str:
        """Generates a high-quality CSV dataset for Canva bulk create."""
        csv_path = os.path.join(self.output_dir, "kundali_ganita_bulk_cards.csv")
        
        fieldnames = [
            "Chapter_Number",
            "Hindi_Title",
            "English_Concept",
            "Lead_Parable",
            "Core_Formula_Rule",
            "Life_Takeaway",
            "Theme_Primary_Color",
            "Theme_Secondary_Color",
            "Book_Title"
        ]

        rows = []
        for ch in CHAPTER_ROSTER:
            rows.append({
                "Chapter_Number": f"अध्याय {ch['num']:02d}",
                "Hindi_Title": ch["hi_title"],
                "English_Concept": ch["en_title"],
                "Lead_Parable": f"जैसे {ch['hi_title']} ब्रह्मांडीय लय को नियंत्रित करता है, वैसे ही मानव चेतना का क्रम निर्धारित होता है।",
                "Core_Formula_Rule": f"गणितीय सूत्र: {ch['engine_file']} से व्युत्पन्न प्रत्यक्ष गणना।",
                "Life_Takeaway": f"{ch['hi_title']} के ज्ञान से साधक अपने कर्म और काल के समन्वय को साधता है।",
                "Theme_Primary_Color": THEME_CONFIG["primary_emerald"],
                "Theme_Secondary_Color": THEME_CONFIG["accent_cyan"],
                "Book_Title": BOOK_META["title_hi"]
            })

        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"[CanvaAssetAgent] Bulk dataset exported: {csv_path} ({len(rows)} chapters)")
        return csv_path

    def get_canva_spec(self) -> Dict[str, Any]:
        """Returns Canva folder specification and integration metadata."""
        return {
            "canva_folder_id": CANVA_FOLDER_ID,
            "canva_folder_name": CANVA_FOLDER_NAME,
            "folder_url": f"https://www.canva.com/folder/{CANVA_FOLDER_ID}",
            "brand_kit_id": "kAFsa11bjyE",
            "primary_colors": [
                THEME_CONFIG["primary_emerald"],
                THEME_CONFIG["accent_cyan"],
                THEME_CONFIG["gold_accent"]
            ],
            "chapters_indexed": len(CHAPTER_ROSTER)
        }

if __name__ == "__main__":
    agent = CanvaAssetAgent()
    agent.generate_bulk_dataset()
    spec = agent.get_canva_spec()
    print("[CanvaAssetAgent] Spec:", json.dumps(spec, indent=2, ensure_ascii=False))
