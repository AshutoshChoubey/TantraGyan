#!/usr/bin/env python3
"""
Astrology Markdown Parser & AST Transformer
============================================
Extends Python-Markdown with custom astrological extensions:
- ::: yoga [Title] ... :::
- ::: shloka [Source] ... :::
- ::: formula [Sutra Name] ... :::
- ::: chart [lagna=X, planets=..., title=...] ::: or ::: chart [sample_key] :::
- ::: warning [Title] ... :::
- Auto-styled high-density book tables
- Chapter section anchors & running header markers
"""

import re
import html
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor

from chart_generator import (
    generate_north_indian_chart,
    generate_aspect_wheel,
    generate_sample_kundlis
)

SAMPLE_CHARTS = generate_sample_kundlis()

class AstrologyCalloutPreprocessor(Preprocessor):
    """
    Transforms custom triple-colon block directives into structured HTML containers.
    """
    BLOCK_REGEX = re.compile(
        r'^:::\s*(\w+)(?:\s*\[(.*?)\])?\s*\n(.*?)\n^:::\s*$',
        re.MULTILINE | re.DOTALL
    )

    def run(self, lines):
        text = "\n".join(lines)

        def replace_block(match):
            block_type = match.group(1).lower().strip()
            title = match.group(2) or ""
            content = match.group(3).strip()

            if block_type == "shloka":
                source_label = title.strip() or "शास्त्रीय प्रमाण (Classical Shastra)"
                # Format verses nicely
                verse_lines = [f"<p class='shloka-line'>{html.escape(l.strip())}</p>" for l in content.split("\n") if l.strip()]
                return f"""<div class="callout callout-shloka">
  <div class="shloka-header">
    <span class="shloka-emblem">ॐ</span>
    <span class="shloka-source">{html.escape(source_label)}</span>
  </div>
  <div class="shloka-verse">
    {"".join(verse_lines)}
  </div>
</div>"""

            elif block_type == "yoga":
                yoga_title = title.strip() or "शास्त्रीय राजयोग (Classical Raja Yoga)"
                return f"""<div class="callout callout-yoga">
  <div class="callout-header">
    <span class="callout-badge">RAJA YOGA</span>
    <span class="callout-title">{html.escape(yoga_title)}</span>
  </div>
  <div class="callout-body">
{content}
  </div>
</div>"""

            elif block_type == "formula":
                formula_title = title.strip() or "फलित सूत्र (Predictive Sutra)"
                return f"""<div class="callout callout-formula">
  <div class="callout-header">
    <span class="callout-badge">SUTRA / सूत्र</span>
    <span class="callout-title">{html.escape(formula_title)}</span>
  </div>
  <div class="callout-body">
{content}
  </div>
</div>"""

            elif block_type == "warning":
                warning_title = title.strip() or "ज्योतिषीय चेतावनी एवं सावधानियां"
                return f"""<div class="callout callout-warning">
  <div class="callout-header">
    <span class="callout-badge">CAVEAT / सावधान</span>
    <span class="callout-title">{html.escape(warning_title)}</span>
  </div>
  <div class="callout-body">
{content}
  </div>
</div>"""

            elif block_type == "chart":
                chart_key = title.strip().lower()
                caption = content.strip() or "वैदिक कुण्डली चक्र (Vedic Chart Diagram)"

                if chart_key in SAMPLE_CHARTS:
                    svg_markup = SAMPLE_CHARTS[chart_key]
                elif chart_key == "aspect_wheel":
                    svg_markup = generate_aspect_wheel()
                else:
                    # Parse parameters like lagna=1, title=...
                    lagna = 1
                    chart_title = "जन्म कुण्डली"
                    planets = {}
                    if "lagna=" in chart_key:
                        m = re.search(r'lagna=(\d+)', chart_key)
                        if m:
                            lagna = int(m.group(1))
                    svg_markup = generate_north_indian_chart(lagna_rashi=lagna, title=chart_title)

                return f"""<figure class="chart-figure" id="chart-{chart_key}">
  <div class="chart-svg-wrapper">
    {svg_markup}
  </div>
  <figcaption class="chart-caption">{caption}</figcaption>
</figure>"""

            else:
                # Generic callout
                return f"""<div class="callout callout-note">
  <div class="callout-header">
    <span class="callout-badge">NOTE / टिप्पणी</span>
    <span class="callout-title">{html.escape(title)}</span>
  </div>
  <div class="callout-body">
{content}
  </div>
</div>"""

        text = self.BLOCK_REGEX.sub(replace_block, text)
        return text.split("\n")


