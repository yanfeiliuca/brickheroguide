# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

BrickHeroGuide.com — a static HTML fan-site guide for the game **LEGO Batman: Legacy of the Dark Knight**. Content-focused gaming guide with SEO, Google Analytics, and AdSense monetization.

## Hosting & Deployment

- **Cloudflare Pages** with static asset serving (`wrangler.jsonc`). The assets directory is `.` (root), so any `.html` file pushed to `main` is deployed live.
- No build step, no package.json, no framework — just static HTML.

## Site Architecture

Every page is fully self-contained: inline `<style>`, inline `<script>`, no external CSS/JS dependencies.

### Design System
- Dark theme: `--bg: #0f1117`, `--bg-card: #1a1d27`, yellow accent `--accent: #fbbf24`
- All CSS custom properties are defined in a `:root` block at the top of each page's `<style>`
- Mobile responsive via `@media (max-width: 768px)` breakpoint
- Sticky nav with `backdrop-filter: blur(12px)`, mobile hamburger menu toggle

### Shared boilerplate on every page
1. **Google Analytics** (`G-F7BNQ7RJDY`) — the `<script async src="https://www.googletagmanager.com/gtag/js?id=G-F7BNQ7RJDY">` block must be at the top of `<head>`
2. **Sticky nav** — logo "BrickHeroGuide" (gear icon + yellow "Hero"), nav links, mobile hamburger
3. **Footer** — links to Home/About/Privacy/Contact, copyright, fan-site disclaimer (not affiliated with LEGO/DC/Warner Bros.)

### Directory Structure
- `index.html` — homepage: hero stats, guide category cards, article list, collectibles section, tips section
- `about.html`, `contact.html`, `privacy.html` — simple standalone pages
- `guides/` — ~20 guide pages. Each follows a common pattern: breadcrumb, article-header with tag + h1 + meta, quick-stats grid, table of contents (`.toc`), `page-layout` grid (1fr + 280px sidebar), article body with sections
- `blog/` — blog index (`blog/index.html`) with blog-layout grid (1fr + 300px sidebar) + individual blog posts
- `sitemap.xml` — auto-generated, do not edit manually
- `generate-sitemap.py` — Python script that scans all `.html` files and produces `sitemap.xml`

### Guide Page Tags
CSS tag classes used across guide/article pages:
- `.tag-walkthrough` (blue) — mission walkthroughs
- `.tag-collectible` (green) — collectible/minikit guides
- `.tag-tips` (yellow) — tips & tricks
- `.tag-characters` (purple) — character/unlock guides
- Blog: `.tag-review` (green), `.tag-news` (blue), `.tag-community` (purple), `.tag-analysis` (yellow)

## Adding a New Guide Page

1. Copy an existing guide page from `guides/` as a template (e.g., `mission-1-walkthrough.html`)
2. Update the title, meta description, canoncical URL, and OG tags
3. Update breadcrumb, article tag, h1, quick-stats, TOC, and article body
4. Add a link to the new page from `index.html`
5. Run `python generate-sitemap.py` for local preview, or push to `main` — the GitHub Action auto-generates the sitemap

## Sitemap Automation

`.github/workflows/auto-sitemap.yml` runs on every push to `main` when `.html` files change:
- Runs `python generate-sitemap.py` to regenerate `sitemap.xml`
- Commits the updated sitemap back (commit message includes `[auto-sitemap]`)
- Pings Google and Bing with the new sitemap URL after a 120s Cloudflare deploy delay

The workflow guards against recursive runs by checking if the commit message contains `[auto-sitemap]`.

## Blog Content Automation

At the start of every session, search the web for the latest news about **LEGO Batman: Legacy of the Dark Knight** and write a new blog post. This keeps the site fresh with minimal effort.

### Workflow

1. **Search for news** — Use `WebSearch` or `curl` to find recent articles about the game (reviews, updates, DLC announcements, community highlights, sales figures, etc.). The game launched May 22, 2026, so post-launch content is expected.
2. **Pick one newsworthy topic** — Choose the most interesting/relevant recent development. Avoid duplicating topics already covered in existing blog posts (check `blog/` first).
3. **Write the blog post** — Copy `blog/lego-batman-series-visual-evolution.html` as a template. Follow the same structure:
   - Same `<head>` boilerplate (GA tag, meta, styles, nav, footer)
   - `article-header` with appropriate tags (`.tag-news` for news, `.tag-review` for reviews, `.tag-analysis` for analysis, `.tag-community` for community)
   - Body content in `.content` div — well-structured with `<h2>`/`<h3>`, at least 500 words
   - Include a featured image — **every new post must use a different image from the library below**. Reference it via the external CDN URL (no local download needed). Set both the `<img src="">` and the `<meta property="og:image">` to the same image URL.
   - OG tags for social sharing (title, description, `og:image`)
   - **No fabricated content** — only report verifiable facts with source links. Use hedging language ("reportedly", "according to") for developing stories.
