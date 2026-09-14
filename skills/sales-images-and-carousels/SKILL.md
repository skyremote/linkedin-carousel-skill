---
name: sales-images-and-carousels
description: Turn a business offer into standalone sales images and LinkedIn carousel PDFs, with brand-matched variants, captions and a reusable community prompt. Use for sales sheets, offer explainers or adapting them into swipeable slides.
---

# Sales images and carousels

Create the requested files, not just another set of briefs. Work with the user's offer, audience, evidence, voice and real brand assets. This skill is self-contained; optional image generation and local rendering depend on the host's available tools.

## Establish the scope

Read the supplied brief and inspect image references. Use known brand settings and the user's writing samples; ask only for missing details that materially affect the message. Do not impose NavAIgate's identity on another business.

Preserve the requested number, formats and theme. For the full example workflow, use five angles: why work together, commercial case, delivery method, working with the existing team, and concrete possibilities. Each angle becomes a standalone portrait sales sheet in light and dark plus a six-slide carousel. A request for one sheet should still produce one sheet, not the whole pack.

For a pasteable starting brief, read [references/reusable-prompt.txt](references/reusable-prompt.txt). Replace its bracketed fields with the user's information. The prompt's full-pack counts are an example scope, not mandatory for every task.

## Copy and evidence

Write in the user's supplied voice. If a voice skill is installed and requested, apply it; do not require access to Daniel's private writing context. Use plain connected sentences, concrete outcomes and one next action. Never invent testimonials, customers, results or stories.

Separate verified results from targets and assumptions. For an illustrative commercial case, put “Illustrative example — not a client result” visibly beside the calculation. Include review time and relevant build/running costs. Released capacity is not automatically a cash saving.

## Sales images

Use portrait A4 proportions unless asked otherwise. Aim for 2480 × 3508 pixels when supported for a 300 dpi A4 output, and report actual dimensions. Smaller images remain digital-resolution outputs.

Give each sheet a large headline, readable copy, generous margins and one meaningful visual. Use accent colour sparingly. Keep light/dark pairs consistent in message and layout. Avoid fake interfaces or decorative objects unrelated to the offer.

Use the host's image-generation tool when image generation is requested. Generate individual assets, never a contact sheet as the final deliverable. For exact logos, dense copy and numerical diagrams, prefer inserting original assets and setting text/charts in a deterministic layout tool when the host and user permit it. Inspect model-rendered text and marks; do not call a generated approximation an exact reproduction. Follow the host's image-editing constraints.

## Carousels

First resolve whether the user wants the approved page images packaged unchanged or a new square-slide adaptation. For standalone image generation and image-preserving portrait carousels, use the companion [sales-page-images skill](../sales-page-images/SKILL.md). Do not rewrite approved images into square slides unless the user asks for that adaptation.

For an explicitly requested square-slide adaptation: Recompose the content into square 1080 × 1080 slides; do not shrink a dense portrait sheet into a square. A useful default is a hook, four slides developing the idea, and a final next action. Keep one idea per slide. Use the actual brand palette and logo, page numbers and consistent footers.

At this canvas size, body text around 28–36 px and headlines around 60–88 px are useful starting points. Inspect phone-size readability rather than trusting font sizes alone. Use light or dark according to the user and their brand; do not assert one universally performs better.

Build self-contained HTML or equivalent editable source. With Playwright, embed assets as data URLs, load HTML with page.setContent(), await document.fonts.ready and image decoding, then export a multi-page PDF with printBackground enabled and one PNG per slide. Validate page breaks and content/footer overlap. Keep dependencies in a local build directory outside streamed cloud storage.

Create a caption per carousel in the user's voice with one clear next action. Under 1,300 characters is the example default, not a platform maximum. Do not claim publishing occurred.

## Quality checks and handoff

Read each output against its intended copy. Check spelling, logo fidelity, contrast, clipping, margins and mobile legibility. Verify arithmetic separately from the image. Bars labelled 60 and 20 must share a zero baseline and have exactly a 3:1 length ratio. If image generation cannot do this reliably, use a deterministic chart where permitted or flag the unresolved defect.

Count all requested outputs. Save versioned files, editable sources, captions and prompts in the user's chosen location. Preserve existing versions. For the full example pack, the count is ten portrait images, five six-page PDFs, thirty slide PNGs and five captions. Report actual output dimensions and any limitations. Draft, saved, hosted and published are distinct states.

If the user wants a community handout, provide a generic prompt, a short walkthrough and labelled examples. A local downloadable pack can embed images for offline viewing. Hosted classroom images require public URLs; local paths cannot serve as public images. Do not expand a prompt-handout request into a whole course or publish without authorisation.

## Worked examples

Read [examples/README.md](examples/README.md) when using the included NavAIgate images. They show layout and review lessons, not transferable claims or a universal template. The dark commercial chart deliberately retains a documented defect. The complete corrected carousel PDF is included for comparison.
