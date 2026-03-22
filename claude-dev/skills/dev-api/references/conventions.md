# FastAPI Conventions Reference

Complete list of FastAPI best practices. Apply every rule when writing or reviewing code.

## 1. Project Structure

1.1. Use app factory pattern in `main.py` — create the `FastAPI()` instance in a function, not at module level.

1.2. Separate concerns: `routers/` for handlers, `services/` for business logic, `schemas/` for Pydantic models, `models/` for ORM models.

1.3. One router file per resource (e.g., `routers/users.py`, `routers/items.py`).

1.4. Shared dependencies live in `dependencies.py`, not scattered across routers.

1.5. Configuration via `pydantic-settings` with environment variable loading.

## 2. Routing

2.1. Use `APIRouter` with `prefix` and `tags` for every router module.

2.2. URL paths use plural nouns and kebab-case: `/users`, `/order-items`.

2.3. Set explicit `status_code` on every endpoint (`status.HTTP_201_CREATED`, not `201`).

2.4. Set `response_model` on every endpoint — never return raw dicts.

2.5. Add `summary` parameter for OpenAPI documentation.

2.6. Use path parameters for resource identity (`/users/{user_id}`), query parameters for filtering/pagination.

2.7. CRUD mapping: `POST` = create, `GET` = read, `PUT` = full update, `PATCH` = partial update, `DELETE` = remove.

## 3. Pydantic Schemas

3.1. Inherit from a shared base: `UserBase` → `UserCreate`, `UserUpdate`, `UserResponse`.

3.2. Use `Field(...)` with constraints: `min_length`, `max_length`, `ge`, `le`, `pattern`.

3.3. Set `model_config = ConfigDict(from_attributes=True)` on response models for ORM compatibility.

3.4. Use `EmailStr`, `HttpUrl`, and other Pydantic types — don't validate manually.

3.5. Partial update schemas: all fields `Optional`, use `model.model_dump(exclude_unset=True)`.

3.6. Never expose internal fields (password hashes, internal IDs) in response models.

3.7. Use `Enum` for fixed-choice fields.

## 4. Dependency Injection

4.1. **Always** use `Annotated` style: `db: Annotated[AsyncSession, Depends(get_db)]`.

4.2. **Never** use bare `Depends()` in function signatures: `db: AsyncSession = Depends(get_db)` is deprecated style.

4.3. Define reusable type aliases for common dependencies:

```python
CurrentUser = Annotated[User, Depends(get_current_user)]
DbSession = Annotated[AsyncSession, Depends(get_db)]
```

4.4. Use `yield` dependencies for resources that need cleanup (DB sessions, file handles).

4.5. Chain dependencies for auth layers: `get_current_user` → `get_admin_user`.

## 5. Error Handling

5.1. Raise `HTTPException` with specific status codes — never return error dicts.

5.2. Include actionable `detail` messages: `"User with email=x@y.com already exists"`, not `"Error"`.

5.3. Create custom exception classes for domain errors.

5.4. Register global exception handlers for unhandled exceptions — return structured JSON, not stack traces.

5.5. Use `status` constants from `fastapi`: `status.HTTP_404_NOT_FOUND`, not `404`.

## 6. Async & Performance

6.1. Use `async def` for endpoints that perform I/O (database, HTTP calls, file operations).

6.2. Use `def` (sync) only for CPU-bound endpoints — FastAPI runs these in a thread pool.

6.3. Never call synchronous blocking I/O inside `async def` endpoints — use `run_in_executor`.

6.4. Use `asyncio.gather()` for concurrent independent I/O operations.

6.5. Add `lifespan` context manager for startup/shutdown (DB connection pools, caches).

## 7. Authentication & Security

7.1. Use OAuth2 with JWT tokens via `OAuth2PasswordBearer`.

7.2. Hash passwords with `bcrypt` or `argon2` — never store plaintext.

7.3. Auth dependency on every protected endpoint — don't check auth in business logic.

7.4. Rate limiting via middleware or dependency.

7.5. Configure CORS explicitly — never use `allow_origins=["*"]` in production.

7.6. Validate and sanitize all user inputs via Pydantic — never trust raw request data.

## 8. Database

8.1. Use async ORM (SQLAlchemy 2.0 async) for non-blocking queries.

8.2. Session-per-request via dependency injection with `yield`.

8.3. Never commit inside route handlers — let the dependency handle commit/rollback.

8.4. Use `select()` with `joinedload()` or `selectinload()` to prevent N+1 queries.

8.5. Add database indexes for frequently queried columns.

8.6. Use Alembic for migrations — never modify schemas manually.

## 9. Testing

9.1. Use `httpx.AsyncClient` with `ASGITransport` for async endpoint tests.

9.2. Override dependencies in tests: `app.dependency_overrides[get_db] = mock_db`.

9.3. Use factory fixtures for test data (`create_test_user()`), not hardcoded values.

9.4. Test both success and error paths for every endpoint.

9.5. Validate response status codes AND response body structure.

## 10. Documentation

10.1. Add `summary` and docstrings to all endpoints — they appear in OpenAPI docs.

10.2. Document raised exceptions in docstrings.

10.3. Use `response_model` for automatic schema documentation.

10.4. Add `examples` to Pydantic models for better Swagger UI.

10.5. Tag routers for logical grouping in API docs.
