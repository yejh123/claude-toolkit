---
name: dev-product-spec
description: Generate a comprehensive Product Specification document for a software product or feature. Use when the user says "write a product spec", "create a PRD", "product requirements document", "spec out this feature", "define the product", "write requirements", "product specification", or any request to formally define what a software product or feature should do, who it's for, how it works technically, and how success is measured.
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Agent, Skill
---

# Product Specification

Generate a complete, engineering-ready Product Specification document. This is NOT a lightweight PRD — it is a detailed specification that bridges product strategy and engineering implementation. It must contain enough detail for an engineer to start building and a QA engineer to start writing test cases without asking follow-up questions.

## When to use this vs. other documents

- **Product Spec (this skill)**: Detailed WHAT + HOW. Includes technical architecture, data models, API contracts, state machines, and acceptance criteria. The primary audience is engineering + design + QA.
- **PRD (Product Requirements Document)**: High-level WHAT + WHY. Focuses on user problems, personas, success metrics. The primary audience is stakeholders + product leadership.
- **Technical Design Doc**: Deep HOW. Focuses on implementation approach, algorithm choices, performance tradeoffs. The primary audience is engineering only.

This skill produces a Product Spec — it includes the strategic context of a PRD AND the technical depth needed by engineering.

## Process

### Step 1: Gather context

Before writing anything, understand the product/feature by asking the user or reading available materials:

1. What problem does this solve? For whom?
2. Is there an existing codebase? If yes, scan it using the project structure, models, routes, and config files.
3. Are there existing PRDs, design mockups, or Slack threads with context?
4. What is the current tech stack?
5. Are there hard constraints (timeline, budget, regulatory, backward compatibility)?

If the user provides vague requirements, ask clarifying questions BEFORE generating the spec. Do not guess — ambiguity in a spec propagates as bugs in code.

### Step 2: Write the specification

Create a file named `PRODUCT_SPEC.md` (or `PRODUCT_SPEC_{feature_name}.md` for feature-level specs). Follow the template in `references/template.md`.

Every section is mandatory. If a section does not apply, state why explicitly.

### Step 3: Add diagrams

Include ASCII diagrams for:
- **System architecture**: How components connect (frontend, backend, DB, external APIs)
- **User flow**: Step-by-step path through the feature (decision points as diamonds)
- **Data model / ER diagram**: Entities with fields, types, and relationships
- **State machine**: For any entity with lifecycle states (orders, subscriptions, deployments)
- **API sequence diagram**: Request/response flow for key interactions

Use the patterns in `references/diagram-patterns.md`.

### Step 4: Define acceptance criteria

Every functional requirement MUST have testable acceptance criteria in Given/When/Then format:

```
**AC-1**: Given a logged-in user with items in cart,
          When they click "Place Order" and payment succeeds,
          Then an order is created with status "confirmed",
          And a confirmation email is sent within 60 seconds,
          And the inventory count is decremented.
```

### Step 5: Annotate critical sections

Add inline annotations for:
- `📌 DECISION`: Records a product decision with rationale (so future readers know WHY)
- `⚠️ RISK`: Flags a risk with mitigation strategy
- `🔒 SECURITY`: Marks security-sensitive requirements
- `📊 METRIC`: Identifies a measurable success indicator
- `🚫 OUT OF SCOPE`: Explicitly excludes something to prevent scope creep
- `💡 FUTURE`: Notes a deliberate deferral for a future iteration

### Step 6: Verify completeness

Before presenting, verify against this checklist:
- [ ] Problem statement is specific and evidence-based
- [ ] Target users/personas are defined with behaviors, not just demographics
- [ ] Success metrics are quantifiable with baseline and target values
- [ ] Every user story has acceptance criteria in Given/When/Then
- [ ] Requirements are prioritized (P0/P1/P2)
- [ ] Data model includes all fields with types and constraints
- [ ] API endpoints are listed with methods, paths, request/response schemas
- [ ] State transitions are defined for stateful entities
- [ ] Non-functional requirements have measurable thresholds
- [ ] At least 3 diagrams are included (architecture, user flow, data model)
- [ ] Security and privacy considerations are addressed
- [ ] Dependencies on other teams/systems are listed
- [ ] Open questions are captured (not silently ignored)
- [ ] Out-of-scope items are explicitly stated

## Quality Standards

- **Precise**: Use exact field names, endpoint paths, status codes. No hand-waving.
- **Testable**: Every requirement must be verifiable. If QA can't write a test for it, it's not a requirement — it's a wish.
- **Prioritized**: P0 = launch blocker, P1 = needed for adoption, P2 = nice-to-have. Be ruthless.
- **Visual**: Diagrams are mandatory, not optional. Engineers think in diagrams.
- **Honest**: Flag unknowns as open questions rather than making assumptions. A spec that acknowledges what it doesn't know is more trustworthy than one that pretends to know everything.
- **Living**: Include a change log section so the spec can evolve without losing history.
