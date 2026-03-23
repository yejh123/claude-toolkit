# Product Specification Template

Use this template for the output document. Every section is mandatory.
Adapt depth to the scope (full product vs. single feature), but never remove sections.

---

```markdown
# {Product/Feature Name} — Product Specification

| Field | Value |
|-------|-------|
| **Document owner** | {Name, Role} |
| **Status** | Draft / In Review / Approved / Archived |
| **Version** | v0.1 |
| **Created** | {YYYY-MM-DD} |
| **Last updated** | {YYYY-MM-DD} |
| **Reviewers** | {Engineering Lead, Design Lead, QA Lead} |
| **Target release** | {Quarter or date} |

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v0.1 | {date} | {author} | Initial draft |

---

## 1 Executive Summary

One paragraph: what is being built, why, and the expected impact. This is the
"elevator pitch" — a reader should understand the initiative in 30 seconds.

> 📌 DECISION: {Record any key framing decisions made here, e.g., "We chose to
> build this as a standalone microservice rather than extending the monolith
> because..."}

---

## 2 Problem Statement

### 2.1 Background

What is the current situation? What are users doing today? What pain do they
experience? Support with data wherever possible (support tickets, analytics,
user research quotes).

### 2.2 Problem Definition

State the problem clearly. Use this format:

> **{Target user}** needs a way to **{accomplish goal}** because **{reason/pain
> point}**, but currently **{obstacle/limitation}**.

### 2.3 Evidence

| Evidence type | Source | Key finding |
|---------------|--------|-------------|
| Support tickets | Zendesk Q4 2025 | 34% of tickets relate to {X} |
| User interviews | Research study #12 | 8/10 users struggled with {Y} |
| Analytics | Mixpanel | 62% drop-off at step 3 of flow |
| Competitor analysis | {Competitor} | They launched {feature} in Q3 |

---

## 3 Goals & Success Metrics

### 3.1 Product Goals

What outcomes does this product/feature aim to achieve?

| # | Goal | Alignment |
|---|------|-----------|
| G1 | {e.g., Reduce onboarding time by 50%} | Company OKR: Improve activation |
| G2 | {e.g., Increase order completion rate to 85%} | Team goal: Revenue growth |

### 3.2 Success Metrics

Every metric MUST have a baseline (current state) and target (desired state).

| Metric | Baseline | Target | Measurement method | Owner |
|--------|----------|--------|--------------------|-------|
| Onboarding completion rate | 45% | 70% | Mixpanel funnel | PM |
| Avg time to first order | 12 min | 5 min | Backend logs | Eng |
| Customer support tickets/week | 120 | < 60 | Zendesk dashboard | CS |
| System latency (p95) | — | < 200ms | Datadog APM | Eng |

> 📊 METRIC: Track these metrics for 4 weeks post-launch before declaring
> success. Establish a monitoring dashboard BEFORE launch.

### 3.3 Non-Goals (Out of Scope)

Explicitly state what this spec does NOT cover:

- 🚫 OUT OF SCOPE: {e.g., Mobile app support — tracked in SPEC-042}
- 🚫 OUT OF SCOPE: {e.g., International payment methods — deferred to Q3}
- 🚫 OUT OF SCOPE: {e.g., Admin dashboard redesign}

---

## 4 Target Users & Personas

### 4.1 Primary Persona

| Attribute | Detail |
|-----------|--------|
| **Name** | {e.g., "Sarah, the Small Business Owner"} |
| **Role** | {Job title / function} |
| **Goal** | {What they want to accomplish} |
| **Pain point** | {What frustrates them today} |
| **Technical skill** | {Low / Medium / High} |
| **Usage frequency** | {Daily / Weekly / Monthly} |
| **Key quote** | {Verbatim from user research} |

### 4.2 Secondary Personas

Repeat the table above for each additional persona.

### 4.3 Anti-Personas (Who This Is NOT For)

List users who might encounter this feature but are NOT the target. This
prevents the team from over-generalizing the design.

---

## 5 User Stories & Requirements

### 5.1 User Stories

Organize by user journey. Prioritize each story.

| ID | Priority | As a... | I want to... | So that... |
|----|----------|---------|-------------|-----------|
| US-1 | P0 | registered user | view my order history | I can track past purchases |
| US-2 | P0 | registered user | filter orders by date range | I can find specific orders quickly |
| US-3 | P1 | registered user | export orders as CSV | I can import into accounting software |
| US-4 | P2 | admin | view all users' orders | I can investigate support issues |

Priority definitions:
- **P0** — Must have for launch. Without this, the feature is broken.
- **P1** — Important for adoption. Launch is possible without it, but adoption suffers.
- **P2** — Nice to have. Improves experience but can wait for v2.

### 5.2 Acceptance Criteria

Every P0 and P1 user story MUST have testable acceptance criteria.

**US-1: View order history**

```
AC-1.1: Given a user with 0 orders,
        When they navigate to /orders,
        Then they see an empty state with message "No orders yet"
        And a CTA button linking to the product catalog.

