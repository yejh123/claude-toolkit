---
name: paper-write
description: "Draft publication-ready ML/AI papers for top conferences (NeurIPS, ICML, ICLR, ACL, AAAI) and systems venues (OSDI, NSDI, ASPLOS). Use when the user wants to write a paper from a research repo, draft specific sections, structure arguments, set up LaTeX templates, or prepare camera-ready submissions. Triggers on: write a paper, draft the introduction, paper writing, prepare submission, LaTeX paper, camera-ready, 写论文, 论文草稿."
metadata:
  version: "1.0"
  last_updated: "2026-03-18"
---

# Paper Write — Academic Paper Drafting

Expert-level guidance for writing publication-ready papers. Combines writing philosophy from top researchers (Nanda, Farquhar, Karpathy, Lipton, Steinhardt, Perez) with practical LaTeX workflows and conference-specific requirements.

## Quick Start

```
Write a paper based on this research repo
Draft the introduction for my NeurIPS submission
Help me structure the experiments section
Set up a LaTeX template for ICML 2026
```

## Trigger Conditions

**Triggers on**: write a paper, draft, paper writing, prepare submission, LaTeX paper, camera-ready, structure my paper, write the introduction/methods/experiments/related work, 写论文, 论文草稿, 投稿准备

**Does NOT trigger on**:
- Literature search → use `paper-research`
- Reviewing/auditing a paper → use `paper-audit`
- Reading a paper for notes → use `note-paper`
- Fixing LaTeX compilation errors only → use shell commands directly

## CRITICAL: Never Hallucinate Citations

**This is the most important rule in academic writing with AI.**

AI-generated citations have ~40% error rate. Hallucinated references are academic misconduct.

| Action | Correct | Wrong |
|--------|---------|-------|
| Adding a citation | Search API → verify → fetch BibTeX | Write BibTeX from memory |
| Uncertain about a paper | Mark as `[CITATION NEEDED]` | Guess the reference |
| Can't find exact paper | Note as placeholder requiring verification | Invent similar-sounding paper |

When you cannot verify a citation:
```latex
\cite{PLACEHOLDER_author2024_verify}  % TODO: Verify this citation exists
```

Always tell the user: "I've marked [N] citations as placeholders that need verification."

## Core Philosophy

### The Narrative Principle

A paper is not a collection of experiments — it's a story with one clear contribution supported by evidence.

**Three Pillars (must be clear by end of introduction):**

| Pillar | Description |
|--------|-------------|
| **The What** | 1-3 specific novel claims within a cohesive theme |
| **The Why** | Rigorous empirical evidence supporting claims |
| **The So What** | Why readers should care — connection to recognized problems |

**If you cannot state the contribution in one sentence, the paper isn't ready.**

### Be Proactive

Default behavior: **deliver a complete draft, then iterate on feedback.**

| Confidence Level | Action |
|-----------------|--------|
| High (clear repo, obvious contribution) | Write full draft, deliver, iterate |
| Medium (some ambiguity) | Write draft with flagged uncertainties |
| Low (major unknowns) | Ask 1-2 targeted questions, then draft |

## Workflow

### Starting from a Research Repository

1. **Explore the repo**: Read README, results directories, existing docs, key scripts
2. **Identify existing citations**: Search for `.bib` files, arxiv references in code/docs
3. **Clarify the contribution**: Confirm framing with the user before writing
4. **Search for literature**: Use web search to find relevant related work
5. **Deliver a first draft**: Write end-to-end, flag uncertainties inline

### Section-by-Section Guide

**Time allocation** (from Neel Nanda): Spend roughly equal time on (1) abstract, (2) introduction, (3) figures, (4) everything else combined.

#### Abstract (5-Sentence Formula, from Farquhar)

1. What you achieved: "We introduce...", "We prove...", "We demonstrate..."
2. Why this is hard and important
3. How you do it (with specialist keywords for discoverability)
4. What evidence you have
5. Your most remarkable result

