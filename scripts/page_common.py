#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Common page components and SVG visual generators for the 108-page Vedic Kundali Ganita Vichar Mahagranth.
Tantra Gyan Research Center • https://t.worldgyan.com
"""

def make_page(page_num: int, chapter: str, title: str, content: str) -> str:
    """Wraps page content in standard reader.html article format."""
    return f'''    <article class="book-page-data" id="page-data-{page_num}" data-page="{page_num}" data-chapter="{chapter}" data-title="{title}">
      <div class="page-inner" style="padding: 1.8rem 1.6rem; font-family: 'Noto Sans Devanagari', -apple-system, sans-serif; line-height: 1.65; color: #1e293b;">
        <div class="page-header" style="display:flex; justify-content:space-between; align-items:center; border-bottom:1.5px solid #d4af37; padding-bottom:0.5rem; margin-bottom:1.1rem;">
          <span style="font-size:0.75rem; font-weight:800; color:#059669; letter-spacing:0.04em; text-transform:uppercase;">{chapter}</span>
          <span style="font-size:0.75rem; font-weight:700; color:#b45309; background:rgba(212,175,55,0.15); padding:0.15rem 0.55rem; border-radius:4px;">पृष्ठ {page_num} / १०८</span>
        </div>
        <h2 style="font-size:1.18rem; font-weight:800; color:#0f172a; margin-top:0; margin-bottom:0.9rem; border-left:4px solid #10b981; padding-left:0.6rem; line-height:1.35;">{title}</h2>
        <div class="page-body-flow" style="font-size:0.875rem; color:#334155;">
{content}
        </div>
        <div class="page-footer" style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:0.5rem; margin-top:1.2rem; font-size:0.7rem; color:#64748b;">
          <span>वैदिक कुण्डली विचार एवं गणित महाग्रंथ • तंत्र ज्ञान शोध संस्थान</span>
          <span>t.worldgyan.com</span>
        </div>
      </div>
    </article>
'''

def get_diamond_chart_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="240" style="max-width:320px; margin:0.6rem auto; display:block; background:#090d16; border-radius:8px;">
  <defs>
    <linearGradient id="gGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c89d3d" />
      <stop offset="100%" stop-color="#10b981" />
    </linearGradient>
  </defs>
  <rect width="600" height="600" fill="#090d16" rx="8" />
  <rect x="50" y="50" width="500" height="500" fill="none" stroke="#2a334a" stroke-width="2" />
  <line x1="50" y1="50" x2="550" y2="550" stroke="#2a334a" stroke-width="2" />
  <line x1="550" y1="50" x2="50" y2="550" stroke="#2a334a" stroke-width="2" />
  <polygon points="300,50 550,300 300,550 50,300" fill="none" stroke="url(#gGold)" stroke-width="3" />
  <text x="300" y="160" fill="#38bdf8" font-size="22" font-weight="bold" text-anchor="middle">१ (लग्न)</text>
  <text x="180" y="100" fill="#cbd5e1" font-size="18" text-anchor="middle">२</text>
  <text x="100" y="180" fill="#cbd5e1" font-size="18" text-anchor="middle">३</text>
  <text x="160" y="300" fill="#cbd5e1" font-size="22" font-weight="bold" text-anchor="middle">४ (सुख)</text>
  <text x="100" y="420" fill="#cbd5e1" font-size="18" text-anchor="middle">५</text>
  <text x="180" y="500" fill="#cbd5e1" font-size="18" text-anchor="middle">६</text>
  <text x="300" y="440" fill="#cbd5e1" font-size="22" font-weight="bold" text-anchor="middle">७ (जाया)</text>
  <text x="420" y="500" fill="#cbd5e1" font-size="18" text-anchor="middle">८</text>
  <text x="500" y="420" fill="#cbd5e1" font-size="18" text-anchor="middle">९</text>
  <text x="440" y="300" fill="#cbd5e1" font-size="22" font-weight="bold" text-anchor="middle">१० (कर्म)</text>
  <text x="500" y="180" fill="#cbd5e1" font-size="18" text-anchor="middle">११</text>
  <text x="420" y="100" fill="#cbd5e1" font-size="18" text-anchor="middle">१२</text>
</svg>'''

def get_circular_zodiac_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="240" style="max-width:320px; margin:0.6rem auto; display:block; background:#0b101b; border-radius:8px;">
  <circle cx="250" cy="250" r="230" fill="none" stroke="#1e293b" stroke-width="2" />
  <circle cx="250" cy="250" r="190" fill="none" stroke="#d4af37" stroke-width="2" stroke-dasharray="4,4" />
  <circle cx="250" cy="250" r="130" fill="#0f172a" stroke="#10b981" stroke-width="2" />
  <text x="250" y="245" fill="#f8fafc" font-size="16" font-weight="bold" text-anchor="middle">कालचक्र</text>
  <text x="250" y="270" fill="#38bdf8" font-size="12" text-anchor="middle">३६०° भचक्र</text>
  <text x="250" y="45" fill="#e2e8f0" font-size="13" font-weight="bold" text-anchor="middle">मेष ०°</text>
  <text x="455" y="255" fill="#e2e8f0" font-size="13" font-weight="bold" text-anchor="middle">कर्क ९०°</text>
  <text x="250" y="465" fill="#e2e8f0" font-size="13" font-weight="bold" text-anchor="middle">तुला १८०°</text>
  <text x="45" y="255" fill="#e2e8f0" font-size="13" font-weight="bold" text-anchor="middle">मकर २७०°</text>
</svg>'''
