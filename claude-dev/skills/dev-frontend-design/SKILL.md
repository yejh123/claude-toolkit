---
name: dev-frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality, solid architecture, and accessible, performant code. Use this skill when the user asks to build web components, pages, dashboards, data visualizations, or applications. Also use when the user is designing UI layouts, creating interactive widgets, building admin panels, implementing dark/light themes, or working on any frontend that needs to look polished and work well. Covers React (primary), Vue, Svelte, and vanilla HTML/CSS/JS. Generates creative, well-architected code that avoids generic AI aesthetics.
---

Build production-grade frontend interfaces that are visually distinctive, well-architected, accessible, and performant. Default to React + TypeScript + Tailwind CSS unless the user specifies otherwise.

## Before Coding

**Existing codebase?** Read the project's design tokens, component patterns, and styling conventions first. Extend and match what's there — don't override or introduce conflicting patterns.

**Greenfield?** Commit to a clear aesthetic direction before writing code. Consider: who uses this, what's the tone (minimal, editorial, brutalist, retro-futuristic, industrial, playful, luxury, etc.), and what makes it memorable. Intentionality matters more than intensity — bold maximalism and refined minimalism both work when executed with precision.

## Architecture

Build components that compose cleanly:

- **Composition over inheritance.** Favor compound components (`<Select>`, `<Select.Trigger>`, `<Select.Content>`) for complex UI with multiple configurable parts. This keeps APIs clean and avoids boolean-prop sprawl.
- **Custom hooks** for reusable logic (`useDebounce`, `useMediaQuery`, `useIntersectionObserver`). Extract when two components share the same stateful pattern.
- **State management:** local `useState` for component state, Context + `useReducer` for shared state that crosses 2+ levels. Reach for external stores only when Context genuinely becomes a bottleneck.
- **Error boundaries** around independently-failing sections (data panels, charts, third-party widgets). Show a graceful fallback rather than crashing the entire page.
- **TypeScript strictly.** Discriminated unions for variant props, generic components where the type flows from data, `as const` for literal config objects.

## Aesthetics

Design with intent — every visual choice should reinforce the interface's purpose and tone.

- **Typography:** Pair a distinctive display font with a refined body font. Use extreme contrast: weight 100–200 vs 700–900, size jumps of 3x+. Recommended by category — Code: JetBrains Mono, Fira Code; Editorial: Playfair Display, Fraunces; Technical: IBM Plex family; Startup: Clash Display, Cabinet Grotesk. System fonts are fine when chosen deliberately (e.g., for a native-feeling tool) — the problem is defaulting to them without thought.
- **Color & Theme:** Define a cohesive palette through CSS variables or Tailwind config. A dominant color with one sharp accent outperforms a timid, evenly-distributed palette. For dark themes: ensure sufficient contrast ratios, use subtle elevation through lighter surface tones rather than shadows alone.
- **Motion:** CSS transitions and animations first; JS animation libraries only when CSS can't express the interaction. One well-orchestrated page load with staggered reveals creates more delight than scattered micro-interactions. Always respect `prefers-reduced-motion`.
- **Spatial composition:** Break out of predictable grids when it serves the content. Asymmetry, overlap, diagonal flow, generous negative space, or controlled density — choose based on the information hierarchy, not just what "looks different."
- **Atmosphere:** Gradient meshes, noise textures, layered transparencies, grain overlays, decorative borders — use sparingly and only when they reinforce the aesthetic. A clean interface with perfect spacing can be more striking than one loaded with effects.

## Performance

- **Virtualize long lists** (hundreds+ items). Use `react-window`, `@tanstack/virtual`, or equivalent — rendering thousands of DOM nodes kills scroll performance in data-dense UIs.
- **Code split** heavy routes and large components with `React.lazy()` + `Suspense`. Load visualization libraries, code editors, and markdown renderers on demand.
- **Debounce** search inputs, resize handlers, and anything triggering expensive re-computation (300ms is a good default).
- **Avoid request waterfalls.** Fetch independent data in parallel. Prefetch or cache-warm data the user is likely to need next.
- **Memo judiciously.** `React.memo()` and `useMemo()` for components/computations that re-render frequently with unchanged props — but don't wrap everything reflexively. Profile first.

## Accessibility

Accessibility isn't a polish step — build it in from the start, because retrofitting it later costs much more effort.

- **Semantic HTML:** Use `<nav>`, `<main>`, `<section>`, `<button>`, `<dialog>` — not `<div onClick>`. Maintain a logical heading hierarchy (`h1` → `h2` → `h3`).
- **Keyboard navigation:** Every interactive element must be reachable and operable via keyboard. Trap focus inside modals. Manage focus when content changes dynamically.
- **Visible focus states:** Style `:focus-visible` distinctly — don't remove outlines without replacing them. Users navigating by keyboard need to see where they are.
- **ARIA:** Add `aria-label` on icon-only buttons, `aria-expanded` on toggles, `role` on custom widgets. But prefer native HTML semantics over ARIA — `<button>` beats `<div role="button">`.

## Avoid

- Generic "AI slop": purple gradients on white, card grids with rounded corners and drop shadows, the same layout every time
- Defaulting to Inter/Roboto/Arial without considering the project's character
- Prop drilling through 4+ levels — restructure with composition or context
- Inline styles when a design token system exists
- Premature abstraction of UI components — extract shared components after you see the pattern repeat, not before
