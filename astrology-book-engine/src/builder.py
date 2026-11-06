#!/usr/bin/env python3
"""
Astrology Book Publishing Engine - Master Build CLI
===================================================
Compiles Vedic Astrology manuscripts into:
1. Target 1: Vector PDF via WeasyPrint & Typst (Trade Paperback 6x9in / A5)
2. Target 2: High-Resolution Rich-Text Web Reader with Enterprise Diamond Charts

Usage:
  python3 src/builder.py --target all
  python3 src/builder.py --target pdf
  python3 src/builder.py --target web
  python3 src/builder.py --target typst
  python3 src/builder.py --serve 8899
"""

import os
import sys
import time
import shutil
import argparse
import yaml
from jinja2 import Environment, FileSystemLoader

# Root paths
ENGINE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ENGINE_ROOT, "src")
sys.path.insert(0, SRC_DIR)

from chart_generator import generate_sample_kundlis
from markdown_parser import parse_manuscript
from typst_compiler import compile_typst_book

MANUSCRIPT_DIR = os.path.join(ENGINE_ROOT, "manuscript")
ASSETS_DIR = os.path.join(ENGINE_ROOT, "assets")
TEMPLATES_DIR = os.path.join(ENGINE_ROOT, "templates")
DIST_DIR = os.path.join(ENGINE_ROOT, "dist")
DIST_PDF_DIR = os.path.join(DIST_DIR, "pdf")
DIST_WEB_DIR = os.path.join(DIST_DIR, "web")


