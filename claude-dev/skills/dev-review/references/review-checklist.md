# Python Code Review Checklist

Apply every category to the code under review. Not all rules apply to every codebase — use judgment.

## 1. Correctness

1.1. Logic handles edge cases: empty inputs, boundary values, `None`, zero, negative numbers.

1.2. No off-by-one errors in loops, slicing, and range operations.

1.3. Error handling catches specific exceptions with actionable messages — no bare `except:`.

1.4. Return values are consistent (don't mix returning `None` and raising exceptions for the same error).

1.5. Mutable default arguments avoided (`def f(items=[])` → `def f(items=None)`).

1.6. Boolean conditions are correct — watch for `and`/`or` precedence and De Morgan's law violations.

1.7. Resource cleanup guaranteed — use context managers (`with`) for files, connections, locks.

1.8. Concurrency safety: no race conditions, proper locking if shared state exists.

## 2. Readability

2.1. Functions do one thing — if "and" appears in the description, split it.

2.2. Functions are short enough to fit on one screen (~30 lines max).

2.3. Variable names are descriptive nouns (`user_count`, not `x` or `data`).

2.4. Function names are verbs (`calculate_tax`, not `process` or `handle`).

2.5. Boolean names are questions (`is_valid`, `has_permission`).

2.6. No magic numbers or strings — use named constants.

2.7. No dead code: unused imports, variables, functions, commented-out blocks.

2.8. Guard clauses used to reduce nesting — return early instead of deep `if/else`.

2.9. Complex logic has comments explaining WHY, not WHAT.

## 3. Type Safety

3.1. All function signatures have type annotations.

3.2. `Optional[X]` used when `None` is a valid value.

3.3. Generic types used where appropriate (`list[str]`, `dict[str, int]`).

3.4. No `Any` type unless truly necessary — annotate precisely.

3.5. Return types annotated on all functions.

## 4. API Design

4.1. Functions have 3 or fewer parameters — group into dataclass/dict if more.

4.2. Public API is minimal — don't expose internals.

4.3. Function contracts are clear from signature alone (no surprising side effects).

4.4. Consistent patterns across similar functions.

## 5. Error Handling

5.1. Exceptions are specific (`ValueError`, `KeyError`), not generic (`Exception`).

5.2. Error messages include context: what failed, what was expected, what was received.

5.3. Fail fast: validate inputs at the boundary, not deep inside.

5.4. No silently swallowed exceptions (`except: pass`).

5.5. Custom exceptions defined for domain-specific error conditions.

## 6. Security

6.1. No hardcoded credentials, API keys, or secrets.

6.2. No SQL injection via string formatting — use parameterized queries.

6.3. No command injection via `os.system()` or `subprocess` with `shell=True`.

6.4. User inputs validated and sanitized at boundaries.

6.5. No `eval()`, `exec()`, or `pickle.loads()` on untrusted data.

6.6. Sensitive data not logged or exposed in error messages.

## 7. Performance

7.1. No unnecessary loops — use list comprehensions, generators, or built-in functions.

7.2. Appropriate data structures: `set` for membership testing, `dict` for lookups.

7.3. No repeated expensive computations — cache or compute once.

7.4. Database queries avoid N+1 pattern — use joins or batch loading.

7.5. Large data processed lazily (generators) instead of loading everything into memory.

## 8. Testing

8.1. New code has corresponding tests.

8.2. Tests cover both happy path and error cases.

8.3. Tests are deterministic — no flaky tests from timing, randomness, or external state.

8.4. Test names describe behavior: `test_login_fails_with_expired_token`, not `test_login_2`.

8.5. No test logic duplication — use fixtures and parametrize.

8.6. Tests are independent — no order dependencies between test functions.

## 9. Python Idioms

9.1. Use f-strings for formatting (not `%` or `.format()` except in logging).

9.2. Use `pathlib.Path` instead of `os.path` for file operations.

9.3. Use `enumerate()` instead of manual counter in loops.

9.4. Use `zip()` for parallel iteration.

9.5. Use `collections` types: `defaultdict`, `Counter`, `namedtuple`.

9.6. Use `dataclasses` or `pydantic` instead of plain dicts for structured data.

9.7. Imports grouped: stdlib, third-party, local. No wildcard imports.

## 10. Documentation

10.1. Public functions/classes have Google-style docstrings.

10.2. Module-level docstring explaining purpose.

10.3. Complex algorithms have inline comments explaining the approach.

10.4. README or module docs explain setup and usage.
