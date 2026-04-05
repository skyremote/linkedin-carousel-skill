---
name: linkedin-carousel
description: Generate branded LinkedIn carousel PDFs with optional AI-generated images. Use this skill whenever the user wants to create a LinkedIn carousel, LinkedIn slides, LinkedIn PDF, swipeable LinkedIn post, or social media carousel. Also triggers when the user says "make me a carousel", "LinkedIn post with slides", "carousel post", or asks for branded social content for LinkedIn.
---

# LinkedIn Carousel Generator

Create professional, branded LinkedIn carousel PDFs — ready to upload as document posts that display as swipeable slides.

## How It Works

Each carousel is built as HTML slides (1080x1080px each), rendered via Playwright, and exported as a multi-page PDF. Individual slide PNGs are also saved for reuse on other platforms.

## Step 0: Brand Setup (First Run Only)

On first use, check if `~/.claude/skills/linkedin-carousel/brand-config.json` exists.

**If it doesn't exist**, ask the user these questions before proceeding:

1. **Company name** — displayed in the footer of every slide
2. **Website URL** — displayed in the footer (e.g. "yoursite.com")
3. **Primary accent colour** — hex code (default: #3B82F6 blue)
4. **Secondary accent colour** — hex code (default: #8B5CF6 purple)  
5. **Tertiary accent colour** — hex code (default: #0EA5E9 teal)
6. **Background colour** — hex code (default: #0F172A dark slate)
7. **Font family** — Google Fonts name (default: Poppins)

Then save to `~/.claude/skills/linkedin-carousel/brand-config.json`:

```json
{
  "company": "Company Name",
  "url": "yoursite.com",
  "colors": {
    "bg": "#0F172A",
    "card_bg": "#1E293B",
    "accent": "#3B82F6",
    "accent_alt": "#8B5CF6",
    "accent_tertiary": "#0EA5E9",
    "text_primary": "#F8FAFC",
    "text_secondary": "#CBD5E1",
    "text_muted": "#64748B"
  },
  "font": "Poppins",
  "font_url": "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap"
}
```

Card background (`card_bg`) is automatically derived by lightening the background colour slightly. Text colours are auto-calculated for contrast — white on dark backgrounds, dark on light backgrounds.

**If the file exists**, read it and use those values for all brand references below. The user can update their brand anytime by saying "update my carousel brand" or editing the JSON directly.

## Brand Colours

Read from `brand-config.json`. Fallback defaults if the file is missing:

```css
--bg: #0F172A;            /* Dark slate background */
--card-bg: #1E293B;       /* Card/panel background */
--accent: #3B82F6;        /* Primary blue */
--accent-alt: #8B5CF6;    /* Secondary purple */
--accent-tertiary: #0EA5E9; /* Tertiary teal */
--text-primary: #F8FAFC;  /* Headings */
--text-secondary: #CBD5E1; /* Body text */
--text-muted: #64748B;    /* Footers, captions */
--font: 'Poppins', sans-serif;
```

## Design Rules

These rules exist because LinkedIn carousels are viewed on mobile at small sizes — clarity and contrast matter more than detail.

- **Blue accent bar** (6px) at the absolute top of every slide — this is the brand signature
- **Footer on every slide**: brand name left, URL right, positioned at bottom with 35px margin
- **Dark theme always** — never white or light backgrounds; dark performs better on LinkedIn feeds
- **Sharp edges** — border-radius 4-6px max, no rounded corners on slides themselves
- **Cards use left-border accent** — 4px left border in accent colour, card background #1E293B
- **Generous padding** — 70px on all sides; content must breathe, especially on mobile
- **No decorative clutter** — no gradients, no drop shadows, no background patterns (except hero images)

### Typography Scale

| Element | Size | Weight | Colour |
|---------|------|--------|--------|
| Kicker | 12-13px | 700 | Accent blue, uppercase, letter-spacing: 3px |
| H1 (hero) | 52-64px | 800 | White #F8FAFC |
| H2 (section) | 40-44px | 700 | White #F8FAFC |
| H3 (card title) | 20-22px | 700 | White or accent |
| Body | 14-16px | 400 | Secondary #CBD5E1 |
| Muted/footer | 11-13px | 400 | Muted #64748B |

## Slide Types

Plan the carousel using a mix of these slide types. A typical carousel is 5-10 slides. Always start with a Hook and end with a CTA.

### Hook (Slide 1 — always)
Big bold headline that stops the scroll. Optionally overlay on a hero image (Nano Banana 2). Include a teaser line like "5 minute read ↓" or "Here's how ↓".

### Problem / Pain Point
List 3-5 challenges using cards with consistent styling. Each card gets a single line of text.

### Solution / Pillars
Numbered cards (01, 02, 03) with coloured left-borders (blue, purple, teal). Title + one-line description per card.

### Stats / Metrics
2-4 big numbers with labels. Numbers in accent colour at 48-60px, labels in muted at 13px. Centre-aligned.

### Steps / How-To
Numbered circles (accent blue background, dark text) with title + description per step.

### Quote / Key Insight
Left blue border, italic text, larger font (18-20px). Attribution below in muted.

### CTA (Final slide — always)
Bold headline ("Get started." / "Try it free."). Followed by 2-3 link boxes: primary CTA in solid accent blue, secondary links in card-bg with border. Contact info centred at bottom.

## Workflow

### Step 1: Plan the Content

From the user's topic/request, decide:
- How many slides (5-10 is ideal, 8 is the sweet spot)
- Which slide types to use
- The narrative arc: Hook → Problem → Solution → Evidence → CTA

### Step 2: Generate Images (optional)

If hero/background images would strengthen the carousel, generate them with Nano Banana 2:

```bash
python3 -c "
from google import genai
from google.genai import types

client = genai.Client(api_key='$GEMINI_API_KEY')
response = client.models.generate_content(
    model='gemini-3.1-flash-image-preview',
    contents='[PROMPT - dark navy bg, blue/teal accents, abstract, no text, no faces]',
    config=types.GenerateContentConfig(response_modalities=['TEXT', 'IMAGE'])
)
for part in response.candidates[0].content.parts:
    if part.inline_data is not None:
        with open('[OUTPUT_PATH]', 'wb') as f:
            f.write(part.inline_data.data)
        break
"
```

Image prompt guidelines:
- Always specify "dark navy background (#0F172A)"
- Use "blue (#3B82F6) and teal (#0EA5E9) accents"
- Add "abstract, no text, no faces, professional, minimal"
- Save to the output directory as `hero-01.png`, `hero-02.png`, etc.

### Step 3: Build the HTML

Create a single HTML document with all slides. Each slide is a `<div class="slide">` at 1080x1080px.

**Base HTML structure:**

```html
<!DOCTYPE html>
<html><head>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: 1080px 1080px; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Poppins',sans-serif; }
.slide {
    width: 1080px;
    height: 1080px;
    background: #0F172A;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    page-break-inside: avoid;
}
.slide:last-child { page-break-after: auto; }
.bar { position:absolute; top:0; left:0; right:0; height:6px; background:#3B82F6; z-index:10; }
.content { padding:70px; position:relative; z-index:2; }
.footer {
    position:absolute; bottom:35px; left:70px; right:70px;
    display:flex; justify-content:space-between;
    font-size:13px; color:#64748B; z-index:2;
}
.logo-text { font-weight:700; color:#3B82F6; letter-spacing:1px; }

/* Hero image support */
.bg-img { position:absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity:0.35; }
.overlay { position:absolute; top:0; left:0; width:100%; height:100%; background:linear-gradient(135deg,rgba(15,23,42,0.85),rgba(15,23,42,0.5)); }

/* Typography */
.kicker { font-size:13px; font-weight:700; letter-spacing:3px; color:#3B82F6; text-transform:uppercase; margin-bottom:10px; }
h1 { font-size:64px; font-weight:800; color:#F8FAFC; line-height:1.05; }
h2 { font-size:44px; font-weight:700; color:#F8FAFC; line-height:1.1; }
.accent { color:#3B82F6; }
.purple { color:#8B5CF6; }
.teal { color:#0EA5E9; }
.accent-bar { width:100px; height:5px; background:#3B82F6; margin:24px 0; border-radius:3px; }
.lead { font-size:20px; color:#CBD5E1; margin-top:20px; }

/* Cards */
.card { background:#1E293B; border-left:4px solid #3B82F6; padding:22px 26px; margin-bottom:14px; border-radius:0 4px 4px 0; }
.card h3 { font-size:20px; font-weight:700; color:#F8FAFC; margin-bottom:4px; }
.card p { font-size:14px; color:#64748B; line-height:1.5; }
.card.purple-border { border-color:#8B5CF6; }
.card.teal-border { border-color:#0EA5E9; }

/* Steps */
.step { display:flex; align-items:flex-start; gap:16px; margin-bottom:24px; }
.step-num { width:40px; height:40px; border-radius:50%; background:#3B82F6; color:#0F172A; font-size:20px; font-weight:700; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.step-text h4 { font-size:18px; font-weight:700; color:#F8FAFC; }
.step-text p { font-size:13px; color:#64748B; }

/* Metrics */
.metric { text-align:center; }
.metric-value { font-size:52px; font-weight:800; color:#3B82F6; line-height:1; }
.metric-label { font-size:13px; color:#64748B; margin-top:8px; }

/* CTA */
.cta-box { background:#3B82F6; border-radius:6px; padding:24px 30px; margin-bottom:16px; }
.cta-box p { font-size:17px; font-weight:700; color:#0F172A; }
.link-box { background:#1E293B; border:1px solid #334155; border-radius:6px; padding:24px 30px; margin-bottom:16px; }
.link-box p { font-size:16px; color:#F8FAFC; }
.link-box span { font-size:13px; color:#64748B; display:block; margin-top:4px; }

/* Quote */
.quote { border-left:4px solid #3B82F6; padding:20px 28px; background:rgba(59,130,246,0.05); border-radius:0 4px 4px 0; }
.quote p { font-size:20px; color:#F8FAFC; font-style:italic; font-weight:300; line-height:1.5; }
.quote .attr { font-size:13px; color:#64748B; font-style:normal; margin-top:12px; }

/* Table rows */
.row { display:flex; justify-content:space-between; padding:14px 20px; border-bottom:1px solid #334155; }
.row:nth-child(odd) { background:#1E293B; }
.row .label { font-size:16px; color:#F8FAFC; }
.row .value { font-size:14px; color:#0EA5E9; }
</style>
</head><body>
<!-- slides go here -->
</body></html>
```

### Step 4: Render PDF + PNGs

Use Playwright to render the HTML to PDF and also capture individual slide PNGs.

```javascript
const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.setViewportSize({ width: 1080, height: 1080 });

    // Load the HTML
    await page.setContent(htmlContent, { waitUntil: 'networkidle' });
    await page.waitForTimeout(2000);

    // Export PDF
    await page.pdf({
        path: 'carousel.pdf',
        width: '1080px',
        height: '1080px',
        printBackground: true,
        margin: { top: 0, right: 0, bottom: 0, left: 0 }
    });

    // Export individual PNGs
    const slides = await page.$$('.slide');
    for (let i = 0; i < slides.length; i++) {
        await slides[i].screenshot({
            path: `slide-${String(i + 1).padStart(2, '0')}.png`
        });
    }

    await browser.close();
})();
```

**Important:** The HTML content must be passed as a string to `page.setContent()`, NOT loaded from a file URL. This avoids CORS issues with local images. If using generated images, either:
- Reference them via relative path in the HTML and use `page.goto('file://...')` instead
- Or convert images to base64 data URIs inline

### Step 5: Write the LinkedIn Caption

Generate a caption that:
- Opens with a hook (question, bold statement, or surprising stat)
- Provides 3-5 lines of context/value
- Includes a clear CTA
- Adds relevant hashtags (5-8)
- Mentions the link in comments or at the end

Keep it under 1,300 characters (LinkedIn truncates at ~210 chars before "see more", so the first line matters most).

## Output Structure

Save everything to `~/Documents/LinkedIn/{topic-slug}/`:

```
~/Documents/LinkedIn/{topic-slug}/
├── carousel.pdf           # Upload this to LinkedIn
├── slide-01.png           # Individual slides for other platforms
├── slide-02.png
├── ...
├── carousel.html          # Source HTML (for future edits)
└── caption.txt            # LinkedIn post text
```

## Dependencies

- **Playwright** (Node.js) — for PDF/PNG rendering. Install with `npm install playwright` in any working directory, then `npx playwright install chromium`
- **Google genai** (Python, optional) — for Nano Banana 2 image generation. Only needed if the carousel uses AI-generated imagery

## Quick Reference

| Carousel Length | Best For |
|----------------|----------|
| 3-4 slides | Quick tips, single insight |
| 5-7 slides | How-to, listicle, mini-guide |
| 8-10 slides | Deep dive, case study, training promo |

| Element | LinkedIn Best Practice |
|---------|----------------------|
| First slide | Must stop the scroll — bold headline, minimal text |
| Last slide | Always a CTA — tell them what to do next |
| Text size | Never below 14px — mobile readability |
| Contrast | White on dark — WCAG AA minimum |
| Branding | Consistent footer on every slide |
