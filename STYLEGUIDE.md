# GraspingAI — Style Guide (v0.3)

This guide explains **how the site’s CSS system works**: how to change typography, spacing, and layout, and how to use the provided utility classes. It reflects all updates from your vertical rhythm and spacing system (v0.3).

---

## 1. Design Tokens Overview

### Colors
All color variables are defined in `:root` in `styles.css`.

| Token | Description |
|--------|-------------|
| `--bg` | Page background |
| `--panel` | Section background or footer panel |
| `--ink` | Main body text color |
| `--muted` | De-emphasized grey text |
| `--accent` | Accent color (buttons, highlights, links) |
| `--border` | Light divider color |

### Type Scale
Fluid and mobile-first via `clamp()`:
```
--step--1 → Small (UI, captions)
--step-0  → Base body
--step-1  → Lead text
--step-2  → h3
--step-3  → h2
--step-4  → h1
```

### Spacing Scale
Defined in `:root` under spacing tokens:
```
--space-2xs: 0.25rem;  /* 4px */
--space-xs:  0.5rem;   /* 8px */
--space-sm:  0.75rem;  /* 12px */
--space-md:  1.25rem;  /* 20px */
--space-lg:  2rem;     /* 32px */
--space-xl:  3rem;     /* 48px */
--space-2xl: 4rem;     /* 64px */
--section-padding: var(--space-2xl);
```
These tokens control all vertical rhythm and spacing.

---

## 2. Typography Utilities

| Class | Effect |
|--------|--------|
| `.text-base` | Normal body text (`var(--step-0)`) |
| `.text-lead` | Larger lead paragraph (`var(--step-1)`) |
| `.text-sm` | Small text (`var(--step--1)`) |
| `.muted` | Greyed, de-emphasized text (uses `--muted`) |
| `.primary` | Forces normal text color (counteracts muted) |
| `.text-center` / `.text-left` | Alignment helpers |

**Example:**
```html
<p class="lead text-lead primary">GraspingAI is your strategic partner...</p>
<p class="text-base muted">Founded by Aaron Kagan (ex-Google, Meta)...</p>
```

> `.muted` changes only color — it does *not* increase size.

---

## 3. Vertical Rhythm & Spacing System

### Element Defaults
```css
h1, h2, h3, p, ul, ol, blockquote { margin-top: 0; }

h1 { margin-bottom: var(--space-sm); line-height: 1.1; }
h2 { margin-bottom: var(--space-xs); line-height: 1.2; }
h3 { margin-bottom: var(--space-xs); line-height: 1.3; }

p, ul, ol, blockquote {
  margin-bottom: var(--space-md);
  line-height: var(--lh-text);
}
```

### Section-Level Rhythm
```css
.section { padding: var(--section-padding) 0; }
.section--alt { padding: calc(var(--section-padding) * 0.8) 0; }
```

### Hero Section
```css
.hero h1 { margin-bottom: var(--space-xs); }
.hero .subhead { margin-top: 0; margin-bottom: var(--space-md); }
.hero .cta { margin-top: var(--space-sm); gap: var(--space-sm); }
```

### Lists and Grids
```css
.grid.two { gap: var(--space-md); }
.container-narrow ul { margin-bottom: var(--space-md); }
#why.section--center ul { margin: var(--space-md) auto; }
#why.section--center li { margin-bottom: var(--space-sm); }
```

---

## 4. Buttons

| Variant | Class | Description |
|----------|--------|-------------|
| Primary | `.btn.primary` | Filled accent background |
| Secondary | `.btn.secondary` | Outline button (inset border) |
| Small | `.small` | Compact version for nav or inline use |

**Example:**
```html
<a class="btn primary" href="#">Book a Call</a>
<a class="btn secondary" href="#">Learn More</a>
```

**Hover Effects:**
- Primary: `color-mix()` brightening + slight lift
- Secondary: semi-transparent accent background on hover

IDs like `#nav-connect` or `#meeting-options` reuse the secondary style safely (Umami tracking unaffected).

---

## 5. Story / Alt Section

Used for content bands that contrast slightly from main background.

**HTML Pattern:**
```html
<section class="section section--alt">
  <div class="container-narrow">
    <h2>The Story</h2>
    <p>Intro paragraph...</p>
    <blockquote>“Key quote or testimonial.”</blockquote>
  </div>
</section>
```

**Styling Highlights:**
```css
.section--alt blockquote {
  color: var(--text);
  border-left: 3px solid rgba(15,23,42,0.3);
  font-style: italic;
  font-size: var(--step-0);
}
```

> Dark mode automatically adapts border and text color.

---

## 6. Layout Helpers

| Class | Effect |
|--------|--------|
| `.section--center` | Centers section heading & container |
| `.text-left` inside `.section--center` | Keeps body content left-aligned |
| `.container-narrow` | Restrains max width (68ch) |
| `.grid.two` | 2-column grid, collapses at 900px |
| `.cta` | Evenly spaced call-to-action row |

---

## 7. Responsive Breakpoints
```css
@media (max-width: 900px) { .grid.two { grid-template-columns: 1fr; } }
@media (max-width: 720px) {
  .menu { display: none; }
  .menu-toggle { display: block; }
  .brand-logo { height: 24px; }
  .hero-logo-img { max-width: 260px; }
  .hero { padding: 4rem 1rem; }
}
```

---

## 8. Maintenance Guidelines
- Use `var(--step-*)` for all font sizes.
- Use `var(--space-*)` for all margins, gaps, and paddings.
- Never hard-code pixel values.
- Prefer `.text-lead.primary` (highlight) and `.text-base.muted` (supporting) for hero text pairs.
- Keep `.section` padding consistent using `--section-padding`.

---

## 9. Example — Hero Block
```html
<section class="hero">
  <div class="container hero-inner">
    <h1>Clear view in the age of AI.</h1>
    <p class="subhead text-lead primary">
      Focus on what matters most, move with confidence.
    </p>
    <p class="text-base muted">
      Founded by Aaron Kagan (ex-Google, Meta)...
    </p>
    <div class="cta">
      <a class="btn primary" href="#">Meeting Options</a>
      <a class="btn secondary" href="#">Explore Services ↓</a>
    </div>
  </div>
</section>
```

---

## 10. Changelog

**v0.3 (2025-10-29)**  
- Introduced full spacing token system (`--space-*`)  
- Applied consistent vertical rhythm for all sections  
- Tightened hero spacing and standardized CTA gaps  
- Added `.text-base`, `.muted`, `.primary` utilities  
- Consolidated grid/list rhythm under tokens  
- Updated docs to reflect final production CSS