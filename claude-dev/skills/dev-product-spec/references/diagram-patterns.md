# Diagram Patterns for Product Specifications

Use ASCII art for all diagrams. It renders universally and lives inside the Markdown
file without external dependencies.

## 1 System Architecture

Show components as boxes, connections with protocol/data labels.

```
┌─────────────┐     HTTPS      ┌──────────────┐     SQL       ┌────────────┐
│   Client    │────────────────▶│  API Server  │─────────────▶│  Database  │
│  (React)    │◀────────────────│  (FastAPI)   │◀─────────────│ (Postgres) │
└─────────────┘   JSON          └──────────────┘              └────────────┘
                                       │
                                       │ AMQP
                                       ▼
                                ┌──────────────┐    SMTP      ┌───────────┐
                                │ Task Worker  │─────────────▶│ SendGrid  │
                                │  (Celery)    │              └───────────┘
                                └──────────────┘
```

## 2 User Flow (with decision points)

Decision points as diamonds. Annotate each step.

```
┌───────────┐
│  Landing  │
│   page    │
└─────┬─────┘
      │
      ▼
 ┌──────────┐     No     ┌────────────┐
 │ Logged   │────────────▶│  Login /   │
 │   in?    │             │  Register  │
 └────┬─────┘             └──────┬─────┘
      │ Yes                      │
      ▼                          │
┌───────────┐◀───────────────────┘
│ Dashboard │
└─────┬─────┘
      │ Click "New Order"
      ▼
┌───────────┐
│  Select   │
│ products  │
└─────┬─────┘
      │
      ▼
 ┌──────────┐     No     ┌────────────┐
 │  Cart    │────────────▶│  Continue  │
 │ empty?   │             │  shopping  │
 └────┬─────┘             └────────────┘
      │ Has items
      ▼
┌───────────┐
│ Checkout  │──── Payment ────▶ ┌─────────┐
│           │                   │ Stripe  │
└─────┬─────┘◀── Confirm ─────│  (PCI)  │
      │                        └─────────┘
      ▼
 ┌──────────┐    Fail     ┌────────────┐
 │ Payment  │────────────▶│  Retry /   │
 │ success? │             │  Support   │
 └────┬─────┘             └────────────┘
      │ Yes
      ▼
┌───────────┐
│  Order    │
│ confirmed │
└───────────┘
```

## 3 Entity-Relationship Diagram

Tables as boxes. PK/FK/UQ annotations. Arrows show relationships.

```
┌──────────────────┐       ┌───────────────────┐       ┌──────────────────┐
│      users       │       │      orders       │       │   order_items    │
├──────────────────┤       ├───────────────────┤       ├──────────────────┤
│ id        PK     │──┐    │ id        PK      │──┐    │ id        PK     │
│ email     UQ     │  │    │ user_id   FK      │  │    │ order_id  FK     │
│ name             │  └──1▶│ status    ENUM    │  └─N▶│ product_id FK    │
│ password_hash    │       │ total     DECIMAL │       │ quantity  INT    │
│ created_at       │       │ created_at        │       │ unit_price DEC   │
└──────────────────┘       └───────────────────┘       └──────────────────┘
```

Cardinality notation: `──1▶` (one), `──N▶` (many), `──1..N▶` (one-to-many)

## 4 State Machine

For entities with lifecycle (orders, payments, subscriptions, tickets).

```
                      create
         ┌──────────────────────────┐
         ▼                          │
    ┌─────────┐    pay     ┌───────────┐    ship     ┌───────────┐
    │ pending │───────────▶│ confirmed │────────────▶│  shipped  │
    └─────────┘            └───────────┘             └───────────┘
         │                       │                         │
         │ cancel                │ refund                  │ deliver
         ▼                       ▼                         ▼
    ┌─────────┐            ┌───────────┐             ┌───────────┐
    │cancelled│            │ refunded  │             │ delivered │
    └─────────┘            └───────────┘             └───────────┘
```

Always accompany with a transition table.

## 5 Sequence Diagram

For API interactions and multi-service flows.

```
Client           API Server        Database        External API
  │                  │                │                  │
  │  POST /orders    │                │                  │
  │─────────────────▶│                │                  │
  │                  │ INSERT order   │                  │
  │                  │───────────────▶│                  │
  │                  │◀──────────────│                  │
  │                  │                │                  │
  │                  │ Create payment │                  │
  │                  │───────────────────────────────────▶│
  │                  │◀──────────────────────────────────│
  │  201 Created     │                │                  │
  │◀─────────────────│                │                  │
```

## 6 Wireframe (UI mockup)

For screen layouts. Use box-drawing for structure.

```
┌────────────────────────────────────────────────┐
│  ☰  My Store                    🔔  👤 Sarah  │  ← Header
├────────────────────────────────────────────────┤
│                                                │
│  📦 Orders (3)                   [+ New Order] │  ← Page title + CTA
│                                                │
│  🔍 Search...        Status: [All ▼]          │  ← Filters
│                                                │
│  ┌────────────────────────────────────────┐    │
│  │ #1042  │ Feb 20  │ ✅ Delivered │ $62 │ ▶ │  │  ← Order row
│  ├────────────────────────────────────────┤    │
│  │ #1039  │ Feb 18  │ 🚚 Shipped  │ $30 │ ▶ │  │
│  ├────────────────────────────────────────┤    │
│  │ #1035  │ Feb 15  │ ❌ Cancelled │  $0 │ ▶ │  │
│  └────────────────────────────────────────┘    │
│                                                │
│              < Page 1 of 3 >                   │  ← Pagination
│                                                │
└────────────────────────────────────────────────┘
```

## 7 Pipeline / Timeline

For CI/CD, rollout phases, or project milestones.

```
Week 1          Week 2-3        Week 4          Week 5-6        Week 7
┌──────┐       ┌──────────┐    ┌──────┐       ┌──────────┐    ┌──────┐
│ Spec │──────▶│ Backend  │───▶│ QA   │──────▶│  Beta    │───▶│  GA  │
│Review│       │ + Front  │    │      │       │ (5% users│    │      │
└──────┘       └──────────┘    └──────┘       └──────────┘    └──────┘
```

## Box-Drawing Reference

```
Corners:  ┌ ┐ └ ┘        Arrows:  ▶ ◀ ▲ ▼ → ← ↑ ↓
Lines:    ─ │              Bullets: • ◦ ▪ ▫
T-joints: ├ ┤ ┬ ┴        Checks:  ✅ ❌ ⚠️ 🔒
Cross:    ┼                Icons:   📦 🔍 📊 💡 📌
Diamond:  Use text: <decision?>     Heavy:   ━ ┃ ┏ ┓ ┗ ┛
```
