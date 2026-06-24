#!/bin/bash
# BrickHeroGuide — git cleanup + commit + push
# Run from Terminal: bash auto-push.sh

set -e
cd "$(dirname "$0")"

echo "🧹 Clearing stale lock files..."
find .git -name "*.lock" -delete 2>/dev/null || true

echo "🔁 Aborting stuck rebase (if any)..."
git rebase --abort 2>/dev/null || true

echo "📦 Staging all changes..."
git add -A

echo "💾 Committing..."
git commit -m "Daily update: blog + guide audit 2026-06-24 (run 2)"

echo "🚀 Pushing to origin/main..."
git push origin main

echo "✅ Done!"
