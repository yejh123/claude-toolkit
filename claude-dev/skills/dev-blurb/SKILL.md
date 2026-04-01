---
name: dev-blurb
description: "Write compelling, human-sounding blurbs that help people instantly understand what a software application does and why they should care. Use when the user needs a product description, README intro, app store description, elevator pitch, social media post, tagline, or any short text explaining a tool/app/library. Triggers on: write a blurb, product description, README intro, elevator pitch, app description, explain my app, describe this project, tagline, one-liner, what does this do, product copy, marketing copy."
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Agent
metadata:
  version: "1.0"
  last_updated: "2026-03-29"
---

# Dev Blurb — Application Copy That Sounds Human

A blurb has one job: make someone who has never heard of this thing understand what it does and want to try it, in under 30 seconds.

The enemy is AI-generated descriptions that could describe any product if you swap the name. They use the same adjectives, the same structure, the same empty promises. They sound like a press release committee wrote them — polished, unanimous, and utterly forgettable.

The bar: read your blurb aloud. If it sounds like it came from a template, rewrite it. If a coworker would say "that sounds like ChatGPT wrote it," rewrite it. Good blurbs sound like a specific human with opinions wrote them about a specific product they actually understand.

## Anti-AI-Smell Rules

This is not a suggestion list. These are hard constraints applied to every blurb you write.

### Banned Words and Phrases

NEVER use any of these. Not "avoid" — never.

| Category | Banned |
|---|---|
| Adjective crutches | seamless, robust, cutting-edge, state-of-the-art, innovative, next-generation, powerful, comprehensive, streamlined, groundbreaking, intuitive, scalable |
| Verb crutches | leverage, unlock, unleash, empower, revolutionize, transform, elevate, supercharge, harness, navigate, streamline, optimize (as marketing verb) |
| Filler openers | "In today's...", "In the world of...", "Whether you're... or...", "Say goodbye to...", "Designed to enhance...", "Introducing..." |
| Vague nouns | game-changer, one-stop solution, best-in-class, end-to-end, complexities, realm, journey, ecosystem, paradigm, synergy |
| Empty promises | "takes it to the next level", "like never before", "the future of", "reimagining", "redefining" |

### Voice Rules

1. **Write like lunch, not a press release.** Explain it the way you would to a smart colleague over lunch — casual, direct, opinionated. Not like you are drafting copy for a billboard.
2. **One concrete detail per blurb, minimum.** A number, a file name, a real scenario, a benchmark, a comparison. "Finds unused deps in 2 seconds" beats "fast dependency analysis" every time.
3. **Vary sentence length deliberately.** Short punchy fragment. Then a longer sentence that unpacks it and gives context. Monotone rhythm is an AI tell.
4. **Take a stance.** Say what the tool is good at AND what it is not trying to be. "Not a linter — it only cares about what you import but never use." Opinions signal a real author.
5. **Allow one imperfection per blurb.** A dash, a parenthetical aside, a sentence fragment, an em dash interruption. Humans do not write in perfect parallel structure.
6. **Never start with the product name.** Start with the problem or the payoff. The product name goes in the second sentence at the earliest.

### Self-Test (Run After Every Draft)

Check each sentence: could this sentence appear unchanged in any other product's blurb? If yes, it is too generic — replace it with something specific to THIS product.

- Any banned words? Remove them.
- Any sentence that works for any product? Replace with a specific detail.
- All sentences the same length? Vary them.
- At least one concrete number or metric in each variant? Add one if missing.
- Does it sound like a press release? Rewrite until it sounds like a person.

## Workflow — Intake First, Write Second

NEVER generate blurbs immediately. Always go through intake first. The quality of a blurb is capped by how well you understand the product AND the context it will be used in.

### Step 1: Scan (if codebase available)

If the user provides or is working in a codebase, silently scan before asking questions:
- `package.json`, `pyproject.toml`, `Cargo.toml`, or equivalent for project metadata
- `README.md` for existing description and stated purpose
- Main entry point for what the code actually does
- Test files for usage patterns and real-world scenarios

Use what you find to pre-fill your understanding and ask smarter questions.

### Step 2: Ask the User

Ask these questions using `AskUserQuestion`. Group them into 1-2 rounds — do not bombard the user with 10 questions one at a time.

**Round 1 — Context and audience** (ask all at once):

1. **Where will this blurb appear?** Options: GitHub README, landing page / Product Hunt, social media (Twitter/LinkedIn), pitch deck / proposal, app store / marketplace, other. This determines which variant(s) to generate.
2. **Who reads it?** Options: developers, technical PMs / team leads, non-technical stakeholders / executives, general public / end users. This determines vocabulary and framing.
3. **What tone?** Options: developer-casual (like sharing a cool find), professional but human (conference talk), enterprise-formal (procurement doc), playful / witty.

**Round 2 — Product specifics** (ask only what you could not extract from the codebase):

4. **One-sentence description**: "What does this do?" — if you scanned the codebase, propose your understanding and ask the user to confirm or correct it.
5. **The pain**: "What was annoying or broken before this existed?" — skip if the README already explains the motivation.
6. **Key differentiator**: "What makes this different from [obvious alternative]?" — name the alternative if you can identify it.
7. **A concrete number**: "Do you have a speed benchmark, user count, file size, or any quantifiable metric?" — skip if you found one in the codebase.

