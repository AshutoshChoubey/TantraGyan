#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TantraGyan QA Architecture • Pillar 7: Security Testing
Validates XSS injection guards, path traversal safety, asset integrity,
git remote push whitelist guard, and secret/credential leakage audit.
"""

import os
import re
import subprocess
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class SecurityTestingPillar(unittest.TestCase):

    def test_01_git_remote_push_whitelist_guard(self):
        """
        Critical Operational Safety Invariant:
        Push code, commits, and branches STRICTLY AND ONLY to repositories
        under the personal GitHub account: https://github.com/AshutoshChoubey/*
        """
        result = subprocess.run(
            ["git", "-C", BASE_DIR, "remote", "-v"],
            capture_output=True, text=True, check=True
        )
        remotes = result.stdout.strip().splitlines()
        self.assertGreater(len(remotes), 0, "No git remotes configured")
        
        for line in remotes:
            parts = line.split()
            if len(parts) >= 2:
                remote_name, remote_url = parts[0], parts[1]
                # Check whitelist
                is_whitelisted = (
                    remote_url.startswith("https://github.com/AshutoshChoubey/") or
                    remote_url.startswith("git@github.com:AshutoshChoubey/")
                )
                self.assertTrue(
                    is_whitelisted,
                    f"PROHIBITED REMOTE DETECTED: Remote '{remote_name}' points to '{remote_url}'. Must strictly point to AshutoshChoubey!"
                )

    def test_02_xss_and_input_sanitization_in_scripts(self):
        js_files = [
            os.path.join(BASE_DIR, "js", "book-engine.js"),
            os.path.join(BASE_DIR, "js", "book-ui.js")
        ]
        for js_path in js_files:
            if not os.path.exists(js_path):
                continue
            with open(js_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Disallow dangerous eval()
            self.assertNotIn("eval(", content, f"Dangerous eval() found in {js_path}")
            
            # Check for URL hash page integer clamping
            if "window.location.hash" in content:
                self.assertIn("parseInt", content, f"URL hash must be sanitized with parseInt in {js_path}")

    def test_03_secure_https_external_assets(self):
        html_files = [
            os.path.join(BASE_DIR, "index.html"),
            os.path.join(BASE_DIR, "tantra-sadhana-siddhi.html"),
            os.path.join(BASE_DIR, "bhrigu-nandi-nadi.html"),
            os.path.join(BASE_DIR, "sadhana-reader.html")
        ]
        http_insecure_pattern = re.compile(r'(?:src|href)=["\']http://[^"\']+["\']')
        for hpath in html_files:
            with open(hpath, "r", encoding="utf-8") as f:
                content = f.read()
            insecure_links = http_insecure_pattern.findall(content)
            self.assertEqual(
                len(insecure_links), 0,
                f"Insecure HTTP assets detected in {os.path.basename(hpath)}: {insecure_links}"
            )

    def test_04_secrets_and_private_keys_leak_audit(self):
        """
        Scans all tracked files for accidental leaks of tokens, keys, or private certs.
        """
        sensitive_patterns = [
            (re.compile(r'-----BEGIN (?:RSA )?PRIVATE KEY-----'), "Private Key Header"),
            (re.compile(r'ghp_[A-Za-z0-9]{36}'), "GitHub Personal Access Token"),
            (re.compile(r'AKIA[0-9A-Z]{16}'), "AWS Access Key ID")
        ]
        
        # Check files in BASE_DIR (excluding .git, venvs, node_modules)
        ignore_dirs = {".git", ".gemini", ".venv", "venv", "node_modules", "dist", "build"}
        for root, dirs, files in os.walk(BASE_DIR):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            for fname in files:
                if fname.endswith((".html", ".js", ".css", ".py", ".json", ".md")):
                    fpath = os.path.join(root, fname)
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                    for pattern, desc in sensitive_patterns:
                        self.assertIsNone(
                            pattern.search(text),
                            f"Sensitive credential ({desc}) leaked in file: {os.path.relpath(fpath, BASE_DIR)}"
                        )

if __name__ == "__main__":
    unittest.main()