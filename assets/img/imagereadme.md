# Table explaining where and when to drop stuff in:
    https://docs.google.com/document/d/1_hyrqNKh595h9B3PEH8caU6aitTky6UpYrzC2XSPXYw/edit?tab=t.lpd6r17pribe

# Section backgrounds (put in /assets/img/sections/)

home-hero.avif – used by the hero (#top)

story-band.avif – optional soft texture behind the Story section (#story)

services-hero.avif – if you want a background for “What I Do” (#services)

who-hero.avif – optional for “Who I Work With” (#who)

contact-hero.avif – optional for “Contact” (#contact)

## To “turn on” a background for more sections, add a line in styles.css under the “Per-section variables” comment

css:
#services { --section-bg: url("/assets/img/sections/services-hero.avif"); }


and add with-bg to that section’s class:

html:
<section id="services" class="section section--center with-bg">

# Content images (put in /assets/img/content/)

shift.avif (with fallbacks shift.webp and shift.png) – the optional image in the Story section

Future diagrams/screenshots: use descriptive slugs, e.g.
    translation-layer-diagram.avif
    workflow-map.avif
    confidence-patterns-example.avif

Use the <picture> pattern I showed for any content image when you have AVIF/WebP/PNG.

# Social sharing image (put in /og/)

og-image.jpg – the 1200×630 social card your head tags already reference/comment about. 

/assets/
  /img/
    /sections/
      home-hero.avif
      story-band.avif
      services-hero.avif
      who-hero.avif
      contact-hero.avif
    /content/
      shift.avif
      shift.webp
      shift.png