def load_metadata():
    meta_path = os.path.join(MANUSCRIPT_DIR, "metadata.yaml")
    if not os.path.exists(meta_path):
        raise FileNotFoundError(f"Metadata file not found: {meta_path}")
    with open(meta_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_charts():
    """Generates all enterprise vector SVG charts in assets/icons/"""
    icons_dir = os.path.join(ASSETS_DIR, "icons")
    os.makedirs(icons_dir, exist_ok=True)
    samples = generate_sample_kundlis()
    for name, svg_str in samples.items():
        svg_file = os.path.join(icons_dir, f"{name}.svg")
        with open(svg_file, "w", encoding="utf-8") as f:
            f.write(svg_str)
    print(f"✓ Generated {len(samples)} enterprise astrological vector charts in {icons_dir}")


def parse_all_chapters(metadata):
    """Parses all chapters listed in metadata.yaml."""
    chapters = []
    chapter_defs = metadata.get("chapters", [])

    for ch_info in chapter_defs:
        ch_file = os.path.join(MANUSCRIPT_DIR, ch_info["file"])
        if not os.path.exists(ch_file):
            print(f"⚠️ Warning: Chapter file not found: {ch_file}")
            continue

        with open(ch_file, "r", encoding="utf-8") as f:
            raw_text = f.read()

        ch_meta, html_body = parse_manuscript(raw_text)
        merged_ch = {
            "id": ch_info.get("id", os.path.splitext(ch_info["file"])[0]),
            "file": ch_info["file"],
            "number": ch_info.get("number", ""),
            "title": ch_info.get("title", ""),
            "english_title": ch_info.get("english_title", ""),
            "raw_text": raw_text,
            "html_content": html_body
        }
        chapters.append(merged_ch)

    print(f"✓ Successfully parsed {len(chapters)} chapters")
    return chapters


def build_pdf_target(metadata, chapters):
    """Target 1: Compiles Trade Paperback Vector PDF via WeasyPrint"""
    print("\n--- Compiling Target 1: Vector PDF (WeasyPrint) ---")
    start_time = time.time()

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template("layout.html")

    html_out = template.render(
        meta=metadata,
        chapters=chapters,
        target="pdf"
    )

    os.makedirs(DIST_PDF_DIR, exist_ok=True)
    pdf_html_path = os.path.join(DIST_PDF_DIR, "index_pdf.html")
    with open(pdf_html_path, "w", encoding="utf-8") as f:
        f.write(html_out)

    shutil.copy(os.path.join(TEMPLATES_DIR, "print.css"), os.path.join(DIST_PDF_DIR, "print.css"))
    dist_pdf_assets = os.path.join(DIST_PDF_DIR, "assets")
    if os.path.exists(dist_pdf_assets):
        shutil.rmtree(dist_pdf_assets)
    shutil.copytree(ASSETS_DIR, dist_pdf_assets)

    output_pdf = os.path.join(DIST_PDF_DIR, "astrology-book.pdf")

    import weasyprint

    print("Executing WeasyPrint vector rendering...")
    wp = weasyprint.HTML(filename=pdf_html_path, base_url=DIST_PDF_DIR)
    wp.write_pdf(output_pdf)

    elapsed = time.time() - start_time
    size_mb = os.path.getsize(output_pdf) / (1024 * 1024)
    print(f"✓ Target 1 (WeasyPrint) Complete: {output_pdf}")
    print(f"  • Size: {size_mb:.2f} MB | Compile Duration: {elapsed:.2f}s")
    return output_pdf


def build_typst_target(metadata, chapters):
    """Target 1B: Compiles Ultra-High Resolution PDF via Typst"""
    print("\n--- Compiling Target 1B: Vector PDF (Typst Engine) ---")
    start_time = time.time()
    os.makedirs(DIST_PDF_DIR, exist_ok=True)
    output_typst_pdf = os.path.join(DIST_PDF_DIR, "astrology-book-typst.pdf")

    compile_typst_book(metadata, chapters, output_typst_pdf, ENGINE_ROOT)

    elapsed = time.time() - start_time
    size_mb = os.path.getsize(output_typst_pdf) / (1024 * 1024)
    print(f"✓ Target 1B (Typst) Complete: {output_typst_pdf}")
    print(f"  • Size: {size_mb:.2f} MB | Compile Duration: {elapsed:.2f}s")
    return output_typst_pdf


def build_web_target(metadata, chapters, pdf_path=None):
    """Target 2: Modern Rich-Text Book Reader with Enterprise Diamond Charts"""
    print("\n--- Compiling Target 2: Modern Rich-Text Web Reader ---")
    start_time = time.time()

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template("layout.html")

    html_out = template.render(
        meta=metadata,
        chapters=chapters,
        target="web"
    )

    os.makedirs(DIST_WEB_DIR, exist_ok=True)

    # 1. Entrypoint HTML
    index_html_path = os.path.join(DIST_WEB_DIR, "index.html")
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(html_out)

    # 2. Copy CSS & Assets
    shutil.copy(os.path.join(TEMPLATES_DIR, "print.css"), os.path.join(DIST_WEB_DIR, "print.css"))
    shutil.copy(os.path.join(TEMPLATES_DIR, "web-reader.css"), os.path.join(DIST_WEB_DIR, "web-reader.css"))

    dist_web_assets = os.path.join(DIST_WEB_DIR, "assets")
    if os.path.exists(dist_web_assets):
        shutil.rmtree(dist_web_assets)
    shutil.copytree(ASSETS_DIR, dist_web_assets)

    os.makedirs(os.path.join(dist_web_assets, "js"), exist_ok=True)
    shutil.copy(os.path.join(TEMPLATES_DIR, "web-reader.js"), os.path.join(dist_web_assets, "js", "web-reader.js"))

    # 3. Copy generated PDF for direct 1-click download in UI and root TantraGyan
    if pdf_path and os.path.exists(pdf_path):
        web_pdf = os.path.join(DIST_WEB_DIR, "astrology-book.pdf")
        shutil.copy(pdf_path, web_pdf)
        root_tantragyan_pdf = os.path.join(os.path.dirname(ENGINE_ROOT), "astrology-book.pdf")
        shutil.copy(pdf_path, root_tantragyan_pdf)
        print(f"  • Copied PDF to web distribution & root TantraGyan for instant download")

    elapsed = time.time() - start_time
    print(f"✓ Target 2 Complete: {index_html_path}")
    print(f"  • Pre-compiled rich-text reader ready with instant zero-lag rendering")
    print(f"  • Compile Duration: {elapsed:.2f}s")
    return index_html_path


def main():
    parser = argparse.ArgumentParser(description="Astrology Book Dual-Target Publishing Pipeline")
    parser.add_argument("--target", choices=["all", "pdf", "web", "typst"], default="all", help="Target output to build")
    parser.add_argument("--clean", action="store_true", help="Clean dist before building")
    parser.add_argument("--serve", type=int, default=0, help="Start localhost HTTP server on given port after build")
    args = parser.parse_args()

    if args.clean and os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
        print("✓ Cleaned dist directory")

    metadata = load_metadata()
    print(f"Loaded Book: {metadata.get('title')} ({metadata.get('english_title')})")
    print(f"Author: {metadata.get('author')} • Edition: {metadata.get('edition')}")

    build_charts()
    chapters = parse_all_chapters(metadata)

    pdf_path = None
    if args.target in ["all", "pdf"]:
        pdf_path = build_pdf_target(metadata, chapters)

    if args.target in ["all", "typst"]:
        build_typst_target(metadata, chapters)

    if args.target in ["all", "web"]:
        if not pdf_path:
            candidate = os.path.join(DIST_PDF_DIR, "astrology-book.pdf")
            if os.path.exists(candidate):
                pdf_path = candidate
        build_web_target(metadata, chapters, pdf_path)

    print("\n=======================================================")
    print("✨ DUAL PUBLISHING PIPELINE COMPLETED SUCCESSFULLY! ✨")
    print(f"1. PDF Target (WeasyPrint): {DIST_PDF_DIR}/astrology-book.pdf")
    if os.path.exists(os.path.join(DIST_PDF_DIR, "astrology-book-typst.pdf")):
        print(f"2. PDF Target (Typst):       {DIST_PDF_DIR}/astrology-book-typst.pdf")
    print(f"3. Web Reader (Rich-Text):   {DIST_WEB_DIR}/index.html")
    print("=======================================================\n")

    if args.serve > 0:
        import http.server
        import socketserver

        port = args.serve
        os.chdir(os.path.dirname(ENGINE_ROOT))
        handler = http.server.SimpleHTTPRequestHandler
        print(f"🚀 Starting Tantra Gyan Localhost Server on port {port}...")
        print(f"• Classic 3D Book:        http://localhost:{port}/index.html")
        print(f"• Modern Rich-Text Book:  http://localhost:{port}/astrology-book-engine/dist/web/index.html")
        print(f"• Direct PDF Download:     http://localhost:{port}/astrology-book-engine/dist/pdf/astrology-book.pdf")
        with socketserver.TCPServer(("", port), handler) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nServer stopped.")


if __name__ == "__main__":
    main()
