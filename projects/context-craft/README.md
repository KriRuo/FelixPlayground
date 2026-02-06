# Context Craft 🎯

**AI-powered project context management**

Define your projects once, let agents understand them forever.

## What is this?

A simple system for storing structured project context that AI agents can read before working on something.

## Quick Start

```bash
# List all context blocks
python src/context.py list

# Show a specific project's context
python src/context.py show voice-to-clipboard

# Create a new context block
python src/context.py new my-project
```

## Context Block Structure

```yaml
---
id: project-id
name: Human-readable name
status: active | paused | done
updated: 2026-02-06
---

# Project Name

## Vision
What success looks like.

## Users  
Who it's for.

## Pain Points
Problems being solved.

## Requirements
What it must do.

## Constraints
Technical/business limits.

## Non-Goals
What it explicitly won't do.
```

## Status

🚧 **Work in progress** — Building the basics first.

---

*Part of Felixx's experiments*
