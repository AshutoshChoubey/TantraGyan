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
from reportlab_compiler import compile_reportlab_book

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


def patch_weasyprint_svg_text():
    """
    Patches WeasyPrint's SVG text renderer to prevent splitting Devanagari combining
    characters into isolated single codepoints (which strips matras like ि and conjuncts)
    and ensures full Pango/HarfBuzz shaping.
    """
    try:
        import sys
        import weasyprint.svg as wsvg
        import weasyprint.svg.text
        wst_mod = sys.modules['weasyprint.svg.text']
        from weasyprint.svg.utils import normalize, size, radians
        from weasyprint.matrix import Matrix
        from weasyprint.svg.bounding_box import extend_bounding_box
        from math import cos, sin, inf

        def fixed_text(svg, node, font_size):
            from weasyprint.css.properties import INITIAL_VALUES
            from weasyprint.draw.text import draw_emojis, draw_first_line
            from weasyprint.text.line_break import split_first_line
            from weasyprint.svg.text import TextBox

            style = INITIAL_VALUES.copy()
            style['font_family'] = [
                font.strip('\"\'') for font in
                node.get('font-family', 'Noto Sans Devanagari, Devanagari MT, sans-serif').split(',')]
            style['font_style'] = node.get('font-style', 'normal')
            style['font_weight'] = node.get('font-weight', 400)
            style['font_size'] = font_size
            if style['font_weight'] == 'normal':
                style['font_weight'] = 400
            elif style['font_weight'] == 'bold':
                style['font_weight'] = 700
            else:
                try:
                    style['font_weight'] = int(style['font_weight'])
                except ValueError:
                    style['font_weight'] = 400

            layout, _, _, width, height, _ = split_first_line(
                node.text or '', style, svg.context, inf, 0)

            x, y, dx, dy, rotate = [], [], [], [], [0]
            if 'x' in node.attrib:
                x = [size(i, font_size, svg.inner_width)
                     for i in normalize(node.attrib['x']).strip().split(' ')]
            if 'y' in node.attrib:
                y = [size(i, font_size, svg.inner_height)
                     for i in normalize(node.attrib['y']).strip().split(' ')]
            if 'dx' in node.attrib:
                dx = [size(i, font_size, svg.inner_width)
                      for i in normalize(node.attrib['dx']).strip().split(' ')]
            if 'dy' in node.attrib:
                dy = [size(i, font_size, svg.inner_height)
                      for i in normalize(node.attrib['dy']).strip().split(' ')]
            if 'rotate' in node.attrib:
                rotate = [radians(float(i)) if i else 0
                          for i in normalize(node.attrib['rotate']).strip().split(' ')]
            last_r = rotate[-1]

            is_multi = len(x) > 1 or len(y) > 1 or len(dx) > 1 or len(dy) > 1 or len(rotate) > 1
            if not is_multi and node.text:
                letters_positions = [
                    ([x.pop(0) if x else None, y.pop(0) if y else None, dx.pop(0) if dx else None, dy.pop(0) if dy else None, rotate.pop(0) if rotate else None], node.text)
                ]
            else:
                letters_positions = [
                    ([pl.pop(0) if pl else None for pl in (x, y, dx, dy, rotate)], char)
                    for char in (node.text or '')]

            letter_spacing = svg.length(node.get('letter-spacing'), font_size)
            text_length = svg.length(node.get('textLength'), font_size)
            scale_x = 1
            if text_length and node.text:
                spaces_count = len(node.text) - 1
                if normalize(node.attrib.get('lengthAdjust')) == 'spacingAndGlyphs':
                    width_with_spacing = width + spaces_count * letter_spacing
                    letter_spacing *= text_length / width_with_spacing
                    spaceless_text_length = text_length - spaces_count * letter_spacing
                    scale_x = spaceless_text_length / width
                elif spaces_count:
                    letter_spacing = (text_length - width) / spaces_count
                width = text_length

            ascent, descent = font_size * .8, font_size * .2
            y_align = 0
            display_anchor = node.get('display-anchor')
            alignment_baseline = node.get(
                'dominant-baseline', node.get('alignment-baseline'))
            if display_anchor == 'middle':
                y_align = -height / 2
            elif display_anchor == 'top':
                pass
            elif display_anchor == 'bottom':
                y_align = -height
            elif alignment_baseline in ('central', 'middle'):
                y_align = (ascent + descent) / 2 - descent
            elif alignment_baseline in (
                    'text-before-edge', 'before_edge', 'top', 'hanging', 'text-top'):
                y_align = ascent
            elif alignment_baseline in (
                    'text-after-edge', 'after_edge', 'bottom', 'text-bottom'):
                y_align = -descent

            text_anchor = node.get('text-anchor', 'start')
            x_align = -width / 2 if text_anchor == 'middle' else (-width if text_anchor == 'end' else 0)

            if not node.text:
                x = x[0] if x else svg.cursor_position[0]
                y = y[0] if y else svg.cursor_position[1]
                dx = dx[0] if dx else 0
                dy = dy[0] if dy else 0
                svg.cursor_position = (x + dx, y + dy)
                return

            svg.stream.push_state()
            svg.stream.begin_text()
            emoji_lines = []

            for i, ((x, y, dx, dy, r), letter) in enumerate(letters_positions):
                if x:
                    svg.cursor_d_position[0] = 0
                if y:
                    svg.cursor_d_position[1] = 0
                svg.cursor_d_position[0] += dx or 0
                svg.cursor_d_position[1] += dy or 0
                layout, _, _, width, height, _ = split_first_line(
                    letter, style, svg.context, inf, 0)
                x = svg.cursor_position[0] if x is None else x
                y = svg.cursor_position[1] if y is None else y
                width *= scale_x
                if i:
                    x += letter_spacing
                svg.cursor_position = x + width, y

                x_position = x + svg.cursor_d_position[0] + x_align
                y_position = y + svg.cursor_d_position[1] + y_align
                angle = last_r if r is None else r
                points = (
                    (x_position, y_position),
                    (x_position + width, y_position - height))
                node.text_bounding_box = extend_bounding_box(
                    node.text_bounding_box, points)

                layout.reactivate(style)
                svg.fill_stroke(node, font_size, text=True)
                matrix = Matrix(a=scale_x, d=-1, e=x_position, f=y_position)
                if angle:
                    a, c = cos(angle), sin(angle)
                    matrix = Matrix(a, -c, c, a) @ matrix
                emojis = draw_first_line(
                    svg.stream, TextBox(layout, style), 'none', 'none', matrix)
                emoji_lines.append((font_size, x, y, emojis))

            svg.stream.end_text()
            svg.stream.pop_state()

            for font_size, x, y, emojis in emoji_lines:
                draw_emojis(svg.stream, font_size, x, y, emojis)

        wst_mod.text = fixed_text
        wsvg.TAGS['text'] = fixed_text
    except Exception as e:
        print(f"⚠️ Notice: Could not patch WeasyPrint SVG text: {e}")


