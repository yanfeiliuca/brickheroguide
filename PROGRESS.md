# BrickHeroGuide — Work Log

## 2026-06-22 — One Month Anniversary Blog + 3 Guide SEO Fixes

### 阶段一：Blog 更新
- **`blog/lego-batman-legacy-one-month-report.html`** — "One Month In: How LEGO Batman: Legacy of the Dark Knight Has Held Up". 700+ words. Covers: critical reception (IGN 8/10, GamesRadar 4/5, Steam Overwhelmingly Positive with 11,600+ reviews), Update 1.006 stability patch (June 2), free HBO Max/WB Games account bonus suits (Dark Knights of Steel + Black Lantern + Golden Age), Twitch Drops recap, Mayhem Collection DLC Sept 18 preview. Tags: Analysis + News. Image: `legobatmangame.com/_astro/fight-2.BFd6neBb_2adSpB.webp` (Red Hood gang vs Batman — lowest reuse count, 1 prior use). Sources: Screen Rant, Game Rant, SteamDB, LEGO.com, WB Games rewards page. 7 min read.

### 阶段二：内容审计结果
**审计页面数：** 31 guide 页面
**关键发现：**
- `collectibles-guide.html` quick stats had critical error: WayneTech Caches displayed as "10" (should be 200); TOC label also wrong. Fixed.
- `suits-abilities-guide.html` missing free account-linked bonus suits section (3 suits: Golden Age/WB Games, Dark Knights of Steel + Black Lantern/HBO Max). Added.
- `deluxe-edition-explained.html` missing note about free account-linked bonus suits for all edition owners. Added highlight box.

**SEO Top 3 更新：**
1. **`guides/collectibles-guide.html`** — Fixed critical stat error: WayneTech Caches quick-stat 10→200; fixed TOC label "10 Total"→"200 Total"; updated total collectibles from "99+" to "247+". High accuracy impact for completionist queries. (评分：9/10)
2. **`guides/suits-abilities-guide.html`** — Added "Free Bonus Suits via Account Linking" section with WB Games (Golden Age Batsuit) and HBO Max (Dark Knights of Steel + Black Lantern Batsuits) instructions. Updated last-modified date to June 22, 2026. High value for suit-unlock searches. (评分：7/10)
3. **`guides/deluxe-edition-explained.html`** — Added highlight box about 3 free account-linked suits (Golden Age, Dark Knights of Steel, Black Lantern) available to all edition owners. Relevant to edition comparison queries. (评分：6/10)

**新建页面（如有）：** 无新建 guide 页面

### Verification Checklist
- [x] Blog 新文章已写入 (`lego-batman-legacy-one-month-report.html`)
- [x] blog/index.html 已更新（顶部新卡片 + Latest Posts 侧边栏）
- [x] 内容审计已完成（31 个 guide 页面扫描）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（如有新建）— 无新建 guide，无需更新
- [x] sitemap.xml 已重新生成（73 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-20 — Character Rankings Blog + Broken Link Fix + 3 Guide Cross-Links

### 阶段一：Blog 更新
- **`blog/best-character-ranking-lego-batman-legacy.html`** — "All 7 LEGO Batman: Legacy of the Dark Knight Characters, Ranked — Tier List & Abilities Guide". 700+ words. Full S–C tier table, per-character breakdown cards (abilities, unique strengths, Free Play utility), consensus ranking from Dexerto and COGconnected (June 7, 2026), Free Play team composition guide for 100% completion. Tags: Analysis + Guide. Image: `legobatmangame.com/_astro/family.CQW_jlFK_2qvCfg.webp` (cycled back — oldest prior use was all-characters-unlock-guide.html, May 27). Sources: Dexerto tier list, COGconnected Michael Chow ranking, GamesRadar skills guide. 6 min read.

### 阶段二：内容审计结果
**审计页面数：** 31 guide 页面
**关键发现：** Broken internal links — 6 blog pages (batman-legacy-tributes-deep-dive.html, best-character-ranking-lego-batman-legacy.html, index.html, lego-batman-legacy-rdr2-graphics-comparison.html, secret-bonus-characters-alfred-lucius-bruce-wayne.html, switch-2-exclusive-batman-minifigure.html) referenced `/guides/trophy-achievement-guide.html` which does not exist (actual file: `/guides/trophy-guide.html`). Fixed all 6 via sed.

**SEO Top 3 更新：**
1. **`guides/best-characters-each-mission.html`** — Added tier-list callout box linking to new character ranking blog post; added blog post to Related Guides list and sidebar. Strengthens internal linking for character-search queries. (评分：8/10)
2. **`guides/jim-gordon-guide.html`** — Added community-reception info-box noting Jim Gordon's surprising #1 ranking by COGconnected despite C-tier objective placement, with source links and cross-link to character ranking post. Adds unique insight that no other guide covers. (评分：7/10)
3. **`guides/waynetech-upgrades-guide.html`** — Added character ranking blog post link to sidebar Related Guides. Helps users who land on upgrades guide find the tier-list context for which character to upgrade first. (评分：6/10)
**修复：** 6 broken `/guides/trophy-achievement-guide.html` links → `/guides/trophy-guide.html`
**新建页面（如有）：** 无新建 guide 页面

### Verification Checklist
- [x] Blog 新文章已写入 (`best-character-ranking-lego-batman-legacy.html`)
- [x] blog/index.html 已更新（顶部新卡片 + Latest Posts 侧边栏）
- [x] 内容审计已完成（31 个 guide 页面扫描）
- [x] 6 个破链已修复（trophy-achievement-guide → trophy-guide）
- [x] SEO Top 3 更新已执行
- [x] sitemap.xml 已重新生成（70 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-19 — Community Interactive Maps Blog + 3 Guide SEO Updates

### 阶段一：Blog 更新
- **`blog/community-interactive-maps-guide.html`** — "The Best Interactive Maps for LEGO Batman: Legacy of the Dark Knight — Every Collectible, Every Secret". 600+ words. Covers 4 community maps (GameRant, Steam community guide, Shacknews, Gamemappers), collectible types table (Riddler Puzzles 121 total, WayneTech Caches 160+40, Batcave Trophies, Red Bricks, Costumes), 4-island Gotham structure, tips for efficient map use. Tags: Community + Tips. Image: `legobatmangame.com/_astro/prefooter-keyart.C5w2I9s1_1Iktj5.jpg` (new URL not previously in library). 6 min read.

### 阶段二：内容审计结果
**审计页面数：** 31 guide 页面
**SEO Top 3 更新：**
1. **`guides/release-date-platforms.html`** — Fixed stale Nintendo Switch 2 performance table row. Replaced "~720p–1080p (estimated) / ~1080p (estimated)" with "720p handheld / up to 1080p docked" based on trailer footage analysis; replaced "performance analysis will be added after launch" placeholder with note that TT Games has not published official specs and full analysis will follow the September 18, 2026 launch. (评分：7/10)
2. **`guides/gotham-districts-guide.html`** — Added missing `<h2 id="landmarks">Key Landmarks per District</h2>` section that was referenced in the TOC anchor (`#landmarks`) but did not exist in the page body. Added 9 district landmark cards covering key named locations, Batcave challenge tie-ins, character requirements, and collectible context for each district. Fixed broken TOC anchor. (评分：8/10)
3. **`guides/collectibles-guide.html`** — Expanded "Optimal Collection Route" section per CLAUDE.md ongoing priority. Restructured flat 6-step list into 5 named phases (Story First / Batcave Sweep / WayneTech Upgrades + Multipliers / Open World by Island / Store Red Bricks). Added island-by-island sequence that minimises backtracking, "why this phase first" rationale for each step, bonus finds flagged per island, and upgraded stud multiplier value note. (评分：8/10)
**新建页面（如有）：** 无

### Verification Checklist
- [x] Blog 新文章已写入 (`community-interactive-maps-guide.html`)
- [x] blog/index.html 已更新（顶部新卡片 + Latest Posts 侧边栏）
- [x] 内容审计已完成（31 个 guide 页面）
- [x] SEO Top 3 更新已执行
- [x] sitemap.xml 已重新生成（69 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-13 — Secret Characters Blog + Trophy/Character Guide Updates

### 阶段一：Blog 更新
- **`blog/secret-bonus-characters-alfred-lucius-bruce-wayne.html`** — New blog post: "3 Secret Playable Characters You Probably Missed: Alfred, Lucius Fox & Bruce Wayne." Covers the community-discovered D-pad trick to unlock 3 bonus characters beyond the advertised roster of 7. Step-by-step instructions for each (Alfred from The Mimes "Home Sweet Home"; Lucius Fox and Bruce Wayne from Wayne Industries "WayneTech R&D"). Also covers Keyboard Cat, Gentleman Ghost, Batcave customization surprises. 700+ words. Image: origin.DSZma2rC_2hKTV2.webp (cycled back from launch-preview post). Source: Brick Fanatics June 10, 2026.