AC-1.2: Given a user with 25 orders,
        When they navigate to /orders,
        Then the 20 most recent orders are displayed (paginated),
        And each order shows: order ID, date, status, total amount.

AC-1.3: Given a user with orders,
        When they click on an order row,
        Then the order detail page opens showing line items,
        shipping address, payment method (last 4 digits), and status history.
```

### 5.3 Functional Requirements

Detailed functional requirements grouped by domain:

#### 5.3.1 {Domain: e.g., Order Management}

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| FR-1 | System shall create an order when payment is confirmed | P0 | Webhook from Stripe |
| FR-2 | System shall send confirmation email within 60s of order creation | P0 | Via SendGrid |
| FR-3 | System shall allow order cancellation within 30 minutes of creation | P1 | |
| FR-4 | System shall auto-cancel unpaid orders after 24 hours | P1 | Cron job |

### 5.4 Non-Functional Requirements

| ID | Category | Requirement | Threshold | Measurement |
|----|----------|-------------|-----------|-------------|
| NFR-1 | Performance | API response time (p95) | < 200ms | Datadog APM |
| NFR-2 | Performance | Page load time (LCP) | < 2.5s | Lighthouse |
| NFR-3 | Availability | Uptime SLA | 99.9% | Uptime monitoring |
| NFR-4 | Scalability | Concurrent users | 1000 | Load test (k6) |
| NFR-5 | Security | Data encryption at rest | AES-256 | Audit |
| NFR-6 | Security | Data encryption in transit | TLS 1.3 | Cert check |
| NFR-7 | Accessibility | WCAG compliance | Level AA | axe-core |
| NFR-8 | Compatibility | Browser support | Last 2 versions of Chrome, Firefox, Safari, Edge | BrowserStack |
| NFR-9 | Data retention | Order data retention | 7 years | Compliance audit |
| NFR-10 | Localization | Supported languages | EN (v1), ES/FR (v2) | Manual QA |

---

## 6 User Flow

### 6.1 Primary User Flow

Trace the main happy path step by step:

```
┌─────────────┐
│  User lands  │
│  on /orders  │
└──────┬──────┘
       │
       ▼
  ┌─────────┐     No     ┌───────────────┐
  │  Has     │───────────▶│  Empty state   │
  │ orders?  │            │  + CTA button  │
  └────┬─────┘            └───────────────┘
       │ Yes
       ▼
┌──────────────┐
│ Display order │
│ list (20/page)│
└──────┬───────┘
       │
       ▼ Click order
┌──────────────┐
│ Order detail  │
│ page          │
└──────┬───────┘
       │
       ├──── [Export PDF] ──▶ Download order invoice
       │
       └──── [Cancel] ──▶ ┌─────────────┐     No      ┌────────────┐
                          │ Within 30   │─────────────▶│ Show error │
                          │ minutes?    │              │ "Too late" │
                          └──────┬──────┘              └────────────┘
                                 │ Yes
                                 ▼
                          ┌─────────────┐
                          │ Confirm     │
                          │ cancellation│
                          └──────┬──────┘
                                 │
                                 ▼
                          ┌─────────────┐
                          │ Order       │
                          │ cancelled   │
                          │ + Refund    │
                          └─────────────┘
