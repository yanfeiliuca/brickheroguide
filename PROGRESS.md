# BrickHeroGuide — Work Log

## 2026-05-26 — Daily automated update: blog + guide audit

### 阶段一：Blog 更新
- **`blog/steam-player-count-analysis.html`** — New analysis post: "33K Steam Peak: LEGO Batman Legacy Dethrones Arkham Knight — But Skywalker Saga Still Reigns Supreme". Covers the game's all-time Steam peak of 33,449 vs Batman: Arkham Knight (27,432) and LEGO Star Wars: Skywalker Saga (82,517). Sources: SteamCharts, Steambase, TheGamer. Image: gear-3 (Batman on Batcycle, previously unused).
- **`blog/index.html`** — New card added at top of blog-list; sidebar "Latest Posts" updated to show new article.

### 阶段二：内容审计结果
**审计页面数：** 21 个 guide 页面  
**SEO Top 3 更新：**
1. **`guides/mission-3-walkthrough.html`** (Open-World Gotham City Guide) — 移除预发行免责声明，将"expected to"措辞改为确认描述，将"Full walkthroughs coming soon"替换为正式关联指南链接。（评分：9/10）
2. **`guides/mission-2-walkthrough.html`** (Combat & Gameplay Guide) — 移除预发行免责声明，更新Boss encounter描述为发售后确认信息，将"coming soon"底部替换为关联指南链接。（评分：8/10）
3. **`guides/mission-4-walkthrough.html`** (Characters & Villains Guide) — 移除预发行免责声明，替换为发售后更新提示，"More Guides Coming Soon"替换为真实指南链接。（评分：8/10）
**新建页面：** 无

### Verification Checklist
- [x] Blog 新文章已写入
- [x] blog/index.html 已更新（新卡片在顶部，侧边栏已更新）
- [x] 内容审计已完成（21个页面扫描）
- [x] SEO Top 3 更新已执行（mission-2/3/4 walkthrough）
- [x] index.html 链接已更新（无新建页面，无需更新）
- [x] sitemap.xml 已重新生成（共 35 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

---

## Session: May 24, 2026 (Part 3 — 定时任务升级)

### Context
完成全部页面更新后，对每日定时任务进行了升级，将单纯的 Blog 更新扩展为全站内容审计 + SEO 优先修改的完整工作流，并加入自动 git push。

### Completed Work

#### 每日定时任务升级（brickheroguide-daily-blog）
- **任务描述更新：** 从"每日 Blog 更新"升级为"每日全站更新：Blog 新文章 + 内容审计 + SEO 优先修改 Top 3"
- **新增阶段二：现有页面内容审计**
  - 每次运行扫描所有 `guides/*.html` 页面
  - 对比网上最新信息，找出内容过时/数据有误/缺失关键板块的页面
  - 按 4 个维度打分：搜索意图强度（3分）、内容准确性差距（3分）、SEO 结构（2分）、内容完整性（2分）
  - 选出 Top 3 优先级最高的页面进行更新（最多修改3个现有页面，或新建最多3个页面）
- **新增步骤 13：自动 git commit + push**
  - 所有文件写入完成后自动执行 `git add -A` → `git commit` → `git push origin main`
  - 加入 `index.lock` 自动清理逻辑（检测到残留锁文件时先删除再继续）
  - 如 push 失败，在 Cowork 聊天中报告并提示手动运行 `auto-push.bat`

### Verification Checklist
- [x] 定时任务 prompt 已更新（含阶段二审计流程 + git push）
- [x] 任务描述已更新
- [x] PROGRESS.md 已追加

---

## Session: May 24, 2026 (Continuation — Context Compacted)

### Context
Continuing full site audit and rewrite with verified post-launch data. Previous session completed Tasks 1–12. This session picks up at Task 13 (new pages) and Task 14 (index + sitemap + push).

### Completed Work

#### Task 13 — 3 New Guide Pages Created
- **`guides/stud-farming-guide.html`** — NEW. Stud multiplier math (×2 → ×3,840 stack), 4 farming methods (Stud Cache Loop, Free Play replay, Batmobile Missile, Jim Gordon Splitter), priority order for new players.
- **`guides/difficulty-modes-guide.html`** — NEW. Full breakdown of Classic / Caped Crusader / Dark Knight modes with side-by-side comparison table, FAQ (trophy compatibility, changeability, Red Brick workaround).
- **`guides/mayhem-collection-dlc.html`** — NEW. Complete Mayhem Collection DLC guide: Joker + Harley Quinn character cards with abilities, Arkham Breakout story mission details, Mayhem Mode villain sandbox explanation, Sinister Pack suits table (7 suits + Batmobile skin + 5 Batcave props), who gets it free (Deluxe/Season Pass), and value verdict.

