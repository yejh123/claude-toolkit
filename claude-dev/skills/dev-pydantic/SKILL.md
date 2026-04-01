---
name: dev-pydantic
description: "Pydantic v2 model design: architect BaseModel hierarchies, validators, custom types, discriminated unions, serialization. Use when designing Pydantic models, reviewing model architecture, building complex schemas, or writing validators. Triggers on: Pydantic, BaseModel, field_validator, model_validator, discriminated union, ConfigDict, custom type, model hierarchy, serialization, model_dump."
metadata:
  version: "1.0"
  last_updated: "2026-03-23"
---

# Dev Pydantic — Model Architecture

Expert-level guidance for designing Pydantic v2 BaseModel hierarchies, validators, custom types, and serialization strategies.

## Quick Start

```
Design Pydantic models for my e-commerce domain
Review my model hierarchy for anti-patterns
Build a discriminated union for payment events
Create reusable custom types for my project
```

## Trigger Conditions

**Triggers on**: Pydantic model, BaseModel, field_validator, model_validator, discriminated union, ConfigDict, custom type, model hierarchy, serialization, model_dump, Annotated type, generic model, RootModel, computed_field

**Does NOT trigger on**:
- FastAPI endpoints or routers → use `dev-api`
- General Python debugging → use `dev-workflow`
- Code review for non-Pydantic code → use `dev-review`

## Core Workflow — Design Mode

Follow these four phases when designing models from scratch.

### Phase 1: Domain Analysis

1. Identify entities (have identity/lifecycle) vs value objects (immutable, identity-free)
2. Map relationships: one-to-one, one-to-many, polymorphic
3. Determine trust boundaries — where does external data enter?

> **Boundary rule**: Use Pydantic at system boundaries (API I/O, config files, external data ingestion). Use dataclasses or plain classes for internal domain logic where validation overhead is unnecessary.

### Phase 2: Base Model Setup

Define a project-wide base model. All domain models inherit from this:

```python
from pydantic import BaseModel, ConfigDict


class AppBaseModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        str_strip_whitespace=True,
        validate_assignment=True,
    )
```

- `extra="forbid"` — reject unknown fields instead of silently ignoring them
- `from_attributes=True` — enable ORM model conversion via `.model_validate(orm_obj)`
- `str_strip_whitespace=True` — auto-strip leading/trailing whitespace on all str fields
- `validate_assignment=True` — re-validate when fields are reassigned after construction

### Phase 3: Model Hierarchy

Use the CRUD pattern: Base → Create → Update → Response.

```python
class UserBase(AppBaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(AppBaseModel):
    email: EmailStr | None = None
    name: str | None = Field(None, min_length=1, max_length=100)
    password: str | None = Field(None, min_length=8)


class UserResponse(UserBase):
    id: int
    created_at: datetime
```

- **Max 2 levels of inheritance.** If you need a third level, flatten with composition (embed models as fields).
- `UserUpdate` makes all fields optional for PATCH semantics. Use `exclude_unset=True` on serialization to distinguish "not sent" from "set to null."

### Phase 4: Anti-Pattern Check

Review models against these common mistakes:

| Anti-Pattern | Fix |
|---|---|
| `extra="ignore"` silently drops fields | `extra="forbid"` to catch typos |
| Deep inheritance (>2 levels) | Flatten with composition |
| Validators with side effects (DB calls, HTTP) | Pure validation only; side effects belong in services |
| Regex patterns without anchors | Always use `^...$` to match the full string |
| Pydantic models for internal logic | Use dataclasses where validation is unnecessary |
| Mutable default values | Use `Field(default_factory=list)` |

## Field Design Reference

### Custom Annotated Types

Prefer declarative `Field()` constraints and `Annotated` types over writing Python validator functions:

```python
from typing import Annotated

from pydantic import Field

NonEmptyStr = Annotated[str, Field(min_length=1, max_length=500)]
Percentage = Annotated[float, Field(ge=0, le=100)]
PositiveInt = Annotated[int, Field(gt=0)]
SlugStr = Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")]
```

Define these once in a `types.py` module and import across models.

### Computed Fields

Use `@computed_field` for derived values that should appear in serialization:

```python
from pydantic import computed_field


class Order(AppBaseModel):
    items: list[OrderItem]

    @computed_field
    @property
    def total(self) -> Decimal:
        return sum(item.price * item.quantity for item in self.items)
```

### Alias Patterns

