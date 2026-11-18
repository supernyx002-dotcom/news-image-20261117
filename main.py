#!/usr/bin/env python3
"""make.fun news-image entry.

Pure Python 3 stdlib (no third-party imports, no network). The entry image
is held in this repository at assets/entry.png; this program copies it,
byte-for-byte, to $MAKEFUN_OUTPUT_DIR/entry.png (default /output)
and validates the result (dimensions, size, every PNG chunk CRC).

Design (the "simplest program" the bounty page allows): the image is
pre-generated and committed to the repo, so the program is deterministic:
running it twice writes the same bytes both times.
"""

import binascii
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
# The grader leaves MAKEFUN_OUTPUT_DIR unset (then /output); a local run
# sets it, as the kit's starter does. The old build hardcoded /output.
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"),
                   "entry.png")

MAX_BYTES = 1 * 1024 * 1024
MAX_DIM = 1024


def png_size(path):
    """Return (width, height) of a PNG by reading its IHDR chunk."""
    with open(path, "rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    if header[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def validate_png(path):
    """Check the whole PNG: every chunk present with a valid CRC, ending
    in IEND. The gate requires a whole image, not just a valid header."""
    data = open(path, "rb").read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    pos = 8
    seen_iend = False
    while pos < len(data):
        if pos + 8 > len(data):
            raise ValueError("truncated PNG chunk header at %d" % pos)
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8]
        end = pos + 8 + length + 4
        if end > len(data):
            raise ValueError("truncated PNG chunk %r" % ctype)
        crc_stored = struct.unpack(">I", data[end - 4:end])[0]
        crc = binascii.crc32(ctype)
        crc = binascii.crc32(data[pos + 8:end - 4], crc) & 0xFFFFFFFF
        if crc != crc_stored:
            raise ValueError("bad CRC in PNG chunk %r" % ctype)
        if ctype == b"IEND":
            seen_iend = True
            if end != len(data):
                raise ValueError("trailing bytes after IEND")
            break
        pos = end
    if not seen_iend:
        raise ValueError("PNG has no IEND chunk")
    return png_size(path)


def main():
    if not os.path.isfile(SRC):
        print("missing source image: %s" % SRC, file=sys.stderr)
        return 1
    width, height = validate_png(SRC)
    if width > MAX_DIM or height > MAX_DIM:
        print("image too large: %dx%d (max %d)" % (width, height, MAX_DIM),
              file=sys.stderr)
        return 1
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        print("image too big: %d bytes (max %d)" % (size, MAX_BYTES),
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    digest = hashlib.sha256(open(DST, "rb").read()).hexdigest()
    print("wrote %s (%dx%d, %d bytes, sha256 %s)" % (DST, width, height, size, digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
