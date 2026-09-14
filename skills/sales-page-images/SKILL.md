---
name: sales-page-images
description: Generate polished standalone portrait sales-page images with complete copy, brand styling and meaningful diagrams. Use for one-page offer explainers, sales sheets, light/dark variants, or a carousel made directly from approved page images.
---

# Sales page images

The deliverable is the finished editorial sales image. Generate the whole page with the image tool: headline, complete copy, visual hierarchy and meaningful diagram together. Do not replace this with generic HTML cards, a website mockup, a deck or a shortened square-slide rewrite.

## Reference-led generation

Inspect the user's approved images before writing the prompt. If no user references exist, inspect relevant images in `examples/` for the visual quality target. These are NavAIgate examples; use the user's own brand and facts. Read [references/original-prompts.md](references/original-prompts.md) for the actual five briefs and prompts that produced this set.

Collect or infer from supplied context: audience, offer, exact copy, brand colours and font, actual logo asset, page count and themes. Each page must independently explain its offer. Preserve supplied copy unless a rewrite is requested. Use an available voice guide when writing new copy.

Use the host's built-in image generation by default, one call per page or variant. Do not silently switch to a paid API. Pass the real logo as a reference and request faithful reproduction. Inspect the result; a generated logo is not guaranteed pixel-identical to the master. Exact logo placement can be a targeted finishing step where permitted, but preserve the approved page's composition.

The demonstrated style is A4 portrait, warm ivory or charcoal ground, large Poppins-like headings, restrained copper, spacious alignment and one meaningful diagram. The page may carry full paragraphs and a complete explanation; do not reduce it to a headline poster. Avoid stock people, fake dashboards, navigation, fake buttons, decorative scenery, endorsement claims and invented results.

For another brand, replace the palette and identity rather than copying NavAIgate. For light/dark variants, preserve the message and graphic relationships. If the first version is approved, use it as an edit reference for the other theme to reduce layout drift.

## Review and targeted correction

Inspect every image at full size and smaller preview size. Check all copy, logo, contrast, page edges and diagram meaning. Arithmetic and chart proportions require separate checks. Keep illustrative-example qualifications visible. Do not turn assumptions into results or released time into automatic cash savings.

Use a targeted image edit to correct a defect, keeping the rest unchanged. If two attempts do not fix a precise numeric graphic, report the limitation and propose a bounded deterministic repair where permitted. Do not rebuild the whole page in a weaker template. The retained dark commercial-case example has an approximate bar ratio; it is a review lesson, not a correct chart master.

Request high resolution when supported; report actual dimensions. The included images are around 1054 × 1492, digital examples rather than 300 dpi A4 print masters. Never imply upscaling adds source detail.

## Carousel from approved images

When the user says to make a carousel from these images, place each complete approved image on one portrait PDF page in the given order. Preserve the original image pixels, typography, visual, crop and aspect ratio. Do not split pages into six slides, retype them, squeeze them into squares, or add covers unless requested.

If both themes were made, create separate light and dark PDFs unless the user asks for a mixed sequence. Do not regenerate already approved images just to package them.

Use [scripts/images_to_pdf.py](scripts/images_to_pdf.py) with Python, Pillow and ReportLab. Supply explicit ordered image paths and a new output filename. It embeds images losslessly on proportionate portrait pages, without resampling; the PDF is raster artwork, not editable text. Include the original PNGs for reuse.

## Deliver

Save versioned individual images and the prompt set. If requested, include the portrait PDF and a caption in the user's voice. Clearly distinguish generated, approved, packaged and published. Only publish when authorised.
