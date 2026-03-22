---
name: paper-research
description: "Systematic literature search, synthesis, and research gap analysis. Use when the user wants to survey a topic, find related work, build a literature review, identify research gaps, or prepare the background for a paper. Triggers on: literature review, related work, survey this topic, find papers on, research gap, what's the state of the art, systematic review, 文献综述, 找论文, 相关工作."
metadata:
  version: "1.0"
  last_updated: "2026-03-18"
---

# Paper Research — Literature Search & Synthesis

Systematic literature search and synthesis skill for academic research. Produces structured literature reviews with verified citations, gap analysis, and research positioning.

## Quick Start

```
Find related work on agent safety evaluation benchmarks
Survey recent papers on LLM alignment via RLHF
What's the state of the art in multi-agent cooperation?
```

## Trigger Conditions

**Triggers on**: literature review, related work, survey this topic, find papers on, research gap, state of the art, systematic review, background research, 文献综述, 相关工作, 研究综述

**Does NOT trigger on**:
- Writing a paper → use `paper-write`
- Reviewing/proofreading a paper → use `paper-audit`
- Reading a single paper for notes → use `note-paper`

## Modes

| Mode | When | Output |
|------|------|--------|
| `survey` (default) | Need comprehensive literature review on a topic | Structured review with themes, gaps, and synthesis |
| `quick` | Need a fast overview of a narrow topic | Annotated bibliography with brief synthesis (10-20 papers) |
| `related-work` | Drafting related work section for a specific paper | Organized related work text with citation keys |

## Workflow

### Phase 1: Scope Definition

1. Parse the user's research topic and clarify scope:
   - What specific aspect of the topic?
   - Time range (default: last 3 years for AI/CS, last 5 for other fields)
   - Target venues (e.g., NeurIPS, ICML, ACL, USENIX)
   - Any known seed papers to start from?

2. Formulate search queries:
   - Primary query: exact topic terms
   - Broadened query: related concepts and synonyms
   - Narrowed query: specific sub-problems
   - Author-based: key researchers in the area

### Phase 2: Literature Search

Execute searches using available tools:

1. **Web search**: Search for "[topic] site:arxiv.org", "[topic] survey", "[topic] benchmark"
2. **Semantic Scholar API** (if available): Query for papers, follow citation graphs
3. **Seed paper expansion**: From known papers, trace:
   - Papers they cite (backward search)
   - Papers that cite them (forward search)
   - Papers by the same authors

For each paper found, extract:
- Title, authors, venue, year
- Abstract summary (1-2 sentences)
- Key contribution
- Relevance to the user's topic (high/medium/low)

### Phase 3: Source Verification

**CRITICAL: Never hallucinate citations.**

For every paper included in the output:
- Verify it exists via web search or API
- Confirm authors, year, and venue are correct
- If a paper cannot be verified, mark it as `[UNVERIFIED — requires manual check]`

### Phase 4: Synthesis & Analysis

Organize findings into a structured review:

1. **Thematic grouping**: Cluster papers by approach, method, or sub-topic
2. **Timeline analysis**: How has the field evolved?
3. **Method comparison**: What approaches exist? What are their trade-offs?
4. **Gap analysis**: What hasn't been addressed? Where are the opportunities?
5. **Research positioning**: How does the user's work fit in?

### Phase 5: Output Compilation

Produce a structured document following this template:

```markdown
# Literature Review: [Topic]

## 1 Overview
Brief introduction to the research area and why it matters.

## 2 Search Methodology
- Databases searched: [list]
- Search queries: [list]
- Time range: [range]
- Inclusion criteria: [criteria]

## 3 Thematic Analysis

### 3.1 [Theme 1]
Discussion of papers in this theme, their contributions, and relationships.

### 3.2 [Theme 2]
...

## 4 Comparison of Approaches
| Method | Key Idea | Strengths | Limitations | Representative Papers |
|--------|----------|-----------|-------------|----------------------|

## 5 Research Gaps
Identified gaps and open questions in the literature.

## 6 Annotated Bibliography
For each paper:
- **[Authors (Year)]** *Title*. Venue.
  - Contribution: [1-2 sentences]
  - Relevance: [high/medium]

## Reference
Full citation list.
```

## Quality Standards

1. **Every citation must be verified** — no hallucinated references
2. **Balanced coverage** — include diverse perspectives and approaches
3. **Recency bias check** — don't ignore foundational older work
4. **Venue quality** — prioritize top-tier venues but include relevant workshop/preprint papers
5. **Synthesis over summary** — don't just list papers; analyze trends, compare methods, identify gaps

## Output Language

Follow the user's language. Academic terminology kept in English. If the user writes in Chinese, produce the review in Chinese following StudyNote CLAUDE.md formatting conventions.

## Related Work Mode Specifics

When mode is `related-work`:
- Output LaTeX-ready text with `\cite{}` placeholders
- Organize by methodology, not chronologically
- Explicitly position the user's work relative to existing approaches
- Include transition sentences between subsections
- Provide a BibTeX block with verified entries
