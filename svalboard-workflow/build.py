#!/usr/bin/env python3
"""
Build script for Svalboard Workflow site.
Converts markdown files in /markdown to HTML in /docs.
Run: python build.py
"""
import markdown
from pathlib import Path

BASE_DIR = Path(__file__).parent
REPO_DIR = BASE_DIR.parent
MD_DIR = BASE_DIR / "markdown"
HTML_DIR = REPO_DIR / "docs" / "workflow"

# Reuse the clinical site's CSS
CSS_REL = "assets/css/clinical.css"

HTML_DIR.mkdir(exist_ok=True)

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
    ("future-of-writing.html", "Home"),
    ("speech.html", "Speech"),
    ("gaze.html", "Gaze"),
    ("motor-input.html", "Motor Input"),
    ("memory.html", "Memory"),
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
  <title>{title} - Svalboard Workflow</title>
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <nav class="top-nav">
    <a href="future-of-writing.html" class="brand">
      <span class="brand-wordmark">svalboard</span>
      <span class="brand-divider"></span>
      <span class="brand-text">Workflow</span>
    </a>
    {nav}
  </nav>

  <div class="hero" style="{hero_style}">
    <h1>{hero_title}</h1>
    <p class="subtitle">{hero_subtitle}</p>
  </div>

  <div class="content">
    {body}
  </div>

  <footer class="footer">
    <p>Svalboard Workflow - Tools and workflows for sustainable knowledge work</p>
    <p><a href="https://svalboard.com">svalboard.com</a> &middot; <a href="https://svalboard.substack.com">Substack</a></p>
  </footer>
</body>
</html>
"""

HERO_COLORS = {
    "future-of-writing": "background: linear-gradient(135deg, #121212 0%, #1a2e1a 100%);",
    "speech": "background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);",
    "gaze": "background: linear-gradient(135deg, #121212 0%, #2e1a2e 100%);",
    "motor-input": "background: linear-gradient(135deg, #121212 0%, #1a2e1a 100%);",
    "memory": "background: linear-gradient(135deg, #121212 0%, #2e2a1a 100%);",
}

def process_markdown(md_text):
    md = markdown.Markdown(extensions=[
        'tables', 'fenced_code', 'attr_list', 'toc', 'md_in_html'
    ])
    return md.convert(md_text)

def build_file(md_path):
    text = md_path.read_text(encoding="utf-8")
    meta, body_md = parse_frontmatter(text)

    title = meta.get("title", "Svalboard Workflow")
    hero_title = meta.get("hero_title", title)
    hero_subtitle = meta.get("hero_subtitle", "")

    stem = md_path.stem
    hero_style = HERO_COLORS.get(stem, "")
    body_html = process_markdown(body_md)

    out_name = stem + ".html"
    nav = build_nav(out_name)

    html = TEMPLATE.format(
        title=title,
        css=CSS_REL,
        nav=nav,
        hero_style=hero_style,
        hero_title=hero_title,
        hero_subtitle=hero_subtitle,
        body=body_html,
    )

    out_path = HTML_DIR / out_name
    out_path.write_text(html, encoding="utf-8")
    print(f"  Built: {out_path.name}")

def copy_assets():
    """Copy assets from the shared repo assets/ into workflow docs/."""
    import shutil
    src = REPO_DIR / "assets"
    dst = HTML_DIR / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print("  Copied assets/")

def main():
    md_files = sorted(MD_DIR.glob("*.md"))
    if not md_files:
        print("No markdown files found in svalboard-workflow/markdown/")
        return

    print(f"Building {len(md_files)} workflow pages...")
    for f in md_files:
        build_file(f)
    copy_assets()
    print("Done!")

if __name__ == "__main__":
    main()
