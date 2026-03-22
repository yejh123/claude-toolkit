---
name: dev-review
description: "Reviews code for quality, style, and common bugs with confidence scoring. Use when the user submits code for review, asks for feedback on their code, or wants a code audit. By default reviews unstaged changes (git diff). Triggers on: review my code, code review, code feedback, code audit, check my code, review this function, review this PR."
metadata:
  version: "2.0"
  last_updated: "2026-03-22"
---

# Dev Review — Code Review

Reviews code for quality, style, and common bugs. Follows a structured protocol with confidence scoring to produce consistent, actionable, high-signal feedback.

## Quick Start

```
Review my code
Give me feedback on this function
Audit this module for bugs
Check this PR for quality issues
```

## Trigger Conditions

**Triggers on**: review my code, code review, code feedback, code audit, check my code, review this function, review this PR, what's wrong with this code

**Does NOT trigger on**:
- Debugging a specific error → use `dev-workflow`
- FastAPI-specific review → use `dev-api`
- Writing code from scratch → just write it
- Planning a project → use `dev-plan`
- Comprehensive PR review with agents → use `dev-review-pr`

## Review Scope

By default, review unstaged changes from `git diff`. If no unstaged changes exist, review the code the user provides or references. The user may specify different files or scope.

## Review Protocol

Follow these four steps exactly. Do not skip any step.

### Step 1: Load Criteria

Load `references/review-checklist.md` for the complete review criteria.

### Step 2: Understand the Code

Read the user's code carefully. Before critiquing:
- Identify the code's purpose and intended behavior
- Note the programming patterns and architecture used
- Understand the context (library, framework, application type)

**Do not jump to findings before understanding intent.**

### Step 3: Apply Checklist with Confidence Scoring

Apply each rule from the checklist to the code. For every potential violation:

1. Assign a confidence score (0-100)
2. **Only report issues with confidence >= 80**

**Confidence Scale:**
- **0-25**: Likely false positive or pre-existing issue
- **26-50**: Minor nitpick, not explicitly in project guidelines
- **51-75**: Valid but low-impact issue
- **76-90**: Important issue requiring attention
- **91-100**: Critical bug or explicit guideline violation

**HIGH SIGNAL — Flag these:**
- Code that will fail to compile or parse (syntax errors, type errors, missing imports)
- Code that will definitely produce wrong results regardless of inputs (clear logic errors)
- Clear, unambiguous guideline violations where you can quote the exact rule being broken

**DO NOT flag:**
- Pre-existing issues not introduced by the current changes
- Pedantic nitpicks a senior engineer would not flag
- Potential issues that depend on specific inputs or state
- Subjective suggestions or improvements
- Code style preferences when the code is consistent
- Issues a linter will catch

For each high-confidence violation found:

- **Location**: Note the file and line number
- **Confidence**: Score (80-100)
- **Severity**: Classify as `error` (must fix), `warning` (should fix), or `info` (consider)
- **Explanation**: Explain WHY it's a problem, not just WHAT is wrong
- **Fix**: Suggest a specific fix with corrected code

### Step 4: Produce Report

Output a structured review with these sections:

```
## Summary

What the code does and overall quality assessment (2-3 sentences).

## Findings

### Errors (must fix)

[E1] file:line — Description (confidence: N)
  Problem: Why this is wrong
  Current: `problematic code`
  Fix: `corrected code`

### Warnings (should fix)

[W1] file:line — Description (confidence: N)
  Problem: Why this matters
  Current: `problematic code`
  Fix: `corrected code`

### Info (consider)

[I1] file:line — Description (confidence: N)
  Suggestion: What could be improved

## Score

N/10 — Brief justification for the score.

## Top 3 Recommendations

1. Most impactful improvement
2. Second most impactful
3. Third most impactful
```

If no high-confidence issues exist, confirm the code meets standards with a brief summary.

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 9-10 | Production-ready, exemplary code |
| 7-8 | Good quality, minor improvements possible |
| 5-6 | Acceptable, several issues to address |
| 3-4 | Significant problems, needs rework |
| 1-2 | Fundamental issues, major rewrite needed |

## Review Principles

- **Be specific**: "Line 42 has a SQL injection risk via f-string formatting" not "security issue found"
- **Be constructive**: Always provide a fix, not just criticism
- **Prioritize**: Errors first, then warnings, then info. Don't bury critical issues in style nits
- **Respect intent**: Review the code the author wrote, not the code you would have written
- **Context matters**: A quick script has different standards than a production service
- **No bikeshedding**: Skip trivial formatting preferences if the code uses a consistent style
- **High signal only**: If you are not certain an issue is real, do not flag it. False positives erode trust.

## Scope

This skill reviews code in any language. Load `references/review-checklist.md` for Python-specific rules and adapt the principles for other languages as needed.
