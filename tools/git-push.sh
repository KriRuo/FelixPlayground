#!/bin/bash
# Git push helper - refreshes GitHub App token before pushing
# Usage: ./tools/git-push.sh [branch]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

cd "$REPO_DIR"

# Get fresh token
echo "🔐 Getting fresh token..."
TOKEN=$(python3 "$SCRIPT_DIR/github-auth.py" --token-only 2>/dev/null)

if [ -z "$TOKEN" ]; then
    echo "❌ Failed to get token"
    exit 1
fi

# Update remote URL with fresh token
git remote set-url origin "https://x-access-token:${TOKEN}@github.com/KriRuo/FelixPlayground"

# Push
BRANCH="${1:-main}"
echo "📤 Pushing to $BRANCH..."
git push origin "$BRANCH"

echo "✅ Done!"
