"""Package approved page images into a lossless portrait PDF without redesign."""
import argparse
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('images', nargs='+', type=Path, help='Image files in page order')
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output already exists; choose a new versioned filename.')
    for path in args.images:
        with Image.open(path) as im:
            im.verify()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(args.output), pageCompression=1)
    pdf.setTitle(args.output.stem.replace('_', ' '))
    for path in args.images:
        with Image.open(path) as im:
            width, height = im.size
        page_width = 595.2756
        page_height = page_width * height / width
        pdf.setPageSize((page_width, page_height))
        pdf.drawImage(ImageReader(str(path)), 0, 0, width=page_width, height=page_height, mask='auto')
        pdf.showPage()
    pdf.save()
    print(f'Saved {len(args.images)} unchanged image pages to {args.output}')

if __name__ == '__main__':
    main()