```

### 6.2 Error / Edge Case Flows

Document what happens when things go wrong:

| Scenario | Expected behavior |
|----------|------------------|
| Payment gateway timeout | Show "Payment processing" screen. Retry 3x. If still failing, show error + support link. |
| Duplicate order submission | Idempotency key prevents duplicate. Return existing order. |
| Insufficient inventory | Show "Item unavailable" before checkout. If race condition at payment, refund automatically. |

---

## 7 Technical Specification

### 7.1 Tech Stack

| Layer | Technology | Justification |
|-------|-----------|---------------|
| Frontend | {e.g., React 18 + TypeScript} | Existing stack, team expertise |
| Backend | {e.g., Python 3.12 + FastAPI} | Performance, async support |
| Database | {e.g., PostgreSQL 16} | ACID compliance, JSON support |
| Cache | {e.g., Redis 7} | Session storage, rate limiting |
| Search | {e.g., Elasticsearch 8} | Full-text search on orders |
| Queue | {e.g., Celery + Redis} | Async email, webhook processing |
| Storage | {e.g., S3} | Invoice PDF storage |
| Auth | {e.g., JWT + OAuth2} | Stateless, SSO integration |

> 📌 DECISION: We use FastAPI over Flask because this feature requires
> WebSocket support for real-time order status updates. Flask would require
> additional libraries (flask-socketio) adding complexity.

### 7.2 System Architecture

```
┌─────────────┐      HTTPS       ┌────────────────┐      SQL       ┌────────────┐
│  React SPA  │─────────────────▶│  FastAPI        │──────────────▶│ PostgreSQL │
│  (Vercel)   │◀─────────────────│  (ECS Fargate)  │◀──────────────│  (RDS)     │
└─────────────┘   JSON / WS      └────────────────┘               └────────────┘
                                        │    │
                                        │    │ Pub/Sub
                                        │    ▼
                                        │  ┌──────────┐     SMTP     ┌───────────┐
                                        │  │ Celery   │─────────────▶│ SendGrid  │
                                        │  │ Worker   │              └───────────┘
                                        │  └──────────┘
                                        │       │
                                 Redis ◀┘       └──▶ S3 (Invoices)
```

> 🔒 SECURITY: All traffic between services is TLS-encrypted. Database
> connections use SSL certificates, not password-only auth.

### 7.3 Data Model

#### Entity-Relationship Diagram

```
┌──────────────────┐       ┌───────────────────┐       ┌──────────────────┐
│      users       │       │      orders       │       │   order_items    │
├──────────────────┤       ├───────────────────┤       ├──────────────────┤
│ id        UUID PK│──┐    │ id        UUID PK │──┐    │ id       UUID PK │
│ email     VARCHAR│  │    │ user_id   UUID FK │  │    │ order_id UUID FK │
│ name      VARCHAR│  └───▶│ status    ENUM    │  └───▶│ product_id  FK   │
│ role      ENUM   │       │ total     DECIMAL │       │ quantity INTEGER │
│ created_at TSTZ  │       │ currency  CHAR(3) │       │ unit_price DEC   │
│ updated_at TSTZ  │       │ shipping_addr JSONB│       │ created_at TSTZ  │
└──────────────────┘       │ payment_intent_id │       └──────────────────┘
                           │ cancelled_at TSTZ │
                           │ created_at  TSTZ  │              │
                           │ updated_at  TSTZ  │              │
                           └───────────────────┘              │
                                                              │
                           ┌───────────────────┐              │
                           │     products      │              │
                           ├───────────────────┤              │
                           │ id        UUID PK │◀─────────────┘
                           │ name      VARCHAR │
                           │ price     DECIMAL │
                           │ inventory INTEGER │
                           │ category_id   FK  │
                           └───────────────────┘
```

#### Field Details

**orders**

| Field | Type | Constraints | Description |
|-------|------|------------|-------------|
| `id` | `UUID` | PK, default `gen_random_uuid()` | Unique order identifier |
| `user_id` | `UUID` | FK → users.id, NOT NULL, indexed | Order owner |
| `status` | `ENUM` | NOT NULL, default `'pending'` | See state machine below |
| `total` | `DECIMAL(10,2)` | NOT NULL, CHECK >= 0 | Total amount in `currency` |
| `currency` | `CHAR(3)` | NOT NULL, default `'USD'` | ISO 4217 currency code |
| `shipping_addr` | `JSONB` | NOT NULL | `{street, city, state, zip, country}` |
| `payment_intent_id` | `VARCHAR(255)` | UNIQUE, nullable | Stripe PaymentIntent ID |
| `cancelled_at` | `TIMESTAMPTZ` | nullable | When the order was cancelled |
| `created_at` | `TIMESTAMPTZ` | NOT NULL, default `now()` | Creation timestamp |
| `updated_at` | `TIMESTAMPTZ` | NOT NULL, auto-update | Last modification |

> ⚠️ RISK: `shipping_addr` as JSONB means no foreign key to an addresses table.
> If we need address validation or reuse later, we should extract to a separate
> table. Acceptable for v1; revisit for v2.

#### State Machine

```
                        create
           ┌────────────────────────────────┐
           ▼                                │
      ┌─────────┐     pay      ┌──────────────┐     ship     ┌───────────┐
      │ pending  │─────────────▶│  confirmed   │────────────▶│  shipped  │
      └─────────┘              └──────────────┘             └───────────┘
           │                         │                            │
           │ cancel (< 30min)        │ refund                    │ deliver
           ▼                         ▼                            ▼
      ┌─────────┐              ┌──────────────┐             ┌───────────┐
      │cancelled│              │   refunded   │             │ delivered │
      └─────────┘              └──────────────┘             └───────────┘
           │                                                      │
           │ expire (24h, no payment)                             │ return
           ▼                                                      ▼
      ┌─────────┐                                           ┌───────────┐
      │ expired  │                                           │  returned │
      └─────────┘                                           └───────────┘
