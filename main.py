#!/usr/bin/env python3
"""news-image-20261117: one image summing up Tuesday 17 November 2026.

A dense newspaper front page — masthead dated TUESDAY 17 NOVEMBER 2026,
lead story on the Kerch Bridge falling, 18 more grid stories and 19
inside lines: 38 verified stories from six continents in total. Every
story was reported on 16–17 November 2026 (Reuters, AP, Al Jazeera,
OHCHR, BBC, CNN and others; see notes.md). All words are rendered in
PIL so the spelling is exact; the two scene photos carry no text.

The program only copies the held image (news-v4.jpg, in this
repository) to /output/entry.png. It is deterministic: two runs write
byte-identical files, with no network and no randomness.

Run locally: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
"""

import hashlib
import os
import sys

ART_FILE = "news-v4.jpg"
ART_SHA256 = "d98e113e4d573f712e59e9efcca91931d884dfefa0616b96d11666363262d76e"
MAX_BYTES = 1048576
JPEG_MAGIC = b"\xff\xd8\xff"


def load_art():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, ART_FILE)
    with open(path, "rb") as handle:
        return handle.read()


def check_art(data):
    if data[:3] != JPEG_MAGIC:
        return "held art is not a JPEG"
    if hashlib.sha256(data).hexdigest() != ART_SHA256:
        return "held art failed its integrity check"
    if len(data) > MAX_BYTES:
        return "held art exceeds the 1 MiB gate"
    return None


def main():
    data = load_art()
    problem = check_art(data)
    if problem is not None:
        sys.exit(problem)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "entry.png")
    with open(out, "wb") as handle:
        handle.write(data)
    with open(out, "rb") as handle:
        written = handle.read()
    if written != data:
        sys.exit("output differs from held art")
    print(f"wrote {out} ({len(data)} bytes, JPEG, "
          f"sha256 {hashlib.sha256(data).hexdigest()[:16]}...)")


if __name__ == "__main__":
    main()