```python
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel


class CamelModel(AppBaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    user_name: str  # accepts both "user_name" and "userName"
```

- `validation_alias` — accept a different name on input only
- `serialization_alias` — output a different name only
- `alias_generator=to_camel` with `populate_by_name=True` — accept both snake_case and camelCase

## Validators Reference

### After Validators (Preferred)

Type-safe, run after Pydantic's own parsing. Attach to `Annotated` for reusability:

```python
from typing import Annotated

from pydantic import AfterValidator


def normalize_email(value: str) -> str:
    return value.lower().strip()


NormalizedEmail = Annotated[str, AfterValidator(normalize_email)]
```

### Model Validators

Use `@model_validator(mode="after")` for cross-field validation:

```python
from pydantic import model_validator


class DateRange(AppBaseModel):
    start: date
    end: date

    @model_validator(mode="after")
    def validate_range(self) -> "DateRange":
        if self.end <= self.start:
            raise ValueError("end must be after start")
        return self
```

### Before Validators

Run before type coercion. Use sparingly — only for input normalization:

```python
FlexibleDate = Annotated[date, BeforeValidator(lambda v: parse_date(v) if isinstance(v, str) else v)]
```

### Reusable Pattern

Always attach validators to `Annotated` types, not individual fields. This avoids duplication and makes validators composable across models.

## Advanced Patterns

### Discriminated Unions

Use `Literal` discriminators for polymorphic types. Always prefer over plain `Union` — O(1) dispatch vs O(n) trial-and-error, with clearer error messages:

```python
from typing import Literal, Union

from pydantic import Field


class CardPayment(AppBaseModel):
    type: Literal["card"]
    card_number: str
    cvv: str


class BankPayment(AppBaseModel):
    type: Literal["bank"]
    account_number: str
    routing_number: str


Payment = Annotated[
    Union[CardPayment, BankPayment],
    Field(discriminator="type"),
]
```

### Generic Models

Use generics for reusable wrappers:

```python
from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    page_size: int
```

### Frozen Models

Use `ConfigDict(frozen=True)` for immutable value objects:

```python
class Money(AppBaseModel):
    model_config = ConfigDict(frozen=True)
    amount: Decimal
    currency: str = Field(pattern=r"^[A-Z]{3}$")
```

### RootModel

For top-level types that aren't dicts:

```python
from pydantic import RootModel

Tags = RootModel[list[str]]
```

### Recursive Models

Use string forward references and call `model_rebuild()` after definition:

```python
class TreeNode(AppBaseModel):
    value: str
    children: list["TreeNode"] = []

TreeNode.model_rebuild()
```

## Serialization

Key `model_dump` / `model_dump_json` kwargs:
- `exclude_unset=True` — omit fields not explicitly set (essential for PATCH)
- `exclude_none=True` — omit fields with `None` values
- `by_alias=True` — use alias names in output
- `mode="json"` — convert all types to JSON-safe equivalents

**Performance**: `model_validate_json(raw_bytes)` is faster than `model_validate(json.loads(raw_bytes))` because it skips the intermediate Python dict.

Use `field_serializer` for custom output formatting:

```python
from pydantic import field_serializer


class Event(AppBaseModel):
    timestamp: datetime

    @field_serializer("timestamp")
    def serialize_timestamp(self, value: datetime) -> str:
        return value.isoformat()
```

## Integration Notes

- **SQLAlchemy**: Keep ORM models and Pydantic schemas separate. Use `from_attributes=True` on the Pydantic side. Never inherit from both `Base` and `BaseModel`.
- **FastAPI**: For endpoint-level guidance (routers, dependencies, error handling) → use `dev-api` skill.
- **Performance**: Create `TypeAdapter` instances at module level — they cache the validation schema. Use `model_construct()` to skip validation for trusted, pre-validated data.

## Quality Standards

| Dimension | Requirement |
|---|---|
| Base model | Project-wide `AppBaseModel` with `ConfigDict` |
| Inheritance | Max 2 levels; prefer composition |
| Constraints | Declarative `Field()` over Python validators |
| Custom types | Reusable via `Annotated` pattern in a shared `types.py` |
| Unions | Discriminated with `Literal` discriminator; never plain `Union` for >2 variants |
| Validators | After-mode preferred; no side effects; reusable via `Annotated` |
| Boundaries | Pydantic at trust boundaries; dataclasses for internal logic |
| Serialization | Use `exclude_unset` for PATCH; `model_validate_json` over `json.loads` |
