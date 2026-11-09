#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TantraGyan Master QA Architecture Test Runner
Executes all 8 QA Pillars and outputs a structured Executive Quality Audit Report.

Pillars:
  1. Test Data (Fixtures, Boundaries & Mathematical Models)
  2. Backend Tests (Pipelines, Build Outputs, Static Assets)
  3. Frontend Tests (DOM Tag Balancing, Navbar, Responsive CSS, Themes)
  4. Unit Tests (Numeral Invariants, Japa Arithmetic, BNN Trine Algorithms)
  5. Playwright E2E Tests (Real Chromium Headless User Journeys & Mobile iPhone 15)
  6. PDF Testing (Headers, Page Counts, Mandated Mantras, Images)
  7. Security Testing (XSS Injection, Path Traversal, Git Whitelist, Secret Leaks)
  8. Google Gemini AI Audit (Sanskrit Shastra Verification & Senior Code Quality)
"""

import sys
import os
import time
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

def run_suite():
    print("\n" + "=" * 76)
    print("🔱  TANTRA GYAN • COMPLETE QA ARCHITECTURE TEST RUNNER  🔱")
    print("    Author: Astrologer Ashutosh Kumar Choubey")
    print("    Platform: Tantra Gyan Research Center (t.worldgyan.com)")
    print("=" * 76 + "\n")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    test_modules = [
        ("Pillar 1: Test Data", "tests.test_01_test_data"),
        ("Pillar 2: Backend Tests", "tests.test_02_backend"),
        ("Pillar 3: Frontend Tests", "tests.test_03_frontend"),
        ("Pillar 4: Unit Tests", "tests.test_04_unit_tests"),
        ("Pillar 5: Playwright E2E", "tests.test_05_playwright_e2e"),
        ("Pillar 6: PDF Testing", "tests.test_06_pdf_testing"),
        ("Pillar 7: Security Testing", "tests.test_07_security_testing"),
        ("Pillar 8: Gemini AI Audit", "tests.test_08_gemini_ai_audit"),
    ]

    results_summary = []
    total_ran = 0
    total_failures = 0
    total_errors = 0
    start_time = time.time()

    for pillar_name, mod_name in test_modules:
        print(f"▶ Running {pillar_name} ({mod_name})...")
        t0 = time.time()
        mod_suite = loader.loadTestsFromName(mod_name)
        runner = unittest.TextTestRunner(verbosity=1)
        res = runner.run(mod_suite)
        dur = time.time() - t0
        
        status = "PASSED ✅" if res.wasSuccessful() else "FAILED ❌"
        results_summary.append((pillar_name, res.testsRun, len(res.failures), len(res.errors), dur, status))
        total_ran += res.testsRun
        total_failures += len(res.failures)
        total_errors += len(res.errors)
        print("-" * 76)

    total_duration = time.time() - start_time

    # Output Executive Quality Table
    print("\n" + "=" * 76)
    print("📋  EXECUTIVE QA ARCHITECTURE SCORECARD")
    print("=" * 76)
    print(f"{'Pillar Name':<30} | {'Tests':<6} | {'Fail':<5} | {'Err':<4} | {'Time (s)':<8} | {'Status'}")
    print("-" * 76)
    for p_name, tests_cnt, fails, errs, dur, stat in results_summary:
        print(f"{p_name:<30} | {tests_cnt:<6} | {fails:<5} | {errs:<4} | {dur:<8.2f} | {stat}")
    print("-" * 76)
    print(f"TOTAL: {total_ran} tests executed across 8 pillars in {total_duration:.2f} seconds.")
    
    if total_failures == 0 and total_errors == 0:
        print("\n🎉 ALL 8 QA PILLARS PASSED 100%! SYSTEM PRODUCTION READY.")
        return 0
    else:
        print(f"\n⚠️ QA RUN FAILED: {total_failures} failures, {total_errors} errors detected.")
        return 1

if __name__ == "__main__":
    exit_code = run_suite()
    sys.exit(exit_code)