Delete generic openings like "Large language models have achieved remarkable success..."

#### Introduction (1-1.5 pages max)

- 2-4 bullet contribution list (max 1-2 lines each)
- Clear problem statement
- Brief approach overview
- Methods should start by page 2-3

#### Methods

- Enable reimplementation: pseudocode, all hyperparameters, architectural details
- Present final design decisions; ablations go in experiments

#### Experiments

For each experiment, explicitly state:
- What claim it supports and how it connects to the main contribution
- Experimental setting (details in appendix)
- What to observe: "the blue line shows X, which demonstrates Y"

Requirements: error bars with methodology, hyperparameter search ranges, compute budget, seed info.

#### Related Work

Organize **methodologically**, not paper-by-paper:
- Good: "One line of work uses X [refs] whereas we use Y because..."
- Bad: "Smith et al. introduced X. Jones et al. introduced Y."

Cite generously — reviewers likely authored relevant papers.

#### Limitations (REQUIRED)

All major conferences require this. Honesty helps:
- Reviewers are instructed not to penalize honest limitation acknowledgment
- Pre-empt criticisms by identifying weaknesses first

## Writing Style

### Sentence-Level Clarity (Gopen & Swan)

| Principle | Rule |
|-----------|------|
| Subject-verb proximity | Keep subject and verb close |
| Stress position | Place emphasis at sentence ends |
| Topic position | Put context first, new info after |
| Old before new | Familiar info → unfamiliar info |
| Action in verb | Use verbs, not nominalizations |

### Word Choice (Lipton, Steinhardt, Perez)

- **Be specific**: "accuracy" not "performance"
- **Eliminate hedging**: Drop "may" and "can" unless genuinely uncertain
- **Consistent terminology**: One term per concept throughout
- **Delete filler words**: "actually", "basically", "very", "quite", "essentially"
- **Minimize pronouns**: "This result shows..." not "This shows..."

## Conference Requirements

### ML/AI Venues

| Conference | Pages | Key Requirement |
|------------|-------|-----------------|
| NeurIPS | 9 | Mandatory checklist |
| ICML | 8 (+1 camera-ready) | Broader Impact required |
| ICLR | 9 (+1 camera-ready) | LLM disclosure required |
| ACL | 8 (long) | Limitations section mandatory |
| AAAI | 7 (+1 camera-ready) | Strict style file |

### Systems Venues

| Conference | Pages | Template |
|------------|-------|----------|
| OSDI | 12 (+2 camera-ready) | USENIX |
| NSDI | 12 | USENIX |
| ASPLOS | 12 | ACM SIGPLAN |
| SOSP | 12 | ACM SIGPLAN |

**Universal**: double-blind, references don't count, appendices unlimited but optional for reviewers, LaTeX required.

## LaTeX Template Setup

When starting from a template:
1. Copy entire template directory to new project
2. Verify template compiles as-is before any changes
3. Read template example content to understand structure
4. Replace content section by section
5. Clean up template artifacts only at the end

## De-AI Editing

Before submission, check for and remove common AI writing patterns:
- Overuse of "delve", "crucial", "landscape", "paradigm", "novel"
- Excessive hedging ("it is worth noting that", "it should be mentioned")
- Generic topic sentences that add no information
- Repetitive sentence structures (Subject-Verb-Object monotony)
- Hollow transitions ("Furthermore", "Moreover", "Additionally" in sequence)

## Output Contract

- Produce LaTeX source with proper `\cite{}`, `\ref{}`, `\label{}`
- Include BibTeX entries for all citations (verified via search)
- Mark unverified citations as `TODO: Verify`
- Preserve existing macros and formatting conventions
- Follow the target venue's style file and conventions

## Safety Boundaries

- Never fabricate experimental results, metrics, or baselines
- Never invent citations or authors
- Never claim contributions the research doesn't support
- Always disclose when content is AI-assisted if required by venue
