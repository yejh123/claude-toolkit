# Diagram Patterns

Use these ASCII patterns for diagrams in CODEBASE.md. Prefer ASCII art over Mermaid
because it renders universally (terminal, GitHub, GitLab, any editor).

## 1 Architecture Diagram

Show major components as boxes, connections as arrows with protocol labels.

```
┌─────────────┐     HTTPS/443    ┌──────────────┐     TCP/5432   ┌────────────┐
│   Client    │─────────────────▶│   API Server │──────────────▶│  Database  │
│  (Browser)  │◀─────────────────│   (FastAPI)  │◀──────────────│ (Postgres) │
└─────────────┘    JSON resp     └──────────────┘               └────────────┘
                                        │
                                        │ AMQP
                                        ▼
                                 ┌──────────────┐     TCP/6379   ┌────────────┐
                                 │ Task Worker  │──────────────▶│   Redis    │
                                 │  (Celery)    │               │  (Cache)   │
                                 └──────────────┘               └────────────┘
```

Rules:
- Boxes: `┌───┐ │ │ └───┘`
- Arrows: `──▶` (one-way), `◀──▶` (bidirectional)
- Label connections with protocol or data type
- Stack vertically for layered architectures, horizontally for pipelines

## 2 Request / Data Flow

Number each step. Show the path through code with file paths.

```
[1] POST /api/orders            ← Client sends HTTP request
       │
       ▼
[2] routes/orders.py            ← Route handler: validate input, extract user from JWT
    │  create_order(request)
    │
    ▼
[3] services/order_svc.py       ← Business logic: calculate total, apply discounts
    │  OrderService.create()
    │
    ▼
[4] models/order.py             ← ORM: INSERT INTO orders + order_items
    │  db.session.commit()
    │
    ▼
[5] tasks/email.py              ← Celery task queued (async, non-blocking)
    │  send_confirmation.delay()
    │
    ▼
[6] Response: 201 Created       ← JSON body returned to client
    { "order_id": 42 }
```

Rules:
- One step per layer (route → service → model → external)
- Include file path and function name
- Mark async operations explicitly
- Add arrow annotations for important context

## 3 Entity-Relationship Diagram

Show tables as boxes with fields. Use arrows for foreign keys.

```
┌──────────────────┐       ┌──────────────────┐
│      users       │       │     orders       │
├──────────────────┤       ├──────────────────┤
│ id          PK   │──┐    │ id          PK   │──┐
│ email       UQ   │  │    │ user_id     FK   │  │
│ name             │  └───▶│ status           │  │
│ role             │       │ total            │  │
│ created_at       │       │ created_at       │  │
└──────────────────┘       └──────────────────┘  │
                                                  │
                           ┌──────────────────┐   │
                           │   order_items    │   │
                           ├──────────────────┤   │
                           │ id          PK   │   │
                           │ order_id    FK   │◀──┘
                           │ product_id  FK   │
                           │ quantity         │
                           │ unit_price       │
                           └──────────────────┘
```

Rules:
- Mark PK (primary key), FK (foreign key), UQ (unique)
- Arrow FROM the "one" side TO the "many" side
- Group related tables visually

## 4 Layer / Stack Diagram

Show the layered architecture from top (user-facing) to bottom (infrastructure).

```
┌─────────────────────────────────────────────┐
│              Presentation Layer              │
│   routes/, templates/, static/               │
│   (HTTP handling, request/response format)   │
├─────────────────────────────────────────────┤
│              Business Logic Layer            │
│   services/                                  │
│   (Domain rules, validation, orchestration)  │
├─────────────────────────────────────────────┤
│              Data Access Layer               │
│   models/, repositories/                     │
│   (ORM queries, data mapping)                │
├─────────────────────────────────────────────┤
│              Infrastructure Layer            │
│   config/, utils/, tasks/                    │
│   (DB connections, cache, email, queues)     │
└─────────────────────────────────────────────┘
```

## 5 Directory Tree

Annotate every entry. Use standard tree characters.

```
project/
├── app/                      # Application source code
│   ├── __init__.py           # App factory: create_app()
│   ├── models/               # SQLAlchemy models
│   │   ├── __init__.py       # Registers all models for Alembic
│   │   ├── user.py           # User: auth, profile, roles
│   │   └── order.py          # Order + OrderItem: purchases
│   ├── services/             # Business logic (no HTTP, no DB imports)
│   │   ├── auth_service.py   # Login, token generation, password hashing
│   │   └── order_service.py  # Order creation, pricing, status updates
│   ├── routes/               # Flask blueprints
│   │   ├── auth.py           # POST /login, POST /register
│   │   └── orders.py         # CRUD /api/v1/orders
│   └── utils/                # Pure helpers (no side effects)
│       ├── validators.py     # Input validation functions
│       └── formatters.py     # Date/currency formatting
├── tests/                    # Mirrors app/ structure
├── migrations/               # Alembic auto-generated migrations
├── Dockerfile                # Multi-stage: build → production
├── docker-compose.yml        # Local dev: app + postgres + redis
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Test + lint dependencies
└── .gitlab-ci.yml            # CI/CD pipeline definition
```

Rules:
- `├──` for middle items, `└──` for last item in a group
- `│   ` for vertical continuation
- Every file/directory gets a `# comment` explaining its purpose
- Group by function, not alphabetically

## 6 State Machine

Use for entities with lifecycle states (orders, payments, deployments).

```
                    create
         ┌──────────────────────────┐
         ▼                          │
    ┌─────────┐    pay     ┌───────────┐    ship     ┌───────────┐
    │ pending │───────────▶│   paid    │────────────▶│  shipped  │
    └─────────┘            └───────────┘             └───────────┘
         │                       │                         │
         │ cancel                │ refund                  │ deliver
         ▼                       ▼                         ▼
    ┌─────────┐            ┌───────────┐             ┌───────────┐
    │cancelled│            │ refunded  │             │ delivered │
    └─────────┘            └───────────┘             └───────────┘
```

## 7 Pipeline / Workflow

```
┌───────┐    ┌───────┐    ┌───────┐    ┌─────────┐    ┌────────┐
│ lint  │───▶│ test  │───▶│ build │───▶│ staging │───▶│  prod  │
│       │    │       │    │       │    │ (auto)  │    │(manual)│
└───────┘    └───────┘    └───────┘    └─────────┘    └────────┘
  flake8      pytest       docker       deploy.sh     deploy.sh
  black       coverage     push         curl /health  blue-green
```

## Box-Drawing Character Reference

```
Corners:  ┌ ┐ └ ┘
Lines:    ─ │
T-joints: ├ ┤ ┬ ┴
Cross:    ┼
Arrows:   ▶ ◀ ▲ ▼ → ← ↑ ↓
Heavy:    ┏ ┓ ┗ ┛ ━ ┃
```
