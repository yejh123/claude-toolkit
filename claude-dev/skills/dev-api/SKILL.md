---
name: dev-api
description: "FastAPI development expert: apply conventions, review endpoints, write production-quality API code. Use when the user is building or reviewing FastAPI applications, designing REST endpoints, configuring dependency injection, or writing Pydantic models. Triggers on: FastAPI, API endpoint, router, Pydantic model, dependency injection, REST API, web API."
metadata:
  version: "1.0"
  last_updated: "2026-03-19"
---

# Dev API — FastAPI Development

Expert-level guidance for FastAPI development. Apply conventions consistently when reviewing or writing API code.

## Quick Start

```
Review my FastAPI endpoint for best practices
Write a CRUD router for the users resource
Help me set up dependency injection for database sessions
Check my Pydantic models
```

## Trigger Conditions

**Triggers on**: FastAPI, API endpoint, router, Pydantic model, dependency injection, REST API, web API, API development, endpoint review

**Does NOT trigger on**:
- General Python debugging → use `dev-workflow`
- Code review for non-API code → use `dev-review`
- Project planning → use `dev-plan`

## Core Conventions

Load `references/conventions.md` for the complete list of FastAPI best practices.

## When Reviewing Code

1. Load the conventions reference
2. Check the user's code against each convention
3. For each violation, cite the specific rule and suggest the fix
4. Group findings by category (routing, models, dependencies, error handling, security)

### Review Output Format

```
[SEVERITY] Convention N.M: Brief description
  Location: file:line
  Current: <problematic code>
  Fix: <corrected code>
  Rule: <convention being violated>
```

Severity levels:
- **error**: Violates a must-follow convention → must fix
- **warning**: Deviates from best practice → should fix
- **info**: Style improvement → consider

## When Writing Code

1. Load the conventions reference
2. Follow every convention exactly
3. Add type annotations to all function signatures
4. Use `Annotated` style for dependency injection
5. Include docstrings on all public endpoints

### Code Structure

Organize FastAPI projects with this structure:

```
app/
├── main.py              # App factory, middleware, CORS
├── config.py            # Settings via pydantic-settings
├── dependencies.py      # Shared dependencies (DB session, auth)
├── models/              # SQLAlchemy / ORM models
├── schemas/             # Pydantic request/response schemas
├── routers/             # Route handlers grouped by resource
│   ├── users.py
│   └── items.py
├── services/            # Business logic layer
└── tests/
```

### Endpoint Template

Every endpoint should follow this pattern:

```python
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_db
from app.schemas.users import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
)
async def create_user(
    user_in: UserCreate,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> UserResponse:
    """Create a new user account.

    Raises:
        HTTPException 409: If email already exists.
    """
    service = UserService(db)
    return await service.create(user_in)
```

### Key Patterns

#### Dependency Injection (Annotated Style)

```python
from typing import Annotated

from fastapi import Depends

# Define reusable type aliases
CurrentUser = Annotated[User, Depends(get_current_user)]
DbSession = Annotated[AsyncSession, Depends(get_db)]

@router.get("/me")
async def get_profile(user: CurrentUser, db: DbSession) -> UserResponse:
    return await UserService(db).get(user.id)
```

#### Pydantic Schemas

```python
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
```

#### Error Handling

```python
from fastapi import HTTPException, status


class NotFoundError(HTTPException):
    def __init__(self, resource: str, id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} with id={id} not found",
        )
```

## Quality Standards

| Dimension | Requirement |
|-----------|-------------|
| Type safety | All function signatures fully annotated |
| Validation | Pydantic models with field constraints |
| Dependencies | `Annotated[T, Depends()]` style, never bare `Depends()` in signatures |
| Responses | Explicit `response_model` and `status_code` on every endpoint |
| Errors | Specific HTTP exceptions with actionable messages |
| Security | Auth dependencies on protected routes, CORS configured |
| Async | Use `async def` for I/O-bound endpoints |