**What to skip**: If you extracted a clear answer from the codebase scan, confirm it briefly ("I see from your README that this is a CLI tool for X — correct?") instead of asking from scratch. Do not ask questions you already know the answer to.

### Step 3: Generate the Right Variant(s)

Based on the user's answers, generate ONLY the variant(s) that match their stated platform. If they said "GitHub README," produce the README Blurb — not all five. If they said "social media," produce the Social Post.

If the user picks multiple platforms, generate one variant per platform. If unsure or the user says "all of them," then generate all five.

## Variant Catalog

Reference specifications for each variant. Generate only the ones the user needs.

### Variant A: Elevator Pitch

**Context**: GitHub subtitle, social bio, answer to "what do you work on?"
**Length**: 1-2 sentences, under 30 words
**Tone**: Direct, no setup, no context — just the answer

Formula: [What it does] + [key differentiator or metric].

No warm-up. No "it's a tool that..." — just say what it does.

Example (for "depclean", a CLI that finds unused Python dependencies):

> Finds unused dependencies in your Python projects. Scans your entire virtualenv in under 2 seconds — catches what pip-audit misses.

### Variant B: README Blurb

**Context**: The paragraph right below your project name on GitHub
**Length**: 50-80 words, 1 paragraph
**Tone**: Informative, specific, a bit more room to breathe

Structure: Problem (1 sentence) → Introduce the tool (1 sentence) → Strongest "why bother" hook (1-2 sentences).

Example:

> Your `requirements.txt` says you need 47 packages. You actually import 31. The rest are dead weight — slowing installs, growing your attack surface, and making audits pointless. depclean reads your source files and cross-references them against installed packages using static analysis (no code execution). Run it once, get a list, delete what you don't need. Average scan: 1.8 seconds on a 200-package project.

### Variant C: Landing Page

**Context**: Marketing page, Product Hunt, documentation landing page
**Length**: 100-150 words, 2-3 short paragraphs
**Tone**: Hook-driven, benefits-first, mobile-friendly (short paragraphs, whitespace)

Structure:
- Para 1: Name the pain, introduce the product as the fix
- Para 2: How it works (1 sentence) + what makes it different
- Para 3: Who it is for + trust signal or CTA

Example:

> Every Python project accumulates dependencies it no longer uses. They bloat your install, expand your vulnerability surface, and make `pip freeze` output meaningless. You could audit by hand — or let depclean do it in seconds.
>
> depclean uses static analysis to compare your import statements against your installed packages. No code execution, no config files, no false positives from dynamic imports (it handles those too). One command, one clean list of packages you can safely remove.
>
> Built for developers who actually read their dependency lists. Works with pip, Poetry, and PDM. 340+ stars on GitHub — try `pip install depclean` and run it on your messiest project.

### Variant D: Pitch Deck Slide

**Context**: Investor deck, internal proposal, tech talk slide
**Length**: 3-5 bullet points
**Tone**: Data-first, scannable — someone glancing during a meeting

Each bullet: [Hard fact or metric] — [what it means].

Example:

> - **47 deps installed, 31 actually used** — the average Python project carries 34% dead weight
> - **1.8s average scan time** — static analysis on a 200-package project, no code execution
> - **Zero config** — point it at a project, get results. No TOML files, no YAML, no setup
> - **Handles dynamic imports** — AST-level analysis catches `importlib` and `__import__` patterns
> - **340+ GitHub stars in 3 months** — organic growth, no marketing spend

### Variant E: Social Post

**Context**: Twitter/X, LinkedIn, Mastodon
**Length**: Under 280 characters
**Tone**: Developer sharing a cool find, not a marketing team launching a campaign

Structure: Hook → what → why → link. Contractions, casual tone, maybe a dash of surprise.

Example:

> TIL my project had 16 unused dependencies. depclean found them in 2 seconds flat — static analysis, no running my code. Just `pip install depclean && depclean .` [link]

## Output Format

Present each requested variant under a clearly labeled header. Only include the variants the user asked for.

```
## [Variant Name]
[blurb text]
```

If multiple variants were requested, separate them with headers. After generating, run the self-test silently — fix any issues before presenting. The output the user sees should already be clean.

After presenting, ask: "Want me to adjust the tone, swap a detail, or generate a variant for a different platform?"

## Adaptation

- **User names competitors** → position against them explicitly. "Unlike X, this does Y." Concrete contrast, not vague superiority.
- **User provides an existing blurb for improvement** → skip intake Round 1 (you already know the context). Identify specific AI-smell issues (banned words, generic sentences, missing specifics), fix them, preserve any good concrete details. Show before/after so the user sees what changed and why.
- **User gives enough context upfront** → if the user's initial message already answers the intake questions (platform, audience, what it does), skip redundant questions. Confirm your understanding briefly and go straight to writing.
- **User says "just write something"** → ask at minimum: where will this appear? That single answer determines length, structure, and tone. Everything else you can infer or ask after the first draft.