```

Valid transitions:

| From | To | Trigger | Side effects |
|------|----|---------|-------------|
| `pending` | `confirmed` | Payment webhook (success) | Send confirmation email, decrement inventory |
| `pending` | `cancelled` | User cancels within 30 min | Refund if payment captured |
| `pending` | `expired` | 24h cron job | No refund (no payment captured) |
| `confirmed` | `shipped` | Admin marks shipped | Send tracking email |
| `confirmed` | `refunded` | Admin processes refund | Stripe refund, restore inventory |
| `shipped` | `delivered` | Carrier webhook | Send delivery email |
| `delivered` | `returned` | User initiates return | Create return label |

> 📌 DECISION: `expired` is a terminal state distinct from `cancelled` because
> expired orders never had a payment, while cancelled orders may require refund
> processing.

### 7.4 API Specification

#### Endpoints

| Method | Path | Auth | Description | Request | Response |
|--------|------|------|-------------|---------|----------|
| `GET` | `/api/v1/orders` | JWT | List user's orders | Query: `?page=1&per_page=20&status=confirmed&from=2025-01-01` | `200`: Paginated order list |
| `GET` | `/api/v1/orders/{id}` | JWT | Get order detail | — | `200`: Full order with items |
| `POST` | `/api/v1/orders` | JWT | Create order | Body: `{items, shipping_addr, coupon_code?}` | `201`: Created order |
| `POST` | `/api/v1/orders/{id}/cancel` | JWT | Cancel order | — | `200`: Updated order |
| `GET` | `/api/v1/orders/{id}/invoice` | JWT | Download invoice PDF | — | `200`: `application/pdf` |

#### Request/Response Schemas

**POST /api/v1/orders**

Request:
```json
{
  "items": [
    { "product_id": "uuid-here", "quantity": 2 }
  ],
  "shipping_address": {
    "street": "123 Main St",
    "city": "Boston",
    "state": "MA",
    "zip": "02115",
    "country": "US"
  },
  "coupon_code": "SAVE10"
}
```

Response (201 Created):
```json
{
  "id": "order-uuid",
  "status": "pending",
  "items": [
    {
      "product_id": "uuid-here",
      "product_name": "Widget Pro",
      "quantity": 2,
      "unit_price": 29.99,
      "subtotal": 59.98
    }
  ],
  "subtotal": 59.98,
  "discount": -5.99,
  "tax": 3.37,
  "shipping": 5.00,
  "total": 62.36,
  "currency": "USD",
  "created_at": "2026-02-20T15:30:00Z"
}
```

#### Error Responses

| Status | Code | Description |
|--------|------|-------------|
| `400` | `INVALID_REQUEST` | Validation error (missing fields, bad format) |
| `401` | `UNAUTHORIZED` | Missing or invalid JWT |
| `403` | `FORBIDDEN` | User doesn't own this order |
| `404` | `ORDER_NOT_FOUND` | Order ID doesn't exist |
| `409` | `ALREADY_CANCELLED` | Order is already cancelled |
| `422` | `CANCELLATION_WINDOW_EXPIRED` | Past 30-minute cancel window |
| `422` | `INSUFFICIENT_INVENTORY` | Product out of stock |
| `500` | `INTERNAL_ERROR` | Unexpected server error |

Error body format:
```json
{
  "error": {
    "code": "CANCELLATION_WINDOW_EXPIRED",
    "message": "Orders can only be cancelled within 30 minutes of creation.",
    "details": {
      "order_id": "uuid-here",
      "created_at": "2026-02-20T15:00:00Z",
      "cancellation_deadline": "2026-02-20T15:30:00Z"
    }
  }
}
```

### 7.5 Sequence Diagram — Order Creation

```
Browser          API Server         Stripe           Database        Celery Worker
  │                  │                │                  │                │
  │  POST /orders    │                │                  │                │
  │─────────────────▶│                │                  │                │
  │                  │ Validate input │                  │                │
  │                  │ Check inventory│                  │                │
  │                  │───────────────────────────────────▶│                │
  │                  │◀──────────────────────────────────│                │
  │                  │                │                  │                │
  │                  │ Create PaymentIntent              │                │
  │                  │───────────────▶│                  │                │
  │                  │◀──────────────│                  │                │
  │                  │ client_secret  │                  │                │
  │                  │                │                  │                │
  │                  │ INSERT order (status=pending)     │                │
  │                  │───────────────────────────────────▶│                │
  │                  │◀──────────────────────────────────│                │
  │                  │                │                  │                │
  │  201 + client_secret              │                  │                │
  │◀─────────────────│                │                  │                │
  │                  │                │                  │                │
  │ stripe.confirmPayment()           │                  │                │
  │──────────────────────────────────▶│                  │                │
  │                  │                │                  │                │
  │                  │ Webhook: payment_intent.succeeded  │                │
  │                  │◀──────────────│                  │                │
  │                  │ UPDATE order status=confirmed     │                │
  │                  │───────────────────────────────────▶│                │
  │                  │                │                  │                │
  │                  │ Enqueue: send_confirmation_email  │                │
  │                  │──────────────────────────────────────────────────▶│
  │                  │                │                  │                │
  │                  │                │                  │        Send email
  │                  │                │                  │                │