### 阶段二：内容审计结果
**审计页面数：** 12 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/all-characters-unlock.html`** — Added new "Secret Bonus Characters" section between DLC and Tips headings. Covers Alfred, Lucius Fox, and Bruce Wayne with mission-section details, D-pad unlock method, and per-character ability notes. Links to new blog post. (Score: 9/10)
2. **`guides/trophy-guide.html`** — Fixed vague "reportedly requires a very large Stud total" language with confirmed specifics: trophy name "Life's been good to me", exact threshold of 1,000,000 Studs, sources linked (Game Rant, Happy Thumbs Gaming). Also renamed the Gold trophy h3 to include trophy name and target. (Score: 7/10)
3. **`guides/tips-for-new-players.html`** — Added Lucius Fox WayneTech terminal tip to Batcave Tips section. Added all-characters-unlock and new blog post to Related Guides list. (Score: 6/10)
**New pages:** None

### Verification Checklist
- [x] Blog 新文章已写入 (secret-bonus-characters-alfred-lucius-bruce-wayne.html, 700+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Latest Posts 更新）
- [x] 内容审计已完成（12 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（N/A — no new guide pages created）
- [x] sitemap.xml 已重新生成（62 pages total）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

---

## 2026-06-06 — Speedrun Community Blog + Chapter 1 Walkthrough + Mission-1 Fixes

### 阶段一：Blog 更新
- **`blog/speedrun-leaderboards-opening.html`** — New blog post: "LEGO Batman: Legacy of the Dark Knight Speedrun Leaderboards Open June 7 — What the Community Has Built." Covers the Speedrun.com embargo ending on June 7, 68 followers, 6 moderators, 18 individual level boards, community Discord and Twitch. Discusses expected categories (Any%, 100%, IL), routing considerations (character abilities, stud multipliers, open-world hub), and the broader LEGO speedrunning context. 700+ words. Image: origin.DSZma2rC.webp (cycling back). Sources: speedrun.com/LotDK, community Discord.

### 阶段二：内容审计结果
**审计页面数：** 22 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/mission-1-walkthrough.html`** — Fixed outdated "TBA" Switch 2 date → "September 18, 2026." Removed pre-launch "confirmed so far" language from story section. Updated "More Guides Coming" to "Full Guide Library" with active link to new Chapter 1 walkthrough. Fixed wrong link text for mission-4-walkthrough (was "Characters & Villains Guide", now correct). (Score: 8/10)
2. **`guides/chapter-1-red-hood-gang-walkthrough.html`** — NEW PAGE. Full Chapter 1 walkthrough covering The Red Hood Gang mission: step-by-step combat/puzzle guide, all 5 Ace Card locations (table), all 5 WayneTech Cache locations (table), Red Brick location (Free Play/Catwoman required), boss section (Red Hood One betrayal + Falcone armored vehicle), quick-stats header, TOC, sidebars. Captures high-intent "LEGO Batman Legacy chapter 1 walkthrough" searches currently returning no on-site content. (Score: 9/10)
3. **`index.html`** — Added Chapter 1 walkthrough link to the Walkthrough section above the existing Story & Premise row.

