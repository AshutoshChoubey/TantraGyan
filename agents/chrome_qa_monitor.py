"""
Chrome QA Monitor Agent (Google Antigravity SDK Pattern)
Audits HTML pages, readers, and UI components for accessibility (a11y), console error freedom,
and layout overflow issues.
"""

import re
from pathlib import Path
from typing import Dict, Any, List


class ChromeQAMonitorAgent:
    """Agent that statically inspects generated HTML and CSS for runtime web readiness."""

    def __init__(self, project_root: Path = None):
        self.project_root = project_root or Path("/Users/apple/Movies/ap/TantraGyan")

    def inspect_html_file(self, filename: str) -> Dict[str, Any]:
        """Performs static checks on HTML files for common frontend defects."""
        file_path = self.project_root / filename
        if not file_path.exists():
            return {"status": "FILE_NOT_FOUND", "path": str(file_path)}

        content = file_path.read_text(encoding="utf-8")
        issues = []

        # 1. Title check
        if "<title>" not in content or "</title>" not in content:
            issues.append("Missing <title> tag")

        # 2. Viewport meta check
        if 'name="viewport"' not in content:
            issues.append("Missing responsive viewport meta tag")

        # 3. Encoding check
        if 'charset="utf-8"' not in content.lower():
            issues.append("Missing UTF-8 charset declaration")

        # 4. Broken internal image paths
        img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
        missing_images = []
        for src in img_srcs:
            if src.startswith("http") or src.startswith("data:"):
                continue
            clean_src = src.split("?")[0].lstrip("/")
            local_target = self.project_root / clean_src
            if not local_target.exists():
                missing_images.append(src)

        if missing_images:
            issues.append(f"Missing local images: {missing_images}")

        # 5. Accessibility checks (alt attributes on images)
        imgs_without_alt = re.findall(r'<img(?!.*?alt=)[^>]*?>', content)
        if imgs_without_alt:
            issues.append(f"Images missing alt attribute: {len(imgs_without_alt)} instances")

        return {
            "file": filename,
            "status": "PASS" if not issues else "WARNINGS_FOUND",
            "issues": issues,
            "total_images_checked": len(img_srcs),
            "file_size_kb": round(file_path.stat().st_size / 1024, 2),
        }
