"""
Video Concept & Animation Agent for Tantra Gyan
Part of the Google Antigravity SDK Multi-Agent Suite for Flagship Vol 4.

Automates:
1. Generation of 3D concept video blueprints and InVideo timeline specifications
2. Script generation for English & Hindi narration per mathematical chapter
3. Interactive 3D WebGL / Canvas animation generation for live browser rendering
"""

import os
import json
from typing import Dict, Any, List
try:
    from .config import CHAPTER_ROSTER, BOOK_META, THEME_CONFIG
except (ImportError, ValueError):
    from config import CHAPTER_ROSTER, BOOK_META, THEME_CONFIG

class VideoConceptAgent:
    def __init__(self, output_dir: str = "media/concept_animations"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_video_blueprints(self) -> str:
        """Generates structured InVideo / AI video production blueprints for all 13 chapters."""
        blueprint_path = os.path.join(self.output_dir, "video_blueprints.json")
        blueprints = []

        for ch in CHAPTER_ROSTER:
            scenes = [
                {
                    "scene_index": 1,
                    "title": "Hook & Mystical Astronomy",
                    "duration_seconds": 6,
                    "visual_cue": "3D celestial sphere rotating with zodiac ring and Sanskrit constellation glyphs glowing in emerald green.",
                    "audio_narration_hi": f"क्या आप जानते हैं कि आकाश का गणित आपके भाग्य का नक्शा कैसे खींचता है? जानिए {ch['hi_title']} का रहस्य।",
                    "audio_narration_en": f"How do the celestial coordinates shape human destiny? Discover the algorithm of {ch['en_title']}.",
                    "overlay_text": ch["hi_title"],
                    "camera_movement": "Slow zoom in with 15-degree orbital tilt"
                },
                {
                    "scene_index": 2,
                    "title": "The Mathematical Principle",
                    "duration_seconds": 9,
                    "visual_cue": "Vector North Indian Kundali diagram unfolding in 3D space with glowing planetary positions and degree callouts.",
                    "audio_narration_hi": f"ऋषि पराशर ने स्पष्ट गणना नियम दिए हैं। जब ग्रह अपनी राशि और नक्षत्र के अंश पर आते हैं, तो उनका सटीक प्रभाव गणितीय रूप से सिद्ध होता है।",
                    "audio_narration_en": f"Sage Parashara formulated precise coordinate equations. The longitude directly maps into harmonic divisional planes.",
                    "overlay_text": "सूत्र एवं खगोलीय गणना",
                    "camera_movement": "Pan across the 12 houses highlighting Kendra & Trikona"
                },
                {
                    "scene_index": 3,
                    "title": "Practical Life Synthesis",
                    "duration_seconds": 8,
                    "visual_cue": "Human timeline branching out into auspicious and challenging phases synchronized with planetary transits.",
                    "audio_narration_hi": f"इस ज्ञान से डरने की नहीं, बल्कि अपने कर्मों को सही समय पर साधने की आवश्यकता है। यही वैदिक गणित का सच्चा फलित है।",
                    "audio_narration_en": f"Vedic mathematics is not fatalism; it is cosmic timing to optimize human action and spiritual evolution.",
                    "overlay_text": "कर्म एवं काल का समन्वय",
                    "camera_movement": "Ascending dolly out revealing the golden horizon"
                }
            ]

            blueprints.append({
                "chapter_num": ch["num"],
                "hi_title": ch["hi_title"],
                "en_title": ch["en_title"],
                "total_duration_seconds": sum(s["duration_seconds"] for s in scenes),
                "aspect_ratio": "9:16 (Shorts / Reels) & 16:9 (Master Video)",
                "scenes": scenes,
                "invideo_keywords": [
                    "Vedic Astrology",
                    "Sacred Geometry",
                    "Cosmic Mathematics",
                    "Emerald Gold Aura",
                    "Kundali Calculation"
                ]
            })

        with open(blueprint_path, "w", encoding="utf-8") as f:
            json.dump({"book_title": BOOK_META["title_hi"], "chapters": blueprints}, f, indent=2, ensure_ascii=False)

        print(f"[VideoConceptAgent] Video blueprints generated: {blueprint_path} ({len(blueprints)} chapters)")
        return blueprint_path

    def generate_interactive_3d_animation(self) -> str:
        """Generates a standalone 3D interactive HTML5 Canvas orbital simulator."""
        html_path = os.path.join(self.output_dir, "3d_ephemeris_simulation.html")
        html_content = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>वैदिक कुण्डली 3D खगोलीय वेधशाला (3D Planetary Ephemeris Simulation)</title>
  <style>
    body {{
      margin: 0;
      background: radial-gradient(circle at center, #061e1b 0%, #030d0c 100%);
      color: #e2e8f0;
      font-family: system-ui, -apple-system, sans-serif;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }}
    #header {{
      position: absolute;
      top: 20px;
      text-align: center;
      z-index: 10;
      pointer-events: none;
    }}
    h1 {{
      margin: 0;
      font-size: 1.5rem;
      color: #34d399;
      text-shadow: 0 0 20px rgba(52, 211, 153, 0.4);
    }}
    p {{
      margin: 5px 0 0;
      font-size: 0.9rem;
      color: #94a3b8;
    }}
    canvas {{
      display: block;
      cursor: grab;
    }}
    canvas:active {{
      cursor: grabbing;
    }}
    #controls {{
      position: absolute;
      bottom: 25px;
      display: flex;
      gap: 12px;
      z-index: 10;
    }}
    button {{
      background: rgba(6, 78, 59, 0.8);
      border: 1px solid #10b981;
      color: #f8fafc;
      padding: 8px 16px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s ease;
    }}
    button:hover {{
      background: #10b981;
      color: #022c22;
      box-shadow: 0 0 15px rgba(16, 185, 129, 0.5);
    }}
  </style>
