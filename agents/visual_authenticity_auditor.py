"""
Visual Authenticity Auditor Agent (Google Antigravity SDK Pattern)
Audits generated books, readers, and templates against Impeccable visual quality standards
to eliminate AI tropes and ensure sacred manuscript aesthetics.
"""

import subprocess
import json
from pathlib import Path
from typing import Dict, Any, List


class VisualAuthenticityAuditorAgent:
    """Agent that runs automated visual authenticity scans via the Impeccable engine."""

    def __init__(self, project_root: Path = None):
        self.project_root = project_root or Path("/Users/apple/Movies/ap/TantraGyan")
        self.engine_script = self.project_root / "visual-authenticity" / "bin" / "engine.mjs"

    def run_detection(self) -> Dict[str, Any]:
        """Runs the detection command and parses raw findings."""
        if not self.engine_script.exists():
            return {
                "status": "SKIPPED",
                "message": f"Engine script not found at {self.engine_script}",
            }

        try:
            res = subprocess.run(
                ["node", str(self.engine_script), "detect"],
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=False,
            )

            results_file = self.project_root / "visual-authenticity" / "audit" / "DETECTION_RESULTS.json"
            total_findings = 0
            if results_file.exists():
                with open(results_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    total_findings = len(data) if isinstance(data, list) else data.get("total", 0)

            return {
                "status": "COMPLETED",
                "exit_code": res.returncode,
                "total_findings": total_findings,
                "stdout": res.stdout.strip(),
                "results_file": str(results_file),
            }
        except Exception as e:
            return {
                "status": "ERROR",
                "error": str(e),
            }

    def check_status(self) -> Dict[str, Any]:
        """Checks the visual authenticity workspace configuration."""
        try:
            res = subprocess.run(
                ["node", str(self.engine_script), "status"],
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=False,
            )
            return {
                "status": "OK" if res.returncode == 0 else "FAIL",
                "output": res.stdout.strip(),
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}
