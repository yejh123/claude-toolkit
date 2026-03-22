---
name: paper-audit
description: "Multi-dimension quality review and proofreading for academic papers before submission. Use when the user wants to check paper quality, proofread, simulate peer review, run pre-submission checks, or verify a revision. Supports LaTeX, Typst, and PDF inputs. Triggers on: review my paper, proofread, check my paper, is this ready to submit, pre-submission check, paper audit, 审稿, 论文检查, 投稿前检查."
metadata:
  version: "1.0"
  last_updated: "2026-03-18"
---

# Paper Audit — Pre-Submission Review & Proofreading

Multi-dimension quality review for academic papers. Combines automated LaTeX checks with reviewer-perspective analysis. Two-phase workflow: detect issues first, then fix only with user approval.

## Quick Start

```
Review my paper before NeurIPS submission
Proofread main.tex for grammar and style issues
Is this paper ready to submit to ICML?
Check if my revision addressed the reviewer comments
```

## Trigger Conditions

**Triggers on**: review my paper, proofread, check my paper, is this ready to submit, pre-submission check, paper audit, find issues, 审稿, 论文检查, 投稿前检查

**Does NOT trigger on**:
- Writing a paper from scratch → use `paper-write`
- Literature search → use `paper-research`
- Reading a paper for notes → use `note-paper`

## Modes

| Mode | When | Output |
|------|------|--------|
| `review` (default) | Comprehensive pre-submission review | Issue list + severity + suggestions |
| `proofread` | Language and grammar focus | Grammar, style, Chinglish fixes |
| `gate` | Binary submission readiness check | PASS/FAIL + blocking issues |
| `revision-check` | Verify fixes against prior review | Addressed/unaddressed checklist |

Infer mode from context. State the assumed mode before proceeding.

## Critical Rules

- **NEVER** modify `\cite{}`, `\ref{}`, `\label{}`, math environments, or domain terminology without explicit user approval
- **NEVER** fabricate bibliography entries
- **TWO-PHASE workflow**: Phase 1 detects, Phase 2 fixes only what user approves
- **Evidence-based**: Every issue must cite specific text, line, or section

## Phase 1: Detection

Read the paper and check systematically across all categories. Do NOT make changes — only report findings.

### Category A: Language & Grammar

- Grammatical errors (subject-verb agreement, article usage, tense consistency)
- Non-native English patterns (Chinglish, word order issues, preposition errors)
- Weak verb usage ("perform an analysis" → "analyze")
- Unclear pronoun references
- Sentence length issues (>40 words warrants splitting)

### Category B: Scientific Claims & Logic

- Overclaiming: claims not supported by presented evidence
- Causal language without causal evidence ("X causes Y" vs "X correlates with Y")
- Unsupported superlatives ("best", "first", "novel" without evidence)
- Logical gaps between sections (claims in intro not addressed in experiments)
- Missing baselines or unfair comparisons

### Category C: Structure & Flow

- Introduction: Does it have problem → gap → contribution → outline?
- Related Work: Organized by methodology or chronologically?
- Methods: Sufficient for reimplementation?
- Experiments: Each experiment clearly supports a specific claim?
- Conclusion: Matches claims in abstract/introduction?
- Cross-section consistency: Do abstract, intro, and conclusion agree?

### Category D: Figures, Tables & Captions

- Captions self-contained (readable without main text)?
- Figure/table referenced in text before appearing?
- Reference order matches appearance order?
- Quantitative consistency (numbers in text match tables/figures)?
- Resolution and readability (especially in two-column format)
- Axes labeled, legends clear, color-blind safe?

### Category E: LaTeX Formatting

- Units: use `\SI{}{}` or `\text{}` (not italic math mode for units)
- Spacing: `\,` between number and unit
- References: `\cref{}` or consistent `Figure~\ref{}`
- Punctuation: Oxford comma, `\ie{}`, `\eg{}`, em-dashes
- Hyphenation: compound adjectives ("state-of-the-art method")
- Math: consistent notation (vectors bold, matrices uppercase)

### Category F: Citations & References

- All citations resolve to bibliography entries?
- No orphan bibliography entries (cited nowhere)?
- Citation style matches venue requirements?
- Self-citation ratio reasonable?
- Key related work missing?
- Citation-as-noun style: "as shown in Smith et al. [3]" → "as shown by Smith et al. [3]"

### Category G: Abstract & Conclusion Quality

- Abstract follows WHY → PROBLEM → HOW → RESULTS structure?
- No undefined abbreviations in abstract?
- Conclusion adds insight beyond abstract (not just repetition)?
- Limitations discussed honestly?

### Category H: Hidden Issues

- TODO/FIXME/XXX comments remaining?
- Placeholder text ("Lorem ipsum", "TBD", "[insert figure]")?
- Commented-out content that should be removed?
- Debug output or test data?
- Author-identifying information (for double-blind)?

## Severity Classification

| Severity | Definition | Action |
|----------|-----------|--------|
| **CRITICAL** | Blocks submission: factual errors, missing required sections, anonymity violations | Must fix before submission |
| **MAJOR** | Significantly impacts quality: overclaiming, missing baselines, logical gaps | Should fix before submission |
| **MINOR** | Style and polish: grammar, formatting, clarity improvements | Fix if time allows |
| **STYLE** | Preference-level: word choice, sentence restructuring | Optional |

## Issue Report Format

For each issue found:
```
[SEVERITY] Category X.N: Brief description
  Location: Section N / Line N / Figure N
  Current: "the exact problematic text"
  Suggested: "the proposed fix"
  Rationale: Why this matters
```

## Phase 2: Fixes (User-Approved Only)

After presenting the Phase 1 report:

1. Ask user which issues to fix (by severity, category, or individually)
2. Apply only approved fixes
3. For each fix, show the exact change (old → new)
4. Re-verify that fixes don't introduce new issues
5. Do NOT make unauthorized changes

## Revision Check Mode

When checking if a revision addressed prior feedback:

1. Read the previous review/audit report
2. Read the revised paper
3. For each prior issue, classify as:
   - `FULLY ADDRESSED`: Issue resolved correctly
   - `PARTIALLY ADDRESSED`: Attempted but incomplete
   - `NOT ADDRESSED`: No change made
   - `REGRESSED`: Fix introduced new problems
4. Check for new issues introduced during revision
5. Provide a summary scorecard

## Venue-Specific Checks

When venue is specified, add venue-specific validation:

| Venue | Additional Checks |
|-------|-------------------|
| NeurIPS | Paper checklist present and filled, broader impact if required |
| ICML | Broader impact statement, page limit (8+1) |
| ICLR | LLM usage disclosure, page limit (9+1) |
| ACL | Limitations section mandatory, ethics statement |
| IEEE | IEEE citation style, keyword section |
| ACM | CCS concepts, ACM reference format |

## Quality Standards

| Dimension | Requirement |
|-----------|-------------|
| Evidence-based | Every issue cites specific text, line, or section |
| Balanced | Report both strengths and weaknesses |
| Actionable | Each issue includes a concrete improvement suggestion |
| Constructive | Professional tone, not dismissive |
| Prioritized | Issues ordered by severity, then by importance |

## Output Language

Match the paper's language. If the paper is in English, report in English. If in Chinese, report in Chinese. Mixed papers: report in the paper's primary language.
