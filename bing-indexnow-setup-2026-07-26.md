# BrickHeroGuide.com — Bing / IndexNow 打通记录
**日期：** 2026-07-26

---

## 背景

GSC数据显示网站过去28天Organic Search点击为0，排名普遍卡在40-90名（新域名沙盒期）。90天回看Google Organic其实有114个session、Bing Organic已有15个session——说明Bing早就在自然抓取，只是没做过任何专属优化。这次做的是"零成本/低成本"的分发动作，不是内容优化。

## 实际操作步骤（按发生顺序）

1. **Bing Webmaster Tools注册 + Import from GSC**：因为brickheroguide.com已经在GSC验证过，用一键导入省掉了重新走DNS/文件验证的步骤，站点和历史数据直接带过去了。

2. **Sitemap提交**：在Bing Webmaster Tools → Sitemaps页面确认/提交了 `https://brickheroguide.com/sitemap.xml`，状态"Processing"，0 errors / 0 warnings。这是最基础但必须做的一步，不依赖robots.txt。

3. **robots.txt 踩了一个坑**：一开始我自己生成了一份简化版robots.txt想加Sitemap指令，但后来抓取线上实际内容才发现，Cloudflare已经在边缘自动管理了一份更完善的robots.txt——通过`Content-Signal`机制屏蔽了GPTBot、ClaudeBot、CCBot、Bytespider等**AI训练爬虫**，同时保留`search=yes`允许正常搜索引擎和AI实时联网检索。这份Cloudflare管理的版本不在代码仓库里，是CDN层面注入的。
   - **教训：改robots.txt之前必须先抓取线上实际内容，不能想当然直接写。** 差点用一份"更简单但更宽松"的版本覆盖掉本来在保护内容不被AI训练爬虫白嫖的规则。
   - 最终处理：discard掉了自己写的那份，没有push，线上配置保持不变。

4. **IndexNow密钥文件**：
   - 第一版是我自己用`python3 -c "import secrets; print(secrets.token_hex(16))"`生成的32位hex密钥，创建了对应的`{key}.txt`。
   - 后来在Bing Webmaster Tools左侧栏发现有独立的"IndexNow"页面，Bing自己生成了一个官方密钥（`82a1f518704946c88baa7370829f1955`），改用这个更可靠，旧的自建密钥文件discard掉了。
   - 最终密钥文件路径：`https://brickheroguide.com/82a1f518704946c88baa7370829f1955.txt`，内容就是这串key本身。

5. **实际提交**：密钥文件push上线确认可访问后，用IndexNow的单URL GET接口给三篇当天新发的攻略提交了索引通知：
   - `https://brickheroguide.com/guides/subwayne-puzzle-solutions-guide`
   - `https://brickheroguide.com/guides/cheat-codes-unlockables-guide`
   - `https://brickheroguide.com/guides/ar-trials-guide`
   
   请求格式：`https://api.indexnow.org/indexnow?url={编码后的URL}&key={key}&keyLocation={编码后的key文件URL}`。响应是空body（IndexNow协议标准行为，成功只返回状态码，不返回内容），没有报错。

## 后续动作

- 以后每次BrickHeroGuide发新攻略/博客，在PROGRESS.md流程里顺手加一步IndexNow提交，不用每次单独交代。
- 通用化的操作方法已经整理成技能库里的 `indexnow-submit` skill，其他网站项目（TarifQC.ca、ImmoCliQ等）需要时可以直接复用，不用重新踩一遍robots.txt那个坑。
