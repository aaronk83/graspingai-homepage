# 🚀 Quick Start - Local Development

## Get Started in 30 Seconds

1. **Start the server**:
   ```bash
   python3 serve.py
   ```

2. **Browser opens automatically** at http://localhost:8000

3. **Edit any file** (HTML, CSS, JS) → **Save** → **Page auto-reloads!** ✨

4. **Stop server**: Press `Ctrl+C` in terminal

---

## What Was Fixed

✅ **Hero background image** - Restored working version using `data-bg="home-hero"`  
✅ **Story section image** - Fixed path to use correct file  
✅ **Auto-reload** - Page refreshes automatically when you save changes  
✅ **Local server** - Simple Python server for development  

---

## Quick Reference

### Start Development
```bash
python3 serve.py
```

### Swap Hero Image (Fastest Method)
```bash
cp /path/to/your/image.avif assets/img/sections/home-hero.avif
```
Then save any file → browser reloads automatically!

### Swap Hero Image (Different Filename)
1. Add image to `assets/img/sections/my-new-hero.avif`
2. Edit `styles.css` line ~207, change:
   ```css
   url("assets/img/sections/home-hero.avif")
   ```
   to:
   ```css
   url("assets/img/sections/my-new-hero.avif")
   ```
3. Save → auto-reload!

---

## Documentation

- **Full Development Guide**: See `DEVELOPMENT.md`
- **Image Swap Reference**: See `IMAGE_SWAP_GUIDE.md`

---

## Cursor Workflow (VS Code Users)

**Everything works the same as VS Code!**

- ✅ File explorer on left
- ✅ Editor in center  
- ✅ Terminal at bottom (`Cmd+\`` to toggle)
- ✅ Command palette: `Cmd+Shift+P`
- ✅ Save: `Cmd+S`

**Plus Cursor AI features**:
- `Cmd+L` - Chat with AI about code
- `Cmd+K` - Inline AI edits
- `Cmd+I` - Composer for larger features

---

**You're all set! Happy coding! 🎉**

