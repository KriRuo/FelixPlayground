---
id: context-craft
name: Context Craft
status: active
updated: 2026-02-06
type: product
owner: Kris
---

# Context Craft

## Vision
The Context Layer for Agentic Development.

A web app where users define project context, and AI agents know where to get it. Agents become informed team members who understand what to build and why.

**Success looks like:** An AI coding agent reads the context and just *knows* what to work on — like a human teammate who's been on the project for months.

## Users
- **Primary:** Solo developers using AI coding tools (Claude Code, Cursor, Copilot)
- **Secondary:** Small development teams collaborating with agents
- **Future:** Enterprise teams

## Pain Points
1. **Context evaporates** — Every AI session starts from zero, users re-explain constantly
2. **Agents guess wrong** — Without context, AI makes assumptions that waste time
3. **Context is scattered** — Lives in heads, Slack, tickets, outdated docs
4. **No standard exists** — No "context protocol" for agents to consume
5. **Onboarding is painful** — New team members (human or AI) take forever to get up to speed

## Requirements

### Must Have (MVP)
- [ ] Web app to create/edit contexts
- [ ] Block-based context structure (vision, requirements, constraints, etc.)
- [ ] API for agents to read context
- [ ] Authentication (who can access what)
- [ ] Cloud storage (Supabase)

### Should Have
- [ ] Context templates (product, project, problem)
- [ ] AI assistant for context creation
- [ ] Access logging (who read what, when)
- [ ] Export as Markdown/JSON

### Won't Have (v1)
- Enterprise features (SSO, audit logs)
- Real-time collaboration
- Integrations with external tools
- Mobile app
- Self-hosted option

## Constraints
- **Tech stack:** TypeScript, React, Supabase
- **Timeline:** MVP in 2-4 weeks
- **Team:** Kris (human) + Felixx (AI) — async collaboration
- **Budget:** Minimal — use free tiers where possible

## User Journey (Agent Integration)

```
1. Developer creates a project in Context Craft
2. Adds context blocks: vision, requirements, constraints
3. Gets an API endpoint: api.contextcraft.dev/ctx/abc123
4. Tells their AI agent: "Use this context: [link]"
5. Agent fetches context before starting work
6. Agent builds the right thing, first time
```

## Non-Goals
- NOT a project management tool (no tasks, sprints, timelines)
- NOT a documentation system (no wikis, full docs)
- NOT a requirements tool (no traceability matrices, approvals)
- NOT replacing existing tools — complementing them

## Technical Architecture (Draft)

```
┌─────────────────────────────────────────────────────────┐
│                    WEB APP (React)                      │
│   - Create/edit contexts                                │
│   - View context blocks                                 │
│   - Manage API access                                   │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│                    API (Express/Edge)                   │
│   - CRUD operations                                     │
│   - Agent access endpoint                               │
│   - Authentication                                      │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│                    SUPABASE                             │
│   - PostgreSQL (contexts, blocks, users)                │
│   - Auth (user authentication)                          │
│   - Edge Functions (API routes)                         │
└─────────────────────────────────────────────────────────┘
```

## Success Metrics
- Users can create a context in < 5 minutes
- Agents can fetch context in < 500ms
- Users report agents "getting it right" more often
- Returning users (people actually use it)

## Risks
1. **Adoption** — People might not bother to write context
   - Mitigation: AI assistant makes it effortless
2. **Format wars** — Different agents want different formats
   - Mitigation: Support multiple export formats
3. **Stale context** — Users don't update
   - Mitigation: Reminders, easy editing, auto-extraction

---

*This context block describes Context Craft itself. Dogfooding FTW.*