def build_pdf_target(metadata, chapters):
    """Target 1: Compiles Trade Paperback Vector PDF via WeasyPrint"""
    print("\n--- Compiling Target 1: Vector PDF (WeasyPrint) ---")
    start_time = time.time()

    patch_weasyprint_svg_text()

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

    # Mirror to root TantraGyan
    root_pdf = os.path.join(os.path.dirname(ENGINE_ROOT), "astrology-book.pdf")
    shutil.copy(output_pdf, root_pdf)

    elapsed = time.time() - start_time
    size_mb = os.path.getsize(output_pdf) / (1024 * 1024)
    print(f"✓ Target 1 (WeasyPrint) Complete: {output_pdf}")
    print(f"  • Size: {size_mb:.2f} MB | Compile Duration: {elapsed:.2f}s")
    return output_pdf


def build_reportlab_target(metadata, chapters):
    """Target 1C: Compiles ReportLab PDF with devanagari-reportlab HarfBuzz shaping"""
    print("\n--- Compiling Target 1C: Devanagari ReportLab PDF ---")
    start_time = time.time()
    os.makedirs(DIST_PDF_DIR, exist_ok=True)
    output_rl_pdf = os.path.join(DIST_PDF_DIR, "astrology-book-reportlab.pdf")

    compile_reportlab_book(metadata, chapters, output_rl_pdf, ENGINE_ROOT)

    root_rl = os.path.join(os.path.dirname(ENGINE_ROOT), "astrology-book-reportlab.pdf")
    shutil.copy(output_rl_pdf, root_rl)

    elapsed = time.time() - start_time
    size_mb = os.path.getsize(output_rl_pdf) / (1024 * 1024)
    print(f"✓ Target 1C (ReportLab Devanagari) Complete: {output_rl_pdf}")
    print(f"  • Size: {size_mb:.2f} MB | Compile Duration: {elapsed:.2f}s")
    return output_rl_pdf


