#!/usr/bin/env python3
"""
GitHub App Authentication for Felixx 🦊

This script authenticates as a GitHub App and provides an access token
for interacting with repositories.

Usage:
    python github-auth.py              # Get an access token
    python github-auth.py --test       # Test authentication and list repos
    python github-auth.py --clone URL  # Clone a repo using the token
"""

import json
import time
import subprocess
import sys
from pathlib import Path

# Configuration
APP_ID = "2806919"
INSTALLATION_ID = "108340895"
PRIVATE_KEY_PATH = Path.home() / ".moltbot" / "github-app.pem"

def check_dependencies():
    """Check if required packages are installed."""
    try:
        import jwt
        import requests
        return True
    except ImportError as e:
        print(f"Missing dependency: {e.name}")
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyJWT", "requests", "cryptography"])
        return True

def create_jwt(app_id: str, private_key: str) -> str:
    """Create a JWT for GitHub App authentication."""
    import jwt
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend
    
    # Load the private key properly
    key = serialization.load_pem_private_key(
        private_key.encode(),
        password=None,
        backend=default_backend()
    )
    
    now = int(time.time())
    payload = {
        "iat": now - 60,  # Issued 60 seconds ago (clock skew tolerance)
        "exp": now + (10 * 60),  # Expires in 10 minutes
        "iss": app_id,
    }
    
    return jwt.encode(payload, key, algorithm="RS256")

def get_installation_token(jwt_token: str, installation_id: str) -> dict:
    """Exchange JWT for an installation access token."""
    import requests
    
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_accessible_repos(token: str) -> list:
    """List repositories accessible to the installation."""
    import requests
    
    url = "https://api.github.com/installation/repositories"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("repositories", [])

def clone_repo(token: str, repo_url: str, target_dir: str = None):
    """Clone a repository using the token."""
    # Convert HTTPS URL to authenticated URL
    if repo_url.startswith("https://github.com/"):
        auth_url = repo_url.replace("https://github.com/", f"https://x-access-token:{token}@github.com/")
    else:
        auth_url = repo_url
    
    if target_dir:
        subprocess.run(["git", "clone", auth_url, target_dir], check=True)
    else:
        subprocess.run(["git", "clone", auth_url], check=True)

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="GitHub App Authentication")
    parser.add_argument("--test", action="store_true", help="Test auth and list accessible repos")
    parser.add_argument("--clone", metavar="URL", help="Clone a repo using the token")
    parser.add_argument("--token-only", action="store_true", help="Just print the token")
    parser.add_argument("--save", metavar="PATH", help="Save token to file")
    args = parser.parse_args()
    
    # Check dependencies
    check_dependencies()
    
    # Read private key
    if not PRIVATE_KEY_PATH.exists():
        print(f"❌ Private key not found at {PRIVATE_KEY_PATH}")
        sys.exit(1)
    
    private_key = PRIVATE_KEY_PATH.read_text()
    
    # Create JWT
    print("🔐 Creating JWT...")
    jwt_token = create_jwt(APP_ID, private_key)
    
    # Get installation token
    print("🎫 Getting installation access token...")
    token_response = get_installation_token(jwt_token, INSTALLATION_ID)
    access_token = token_response["token"]
    expires_at = token_response["expires_at"]
    
    if args.token_only:
        print(access_token)
        return
    
    if args.save:
        Path(args.save).write_text(access_token)
        print(f"✅ Token saved to {args.save}")
        return
    
    print(f"✅ Got access token (expires: {expires_at})")
    
    if args.test:
        print("\n📦 Accessible repositories:")
        repos = get_accessible_repos(access_token)
        if repos:
            for repo in repos:
                print(f"  - {repo['full_name']} ({repo['html_url']})")
        else:
            print("  (no repositories accessible)")
    
    if args.clone:
        print(f"\n📥 Cloning {args.clone}...")
        clone_repo(access_token, args.clone)
        print("✅ Clone complete!")
    
    if not args.test and not args.clone:
        print("\n💡 Usage:")
        print("  --test        List accessible repositories")
        print("  --clone URL   Clone a repository")
        print("  --token-only  Just print the token")
        print(f"\n🔑 Token (valid until {expires_at}):")
        print(f"  {access_token[:20]}...{access_token[-10:]}")

if __name__ == "__main__":
    main()
