# BrickHeroGuide — Work Log

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

<<<<<<< Updated upstream
**新建页面（如有）：** None (blog pos
=======
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
>>>>>>> Stashed changes

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
- [ ] Git commit + push 已完成
