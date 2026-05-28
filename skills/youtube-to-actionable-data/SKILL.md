---
name: youtube-to-actionable-data
description: Reads a YouTube URL (or video ID) and converts it into structured, actionable data for the LLM — pulling timestamped transcript, metadata (title, channel, duration, chapters, description, tags), and producing both machine-readable JSON and a pre-formatted markdown synthesis input. Use this skill ANY TIME a user pastes a YouTube link, youtu.be link, shorts link, or asks to "analyze", "summarize", "extract from", "pull insights from", "get the transcript of", "turn this video into", "make actionable", or "what's in this video" — including casual phrasings like "watch this for me", "TL;DR this YouTube", "what does he say about X in this video", "rip the transcript", or "give me the key points from this clip". Also triggers when a user wants to repurpose a video into notes, action items, social posts, blog content, frameworks, or quotes. Outputs raw_transcript.json, metadata.json, raw_transcript.txt, and summary_input.md. After running, Claude reads summary_input.md and synthesizes the actionable output per the user's intent. Do NOT use this skill for downloading the video file, generating thumbnails, or any non-text extraction.
---

# YouTube to Actionable Data

Extracts transcript + metadata from a YouTube URL and converts it into structured data the LLM can act on.

## When to trigger

Any of these signal a trigger:

- User pastes a `youtube.com/watch?v=...`, `youtu.be/...`, `youtube.com/shorts/...`, `youtube.com/live/...`, or `youtube.com/embed/...` URL
- User pastes a bare 11-character video ID and references YouTube
- Phrases: "analyze this video", "summarize this YouTube", "TL;DR this", "key points from", "get the transcript", "pull insights from", "rip this video", "what does X say in this video", "turn this into [notes/posts/blog/script]", "make this actionable", "repurpose this video"

Do NOT trigger for: video file downloads, thumbnail generation, audio extraction, channel-level analytics. This skill is text-extraction → LLM-actionable structured data only.

## How it works (3 steps)

### Step 1 — Run the extractor

Always run the extraction script as the first move. Do not paraphrase the URL or ask follow-up questions before extracting.

```bash
python3 /mnt/skills/user/youtube-to-actionable-data/scripts/extract.py "<URL>" --out-dir /home/claude
```

Optional flags:
- `--lang es` (or any 2-letter code) — prefer a non-English transcript language
- `--json-only` — skip writing `summary_input.md` (use when piping to another skill)

The script writes up to 4 files to `--out-dir`:

| File | Contains |
|---|---|
| `metadata.json` | title, channel, duration, upload date, views/likes, tags, chapters, description, thumbnail URL |
| `raw_transcript.json` | timestamped segments + pre-merged ~60s chunks + language code |
| `raw_transcript.txt` | plain-text transcript, one line per segment with `[mm:ss]` prefix |
| `summary_input.md` | pre-formatted markdown combining metadata + chunked transcript — **read this to synthesize** |

The script also prints a JSON status block to stdout. Inspect it for:
- `ok: true/false`
- `transcript_available: true/false`
- `transcript_error: <code>` if extraction failed
- `chapter_count` — useful fallback signal when transcript is unavailable

### Step 2 — Read `summary_input.md`

```
view /home/claude/summary_input.md
```

For videos under 30 minutes this is the single source of truth. For videos over 30 minutes, `summary_input.md` may exceed comfortable context — in that case, read `metadata.json` first plus targeted chunks from `raw_transcript.json`.

### Step 3 — Synthesize per the user's intent

Match the user's ask to the synthesis template. **Always include timestamp citations** (e.g., `[12:34]`) when quoting or referencing specific claims so the user can verify.

#### Default template (no specific ask)

```
## TL;DR
<2-3 sentences>

## Key Points (with timestamps)
- [0:34] <point>
- [4:12] <point>
- ...

## Action Items
- [ ] <thing the viewer should do>
- [ ] <thing the viewer should do>

## Notable Quotes
> "<short verbatim quote>" — [mm:ss]

## Topics covered
<tags / themes>
```

#### Other intents — pick the right one

| User said | Use this template |
|---|---|
| "make this into social posts" | Pull 3-5 hook-worthy quotes + 1 carousel concept. Route to `/social-creative-designer` if heavy lift. |
| "turn this into a blog post" | Outline → H2s from chapters (or invented if none) → bullet-supported sections → CTA. |
| "key frameworks / mental models" | Extract any named systems, acronyms, step-by-step processes. Format as numbered lists with timestamps. |
| "what does [person] say about [topic]" | Search the transcript text for the topic, return matched chunks with timestamps + 1-line gloss each. |
| "objections / counterpoints" | Pull skeptical claims, caveats, and "but" statements. |
| "build a workflow from this" | Route to the `YouTube Comes Alive!` workflow artifact skill if it's installed. |

## Failure modes — handle these explicitly

The extractor will tell you what went wrong via the stdout JSON. Respond appropriately:

| `transcript_error` | What to do |
|---|---|
| `transcripts_disabled` | Tell the user the creator disabled transcripts. Use `metadata.json` (chapters + description + tags) as the actionable signal and label it clearly: "no transcript — synthesis based on chapters + description only." |
| `no_transcript_in_requested_lang` | Re-run with `--lang en` (default) or ask the user which language. |
| `video_unavailable` | Stop. Tell the user the video is private, region-blocked, deleted, or age-gated. Do not retry. |
| `invalid_url` | Ask the user for a clean URL. |
| metadata fails but transcript succeeds | Proceed with transcript-only synthesis; note that title/channel are missing. |

## Hard constraints

- **Never invent timestamps.** If you cite `[12:34]`, that timestamp must exist in `raw_transcript.json` or `metadata.json` chapters.
- **Never invent quotes.** Quotes must be lifted verbatim (within a few words for fluency) from `raw_transcript.txt`.
- **Don't paraphrase the whole video back.** Compress aggressively. The point is *actionable* output, not a transcript rewrite.
- **Respect copyright.** Per global rules: keep verbatim quotes under 15 words each, and one quote per source-chunk is the limit when delivering output to the user.
- **Don't claim views/likes if metadata failed.** The stdout JSON tells you if metadata is missing.

## Chaining with other skills

This skill is the upstream extraction layer. Common chains:

- `youtube-to-actionable-data` → `social-creative-designer` (video → 5 social posts)
- `youtube-to-actionable-data` → `content-style-synthesizer` (video → branded blog content)
- `youtube-to-actionable-data` → `perfect-hero-page-builder` (founder interview → hero copy)

When chaining, pass `--json-only` and hand the downstream skill the path to `raw_transcript.json` + `metadata.json`.

## One-line invocation reminder

```bash
python3 /mnt/skills/user/youtube-to-actionable-data/scripts/extract.py "<URL>" --out-dir /home/claude && cat /home/claude/summary_input.md
```
