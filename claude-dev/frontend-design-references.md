# Frontend Design Skill References

References collected for improving the `dev-frontend-design` skill, with a focus on building data-dense developer tools like [VibeLens](https://github.com/anthropics/VibeLens) (React 19 + TypeScript + Tailwind CSS dark theme).

## References

### 1. Anthropic Official `frontend-design` Skill

**Link:** [github.com/anthropics/claude-code/.../frontend-design/SKILL.md](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md)

The canonical frontend-design skill from Anthropic (277K+ installs). Addresses "distributional convergence" where Claude defaults to statistically average design choices (Inter font, purple gradient, card layout). Injects a design-thinking phase before code generation, requiring commitment to a bold aesthetic direction.

**Techniques:** Design thinking framework (purpose, tone, constraints, differentiation) with 11 aesthetic directions (brutalist, retro-futuristic, editorial, etc.). Explicit bans on overused fonts (Inter, Roboto, Arial). Typography pairing, CSS variable theming, staggered motion reveals, asymmetric spatial composition.

| Pros | Cons |
|------|------|
| Well-crafted anti-convergence framing | Pure aesthetics -- no component architecture |
| Strong typography and color guidance | No performance or accessibility coverage |
| Proven at scale (277K+ installs) | Bans system fonts that some projects intentionally use |
| Concise (~400 tokens) | No data visualization guidance |
| Forces intentional design decisions upfront | Not tailored to dark-mode-only or data-dense UIs |

---

### 2. Anthropic "Prompting for Frontend Aesthetics" Cookbook

**Link:** [platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics](https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics)

The complete prompt engineering guide from Anthropic for frontend aesthetics. Contains the exact `DISTILLED_AESTHETICS_PROMPT` and isolated sub-prompts for typography, theme constraints, and base system prompts. Three core strategies: guide specific design dimensions individually, reference design inspirations, and explicitly call out common defaults to avoid.

**Techniques:** Isolated sub-prompts for targeted control. Typography-only prompt with font recommendations by aesthetic category (Code: JetBrains Mono; Editorial: Playfair Display; Startup: Clash Display; Technical: IBM Plex). Extreme weight ranges (100/200 vs 800/900, not 400 vs 600). Size jumps of 3x+. Theme constraint prompts (e.g., Solarpunk palette). Concatenation pattern for composing prompts.

| Pros | Cons |
|------|------|
| Granular sub-prompts for each design dimension | Focused on standalone HTML artifacts, not component systems |
| Concrete font recommendations by category | No React/TypeScript patterns |
| Composable prompt concatenation pattern | Assumes generating from scratch, not extending existing design systems |
| Teaches extreme typographic contrast | No accessibility or performance guidance |

---

### 3. Anthropic Blog -- "Improving Frontend Design Through Skills"

**Link:** [claude.com/blog/improving-frontend-design-through-skills](https://claude.com/blog/improving-frontend-design-through-skills)

Conceptual explanation of why the frontend-design skill works. Treats distributional convergence as a "steerability opportunity" -- Claude is highly responsive to targeted guidance when given domain-specific context at the right abstraction level.

**Techniques:** ~400-token skill with meta-commentary framing. Four axes of improvement: typography, color/theme, motion, backgrounds. Dynamic context loading -- specialized guidance activates just-in-time for frontend tasks. References complementary `web-artifacts-builder` skill for React + Tailwind + shadcn/ui bundling.

| Pros | Cons |
|------|------|
| Explains the "why" behind skill design | Conceptual, not directly actionable |
| Validates ~400-token skill size as effective | No code examples or patterns |
| Introduces dynamic context loading concept | Blog format, not a reusable artifact |
| Demonstrates measurable quality improvements | Limited to aesthetics axis |

---

### 4. Vercel Agent Skills (`web-design-guidelines` + `react-best-practices`)

**Link:** [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md)

Vercel's official skills for auditing and enforcing frontend quality. Two complementary skills: `web-design-guidelines` validates against 100+ accessibility and UX rules; `react-best-practices` provides 57 performance optimization rules prioritized by impact.

**Techniques:**

- `web-design-guidelines`: ARIA attributes, visible focus states, labeled inputs, touch target sizes, reduced-motion support, semantic HTML, keyboard navigation, heading hierarchy, dark mode, typography, images, performance, internationalization. Four-step workflow: retrieve guidelines, read files, validate rules, report results.
- `react-best-practices`: Request waterfalls first, then bundle size, server-side performance, data fetching, re-renders, rendering, JavaScript performance.
- `composition-patterns`: Compound components, context providers, replacing boolean prop proliferation.

| Pros | Cons |
|------|------|
| 100+ concrete, auditable rules | Audit-focused, not generation-focused |
| Covers accessibility, performance, semantic HTML | Fetches rules from remote URL (fragile dependency) |
| Prioritized by impact (perf rules) | No aesthetic or design guidance |
| Compound component patterns for clean APIs | Vercel/Next.js biased (some rules less relevant for Vite) |
| Keyboard navigation and focus management | Rules are generic, not project-specific |

---

### 5. Community `frontend-patterns` Skill

**Link:** [github.com/affaan-m/everything-claude-code/.../frontend-patterns/SKILL.md](https://github.com/affaan-m/everything-claude-code/blob/main/skills/frontend-patterns/SKILL.md)

A comprehensive frontend patterns skill covering React, Next.js, and performant UIs at the code architecture level. Complements the aesthetics-focused official skill by teaching established component patterns, state management, performance optimization, and accessibility.

**Techniques:** Composition over inheritance, compound components via Context API, render props pattern. Custom hooks (`useToggle`, `useQuery`, `useDebounce`). Context + Reducer state management without external libraries. `React.memo()`, `useMemo()`, `useCallback()`, code splitting with `React.lazy()`, virtualization for long lists. Controlled forms with Zod schema validation. Error boundaries. Animation patterns via Framer Motion or CSS transitions.

| Pros | Cons |
|------|------|
| Covers real React architecture patterns | Generic patterns, not project-tailored |
| Custom hooks, state management, code splitting | Some patterns outdated for React 19 (e.g., forwardRef) |
| Virtualization for long lists (relevant for data-dense UIs) | No design system or theming guidance |
| Error boundaries for graceful failure | No TypeScript-specific patterns |
| Accessibility: keyboard nav, focus management, semantic HTML | No data visualization patterns |

---

### 6. DEV Community -- Skill Chaining Workflow

**Link:** [dev.to/blamsa0mine/claude-code-skills-install-ui-skills-build-a-frontend-design-workflow](https://dev.to/blamsa0mine/claude-code-skills-install-ui-skills-build-a-frontend-design-workflow-claude-code-cursorvs-4n43)

Practical guide for chaining multiple UI skills into a progressive refinement pipeline. Each skill refines the output of the previous one.

**Techniques:** Sequential skill chaining: (1) `/frontend-design` for design direction + code, (2) `/baseline-ui` to remove AI slop and improve spacing/typography/states, (3) `/fixing-accessibility` for keyboard/labels/focus/semantics, (4) `/fixing-motion-performance` to optimize motion and `prefers-reduced-motion` compliance. Covers skill storage locations (global `~/.claude/skills/` vs project `.claude/skills/`).

| Pros | Cons |
|------|------|
| Progressive refinement pipeline concept | Requires multiple separate skills to install |
| Each step addresses a specific quality dimension | Sequential execution is slow |
| Covers accessibility and motion performance | Individual skills are shallow |
| Practical installation and troubleshooting guide | UI skills pack (`ibelick/ui-skills`) may not be maintained |

---

### 7. Addy Osmani -- "My LLM Coding Workflow Going Into 2026"

**Link:** [addyosmani.com/blog/ai-coding-workflow/](https://addyosmani.com/blog/ai-coding-workflow/)

A senior Google Chrome engineer's complete LLM workflow including frontend-specific techniques, CLAUDE.md patterns, and quality assurance. Treats LLMs as "over-confident junior developers" requiring structured planning, context provision, and human accountability.

**Techniques:** CLAUDE.md with persistent coding preferences. Spec-first development (brainstorm `spec.md` before writing code). Chunking (one function/fix/feature at a time). Prompt plan files for sequenced execution. In-line examples (show similar existing code before requesting new). Context tools (`gitingest`, `repo2txt`). Dual-model reviews (second AI critiques the first). Hallucination prevention prompts. Chrome DevTools MCP for live browser inspection.

| Pros | Cons |
|------|------|
| Battle-tested workflow from a senior engineer | General workflow, not a reusable skill |
| Spec-first approach prevents wasted iterations | Frontend-specific advice is brief |
| Dual-model review catches more issues | Requires Chrome DevTools MCP setup |
| Chunking strategy reduces errors | Not directly translatable to SKILL.md format |
| Context tools for large codebases | Some tooling references may become outdated |

---

### 8. Builder.io -- "11 Prompting Tips for Building UIs That Don't Suck"

**Link:** [builder.io/blog/prompting-tips](https://www.builder.io/blog/prompting-tips)

Practical, tool-agnostic prompting tips for frontend UI generation. Focused on the feedback loop between human intent and AI output.

**Techniques:** Show the AI its rendered output (screenshot feedback loop). Reference specific file paths as pattern examples. Connect prompts to actual design system docs. Use Figma integration via MCP for exact fonts/colors/spacing. Work section-by-section (get design right before adding functionality). Explicit instructions ("Add a blue primary button labeled 'Login' in the top-right corner"). Start from existing resources rather than generating from scratch.

| Pros | Cons |
|------|------|
| "Show AI its own output" technique for self-correction | Requires visual feedback tools (screenshots) |
| Section-by-section workflow reduces complexity | Tool-specific integrations (Figma MCP) |
| Design system connection keeps consistency | Tips, not a structured skill |
| Practical and immediately actionable | No architecture or performance patterns |
| "Start from existing" philosophy prevents over-generation | Assumes access to design system documentation |

---

## Cross-Reference Matrix

| Technique | Ref 1 | Ref 2 | Ref 3 | Ref 4 | Ref 5 | Ref 6 | Ref 7 | Ref 8 |
|-----------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| Anti-convergence / anti-AI-slop | x | x | x | | | x | | |
| Typography guidance | x | x | | | | | | |
| Color / theming system | x | x | | x | | | | x |
| Motion / animation | x | x | | | x | x | | |
| Accessibility rules | | | | x | x | x | | |
| Performance optimization | | | | x | x | | | |
| React component patterns | | | | x | x | | | |
| State management | | | | | x | | | |
| Virtualization / data-dense UI | | | | x | x | | | |
| Design system integration | | | | | | | | x |
| Workflow / chaining | | | | | | x | x | x |
| Spec-first / planning | | | | | | | x | |
| Visual feedback loop | | | | | | | | x |

## Relevance to VibeLens

VibeLens is a data-dense developer tool with a consistent dark theme, centralized design tokens (`styles.ts`), and 20+ React components. The current skill (based on Ref 1) is aesthetics-only. Key gaps:

| Gap | Best Reference |
|-----|---------------|
| Data visualization (charts, heatmaps, flow diagrams) | None directly -- needs custom guidance |
| Performance (virtualization, lazy loading, debounce) | Ref 4 (Vercel), Ref 5 (community) |
| Accessibility (keyboard nav, focus, ARIA) | Ref 4 (Vercel), Ref 5 (community) |
| React 19 architecture (compound components, hooks) | Ref 5 (community) |
| Dark-mode-specific design | Ref 4 (Vercel, partial) |
| Extending existing design tokens (not overriding) | Ref 8 (Builder.io philosophy) |
