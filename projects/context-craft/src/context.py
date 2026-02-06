#!/usr/bin/env python3
"""
Context Craft - Simple context block manager for AI agents

Usage:
    python context.py list                    # List all context blocks
    python context.py show <project-id>       # Show a project's context
    python context.py new <project-id>        # Create new context block
    python context.py summary <project-id>    # Get a brief summary
"""

import argparse
import os
import re
import sys
from pathlib import Path
from datetime import date

# Default context directory
CONTEXT_DIR = Path(__file__).parent.parent / "context"

TEMPLATE = '''---
id: {id}
name: {name}
status: active
updated: {date}
---

# {name}

## Vision
*What does success look like?*

## Users
*Who is this for?*

## Pain Points
*What problems are we solving?*

1. 

## Requirements

### Must Have
- [ ] 

### Should Have
- [ ] 

### Won't Have (this version)
- 

## Constraints
*Technical, business, or time limits*

- 

## Non-Goals
*What this explicitly won't do*

- 

## Notes
*Anything else relevant*

'''


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    frontmatter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()
    
    return frontmatter, parts[2].strip()


def list_contexts(context_dir: Path) -> list[dict]:
    """List all context blocks."""
    contexts = []
    
    if not context_dir.exists():
        return contexts
    
    for file in context_dir.glob('*.md'):
        content = file.read_text()
        meta, _ = parse_frontmatter(content)
        meta['file'] = file.name
        contexts.append(meta)
    
    return contexts


def show_context(context_dir: Path, project_id: str) -> str | None:
    """Get the full content of a context block."""
    file_path = context_dir / f"{project_id}.md"
    
    if not file_path.exists():
        # Try to find by id in frontmatter
        for file in context_dir.glob('*.md'):
            content = file.read_text()
            meta, _ = parse_frontmatter(content)
            if meta.get('id') == project_id:
                return content
        return None
    
    return file_path.read_text()


def get_summary(context_dir: Path, project_id: str) -> str | None:
    """Get a brief summary of a context block."""
    content = show_context(context_dir, project_id)
    if not content:
        return None
    
    meta, body = parse_frontmatter(content)
    
    # Extract vision section
    vision_match = re.search(r'## Vision\s*\n(.*?)(?=\n##|\Z)', body, re.DOTALL)
    vision = vision_match.group(1).strip() if vision_match else "No vision defined"
    
    # Extract first few requirements
    reqs_match = re.search(r'### Must Have\s*\n(.*?)(?=\n###|\n##|\Z)', body, re.DOTALL)
    reqs = reqs_match.group(1).strip()[:200] if reqs_match else "No requirements"
    
    return f"""**{meta.get('name', project_id)}** ({meta.get('status', 'unknown')})

**Vision:** {vision[:200]}...

**Key Requirements:**
{reqs}
"""


def create_context(context_dir: Path, project_id: str, name: str = None) -> Path:
    """Create a new context block from template."""
    context_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = context_dir / f"{project_id}.md"
    
    if file_path.exists():
        raise FileExistsError(f"Context block already exists: {file_path}")
    
    name = name or project_id.replace('-', ' ').title()
    content = TEMPLATE.format(
        id=project_id,
        name=name,
        date=date.today().isoformat()
    )
    
    file_path.write_text(content)
    return file_path


def main():
    parser = argparse.ArgumentParser(description="Context Craft - Manage project context blocks")
    parser.add_argument('--dir', type=Path, default=CONTEXT_DIR, help="Context directory")
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # List command
    subparsers.add_parser('list', help='List all context blocks')
    
    # Show command
    show_parser = subparsers.add_parser('show', help='Show a context block')
    show_parser.add_argument('project_id', help='Project ID')
    
    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Get brief summary')
    summary_parser.add_argument('project_id', help='Project ID')
    
    # New command
    new_parser = subparsers.add_parser('new', help='Create new context block')
    new_parser.add_argument('project_id', help='Project ID')
    new_parser.add_argument('--name', help='Human-readable name')
    
    args = parser.parse_args()
    
    if args.command == 'list':
        contexts = list_contexts(args.dir)
        if not contexts:
            print("No context blocks found.")
            print(f"Create one with: python context.py new <project-id>")
            return
        
        print(f"📦 Context blocks ({len(contexts)}):\n")
        for ctx in contexts:
            status = ctx.get('status', '?')
            status_emoji = {'active': '🟢', 'paused': '🟡', 'done': '✅'}.get(status, '⚪')
            print(f"  {status_emoji} {ctx.get('id', ctx['file'])} - {ctx.get('name', 'Unnamed')}")
    
    elif args.command == 'show':
        content = show_context(args.dir, args.project_id)
        if content:
            print(content)
        else:
            print(f"❌ Context block not found: {args.project_id}")
            sys.exit(1)
    
    elif args.command == 'summary':
        summary = get_summary(args.dir, args.project_id)
        if summary:
            print(summary)
        else:
            print(f"❌ Context block not found: {args.project_id}")
            sys.exit(1)
    
    elif args.command == 'new':
        try:
            path = create_context(args.dir, args.project_id, args.name)
            print(f"✅ Created: {path}")
            print(f"Edit it to add your project context!")
        except FileExistsError as e:
            print(f"❌ {e}")
            sys.exit(1)
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
