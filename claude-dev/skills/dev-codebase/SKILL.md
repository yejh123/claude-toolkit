---
name: dev-codebase
description: Generate a comprehensive, self-contained documentation of a codebase. Use when the user says "understand this codebase", "explain the project", "document the architecture", "how does this project work", "write a codebase overview", "onboard me to this repo", or any request to analyze and document a project's structure, architecture, data flow, or implementation details. Also use when the user opens a new unfamiliar repository.
source: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/understand-codebase
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Agent, Skill
---

# Understand Codebase

Generate a comprehensive Markdown document that fully explains a codebase. The output must be detailed enough for a new engineer to understand, run, modify, and debug the project without asking anyone else.

## Process

Follow these steps in order. Do NOT skip any step.

### Step 1: Scan the project

Read the project structure and key files to build a mental model:

1. Run `find . -type f -not -path './.git/*' -not -path './node_modules/*' -not -path './.venv/*' -not -path './venv/*' -not -path './__pycache__/*' -not -path './dist/*' -not -path './build/*' | head -200` to see the file tree.
2. Read configuration files first — they reveal the tech stack instantly:
   - `package.json`, `pyproject.toml`, `setup.py`, `requirements.txt`, `Cargo.toml`, `go.mod`, `Gemfile`, `pom.xml`, `build.gradle`
   - `Dockerfile`, `docker-compose.yml`, `.gitlab-ci.yml`, `.github/workflows/`
   - `.env.example`, `config/`, `settings.py`
3. Read the entrypoint(s): `main.py`, `app.py`, `index.ts`, `cmd/main.go`, `src/main.rs`, etc.
4. Read data models / schemas: `models/`, `schema/`, `migrations/`, `prisma/schema.prisma`, etc.
5. Read core business logic: `services/`, `handlers/`, `routes/`, `controllers/`.
6. Read tests to understand expected behavior: `tests/`, `test/`, `__tests__/`, `spec/`.

### Step 2: Write the document

Create a file named `CODEBASE.md` at the project root. Follow the template in `references/template.md` for structure. Every section is mandatory — if information is not applicable, explicitly state why.

### Step 3: Visualize

Include ASCII diagrams directly in the Markdown for:
- **Architecture diagram**: Show how major components connect.
- **Request/data flow**: Trace a typical operation end-to-end.
- **Data model / ER diagram**: Show entities and relationships.
- **Directory structure**: Annotated tree with purpose of each directory.

Use the diagramming patterns in `references/diagram-patterns.md`.

### Step 4: Annotate

Add inline annotations for:
- Non-obvious design decisions (WHY something is done a certain way).
- Potential pitfalls or gotchas a new developer might encounter.
- Performance-sensitive code paths.
- Security-relevant patterns (auth, input validation, secrets handling).

Use this format in code blocks:
```
# ⚠️ GOTCHA: This cache has no TTL — stale data persists until restart.
# 💡 DESIGN: We use a write-through cache here because read latency is critical.
# 🔒 SECURITY: Input is sanitized before reaching the SQL query.
```

### Step 5: Verify completeness

Before presenting the document, verify:
- [ ] Every directory in the project root is explained
- [ ] The tech stack table is complete (language, framework, database, etc.)
- [ ] At least one request/data flow is traced end-to-end
- [ ] Setup instructions are copy-paste runnable
- [ ] Environment variables are listed with descriptions
- [ ] Data models include field types and relationships
- [ ] Tests are documented (how to run, what they cover)
- [ ] Deployment process is described
- [ ] Diagrams are included (architecture + data flow minimum)

## Quality Standards

- **Self-contained**: A reader should need NOTHING else to understand the project.
- **Precise**: Use exact file paths, function names, class names. No vague references like "the main module".
- **Annotated**: Every non-obvious design choice gets a WHY comment.
- **Runnable**: All commands must be copy-paste ready. Include the shell, working directory, and expected output.
- **Visual**: At least 3 diagrams (architecture, data flow, data model). More is better.
- **Honest**: If something is unclear, messy, or undocumented in the codebase, say so explicitly rather than guessing.
