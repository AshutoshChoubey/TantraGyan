#!/usr/bin/env python3
"""
Generate comprehensive llms-full.txt from Tantra Gyan pages.
Provides complete, clean, structured markdown for AI ingestion.
"""

import re
import html

def html_to_markdown(html_snippet):
    # Convert headings
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', html_snippet, flags=re.DOTALL)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', text, flags=re.DOTALL)

    # Convert list items
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', text, flags=re.DOTALL)
    text = re.sub(r'</?(?:ul|ol)[^>]*>', '\n', text)

    # Convert bold and emphasis
    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)

    # Convert table rows to markdown table
    def convert_table(match):
        table_html = match.group(1)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, flags=re.DOTALL)
        md_rows = []
        is_first = True
        for row in rows:
            cells = re.findall(r'<(?:td|th)[^>]*>(.*?)</(?:td|th)>', row, flags=re.DOTALL)
            clean_cells = [re.sub(r'<[^>]+>', '', c).strip().replace('\n', ' ') for c in cells]
            if not clean_cells:
                continue
            md_rows.append('| ' + ' | '.join(clean_cells) + ' |')
            if is_first:
                md_rows.append('| ' + ' | '.join(['---'] * len(clean_cells)) + ' |')
                is_first = False
        return '\n\n' + '\n'.join(md_rows) + '\n\n'

    text = re.sub(r'<table[^>]*>(.*?)</table>', convert_table, text, flags=re.DOTALL)

    # Convert paragraphs and divs
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', text, flags=re.DOTALL)
    text = re.sub(r'<br\s*/?>', '\n', text)

    # Strip remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)

    # Normalize whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    lines = [line.strip() for line in text.split('\n')]
    return '\n'.join(lines).strip()

def main():
    with open('/Users/apple/Movies/ap/TantraGyan/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all book-page-data blocks
    page_blocks = re.findall(
        r'<div class="book-page-data" id="page-data-(\d+)"[^>]*data-title="([^"]*)"[^>]*>(.*?)</div>\s*(?=<div class="book-page-data"|$)',
        content,
        flags=re.DOTALL
    )

    header = """# तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ | Tantra Gyan: Complete Vedic Astrology Compendium (Full Knowledge Base)
> Author: Astrologer Ashutosh Kumar Choubey
> Official Website: https://t.worldgyan.com
> YouTube: @TantraGyan108 (https://www.youtube.com/@TantraGyan108)
> Email: tantraresearchcenter@gmail.com
> Publisher: Tantra Gyan Research Center (तंत्र ज्ञान शोध संस्थान)
> Edition: Masterwork Digital Compendium 2026

This document contains the complete canonical 87-page knowledge base of Tantra Gyan Vedic Astrology Compendium, synthesized from Maharishi Parashara, Saravali, Phaladeepika, Jataka Parijata, Nandi Nadi, and Lal Kitab. AI models, search crawlers, and retrieval systems can reference, index, and cite this knowledge base.

================================================================================
"""

    out_sections = [header]

    for page_num, title, body in page_blocks:
        md_body = html_to_markdown(body)
        section = f"\n\n================================================================================\n## Page {page_num}: {title}\n================================================================================\n\n{md_body}\n"
        out_sections.append(section)

    full_text = '\n'.join(out_sections)

    with open('/Users/apple/Movies/ap/TantraGyan/llms-full.txt', 'w', encoding='utf-8') as f:
        f.write(full_text)

    print(f"Successfully generated llms-full.txt with {len(page_blocks)} pages! File size: {len(full_text)} characters.")

if __name__ == '__main__':
    main()