class AstrologyTablePostprocessor(Postprocessor):
    """
    Wraps standard markdown tables into professional print-ready responsive book tables.
    Automatically assigns .table-dense for tables with 6+ columns to guarantee zero horizontal scrollbars.
    """
    def run(self, text):
        def wrap_table(m):
            tbl = m.group(0)
            first_row = re.search(r'<tr>(.*?)</tr>', tbl, re.DOTALL)
            col_count = len(re.findall(r'<t[hd]', first_row.group(1))) if first_row else 0
            cls = 'astro-book-table'
            if col_count >= 6:
                cls += ' table-dense'
            inner = tbl[len('<table>'):-len('</table>')]
            return f'<div class="table-container"><table class="{cls}">{inner}</table></div>'

        return re.sub(r'<table>[\s\S]*?</table>', wrap_table, text)


# Authentic Vedic Jyotish Planet Color Palette Rules
PLANET_RULES = [
    ('sun', r'(?<![क-हअ-औ्])(?:सूर्य\s*\(\s*Sun\s*\)|सूर्यदेव|सूर्य|\bSun\b)(?![क-हअ-औ्ा-ौ])'),
    ('moon', r'(?<![क-हअ-औ्])(?:चन्द्र\s*\(\s*Moon\s*\)|चंद्र\s*\(\s*Moon\s*\)|चन्द्रमा|चंद्रमा|चन्द्र|चंद्र|\bMoon\b)(?![क-हअ-औ्ा-ौ])'),
    ('mars', r'(?<![क-हअ-औ्])(?:मंगल\s*\(\s*Mars\s*\)|मंगलदेव|मंगल|\bMars\b)(?![क-हअ-औ्ा-ौ])'),
    ('mercury', r'(?<![क-हअ-औ्])(?:बुध\s*\(\s*Mercury\s*\)|बुधदेव|बुध|\bMercury\b)(?![क-हअ-औ्ा-ौ])'),
    ('jupiter', r'(?<![क-हअ-औ्])(?:(?:गुरु\s*/\s*बृहस्पति|बृहस्पति|देवगुरु|गुरु(?!\s*जन))\s*\(\s*Jupiter\s*\)|बृहस्पति|देवगुरु|गुरु(?!\s*जन)|\bJupiter\b)(?![क-हअ-औ्ा-ौ])'),
    ('venus', r'(?<![क-हअ-औ्])(?:शुक्र\s*\(\s*Venus\s*\)|शुक्रदेव|शुक्र|\bVenus\b)(?![क-हअ-औ्ा-ौ])'),
    ('saturn', r'(?<![क-हअ-औ्])(?:शनि\s*\(\s*Saturn\s*\)|शनिदेव|शनैश्चर|शनि|\bSaturn\b)(?![क-हअ-औ्ा-ौ])'),
    ('rahu', r'(?<![क-हअ-औ्])(?:राहु\s*\(\s*Rahu\s*\)|राहु|\bRahu\b)(?![क-हअ-औ्ा-ौ])'),
    ('ketu', r'(?<![क-हअ-औ्])(?:केतु\s*\(\s*Ketu\s*\)|केतु|\bKetu\b)(?![क-हअ-औ्ा-ौ])'),
]


