# Project Plan Template

Fill in every section below using the requirements gathered during the interview phases.

## 1. Project Overview

**Project Name**: [name]

**Problem Statement**: [1-2 sentences describing the problem this project solves]

**Target Users**: [who will use this, their technical level]

**Success Criteria**: [how do we know the project is successful]

## 2. Requirements

### Functional Requirements

List the core features as user stories:

- As a [user], I want to [action] so that [benefit]
- ...

### Non-Functional Requirements

| Requirement | Target |
|-------------|--------|
| Availability | [e.g., 99.9%] |
| Latency | [e.g., p95 < 200ms] |
| Throughput | [e.g., 1000 req/s] |
| Data retention | [e.g., 90 days] |
| Compliance | [e.g., GDPR, HIPAA, none] |

## 3. Architecture

### System Components

List the major components and their responsibilities:

1. **[Component]**: [what it does]
2. ...

### Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Language | [e.g., Python 3.12] | [why] |
| Framework | [e.g., FastAPI] | [why] |
| Database | [e.g., PostgreSQL] | [why] |
| Cache | [e.g., Redis] | [why] |
| Deployment | [e.g., Docker + AWS ECS] | [why] |

### Data Model

Describe the core entities and their relationships:

- **[Entity]**: [key fields, relationships]
- ...

## 4. API Design

List the primary endpoints or interfaces:

| Method | Path | Description |
|--------|------|-------------|
| POST | /resource | Create |
| GET | /resource/{id} | Read |
| ... | ... | ... |

## 5. Project Structure

```
project-name/
├── src/
├── tests/
├── docs/
├── ...
└── README.md
```

## 6. Implementation Plan

### Phase 1: Foundation
- [ ] Project setup, CI/CD, basic structure
- [ ] Core data models and database schema
- [ ] Authentication (if applicable)

### Phase 2: Core Features
- [ ] [Feature 1]
- [ ] [Feature 2]
- [ ] ...

### Phase 3: Polish
- [ ] Error handling and edge cases
- [ ] Testing (unit + integration)
- [ ] Documentation
- [ ] Deployment configuration

## 7. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| [risk] | [high/medium/low] | [how to address] |

## 8. Open Questions

- [Any unresolved decisions or areas needing further research]