def build_typst_target(metadata, chapters):
    """Target 1B: Compiles Ultra-High Resolution PDF via Typst"""
    print("\n--- Compiling Target 1B: Vector PDF (Typst Engine) ---")
    start_time = time.time()
    os.makedirs(DIST_PDF_DIR, exist_ok=True)
    output_typst_pdf = os.path.join(DIST_PDF_DIR, "astrology-book-typst.pdf")

    compile_typst_book(metadata, chapters, output_typst_pdf, ENGINE_ROOT)

    root_typst = os.path.join(os.path.dirname(ENGINE_ROOT), "astrology-book-typst.pdf")
    shutil.copy(output_typst_pdf, root_typst)
    web_typst = os.path.join(DIST_WEB_DIR, "astrology-book-typst.pdf")
    os.makedirs(DIST_WEB_DIR, exist_ok=True)
    shutil.copy(output_typst_pdf, web_typst)

    elapsed = time.time() - start_time
    size_mb = os.path.getsize(output_typst_pdf) / (1024 * 1024)
    print(f"✓ Target 1B (Typst) Complete: {output_typst_pdf}")
    print(f"  • Size: {size_mb:.2f} MB | Compile Duration: {elapsed:.2f}s")
    return output_typst_pdf


def build_vivliostyle_target(metadata, chapters):
    """Target 1D: Compiles Publication Masterwork Vector PDF via Vivliostyle + Chromium"""
    print("\n--- Compiling Target 1D: Vector PDF (Vivliostyle + Chromium) ---")
    start_time = time.time()
    os.makedirs(DIST_PDF_DIR, exist_ok=True)

    pdf_html_path = os.path.join(DIST_PDF_DIR, "index_pdf.html")
    if not os.path.exists(pdf_html_path):
        env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
        template = env.get_template("layout.html")
        html_out = template.render(meta=metadata, chapters=chapters, target="pdf")
        with open(pdf_html_path, "w", encoding="utf-8") as f:
            f.write(html_out)
        shutil.copy(os.path.join(TEMPLATES_DIR, "print.css"), os.path.join(DIST_PDF_DIR, "print.css"))
        dist_pdf_assets = os.path.join(DIST_PDF_DIR, "assets")
        if os.path.exists(dist_pdf_assets):
            shutil.rmtree(dist_pdf_assets)
        shutil.copytree(ASSETS_DIR, dist_pdf_assets)

    output_vivlio_pdf = os.path.join(DIST_PDF_DIR, "astrology-book-vivliostyle.pdf")

    cmd = [
        "vivliostyle",
        "build",
        pdf_html_path,
        "-o",
        output_vivlio_pdf
    ]
    print(f"Executing Vivliostyle build: {' '.join(cmd)}")
    import subprocess
    subprocess.run(cmd, check=True)

    root_vivlio = os.path.join(os.path.dirname(ENGINE_ROOT), "astrology-book-vivliostyle.pdf")
    shutil.copy(output_vivlio_pdf, root_vivlio)
    web_vivlio = os.path.join(DIST_WEB_DIR, "astrology-book-vivliostyle.pdf")
    os.makedirs(DIST_WEB_DIR, exist_ok=True)
    shutil.copy(output_vivlio_pdf, web_vivlio)

    # Primary Clean Branded Masterwork PDF (Tantra Gyan: Vedic Jyotish Maha Granth)
    primary_pdf_name = "tantra-gyan-vedic-jyotish-mahagranth.pdf"
    dist_primary = os.path.join(DIST_PDF_DIR, primary_pdf_name)
    shutil.copy(output_vivlio_pdf, dist_primary)
    root_primary = os.path.join(os.path.dirname(ENGINE_ROOT), primary_pdf_name)
    shutil.copy(output_vivlio_pdf, root_primary)
    web_primary = os.path.join(DIST_WEB_DIR, primary_pdf_name)
    shutil.copy(output_vivlio_pdf, web_primary)

    elapsed = time.time() - start_time
    size_mb = os.path.getsize(output_vivlio_pdf) / (1024 * 1024)
    print(f"✓ Target 1D (Vivliostyle) Complete: {output_vivlio_pdf}")
    print(f"  • Size: {size_mb:.2f} MB | Compile Duration: {elapsed:.2f}s")
    return output_vivlio_pdf


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

    # 3. Copy generated PDFs for direct 1-click download in UI and root TantraGyan
    for pdf_name in ["tantra-gyan-vedic-jyotish-mahagranth.pdf", "astrology-book-vivliostyle.pdf", "astrology-book-typst.pdf", "astrology-book.pdf"]:
        src_p = os.path.join(DIST_PDF_DIR, pdf_name)
        if os.path.exists(src_p):
            web_pdf = os.path.join(DIST_WEB_DIR, pdf_name)
            shutil.copy(src_p, web_pdf)
            root_tantragyan_pdf = os.path.join(os.path.dirname(ENGINE_ROOT), pdf_name)
            shutil.copy(src_p, root_tantragyan_pdf)
            print(f"  • Copied {pdf_name} to web distribution & root TantraGyan for instant download")

    elapsed = time.time() - start_time
    print(f"✓ Target 2 Complete: {index_html_path}")
    print(f"  • Pre-compiled rich-text reader ready with instant zero-lag rendering")
    print(f"  • Compile Duration: {elapsed:.2f}s")
    return index_html_path


