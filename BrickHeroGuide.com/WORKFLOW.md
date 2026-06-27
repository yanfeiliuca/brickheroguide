# BrickHeroGuide.com — Content Production Workflow

**Game:** LEGO Batman: Legacy of the Dark Knight  
**Last updated:** 2026-06-27

---

## 核心原则

> "不知道就说不知道。先看再改。每条数值必须标注来源。"

所有内容生产分两类：**攻略页（高准确性要求）** 和 **博客文章（时效性优先）**。

---

## 一、四层防幻觉验证系统

### 第一层：提示词层

每次生成攻略内容时，提示词必须包含以下约束：

```
规则：
1. 如果不确定某个数值，直接写"[待查证]"，不要猜。
2. 每个数值旁边必须标注来源（例如：来源：IGN评测、官方Steam页面）。
3. 不准引入 data/game-facts.json 中没有记录的数值。
4. 禁止使用"大约"、"可能"、"估计"等模糊表述处理数值类内容。
```

### 第二层：审核员流程

攻略初稿生成后，用以下审核提示词过一遍：

```
你是内容审核员，不是作者。任务：
1. 对照 data/game-facts.json，逐一核查文中所有数值。
2. 不一致的地方用 ⚠️ 标红，列出：[原文内容] vs [JSON中的正确值]。
3. forbidden_errors 列表中的错误，如果出现直接标为 ❌ 致命错误。
4. 输出：通过 ✅ / 待修改 ⚠️ / 致命错误 ❌ 三档结论。
```

### 第三层：数据库取值（最高优先级）

**唯一数据来源：`data/game-facts.json`**

- AI生成内容时，数值只能从这个文件取
- 文件里没有的数值 → 先人工查证，写入JSON，再生成内容
- JSON更新时，必须记录 `last_verified` 日期和来源

**当前已验证数值（截至 2026-06-27）：**

| 数值类型 | 正确值 |
|---------|--------|
| 主线任务数 | 21 |
| 可玩角色 | 7（+3隐藏）|
| 基础服装 | 101（含全DLC 129）|
| 收藏品总数 | 247+ |
| 谜题 | 121 |
| WayneTech缓存 | 200 |
| PS5奖杯数 | 52 |
| Xbox成就数 | 51 |
| 哥谭岛屿数 | 4 |
| IGN评分 | 8/10 |
| Steam状态 | 压倒性好评（11600+评测）|
| Switch 2 掌机分辨率 | 720p |
| Switch 2 底座分辨率 | 最高1080p |
| Mayhem DLC发布日期 | 2026-09-18 |

### 第四层：内容风险分层

| 风险等级 | 内容类型 | 验证要求 |
|---------|---------|---------|
| 🔴 高风险 | 数值、掉落率、奖杯条件、技能效果 | 第二层审核员 + 第三层JSON取值 |
| 🟡 中风险 | 配装思路、角色推荐、难度评估 | AI生成 + 人工抽检（10篇取1篇）|
| 🟢 低风险 | 游戏背景介绍、通用攻略框架、操作说明 | AI生成即可 |

---

## 二、博客自动更新流程

### 每日执行顺序

```
搜索阶段（10分钟）
  ↓
搜索关键词：
  - "LEGO Batman Legacy Dark Knight" + 当天日期
  - "LEGO Batman Legacy news" site:ign.com OR site:gamesradar.com
  - Reddit r/LEGOGaming 最新帖子
  - WB Games 官方 Twitter/社交媒体

筛选阶段
  ↓
优先级：官方公告 > 版本更新 > 社区发现 > 一般评测

生成阶段（使用 web-content-fact-guard-en skill）
  ↓
- 最少600字，目标700-1000字
- H2分节，底部列来源
- 风险分层：博客文章默认为中/低风险
- 图片从已批准列表轮换（记录使用次数）

发布阶段
  ↓
- 写入 blog/YYYY-MM-DD-[slug].html
- 更新 blog/index.html（顶部新卡片 + Latest Posts侧边栏）
- 更新 sitemap.xml
```

### 已批准图片库（追踪使用次数）

| 图片URL | 已用次数 |
|--------|---------|
| `legobatmangame.com/_astro/og-image.BcIYb3Fq.jpg` | — |
| `legobatmangame.com/_astro/fight-2.BFd6neBb_2adSpB.webp` | — |
| `legobatmangame.com/_astro/family.CQW_jlFK_2qvCfg.webp` | — |
| `legobatmangame.com/_astro/foes.CtQfCF5a_1k24YI.webp` | — |
| `legobatmangame.com/_astro/gear-3.5F2kKy0I_1z9tbe.webp` | — |
| `legobatmangame.com/_astro/fight-3.KeK453wH_Z23bgKb.webp` | — |
| `legobatmangame.com/_astro/prefooter-keyart.C5w2I9s1_1Iktj5.jpg` | — |
| `legobatmangame.com/_astro/origin.DSZma2rC_2hKTV2.webp` | — |
| `legobatmangame.com/_astro/postfooter.Bp36eHDB_Z2cb3ek.webp` | — |

规则：每次生成博客前，选用次数最少的图片，更新上表。

---

## 三、验证指标（KPI）

| 指标 | 测量方法 | 目标 |
|-----|---------|------|
| 攻略准确性 | 抽检10篇，人工核对数值 | 零数值错误 |
| 博客更新频率 | PROGRESS.md条目数 | 每天1篇 |
| 流量变化 | GA4对比AI自动更新前后 | 持续上升 |
| 关键词排名 | Google Search Console | 核心词前10 |

---

## 四、绝对禁止重新引入的错误

直接来自 `data/game-facts.json` 的 `forbidden_errors` 字段：

- ❌ `trophy-achievement-guide.html` → 正确：`trophy-guide.html`
- ❌ WayneTech缓存 = 10 → 正确：200
- ❌ 主线任务 = 29+ 或 8 → 正确：21  
- ❌ Dark Knight Returns Batsuit 是 Switch 2 独家 → 错误，全平台可获取
- ❌ Switch 2 性能"估计/待定" → 已知：720p掌机/1080p底座
- ❌ 收藏品总数 "99+" → 正确：247+
- ❌ canonical URL 含 .html 后缀 → 全站统一干净URL

---

## 五、会话结束检查清单

```
- [ ] Blog 新文章已写入 blog/
- [ ] blog/index.html 已更新（顶部新卡片 + Latest Posts侧边栏）
- [ ] 审计已完成（扫描31个guide页面）
- [ ] SEO Top 3 更新已执行
- [ ] index.html 链接已更新（仅当有新guide页面时）
- [ ] sitemap.xml 已重新生成
- [ ] PROGRESS.md 已追加（只许添加，不许删除）
- [ ] data/game-facts.json 如有新数值已更新
- [ ] Git commit + push 已完成
```
