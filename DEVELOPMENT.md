# Development Guide for GraspingAI Homepage

This guide will help you set up local development and understand the Cursor workflow for this project.

## 🚀 Quick Start: Local Development

### Step 1: Start the Local Server

Open a terminal in this directory and run:

```bash
python3 serve.py
```

Or if you made it executable:

```bash
./serve.py
```

The server will start at **http://localhost:8000** and should automatically open in your browser.

### Step 2: Edit and See Changes Live

1. **Keep the server running** in your terminal
2. **Edit any file** (HTML, CSS, JS) in Cursor
3. **Save the file** (Cmd+S on Mac, Ctrl+S on Windows/Linux)
4. **The browser will automatically reload** within 1 second!

The auto-reload script only runs when you're on `localhost` or `127.0.0.1`, so it won't affect your production site.

### Step 3: Stop the Server

Press `Ctrl+C` in the terminal where the server is running.

---

## 📝 Cursor Workflow (for VS Code users)

If you're used to VS Code, here's how Cursor is different and similar:

### Similarities:
- **File Explorer** on the left (same as VS Code)
- **Editor** in the center (same behavior)
- **Terminal** at the bottom (Cmd+` to toggle, same as VS Code)
- **Command Palette** (Cmd+Shift+P, same shortcuts)
- **Multi-cursor editing** (Cmd+D, Alt+Click, same as VS Code)

### Key Differences:

1. **AI Features**:
   - `Cmd+K` - Inline AI edits (edits code where your cursor is)
   - `Cmd+L` - Chat with AI about your codebase
   - `Cmd+I` - Composer (AI helps write entire features)

2. **Terminal Integration**:
   - Cursor's terminal works exactly like VS Code
   - You can open multiple terminals with `Cmd+\``
   - Run `python3 serve.py` in the terminal just like VS Code

3. **File Watching**:
   - Cursor automatically detects file changes (same as VS Code)
   - No special setup needed for the auto-reload to work

### Recommended Workflow:

1. **Split your screen**:
   - Left: Cursor editor
   - Right: Browser (http://localhost:8000)

2. **Edit in Cursor, see changes instantly**:
   - Make changes in `index.html` or `styles.css`
   - Save (Cmd+S)
   - Browser auto-reloads in ~1 second

3. **Use Cursor's AI**:
   - Highlight code and press `Cmd+K` for inline suggestions
   - Press `Cmd+L` to ask questions about your code
   - Use `Cmd+I` (Composer) for larger refactoring

---

## 🖼️ Swapping Background Images

Your site uses a data-attribute system for background images. Here's how to swap them:

### Current Image Locations:

- **Hero section**: `assets/img/sections/home-hero.avif`
- **Story section**: `assets/img/sections/story-band.avif`

### How to Replace an Image:

#### Option 1: Replace the file directly (easiest)

1. Keep the same filename (e.g., `home-hero.avif`)
2. Replace the file in the same location
3. Save and the browser will reload automatically

**Example:**
```bash
# In terminal, navigate to your project
cd /Users/aaronkagan/Documents/CodeProjectsLocal/GraspingAI/homepage

# Replace the hero image
cp /path/to/your/new/image.avif assets/img/sections/home-hero.avif
```

#### Option 2: Use a different image

1. Add your new image to `assets/img/sections/` (or `assets/img/content/`)
2. Update `styles.css` to point to the new file

**For Hero section:**

Edit `styles.css` around line 204:

```css
.hero[data-bg="home-hero"]::before {
  background:
    linear-gradient(to bottom, rgba(11,18,32,.45), rgba(11,18,32,.45)),
    url("assets/img/sections/YOUR_NEW_IMAGE.avif") center/cover no-repeat;
}
```

**For Story section:**

Edit `styles.css` around line 302:

```css
#story[data-bg="story-band"]{ 
  background-image:url("assets/img/sections/YOUR_NEW_IMAGE.avif"); 
}
```

3. Save and the page will reload!

---

## 🎨 Image Format Tips

### Recommended formats:
- **AVIF** - Best compression, modern browsers
- **WebP** - Good fallback, wide support
- **JPG/PNG** - Universal fallback

### Converting images:

If you have a JPG/PNG and want AVIF:

```bash
# Using ImageMagick (install with: brew install imagemagick)
magick input.jpg -quality 85 output.avif

# Or use online converters like:
# - https://squoosh.app/
# - https://convertio.co/jpg-avif/
```

---

## 🔍 Troubleshooting

### Server won't start (Port already in use)

**Solution 1**: Kill the process using port 8000
```bash
lsof -ti:8000 | xargs kill -9
```

**Solution 2**: Use a different port (edit `serve.py` and change `PORT = 8000` to `PORT = 8001`)

### Changes not showing in browser

1. **Hard refresh**: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows/Linux)
2. **Check terminal**: Make sure server is still running
3. **Check file path**: Make sure you're editing the right file

### Auto-reload not working

- Make sure you're accessing via `http://localhost:8000` (not `file://`)
- Check browser console (F12) for JavaScript errors
- The auto-reload script only works on localhost

---

## 📂 Project Structure

```
homepage/
├── index.html          # Main HTML file
├── styles.css          # All your styles
├── script.js           # JavaScript (currently minimal)
├── serve.py            # Local development server
├── assets/
│   ├── img/
│   │   ├── sections/   # Background images for sections
│   │   │   ├── home-hero.avif
│   │   │   └── story-band.avif
│   │   └── content/    # Inline content images
│   └── logo-*.svg      # Logo files
└── forms/              # Contact form pages
```

---

## 🚢 Deploying to Production

After you're happy with your local changes:

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Update hero image and layout"
   ```

2. **Push to your branch**:
   ```bash
   git push origin images
   ```

3. **Merge/deploy** through your normal process (GitHub Actions, Netlify, etc.)

The auto-reload script in `index.html` only runs on localhost, so it won't affect production.

---

## 💡 Tips for Working with Cursor

1. **Use Composer (Cmd+I)** for larger refactors:
   - "Add a new section for testimonials"
   - "Update all button colors to match the new brand"

2. **Use Chat (Cmd+L)** for questions:
   - "Why isn't my hero image showing?"
   - "How do I add a new background image?"

3. **Use Inline Edit (Cmd+K)** for quick fixes:
   - Select code, press Cmd+K, describe the change

4. **Keep terminal open**: Run `python3 serve.py` and leave it running while you work

---

## 🎯 Common Tasks

### Add a new background image section

1. Add image to `assets/img/sections/new-section.avif`
2. In `index.html`, add `data-bg="new-section"` to the section:
   ```html
   <section id="services" class="section" data-bg="new-section">
   ```
3. In `styles.css`, add the mapping:
   ```css
   #services[data-bg="new-section"] {
     background-image: url("assets/img/sections/new-section.avif");
   }
   ```

### Test different images quickly

1. Put all test images in `assets/img/sections/`
2. Update the CSS `url()` path to swap between them
3. Save and see the change instantly

---

Happy coding! 🎉

