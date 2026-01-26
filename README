A minimal static site generator that compiles Markdown into a fully static HTML website using templates.

## Project Structure
```php
site/
├── build.py            # build entry point
├── loader.py           # loads markdown → Page objects
├── renderer.py         # renders Page → HTML
├── page.py             # Page data structure
│
├── content/            # markdown source files
├── theme/              # templates + theme assets
├── static/             # raw static assets (images, etc.)
└── output/             # generated site (ignored by git)
```

## How it works (brief)
```css
content/*.md
   ↓
Page objects (metadata + HTML fragment)
   ↓
Jinja templates (theme)
   ↓
Static HTML files in output/
```

Each page is generated as index.html inside a directory to enable clean URLs.

## Usage
1. Write content

Add Markdown files to content/:
```css
content/
├── index.md
├── about.md
└── blog/
    └── first-post.md
```

Optional metadata format at top of file:
```markdown
meta-title: My Post
meta-tags: python, static-site
meta-date: 2026-01-26
```

2. Build the site
```bash
python build.py
```

Output is generated in: `output/`

3. Preview locally

You can open files directly:
```bash
xdg-open output/index.html
```

Or serve with any static server.

### License

Do whatever you want.
This project exists for learning and experimentation.