### Verification Checklist
- [x] Blog 新文章已写入 (speedrun-leaderboards-opening.html, 700+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Featured Posts 更新）
- [x] 内容审计已完成（22 guide pages scanned）
- [x] SEO Top 3 更新已执行（mission-1 fixes + new Chapter 1 walkthrough）
- [x] index.html 链接已更新（Chapter 1 walkthrough card added）
- [x] sitemap.xml 已重新生成（48页，含2新页面）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成 (b71b49e)

## 2026-06-09 — RDR2 Comparison Blog + DLC / Release Guides Audit

### 阶段一：Blog 更新
- **`blog/lego-batman-legacy-rdr2-graphics-comparison.html`** — New blog post: "Why Fans Can't Stop Comparing LEGO Batman: Legacy to Red Dead Redemption 2." Covers the viral community trend (Screen Rant, May 25, 2026) of fans comparing Gotham's UE5 rain/snow/lighting effects to RDR2; the LEGO Group's X account acknowledgment; the "Arkham-ification" of LEGO's visual style; and why the comparison isn't entirely fair but still meaningful. 600+ words. Image: origin.DSZma2rC.webp (cycled back from lego-batman-legacy-launch-preview.html). Sources: Screen Rant, OpenCritic.

### 阶段二：内容审计结果
**审计页面数：** 30 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/mayhem-collection-dlc.html`** — Updated "Rumored Content" section: renamed to "Unconfirmed Extras — Datamine Findings"; updated callout to clearly state that core DLC contents (Joker/Harley, Arkham Breakout, Mayhem Mode, Sinister Pack) are ALL officially confirmed per WB June 3 press release, and this section covers only additional unconfirmed datamined elements. (Score: 9/10)
2. **`guides/all-characters-unlock.html`** — Updated Sinister Pack description to include officially confirmed specifics: 7 villain-themed suits (one per original character), 5 Batcave decorative items, 1 Batmobile skin — per WB Games June 3, 2026 press release. (Score: 6/10)
3. **`guides/release-date-platforms.html`** — Fixed Switch 2 performance table row: replaced "technical analysis pending" with accurate "performance analysis will be added after launch" note tied to the confirmed September 18 date. (Score: 5/10)
**新建页面：** None

### Verification Checklist
- [x] Blog 新文章已写入 (lego-batman-legacy-rdr2-graphics-comparison.html, 600+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏更新）
- [x] 内容审计已完成（30 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新建页面）
- [x] sitemap.xml 已重新生成（58页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

---

## 2026-06-04 — Nintendo Switch 2 Date Announcement + Guide Accuracy Updates

### 阶段一：Blog 更新
- **`blog/switch-2-release-date-september-2026.html`** — New blog post: "LEGO Batman: Legacy of the Dark Knight Confirmed for Nintendo Switch 2 on September 18." Covers the June 3, 2026 Warner Bros. Games official press release confirming the Switch 2 launch date, simultaneous Mayhem Collection DLC release on all platforms, Switch 2 Deluxe Edition content breakdown, pre-order bonus (*The Dark Knight Returns* Batsuit), account-linked free Batsuits, and LEGO set tie-ins. 700+ words. Image: Steam Heroes & Villains Trailer promo image (first use). Sources: WB Games Press Room, Nintendo Everything, Nintendo.com eShop.

### 阶段二：内容审计结果
**审计页面数：** 22 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/release-date-platforms.html`** — Fixed critical "TBA" entries: Switch 2 date now shows confirmed September 18, 2026 in the platforms table, platform differences table, post-launch bullet, and development history. Added pre-order pricing and pre-order bonus detail. (Score: 9/10)
2. **`guides/mayhem-collection-dlc.html`** — Updated release window from "September 2026 (exact date TBA)" to confirmed September 18, 2026. Updated overview paragraph to note simultaneous Switch 2 launch. Added confirmed $24.99 Deluxe Edition upgrade price. Updated sidebar summary. (Score: 8/10)
3. **`guides/deluxe-edition-explained.html`** — Updated all "September 2026" references to "September 18, 2026" (5 occurrences including TOC, section header, badge, and prose). Added $24.99 upgrade price confirmation and Switch 2 context to the Mayhem Collection note. (Score: 7/10)
**新建页面：** none (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (switch-2-release-date-september-2026.html, 700+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Featured Posts 更新）
- [x] 内容审计已完成（22 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新建guide，不需要）
- [x] sitemap.xml 已重新生成（45页，含新blog post）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成 (828716a)
- [x] Follow-up: 8 pages structural fixes — completed missing footers, sidebars, and hamburger JS (f4066c3)

---

## 2026-06-03 — Daily Blog Update + Guide SEO Audit

### 阶段一：Blog 更新
- **`blog/update-1-006-patch-notes-june-2026.html`** — New blog post: "LEGO Batman Legacy Update 1.006: What TT Games Fixed (and What's Still on the List)." Covers patch 1.006 released June 2, 2026 — stuttering fix, crash fixes, performance improvements — plus known outstanding bugs (co-op crash, Riddler unlock save issue, chest tracker). 750+ words. Image: origin.webp (cycling back to launch-preview's image). Sources: UpdateCrazy (June 2, 2026), SteamDB, KeenGamer.

### 阶段二：内容审计结果
**审计页面数：** 22 guide pages scanned
**SEO Top 3 更新：**
1. **`blog/post-launch-patch-tracker.html`** — Added Update 1.006 patch card (June 2, 2026) with full notes and styled highlight. Added 4 new rows to bug status table (stuttering ✅ fixed, loading crashes ✅ fixed, co-op crash ❌ pending, Riddler saves ❌ pending). Updated meta description and keywords to include 1.006. (Score: 9/10)
2. **`guides/all-characters-unlock.html`** — Updated DLC pricing note: replaced "not yet announced" with accurate info about Deluxe Edition upgrade availability on Steam and console stores. More actionable for Standard Edition players. (Score: 7.5/10)
3. **`guides/mayhem-collection-dlc.html`** — Fixed two speculative statements: trophy/achievement callout now cites confirmed base game platinum count (52 PS5 / 51 Xbox) and properly hedges the DLC trophy list as unconfirmed. Updated 100% completion paragraph to correctly state no DLC required for base platinum. (Score: 7/10)
**新建页面：** none (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (update-1-006-patch-notes-june-2026.html, 750+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Featured Posts 更新）
- [x] 内容审计已完成（22 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新建guide，不需要）
- [x] sitemap.xml 已重新生成（44页，含新blog post）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

---

## 2026-06-02 — Daily Blog Update + Guide SEO Audit

### 阶段一：Blog 更新
- **`blog/jonathan-smith-post-launch-interview.html`** — New blog post: "Jonathan Smith on Making LEGO Batman Feel New Again — Post-Launch Reflections." Covers the June 1, 2026 Dark Knight News / Deadline interview with TT Games head of development, focusing on representing all Batman history (incl. Batman & Robin), reinvented combat mechanics, and Gotham world design. 600+ words, sourced from verified interviews. Image: cover art (cycling back from oldest post — lego-batman-series-visual-evolution.html, May 19). Sources: Dark Knight News (June 1, 2026), Deadline.

### 阶段二：内容审计结果
**审计页面数：** 22 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/pc-requirements.html`** — Fixed critical factual error: page said "not yet Steam Deck Verified as of May 29, 2026" but the game received official Steam Deck Verified status on May 12, 2026 (before launch). Updated both the main Steam Deck section and the FAQ entry. Added accurate performance data (30–60fps depending on area, 720p + FSR3 Performance mode) and links to Steam announcement and Steam Deck HQ. Updated date to June 2. (Score: 9/10)
2. **`guides/release-date-platforms.html`** — Updated "as of May 29" language to June 2, 2026. Added Nintendo.com Switch 2 store listing link. Added verified post-launch data: 84 Metacritic, 33K Steam peak, patch 1.005, Steam Deck Verified status. (Score: 8/10)
3. **`guides/batcave-hub-guide.html`** — Updated date from May 19 to June 2 (oldest guide). Added DLC suit count for Deluxe Edition owners (122 total: 101 base + 21 Legacy Collection). Added cross-link to Suits & Abilities Guide in Wardrobe section. (Score: 6/10)
**新建页面：** none (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (jonathan-smith-post-launch-interview.html, 600+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Featured Posts 更新）
- [x] 内容审计已完成（22 guide pages）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新建guide，不需要）
- [x] sitemap.xml 已重新生成（43页，含新blog post）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

---

## 2026-05-30 — Daily Blog Update + Guide SEO Audit

### 阶段一：Blog 更新
- **`blog/best-pc-mods-lego-batman-legacy.html`** — New blog post covering the PC modding scene: 50+ mods on Nexus Mods within one week of launch. Covers UE scripting framework, TheDCfanXO Rebirth/New 52 skin pack, Auto-Collect Studs mod, Gotham Optimization Project, PLITCH trainer tool, and future mod outlook. 500+ words, uses `postfooter.Bp36eHDB_Z2cb3ek.webp` image (cycling back). Sources: Nexus Mods, PLITCH, xmodhub.

### 阶段二：内容审计结果
**审计页面数：** 10 guide pages checked
**SEO Top 3 更新：**
1. **`guides/mission-3-walkthrough.html`** — Fixed binary file corruption (32 trailing null bytes stripped). Page is now readable by all tools. (SEO score: 8/10)
2. **`guides/suits-abilities-guide.html`** — Added "Extra Suits via PC Mods" section cross-linking to new blog post. Captures PC modding search intent. (SEO score: 8/10)
3. **`guides/all-villains-guide.html`** — Replaced internal "Search Console insight" tip box with player-friendly DLC navigation tip. Updated meta description to remove pre-release "confirmed" language. (SEO score: 7/10)
**新建页面：** none (blog post only)

### 阶段三：Canonical URL 全站修复（Search Console 问题）

**触发原因：** Google Search Console 显示4个页面被标为 "Alternate page with proper canonical tag"，未被索引：
- `https://brickheroguide.com/guides/is-it-good-for-kids`
- `https://brickheroguide.com/guides/mission-4-walkthrough`
- `https://brickheroguide.com/guides/tips-for-new-players`
- `http://brickheroguide.com/`（HTTP版本）

**根本原因：** Cloudflare Pages 同时响应带和不带 `.html` 后缀的URL，Google爬到了无后缀版本，但canonical标签指向 `.html` 版本，导致重复页面问题。

**修复内容：**
1. **新建 `_redirects` 文件** — 所有带 `.html` 的URL 301重定向至干净URL（覆盖全部22个guide页面 + 13个blog页面 + 3个静态页面）
2. **批量更新canonical标签** — 全站35个页面的 `rel="canonical"` 和 `og:url` 全部改为无 `.html` 后缀的干净URL
3. **更新 sitemap.xml** — 所有40个URL同步改为干净URL

**预期效果：** 1-2周后 Search Console 中4个 "Alternate page" 问题消失，这些页面转为正常索引。可点击 "Validate Fix" 告知Google重新检查。

### Verification Checklist
- [x] Blog 新文章已写入 (best-pc-mods-lego-batman-legacy.html)
- [x] blog/index.html 已更新（新卡片 + 侧边栏Latest Posts）
- [x] 内容审计已完成（10 guide pages）
- [x] SEO Top 3 更新已执行
- [x] _redirects 文件已创建（全站.html → 干净URL）
- [x] 全站35页 canonical 标签已更新（去除.html后缀）
- [x] sitemap.xml 已更新为干净URL（40页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成（两次推送：每日更新 + canonical修复）

### 补充：Git锁文件彻底修复流程（2026-05-30下午）

沙盒的git锁文件长期积累导致GitHub Desktop也无法commit，最终在Windows PowerShell（管理员）用两步彻底解决：

```powershell
# 步骤1：删除所有锁文件
cd "C:\Users\yanfe\OneDrive\Desktop\brickheroguide"
Get-ChildItem .git -Recurse -Filter "*.lock*" | Remove-Item -Force

# 步骤2：修复损坏的分支引用（写入最新commit SHA）
"7c8f54edb1e7d424b3a46fc421bb3d7d79af8f6b" | Out-File -FilePath ".git\refs\heads\main" -Encoding ascii -NoNewline
```

执行后GitHub Desktop恢复正常（分支从"unknown"→"main"，0 changed files）。**结论：以后遇到git锁文件报错，直接用PowerShell管理员模式处理，比沙盒操作可靠。**

---

## 2026-05-29 — Daily Blog Update + Guide SEO Audit

### 阶段一：Blog 更新
- **`blog/ps-share-of-the-week-community-screenshots.html`** — New blog post covering PlayStation's Share of the Week spotlight on LEGO Batman Legacy community screenshots (published May 29, 2026). Features 6 community screenshots from PS Blog post, 500+ words, uses Steam Heroes & Villains promo image. Source: blog.playstation.com.

### 阶段二：内容审计结果
**审计页面数：** 7 guide pages checked
**SEO Top 3 更新：**
1. **`guides/mission-4-walkthrough.html`** — Major fix: page had mismatched content ("Characters & Villains Guide") vs URL. Rewrote as proper Chapter 4 Walkthrough covering Firefly, Batgirl Begins, Out of Commission, and Mr. Freeze missions. Added verified Snow Globe and Red Brick locations from Push Square. Added og:image tag. (SEO score: 9/10)
2. **`guides/release-date-platforms.html`** — Fixed stale pre-launch language: updated "Pre-ordering grants early access" to past tense, updated Deluxe Edition note to reflect current availability post-launch. (SEO score: 7/10)
3. **`guides/best-characters-each-mission.html`** — Added missing og:title, og:description, og:image, og:type, and robots meta tags. (SEO score: 6/10)
**新建页面：** none (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (ps-share-of-the-week-community-screenshots.html)
- [x] blog/index.html 已更新（新卡片 + 侧边栏Latest Posts）
- [x] 内容审计已完成（7 guide pages）
- [x] SEO Top 3 更新已执行
- [x] sitemap.xml 已手动添加新博客页面（bash unavailable, manual edit）
- [x] PROGRESS.md 已追加
- [x] Git commit + push (completed manually by user via PowerShell)

### 内容策略决策记录（2026-05-29）
- **决策**：不为 LEGO Batman 新建"垂直稀有物品合成攻略"栏目（该构想保留用于下一个游戏项目网站）
- **原因**：LEGO Batman 无物品合成机制，构想不适配当前游戏
- **替代方案**：将该构想的"最优路线 + 隐藏宝物"思路应用于升级现有页面：
  - `guides/collectibles-guide.html` → 改版为"最优收集路线"格式
  - `guides/100-percent-completion.html` → 增加"最高效完成顺序"版块
- **执行方式**：在每次日常 guide 审计时逐步升级，已写入 CLAUDE.md

---

## 2026-05-27 — 收工文档更新：进度记录 + 建站指南

### 文档更新（良辰美AI网站目录）

- **`开发进度记录.md`** — 全面补录5月19-27日工作进程：
  - 文档头部更新（最后更新日期、总览表状态）
  - 2.4节：内容清单更新（22篇攻略 + 10篇博客 + 37页sitemap）
  - 2.5节：AdSense状态从"待申请"更新为"已激活"
  - 2.8节：待完成事项按最新状态重整
  - 2.9节：成功指标填入真实数据（45 clicks / 1.48K impressions / 138用户 / 排名8.9）
  - 新增2.10节：完整记录5月19-27日内容扩张与变现激活全过程

- **`游戏攻略网站建站维护流量指南.md`** — 新建，基于BrickHeroGuide完整实战经验整理的可复用蓝本：
  - 12个章节，覆盖选题→建站→内容生产→SEO→AdSense→自动化运营→数据复盘
  - 包含：完整Claude Prompt模板、Sitemap自动化代码、CLAUDE.md模板、Day 0-21快速启动清单
  - 用途：下一个游戏攻略站直接参照此文档复制流程

### 其他讨论
- 确认当前网站无留言/评论功能（contact.html 仅显示邮件地址）
- 决策：保持现状，静态攻略站不需要评论区

### Verification Checklist
- [x] 开发进度记录.md 已更新（5月27日收工版）
- [x] 游戏攻略网站建站维护流量指南.md 已创建
- [x] PROGRESS.md 已追加

---

## 2026-05-27 — 反派大全页面上线 + SEO流量分析与优化

### 新建页面：All Villains Guide
- **`guides/all-villains-guide.html`** — "All Villains in LEGO Batman: Legacy of the Dark Knight — Complete Rogues Gallery Guide"
  - 触发原因：Google Search Console 数据显示 `"lego batman legacy of the dark knight all villains"` 是当前最热搜索词之一，但网站无对应专页
  - 内容：全部 14 个确认反派（Joker、Bane、Mr. Freeze、Two-Face、Poison Ivy、Riddler、Penguin、Firefly、Catwoman、Talia、Ra's al Ghul、Harley Quinn、Egghead、Condiment King）
  - 结构：快速参考表格 + 每个反派单独卡片 + League of Shadows 派系专节 + Boss 战技巧 + DLC 说明
  - 广告：3 个 AdSense 广告位（文中 ×2 + 侧边栏 ×1）
  - 图片：`fight-3.KeK453wH_Z23bgKb.webp`（Mr. Freeze 在冰冻卡车，首次使用）
  - 来源：AllThings.How、GameRant、官方 legobatmangame.com
- **`index.html`** — 首页新增两处反派大全入口（顶部 Game Guides 卡片区 + 文章列表区）
- **`sitemap.xml`** — 重新生成，共 37 页
- **GitHub** — 成功推送至 main（commits: `aeecc5d` + `700f9c7`）
  - 注：因 git 锁文件冲突，使用临时克隆方式完成推送（已知 Cloudflare Pages 后台进程导致的锁文件问题）

### SEO 状态分析（基于 Google Search Console + Analytics 截图）
- **Search Console（28天）：** 45 clicks / 1,480 impressions / 平均排名 8.9 / CTR 3.1%
- **Analytics（28天）：** 138 活跃用户 / 47 来自 Google 自然搜索（占 34%）
- **Top 页面：** 首页 177次浏览 / Blog 39次 / Batcave Guide 24次 / 角色解锁指南 16次
- **关键发现：** 平均排名 8.9 — 距前 5 只差 3-4 位，点击量可翻倍
- **行动方向：** 填补搜索词缺口（all villains）、优化首页引导（跳出率 62.7% 偏高）

### Verification Checklist
- [x] guides/all-villains-guide.html 已创建（14 反派完整覆盖）
- [x] index.html 首页已添加反派大全入口（卡片 + 文章列表两处）
- [x] AdSense 广告位已嵌入（3处）
- [x] sitemap.xml 已重新生成（共 37 页）
- [x] Git commit + push 已完成（临时克隆方式绕过锁文件）
- [x] PROGRESS.md 已追加

---

## 2026-05-27 — Daily automated update: blog + guide audit

### 阶段一：Blog 更新
- **`blog/all-characters-unlock-guide.html`** — New guide/analysis post: "All 7 Playable Characters in LEGO Batman: Legacy of the Dark Knight — How to Unlock Each One". Covers the full roster (Batman, Jim Gordon, Catwoman, Robin, Batgirl, Nightwing, Talia al Ghul), unlock order by chapter, gadget loadouts, and the September 2026 DLC additions. Source: GameRant. Image: `family.CQW_jlFK_2qvCfg.webp` (Gordon and Catwoman smiling — previously unused).
- **`blog/index.html`** — New card added at top of blog-list; sidebar "Latest Posts" updated (new article top, oldest dropped).

### 阶段二：内容审计结果
**审计页面数：** 21 个 guide 页面  
**SEO Top 3 更新：**
1. **`guides/mission-1-walkthrough.html`** (Story & Premise Overview) — 更新预发行 tip box 为发售后内容，intro 段落移除"ahead of launch"措辞改为发售后描述。（评分：8/10）
2. **`guides/mission-2-walkthrough.html`** (Combat & Gameplay Guide) — 修复 TOC 中"Full Walkthroughs Coming Soon"→正确锚点"More Combat Resources"，更新 intro 段落移除"developer previews and early access"措辞。（评分：7/10）
3. **`guides/mission-4-walkthrough.html`** (Characters & Villains Guide) — 修复 TOC 中"Full Walkthroughs Coming Soon"→正确锚点"More Character Resources"，更新 intro 段落移除"developer announcements, previews, and early access"措辞。（评分：7/10）
**新建页面：** 无

### Verification Checklist
- [x] Blog 新文章已写入
- [x] blog/index.html 已更新（新卡片在顶部，侧边栏已更新）
- [x] 内容审计已完成（21个页面扫描）
- [x] SEO Top 3 更新已执行（mission-1/2/4 walkthrough）
- [x] index.html 链接已更新（无新建页面，无需更新）
- [x] sitemap.xml 已重新生成（共 36 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

---

## 2026-05-26 — GitHub 仓库清理

### 安全审查 + 文件清理
- **安全扫描：** 全仓库搜索 PAT、API Key、硬编码 token → 全部干净，零命中
- **发现问题：** `scripts/daily-blog.py` 引用了 `ANTHROPIC_API_KEY`（通过环境变量读取，非硬编码，安全）
- **清理内容：**
  - `scripts/daily-blog.py` — 删除（早期未使用的旧草稿，非当前工作流）
  - `-w` — 删除（意外创建的 Metacritic 抓取 HTML 垃圾文件）
  - `.claude/settings.local.json` — 从 git 移除（Claude Code 本地权限配置，不应公开）
  - `CLAUDE.md` — 从 git 移除，保留本地（AI 工作指令，不属于网站内容）
  - `PROGRESS.md` — 从 git 移除，保留本地（工作日志，不属于网站内容）
- **`.gitignore` 更新：** 新增 `CLAUDE.md`、`PROGRESS.md`、`.claude/`、`scripts/`、`-w` 防止再次误提交
- **Git commits：** `a6c918e`（删 daily-blog.py）、`904ca46`（清理其余文件）
- **恢复方式：** 所有删除文件均可通过 `git show <commit>:<path>` 从历史记录找回

### 修复 git index 损坏
- 上一 session 遗留问题：`git update-index --cacheinfo` 导致 index 文件损坏
- 修复方法：`git read-tree HEAD` 重建索引，恢复正常状态

### Verification Checklist
- [x] 安全扫描通过（无硬编码 token）
- [x] 所有非网站文件已从 GitHub 移除
- [x] `.gitignore` 已更新，防止再次误提交
- [x] CLAUDE.md 和 PROGRESS.md 保留在本地
- [x] git index 已修复并正常工作
- [x] 推送至 GitHub main（commit `904ca46`）

---

## 2026-05-26 — AdSense integration (manual session) + CLAUDE.md / PROGRESS.md updates

### AdSense 全站集成
- **Publisher ID：** `ca-pub-1971262808837870`
- **覆盖范围：** 全站 35 个 HTML 页面（guides/ × 21、blog/ × 9、根目录 × 5）
- **做了什么：**
  - 每个页面 `<head>` 里 GA 脚本之后插入 AdSense 脚本标签（Auto Ads 驱动）
  - 所有 `<div class="ad-inline">Advertisement</div>` 占位符 → 替换为标准 `<ins class="adsbygoogle">` 响应式广告单元
  - 所有侧边栏虚线 "Ad Space" 占位框 → 替换为标准 `<ins>` 广告单元
  - `index.html` 的 `.ad-slot` 占位块 → 替换为标准 `<ins>` 广告单元
  - 已推送至 GitHub（commit: `9a6956c`）
- **AdSense 后台状态：** 审核进行中（"Getting ready to show ads"）。审核通过后在 AdSense → 广告 → 按网站 → 开启 Auto Ads 即可。
- **注意：** 新建页面以现有模板为基础，天然包含 AdSense 代码，无需额外操作。

### 文档更新
- **`CLAUDE.md`** — 更新以下内容：
  - "Shared boilerplate" 章节新增 AdSense 脚本为必填项（第2条）
  - 新增 "Ad unit placement" 章节，说明 inline 和 sidebar 广告单元的标准 HTML 结构
  - Image Library 表格更新：clues-2 → redeem-codes、og-image → mayhem-dlc、gear-3 → steam-player-count；family / fight-3 / clan.fastly 标记 *available*
  - Git Conventions 新增两条注意事项：① PAT 无 workflow scope，commit 时不得包含 `.github/workflows/` 文件；② stale lock 文件用 `mv` 而非 `rm` 移除
- **`PROGRESS.md`** — 本条记录

### Verification Checklist
- [x] 全站 35 个页面均含 AdSense 脚本
- [x] 所有 ad-inline 和 sidebar 占位符已替换为 `<ins>` 块
- [x] 已推送至 GitHub main
- [x] CLAUDE.md boilerplate / image table / git notes 已更新
- [x] PROGRESS.md 已追加

---

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

## 2026-05-28 — Daily Update: Metacritic Record Blog + Guide Audit

### 阶段一：Blog 更新
- **`blog/highest-rated-lego-game-metacritic.html`** — New blog post: "LEGO Batman: Legacy of the Dark Knight Is Now the Highest-Rated LEGO Game Ever on Metacritic." Covers: Metascore 84 (47 reviews, 91% positive, 0 negative), dethroning The Skywalker Saga (82) and LEGO Star Wars 2's 16-year record, GamesRadar quote from Rollin Bishop (4/5), OpenCritic 85, user score 8.9. Full ranking table included. Sources: GamesRadar+, Metacritic, ComicBasics. Image: `fight-3.KeK453wH_Z23bgKb.webp` (Mr. Freeze in Freeze Truck).
- **`blog/index.html`** — New post card inserted at top; Latest Posts sidebar updated (3 posts kept).

### 阶段二：内容审计结果
**审计页面数：** 22 guide pages
**SEO Top 3 更新：**
1. **`gotham-map-guide.html`** — Replaced pre-release placeholder ("not officially detailed yet, check back after May 22") with confirmed post-launch content: 4 named islands (Tricorner, South, Central, North), 9 SubWayne fast travel stations with unlock mechanics, Tower activation system, full activity type list (Riddler Puzzles, Cluemaster Puzzles, WayneTech Caches, Races, Side Activities). Updated read time 3→5 min, last-updated date. (Score: 9/10)
2. **`best-characters-each-mission.html`** — Replaced pre-release placeholder ("will be published after May 22 launch") with full mission-by-mission chapter breakdown and character recommendations for all 6 chapters + Prologue. Confirmed mission names from Push Square. (Score: 8/10)
3. **`mayhem-collection-dlc.html`** — Removed "not yet confirmed" language from three locations; updated standalone pricing TBA text and trophy note to post-launch hedged language. (Score: 7/10)

**新建页面（如有）：** None (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (`blog/highest-rated-lego-game-metacritic.html`)
- [x] `blog/index.html` 已更新（卡片+侧边栏）
- [x] 内容审计已完成（22个guide页面）
- [x] SEO Top 3 更新已执行
- [x] `index.html` 无需更新（未新建guide页面）
- [x] `sitemap.xml` 已重新生成（38页）
- [x] `PROGRESS.md` 已追加
- [x] Git commit + push 已完成

## 2026-05-31 — Daily Update: Legacy Collection DLC Blog + Guide Audit

### 阶段一：Blog 更新
- **`blog/legacy-collection-dlc-breakdown.html`** — Full breakdown of the Legacy Collection DLC included with the Deluxe Edition: 21 suits across Arkham Trilogy, Batman Beyond, and Party Music packs; 3 Batmobiles; 15 Batcave props. Sources: Steam Deluxe Edition listing, legobatmangame.com. Image: `origin.DSZma2rC_2hKTV2.webp` (cycled from earliest post).

### 阶段二：内容审计结果
**审计页面数：** 22 guide pages
**SEO Top 3 更新：**
1. **`guides/suits-abilities-guide.html`** — Fixed DLC suit count from 126 → 129 (Legacy Collection = 21 suits + Sinister Pack = 7). Updated quick-stats, intro paragraph, DLC highlight box, and sidebar stat. Added detailed Legacy Collection pack breakdown with link to new blog post. (评分：8/10)
2. **`guides/all-characters-unlock.html`** — Added Legacy Collection cross-reference in the Mayhem DLC section: 21 suits across 3 themed packs, with link to new Legacy Collection blog post. (评分：7/10)
3. **`guides/stud-farming-guide.html`** — Added tip box clarifying that Legacy Collection (21 suits) and Mayhem Sinister Pack (7 suits) unlock without Stud cost, so Stud farming only applies to 101 base-game suits. Cross-link to Legacy Collection blog post. (评分：7/10)
**新建页面：** なし

### Verification Checklist
- [x] Blog 新文章已写入
- [x] blog/index.html 已更新
- [x] 内容审计已完成
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（如有）
- [x] sitemap.xml 已重新生成（41 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

---

## 2026-06-01 — Daily blog + guide audit (patch tracker focus)

### 阶段一：Blog 更新
- **`blog/post-launch-patch-tracker.html`** — New post: "Post-Launch Patch Tracker: Every Fix in LEGO Batman: Legacy of the Dark Knight". Covers pre-load build 23314029, Day 1 patch 1.005 (stability/crash fixes), suits progress bug fix (100/101 at 99.8% — patched), and a full known-bugs table with 6 community-reported issues and their current status. 600+ words. Image: `origin.DSZma2rC` (recycled — all images exhausted). Sources: UpdateCrazy, SteamDB, JayShockblast/X, Steam community.

### 阶段二：内容审计结果
**审计页面数：** 22 guide pages
**SEO Top 3 更新：**
1. **`suits-abilities-guide.html`** — Added tip box about the suits progress bug fix (100/101 at 99.8% now patched) with link to new patch tracker. (Score: 9/10)
2. **`100-percent-completion.html`** — Added known bugs warning box at top of content: disappearing Tricorner chest (pending fix) + suits counter bug (patched). Links to patch tracker. (Score: 8/10)
3. **`mission-3-walkthrough.html`** — Removed dead "Full Walkthroughs Coming Soon" TOC link, replaced with correct `#more-guides` anchor. (Score: 7/10)
**新建页面：** none

### Verification Checklist
- [x] Blog 新文章已写入
- [x] blog/index.html 已更新
- [x] 内容审计已完成
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（如有）
- [x] sitemap.xml 已重新生成（42 pages）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-05 — How Long to Beat Blog Post + DLC Date Accuracy Pass

### 阶段一：Blog 更新
- **`blog/how-long-to-beat-lego-batman-legacy.html`** — New blog post: "How Long to Beat LEGO Batman: Legacy of the Dark Knight — Story, 100%, and Free Play Times." Covers story-only runtime (10–15 hrs), average playthrough (~16 hrs), 100% completion (25–35 hrs), and full completionist time (~50 hrs). Includes comparison table vs other LEGO games, tips on Stud Multipliers for efficiency, and links to collectibles/completion guides. 600+ words. Image: official cover art (cycled back to oldest post). Sources: GamesRadar, VGC, Insider Gaming, Game8, TrueAchievements, Brick Fanatics.

### 阶段二：内容审计结果
**审计页面数：** 22 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/all-characters-unlock.html`** — Updated DLC section heading and banner from "September 2026" to "September 18, 2026". Added confirmed $24.99 Deluxe Edition upgrade pricing for Standard Edition owners. Clarified that standalone Mayhem Collection listing has not yet appeared on storefronts. (Score: 8/10)
2. **`guides/mayhem-collection-dlc.html`** — Updated quick stat from "Sep 2026" to "Sep 18". Updated "Is It Worth Buying" section to reference Sept 18 as confirmed date with pre-orders live. Updated Platinum note to reference "September 18, 2026" instead of vague "September 2026". (Score: 7.5/10)
3. **`guides/trophy-guide.html`** — Added new "Mayhem Collection DLC Trophies (September 18, 2026)" section. Notes that base Platinum requires no DLC, explains why DLC trophy list may or may not exist, and adds Mayhem Collection DLC Guide to Related Guides list. (Score: 7.5/10)
**新建页面：** none (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (how-long-to-beat-lego-batman-legacy.html, 600+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Featured Posts 更新）
- [x] 内容审计已完成（22 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新建页面）
- [x] sitemap.xml 已重新生成（46 pages）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-07 — Trophy Platinum Guide + Three-Guide SEO Audit

### 阶段一：Blog 更新
- **`blog/trophy-guide-platinum-road.html`** — New blog post: "LEGO Batman Legacy Trophy Guide — Road to Platinum 'I am Batman'". Covers all 52 trophies (1 Platinum, 3 Gold, 4 Silver, 44 Bronze), no missables, 3/10 difficulty, recommended two-phase roadmap (Story Mode → Free Play cleanup), tips on Stud Multipliers, and Riddler trophy / True Hero / Batcave prop strategies. 700+ words. Image: origin.DSZma2rC_2hKTV2.webp (cycled back — all images now used). Sources: PowerPyx, PSNProfiles, GameRiv, KeenGamer, HTG.

### 阶段二：内容审计结果
**审计页面数：** 30 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/trophy-guide.html`** — Updated Platinum time estimate from "25–40 hours" to "40–50 hours" (aligned with verified sources). Added cross-link to new blog post. Updated "Last updated" from May 24 to June 7, 2026. (Score: 8/10)
2. **`guides/release-date-platforms.html`** — Updated patch reference from 1.005 only to 1.005 + 1.006. Updated "Last updated" from June 2 to June 7, 2026. Updated "nearly two weeks" phrasing to "over two weeks." (Score: 6/10)
3. **`guides/100-percent-completion.html`** — Updated total time estimate from "25–40 hours" to "25–50 hours." Updated sidebar stat from "25–40 hrs" to "40–50 hrs." Added cross-link to new Platinum blog post. Added sidebar link to Platinum Roadmap. Updated "Last updated" to June 7, 2026. (Score: 7/10)
**新建页面：** none (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (trophy-guide-platinum-road.html, 700+ words)
- [x] blog/index.html 已更新（新卡片顶部）
- [x] 内容审计已完成（30 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新建页面）
- [x] sitemap.xml 已重新生成（56 pages）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

---

## 2026-06-08 — 每日全站更新：销量分析 blog + 多 guide SEO 修正

### 阶段一：Blog 更新
- **`blog/cross-platform-sales-breakdown.html`** — New blog post: "LEGO Batman Legacy Sells 1.2 Million Copies in Week One: PS5 Leads, Xbox Beats Steam". Covers Alinea Analytics sales data (PS5: 612K, Xbox: 289K, Steam: 249K), $83M revenue, Xbox vs Steam analysis, Skywalker Saga comparison, Switch 2 wild card. 700+ words. Image: /images/lego-batman-legacy-cover.jpg (cycled back to oldest post). Sources: Alinea Analytics, FRVR, Windows Central.
- **`blog/index.html`** — Added new card at top; also fixed pre-existing file truncation (file was cut off at line 379 mid-tag — completed missing cards for easter-eggs, launch-preview, visual-evolution, plus full sidebar and footer).

### 阶段二：内容审计结果
**审计页面数：** 30 guide pages scanned
**SEO Top 3 更新（+ 批量修正）：**
1. **`guides/deluxe-edition-explained.html`** — Fixed factual error: suit count 126 → 129 (Sinister Pack is 7 suits not 4); updated meta description; added Switch 2 pre-order bonus callout (Dark Knight Returns Batsuit). (Score: 8/10)
2. **`guides/all-villains-guide.html`** — Updated all "September 2026" → "September 18, 2026" (5 instances) with confirmed DLC release date. (Score: 7/10)
3. **`guides/suits-abilities-guide.html`** — Updated Sinister Pack date to September 18, 2026; added Switch 2 pre-order bonus suit entry (Dark Knight Returns Batsuit). (Score: 8/10)
**批量日期修正（September 2026 → September 18, 2026）：** batcave-hub-guide, pc-requirements, post-game-checklist, release-date-platforms, mayhem-collection-dlc (3×), stud-farming-guide
**新建页面：** none (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (cross-platform-sales-breakdown.html, 700+ words)
- [x] blog/index.html 已更新（新卡片顶部，并修复文件截断问题）
- [x] 内容审计已完成（30 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] 批量日期修正已完成（8个文件，"September 2026" → "September 18, 2026"）
- [x] index.html 链接已更新（无新建页面）
- [x] sitemap.xml 已重新生成（57 pages）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成
## 2026-06-10 — Dark Knight Mode Blog + Guide Audit

### 阶段一：Blog 更新
- **`blog/dark-knight-mode-survival-guide.html`** — New blog post: "Dark Knight Mode Survival Guide: Tips for LEGO Batman's Hardest Difficulty." Covers the lives system, 20% stud death penalty, red flash attack dodge technique, defensive upgrade priority, and co-op aggro-split advantage. 700+ words. Image: origin.DSZma2rC_2hKTV2.webp (cycling back — oldest post). Sources: Neon Lights Media, Games.gg, XModHub, Game Informer (Kotaku), Game8.

### 阶段二：内容審計結果
**审计页面数：** 30 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/difficulty-modes-guide.html`** — Enhanced Dark Knight tips section: added red flash dodge-roll requirement, 20% stud death penalty warning, co-op aggro-split benefit. Added cross-link to new Dark Knight Mode blog post. (Score: 8/10)
2. **`guides/waynetech-upgrades-guide.html`** — Added Dark Knight Mode callout box before Priority Phases section: warns about stud death penalty changing upgrade priority, links to Dark Knight Mode Survival Guide. (Score: 7.5/10)
3. **`guides/100-percent-completion.html`** — Updated bug notice: clarified Tricorner chest bug remains unconfirmed fixed in 1.006 (not in patch notes), added workaround tip. Added Dark Knight Mode stud management warning. (Score: 7/10)
**新建页面：** none (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (dark-knight-mode-survival-guide.html, 700+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Latest Posts 更新）
- [x] 内容审计已完成（30 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新建页面）
- [x] sitemap.xml 已重新生成（59 pages）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成
## 2026-06-11 — Switch 2 Minifigure Blog + DLC / Trophy Guide Audit

### 阶段一：Blog 更新
- **`blog/switch-2-exclusive-batman-minifigure.html`** — New blog post: "Switch 2 Deluxe Edition Comes with an Exclusive Retro Video Game Batman Minifigure." Covers the physical-only "Retro Video Game Batman" minifigure (based on the 1989 NES Sunsoft game) included with the physical Switch 2 Deluxe Edition ($89.99, Sept 18, 2026); no standalone option; why it matters to LEGO collectors; Switch 2 in-game features; comparison to LEGO Dimensions-era collectibles. 600+ words. Image: /images/lego-batman-legacy-cover.jpg (cycling back — oldest post). Sources: WB Games press release, The Brick Fan, Stonewars, GamesRadar, Brick Fanatics.

### 阶段二：内容审计结果
**审计页面数：** 30 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/mayhem-collection-dlc.html`** — Updated "TBA" standalone price entries (×2): replaced with confirmed info — no standalone listing exists, only the $24.99 Deluxe Edition upgrade. Updated Quick Facts sidebar and Ownership & Pricing grid. (Score: 9/10)
2. **`guides/trophy-guide.html`** — Updated DLC trophy uncertainty section: replaced "not yet confirmed" phrasing with "as of June 2026" datestamped language, tightened speculative framing around possible DLC trophy list. (Score: 8/10)
3. **`guides/all-characters-unlock.html`** — Updated stale "has not yet been listed on storefronts" language in DLC section with confirmed June 2026 datestamp. (Score: 7/10)
**新建页面：** none (blog post only)

### Verification Checklist
- [x] Blog 新文章已写入 (switch-2-exclusive-batman-minifigure.html, 600+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Latest Posts 更新）
- [x] 内容审计已完成（30 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新建页面）
- [x] sitemap.xml 已重新生成（60 pages）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-12 — June Mod Roundup + Guide SEO Audit

### 阶段一：Blog 更新
- **`blog/june-2026-mod-roundup.html`** — New blog post: "LEGO Batman Legacy Mod Roundup: The Best New Mods from June 2–7, 2026." Covers 5 new Nexus Mods released June 2–7: Dark Night Realism Reshade (Jun 2), Dark Knight Returns Battle Damaged skin by CharlesCardy (Jun 6), Dark Knight Suit Retexture by 1Borgir1 (Jun 3), Arkham City Batman by CreamySheev15 (Jun 7), Superbat by SwiftKnight5051 (Jun 7), Superman Legacy of the Man of Steel by SQUALLY242 (Jun 3). 700+ words. Follow-up to existing launch-week mods post. Image: foes.CtQfCF5a (cycling back — used in older easter-eggs post). Sources: Nexus Mods mod pages, SteamDB June 2 build note.

### 阶段二：内容审计结果
**审计页面数：** 30 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/suits-abilities-guide.html`** — Added new "LEGO Set QR Redemption Suits" section (id="qr-suits") covering the 4 LEGO set redemption codes (#76330–76333), how the wardrobe display works, and cross-link to QR Rewards blog post. Added to TOC. (Score: 9/10 — high search intent for suit unlock guides, clear content gap)
2. **`guides/collectibles-guide.html`** — Added "Character Requirement Risk Warnings" section (id="risk-warnings") with per-character ability gates: Batgirl Hack, Catwoman Lockpick, Nightwing Wall-Jump, Jim Gordon Rebound Launcher, Talia Shadow Dash. Added to TOC. Per CLAUDE.md long-term upgrade priority. (Score: 8/10)
3. **`guides/all-villains-guide.html`** — Expanded boss fight tips section from 6 to 9 villains, adding Ra's al Ghul (Lazarus Pit mechanic), The Joker (3-phase final boss), and The Penguin (umbrella rotation + drone phase). Added universal unblockable attack tip. (Score: 7/10)
**新建页面：** none

### Verification Checklist
- [x] Blog 新文章已写入 (june-2026-mod-roundup.html, 700+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Latest Posts 更新）
- [x] 内容审计已完成（30 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新建页面）
- [x] sitemap.xml 已重新生成（61 pages）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-14 — Batcave Challenges Blog + Falcone Fortunes Guide Updates

### 阶段一：Blog 更新
- **`blog/batcave-challenges-complete-guide.html`** — New blog post: "All 43 Batcave Challenges in LEGO Batman: Legacy of the Dark Knight — Complete Guide." 900+ words covering all challenge types (combat, stealth, character-specific, exploration, stud/progression), full tables with how-to strategies for each challenge, rewards info (465,000 Studs total, Batcave mural), and tips for efficient completion. Image: origin.DSZma2rC_2hKTV2.webp (cycled back). Sources: GameRant, Destructoid, TheGamer.

### 阶段二：内容审计結果
**审计页面数：** 10 guide pages scanned
**发现的内容缺口：** Falcone Fortunes (14 total, 2 WayneTech Chips each) entirely absent from all guide pages
**SEO Top 3 更新：**
1. **`guides/collectibles-guide.html`** — Added full Falcone Fortunes section (Score: 9/10): new `<h2 id="falcone">` with c-card overview, why they matter (28 total WayneTech Chips), character requirements (Batman + Catwoman, one needs Batgirl), and all 14 named locations with map coordinates. Also updated meta description and keywords, TOC, and overview list to include Falcone Fortunes.
2. **`guides/100-percent-completion.html`** — Added Falcone Fortunes as a named bullet in Phase 2 open-world activities list, with reward details and character requirements. Added to the full checklist. (Score: 7/10)
3. **`guides/post-game-checklist.html`** — Added new checklist item for all 14 Falcone Fortunes with time estimate (2–3 hours), reward note (28 WayneTech Chips), and link to collectibles guide Falcone section. (Score: 6/10)
**新建页面：** None

### Verification Checklist
- [x] Blog 新文章已写入 (batcave-challenges-complete-guide.html, 900+ words, 43 challenges covered)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Latest Posts 更新）
- [x] 内容审计已完成（10 guide pages scanned, Falcone Fortune gap identified）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新 guide 页面）
- [x] sitemap.xml 已重新生成（64 页，含新 blog 文章）
- [x] PROGRESS.md 已追加
- [x] Git commit + push

## 2026-06-15 — Stud Farming Blog + Guide Meta/Date Audit

### 阶段一：Blog 更新
- **`blog/stud-farming-guide-fast-studs.html`** — New blog post: "How to Farm Studs Fast in LEGO Batman: Legacy of the Dark Knight." 700+ words covering: the in-mission Stud Multiplier (x2→x4 via Hyper Combo skill upgrades), The Joker's Funhouse Free Play route (best farming level), the Batcave Stud Cache loop (~30k studs per visit), Jim Gordon's Rebound Launcher room-clearing tip, and skill tree picks (Stealthy Studs, Collectible Detective). Image: origin.DSZma2rC_2hKTV2.webp (cycled back — all library images used). Sources: GamesRadar, VGC, TheGamer, Games.gg.

### 阶段二：内容审计结果
**审计页面数：** 31 guide pages scanned
**SEO Top 3 更新：**
1. **`guides/tips-for-new-players.html`** — Fixed meta description/OG tags mismatch (Score: 8/10): meta said "Advanced tips and tricks...that go beyond the basics" but page targets new players. Updated to "Essential tips for new players...difficulty modes, Detective Mode, Red Bricks, stud farming, combat basics, and beginner mistakes." Title tag also refined. Keywords updated to beginner-focused terms.
2. **`guides/release-date-platforms.html`** — Updated dated post-launch section (Score: 7/10): changed "over two weeks" → "nearly four weeks", updated "as of June 7" → "as of June 15, 2026", updated Game Pass note from "as of May 29" → "as of June 15, 2026". Section heading changed from "First Week Reception" → "Reception & Updates" to reflect continued coverage.
3. **`guides/stud-farming-guide.html`** — Added internal link to new blog post (Score: 5/10): new sidebar link "Blog: Combo Multiplier Tips" pointing to blog/stud-farming-guide-fast-studs.html.
**新建页面：** None

### Verification Checklist
- [x] Blog 新文章已写入 (stud-farming-guide-fast-studs.html, 700+ words)
- [x] blog/index.html 已更新（新卡片顶部 + 侧边栏 Latest Posts 更新）
- [x] 内容审计已完成（31 guide pages scanned）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新 guide 页面）
- [x] sitemap.xml 已重新生成（65 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-16 — Complete Suits Guide Blog + 3 Guide SEO Updates

### 阶段一：Blog 更新
- **`blog/all-batsuits-unlock-guide.html`** — "All Suits in LEGO Batman: Legacy of the Dark Knight — Complete Unlock Guide". Full character-by-character breakdown of all 101 base-game suits (35 for Batman + 6 supporting characters) with exact unlock requirements per GameRant's post-launch database. Tag: Analysis. Image: legobatmangame.com origin diptych (recycled from oldest post). 7 min read.

### 阶段二：内容审计结果
**审计页面数：** 31 guide 页面
**SEO Top 3 更新：**
1. **`guides/suits-abilities-guide.html`** — Expanded "3 Ways to Unlock Suits" to 7 confirmed methods with specific milestones (WayneTech cache counts, animal milestones, Riddler/Cluemaster requirements, Falcone missions). Added link to new blog post. (评分：8/10)
2. **`guides/batcave-hub-guide.html`** — Corrected Wardrobe Room section: removed fabricated "11 from Red Brick colour scheme unlocks" claim; replaced with confirmed unlock methods (Main Story, Bat-Mite Store, Zoo Animals, WayneTech Caches, AR Trials, Riddler/Cluemaster, Wanted Posters, Falcone missions). (评分：6/10)
3. **`guides/mayhem-collection-dlc.html`** — Updated "Mayhem Mode is expected to have its own collectibles" to "includes its own objectives and collectibles according to the June 3, 2026 WB Games announcement". (评分：7/10)
**新建页面（如有）：** 无

### Verification Checklist
- [x] Blog 新文章已写入
- [x] blog/index.html 已更新（顶部新卡片 + Latest Posts 侧边栏）
- [x] 内容审计已完成（31 个 guide 页面）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新 guide 页面）
- [x] sitemap.xml 已重新生成（66 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-17 — Co-Op Blog + Beginner Guide Co-Op Section + Release Date Freshening

### 阶段一：Blog 更新
- **`blog/co-op-multiplayer-guide.html`** — "LEGO Batman: Legacy of the Dark Knight — Complete Co-Op Multiplayer Guide". Covers: how to enable local split-screen co-op (step-by-step), split-screen mechanics, Steam Remote Play Together + PlayStation Share Play online workarounds, best character combos (4 pairings), collectible hunting tips in co-op, and story mode co-op notes. 600+ words. Tag: Guide. Image: `legobatmangame.com/_astro/family.CQW_jlFK_2qvCfg.webp` (Gordon + Catwoman; cycled). Sources: Game Rant, GamesRadar, Nerdschalk. 6 min read.

### 阶段二：内容审计结果
**审计页面数：** 31 guide 页面
**SEO Top 3 更新：**
1. **`guides/beginners-guide.html`** — Added "Playing Co-Op" section (completely missing). Covers: how to drop in second player, split-screen basics, Steam Remote Play Together / PS Share Play note, link to co-op guide. Added co-op guide to sidebar "Next Guides" list. (评分：9/10)
2. **`guides/co-op-guide.html`** — Added cross-link to new blog post `co-op-multiplayer-guide.html` in sidebar "Related Guides". Strengthens internal linking between authoritative guide and new editorial post. (评分：8/10)
3. **`guides/release-date-platforms.html`** — Updated "as of June 15" to "June 17". Updated Multiplayer section from vague "preview reports" language to confirmed post-launch co-op details with drop-in instructions and link to co-op guide. (评分：7/10)
**新建页面（如有）：** 无

### Verification Checklist
- [x] Blog 新文章已写入
- [x] blog/index.html 已更新（顶部新卡片 + Latest Posts 侧边栏）
- [x] 内容审计已完成（31 个 guide 页面）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新 guide 页面）
- [x] sitemap.xml 已重新生成（67 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-18 — Daily update: Batman mythology tributes blog + 3 guide SEO updates

### 阶段一：Blog 更新
- **`blog/batman-legacy-tributes-deep-dive.html`** — "Every Batman Movie, BTAS & Comics Tribute in LEGO Batman: Legacy of the Dark Knight" — 700+ words. Based on DC.com's June 8 post-launch feature by Joshua Lapin-Bertone, covering Kevin Conroy tribute billboard, shot-for-shot BTAS Chapter 4 intro, Batman Returns Catwoman recreation, Cesar Romero decoy Joker, Arkham Asylum opening recreation, NES purple Batsuit, Court of Owls Easter eggs, Loeb & Sale's Comic Store. Image: fight-3.KeK453wH_Z23bgKb.webp (Mr. Freeze). Tag: Analysis.

### 阶段二：内容审计结果
**审计页面数：** 31 guide 页面
**SEO Top 3 更新：**
1. **`suits-abilities-guide.html`** — Added "Video Game Legacy Skins" subsection with the confirmed 1990 NES purple Batsuit unlock (sourced from DC.com June 8 article). Previously missing from the guide.（评分：9/10）
2. **`tips-for-new-players.html`** — Added new "Hidden Interactions & Community Discoveries" section with 5 verified secrets: yak petting in Nanda Parbat, Batusi dance in Chapter 1, throne dialogue Easter egg, Bat-Signal chapter changes, Kevin Conroy billboard. All sourced from DC.com June 8 article.（评分：7/10）
3. **`all-villains-guide.html`** — Added Cesar Romero decoy Joker Easter egg in Chapter 5 to the Joker villain card (complete with confirmed mustache detail). Sourced from DC.com June 8 article.（评分：7/10）
**新建页面：** 无

### Verification Checklist
- [x] Blog 新文章已写入
- [x] blog/index.html 已更新
- [x] 内容审计已完成（31 页）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新 guide 页面）
- [x] sitemap.xml 已重新生成（68 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-21 — Mayhem Collection DLC Confirmed Blog + Collectibles/Suits/Trophy Guide Updates

### 阶段一：Blog 更新
- **`blog/mayhem-collection-dlc-confirmed.html`** — "Mayhem Collection DLC Confirmed: September 18 Release Date & Full Content Breakdown" — 650+ words. Topic: Official confirmation of September 18, 2026 DLC release date, Joker & Harley Quinn playable characters, Arkham Asylum breakout story mission, Mayhem Mode, and Sinister Pack (7 suits, 5 Batcave items, 1 Batmobile). Sources: game8.co, LEGO.com, Steam. Tag: News + Analysis. Distinct from earlier "mayhem-collection-dlc-leak.html" (unconfirmed leak). Image: foes.CtQfCF5a_1k24YI.webp (Batman vs Joker).

### 阶段二：内容审计结果
**审计页面数：** 32 guide 页面（重点检查 suits, collectibles, trophy, characters, beginners, mayhem DLC, release-date, deluxe-edition）
**SEO Top 3 更新：**
1. **`collectibles-guide.html`** — Fixed major accuracy error: WayneTech Caches section said "10 Total hidden in Batcave" — corrected to "200 Total scattered across story missions and Gotham open world." Added suit unlock milestone thresholds (10, 30, 50, 70, 80, 90, 110, 140, 150, 160, 180). Updated meta description to include accurate counts. Sources: thegamer.com, games.gg.（评分：9/10）
2. **`suits-abilities-guide.html`** — Updated meta description and OG description from imprecise "101+" to accurate "101 base suits (129 with all DLC)." Better matches user search intent for exact counts.（评分：7/10）
3. **`trophy-guide.html`** — Added PowerPyx Trophy Guide & Roadmap as a key external resource (was missing from the guide). Added patch 1.006 note about Mr. Freeze boss crash fix that was blocking story trophy unlocks for some players.（评分：7/10）
**新建页面：** 无

### Verification Checklist
- [x] Blog 新文章已写入
- [x] blog/index.html 已更新（顶部新卡片 + Latest Posts 侧边栏）
- [x] 内容审计已完成（32 个 guide 页面）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接已更新（无新 guide 页面）
- [x] sitemap.xml 已重新生成（72 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-22 (Session 2) — Twitch Drops Blog + Suit Count Fixes + Batcave Props Guide

### 阶段一：Blog 更新
- **`blog/twitch-drops-batcave-cosmetics-guide.html`** — "LEGO Batman Legacy Twitch Drops: All 8 Free Batcave Rewards Explained". 5 min read. Complete coverage of the May 19–31, 2026 Twitch drops campaign: all 8 Batcave prop rewards (table with channel requirements), step-by-step account linking guide, DC Twitch exclusives (Comic Stand + Neon Bat-Symbol), in-game item location (Chapter 2 unlock), missed-campaign FAQ, future drops speculation tied to September 18 Mayhem Collection DLC launch. Sources: WB Games Rewards page, TheGamer, Insider Gaming, Dexerto. Image: `legobatmangame.com/_astro/origin.DSZma2rC_2hKTV2.webp` (cycled). Tags: Community + News.

### 阶段二：内容审计结果
**审计页面数：** 8 guide 页面
**关键发现：** suits-abilities-guide.html 有 git rebase 冲突+文件截断；100-percent-completion.html 显示补丁前的 101 suit stat；batcave-hub-guide.html 无 Twitch drops 提及。

**SEO Top 3 更新：**
1. **`guides/suits-abilities-guide.html`** — 重建无冲突版本；meta description 更新为"128 suits (100 base + 28 DLC)"；stat card、正文、og:description 全部统一为 100/28/128。（评分：9/10）
2. **`guides/100-percent-completion.html`** — Suits to Collect stat 101→100；购买成本文字更正。（评分：8/10）
3. **`guides/batcave-hub-guide.html`** — 修正 Wardrobe Room suit 数字；新增 Batcave Props & Customization 章节，含 Twitch drops 内链。（评分：7/10）

**新建页面：** blog/twitch-drops-batcave-cosmetics-guide.html

### Verification Checklist
- [x] Blog 新文章已写入
- [x] blog/index.html 已更新
- [x] 内容审计已完成
- [x] SEO Top 3 更新已执行
- [x] sitemap.xml 已重新生成（74 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-23 — Steam Summer Sale blog + 3 guide SEO fixes

### 阶段一：Blog 更新
- **`blog/steam-summer-sale-2026-guide.html`** — Steam Summer Sale 2026（6月25日开始）时效性内容：解析LEGO Batman Legacy是否会打折、Fanatical Mystery Egg Bundle $1机会、Standard vs Deluxe版本性价比、历史低价数据及追踪工具。来源：gHacks/Steamworks官方文档/Game Rant。图片循环：og-image.BcIYb3Fq.jpg。

### 阶段二：内容审计结果
**审计页面数：** 31 个 guide 页面（全扫描）

**SEO Top 3 更新：**
1. **`guides/suits-abilities-guide.html`**（评分：8/10）— meta description 更新：明确当前可用 121 件（100 基础 + 21 Legacy Collection），Sinister Pack 7 件 9月18日上线，总计 128 件。OG title 加入"121 Now / 128 with DLC"便于搜索识别。
2. **`guides/mission-1-walkthrough.html`**（评分：8/10）— URL 为 mission-1-walkthrough 但内容为故事概览，搜索意图严重错配。更新：meta title/description 重新对齐实际内容；替换原有 tip-box，加入章节攻略导航（Chapter 1 Red Hood、Chapter 4、Beginner's Guide），解决跳出率问题。
3. **`guides/release-date-platforms.html`**（评分：6/10）— OG description 由未来时"launches"改为过去时；meta description 补充 Switch 2 九月十八日上线信息；正文"is launching on four platforms"修正为"launched on three of four"。

**新建页面：** 无

### Verification Checklist
- [x] Blog 新文章已写入（steam-summer-sale-2026-guide.html，500+字）
- [x] blog/index.html 已更新（新卡片置顶，侧边栏 Latest Posts 已更新）
- [x] 内容审计已完成（31 guide 页面）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接未变动（无新 guide 页面）
- [x] sitemap.xml 已重新生成（74 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成

## 2026-06-24 — LEGO Batman Returns Batmobile Rumour Blog + 3 Guide SEO Fixes

### 阶段一：Blog 更新
- **`blog/lego-batman-returns-set-76355-batmobile-rumor.html`** — 新文章：LEGO Batman Returns Set 76355 rumoured 1992 Batmobile (2,272 pieces, ~$220, September 1, 2026). 来源：StoneWars.com (Reddit leaker Brick Tap). 500+字，含对比表格（vs 76139、76328）、详细分析、跨产品 September 时间节点。图片：gear-3（蝙蝠摩托，循环使用）。
- **`blog/index.html`** 已更新：新卡片置顶，侧边栏 Latest Posts 已更新。

### 阶段二：内容审计结果
**审计页面数：** 31 个 guide 页面（全扫描）

**SEO Top 3 更新：**
1. **`guides/release-date-platforms.html`**（评分：9/10）— 补充 Nintendo Switch 2 实体版信息：Game Key Cards、专属 Retro Video Game Batman 实体人仔（Deluxe 实体限定，限量供应）。来源：StoneWars June 4, 2026。
2. **`guides/deluxe-edition-explained.html`**（评分：9/10）— 修正套装总数错误（101基础→100，129总→128）；新增 Switch 2 实体 Deluxe Edition 专属人仔信息；更新 meta description。
3. **`guides/mayhem-collection-dlc.html`**（评分：8/10）— 新增 callout：Switch 2 Deluxe 实体版人仔说明，澄清 Switch 2 买家在一个包装里获得的全部内容（DLC + Legacy Collection + 预购套装 + 实体人仔）。

**新建页面：** 无

### Verification Checklist
- [x] Blog 新文章已写入（lego-batman-returns-set-76355-batmobile-rumor.html，500+字）
- [x] blog/index.html 已更新（新卡片置顶，侧边栏 Latest Posts 已更新）
- [x] 内容审计已完成（31 guide 页面）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接未变动（无新 guide 页面）
- [x] sitemap.xml 已重新生成（75 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成
                                                                                                        
## 2026-06-25 — Kevin Conroy Voice Tribute Blog + 3 Guide SEO Updates

### 阶段一：Blog 更新
- **`blog/kevin-conroy-voice-tribute-lego-batman.html`** — 新文章：Kevin Conroy 的声音隐藏在《LEGO Batman: Legacy of the Dark Knight》的阿卡姆疯人院关卡中，TT Games 高级关卡设计师 Mike Consalvey 于 2026 年 6 月 18 日在 X 上确认。文章详细介绍了两处隐藏存档声线（保安警报 + 电梯故障广播）、Gotham 城市中的"After Hours With Conroy"广告牌致敬，以及字幕表中的署名。600+字，含引用框、来源侧边栏、完整的深色主题 HTML。图片：clues-2（哥谭夜景 — 霓虹灯、蝙蝠信号），循环自 lego-batman-redeem-codes-qr-rewards.html。来源：GamingBible (June 19)、DC.com (June 8)、Screen Rant、TheGamer、OpenCritic。
- **`blog/index.html`** 已更新：新卡片置顶，侧边栏 Latest Posts 已更新（Kevin Conroy / 76355 Batmobile / Steam Summer Sale）。

### 阶段二：内容审计结果
**审计页面数：** 30 个 guide 页面（全扫描）

**SEO Top 3 更新：**
1. **`guides/trophy-guide.html`**（评分：8/10）— 在"Character & Suit Trophies"板块新增具名奖杯"Let's see what Batgirl can do"（PS5 专属，解锁 Batgirl 时触发），注明出处为 BTAS《Shadow of the Bat, Part One》，来源 DC.com June 8, 2026。
2. **`guides/post-game-checklist.html`**（评分：8/10）— 目录"Upcoming DLC"改为"Mayhem Collection DLC (September 18, 2026)"；新增章节"Secret Easter Egg: Kevin Conroy's Hidden Voice Lines"，包含两处声线位置及广告牌信息，并链接到 Blog 深度文章。
3. **`guides/collectibles-guide.html`**（评分：7/10）— 在 Batcave Minikits 板块新增"Optimal Minikit Sweep Route (Post-Story)"，提供 7 个 Batcave 房间的逐房间路线（Main Chamber → Batcomputer Room → Workbench & Armoury → Trophy Room → Vehicle Bay → Chapter 5 Room → Chapter 6 Room），含具体隐藏位置提示。符合 CLAUDE.md 持续升级优先级。

**新建页面：** 无

### Verification Checklist
- [x] Blog 新文章已写入（kevin-conroy-voice-tribute-lego-batman.html，600+字）
- [x] blog/index.html 已更新（新卡片置顶，侧边栏 Latest Posts 已更新）
- [x] 内容审计已完成（30 guide 页面）
- [x] SEO Top 3 更新已执行
- [x] index.html 链接未变动（无新 guide 页面）
- [x] sitemap.xml 已重新生成（77 页）
- [x] PROGRESS.md 已追加
- [x] Git commit + push 已完成
