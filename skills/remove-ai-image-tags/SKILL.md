---
name: remove-ai-image-tags
description: Strips AI-generation metadata from image files — including XMP, EXIF, and IPTC fields that identify an image as AI-generated (e.g., CreatorTool, DigitalSourceType, prompt text, model name, seed values, and generator comments). Works on single files, batches, and directories. Outputs clean copies by default; can overwrite in-place with an explicit flag. Use this skill when a user asks to "remove AI tags", "clean metadata", "strip AI fingerprints", "remove prompt data from images", "sanitize image metadata", or "make images look non-AI". Does NOT alter pixel data, re-encode lossy formats beyond what the stripping tool requires, or guarantee removal of steganographic watermarks embedded in pixel data.
---

# Remove AI Image Tags

Strips AI-generation metadata fields from image files without altering pixel data.

## When to trigger

Any of these signal a trigger:

- User asks to "remove AI tags / metadata / fingerprints" from an image or folder
- User says "clean the metadata", "strip the prompt from this image", "remove generator info", or "sanitize these images"
- User wants images to not show AI origin in metadata viewers (e.g., Lightroom, Bridge, `exiftool -v`)
- User provides a path to one or more images (JPEG, PNG, WebP, TIFF, AVIF, HEIC)

Do NOT trigger for: pixel-level watermark removal, re-encoding, format conversion, or editing image content.

## What counts as an AI tag

### XMP fields (most common in AI-generated images)

| Field | Examples |
|---|---|
| `xmp:CreatorTool` | `Stable Diffusion`, `DALL-E 3`, `Midjourney`, `ComfyUI`, `Firefly` |
| `xmp:Label` / `xmp:Rating` | Pipeline-stamped values |
| `Iptc4xmpExt:DigitalSourceType` | `http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia` |
| `dc:description` / `dc:subject` | Prompt text, model name, seed embedded as description |
| `photoshop:History` | Generative fill history steps |
| Any `ai:*` or `comfy:*` namespace | Custom AI pipeline namespaces |

### EXIF fields

| Field | Examples |
|---|---|
| `EXIF:Software` | `Stable Diffusion`, `NovelAI`, `Automatic1111` |
| `EXIF:ImageDescription` | Prompt text |
| `EXIF:UserComment` | Seed, CFG scale, sampler, model hash |
| `EXIF:Artist` | AI service attribution |
| `EXIF:Copyright` | AI-generated copyright strings |
| `EXIF:Make` / `EXIF:Model` | Fake or missing camera data |

### IPTC fields

| Field | Examples |
|---|---|
| `IPTC:Caption-Abstract` | Embedded prompt |
| `IPTC:OriginatingProgram` | Generator name |
| `IPTC:ProgramVersion` | Model version string |

## How it works (3 steps)

### Step 1 — Detect and inventory

Run a metadata read to confirm which AI fields are present before stripping:

```bash
exiftool -s -XMP:CreatorTool -XMP:DigitalSourceType -EXIF:Software \
  -EXIF:UserComment -EXIF:ImageDescription -IPTC:OriginatingProgram \
  "<file_or_dir>"
```

Report the findings to the user: which files have AI fields, which fields, and a sample of values. Pause here if the user asked "what's in this image" rather than "remove it."

### Step 2 — Strip AI fields

#### Option A — Targeted strip (recommended, preserves non-AI metadata like GPS, camera EXIF)

```bash
exiftool -overwrite_original_in_place \
  -XMP:CreatorTool= \
  -XMP:DigitalSourceType= \
  -XMP:all= \
  -EXIF:Software= \
  -EXIF:ImageDescription= \
  -EXIF:UserComment= \
  -EXIF:Artist= \
  -EXIF:Copyright= \
  -IPTC:Caption-Abstract= \
  -IPTC:OriginatingProgram= \
  -IPTC:ProgramVersion= \
  "<file_or_dir>"
```

#### Option B — Nuclear strip (removes ALL metadata; use only when user explicitly asks)

```bash
exiftool -all= -overwrite_original_in_place "<file_or_dir>"
```

#### Safe-copy mode (default when user has not explicitly approved in-place)

```bash
exiftool -all= -o "<output_dir>/" "<file_or_dir>"
```

Always default to safe-copy mode unless the user says "overwrite", "in-place", or "replace the originals."

### Step 3 — Verify and report

Re-run the inventory command from Step 1 on the output files to confirm the target fields are gone. Report:

- Files processed count
- Fields removed per file
- Any files skipped (unsupported format, read-only, locked)
- Output location (if safe-copy mode)

## Tool requirements

This skill requires `exiftool` to be available in the environment:

```bash
# Check
exiftool -ver

# Install if missing
# macOS:  brew install exiftool
# Ubuntu: sudo apt install libimage-exiftool-perl
# Windows: choco install exiftool
```

If `exiftool` is not available, report the missing dependency and the install command for the user's platform. Do not attempt pixel-level stripping as a fallback.

## Flags and options

| User says | Behavior |
|---|---|
| "just these files: a.jpg b.png" | Run on the listed files only |
| "do the whole folder" | Pass the directory path; `exiftool` recurses with `-r` |
| "keep the camera metadata" | Use Option A (targeted), not Option B (nuclear) |
| "overwrite" / "in-place" | Add `-overwrite_original_in_place`; skip safe-copy |
| "what's in it first" | Run Step 1 only; do not strip without confirmation |
| "also remove GPS" | Add `-GPS:all=` to the targeted strip command |

## Failure modes

| Problem | What to do |
|---|---|
| `exiftool` not found | Report missing dependency + platform install command; stop |
| File is read-only | Skip and list in the report; do not `chmod` without asking |
| Unsupported format (e.g., SVG, GIF) | Note in report; exiftool supports limited GIF EXIF but not SVG |
| PNG with iTXt/tEXt AI chunks | Use `-PNG:all=` in addition to the standard fields |
| Field reappears after strip | Likely written in a non-standard namespace; run `-XMP:all=` and reinspect |

## PNG-specific notes

PNG files store AI metadata in `tEXt`/`iTXt` chunks rather than XMP/EXIF. Stable Diffusion, ComfyUI, and Automatic1111 commonly embed full prompt JSON in `iTXt` chunks. Use:

```bash
exiftool -overwrite_original_in_place -PNG:all= "<file.png>"
```

This removes all PNG text chunks. To keep non-AI PNG text chunks, inspect first with `exiftool -v3 "<file.png>"` and strip only the named chunks containing AI data.

## Hard constraints

- **Never alter pixel data.** This skill touches only metadata, not image content.
- **Default to safe-copy.** Do not overwrite originals without explicit user approval.
- **Do not guarantee steganographic watermark removal.** Pixel-embedded watermarks (e.g., Stable Diffusion invisible watermarks, Nightshade) require separate tools and are out of scope.
- **Do not re-encode.** `exiftool` metadata stripping is lossless for JPEG and does not re-encode. Flag if the user's request would require re-encoding (e.g., burning metadata into pixels).
