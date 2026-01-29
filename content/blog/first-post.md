meta-title:Title Is First Post
meta-desc:This is 1st post desctiption
meta-author:Cyber
meta-tags:markdown, demo, test, parser, first post, arcane
meta-random:

## New Features and Implementation Ideas for this site

> Ideas to implement Pagination


- [x] create data.json(contains all page data) from python
    - [x] change code where generating links into index.html
- [x] make script.js which will add all post cards using dom 
- [x] it will help in both search and pagination
- [ ] add `draft` meta data to md pages so that pages currently in progress don't get compiled
- Configuration file & extensibility:  
Almost every serious SSG supports a config file (YAML/TOML/JSON). This lets you specify things like site title, permalink patterns, date formats, RSS output, plugins, etc. Right now it’s all probably hard-coded or implicit. A config layer lets users adjust behavior without editing Python code (big UX win).

- No plugin ecosystem:  
By design your generator is minimal. That’s intentional. However, many SSGs support plugins — shortcodes, syntax highlighters, sitemap generators, RSS feeds, search indexing. Without those, you end up reinventing functionality each time.

`pactl list short sinks`  
`ffmpeg -f pulse -i alsa_output.pci-0000_00_1f.3.analog-stereo.monitor output.wav`  
`ffmpeg -f pulse -i @DEFAULT_SINK@.monitor -c:a libopus -b:a 160k output.opus`  

Volume normalization (post-process)  
`ffmpeg -i output.wav -af loudnorm normalized.wav`

to remove all /static from all image links exec this regex replacement 

```bash
:%s/\(!\[[^]]*\](\)\/static/\1/gc
```

```python
def some():
    pass
print(math.round(23/3))
```

## Image optimazations for this place
1. Pick formats like a compression engineer, not a designer

AVIF
Use it as your default for static images. It beats WebP and JPEG in both size and perceptual quality, especially for gradients, screenshots, and UI mockups. Encode with a perceptual quality target (CQ) instead of a fixed bitrate to avoid wasting bits on simple images.

WebP (lossy + lossless)
Keep it as a fallback for browsers that still don’t fully support AVIF (rare now, but not extinct). WebP lossless is excellent for diagrams and pixel-sharp UI.

JPEG XL (JXL)
Technically superb. Practically risky. Browser support is still fragmented. Worth experimenting with locally, not yet as a primary production format.

PNG
Only for cases where you need true lossless + wide compatibility (icons, small diagrams). Otherwise it’s a byte hog.

SVG
For diagrams, flowcharts, and icons—this is secretly your best “image format.” Tiny, scalable, styleable, scriptable. Optimize the SVG itself (remove metadata, collapse paths).

2. Encode smarter, not harder

Perceptual metrics > file size
Tune encoders using SSIM or Butteraugli targets instead of arbitrary quality numbers. A CQ of 28 in AVIF can look better than a JPEG at “90” while being half the size.

Chroma subsampling awareness
Screenshots and code snippets suffer under 4:2:0. Use 4:4:4 when text clarity matters, but only on images that actually need it.

Strip everything
Metadata, ICC profiles (unless color accuracy is critical), EXIF, thumbnails—gone. Metadata can be larger than the visible entropy of the image.


### GIF optimizations for web

```
ffmpeg -i input.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -crf 25 -preset slow output.mp4
```

- libx264 → best compression-quality tradeoff for MP4
- -crf 23 → visually lossless for GIF content (lower = higher quality, bigger file)
- yuv420p → maximum browser compatibility
- scale=trunc(iw/2)*2 → fixes odd dimensions (H.264 requirement)
- -movflags faststart → instant playback on the web
- baseline profile → plays everywhere, even ancient devices


for HTML use 

```html
<video autoplay loop muted playsinline>
```

## Vim

To do same edits on multiple lines

1. Visual block mode
    1. `Ctrl+v`
    2. Select lines
    3. Press `I` and do the edit 
    4. `Esc`
