# Context Canvas AI Bridge — Analysis

*Reviewed by Felixx on 2026-02-06*

## What Kris Has Built

A **full web application** for managing project context with AI integration.

### Tech Stack
- **Frontend:** React + TypeScript + Vite + TailwindCSS + shadcn/ui
- **Whiteboard:** TLDraw (for visual canvas)
- **Backend:** Express.js with OpenAI integration
- **Database:** Supabase (PostgreSQL + vector embeddings)
- **Builder:** Lovable.dev (AI app builder)

### Core Data Model

```typescript
Context {
  id, name, description
  contextType: 'product' | 'project' | 'problem' | 'custom'
  blocks: ContextBlock[]
  systemPrompt?: string
  tenantId?: string  // Multi-tenant support
}

ContextBlock {
  id, title, content
  type: 'vision' | 'problem' | 'solution' | 'painpoint' | 
        'feature' | 'persona' | 'goal' | 'metric' | 'custom'
}
```

### Key Features

1. **Context Management**
   - Create contexts with typed blocks
   - Templates with suggested blocks
   - CRUD operations with localStorage + Supabase sync

2. **AI Integration**
   - `/api/whisper` — Voice transcription
   - `/api/interpret` — Convert voice to whiteboard shapes
   - `/api/generate-prompt` — Generate system prompts from context

3. **Multi-Tenant**
   - Tenant isolation
   - Per-tenant AI settings (model, temperature, etc.)

4. **Export**
   - Markdown format for humans
   - JSON format for AI consumption

---

## Comparison: My Prototype vs Kris's App

| Aspect | My Prototype | Kris's App |
|--------|--------------|------------|
| **Format** | Markdown files | Database + JSON |
| **UI** | CLI only | Full web UI |
| **Storage** | Local files | Supabase |
| **Block Types** | Freeform sections | Typed blocks (9 types) |
| **AI Integration** | None yet | OpenAI (Whisper + GPT-4) |
| **Multi-user** | No | Yes (tenants) |
| **Voice Input** | No | Yes |
| **Whiteboard** | No | Yes (TLDraw) |

---

## What I Can Add / Integrate

### 1. CLI Bridge
Make my CLI tool work with Kris's database:
```bash
# Sync local markdown ↔ Supabase
context sync

# Export context for AI agent use
context export voice-to-clipboard --format agent
```

### 2. Agent-Readable Format
Create an optimized export format specifically for AI agents:
```markdown
# CONTEXT: Voice to Clipboard
## VISION
[content]
## REQUIREMENTS  
[content]
## CONSTRAINTS
[content]
---
Use this context when working on this project.
```

### 3. Moltbot Skill
A skill that:
- Loads context before I work on a project
- Auto-injects relevant context into my prompts
- Updates context blocks based on our conversations

### 4. Context-Defining Agent
An agent persona that:
- Asks probing questions
- Extracts requirements from conversations
- Populates context blocks automatically

---

## POC Concept: "Context Loader" Skill

### Goal
Let me (Felixx) quickly load project context before working on something.

### Flow
```
Kris: "Work on the voice-to-clipboard project"
        ↓
Felixx: [reads context-canvas-ai-bridge DB or local cache]
        ↓
Felixx: "Got it. I see the context:
         - Vision: Local transcription tool
         - 6 must-have requirements
         - WSL2 + Windows constraint
         - No cloud, no AI responses
         Ready to help. What's the task?"
```

### Implementation Options

**Option A: Local Cache**
- Sync from Supabase to local markdown files
- Use my existing context.py to read them
- Fast, works offline

**Option B: Direct API**
- Query Supabase directly
- Always up-to-date
- Needs network

**Option C: Export Hook**
- Kris clicks "Export for Felixx" in the web app
- JSON/Markdown lands in my workspace
- Manual but simple

---

## Immediate Next Steps

1. [ ] Create a Supabase client for reading contexts
2. [ ] Build the "context loader" that injects into my prompts
3. [ ] Test with Voice-to-Clipboard project
4. [ ] Share working POC with Kris

---

## Questions for Kris

1. Do you want me to integrate directly with Supabase, or use file export?
2. Should I sync the existing context to your app, or keep them separate?
3. What's the Supabase project URL / do I need credentials?
