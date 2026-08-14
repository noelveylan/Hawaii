#!/usr/bin/env python3
"""Convert site images (JPG/JPEG/PNG) to WebP for faster page loads.

Originals are kept in place so the site never breaks mid-migration; the
WebP file is written alongside its source (files/cover.jpg -> files/cover.webp).

Usage:
    python convert_images.py                 # convert anything not already done
    python convert_images.py --force         # redo every image
    python convert_images.py --max-width 900 # also downscale wide images
    python convert_images.py --quality 90    # tune quality (default 82)
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is not installed. Run:  python -m pip install Pillow")

SOURCE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
SKIP_DIRECTORIES = {".git", ".vscode", ".claude", "__pycache__", "node_modules"}


def find_images(root: Path):
    """Yield every convertible image under root, skipping tooling directories."""
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() not in SOURCE_EXTENSIONS or not path.is_file():
            continue
        if SKIP_DIRECTORIES.intersection(path.relative_to(root).parts):
            continue
        yield path


def convert(source: Path, quality: int, max_width: int | None, force: bool):
    """Convert one image to WebP. Returns (source_bytes, webp_bytes) or None if skipped."""
    target = source.with_suffix(".webp")

    if target.exists() and not force and target.stat().st_mtime >= source.stat().st_mtime:
        return None

    with Image.open(source) as image:
        # WebP has no CMYK/palette support, and RGBA only matters if there is
        # real transparency worth preserving.
        if image.mode in ("RGBA", "LA") and image.getchannel("A").getextrema()[0] < 255:
            image = image.convert("RGBA")
        else:
            image = image.convert("RGB")

        if max_width and image.width > max_width:
            height = round(image.height * max_width / image.width)
            image = image.resize((max_width, height), Image.LANCZOS)

        # method=6 is the slowest, smallest setting -- fine for a handful of images.
        image.save(target, "WEBP", quality=quality, method=6)

    return source.stat().st_size, target.stat().st_size


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).parent,
                        help="directory to scan (default: this script's folder)")
    parser.add_argument("--quality", type=int, default=82, help="WebP quality, 1-100")
    parser.add_argument("--max-width", type=int, default=None,
                        help="downscale images wider than this many pixels")
    parser.add_argument("--force", action="store_true", help="reconvert existing WebP files")
    args = parser.parse_args()

    root = args.root.resolve()
    images = list(find_images(root))

    if not images:
        print(f"No JPG/PNG images found under {root}")
        return

    total_before = total_after = 0
    converted = skipped = 0

    for source in images:
        relative = source.relative_to(root)
        result = convert(source, args.quality, args.max_width, args.force)

        if result is None:
            print(f"  skip  {relative}  (WebP already up to date)")
            skipped += 1
            continue

        before, after = result
        total_before += before
        total_after += after
        converted += 1
        saving = (1 - after / before) * 100
        print(f"  ok    {relative}  {before / 1024:,.0f} KB -> "
              f"{after / 1024:,.0f} KB  ({saving:.0f}% smaller)")

    print(f"\nConverted {converted} image(s), skipped {skipped}.")
    if converted:
        saving = (1 - total_after / total_before) * 100
        print(f"Total: {total_before / 1024:,.0f} KB -> {total_after / 1024:,.0f} KB "
              f"({saving:.0f}% smaller)")


if __name__ == "__main__":
    main()
