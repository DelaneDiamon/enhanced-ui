#!/usr/bin/env python3
"""Copy the mod overlay from mods_source/enhanced_ui/ssl into the buildable ssl/ tree."""

import os
import shutil
import sys

SRC_ROOT = os.path.join('mods_source', 'enhanced_ui', 'ssl')
DEST_ROOT = 'ssl'

if not os.path.isdir(SRC_ROOT):
    print(f"source tree missing: {SRC_ROOT}", file=sys.stderr)
    sys.exit(1)

if os.path.isdir(DEST_ROOT):
    shutil.rmtree(DEST_ROOT)

for base, dirs, files in os.walk(SRC_ROOT):
    rel_base = os.path.relpath(base, SRC_ROOT)
    dest_base = DEST_ROOT if rel_base == '.' else os.path.join(DEST_ROOT, rel_base)
    os.makedirs(dest_base, exist_ok=True)
    for f in files:
        src_path = os.path.join(base, f)
        dest_path = os.path.join(dest_base, f)
        shutil.copy2(src_path, dest_path)

print(f"Copied overlay from {SRC_ROOT} -> {DEST_ROOT}")
