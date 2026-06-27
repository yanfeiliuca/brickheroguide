# git-push-brickhero.ps1
# BrickHeroGuide.com — 一键提交并推送到 GitHub main
# Token 存放于：~/.brickhero-token（不提交到 git）
# 用法：pwsh git-push-brickhero.ps1 ["可选提交信息"]

param(
    [string]$Message = ""
)

$RepoRoot  = "$PSScriptRoot/.."
$Branch    = "main"
$Today     = Get-Date -Format "yyyy-MM-dd"
$CommitMsg = if ($Message) { $Message } else { "BrickHero update: $Today" }

# ── 读取 token（从本地文件，不提交到 git）──────────────────────
$TokenFile = "$HOME/.brickhero-token"
if (-not (Test-Path $TokenFile)) {
    Write-Host "❌ Token 文件不存在：$TokenFile" -ForegroundColor Red
    Write-Host "   请执行：echo 'YOUR_TOKEN' > ~/.brickhero-token" -ForegroundColor Yellow
    exit 1
}
$Token  = (Get-Content $TokenFile -Raw).Trim()
$Remote = "https://yanfeiliuca:${Token}@github.com/yanfeiliuca/brickheroguide.git"

Set-Location $RepoRoot
Write-Host ""
Write-Host "📁 仓库路径：$(Resolve-Path .)" -ForegroundColor Cyan

# ── 1. 清理残留 lock 文件 ────────────────────────────────────────
Write-Host "🔓 清理 lock 文件..." -ForegroundColor Yellow
Remove-Item ".git/index.lock" -ErrorAction SilentlyContinue
Remove-Item ".git/HEAD.lock"  -ErrorAction SilentlyContinue

# ── 2. 检查是否有变更 ────────────────────────────────────────────
$Status = git status --porcelain
if (-not $Status) {
    Write-Host "✅ 无变更，无需提交。" -ForegroundColor Green
    exit 0
}

Write-Host "📋 待提交文件：" -ForegroundColor Cyan
git status --short

# ── 3. 暂存所有变更 ──────────────────────────────────────────────
git add -A
if ($LASTEXITCODE -ne 0) { Write-Host "❌ git add 失败" -ForegroundColor Red; exit 1 }

# ── 4. 提交 ──────────────────────────────────────────────────────
git commit -m $CommitMsg
if ($LASTEXITCODE -ne 0) { Write-Host "❌ git commit 失败" -ForegroundColor Red; exit 1 }
Write-Host "✅ Commit：$CommitMsg" -ForegroundColor Green

# ── 5. Pull --rebase ─────────────────────────────────────────────
Write-Host "⬇️  Pull --rebase..." -ForegroundColor Yellow
git pull --rebase $Remote $Branch
if ($LASTEXITCODE -ne 0) { Write-Host "❌ git pull 失败，请手动解决冲突" -ForegroundColor Red; exit 1 }

# ── 6. Push ──────────────────────────────────────────────────────
Write-Host "🚀 推送到 GitHub..." -ForegroundColor Yellow
git push $Remote $Branch
if ($LASTEXITCODE -ne 0) { Write-Host "❌ git push 失败" -ForegroundColor Red; exit 1 }

Write-Host ""
Write-Host "✅ 推送成功！[$CommitMsg]" -ForegroundColor Green
Write-Host "🌐 https://github.com/yanfeiliuca/brickheroguide" -ForegroundColor Cyan
