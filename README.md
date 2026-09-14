# LinkedIn Carousel Skill

A [Claude Code](https://claude.ai/code) skill that generates professional, branded LinkedIn carousel PDFs. Upload the PDF as a document post and LinkedIn displays it as swipeable slides.

Built by [NavAIgate](https://navaigate.dev).

## What It Does

- Generates multi-slide carousel PDFs (1080x1080px per page)
- Applies your brand colours, fonts, and logo automatically
- Supports 7 slide types: hook, problem, solution, stats, steps, quote, CTA
- Optional AI-generated hero images via Nano Banana 2 (Gemini)
- Outputs individual slide PNGs for reuse on other platforms
- Writes a LinkedIn post caption to accompany the carousel

## Installation

1. Copy the `SKILL.md` file to your Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills/linkedin-carousel
curl -o ~/.claude/skills/linkedin-carousel/SKILL.md \
  https://raw.githubusercontent.com/skyremote/linkedin-carousel-skill/main/SKILL.md
```

2. On first use, the skill will ask you to set up your brand — company name, colours, font. This saves to `brand-config.json` so every carousel matches your identity automatically.

## Brand Setup

On first run, the skill asks for:

| Setting | Example | Default |
|---------|---------|---------|
| Company name | NavAIgate | — |
| Website URL | navaigate.dev | — |
| Primary accent | #3B82F6 | Blue |
| Secondary accent | #8B5CF6 | Purple |
| Tertiary accent | #0EA5E9 | Teal |
| Background | #0F172A | Dark slate |
| Font | Poppins | Poppins |

See [`brand-config.example.json`](brand-config.example.json) for the full config structure. You can also edit it directly at `~/.claude/skills/linkedin-carousel/brand-config.json`.

## Usage

Just ask Claude Code:

```
"Make me a LinkedIn carousel about the 5 biggest AI trends in 2026"
"Create a carousel post for our product launch"
"LinkedIn slides about why persistent memory matters for AI"
```

## Output

Carousels are saved to `~/Documents/LinkedIn/{topic}/`:

```
~/Documents/LinkedIn/ai-trends-2026/
├── carousel.pdf      # Upload this to LinkedIn
├── slide-01.png      # Individual slides
├── slide-02.png
├── ...
├── carousel.html     # Source HTML
└── caption.txt       # LinkedIn post text
```

## Requirements

- **Claude Code** (CLI, desktop, or web)
- **Playwright** (Node.js) — for rendering. Installed automatically on first use
- **Google genai** (Python, optional) — only needed for AI-generated images

## Resources

- [NavAIgate Resources](https://navaigate.dev/resources) — more skills and training materials
- [Claude Code + NotebookLM Skills](https://github.com/skyremote/claude-code-notebooklm-skills) — persistent memory for Claude

---

*Built with Claude Code by [NavAIgate](https://navaigate.dev)*


## Sales images and carousels — new companion skill

Turn one business offer into standalone sales sheets and swipeable carousels, with a reusable prompt your community can adapt. Built from five NavAIgate sales sheets in light and dark and five six-slide carousels.

Read [the skill](skills/sales-images-and-carousels/SKILL.md), copy [the generic prompt](skills/sales-images-and-carousels/references/reusable-prompt.txt), or browse [the worked examples](skills/sales-images-and-carousels/examples/README.md). The examples include an explicitly documented image-generation chart defect and a corrected PDF so you can see what the review caught.

### Install the companion skill

Clone this repository into a permanent local folder, then copy the **whole skill folder**, including references and examples, into your harness's skills directory:

```sh
git clone https://github.com/skyremote/linkedin-carousel-skill.git
mkdir -p ~/.codex/skills
# Check that the destination does not already exist before copying.
cp -R -n linkedin-carousel-skill/skills/sales-images-and-carousels ~/.codex/skills/
```

For Claude Code use `~/.claude/skills/`; for a Cursor setup that discovers project skills, use your project's `.cursor/skills/`. Restart or refresh discovery, then ask the assistant to read the installed SKILL.md. The original root-level LinkedIn Carousel skill remains separate.

Try: “Use sales-images-and-carousels to make five sales sheets in light and dark and five six-slide carousels for this offer. Use my logo and writing samples, and save the actual files.”

The skill needs an image-capable host for generated images and a local renderer such as Node.js/Playwright for PDF and PNG exports. No API key is bundled or required just to read the skill; any external generation service needs your own authorised access. The prompt has explicit fallback instructions when a host cannot produce a file. Nothing is published automatically.


## Sales Page Images — complete designed pages

**Use this when you want the standalone sales images shown in the examples.** It generates the entire editorial page, including the copy and visual, and can package approved images directly into a portrait carousel PDF. It preserves the image design instead of rewriting it into square slides.

[Read the Sales Page Images skill](skills/sales-page-images/SKILL.md) · [Browse the ten examples](skills/sales-page-images/examples/) · [See the original prompts](skills/sales-page-images/references/original-prompts.md)

Install the whole `skills/sales-page-images` folder into your harness's skills directory, using the same clone-and-copy approach above. Keep existing installations intact. The companion skill remains available for explicitly requested square-slide adaptations.

Try: “Use sales-page-images to make five standalone sales sheets in our theme, in light and dark. Once approved, make two portrait carousel PDFs with one unchanged image per page.”

To package existing images locally, install Pillow and ReportLab, then run:

```sh
python3 -m pip install Pillow reportlab
python3 skills/sales-page-images/scripts/images_to_pdf.py --output light-v1.pdf first-light.png second-light.png
```

Pass files in the intended order. The script refuses to overwrite an existing PDF. These PDFs preserve raster artwork; they do not create editable text or increase image resolution.