4. **File naming** — `blog/<topic-slug>.html` (lowercase, hyphenated, descriptive)
5. **Update blog index** — Add the new post card to `blog/index.html` at the top of `.blog-list` (reverse chronological order). The card follows this format:
   ```html
   <a href="<topic-slug>.html" class="blog-card">
     <div class="blog-card-tags">
       <span class="blog-tag tag-news">News</span>
     </div>
     <h2>Post Title Here</h2>
     <p class="blog-card-excerpt">Compelling 1-2 sentence excerpt...</p>
     <div class="blog-card-meta">
       <span>&#128197; Month DD, 2026</span>
       <span>&#9201; X min read</span>
       <span>&#128172; Category</span>
     </div>
   </a>
   ```
6. **Run `python generate-sitemap.py`** to include the new page.
7. **Commit** with a message like `"Added blog post: <title>"`.

### Image Attribution Format

Every featured image must include a `<figcaption>` with this format:

```html
<figcaption>[Descriptive caption of what's shown]. Image: &copy; TT Games / Warner Bros. Games. Official promotional screenshot via <a href="https://legobatmangame.com" target="_blank" rel="noopener">legobatmangame.com</a>, used for editorial purposes.</figcaption>
```

For the cover art (Wikipedia source), use:
```html
<figcaption>[Caption]. Image: &copy; TT Games / Warner Bros. Games. Source: <a href="https://en.wikipedia.org/wiki/File:Lego_Batman_Legacy_of_the_Dark_Knight_cover_art.jpg" target="_blank" rel="noopener noreferrer">Wikipedia</a> — used for editorial identification under fair use.</figcaption>
```

### Official Image Library

All images are official promotional screenshots from `legobatmangame.com` — © TT Games / Warner Bros. Games, used for editorial fan-site purposes. **Check this list before each new post and pick one not yet used.**

| Image URL | Description | Used in |
|---|---|---|
| `/images/lego-batman-legacy-cover.jpg` | Official cover art (local, from Wikipedia) | lego-batman-series-visual-evolution.html |
| `https://legobatmangame.com/_astro/origin.DSZma2rC_2hKTV2.webp` | Young Bruce Wayne ascending a cliffside + Batman in moonlight (origin diptych) | lego-batman-legacy-launch-preview.html |
| `https://legobatmangame.com/_astro/foes.CtQfCF5a_1k24YI.webp` | Batman holds Joker up by the shirt | easter-eggs-hidden-references.html |
| `https://legobatmangame.com/_astro/fight-2.BFd6neBb_2adSpB.webp` | Red Hood Gang member vs Batman face-off in industrial room | launch-day-reception.html |
| `https://legobatmangame.com/_astro/postfooter.Bp36eHDB_Z2cb3ek.webp` | Red Hood reaches from acid vat, Joker card floating nearby | developer-interview-roundup.html |
| `https://legobatmangame.com/_astro/clues-2.D9jQ9zQy_Z12vcyH.webp` | Gotham City at night — neon lights, billboards, Bat-Signal in sky | *available* |
| `https://legobatmangame.com/_astro/family.CQW_jlFK_2qvCfg.webp` | Commissioner Gordon and Catwoman smiling (Bat-Family) | *available* |
| `https://legobatmangame.com/_astro/fight-3.KeK453wH_Z23bgKb.webp` | Mr. Freeze sits in his Freeze Truck, grinning | *available* |
| `https://legobatmangame.com/_astro/gear-3.5F2kKy0I_1z9tbe.webp` | Batman rides Batcycle through Gotham City streets | *available* |
| `https://legobatmangame.com/_astro/og-image.BcIYb3Fq.jpg` | Official OG image (key art, horizontal) | *available* |
| `https://clan.fastly.steamstatic.com/images/45746841/c84e906c37b4bf2fd1c6297b933f31a2479fd477.png` | Heroes & Villains Trailer promo image (Steam) | *available* |

When all images in the table are used, cycle back to ones with the oldest posts, or search for new official screenshots.

### Blog Post Ideas
- Review roundups (Metacritic scores, critic quotes with sources)
- New DLC or update announcements
- Community discoveries (Easter eggs, speedrun records, hidden secrets)
- Sales milestones or player count announcements
- Comparisons with other LEGO games
- Character/suit deep dives based on post-launch gameplay

## Session Work Tracking

At the end of every session, update `PROGRESS.md` with a summary of all work completed during that session. Follow the existing format: date heading, context, completed work sections, and a verification checklist. This file is the authoritative work log for the project.

## Git Conventions

- Branch: `main` only (no PR workflow)
- Commit messages: past-tense, brief ("Added Blog page", "Added Mission 3-4")
