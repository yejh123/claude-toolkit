---
name: dev-plan
description: "Plans a new software project by gathering requirements through structured questions before producing a plan. Use when the user says 'I want to build', 'help me plan', 'design a system', 'start a new project', or needs to scope and architect a software project. Triggers on: plan a project, design a system, build an app, system design, architecture, project planning, I want to build."
metadata:
  version: "1.0"
  last_updated: "2026-03-19"
---

# Dev Plan — Project Planning

Plans a new software project by gathering requirements through structured questions before producing a plan. Prevents premature implementation by ensuring all critical requirements are captured first.

## Quick Start

```
I want to build a task management API
Help me plan a real-time chat application
Design a system for processing research papers
Start a new project for data pipeline automation
```

## Trigger Conditions

**Triggers on**: plan a project, design a system, build an app, system design, architecture, project planning, I want to build, help me plan, scope a project, start a new project

**Does NOT trigger on**:
- Debugging existing code → use `dev-workflow`
- Reviewing code quality → use `dev-review`
- Writing FastAPI endpoints → use `dev-api`
- Writing a paper → use `paper-write`

## Critical Rule

```
DO NOT start building or designing until all phases are complete.
```

No code, no architecture diagrams, no technology choices until requirements are fully gathered. Premature design leads to rework.

## Phase 1 — Problem Discovery

Ask these questions **one at a time**. Wait for each answer before proceeding to the next.

**Q1**: "What problem does this project solve for its users?"
- Understand the core value proposition
- Clarify who benefits and how

**Q2**: "Who are the primary users? What is their technical level?"
- Identify user personas
- Understand technical sophistication (developers, non-technical users, mixed)

**Q3**: "What is the expected scale? (users per day, data volume, request rate)"
- Distinguish hobby project from production system
- Inform architecture decisions (monolith vs microservices, DB choice)

## Phase 2 — Technical Constraints

Only proceed after Phase 1 is fully answered.

**Q4**: "What deployment environment will you use?"
- Cloud provider, on-premise, local development only
- Container orchestration requirements
- CI/CD expectations

**Q5**: "Do you have any technology stack requirements or preferences?"
- Language, framework, database preferences
- Existing systems to integrate with
- Team expertise constraints

**Q6**: "What are the non-negotiable requirements? (latency, uptime, compliance, budget)"
- SLA requirements
- Regulatory constraints (GDPR, HIPAA)
- Budget limitations
- Timeline

## Phase 3 — Synthesis

Only proceed after all questions are answered.

1. Load `assets/plan-template.md` for the output format
2. Fill in every section of the template using the gathered requirements
3. Present the completed plan to the user
4. Ask: "Does this plan accurately capture your requirements? What would you change?"
5. Iterate on feedback until the user confirms

## Conversation Guidelines

- **One question at a time**: Don't overwhelm with all questions at once
- **Acknowledge answers**: Briefly confirm understanding before moving to the next question
- **Probe vague answers**: If an answer is too vague, ask a follow-up before proceeding
- **Skip what's irrelevant**: If a question clearly doesn't apply (e.g., scale for a personal script), acknowledge and move on
- **Summarize before synthesis**: After all questions, summarize gathered requirements and confirm before writing the plan