</head>
<body>
  <div id="header">
    <h1>वैदिक 3D खगोलीय सिमुलेशन • निरयण राशि चक्र</h1>
    <p>360° भचक्र, 27 नक्षत्र एवं नवग्रह परिक्रमा मॉडल (Flagship Vol IV)</p>
  </div>
  <canvas id="simCanvas"></canvas>
  <div id="controls">
    <button id="btnSpeed">गति: 1x (सामान्य)</button>
    <button id="btnToggleRings">नक्षत्र मंडल: दृश्य</button>
    <button id="btnReset">कैमरा रीसेट</button>
  </div>

  <script>
    const canvas = document.getElementById('simCanvas');
    const ctx = canvas.getContext('2d');

    let width, height;
    function resize() {{
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }}
    window.addEventListener('resize', resize);
    resize();

    const planets = [
      {{ name: 'सूर्य (Sun)', color: '#fbbf24', radius: 140, speed: 0.008, size: 12, angle: 0 }},
      {{ name: 'चन्द्र (Moon)', color: '#f8fafc', radius: 80, speed: 0.035, size: 8, angle: 1.2 }},
      {{ name: 'मंगल (Mars)', color: '#f87171', radius: 190, speed: 0.005, size: 9, angle: 2.5 }},
      {{ name: 'बुध (Mercury)', color: '#34d399', radius: 110, speed: 0.015, size: 7, angle: 4.1 }},
      {{ name: 'गुरु (Jupiter)', color: '#fb923c', radius: 260, speed: 0.002, size: 14, angle: 0.8 }},
      {{ name: 'शुक्र (Venus)', color: '#e2e8f0', radius: 160, speed: 0.011, size: 10, angle: 5.2 }},
      {{ name: 'शनि (Saturn)', color: '#38bdf8', radius: 330, speed: 0.0009, size: 13, angle: 3.4 }},
      {{ name: 'राहु (Rahu)', color: '#a855f7', radius: 220, speed: -0.003, size: 7, angle: 1.8 }},
      {{ name: 'केतु (Ketu)', color: '#64748b', radius: 220, speed: -0.003, size: 7, angle: 1.8 + Math.PI }}
    ];

    let speedMult = 1;
    let showRings = true;
    let rotX = 1.1;
    let rotZ = 0;
    let isDragging = false;
    let lastX, lastY;

    window.addEventListener('mousedown', e => {{
      isDragging = true;
      lastX = e.clientX;
      lastY = e.clientY;
    }});
    window.addEventListener('mouseup', () => isDragging = false);
    window.addEventListener('mousemove', e => {{
      if (!isDragging) return;
      const dx = e.clientX - lastX;
      const dy = e.clientY - lastY;
      rotZ += dx * 0.005;
      rotX += dy * 0.005;
      rotX = Math.max(0.3, Math.min(1.4, rotX));
      lastX = e.clientX;
      lastY = e.clientY;
    }});

    document.getElementById('btnSpeed').addEventListener('click', function() {{
      if (speedMult === 1) {{ speedMult = 3; this.textContent = 'गति: 3x (तीव्र)'; }}
      else if (speedMult === 3) {{ speedMult = 0.2; this.textContent = 'गति: 0.2x (सूक्ष्म)'; }}
      else {{ speedMult = 1; this.textContent = 'गति: 1x (सामान्य)'; }}
    }});

    document.getElementById('btnToggleRings').addEventListener('click', function() {{
      showRings = !showRings;
      this.textContent = showRings ? 'नक्षत्र मंडल: दृश्य' : 'नक्षत्र मंडल: अदृश्य';
    }});

    document.getElementById('btnReset').addEventListener('click', () => {{
      rotX = 1.1;
      rotZ = 0;
      speedMult = 1;
    }});

    function project(x, y, z) {{
      const cz = Math.cos(rotZ), sz = Math.sin(rotZ);
      const cx = Math.cos(rotX), sx = Math.sin(rotX);
      const x1 = x * cz - y * sz;
      const y1 = x * sz + y * cz;
      const y2 = y1 * cx - z * sx;
      const z2 = y1 * sx + z * cx;
      const fov = 800;
      const scale = fov / (fov + z2 + 400);
      return {{
        x: width / 2 + x1 * scale,
        y: height / 2 + y2 * scale,
        scale: scale,
        depth: z2
      }};
    }}

    function draw() {{
      ctx.clearRect(0, 0, width, height);

      // Draw Earth at Center
      const center = project(0, 0, 0);
      ctx.beginPath();
      ctx.arc(center.x, center.y, 16 * center.scale, 0, Math.PI * 2);
      ctx.fillStyle = '#0284c7';
      ctx.shadowColor = '#38bdf8';
      ctx.shadowBlur = 20;
      ctx.fill();
      ctx.shadowBlur = 0;

      // Draw Zodiac Wheel / Nakshatra Orbit
      if (showRings) {{
        ctx.beginPath();
        for (let a = 0; a <= Math.PI * 2; a += 0.05) {{
          const pt = project(Math.cos(a) * 380, Math.sin(a) * 380, 0);
          if (a === 0) ctx.moveTo(pt.x, pt.y);
          else ctx.lineTo(pt.x, pt.y);
        }}
        ctx.strokeStyle = 'rgba(16, 185, 129, 0.25)';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        // 12 Rashi Segments
        for (let r = 0; r < 12; r++) {{
          const angle = (r * Math.PI) / 6;
          const p1 = project(Math.cos(angle) * 360, Math.sin(angle) * 360, 0);
          const p2 = project(Math.cos(angle) * 400, Math.sin(angle) * 400, 0);
          ctx.beginPath();
          ctx.moveTo(p1.x, p1.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.strokeStyle = 'rgba(52, 211, 153, 0.4)';
          ctx.stroke();
        }}
      }}

      // Update and Draw Planets
      planets.forEach(p => {{
        p.angle += p.speed * speedMult;

        // Draw Orbit Path
        ctx.beginPath();
        for (let a = 0; a <= Math.PI * 2; a += 0.1) {{
          const pt = project(Math.cos(a) * p.radius, Math.sin(a) * p.radius, 0);
          if (a === 0) ctx.moveTo(pt.x, pt.y);
          else ctx.lineTo(pt.x, pt.y);
        }}
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Planet Coordinate
        const px = Math.cos(p.angle) * p.radius;
        const py = Math.sin(p.angle) * p.radius;
        const pt = project(px, py, 0);

        ctx.beginPath();
        ctx.arc(pt.x, pt.y, p.size * pt.scale, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.shadowColor = p.color;
        ctx.shadowBlur = 12;
        ctx.fill();
        ctx.shadowBlur = 0;

        // Label
        ctx.fillStyle = '#cbd5e1';
        ctx.font = `${{Math.round(11 * pt.scale)}}px sans-serif`;
        ctx.fillText(p.name, pt.x + 8 * pt.scale, pt.y - 4 * pt.scale);
      }});

      requestAnimationFrame(draw);
    }}

    draw();
  </script>
</body>
</html>
"""
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"[VideoConceptAgent] Interactive 3D simulation created: {html_path}")
        return html_path

if __name__ == "__main__":
    agent = VideoConceptAgent()
    agent.generate_video_blueprints()
    agent.generate_interactive_3d_animation()
