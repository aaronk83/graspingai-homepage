# Quick Reference: Swapping Background Images

This is a quick cheat sheet for changing background images on your site.

## 🎯 Current Image Setup

Your site uses **data attributes** to assign background images to sections:

| Section | HTML Attribute | CSS Rule | Image File |
|---------|---------------|----------|------------|
| Hero | `data-bg="home-hero"` | `.hero[data-bg="home-hero"]` (around line 191) | `assets/img/sections/home-hero.avif` |
| Story | `data-bg="story-band"` | `#story[data-bg="story-band"]` (around line 349) | `assets/img/sections/story-band.avif` |

## 🔄 Quick Swap (3 Steps)

### Method 1: Replace the File (Fastest)

1. **Find your current image**:
   - Hero: `assets/img/sections/home-hero.avif`
   - Story: `assets/img/sections/story-band.avif`

2. **Replace it** with your new image (same filename):
   ```bash
   # Copy your new image over the old one
   cp /path/to/new-hero.avif assets/img/sections/home-hero.avif
   ```

3. **Save** - Browser auto-reloads! ✨

### Method 2: Add New Image and Update CSS

1. **Add your image** to `assets/img/sections/`:
   ```bash
   cp /path/to/your-image.avif assets/img/sections/my-new-hero.avif
   ```

2. **Update CSS** in `styles.css`:

   **For Hero:**
   ```css
   /* Find around line 191 */
   .hero[data-bg="home-hero"] {
     background-image: url("assets/img/sections/my-new-hero.avif");
     background-size: cover;
     background-position: center;
     background-repeat: no-repeat;
   }
   ```

   **For Story:**
   ```css
   /* Find around line 349 */
   #story[data-bg="story-band"] {
     background-image: url("assets/img/sections/my-new-story.avif");
     background-position: center top; /* Adjust if needed - see positioning section */
     background-size: cover;
   }
   ```

3. **Save** - Done!

---

## 🖼️ Image Format Options

Your CSS accepts any image format. Here's what works best:

- ✅ **AVIF** - Best quality/size ratio (recommended)
- ✅ **WebP** - Good alternative, wider support
- ✅ **JPG** - Universal, larger file size
- ✅ **PNG** - Good for graphics, larger for photos

**Tip**: Use `.avif` or `.webp` for faster loading. Convert at [squoosh.app](https://squoosh.app/)

---

## 🎨 Image Positioning & Overlay

### Adjust the overlay darkness (Hero section):

The hero has a dark overlay for text readability. Edit in `styles.css`:

```css
/* Around line 199 - make it darker (increase .45) */
.hero[data-bg="home-hero"]::before {
  background: linear-gradient(to bottom, rgba(11,18,32,.45), rgba(11,18,32,.45));
  /* ↑ change .45 to .55 or .65 for darker overlay */
}
```

### Change image position:

**Hero section** (around line 191):
```css
.hero[data-bg="home-hero"] {
  background-image: url("assets/img/sections/home-hero.avif");
  background-position: center; /* Try: top, bottom, center top, center bottom, 50% 30% */
  background-size: cover; /* Try: contain to fit entire image */
}
```

**Story section** (around line 349):
```css
#story[data-bg="story-band"] {
  background-image: url("assets/img/sections/story-band.avif");
  background-position: center top; /* Current: shows top of image */
  /* Try these instead:
     - center center (shows middle)
     - center bottom (shows bottom)
     - 50% 40% (specific percentage)
  */
  background-size: cover;
}
```

### Adjust section height for image visibility:

**Story section** - If you only see part of the image, adjust the min-height (around line 306):

```css
#story {
  min-height: 40vh; /* Current: shows ~40% of viewport height */
  /* Try: 45vh, 50vh, or 60vh to show more of the image */
  /* Lower values (30vh, 35vh) show less but reduce spacing */
}
```

**Note**: The hero section doesn't have a fixed min-height, so it adapts to content. The story section uses `min-height: 40vh` to ensure enough space to display the background image properly.

---

## 🧪 Testing Multiple Images

Want to quickly compare different images?

1. **Put all test images** in `assets/img/sections/`:
   ```
   assets/img/sections/
     ├── home-hero.avif
     ├── test-hero-1.avif
     ├── test-hero-2.avif
     └── test-hero-3.avif
   ```

2. **Swap in CSS** by changing the filename:
   ```css
   url("assets/img/sections/test-hero-1.avif")  /* Test 1 */
   url("assets/img/sections/test-hero-2.avif")  /* Test 2 */
   url("assets/img/sections/test-hero-3.avif")  /* Test 3 */
   ```

3. **Save and compare** - Auto-reload shows changes instantly!

---

## 📍 File Locations Reference

```
assets/img/
├── sections/           ← Section background images go here
│   ├── home-hero.avif      (Hero section)
│   ├── story-band.avif     (Story section)
│   ├── services-hero.avif  (Future use)
│   └── who-hero.avif       (Future use)
└── content/            ← Inline content images go here
    └── story-band.avif     (Not currently used)
```

---

## ⚡ Quick Commands

### View current images:
```bash
ls -lh assets/img/sections/
```

### Copy a new image:
```bash
cp ~/Downloads/my-image.avif assets/img/sections/home-hero.avif
```

### Check image dimensions:
```bash
# Using ImageMagick
identify assets/img/sections/home-hero.avif

# Or just open it in Preview/Finder to see size
open assets/img/sections/home-hero.avif
```

---

## 🐛 Troubleshooting

### Image not showing?

1. **Check file path** - Make sure the path in CSS matches the actual file location
2. **Check filename** - Case-sensitive! `home-hero.avif` ≠ `Home-Hero.avif`
3. **Hard refresh** - `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)
4. **Check browser console** - Press F12, look for 404 errors

### Image looks wrong?

1. **Only seeing part of image?** - Adjust `min-height` on story section (see positioning section above)
2. **Wrong part of image showing?** - Change `background-position` (see positioning section above)
3. **Try different sizing** - Change `background-size: cover` to `contain` to show full image
4. **Adjust overlay** - Make it darker/lighter (see overlay section above)
5. **Check image dimensions** - Very wide images work best for backgrounds

---

## 💡 Pro Tips

1. **Keep originals**: Always keep a backup of images before replacing
2. **Optimize first**: Use [Squoosh](https://squoosh.app/) to compress before adding
3. **Test on mobile**: Background images should work on small screens too
4. **Use AVIF**: Best quality/size ratio, supported by modern browsers
5. **Adjust min-height**: If you only see part of the story section image, increase `min-height` from `40vh` to `45vh` or `50vh`
6. **Adjust positioning**: If the wrong part of your image shows, experiment with `background-position` values (see positioning section)
7. **Maintain spacing**: The story section uses reduced bottom padding to match hero spacing - adjust if needed at line 304

---

**Need help?** Use Cursor's chat (`Cmd+L`) and ask: "How do I change the hero background image?"