#### Task 14 — index.html + Sitemap + Git Push
- **`index.html`** — Added 3 new article rows to Game Information section: stud-farming-guide, difficulty-modes-guide, mayhem-collection-dlc.
- **`index.html`** — Updated review scores in News & Updates section from vague "100% recommend" to confirmed: "Metacritic 84, OpenCritic 85, Steam 97% Positive".
- **`sitemap.xml`** — Regenerated. Now includes 33 pages (up from 30). All new guides indexed.
- **Git** — Committed and pushed all changes to `main`.

### Verification Checklist
- [x] `mayhem-collection-dlc.html` created with GA tag, canonical URL, OG tags, sidebar links
- [x] `stud-farming-guide.html` — verified created in previous session
- [x] `difficulty-modes-guide.html` — verified created in previous session
- [x] All 3 new pages appear in sitemap.xml (33 total)
- [x] index.html article list updated with links to all 3 new pages
- [x] Review scores updated to confirmed post-launch figures
- [x] `PROGRESS.md` updated

---

## Session: May 24, 2026 (Part 1 — Pre-Compaction)

### Context
Full site audit and rewrite with verified post-launch data sourced from GameRant, GamesRadar, TwistedVoxel, TheGamer, VGC, and other post-launch publications.

### Completed Work

#### Tasks 7–10 — Full Rewrites
- `suits-abilities-guide.html` — Rewritten with 101 confirmed suits, 25 DLC suits, suit mechanics
- `collectibles-guide.html` — Rewritten with Minikit counts, Red Brick list, collectible types
- `trophy-guide.html` — Rewritten with confirmed trophy list and Platinum roadmap
- `100-percent-completion.html` — Rewritten with post-launch checklist

#### Task 11 — Character Guide Updated
- `all-characters-unlock.html` — Full rewrite with all 7 confirmed characters (Batman, Gordon, Catwoman, Robin, Batgirl, Nightwing, Talia al Ghul), unlock chapters, gadgets, and abilities

#### Task 12 — 3 Guide Updates
- `deluxe-edition-explained.html` — Full rewrite with DLC breakdown, Legacy Collection, Arkham Trilogy Pack, Batman Beyond Pack, Mayhem Collection info
- `pc-requirements.html` — Full rewrite with confirmed specs (3 tiers), upscaling table (DLSS 3/FSR 3/XeSS), SSD mandatory note, Steam Deck compatibility
- `beginners-guide.html` — Full rewrite with 3 difficulty mode cards, Detective Mode, Red Bricks, 15 tip cards, stud multiplier math

---

## 2026-05-25 — Daily Automated Update: Blog + Guide Audit

### 阶段一：Blog 更新
- **`blog/mayhem-collection-dlc-leak.html`** — New blog post: "Mayhem Collection DLC Leak: 13 Suicide Squad Characters Datamined for LEGO Batman Legacy." Covers datamined Task Force X character list (Deadshot, King Shark, Captain Boomerang, Deathstroke, Killer Croc, Katana + 7 more), confirmed Joker/Harley Mayhem Mode details, leaked Mayhem Hideout hub, separate currency system, and Bud & Lou hyenas. Sources: Game Rant, Brick Fanatics, GamingBolt, ExpansiveDLC. Image: `og-image.BcIYb3Fq.jpg` (official key art).
- **`blog/index.html`** — New post card inserted at top of `.blog-list`; Latest Posts sidebar updated (new post added, oldest removed, 3 kept).

### 阶段二：内容审计结果
**审计页面数：** 21 guide pages
**SEO Top 3 更新：**
1. **`all-characters-unlock.html`** — DLC section updated: replaced vague pre-release Joker/Harley speculation with confirmed TT Games DLC description + datamine rumor section with link to blog post (Score: 9/10)
2. **`mayhem-collection-dlc.html`** — Added new "Rumored Content (Datamine)" section with full leaked character list and gameplay details (clearly labeled as unconfirmed); updated TBA language and TOC (Score: 8/10)
3. **`mission-1-walkthrough.html`** — Updated TOC "Coming Soon" link to "More Guides"; updated Matt Berry "expected to create" tip box to post-launch confirmed language; updated "walkthroughs will be added" section (Score: 7/10)

### Verification Checklist
- [x] Blog 新文章已写入 (`blog/mayhem-collection-dlc-leak.html`)
- [x] `blog/index.html` 已更新（卡片+侧边栏）
- [x] 内容审计已完成（21个guide页面）
- [x] SEO Top 3 更新已执行
- [x] `index.html` 无需更新（未新建guide页面）
- [x] `sitemap.xml` 已重新生成（34页）
- [x] `PROGRESS.md` 已追加
- [x] Git commit + push 已完成
