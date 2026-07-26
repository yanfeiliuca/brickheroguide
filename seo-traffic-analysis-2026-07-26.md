# BrickHeroGuide.com — GSC / GA4 数据分析与整改意见
**分析日期：** 2026-07-26 ｜ **数据窗口：** 过去28天 ｜ **数据来源：** Google Search Console（`sc-domain:brickheroguide.com`）+ GA4（Property 538277512），经 Supermetrics 直接拉取，非估算

---

## 一、核心结论（先说重点）

**ChatGPT 是目前网站的第一大流量来源，超过 Google。** 过去28天GA4总计74个session，其中41个（55%）来自 `chatgpt.com` 的 AI Assistant 渠道，31个是 Direct，**Organic Search 渠道是零**——GSC 同期数据印证了这一点：0次点击，尽管有53+次曝光。

**结论不是"内容不行"，是"域名还没被Google信任"。** 两个月大的新站，平均排名卡在40-90名（第4-9页），这是新域名的典型沙盒期表现，跟内容质量关系不大。真正验证内容质量的信号，反而是 ChatGPT 已经在主动引用并被点击——说明攻略页的结构化程度和事实密度已经达到被AI引擎摘录的门槛，只是 Google 的信任积累还没跟上。

---

## 二、GSC 数据快照（过去28天）

### 曝光最多的页面
| 页面 | 曝光 | 点击 | 平均排名 |
|---|---|---|---|
| 首页 `/` | 53 | 0 | 49.5 |
| `/blog/developer-interview-roundup` | 2 | 0 | 3 |
| `/blog/highest-rated-lego-game-metacritic` | 1 | 0 | 3 |
| `/blog/lego-batman-redeem-codes-qr-rewards` | 1 | 0 | 4 |
| `/guides/mission-3-walkthrough` | 1 | 0 | 59 |

注意：后三个页面排名其实是第1页（position 3-4），但曝光量只有1-2次——不是排名问题，是这几个词本身搜索量极低，样本太小，暂时看不出趋势。

### 24个真实搜索词，全部0点击
排名普遍在40-90之间（第4-9页），例外是 `lego batman: legacy of the dark knight checklist`（排名22，第3页，仍然进不了点击区）。完整词表里最值得关注的是这几个已经出现在Google索引里、但站内可能覆盖不够精确的词：

- `how to unlock tumbler lego batman`
- `how to get the dinosaur in lego batman`
- `computer wiz lego batman challenge` / `box ambush` / `hair trigger challenge`（这三个是Batcave Mural Challenge的具体挑战名）
- `lego batman legacy of the dark knight skill bricks`
- `bat cave minikit locations`

这些是Google自己反馈的真实需求，比外部last30days搜索猜测的选题准得多，建议后续内容/审计流程直接把这份词表当输入源。

---

## 三、GA4 数据快照（过去28天）

### 渠道分布
| 渠道 | Session | 用户 | 互动率 |
|---|---|---|---|
| AI Assistant（100% 来自 chatgpt.com） | 41 | 29 | 34.2% |
| Direct | 31 | 29 | 35.5% |
| Unassigned | 2 | 2 | 0% |
| **Organic Search** | **0** | **0** | — |

### 页面表现（Top 5，按session）
| 页面 | Session | 停留(秒) | 跳出率 |
|---|---|---|---|
| `/` | 23 | 4.1 | 78.3% |
| `/guides/100-percent-completion` | 18 | 35.1 | 72.2% |
| `/guides/collectibles-guide` | 12 | 5.2 | 83.3% |
| `/guides/suits-abilities-guide` | 4 | 170.1 | 50% |
| `/blog/post-launch-patch-tracker` | 3 | 49.3 | 0% |

**数据质量提醒：** 大量长尾页面显示"1 session / 100%互动 / 停留100+秒"，样本量是1，大概率是发布后自己预览产生的，不能当真实读者行为解读。真正该盯的是曝光量和session总数的周趋势，不是单页面的互动率。

### 每日趋势
7月15-17号出现小高峰（9、9个session/天），随后回落到1-6/天，过去28天没有稳定增长曲线，波动大于趋势。

---

## 四、整改意见：如何做外链/权重建设（重点）

诊断很明确：内容产出节奏没问题（75+页、每日更新），瓶颈在**域名权重和外部信任信号**，不是继续写更多攻略能解决的。下面按"投入产出比"从高到低排：

### 优先级1 — 几乎零成本，今天就能做
- **打通自己的站群内链**：Supermetrics账号里能看到你名下还有 `s2guidehub.com`、`relictrek.com`、`relictrek.net`、`preachkit.net`、`aitextcoach.com` 几个站点。如果其中任何一个话题跟LEGO Batman Legacy有交集（尤其s2guidehub.com，光看名字像是Switch 2相关站），从那边给BrickHeroGuide的具体攻略页（不是首页）加一条真实相关的外链，是你完全控制、零成本、立刻生效的权重来源。
- **提交Bing Webmaster Tools**：大部分人只提交Google，Bing的沙盒期短得多，而且Bing索引会被Copilot等AI工具直接调用——鉴于你现在ChatGPT流量已经跑通，Bing这条路径的边际收益可能比继续抠Google SEO更高。

### 优先级2 — 每次10-20分钟，效果可累积
- **Reddit真实回答带链接**：`r/LegoVideoGames`、`r/legobatman`（如果存在）、游戏发售期相关的discussion thread。原则是先给出有价值的直接答案，链接放在"这里有完整攻略"的自然位置，不要开局就甩链接——Reddit对纯广告式回复的惩罚（删帖/限流）比不带链接的沉默帖子伤害更大。
- **GameFAQs留言板**：LEGO Batman Legacy的官方GameFAQs board一直有玩家提问（前面搜到的具体挑战名问题很多就是这类板子上会出现的）。回答问题+带具体攻略页链接，这类论坛的外链权重通常比社交媒体更被Google看重。
- **Wiki外链请求**：`legobatmanwiki.com`、Fandom上的LEGO Batman wiki，如果某个页面（比如SubWayne、Falcone Fortune）内容比你的攻略简略，直接联系wiki维护者提议把你的完整攻略加进"External Links"区块——这类高权重、高相关性的wiki外链性价比最高，但需要主动邮件/私信联系，不是被动等待。

### 优先级3 — 有余力再做，非当务之急
- YouTube攻略视频简介区放链接（需要先有视频，或联系已有创作者）
- Discord官方/粉丝社群问答带链接（注意各服务器的自我推广规则）
- 结构化数据标记（FAQPage / HowTo schema）——不是外链，但能同时提升Google富摘要展示概率和AI引擎抓取效率，技术成本一次性，长期受益

### 时间预期
新域名沙盒期通常是2-6个月起，现在两个月，属于正常范围。外链建设不会让排名一夜从90名跳到10名，但会缩短沙盒期、加快Google对域名的信任评估。接下来该盯的核心指标是**GSC总曝光量的周环比趋势**，而不是点击量或排名——曝光在涨，说明Google正在加大试探性展示的力度，这是排名突破前必经的信号。

---

## 五、下一步

后续内容选题流程建议把本文件第二节的GSC真实搜索词列为输入源之一，跟last30days外部搜索结果并列使用，而不是只依赖外部搜索推测需求。

*本文件仅记录分析结果，不涉及网站文件改动，无需git commit。*
