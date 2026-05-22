"""
Daily blog generator for BrickHeroGuide.com
=============================================
Runs via GitHub Actions on a schedule (daily at 9am UTC+8).
Gathers the latest news about LEGO Batman: Legacy of the Dark Knight,
calls the Anthropic API to evaluate newsworthiness and generate a blog post,
then commits the new post to the repository.

Requirements:
  pip install anthropic requests
  Environment variable: ANTHROPIC_API_KEY
"""

import os
import sys
import json
import re
import datetime
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

# Anthropic SDK
try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

# ── Configuration ──────────────────────────────────────────────

GAME_FULL_NAME = "LEGO Batman: Legacy of the Dark Knight"
WIKIPEDIA_PAGE = "Lego_Batman:_Legacy_of_the_Dark_Knight"
DOMAIN = "https://brickheroguide.com"
REPO_ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = REPO_ROOT / "blog"
TEMPLATE_FILE = BLOG_DIR / "lego-batman-legacy-launch-preview.html"
BLOG_INDEX_FILE = BLOG_DIR / "index.html"
SITEMAP_SCRIPT = REPO_ROOT / "generate-sitemap.py"

TODAY = datetime.date.today()
TODAY_STR = TODAY.strftime("%B %d, %Y").replace(" 0", " ")
TODAY_ISO = TODAY.isoformat()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
if not ANTHROPIC_API_KEY:
    print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
    sys.exit(1)

client = Anthropic(api_key=ANTHROPIC_API_KEY)


# ── Data Gathering ─────────────────────────────────────────────

def get_existing_posts():
    """Return list of existing blog post filenames (without .html)."""
    posts = []
    if BLOG_DIR.exists():
        for f in sorted(BLOG_DIR.glob("*.html")):
            if f.name != "index.html":
                posts.append(f.stem)
    return posts


def fetch_wikipedia_revisions():
    """Fetch recent revisions to the Wikipedia page."""
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "titles": WIKIPEDIA_PAGE,
        "rvlimit": 5,
        "rvprop": "timestamp|comment|user",
        "rvdir": "older",
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        data = resp.json()
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            return page.get("revisions", [])
    except Exception as e:
        print(f"  Wikipedia API error: {e}")
    return []


def fetch_wikipedia_extract():
    """Fetch current Wikipedia page extract (first 4000 chars)."""
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": WIKIPEDIA_PAGE,
        "explaintext": 1,
        "exintro": 0,
        "exlimit": 1,
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        data = resp.json()
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            text = page.get("extract", "")
            return text[:4000]
    except Exception as e:
        print(f"  Wikipedia extract error: {e}")
    return ""


