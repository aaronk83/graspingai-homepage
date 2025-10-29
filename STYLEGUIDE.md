GraspingAI — Style Guide (v0.2)

This guide explains which CSS knobs to turn to change specific content on the page, and which HTML classes/ids to use to get the result you want.

1) Typography
Scale (fluid via CSS variables)

Defined in styles.css under :root:

--step--1  → Small (UI, tables, footnotes)
--step-0   → Base (default body: p, li)
--step-1   → Lead (emphasis body, subheads)
--step-2   → h3
--step-3   → h2
--step-4   → h1


To change body or heading sizes:
Edit the --step-* clamp values in :root. The whole site updates automatically.

HTML → CSS mapping

Base body: <p>, <li> → font-size: var(--step-0)

Lead paragraph: add .text-lead → font-size: var(--step-1)

Small text: add .text-sm → font-size: var(--step--1)

Headings: h1 → --step-4, h2 → --step-3, h3 → --step-2

To make a paragraph bigger/smaller:
Add or swap classes: .text-lead, .text-base, .text-sm.

To center only one line:
Add .text-center or use style="text-align:center" on that element.

2) Colors
Tokens (edit once → site-wide effect)

Defined in :root in styles.css:

--bg, --panel, --ink (body text), --muted, --accent, --border


To change the site’s accent color:
Update --accent only. Buttons, links, outlines, and accents will follow.

To dim secondary copy:
Use .muted (color-only class; size is inherited).

3) Layout & Alignment
Containers

.container → max-width ~1100px + side padding

.container-narrow → max-width ~820px (great for long-form)

To center a section block:
Add .section--center to the <section>.

Centered section, but left-aligned body:

<section class="section section--center">
  <div class="container-narrow">
    <h2>Centered Heading</h2>
    <div class="text-left">
      <p>Left-aligned body text…</p>
    </div>
  </div>
</section>


.text-left keeps paragraphs/lists left while staying within the same centered column width.

Grids

.grid two → two columns that collapse at ≤900px
To change the breakpoint: edit the @media (max-width: 900px) rule for .grid.two.

4) Buttons
Variants

Primary (filled): .btn.primary

Hover: brighter + slight lift

Secondary (outline): .btn.secondary

Outline is drawn with box-shadow: inset 0 0 0 1px var(--accent) to avoid clipping

Small size: add .small to either variant

To add hover feedback to any button:

Primary: tweak background: color-mix(...) or filter/transform in .btn.primary:hover

Secondary: tweak background alpha in .btn.secondary:hover and leave the inset stroke

To make a nav/utility link look like the secondary outline:
Give it id or classes and apply the same inset-stroke style (we use #nav-connect, #meeting-options to match current markup).
If you’d rather not use ids, just apply class="btn secondary small" in the HTML.

Tracking note:
IDs like #nav-connect are safe for Umami tracking. Styling doesn’t affect analytics.

5) Story / Alt Section (Soft Contrast Band)

Use on content bands that need a subtle change in tone.

HTML pattern

<section id="story" class="section section--alt">
  <div class="container-narrow">
    <h2>Story</h2>
    <p>Intro paragraph…</p>
    <blockquote>
      “A short pull-quote, testimonial, or key insight.”
    </blockquote>
  </div>
</section>


To adjust readability on the alt band:

Change background: .section--alt { background: … }

Blockquote color uses color: var(--text) for contrast (already set).

For emphasis size on blockquotes, switch font-size between var(--step-0) and var(--step-1) in .section--alt blockquote.

6) Links & Hovers

Global link styles: in the a { … } block.
To make links more/less pronounced: adjust border-bottom and color hover values.
Nav “Connect” hover: handled via #nav-connect:hover (or convert to .btn.secondary small if you prefer class-only).

7) Imagery (Minimalist)

Keep imagery light and responsive (SVGs, soft gradients, simple geometric shapes).

Place assets within sections inside .container/.container-narrow.

Use max-width: 100%; height: auto; for responsive images.

To add a subtle background to a hero/section:
Prefer radial-gradient(...) layers in CSS (already used in .hero) rather than raster images.

8) Quick Mapping — HTML → CSS knobs
Goal	HTML you write	CSS you change
Emphasize a paragraph	<p class="text-lead">...</p>	If needed, tune --step-1 in :root
Footnote text	<p class="muted text-sm">...</p>	None; uses tokens
Center one line only	<p class="text-lead text-center">...</p>	None
Centered section, left body	see pattern in §3	None (already supported)
Two-column content	Wrap with <div class="grid two">…</div>	Change breakpoint in @media (max-width: 900px)
Primary CTA	<a class="btn primary">...</a>	Hover in .btn.primary:hover
Outline CTA	<a class="btn secondary">...</a>	Outline & hover in .btn.secondary rules
Nav outline CTA (tracked)	<a id="nav-connect" class="btn small">Connect</a>	#nav-connect rules (or switch to class="btn secondary small")
Quote on alt band	<blockquote>…</blockquote> inside .section--alt	font-size token & color: var(--text) in .section--alt blockquote
Section width	<div class="container[-narrow]">	Edit .container/.container-narrow max-width
9) Accessibility & Motion

Respect prefers-reduced-motion (already included).

Ensure focus visibility: primary and secondary buttons have hover/focus states; add :focus-visible where needed.

10) Maintenance Rules (Please Follow)

Do not hard-code font sizes in px/rem; always use var(--step-*).

Do not reintroduce media-query font overrides for headings; the clamp() scale handles it.

Prefer utility classes (.text-lead, .text-sm, .muted, .text-center) for quick local tweaks.

Keep section centering consistent: use .section--center + .container[-narrow]; for left body, wrap content in .text-left.

11) What’s Deprecated / Should Be Removed

Any old rules that set explicit sizes (e.g., font-size: 1.1rem, or hero h1 fixed sizes at mobile).

Custom clamps inside components that duplicate the scale (e.g., clamp(...) on .section--alt h2).

Nested/typo rules (e.g., malformed .kicker block) — replace with a clean .kicker using --step--1.

12) Examples
A) “What We Do” (centered section + left body)
<section id="services" class="section section--center">
  <div class="container-narrow">
    <h2>What We Do</h2>
    <p class="text-lead text-center">We design clarity and trust into complex AI systems.</p>
    <div class="text-left">
      <div class="grid two">…</div>
    </div>
  </div>
</section>

B) Outline nav CTA with tracking
<a id="nav-connect" class="btn small" href="https://cal.com/graspingai">Connect</a>


(CSS gives it the outline style + hover without interfering with Umami.)