---
name: dev-workflow
description: "Comprehensive software development methodology: systematic debugging, test-driven development, and code review. Use when implementing features, fixing bugs, debugging issues, writing tests, or reviewing code quality. Triggers on: debug this, fix this bug, write tests, TDD, code review, why is this failing, test failure."
metadata:
  version: "1.0"
  last_updated: "2026-03-18"
---

# Dev Workflow — Debug, Test, Review

Comprehensive development methodology combining systematic debugging, test-driven development (TDD), and code review practices. Designed for research code that needs to be correct and reproducible.

## Quick Start

```
Debug why my training script fails at epoch 5
Write tests for the evaluation pipeline
Review my changes before I push
Fix this flaky test
```

## Trigger Conditions

**Triggers on**: debug, fix bug, test failure, write tests, TDD, code review, why is this failing, unexpected behavior, 调试, 修复, 写测试, 代码审查

## When to Use Which Section

| Situation | Go To |
|-----------|-------|
| Something is broken or behaving unexpectedly | Systematic Debugging |
| Implementing new feature or fixing a known bug | Test-Driven Development |
| Code is ready, need quality check before commit | Code Review |

---

## Part 1: Systematic Debugging

### The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes. Symptom fixes create new bugs and waste time.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read error messages carefully**
   - Read stack traces completely, note line numbers and file paths
   - Don't skip warnings — they often contain the answer

2. **Reproduce consistently**
   - What are the exact steps to trigger it?
   - Does it happen every time?
   - If not reproducible, gather more data — don't guess

3. **Check recent changes**
   - `git diff` and recent commits
   - New dependencies, config changes, environment differences

4. **Gather evidence in multi-component systems**
   - Add diagnostic logging at each component boundary
   - Log what enters and exits each component
   - Run once to find WHERE it breaks, then investigate that component

5. **Trace data flow**
   - Where does the bad value originate?
   - Trace backward through the call stack until you find the source
   - Fix at the source, not at the symptom

### Phase 2: Pattern Analysis

1. Find similar working code in the same codebase
2. Compare working vs broken — list every difference
3. Understand dependencies: what settings, config, environment does it need?

### Phase 3: Hypothesis Testing

1. Form a single, specific hypothesis: "I think X because Y"
2. Make the smallest possible change to test it
3. One variable at a time — never fix multiple things at once
4. If it doesn't work, form a NEW hypothesis (don't pile on more fixes)

### Phase 4: Implementation

1. Write a failing test that reproduces the bug
2. Implement a single fix addressing the root cause
3. Verify: test passes, no other tests broken

**If 3+ fixes have failed**: STOP. This signals an architectural problem, not a simple bug. Discuss with the user before attempting more fixes.

### Red Flags — STOP and Return to Phase 1

- "Quick fix for now, investigate later"
- "Just try changing X and see"
- Proposing solutions before tracing data flow
- Making multiple changes at once
- "I don't fully understand but this might work"

---

## Part 2: Test-Driven Development

### The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Wrote code before the test? Delete it. Start over. No exceptions.

### Red-Green-Refactor Cycle

#### RED — Write a Failing Test

Write one minimal test showing what should happen:
- Tests ONE behavior (if "and" appears in test name, split it)
- Clear, descriptive name
- Uses real code, not mocks (unless truly unavoidable)

```python
def test_retry_stops_after_max_attempts():
    attempts = 0
    def failing_op():
        nonlocal attempts
        attempts += 1
        raise ConnectionError("timeout")

    with pytest.raises(ConnectionError):
        retry(failing_op, max_retries=3)

    assert attempts == 3
```

**Run the test. Verify it fails for the expected reason** (feature missing, not a typo).

#### GREEN — Minimal Code

Write the simplest code that makes the test pass. Don't add features, don't refactor, don't "improve" beyond what the test requires.

```python
def retry(fn, max_retries: int = 3):
    for i in range(max_retries):
        try:
            return fn()
        except Exception:
            if i == max_retries - 1:
                raise
```

**Run the test. Verify it passes.** Check that other tests still pass.

#### REFACTOR — Clean Up

Only after green: remove duplication, improve names, extract helpers. Keep tests green throughout.

Then repeat: next failing test for next behavior.

### When to Use TDD

- **Always**: new features, bug fixes, behavior changes
- **Exception (ask user first)**: throwaway prototypes, generated code, config files

### Common Rationalizations to Reject

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests-after pass immediately, proving nothing. |
| "TDD slows me down" | TDD is faster than debugging. |
| "Need to explore first" | Fine. Throw away exploration, then TDD. |

---

## Part 3: Code Review

### When to Request Review

- Before merging any feature branch
- After fixing a bug (review the fix + test)
- Before submitting research code that produces paper results

### Review Checklist

#### Correctness
- [ ] Logic handles edge cases (empty inputs, boundary values, None/null)
- [ ] Error handling catches specific exceptions with actionable messages
- [ ] No off-by-one errors in loops and indexing
- [ ] Concurrency-safe if applicable (no race conditions, proper locking)

#### Readability
- [ ] Functions do one thing (no "and" in description)
- [ ] Variables are nouns, functions are verbs, booleans are questions
- [ ] No magic numbers — named constants used
- [ ] Complex logic has explanatory comments (WHY, not WHAT)

#### Testing
- [ ] New code has corresponding tests
- [ ] Tests cover both happy path and error cases
- [ ] Tests are deterministic (no flaky tests from timing/randomness)
- [ ] Test names describe behavior, not implementation

#### Research Code Specifics
- [ ] Random seeds set and documented
- [ ] Hyperparameters in config, not hardcoded
- [ ] Results are reproducible with documented environment
- [ ] Data paths are configurable, not absolute
- [ ] GPU/CPU compatibility handled

#### Security & Safety
- [ ] No hardcoded credentials or API keys
- [ ] User inputs validated at boundaries
- [ ] No command injection via string formatting
- [ ] Dependencies pinned to specific versions

### Review Output Format

For each issue found:
```
[SEVERITY] file:line — Description
  Current: <problematic code>
  Suggested: <improved code>
  Reason: <why this matters>
```

Severity levels:
- **Critical**: Bug, security issue, or data corruption risk → must fix
- **Important**: Significant quality/correctness concern → should fix
- **Minor**: Style, naming, or minor improvement → nice to fix

### Acting on Review Feedback

1. Fix all Critical and Important issues
2. Address Minor issues if straightforward
3. For disagreements, discuss rationale — don't ignore silently
4. After fixes, verify all tests still pass

---

## Integration

The three parts work together:

1. **Bug reported** → Systematic Debugging (find root cause)
2. **Root cause found** → TDD (write failing test, then fix)
3. **Fix implemented** → Code Review (verify quality before commit)

This cycle ensures bugs are fixed correctly, tested thoroughly, and reviewed before merge.