def search_google_news():
    """Search Google News RSS for recent articles about the game."""
    url = "https://news.google.com/rss/search"
    params = {
        "q": f"LEGO Batman Legacy Dark Knight",
        "hl": "en-US",
        "gl": "US",
        "ceid": "US:en",
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code != 200:
            print(f"  Google News returned HTTP {resp.status_code}")
            return []
        root = ET.fromstring(resp.text)
        items = []
        for item in root.iter("item"):
            title_el = item.find("title")
            pubdate_el = item.find("pubDate")
            link_el = item.find("link")
            source_el = item.find("source")
            items.append({
                "title": title_el.text if title_el is not None else "",
                "pubDate": pubdate_el.text if pubdate_el is not None else "",
                "link": link_el.text if link_el is not None else "",
                "source": source_el.text if source_el is not None else "",
            })
        return items[:10]
    except ET.ParseError as e:
        print(f"  Google News RSS parse error: {e}")
    except Exception as e:
        print(f"  Google News error: {e}")
    return []


# ── Anthropic API Call ─────────────────────────────────────────

def generate_blog_post(wiki_revisions, wiki_extract, news_items, existing_posts):
    """Call Anthropic API to evaluate newsworthiness and generate blog content."""

    wiki_rev_text = "\n".join(
        f"- {r.get('timestamp','')}: {r.get('comment','no comment')} (by {r.get('user','unknown')})"
        for r in wiki_revisions[:5]
    ) if wiki_revisions else "(no recent revisions)"

    news_text = "\n".join(
        f"- [{n['source']}] {n['title']} ({n['pubDate']})"
        for n in news_items[:10]
    ) if news_items else "(no recent news found)"

    posts_text = "\n".join(f"- {p}" for p in existing_posts) if existing_posts else "(none)"

    prompt = f"""You are a blog editor for BrickHeroGuide.com, a fan guide site for {GAME_FULL_NAME}.

Here is the latest available data:

── Wikipedia Recent Revisions ──
{wiki_rev_text}

── Wikipedia Content (first 4000 chars) ──
{wiki_extract[:3000]}

── Google News Headlines ──
{news_text}

── Existing Blog Posts (slugs) ──
{posts_text}

── Today's Date ──
{TODAY_STR}

First, determine if there is genuinely newsworthy new information worth a blog post. If the news items and Wikipedia revisions contain nothing substantially new (no new review scores, no DLC/update announcements, no sales milestones, no community discoveries, no developer statements), respond with:
{{"newsworthy": false, "reason": "explain why no post is needed"}}

If there IS newsworthy content, respond with a JSON object containing the blog post:
{{
  "newsworthy": true,
  "title": "Post title (compelling, SEO-friendly, under 60 chars)",
  "slug": "url-friendly-slug",
  "excerpt": "1-2 sentence excerpt for the blog card (under 160 chars)",
  "tags": ["News"],
  "read_time": "X min read",
  "meta_description": "SEO meta description (under 160 chars)",
  "keywords": "comma, separated, keywords",
  "content_html": "<full blog post body HTML using only <p>, <h2>, <h3>, <ul>, <li>, <strong>, <a>, <figure>, <figcaption>, <img>, <div class='tip-box'>, <div class='highlight-box'>, <div class='quick-facts'>, <div class='qf-item'>, <div class='qf-label'>, <div class='qf-value'> tags. At least 400 words. Use the site's design patterns: quick-facts grid for stats, tip-box for callouts, highlight-box for key info. No inline CSS. All source claims must be linked. No fabricated content — only verifiable facts from the provided data. Use hedging language for developing stories. Do not invent review scores, quotes, or release dates."
}}

IMPORTANT: Only return valid JSON. Do not wrap in markdown code blocks."""

    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=4000,
            system="You are a blog editor for BrickHeroGuide.com. You write factual, well-structured blog posts about LEGO Batman: Legacy of the Dark Knight. You NEVER fabricate content — every claim must be traceable to provided source data. You return only valid JSON.",
            messages=[{"role": "user", "content": prompt}],
        )

        text = response.content[0].text.strip()

        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

        return json.loads(text)

    except json.JSONDecodeError as e:
        print(f"  Failed to parse API response as JSON: {e}")
        print(f"  Raw response: {text[:500]}")
        return {"newsworthy": False, "reason": f"JSON parse error: {e}"}
    except Exception as e:
        print(f"  Anthropic API error: {e}")
        return {"newsworthy": False, "reason": f"API error: {e}"}


# ── HTML Generation ────────────────────────────────────────────

