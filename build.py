#!/usr/bin/env python3
"""
Build script: converts markdown files in /markdown to HTML in /docs.
Uses a shared template with nav, hero, and footer.
Run: python build.py
"""
import os
import re
import markdown
from pathlib import Path

BASE_DIR = Path(__file__).parent
MD_DIR = BASE_DIR / "markdown"
HTML_DIR = BASE_DIR / "docs"
CSS_REL = "assets/css/clinical.css"

HTML_DIR.mkdir(exist_ok=True)

# Extract metadata from markdown frontmatter (simple YAML-like)
def parse_frontmatter(text):
    meta = {}
    if text.startswith("---"):
        end = text.index("---", 3)
        for line in text[3:end].strip().split("\n"):
            if ":" in line:
                key, val = line.split(":", 1)
                meta[key.strip()] = val.strip()
        text = text[end+3:].strip()
    return meta, text

NAV_LINKS = [
    ("index.html", "Home"),
    ("carpal-tunnel.html", "Carpal Tunnel"),
    ("cubital-tunnel.html", "Cubital Tunnel"),
    ("muscular-dystrophy.html", "Muscular Dystrophy"),
    ("ehlers-danlos.html", "Ehlers-Danlos"),
    ("de-quervains.html", "De Quervain's"),
    ("dupuytrens.html", "Dupuytren's"),
    ("trigger-finger.html", "Trigger Finger"),
    ("shoulder-neck.html", "Shoulder & Neck"),
    ("hsa-draft.html", "HSA Draft"),
]

def build_nav(current_file):
    links = []
    for href, label in NAV_LINKS:
        cls = ' style="color:#fff;font-weight:700"' if href == current_file else ''
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n    ".join(links)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Svalboard Clinical</title>
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <nav class="top-nav">
    <a href="index.html" class="brand">
      <span class="brand-wordmark">svalboard</span>
      <span class="brand-divider"></span>
      <span class="brand-text">Clinical</span>
    </a>
    {nav}
  </nav>

  <div class="hero" style="{hero_style}">
    <h1>{hero_title}</h1>
    <p class="subtitle">{hero_subtitle}</p>
    {hero_buttons}
  </div>

  <div class="content">
    {body}
  </div>

  <footer class="footer">
    <p>Svalboard Clinical Resources - For healthcare providers and patients</p>
    <p><a href="https://svalboard.com">svalboard.com</a> &middot; <a href="https://svalboard.substack.com">Substack</a></p>
  </footer>
</body>
</html>
"""

# Default hero buttons for clinical pages
DEFAULT_BUTTONS = (
    '<div class="cta-group">\n'
    '      <a href="#provider" class="btn btn-primary">Provider Overview</a>\n'
    '      <a href="#mechanism" class="btn btn-outline">See the Biomechanics</a>\n'
    '    </div>'
)

def build_hero_buttons(meta):
    """Build hero CTA buttons from frontmatter, or use defaults."""
    if meta.get("hero_buttons", "").lower() == "none":
        return ""
    btn1_text = meta.get("hero_btn1_text", "")
    btn1_href = meta.get("hero_btn1_href", "")
    btn2_text = meta.get("hero_btn2_text", "")
    btn2_href = meta.get("hero_btn2_href", "")
    if not btn1_text and not btn2_text:
        return DEFAULT_BUTTONS
    parts = ['<div class="cta-group">']
    if btn1_text and btn1_href:
        parts.append(f'      <a href="{btn1_href}" class="btn btn-primary">{btn1_text}</a>')
    if btn2_text and btn2_href:
        parts.append(f'      <a href="{btn2_href}" class="btn btn-outline">{btn2_text}</a>')
    parts.append('    </div>')
    return "\n".join(parts)

# Condition accent colors for hero gradients
HERO_COLORS = {
    "carpal-tunnel": "background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);",
    "cubital-tunnel": "background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);",
    "muscular-dystrophy": "background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);",
    "ehlers-danlos": "background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);",
    "de-quervains": "background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);",
    "dupuytrens": "background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);",
    "trigger-finger": "background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);",
    "shoulder-neck": "background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);",
    "index": "background: #121212;",
}

def process_markdown(md_text):
    """Convert markdown to HTML with extensions."""
    md = markdown.Markdown(extensions=[
        'tables', 'fenced_code', 'attr_list', 'toc', 'md_in_html'
    ])
    return md.convert(md_text)

def build_file(md_path):
    text = md_path.read_text(encoding="utf-8")
    meta, body_md = parse_frontmatter(text)

    title = meta.get("title", "Svalboard Clinical")
    hero_title = meta.get("hero_title", title)
    hero_subtitle = meta.get("hero_subtitle", "")

    stem = md_path.stem
    hero_style = HERO_COLORS.get(stem, "")

    body_html = process_markdown(body_md)

    out_name = stem + ".html"
    nav = build_nav(out_name)
    hero_buttons = build_hero_buttons(meta)

    html = TEMPLATE.format(
        title=title,
        css=CSS_REL,
        nav=nav,
        hero_style=hero_style,
        hero_title=hero_title,
        hero_subtitle=hero_subtitle,
        hero_buttons=hero_buttons,
        body=body_html,
    )

    out_path = HTML_DIR / out_name
    out_path.write_text(html, encoding="utf-8")
    print(f"  Built: {out_path.name}")

def copy_assets():
    """Copy assets into docs/ so GitHub Pages can serve them."""
    import shutil
    src = BASE_DIR / "assets"
    dst = HTML_DIR / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print("  Copied assets/")

def main():
    md_files = sorted(MD_DIR.glob("*.md"))
    if not md_files:
        print("No markdown files found in /markdown")
        return

    print(f"Building {len(md_files)} pages...")
    for f in md_files:
        build_file(f)
    copy_assets()
    print("Done!")

if __name__ == "__main__":
    main()
