# GraspingAI — Style Guide (v0.2)

This guide explains **which CSS knobs to turn** to change specific content on the page, and **which HTML classes or IDs** to use to get the result you want.

---

## 1. Typography

### Scale (fluid via CSS variables)
Defined in `styles.css` under `:root`:

```
--step--1 → Small (UI, tables, footnotes)
--step-0  → Base (default body: p, li)
--step-1  → Lead (emphasis body, subheads)
--step-2  → h3
--step-3  → h2
--step-4  → h1
```

**To change body or heading sizes:**  
Edit the `--step-*` clamp values in `:root`. The whole site updates automatically.

### HTML → CSS mapping

| Purpose | HTML | CSS class / selector |
|----------|------|----------------------|
| Base body | `<p>`, `<li>` | uses `var(--step-0)` |
| Emphasis / Lead | `<p class="text-lead">` | uses `var(--step-1)` |
| Small text | `<p class="text-sm">` | uses `var(--step--1)` |
| Headings | `<h1>` → `--step-4`, `<h2>` → `--step-3`, `<h3>` → `--step-2` |

**To make a paragraph bigger or smaller:**  
Add or swap `.text-lead`, `.text-base`, or `.text-sm`.

**To center one line only:**  
Add `.text-center` or use an inline `style="text-align:center"`.

---

## 2. Colors

### Tokens (edit once → site-wide)
Defined in `:root` in `styles.css`:

```
--bg, --panel, --ink (body text), --muted, --accent, --border
```

**To change the site’s accent color:**  
Edit `--accent`. Buttons, links, outlines, and accents follow automatically.

**To dim secondary copy:**  
Add the `.muted` class (color only; size is inherited).

---

## 3. Layout & Alignment

### Containers
- `.container` → centered section, ~1100px max width.  
- `.container-narrow` → centered, ~820px max width.

**Centered section, left-aligned body example:**

```html
<section class="section section--center">
  <div class="container-narrow">
    <h2>Centered Heading</h2>
    <div class="text-left">
      <p>Left-aligned body text…</p>
    </div>
  </div>
</section>
```

### Grids
- `.grid.two` → two columns, collapses at ≤900 px.  
**To change breakpoint:** edit `@media (max-width: 900px)` in `styles.css`.

---

## 4. Buttons

### Variants

| Type | Class | Description |
|------|--------|-------------|
| Primary | `.btn.primary` | Filled accent background, light text |
| Secondary | `.btn.secondary` | Outline (inset stroke) |
| Small | `.small` | Reduces padding |

**To add or edit hover effects:**
- Primary → tweak color/brightness in `.btn.primary:hover`
- Secondary → tweak `background` alpha in `.btn.secondary:hover`

**To make a nav/utility link look like the outline button:**
Add `class="btn secondary small"` to the link, or use the existing `#nav-connect` / `#meeting-options` IDs.

**Tracking (Umami):**  
Styling never affects analytics. IDs remain intact and events still fire.

---

## 5. Story / Alt Section (Soft Contrast Band)

### HTML pattern

```html
<section id="story" class="section section--alt">
  <div class="container-narrow">
    <h2>The Story</h2>
    <p>Intro paragraph...</p>
    <blockquote>
      “A short pull quote or testimonial.”
    </blockquote>
  </div>
</section>
```

### CSS knobs
| Goal | Change this in `styles.css` |
|------|------------------------------|
| Adjust background tint | `.section--alt { background: … }` |
| Strengthen contrast of quote text | `.section--alt blockquote { color: var(--text); }` |
| Make quote larger | switch `font-size` → `var(--step-1)` |
| Soften border | change `border-left` alpha (default = 0.3) |

**Dark mode:** handled in the `@media (prefers-color-scheme: dark)` block automatically.

---

## 6. Links & Hovers

Global link styles live in the `a { … }` rule.  
To make links more/less visible, adjust the hover `color` or `border-bottom` opacity.

---

## 7. Imagery (Minimalist)

- Use responsive SVG or high-res PNGs: `max-width:100%; height:auto;`
- Keep imagery light, geometric, and mobile-safe.
- Background gradients preferred over raster textures.

---

## 8. HTML → CSS “Knob” Reference

| You want to... | Do this in HTML | Change this in CSS |
|-----------------|-----------------|--------------------|
| Emphasize a paragraph | `<p class="text-lead">` | adjust `--step-1` |
| Make small caption | `<p class="muted text-sm">` | adjust `--step--1` |
| Center a line | `<p class="text-center">` | none |
| Center section, left body | use pattern in §3 | none |
| Add two columns | wrap in `<div class="grid two">` | adjust breakpoint |
| Add filled CTA | `<a class="btn primary">` | tweak `.btn.primary:hover` |
| Add outline CTA | `<a class="btn secondary">` | tweak `.btn.secondary:hover` |
| Add nav CTA (tracked) | `<a id="nav-connect" class="btn small">` | edit `#nav-connect` rules |
| Add blockquote | `<blockquote>…</blockquote>` inside `.section--alt` | edit `.section--alt blockquote` |
| Change section width | `<div class="container[-narrow]">` | edit `.container` widths |

---

## 9. Accessibility & Motion

- Respects `prefers-reduced-motion`.  
- Buttons and links have visible focus styles (`:focus-visible`).  
- Maintain text contrast (use `var(--text)` for readable color).

---

## 10. Maintenance Rules

- Never hard-code font sizes (`px`, `rem`); always use `var(--step-*)`.
- Don’t reintroduce media-query font overrides for headings — the clamp scale handles it.
- Prefer utility classes (`.text-lead`, `.text-sm`, `.muted`, `.text-center`) for one-off tweaks.
- Keep sections centered with `.section--center` and `.container[-narrow]`.

---

## 11. Deprecated / Remove

- Custom font clamps (`clamp(...)`) inside components.  
- Hard-coded `font-size: 1.1rem` (use tokens).  
- Malformed `.kicker` nesting (replace with clean rule using `--step--1`).  
- Old responsive `h1` pixel override at 720 px.

---

## 12. Example Patterns

### “What We Do” (centered section + left body)
```html
<section id="services" class="section section--center">
  <div class="container-narrow">
    <h2>What We Do</h2>
    <p class="text-lead text-center">
      We design clarity and trust into complex AI systems.
    </p>
    <div class="text-left">
      <div class="grid two">…</div>
    </div>
  </div>
</section>
```

### Nav Outline CTA (tracked)
```html
<a id="nav-connect" class="btn small" href="https://cal.com/graspingai">Connect</a>
```

*(CSS gives it the outline style + hover; analytics unchanged.)*

---

## 13. Changelog

**2025-10-29**  
- Unified button hover behavior (lift + color-mix)  
- Fixed blockquote contrast (`color: var(--text)`)  
- Simplified `.section--alt` rules  
- Removed redundant font-size clamps  
- Added unified typography scale and utilities

---