def html_escape(text):
    """Escape text for safe HTML attribute/body insertion."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def generate_blog_html(post_data):
    """Generate the full blog post HTML from the template and post data."""
    if not TEMPLATE_FILE.exists():
        print(f"  ERROR: Template file not found: {TEMPLATE_FILE}")
        return None

    template = TEMPLATE_FILE.read_text(encoding="utf-8")

    title = post_data["title"]
    safe_title = html_escape(title)
    safe_canonical = html_escape(post_data["slug"])
    safe_meta_desc = html_escape(post_data.get("meta_description", post_data["excerpt"]))
    safe_keywords = html_escape(post_data.get("keywords", ""))
    safe_og_desc = html_escape(post_data.get("meta_description", post_data["excerpt"]))
    safe_excerpt = html_escape(post_data["excerpt"])
    tag_html = post_data.get("tags_html", "")
    if not tag_html:
        tags = post_data.get("tags", ["News"])
        tag_spans = []
        for tag in tags:
            tag_lower = tag.lower()
            if tag_lower in ("news", "review", "analysis", "community"):
                tag_spans.append(f'<span class="article-tag tag-{tag_lower}">{tag}</span>')
            else:
                tag_spans.append(f'<span class="article-tag tag-news">{tag}</span>')
        tag_html = "\n        ".join(tag_spans)
    read_time = post_data.get("read_time", "3 min read")
    content_html = post_data["content_html"]

    # ── Targeted replacements ──

    # <title>
    template = re.sub(
        r"<title>.*?</title>",
        f"<title>{safe_title} - BrickHeroGuide</title>",
        template, count=1,
    )

    # Meta description
    template = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{safe_meta_desc}">',
        template, count=1,
    )

    # Meta keywords
    template = re.sub(
        r'<meta name="keywords" content=".*?">',
        f'<meta name="keywords" content="{safe_keywords}">',
        template, count=1,
    )

    # Canonical URL
    template = re.sub(
        r'<link rel="canonical" href="https://brickheroguide\.com/blog/.*?">',
        f'<link rel="canonical" href="https://brickheroguide.com/blog/{safe_canonical}.html">',
        template, count=1,
    )

    # OG title
    template = re.sub(
        r'<meta property="og:title" content=".*?">',
        f'<meta property="og:title" content="{safe_title}">',
        template, count=1,
    )

    # OG description
    template = re.sub(
        r'<meta property="og:description" content=".*?">',
        f'<meta property="og:description" content="{safe_og_desc}">',
        template, count=1,
    )

    # OG image — keep existing if present, otherwise remove
    if not post_data.get("og_image"):
        template = re.sub(
            r'<meta property="og:image" content=".*?">\n',
            "",
            template, count=1,
        )

    # Breadcrumb last segment
    template = re.sub(
        r"(&rsaquo; ).*?(</div>\s*<div class=\"article-header\">)",
        rf"\1{safe_title}\2",
        template, count=1,
    )

    # Article tags in header
    template = re.sub(
        r'(<div class="article-header">\s*)\n?(<span class="article-tag[^<]*</span>\s*)+',
        rf'\1{tag_html}',
        template, count=1,
    )

    # H1 title
    template = re.sub(
        r"<h1>.*?</h1>",
        f"<h1>{safe_title}</h1>",
        template, count=1,
    )

    # Article meta (date + read time)
    template = re.sub(
        r'<div class="article-meta">Published: .*?</div>',
        f'<div class="article-meta">Published: {TODAY_STR} &middot; {read_time}</div>',
        template, count=1,
    )

    # Content div inner HTML
    content_pattern = re.compile(
        r'(<div class="content">)\s*(.*?)\s*(</div>\s*</main>)',
        re.DOTALL,
    )
    template = content_pattern.sub(
        rf"\1\n        {content_html}\n\n      \3",
        template,
        count=1,
    )

    # Update sidebar "More Blog Posts" — add new post at top
    new_sidebar_link = f'<a href="{safe_canonical}.html" class="sidebar-link">{safe_title}</a>'
    # Find the first sidebar-link in the "More Blog Posts" section and insert before it
    sidebar_pattern = re.compile(
        r'(<div class="sidebar-box">\s*<h3>More Blog Posts</h3>\s*)(<a href="[^"]*\.html" class="sidebar-link">)',
        re.DOTALL,
    )
    template = sidebar_pattern.sub(
        rf"\1{new_sidebar_link}\n        \2",
        template,
        count=1,
    )

    return template


def update_blog_index(post_data):
    """Insert a new blog card at the top of blog/index.html."""
    if not BLOG_INDEX_FILE.exists():
        print("  ERROR: Blog index file not found")
        return False

    index_html = BLOG_INDEX_FILE.read_text(encoding="utf-8")

    title = html_escape(post_data["title"])
    slug = html_escape(post_data["slug"])
    excerpt = html_escape(post_data["excerpt"])
    read_time = post_data.get("read_time", "3 min read")

    tags = post_data.get("tags", ["News"])
    tag_spans = "\n          ".join(
        f'<span class="blog-tag tag-{t.lower()}">{t}</span>' for t in tags
    )

    category = tags[0] if tags else "News"

    new_card = f"""<a href="{slug}.html" class="blog-card">
        <div class="blog-card-tags">
          {tag_spans}
        </div>
        <h2>{title}</h2>
        <p class="blog-card-excerpt">{excerpt}</p>
        <div class="blog-card-meta">
          <span>&#128197; {TODAY_STR}</span>
          <span>&#9201; {read_time}</span>
          <span>&#128172; {category}</span>
        </div>
      </a>"""

    # Insert after the opening <div class="blog-list"> and its newline
    insertion_marker = '<div class="blog-list">\n'
    if insertion_marker in index_html:
        index_html = index_html.replace(
            insertion_marker,
            insertion_marker + "\n      " + new_card + "\n\n",
            1,
        )
        BLOG_INDEX_FILE.write_text(index_html, encoding="utf-8")
        print("  Blog index updated with new card")
        return True
    else:
        print("  ERROR: Could not find insertion point in blog index")
        return False


# ── Git Operations ─────────────────────────────────────────────

def run_git(*args):
    """Run a git command in the repo root."""
    cmd = ["git", "-C", str(REPO_ROOT)] + list(args)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  Git error: {result.stderr.strip()}")
    return result


def commit_and_push(slug):
    """Stage, commit, and push the new blog post and updated index."""
    blog_file = BLOG_DIR / f"{slug}.html"

    run_git("config", "user.name", "github-actions[bot]")
    run_git("config", "user.email", "github-actions[bot]@users.noreply.github.com")

    run_git("add", str(blog_file), str(BLOG_INDEX_FILE))

    # Run sitemap generator
    print("  Running sitemap generator...")
    sitemap_result = subprocess.run(
        ["python3", str(SITEMAP_SCRIPT)],
        capture_output=True, text=True, cwd=str(REPO_ROOT),
    )
    if sitemap_result.returncode == 0:
        run_git("add", str(REPO_ROOT / "sitemap.xml"))
        print("  Sitemap regenerated")
    else:
        print(f"  Sitemap generator error: {sitemap_result.stderr}")

    # Check if there are changes to commit
    diff_result = run_git("diff", "--cached", "--quiet")
    if diff_result.returncode == 0:
        print("  No changes to commit")
        return False

    commit_msg = f"[daily-blog] New post: {slug}"
    run_git("commit", "-m", commit_msg)
    run_git("push")
    print(f"  Committed and pushed: {commit_msg}")
    return True


# ── Main ───────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print(f"BrickHeroGuide Daily Blog Generator")
    print(f"Date: {TODAY_STR}")
    print("=" * 60)

    # 1. Gather existing posts
    print("\n[1/4] Checking existing blog posts...")
    existing = get_existing_posts()
    print(f"  Found {len(existing)} existing posts")

    # 2. Gather news data
    print("\n[2/4] Gathering news data...")

    print("  Fetching Wikipedia revisions...")
    wiki_revisions = fetch_wikipedia_revisions()
    print(f"  Got {len(wiki_revisions)} revisions")

    print("  Fetching Wikipedia extract...")
    wiki_extract = fetch_wikipedia_extract()
    print(f"  Got {len(wiki_extract)} chars")

    print("  Searching Google News...")
    news_items = search_google_news()
    print(f"  Got {len(news_items)} news items")
    for n in news_items[:3]:
        print(f"    - [{n['source']}] {n['title'][:80]}")

    # 3. Call Anthropic API
    print("\n[3/4] Calling Anthropic API to evaluate and generate...")
    result = generate_blog_post(wiki_revisions, wiki_extract, news_items, existing)

    if not result.get("newsworthy"):
        reason = result.get("reason", "No newsworthy content found")
        print(f"  SKIPPING: {reason}")
        print("\nNo blog post generated today. Exiting cleanly.")
        return

    print(f"  Newsworthy! Generating post: \"{result.get('title', 'Untitled')}\"")
    slug = result.get("slug", "")
    if not slug:
        print("  ERROR: No slug in API response")
        sys.exit(1)

    # Safety check: don't overwrite existing posts
    if slug in existing:
        print(f"  WARNING: Post with slug '{slug}' already exists. Appending date suffix.")
        slug = f"{slug}-{TODAY_ISO}"
        result["slug"] = slug

    # 4. Write files and commit
    print(f"\n[4/4] Writing files and committing...")

    print("  Generating blog HTML...")
    blog_html = generate_blog_html(result)
    if blog_html is None:
        print("  ERROR: Failed to generate blog HTML")
        sys.exit(1)

    blog_path = BLOG_DIR / f"{slug}.html"
    blog_path.write_text(blog_html, encoding="utf-8")
    print(f"  Blog post written: {blog_path}")

    print("  Updating blog index...")
    update_blog_index(result)

    print("  Committing and pushing...")
    commit_and_push(slug)

    print(f"\nDone! New blog post: {slug}.html")


if __name__ == "__main__":
    main()
