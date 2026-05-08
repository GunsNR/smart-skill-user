# Assets

## Social Preview

`assets/social-preview.svg` is the source artwork for the GitHub social preview, README hero image, and launch post visual.

The image is a self-contained SVG with no external images, hotlinks, screenshots, proprietary assets, or private client data. It illustrates the Smart Skill User flow: prompt, preflight, selected skills, skipped skills, and safer execution.

`assets/social-preview.png` is an exported copy of the SVG for platforms that prefer raster images. It is 1280x640.

Regenerate it from the repository root with a local SVG-capable renderer, for example:

```bash
magick assets/social-preview.svg assets/social-preview.png
```

On systems with Chrome installed, headless Chrome can also export it:

```bash
chrome --headless=new --disable-gpu --hide-scrollbars --screenshot=assets/social-preview.png --window-size=1280,640 assets/social-preview.svg
```

The SVG remains the source of truth.
