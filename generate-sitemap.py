"""
BrickHeroGuide - Automatic Sitemap Generator
=============================================
Usage:  python generate-sitemap.py
Output: sitemap.xml (in the same folder)

This script scans the current folder and guides/ subfolder
for all .html files and generates a fresh sitemap.xml.
Run it locally to preview, or let the GitHub Action run it
automatically after each push.
"""

import os
import sys
import datetime

# Fix Windows console encoding so paths with non-ASCII characters don't crash
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# === Configuration ===
DOMAIN = "https://brickheroguide.com"
TODAY = datetime.date.today().isoformat()

# Priority rules: filename pattern -> (priority, changefreq)
PRIORITY_RULES = {
    "index.html":    ("1.0", "daily"),
    "privacy.html":  ("0.3", "monthly"),
    "about.html":    ("0.3", "monthly"),
    "contact.html":  ("0.3", "monthly"),
}

# Guide-level priority rules (checked by keyword in filename)
GUIDE_PRIORITY = {
    "mission-":          ("0.9", "weekly"),   # Mission walkthroughs
    "all-characters":    ("0.9", "weekly"),   # Character guide
    "release-date":      ("0.7", "monthly"),  # Info pages
    "deluxe-edition":    ("0.7", "monthly"),
    "pc-requirements":   ("0.6", "monthly"),
    "is-it-good":        ("0.7", "monthly"),
}
DEFAULT_GUIDE = ("0.8", "weekly")


def get_priority(filepath):
    """Determine priority and changefreq based on filename."""
    filename = os.path.basename(filepath)

    # Check exact matches first
    if filename in PRIORITY_RULES:
        return PRIORITY_RULES[filename]

    # Check keyword matches for guides
    for keyword, values in GUIDE_PRIORITY.items():
        if keyword in filename:
            return values

    return DEFAULT_GUIDE


def scan_html_files(root_dir):
    """Find all .html files and return as list of (url_path, priority, changefreq)."""
    pages = []

    # Directories that are not part of the published site (internal working
    # files, stray nested clones, etc.) and must never be crawled or listed
    # in sitemap.xml.
    EXCLUDED_DIRS = {'data'}  # internal data files / audit tools, not public content

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories and known non-site directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in EXCLUDED_DIRS]

        for filename in sorted(filenames):
            if not filename.endswith('.html'):
                continue

            filepath = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(filepath, root_dir).replace('\\', '/')

            # Build URL
            if rel_path == 'index.html':
                url = f"{DOMAIN}/"
            else:
                url = f"{DOMAIN}/{rel_path}"

            priority, changefreq = get_priority(filepath)
            pages.append((url, priority, changefreq))

    return pages


def generate_sitemap(pages):
    """Generate sitemap XML string."""
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '',
    ]

    for url, priority, changefreq in pages:
        lines.append('  <url>')
        lines.append(f'    <loc>{url}</loc>')
        lines.append(f'    <lastmod>{TODAY}</lastmod>')
        lines.append(f'    <changefreq>{changefreq}</changefreq>')
        lines.append(f'    <priority>{priority}</priority>')
        lines.append('  </url>')

    lines.append('')
    lines.append('</urlset>')
    return '\n'.join(lines)


def main():
    # Get the directory where this script lives
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print(f"Scanning: {script_dir}")
    pages = scan_html_files(script_dir)

    print(f"Found {len(pages)} HTML pages:")
    for url, priority, _ in pages:
        print(f"  [{priority}] {url}")

    sitemap_content = generate_sitemap(pages)
    output_path = os.path.join(script_dir, 'sitemap.xml')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"\nSitemap generated: {output_path}")
    print(f"Total pages: {len(pages)}")
    print(f"Date stamp: {TODAY}")


if __name__ == '__main__':
    main()
