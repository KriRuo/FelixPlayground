# Context Craft — Project Plan

*Version 0.1 | Created: 2026-02-06 | Owner: Kris + Felixx*

---

## Vision
**The Context Layer for Agentic Development**

A place where users define project context (via web app), and AI agents know where to get it. Agents work like informed team members, not guessing machines.

---

## Target Users
- Solo developers working with AI coding tools
- Small teams collaborating with agents
- *Later: Enterprise/larger teams*

---

## Core Decisions

| Question | Decision |
|----------|----------|
| User interface | Web app |
| Storage | Cloud (Supabase) |
| Agent integration | TBD — safe, traceable |
| Open source? | TBD |

---

## Development Loop (PDCA/Ralph)

We'll work in **tight loops**:

```
┌─────────────────────────────────────────┐
│  PLAN → DO → CHECK → ADJUST → repeat   │
└─────────────────────────────────────────┘

1. PLAN   — Define what we're building (scope, acceptance criteria)
2. DO     — Build it (small increments)
3. CHECK  — Review together (does it work? is it right?)
4. ADJUST — Fix issues, update plan, next iteration
```

Each loop should be **1-4 hours max**. Ship small, learn fast.

---

## Quality Foundations

Before we code, we need:

### 1. ✅ Context Block (this project)
We'll eat our own dogfood — define Context Craft's context.

### 2. 📁 Repository Structure
```
context-craft/
├── README.md           # What is this, how to run
├── CONTEXT.md          # Project context (our own dogfood)
├── docs/
│   ├── architecture.md # System design
│   ├── decisions/      # ADRs (Architecture Decision Records)
│   └── api.md          # API documentation
├── src/
│   ├── web/            # React frontend
│   ├── api/            # Backend API
│   └── shared/         # Shared types/utils
├── tests/
└── scripts/
```

### 3. 🔧 Development Setup
- [ ] TypeScript (type safety)
- [ ] ESLint + Prettier (code consistency)
- [ ] Vitest or Jest (testing)
- [ ] GitHub Actions (CI/CD)
- [ ] Supabase (database + auth)

### 4. 📋 Definition of Done
A feature is "done" when:
- [ ] Code written and working
- [ ] Types defined (no `any`)
- [ ] Tests pass (if applicable)
- [ ] Reviewed by human (Kris)
- [ ] Documented (if user-facing)
- [ ] Committed with clear message

---

## Phases

### Phase 0: Foundation (Current)
**Goal:** Set up the project properly

- [x] Vision and target users defined
- [x] Project plan created
- [ ] Create CONTEXT.md (dogfooding)
- [ ] Set up repo structure
- [ ] Set up dev environment
- [ ] Define data model (final)

**Deliverable:** Clean repo ready for development

---

### Phase 1: Core Context Management
**Goal:** Users can create and view contexts

**Features:**
- [ ] Create a new context (name, description, type)
- [ ] Add blocks to a context
- [ ] Edit blocks
- [ ] Delete blocks
- [ ] View context in readable format
- [ ] List all contexts

**Tech:**
- Supabase for storage
- React + shadcn/ui for frontend
- Basic API routes

**Deliverable:** Working web app where user can manage contexts

---

### Phase 2: Agent Access
**Goal:** Agents can read contexts

**Features:**
- [ ] Public API endpoint: `GET /api/context/:id`
- [ ] API key authentication
- [ ] Rate limiting
- [ ] Agent-optimized export format
- [ ] Access logging (who read what, when)

**Options to explore:**
- MCP (Model Context Protocol) server
- Simple REST API
- GraphQL?
- Webhook notifications

**Deliverable:** Agents can fetch context via API

---

### Phase 3: Context Definition Assistant
**Goal:** AI helps users define context

**Features:**
- [ ] Chat interface for context creation
- [ ] AI asks clarifying questions
- [ ] Auto-generates context blocks from conversation
- [ ] Suggestions for missing context

**Deliverable:** Users don't write context from scratch — they have a conversation

---

### Phase 4: Integrations
**Goal:** Connect to where users already work

**Potential integrations:**
- [ ] GitHub (read README, issues, PRs)
- [ ] Linear (import requirements)
- [ ] Notion (sync pages)
- [ ] VS Code extension
- [ ] Cursor integration

**Deliverable:** Context stays in sync with existing tools

---

### Phase 5: Team & Collaboration
**Goal:** Teams share context

**Features:**
- [ ] Workspaces / organizations
- [ ] User roles (admin, editor, viewer)
- [ ] Context versioning
- [ ] Change history
- [ ] Comments / discussions

**Deliverable:** Teams collaborate on context

---

## Current Focus

**Phase 0: Foundation**

Next immediate steps:
1. Create CONTEXT.md for this project (dogfood)
2. Review existing code in context-canvas-ai-bridge
3. Decide: build on top of existing, or fresh start?
4. Set up clean repo structure

---

## Open Questions

1. **Build on existing code or fresh start?**
   - Existing has UI, Supabase, TLDraw
   - But might have tech debt / complexity
   
2. **What's the MVP scope?**
   - Phase 1 only?
   - Phase 1 + 2?

3. **Name?**
   - Context Craft?
   - Context Canvas?
   - Something else?

4. **Pricing model?**
   - Free tier + paid?
   - Open source + hosted?

---

*Ready to start Loop 1 of Phase 0!*
