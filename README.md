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