def main():
    parser = argparse.ArgumentParser(description="Astrology Book Multi-Target Publishing Pipeline")
    parser.add_argument("--target", choices=["all", "pdf", "web", "typst", "vivliostyle", "reportlab"], default="all", help="Target output to build")
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

    if args.target in ["all", "vivliostyle"]:
        build_vivliostyle_target(metadata, chapters)

    if args.target == "reportlab":
        build_reportlab_target(metadata, chapters)

    if args.target in ["all", "web"]:
        if not pdf_path:
            candidate = os.path.join(DIST_PDF_DIR, "astrology-book.pdf")
            if os.path.exists(candidate):
                pdf_path = candidate
        build_web_target(metadata, chapters, pdf_path)

    print("\n=======================================================")
    print("✨ ASTROLOGY BOOK PUBLISHING PIPELINE COMPLETED! ✨")
    print(f"1. PDF Target (Vivliostyle Chromium): {DIST_PDF_DIR}/astrology-book-vivliostyle.pdf")
    if os.path.exists(os.path.join(DIST_PDF_DIR, "astrology-book-typst.pdf")):
        print(f"2. PDF Target (Typst Academic):        {DIST_PDF_DIR}/astrology-book-typst.pdf")
    if os.path.exists(os.path.join(DIST_PDF_DIR, "astrology-book.pdf")):
        print(f"3. PDF Target (WeasyPrint Trade):      {DIST_PDF_DIR}/astrology-book.pdf")
    print(f"4. Web Reader (Rich-Text):             {DIST_WEB_DIR}/index.html")
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