class PlanetColoringPostprocessor(Postprocessor):
    """
    Intelligently colors planet names across all text and tables according to authentic Jyotish symbolism:
    - Sun: Saffron
    - Moon: Pearl / Silver Moon
    - Mars: Fiery Red
    - Mercury: Emerald Green
    - Jupiter: Golden Turmeric Yellow
    - Venus: Brilliant Diamond Rose Pink
    - Saturn: Deep Cosmic Royal Blue
    - Rahu: Shadow Obsidian Black
    - Ketu: Smokey Ash Shadow Gray
    """
    def run(self, text):
        protected = []
        def save_block(m):
            protected.append(m.group(0))
            return f'___PROTECTED_PLANET_{len(protected)-1}___'

        # Protect SVG diagrams, Sanskrit Shlokas, code blocks, and attributes
        s = re.sub(r'<svg[\s\S]*?</svg>', save_block, text)
        s = re.sub(r'<div class="callout callout-shloka"[\s\S]*?</div>\s*</div>', save_block, s)
        s = re.sub(r'<pre[\s\S]*?</pre>', save_block, s)
        s = re.sub(r'<code[\s\S]*?</code>', save_block, s)

        parts = re.split(r'(<[^>]+>)', s)
        out = []
        for p in parts:
            if p.startswith('<'):
                out.append(p)
            else:
                txt = p
                for p_key, pat in PLANET_RULES:
                    txt = re.sub(pat, lambda m: f'<span class="planet-badge planet-{p_key}">{m.group(0)}</span>', txt)
                out.append(txt)

        res = ''.join(out)
        for idx, orig in enumerate(protected):
            res = res.replace(f'___PROTECTED_PLANET_{idx}___', orig)
        return res


class AstrologyExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(AstrologyCalloutPreprocessor(md), 'astrology_callouts', 30)
        md.postprocessors.register(AstrologyTablePostprocessor(md), 'astrology_tables', 30)
        md.postprocessors.register(PlanetColoringPostprocessor(md), 'planet_coloring', 25)


def parse_manuscript(md_content):
    """
    Parses an astrological markdown manuscript into clean semantic HTML.
    Extracts frontmatter, chapter metadata, and returns (metadata, html_content).
    """
    meta = {}
    content = md_content

    # Extract YAML frontmatter if present
    if md_content.startswith("---"):
        parts = md_content.split("---", 2)
        if len(parts) >= 3:
            raw_meta = parts[1]
            content = parts[2].strip()
            import yaml
            try:
                meta = yaml.safe_load(raw_meta) or {}
            except Exception:
                meta = {}

    md = markdown.Markdown(
        extensions=[
            'extra',
            'tables',
            'toc',
            'codehilite',
            AstrologyExtension()
        ]
    )

    html_out = md.convert(content)

    return meta, html_out


if __name__ == "__main__":
    sample_text = """
# अध्याय १: ज्योतिषीय आधार एवं भाव कारकत्व

प्रारंभिक फलित ज्योतिष का मुख्य आधार १२ राशियां, ९ ग्रह और १२ भाव हैं।

::: shloka [बृहत्पाराशर होरा शास्त्र - अध्याय १, श्लोक ३]
यथा शिखा मयूराणां नागानां मणयो यथा।
तद्वद्वेदांगशास्त्राणां ज्योतिषं मूर्धनि स्थितम्॥
:::

::: yoga [गजकेसरी राजयोग]
जब जन्म कुण्डली में बृहस्पति चन्द्रमा से केन्द्र भाव (१, ४, ७, १०) में स्थित हो, तब गजकेसरी योग का निर्माण होता है। जातक प्रखर बुद्धि, राजमान्य एवं दीर्घायु होता है।
:::

::: chart [lagna_chart]
चित्र १.१: कालपुरुष कुण्डली एवं केन्द्र-त्रिकोण भाव विन्यास
:::

| भाव | शास्त्रीय नाम | मुख्य कारकत्व | प्राकृतिक स्वामी |
| :--- | :--- | :--- | :--- |
| प्रथम | तनु भाव | देह, स्वास्थ्य, आत्मबल, रूप | मेष (मंगल) |
| द्वितीय | धन भाव | पैतृक संपत्ति, वाणी, संचित कोष | वृषभ (शुक्र) |
| चतुर्थ | सुख भाव | माता, गृह, वाहन, मानसिक शांति | कर्क (चन्द्रमा) |
| नवम | भाग्य भाव | धर्म, गुरु, पिता, उच्च ज्ञान | धनु (बृहस्पति) |
| दशम | कर्म भाव | राज्य पद, आजीविका, कीर्ति | मकर (शनि) |
"""
    meta, rendered = parse_manuscript(sample_text)
    print("Rendered HTML preview (first 500 chars):")
    print(rendered[:500])