```

---

## 8 Design & UX

### 8.1 Wireframes / Mockups

Link to design files or embed ASCII wireframes:

```
┌────────────────────────────────────────────────┐
│  My Orders                          [Export ▼] │
├────────────────────────────────────────────────┤
│  🔍 Search orders...    📅 Date range: ▼       │
├────────┬──────────┬──────────┬────────┬────────┤
│ Order  │ Date     │ Status   │ Total  │        │
├────────┼──────────┼──────────┼────────┼────────┤
│ #1042  │ Feb 20   │ ✅ Done  │ $62.36 │  ▶     │
│ #1039  │ Feb 18   │ 🚚 Ship  │ $29.99 │  ▶     │
│ #1035  │ Feb 15   │ ❌ Canc  │ $0.00  │  ▶     │
├────────┴──────────┴──────────┴────────┴────────┤
│              Page 1 of 3    < 1 2 3 >          │
└────────────────────────────────────────────────┘
```

### 8.2 Design Principles

- Show status prominently — users come here to check "where is my order?"
- Progressive disclosure — list shows summary, detail page shows everything
- Empty states are opportunities — guide users to make their first purchase

---

## 9 Security & Privacy

| Concern | Requirement | Implementation |
|---------|-------------|---------------|
| Authentication | All order endpoints require valid JWT | FastAPI dependency injection |
| Authorization | Users can only access their own orders | Query filter: `WHERE user_id = current_user.id` |
| PII handling | Shipping addresses are PII | Encrypt at rest (RDS encryption), mask in logs |
| Payment data | Never store full card numbers | Stripe handles; we only store `payment_intent_id` |
| Rate limiting | Prevent order spam | 10 orders/minute per user (Redis token bucket) |
| Input validation | Prevent injection | Pydantic schemas validate all input |
| CSRF | Protect state-changing endpoints | SameSite cookies + CSRF token |
| Audit trail | Track who did what | Log all state transitions with actor and timestamp |

> 🔒 SECURITY: We NEVER log request bodies that contain shipping addresses.
> Logger configuration must strip PII fields. See `app/middleware/logging.py`.

---

## 10 Dependencies & Integrations

| Dependency | Type | Owner | Status | Risk |
|-----------|------|-------|--------|------|
| Stripe Payment API | External | Stripe | Available | Payment gateway outage |
| SendGrid Email API | External | SendGrid | Available | Email delivery delay |
| Product Catalog service | Internal | Catalog team | Available | API contract change |
| Inventory service | Internal | Warehouse team | In development | May not be ready by launch |
| User Authentication | Internal | Auth team | Available | — |

> ⚠️ RISK: Inventory service is still in development. Mitigation: for v1, check
> inventory via direct DB query to products table. Switch to service call in v2.

---

## 11 Rollout & Launch Plan

### 11.1 Rollout Strategy

| Phase | Audience | Duration | Success gate |
|-------|----------|----------|-------------|
| Alpha | Internal team (10 users) | 1 week | No P0 bugs |
| Beta | 5% of users (feature flag) | 2 weeks | Error rate < 0.1% |
| GA | 100% of users | — | Success metrics trending up |

### 11.2 Feature Flags

| Flag | Default | Description |
|------|---------|-------------|
| `order_history_v2` | `false` | Enables new order history page |
| `order_cancellation` | `false` | Enables self-service cancellation |
| `order_export_csv` | `false` | Enables CSV export (P2 feature) |

### 11.3 Monitoring & Alerting

| Signal | Tool | Alert threshold |
|--------|------|----------------|
| API error rate (5xx) | Datadog | > 1% for 5 minutes |
| API latency (p95) | Datadog | > 500ms for 5 minutes |
| Order creation failures | Custom metric | > 5 in 10 minutes |
| Celery queue depth | Redis monitoring | > 1000 pending tasks |
| Payment webhook failures | Stripe dashboard | Any failure |

### 11.4 Rollback Plan

If critical issues are detected post-launch:
1. Disable feature flag `order_history_v2` → instantly reverts to old page
2. If data corruption: halt writes, assess impact, restore from last backup
3. Communicate via status page and Slack #incidents

---

## 12 Timeline & Milestones

| Milestone | Target date | Owner | Dependencies |
|-----------|-------------|-------|-------------|
| Spec approved | {date} | PM | Design review, Eng review |
| Design complete | {date} | Design | PM sign-off on user flow |
| Backend API complete | {date} | Eng | Database migrations, Stripe integration |
| Frontend complete | {date} | Eng | Backend API available |
| QA testing complete | {date} | QA | All code merged |
| Alpha release | {date} | Eng | Feature flag ready |
| Beta release | {date} | PM | Alpha success gate passed |
| GA release | {date} | PM | Beta success gate passed |

---

## 13 Assumptions & Risks

### 13.1 Assumptions

| # | Assumption | Impact if wrong |
|---|-----------|----------------|
| A1 | Users have a modern browser (last 2 versions) | Would need polyfills, slower performance |
| A2 | Stripe webhooks arrive within 30 seconds | Order status may appear stale |
| A3 | Average order has < 20 line items | Pagination may be needed in order detail |

### 13.2 Risks

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|-----------|
| R1 | Stripe API outage | Low | High | Queue orders, retry on recovery |
| R2 | Inventory service not ready | Medium | High | Direct DB fallback for v1 |
| R3 | High traffic at launch | Low | Medium | Load test before beta |
| R4 | Shipping address validation errors | Medium | Low | Use Google Address API |

---

## 14 Open Questions

Track unresolved questions. Do NOT pretend you know the answer.

| # | Question | Owner | Status | Decision |
|---|----------|-------|--------|----------|
| Q1 | Do we need to support guest checkout (no account)? | PM | Open | — |
| Q2 | What is the maximum order value before requiring manual review? | Finance | Open | — |
| Q3 | Should cancelled orders count toward loyalty points? | PM | Resolved | No — points only for delivered orders |

---

## 15 Future Considerations

Items deliberately deferred to future iterations:

- 💡 FUTURE: Subscription/recurring orders (Q3)
- 💡 FUTURE: Multi-currency support (Q4)
- 💡 FUTURE: Order splitting (ship items from different warehouses separately)
- 💡 FUTURE: Real-time order tracking via WebSocket

---

## Appendix

### A. Glossary

| Term | Definition |
|------|-----------|
| PaymentIntent | Stripe object representing a payment attempt |
| Idempotency key | Client-generated key to prevent duplicate operations |
| Feature flag | Runtime toggle to enable/disable features without deploy |

### B. Related Documents

| Document | Link |
|----------|------|
| Product Roadmap | {link} |
| Design mockups (Figma) | {link} |
| Technical Design Doc | {link} |
| User Research Report | {link} |
| Competitive Analysis | {link} |
```

---

Adapt the depth to the scope. A full product spec needs every section. A single
feature spec may have lighter sections 4 (personas) and 11 (rollout) but MUST
be thorough on sections 5–7 (requirements, flows, technical spec).
